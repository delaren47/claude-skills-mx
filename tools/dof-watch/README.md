# dof-watch

A daily watcher of Mexico's *Diario Oficial de la Federación* (DOF). It reads the day's notes, matches each title against a per-skill watchlist, writes a dated Markdown digest, and opens one GitHub Issue per hit, so a publication that may change a rule in one of the skills in this repo is visible the same day, next to the skill it touches.

No language model runs anywhere in this path. It is two Python files (`dof_watch.py` and the SAT parser `sat_rmf.py`), standard library only (Python 3.11+), plus the `gh` CLI for issues.

## How it works

1. **Read the day.** Two sources, tried in order (`--order sidof,rss` by default):
   - **SIDOF JSON**: `GET https://sidof.segob.gob.mx/dof/sidof/notas/DD-MM-YYYY`. One response holds the morning (`NotasMatutinas`), evening (`NotasVespertinas`) and extraordinary (`NotasExtraordinarias`) editions. Each note has `codNota`, `titulo`, `codOrgaDos` (agency) and `nombreCodOrgaUno` (branch or section). The date must be `DD-MM-YYYY`; `YYYY-MM-DD` returns HTTP 400. Many notes come with `titulo` or `codOrgaDos` set to `null`.
   - **RSS sumario**: `https://dof.gob.mx/sumario.xml`, RSS 2.0 in ISO-8859-1. Item `<title>` is the agency, `<description>` is the note title (CDATA with HTML entities such as `&oacute;`), `<link>` is `https://dof.gob.mx/nota_detalle.php?codigo=<codNota>&fecha=DD/MM/YYYY`. It only carries the current edition, so notes dated on another day are discarded.
   - If every source fails, the run records an **outage**: the digest says `OUTAGE: <reasons>` and the command exits with code 2. A day with zero notes is not an outage; its digest says `notes read: 0`.
2. **Match.** Titles are normalized (accents removed, lower case, whitespace collapsed) and tested against `watchlist.json`:
   - `exclude`: regexes for routine noise (SAT 69-B lists, coordination agreements, tenders, judicial notices and the like). An excluded note produces no hit and is counted in the digest.
   - `skills.<name>.patterns`: regexes against the normalized title. Any match is a hit for that skill.
   - `skills.<name>.agencies`: informational. Agencies are kept for forks and for the reader; they never produce a hit on their own.
3. **Write.** `OUT_DIR/digest/YYYY-MM-DD.md` with a status line (`source: sidof · notes read: 70 · excluded: 4 · hits: 0`) and one table row per hit: skill, edition, agency, title, matched pattern, DOF link. Re-running the same day overwrites the file with the same content.
4. **File issues** (optional). One issue per hit, titled `[dof-hit][<skill>] YYYY-MM-DD · <title> · DOF-<codNota>`, labelled `dof-hit` and `skill:<name>`. Before creating, it searches all issues (open and closed) for `DOF-<codNota>` in the title, so a second run for the same day creates nothing new. The issue body is in Spanish: the digest row, the DOF link, the SIDOF full-text link, and three questions for the reader.

### SAT minisitio (second source)

The SAT posts *versiones anticipadas* of changes to the Resolución Miscelánea Fiscal on its minisitio before they reach the DOF, and that page has no feed. On every run that reached the DOF, dof-watch also reads `https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/normatividad_rmf_rgce2026.html` (static HTML) and takes every link to a PDF: the RMF and its Resoluciones de Modificaciones, their annexes, the anticipadas, the compiled versions, and the RGCE and RFA documents on the same page. Each link keeps its text as the title, the date written next to it ("publicada el 22 de octubre de 2026") and a kind read from that text: `anticipada`, `publicada` (the text says DOF or publicada/publicado) or `otro`.

- **State.** `OUT_DIR/sat_seen.json` is a JSON list of the PDF URLs already reported. A URL not in the list is new: it becomes a `mexico-sat-tax` row in the digest (edition `sat`, pattern `sat-rmf:<kind>`, token `DOF-SAT-<first 10 hex of the SHA-1 of the URL>`) and, with `--create-issues`, an issue deduplicated on that token like any DOF hit. The URLs are appended after the issues are opened. `--dry-run` never writes the file, so a dry run reports the same items every time. The first run on an empty out-dir reports every link on the page (144 on 2026-10-23); seed `sat_seen.json` with a plain run (no `--create-issues`) before the first run that opens issues.
- **Status line.** The digest status line gains `sat: <n> new`, or `sat: outage (<reason>)` when the page cannot be read or has no PDF links. A SAT outage never changes the exit code; the DOF is the primary source. When the DOF itself is out, the SAT is not read and its items wait for the next run.
- **`--no-sat`** skips the SAT page; the status line then has no `sat:` segment.
- **A pointer, not the law.** The minisitio tells you that a change is coming. Its documents, anticipadas in particular, become authoritative only when published in the DOF; that publication arrives through the DOF source above.

## Usage

```sh
# Read today's DOF (Mexico City date), write the digest, print hits as JSON lines.
python3 tools/dof-watch/dof_watch.py run --date today \
  --watchlist tools/dof-watch/watchlist.json --out-dir digests --dry-run

# Same, for a given day, opening issues in a repository.
python3 tools/dof-watch/dof_watch.py run --date 23-10-2026 \
  --watchlist tools/dof-watch/watchlist.json --out-dir digests \
  --create-issues OWNER/REPO

# Rewrite digests/STATS.md: runs, notes read, hits and outages per month,
# plus closed dof-hit issues counted by their outcome:* label.
python3 tools/dof-watch/dof_watch.py stats --out-dir digests --repo OWNER/REPO
```

Exit codes for `run`: `0` success (with or without hits), `2` outage (written to the digest first). `--dry-run` makes no `gh` calls and prints the issue titles it would create to stderr.

Tests: `python3 -m unittest discover -s tools/dof-watch/tests -v`. The fixtures are real responses recorded on 2026-10-23.

## Running on GitHub Actions

`.github/workflows/dof-watch.yml` runs at 14:00 and 23:00 UTC, Monday to Friday, and can be started by hand with two inputs: `date` (`DD-MM-YYYY`, empty means today in Mexico City) and `create_issues` (default `true`).

Before the first scheduled run, start it once by hand with `create_issues=false`. This seed run writes the digest and fills `sat_seen.json`, so the SAT items already published (144 on 2026-10-23) are recorded as seen instead of becoming 144 issues.

The bot writes only to the `digests` branch (`digest/YYYY-MM-DD.md`, `STATS.md`, `sat_seen.json`) and to Issues. It never writes to `main`. An outage (exit code `2`) fails the job after the digest is pushed.

## Forking it for your own skills

1. Edit `watchlist.json`. Keep one entry per skill under `skills`, named like your skill folders. Write `patterns` and `exclude` in **lower case without accents**, because they are matched against the normalized title (`resolucion miscelanea`, not `Resolución Miscelánea`). Give short tokens word boundaries, written `"\\bimss\\b"` inside the JSON string, so they do not match inside longer words.
2. Create the labels once in your repository: `dof-hit`, one `skill:<name>` per skill, and `outcome:no-op`, `outcome:patched`, `outcome:audit`. For example: `gh label create dof-hit -R OWNER/REPO --force`.
3. Close each issue with one `outcome:*` label after reading it; `stats` counts them.

## Source terms

The DOF texts belong to the Secretaría de Gobernación. Its legal notice, quoted verbatim from <https://sidof.segob.gob.mx/avisoLegal> (read on 2026-10-23):

> La reproducción total o parcial del contenido de la información o documentos que se publican en este sitio web sin fines de lucro es permitida siempre y cuando se cite la fuente.

> El acceso a este sitio no implica licencia para la reproducción o distribución de ninguna de sus partes con fines de lucro, y sólo se permitirá con el previo consentimiento por escrito por parte de la Secretaría de Gobernación. Algunos derechos reservados.

The digest and issues reproduce only titles, agencies and links, each with the DOF as source. Check the notice yourself before any commercial use.

## Reading the full text

To read a note's full text inside Claude Code, use [`amatiasdev/dof-mcp`](https://github.com/amatiasdev/dof-mcp), an MCP server and TypeScript client for the DOF (publications and FIX/UDIS/TIIE indicators). dof-watch tells you *which* note to read; dof-mcp lets you read it in the same session.
