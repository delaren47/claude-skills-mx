"""dof-watch: a daily, LLM-free watcher of Mexico's Diario Oficial de la Federación.

Reads the day's DOF from SIDOF (JSON) with the DOF RSS sumario as fallback,
matches each note against a per-skill watchlist, writes a dated digest and
opens one GitHub Issue per hit through the `gh` CLI. A second source, the SAT
minisitio of the RMF (sat_rmf.py), adds its newly listed PDFs as
mexico-sat-tax hits. Standard library only.

    python3 dof_watch.py run --date today --watchlist watchlist.json --out-dir DIR
    python3 dof_watch.py stats --out-dir DIR [--repo OWNER/NAME]
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import html
import json
import re
import subprocess
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from collections.abc import Callable
from dataclasses import asdict, dataclass
from pathlib import Path
from zoneinfo import ZoneInfo

from sat_rmf import SAT_RMF_URL, SatItem, new_sat_items, parse_sat_rmf  # noqa: F401

USER_AGENT = "claude-skills-mx dof-watch (+https://github.com/delaren47/claude-skills-mx)"
SIDOF_URL = "https://sidof.segob.gob.mx/dof/sidof/notas/{fecha}"  # fecha as DD-MM-YYYY
RSS_URL = "https://dof.gob.mx/sumario.xml"
NOTE_URL = "https://dof.gob.mx/nota_detalle.php?codigo={cod}&fecha={fecha}"  # DD/MM/YYYY
SIDOF_TEXT_URL = "https://sidof.segob.gob.mx/dof/sidof/notas/nota/{cod}"
CDMX = ZoneInfo("America/Mexico_City")

SIDOF_EDITIONS = (("NotasMatutinas", "matutina"), ("NotasVespertinas", "vespertina"),
                  ("NotasExtraordinarias", "extraordinaria"))


class SourceError(Exception):
    """A source could not be read; carries the URL and the reason."""

    def __init__(self, url: str, reason: str):
        super().__init__(f"{url}: {reason}")
        self.url = url
        self.reason = reason


@dataclass(frozen=True)
class Note:
    cod_nota: str
    titulo: str
    organismo: str
    edicion: str
    fecha: datetime.date
    url: str


@dataclass(frozen=True)
class SkillRule:
    agencies: list[str]
    patterns: list[re.Pattern]


@dataclass(frozen=True)
class Watchlist:
    skills: dict[str, SkillRule]
    exclude: list[re.Pattern]


@dataclass(frozen=True)
class Hit:
    skill: str
    pattern: str
    note: Note


def note_url(cod_nota: str, fecha: datetime.date) -> str:
    """Public DOF detail page for a note."""
    return NOTE_URL.format(cod=cod_nota, fecha=fecha.strftime("%d/%m/%Y"))


def parse_sidof(payload: dict, fecha: datetime.date) -> list[Note]:
    """Turn a SIDOF /notas/DD-MM-YYYY payload into Notes, all three editions.
    A null titulo becomes ""; a null codOrgaDos falls back to nombreCodOrgaUno."""
    notes: list[Note] = []
    for key, edicion in SIDOF_EDITIONS:
        for raw in payload.get(key) or []:
            cod = str(raw.get("codNota") or "")
            organismo = raw.get("codOrgaDos") or raw.get("nombreCodOrgaUno") or ""
            notes.append(Note(cod, raw.get("titulo") or "", organismo, edicion, fecha,
                              note_url(cod, fecha)))
    return notes


def parse_rss(xml_bytes: bytes) -> list[Note]:
    """Turn the DOF sumario.xml into Notes. The encoding comes from the XML
    declaration (ISO-8859-1); the CDATA text also holds HTML entities
    ("Resoluci&oacute;n"), so it is entity-decoded to keep the accents."""
    root = ET.fromstring(xml_bytes)
    notes: list[Note] = []
    for item in root.iter("item"):
        link = (item.findtext("link") or "").strip()
        query = urllib.parse.parse_qs(urllib.parse.urlparse(link).query)
        cod = (query.get("codigo") or [""])[0]
        fecha = datetime.datetime.strptime((query.get("fecha") or [""])[0], "%d/%m/%Y").date()
        titulo = html.unescape(item.findtext("description") or "").strip()
        organismo = html.unescape(item.findtext("title") or "").strip()
        notes.append(Note(cod, titulo, organismo, "rss", fecha, note_url(cod, fecha)))
    return notes


def fetch(url: str, timeout: int = 30) -> bytes:
    """GET a URL and return the body; any failure becomes SourceError."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            if response.status != 200:
                raise SourceError(url, f"HTTP {response.status}")
            return response.read()
    except urllib.error.HTTPError as exc:
        raise SourceError(url, f"HTTP {exc.code}") from exc
    except (urllib.error.URLError, OSError) as exc:
        raise SourceError(url, str(getattr(exc, "reason", exc))) from exc


def fetch_sidof(fecha: datetime.date) -> list[Note]:
    """Read one day from SIDOF; a non-200 messageCode counts as a failure."""
    url = SIDOF_URL.format(fecha=fecha.strftime("%d-%m-%Y"))
    try:
        payload = json.loads(fetch(url))
    except ValueError as exc:
        raise SourceError(url, f"invalid JSON: {exc}") from exc
    code = payload.get("messageCode") if isinstance(payload, dict) else None
    if code != 200:
        raise SourceError(url, f"messageCode {code}")
    return parse_sidof(payload, fecha)


def fetch_rss() -> list[Note]:
    """Read the current DOF sumario RSS."""
    body = fetch(RSS_URL)  # a SourceError from fetch passes straight through
    try:
        return parse_rss(body)
    except (ET.ParseError, ValueError) as exc:
        raise SourceError(RSS_URL, f"unreadable RSS: {exc}") from exc


def _fetch_rss_dated(fecha: datetime.date) -> list[Note]:
    """RSS notes dated `fecha` only (the sumario is always the current edition);
    none left is an outage, never a quiet zero."""
    notes = [n for n in fetch_rss() if n.fecha == fecha]
    if not notes:
        raise SourceError(RSS_URL, f"no notes dated {fecha:%d-%m-%Y} in sumario.xml")
    return notes


def get_notes(fecha: datetime.date,
              order: tuple[str, ...] = ("sidof", "rss")) -> tuple[list[Note], str]:
    """Try each source in order; return (notes, source name that worked).

    Raises SourceError naming every URL and reason when all sources fail; any
    other exception from a reader is wrapped, so it reads as an outage."""
    readers = {
        "sidof": (SIDOF_URL.format(fecha=f"{fecha:%d-%m-%Y}"), lambda: fetch_sidof(fecha)),
        "rss": (RSS_URL, lambda: _fetch_rss_dated(fecha)),
    }
    errors: list[SourceError] = []
    for name in order:
        if name not in readers:
            raise ValueError(f"unknown source: {name}")
        url, reader = readers[name]
        try:
            return reader(), name
        except SourceError as exc:
            errors.append(exc)
        except Exception as exc:  # noqa: BLE001 - an unexpected failure is still an outage
            errors.append(SourceError(url, repr(exc)))
    raise SourceError(" | ".join(e.url for e in errors),
                      " | ".join(f"{e.url}: {e.reason}" for e in errors))


def fetch_sat_rmf() -> list[SatItem]:
    """Read the SAT minisitio; a page with no PDF links counts as a failure."""
    try:
        items = parse_sat_rmf(fetch(SAT_RMF_URL))
    except SourceError:
        raise
    except Exception as exc:  # noqa: BLE001 - an unreadable page is an outage
        raise SourceError(SAT_RMF_URL, repr(exc)) from exc
    if not items:
        raise SourceError(SAT_RMF_URL, "no PDF links")
    return items


def sat_hit(item: SatItem, run_date: datetime.date) -> Hit:
    """A SAT item as a mexico-sat-tax hit; its code token is DOF-SAT-<sha1[:10]>."""
    cod = "SAT-" + hashlib.sha1(item.url.encode("utf-8")).hexdigest()[:10]
    return Hit("mexico-sat-tax", f"sat-rmf:{item.kind}",
               Note(cod, item.title, "SAT (minisitio RMF)", "sat", item.fecha or run_date,
                    item.url))


def normalize(s: str) -> str:
    """NFKD, drop combining marks, casefold, collapse whitespace."""
    decomposed = unicodedata.normalize("NFKD", s)
    stripped = "".join(c for c in decomposed if not unicodedata.combining(c))
    return " ".join(stripped.casefold().split())


def load_watchlist(path: Path) -> Watchlist:
    """Load watchlist.json; regexes are written against normalize() output."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    skills = {name: SkillRule([normalize(a) for a in rule.get("agencies", [])],
                              [re.compile(p) for p in rule.get("patterns", [])])
              for name, rule in data.get("skills", {}).items()}
    return Watchlist(skills=skills, exclude=[re.compile(p) for p in data.get("exclude", [])])


def match(notes: list[Note], wl: Watchlist) -> tuple[list[Hit], int]:
    """Return (hits, number of excluded notes).

    A note whose normalized titulo matches any exclude regex is dropped.
    Otherwise it yields one Hit per skill whose patterns match the titulo,
    or whose agencies list the organismo and a pattern also matches. The
    agency is a booster, never a gate, and never fires on its own: since the
    agency branch also needs a titulo pattern, the titulo test decides alone.
    Agencies stay in the watchlist for forks and for the digest reader."""
    hits: list[Hit] = []
    excluded = 0
    for note in notes:
        titulo = normalize(note.titulo)
        if any(rx.search(titulo) for rx in wl.exclude):
            excluded += 1
            continue
        for skill, rule in wl.skills.items():
            pattern = next((rx.pattern for rx in rule.patterns if rx.search(titulo)), None)
            if pattern is not None:
                hits.append(Hit(skill=skill, pattern=pattern, note=note))
    return hits, excluded


TABLE_HEAD = ("| skill | edición | organismo | título | patrón | DOF |\n"
              "|---|---|---|---|---|---|")
STATUS_RX = re.compile(
    r"^source: \S+ · notes read: (\d+) · excluded: (\d+) · hits: (\d+)(?: · sat: .*)?$",
    re.MULTILINE
)


def _cell(text: str) -> str:
    """Make text safe for one markdown table cell."""
    return " ".join(text.split()).replace("|", "\\|")


def _row(hit: Hit) -> str:
    n = hit.note
    return (f"| {hit.skill} | {n.edicion} | {_cell(n.organismo)} | {_cell(n.titulo)} "
            f"| `{_cell(hit.pattern)}` | [DOF-{n.cod_nota}]({n.url}) |")


def render_digest(fecha: datetime.date, source: str | None, notes_read: int, excluded: int,
                  hits: list[Hit], outage: str | None, sat_status: str | None = None,
                  sat_hits: list[Hit] = ()) -> str:
    """Markdown digest for one day; the same inputs always give the same text.
    `hits` counts DOF matches only; SAT rows follow them in the same table."""
    if outage is not None:
        return f"# DOF {fecha.isoformat()}\n\nOUTAGE: {' '.join(outage.split())}\n"
    status = (f"source: {source} · notes read: {notes_read} · excluded: {excluded} · "
              f"hits: {len(hits)}" + (f" · {sat_status}" if sat_status else ""))
    lines = [f"# DOF {fecha.isoformat()}", "", status, "", TABLE_HEAD]
    lines += [_row(h) for h in sorted(hits, key=lambda h: (h.skill, h.note.cod_nota))]
    lines += [_row(h) for h in sorted(sat_hits, key=lambda h: h.note.cod_nota)]
    return "\n".join(lines) + "\n"


def run_gh(argv: list[str]) -> str:
    """Run a `gh` command and return its stdout; a failure raises."""
    return subprocess.run(argv, check=True, capture_output=True, text=True).stdout


def issue_title(hit: Hit) -> str:
    n = hit.note
    return f"[dof-hit][{hit.skill}] {n.fecha.isoformat()} · {n.titulo[:80]} · DOF-{n.cod_nota}"


def issue_body(hit: Hit) -> str:
    """Issue body in Spanish: the digest row, both links and the three questions."""
    n = hit.note
    if n.edicion == "sat":
        head = (f"Documento del minisitio del SAT del {n.fecha.isoformat()} que toca el skill "
                f"`{hit.skill}`. Sólo es vigente cuando se publica en el DOF.")
        links = [f"- SAT: {n.url}"]
    else:
        head = f"Publicación del DOF del {n.fecha.isoformat()} que toca el skill `{hit.skill}`."
        links = [f"- DOF: {n.url}",
                 f"- Texto completo (SIDOF): {SIDOF_TEXT_URL.format(cod=n.cod_nota)}"]
    return "\n".join([
        head, "", TABLE_HEAD, _row(hit), "", *links, "",
        "¿Cambia una regla que el skill afirma? ¿Qué sección? "
        "¿Parche ahora o entra a la siguiente auditoría?", "",
        "Cierra con una etiqueta outcome:no-op | outcome:patched | outcome:audit"]) + "\n"


def create_issues(hits: list[Hit], repo: str,
                  run: Callable[[list[str]], str] = run_gh) -> list[str]:
    """Open one issue per hit unless one titled DOF-<cod> exists (open or closed).

    One search per distinct cod_nota; a same-day re-run creates nothing new."""
    created: list[str] = []
    by_cod: dict[str, list[Hit]] = {}
    for hit in hits:
        by_cod.setdefault(hit.note.cod_nota, []).append(hit)
    for cod, group in by_cod.items():
        found = run(["gh", "issue", "list", "-R", repo, "--state", "all",
                     "--search", f"DOF-{cod} in:title", "--json", "number"])
        if json.loads(found or "[]"):
            continue
        for hit in group:
            title = issue_title(hit)
            run(["gh", "issue", "create", "-R", repo, "--title", title, "--body",
                 issue_body(hit), "--label", "dof-hit", "--label", f"skill:{hit.skill}"])
            created.append(title)
    return created


def render_stats(digest_dir: Path, closed_by_outcome: dict[str, int]) -> str:
    """STATS.md: per-month totals read from digest status lines, then outcomes."""
    months: dict[str, list[int]] = {}  # month -> [runs, notes read, hits, outages]
    for path in sorted(Path(digest_dir).glob("????-??-??.md")):
        row = months.setdefault(path.stem[:7], [0, 0, 0, 0])
        row[0] += 1
        text = path.read_text(encoding="utf-8")
        if status := STATUS_RX.search(text):
            row[1] += int(status.group(1))
            row[2] += int(status.group(3))
        elif "\nOUTAGE: " in text:
            row[3] += 1
    lines = ["# dof-watch stats", "", "| month | runs | notes read | hits | outages |",
             "|---|---|---|---|---|"]
    lines += [f"| {m} | {r[0]} | {r[1]} | {r[2]} | {r[3]} |" for m, r in months.items()]
    lines += ["", "## Closed issues by outcome", "", "| outcome | closed |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(closed_by_outcome.items())]
    return "\n".join(lines) + "\n"


def closed_outcomes(repo: str, run: Callable[[list[str]], str] = run_gh) -> dict[str, int]:
    """Count closed dof-hit issues by their outcome:* labels."""
    raw = run(["gh", "issue", "list", "-R", repo, "--label", "dof-hit", "--state", "closed",
               "--json", "labels", "--limit", "1000"])
    issues = json.loads(raw or "[]")
    names = [lb.get("name", "") for issue in issues for lb in issue.get("labels", [])]
    return dict(Counter(n for n in names if n.startswith("outcome:")))


def _parse_date(value: str) -> datetime.date:
    if value == "today":
        return datetime.datetime.now(CDMX).date()
    return datetime.datetime.strptime(value, "%d-%m-%Y").date()


def cmd_run(args: argparse.Namespace) -> int:
    fecha = _parse_date(args.date)
    order = tuple(s.strip() for s in args.order.split(",") if s.strip())
    wl = load_watchlist(Path(args.watchlist))
    try:
        notes, source = get_notes(fecha, order)
        outage = None
    except SourceError as exc:
        notes, source, outage = [], None, exc.reason
    hits, excluded = match(notes, wl)
    seen_path = Path(args.out_dir) / "sat_seen.json"
    sat_new: list[SatItem] = []
    sat_status = None
    if args.sat and outage is None:  # on a DOF outage the SAT waits for the next run
        try:
            sat_new = new_sat_items(fetch_sat_rmf(), seen_path, write=False)
            sat_status = f"sat: {len(sat_new)} new"
        except SourceError as exc:
            sat_status = f"sat: outage ({' '.join(exc.reason.split())})"
            print(sat_status, file=sys.stderr)
    sat_hits = [sat_hit(item, fecha) for item in sat_new]
    digest = Path(args.out_dir) / "digest" / f"{fecha.isoformat()}.md"
    digest.parent.mkdir(parents=True, exist_ok=True)
    text = render_digest(fecha, source, len(notes), excluded, hits, outage, sat_status, sat_hits)
    digest.write_text(text, encoding="utf-8")
    hits = hits + sat_hits
    for hit in hits:
        row = {"skill": hit.skill, "pattern": hit.pattern, **asdict(hit.note)}
        print(json.dumps(row, ensure_ascii=False, default=str))
    if args.dry_run:
        for hit in hits:
            print(f"dry-run, would create: {issue_title(hit)}", file=sys.stderr)
    elif args.create_issues:
        for title in create_issues(hits, args.create_issues, run_gh):
            print(f"created: {title}", file=sys.stderr)
    if sat_new and not args.dry_run:  # recorded only after any issues were opened
        new_sat_items(sat_new, seen_path)
    if outage is not None:
        print(f"OUTAGE: {outage}", file=sys.stderr)
        return 2
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    closed = closed_outcomes(args.repo, run_gh) if args.repo else {}
    (out := Path(args.out_dir)).mkdir(parents=True, exist_ok=True)
    (out / "STATS.md").write_text(render_stats(out / "digest", closed), encoding="utf-8")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="dof_watch.py", description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    run_p = sub.add_parser("run", help="read one DOF day, write its digest, open issues")
    run_p.add_argument("--date", required=True, help="DD-MM-YYYY or 'today' (CDMX)")
    for flag in ("--watchlist", "--out-dir"):
        run_p.add_argument(flag, required=True)
    run_p.add_argument("--order", default="sidof,rss")
    run_p.add_argument("--create-issues", metavar="REPO")
    run_p.add_argument("--dry-run", action="store_true", help="no gh calls, no sat_seen.json")
    run_p.add_argument("--sat", action=argparse.BooleanOptionalAction, default=True,
                       help="also read the SAT minisitio of the RMF (default on)")
    run_p.set_defaults(func=cmd_run)
    stats_p = sub.add_parser("stats", help="rewrite OUT_DIR/STATS.md")
    stats_p.add_argument("--out-dir", required=True)
    stats_p.add_argument("--repo")
    stats_p.set_defaults(func=cmd_stats)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
