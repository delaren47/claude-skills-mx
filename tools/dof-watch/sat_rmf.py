"""Second source for dof-watch: the SAT minisitio of the RMF and RGCE.

The SAT posts "versiones anticipadas" of Resolución Miscelánea Fiscal changes
before they reach the DOF, on a static page with no feed. This module parses
that page into dated PDF links and keeps a list of URLs already seen. It has
no network code: dof_watch.fetch_sat_rmf() reads the page. Standard library only.
"""

from __future__ import annotations

import datetime
import json
import re
import unicodedata
import urllib.parse
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path

SAT_RMF_URL = ("https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/"
               "normatividad_rmf_rgce2026.html")
MONTHS = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
          "julio": 7, "agosto": 8, "septiembre": 9, "setiembre": 9, "octubre": 10,
          "noviembre": 11, "diciembre": 12}
DATE_RX = re.compile(r"(\d{1,2})\s+de\s+([a-z]+)\s+(?:de|del)\s+(\d{4})")


@dataclass(frozen=True)
class SatItem:
    title: str
    url: str
    fecha: datetime.date | None
    kind: str  # "anticipada" | "publicada" | "otro"


def _fold(s: str) -> str:
    """Accents removed, case folded, whitespace collapsed."""
    decomposed = unicodedata.normalize("NFKD", s)
    return " ".join("".join(c for c in decomposed if not unicodedata.combining(c))
                    .casefold().split())


def parse_spanish_date(text: str) -> datetime.date | None:
    """First "28 de diciembre de 2025" in text, or None."""
    for day, month, year in DATE_RX.findall(_fold(text)):
        if month in MONTHS:
            try:
                return datetime.date(int(year), MONTHS[month], int(day))
            except ValueError:
                continue
    return None


def infer_kind(text: str) -> str:
    """"anticipada" wins; then "DOF" or "publicada/o" means published."""
    folded = _fold(text)
    if "anticipada" in folded:
        return "anticipada"
    if re.search(r"\bdof\b|\bpublicad[ao]s?\b", folded):
        return "publicada"
    return "otro"


class _PdfLinks(HTMLParser):
    """Collect (href, link text, text after the link up to the next link or item)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.found: list[tuple[str, str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []
        self._tail: list[str] | None = None
        self._pending: tuple[str, str] | None = None

    def _flush(self):
        if self._pending is not None:
            self.found.append((*self._pending, " ".join(self._tail or [])))
        self._pending, self._tail = None, None

    def handle_starttag(self, tag, attrs):
        if tag in ("a", "li"):
            self._flush()
        if tag == "a":
            href = dict(attrs).get("href") or ""
            self._href = href if href.lower().split("?")[0].endswith(".pdf") else None
            self._text = []

    def handle_endtag(self, tag):
        if tag == "a" and self._href is not None:
            self._pending = (self._href, " ".join(" ".join(self._text).split()))
            self._href, self._tail = None, []
        elif tag == "li":
            self._flush()

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)
        elif self._tail is not None:
            self._tail.append(data)

    def close(self):
        super().close()
        self._flush()


def parse_sat_rmf(html: bytes, base: str = SAT_RMF_URL) -> list[SatItem]:
    """One SatItem per distinct PDF link; the date and kind come from the link
    text plus the text that follows it in the same list item."""
    parser = _PdfLinks()
    parser.feed(html.decode("utf-8", "replace"))
    parser.close()
    items: list[SatItem] = []
    seen: set[str] = set()
    for href, title, tail in parser.found:
        url = urllib.parse.urljoin(base, href.strip())
        if url in seen:
            continue
        seen.add(url)
        items.append(SatItem(title, url, parse_spanish_date(tail) or parse_spanish_date(title),
                             infer_kind(f"{title} {tail}")))
    return items


def new_sat_items(items: list[SatItem], seen_path: Path, write: bool = True) -> list[SatItem]:
    """Items whose URL is not in seen_path (a JSON list of URLs). With write,
    their URLs are appended to the file, which is created when missing."""
    path = Path(seen_path)
    seen = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    known = set(seen)
    fresh = [i for i in items if i.url not in known]
    if write and fresh:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(seen + [i.url for i in fresh], ensure_ascii=False, indent=2)
                        + "\n", encoding="utf-8")
    return fresh
