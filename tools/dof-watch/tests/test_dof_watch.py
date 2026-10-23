"""Tests for the DOF watcher core: parsers, fallback and matcher."""

import contextlib
import datetime
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import dof_watch  # noqa: E402

FIXTURES = HERE / "fixtures"
SIDOF_JSON = FIXTURES / "sidof_23-10-2026.json"
SUMARIO_XML = FIXTURES / "sumario_2026-10-23.xml"
SAT_HTML = FIXTURES / "sat_rmf_2026-10-23.html"
WATCHLIST = HERE.parent / "watchlist.json"
FECHA = datetime.date(2026, 10, 23)


def synthetic(titulo, organismo=""):
    return dof_watch.Note(
        cod_nota="1",
        titulo=titulo,
        organismo=organismo,
        edicion="matutina",
        fecha=FECHA,
        url="https://dof.gob.mx/nota_detalle.php?codigo=1&fecha=23/10/2026",
    )


class TestDofWatch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(SIDOF_JSON.read_text(encoding="utf-8"))
        cls.rss_bytes = SUMARIO_XML.read_bytes()
        cls.wl = dof_watch.load_watchlist(WATCHLIST)

    def test_parse_sidof_reads_all_editions_and_nulls(self):
        notes = dof_watch.parse_sidof(self.payload, FECHA)
        expected = sum(
            len(self.payload.get(k) or [])
            for k in ("NotasMatutinas", "NotasVespertinas", "NotasExtraordinarias")
        )
        self.assertEqual(len(notes), expected)
        null_cods = {
            str(n["codNota"]) for n in self.payload["NotasMatutinas"] if n.get("titulo") is None
        }
        self.assertTrue(null_cods, "fixture must contain a note with titulo: null")
        for n in notes:
            self.assertIsInstance(n.titulo, str)
            self.assertIsInstance(n.organismo, str)
            if n.cod_nota in null_cods:
                self.assertEqual(n.titulo, "")
        # A null codOrgaDos falls back to nombreCodOrgaUno.
        aviso = next(n for n in self.payload["NotasMatutinas"] if n.get("codOrgaDos") is None)
        parsed = next(n for n in notes if n.cod_nota == str(aviso["codNota"]))
        self.assertEqual(parsed.organismo, aviso["nombreCodOrgaUno"])
        first = next(n for n in notes if n.cod_nota == "5801997")
        self.assertEqual(first.edicion, "matutina")
        self.assertEqual(first.fecha, FECHA)
        self.assertEqual(
            first.url, "https://dof.gob.mx/nota_detalle.php?codigo=5801997&fecha=23/10/2026"
        )
        # A null-titulo note goes through the matcher without crashing.
        hits, _ = dof_watch.match([n for n in notes if n.titulo == ""], self.wl)
        self.assertEqual(hits, [])

    def test_parse_rss_keeps_accents(self):
        notes = dof_watch.parse_rss(self.rss_bytes)
        self.assertTrue(notes)
        self.assertTrue(any("ó" in n.titulo or "á" in n.titulo for n in notes))
        first = next(n for n in notes if n.cod_nota == "5801997")
        self.assertEqual(first.edicion, "rss")
        self.assertEqual(first.fecha, FECHA)
        self.assertEqual(first.organismo, "PODER EJECUTIVO SECRETARIA DE HACIENDA Y CREDITO PUBLICO")
        # The recorded feed carries accents only as HTML entities inside CDATA,
        # so also prove raw ISO-8859-1 bytes decode from the XML declaration.
        raw = (
            '<?xml version="1.0" encoding="ISO-8859-1" ?><rss version="2.0"><channel>'
            "<item><title>PODER EJECUTIVO SECRETARIA DE HACIENDA Y CREDITO PUBLICO</title>"
            "<description>Resolución Miscelánea Fiscal para 2027</description>"
            "<link>https://dof.gob.mx/nota_detalle.php?codigo=42&amp;fecha=24/10/2026</link>"
            "</item></channel></rss>"
        ).encode("iso-8859-1")
        (note,) = dof_watch.parse_rss(raw)
        self.assertEqual(note.titulo, "Resolución Miscelánea Fiscal para 2027")
        self.assertEqual(note.cod_nota, "42")
        self.assertEqual(note.fecha, datetime.date(2026, 10, 24))

    def test_normalize_strips_accents_and_case(self):
        self.assertEqual(dof_watch.normalize("Resolución Miscelánea"), "resolucion miscelanea")
        self.assertEqual(dof_watch.normalize("  ÍNDICE \n nacional  "), "indice nacional")

    def test_match_sat_rule_on_rmf_title(self):
        hits, excluded = dof_watch.match(
            [synthetic("Resolución Miscelánea Fiscal para 2027")], self.wl
        )
        self.assertEqual(excluded, 0)
        self.assertEqual([h.skill for h in hits], ["mexico-sat-tax"])

    def test_match_excludes_69b_oficio(self):
        notes = dof_watch.parse_sidof(self.payload, FECHA)
        oficio = next(n for n in notes if n.cod_nota == "5801997")
        self.assertIn("listado de contribuyentes", oficio.titulo)
        hits, excluded = dof_watch.match([oficio], self.wl)
        self.assertEqual(excluded, 1)
        self.assertEqual(hits, [])

    def test_agency_alone_never_fires(self):
        note = synthetic("Convenio de colaboración", "INSTITUTO MEXICANO DEL SEGURO SOCIAL")
        hits, excluded = dof_watch.match([note], self.wl)
        self.assertEqual(excluded, 0)
        self.assertEqual(hits, [])

    def test_match_imss_modalidad_40_agreement(self):
        note = synthetic(
            "ACUERDO por el que se aprueban los lineamientos para la continuación "
            "voluntaria en el régimen obligatorio"
        )
        hits, _ = dof_watch.match([note], self.wl)
        self.assertEqual([h.skill for h in hits], ["mexico-imss"])

    def test_get_notes_falls_back_to_rss(self):
        def fake_fetch(url, timeout=30):
            if "sidof.segob.gob.mx" in url:
                raise dof_watch.SourceError(url, "HTTP 503")
            return self.rss_bytes

        with mock.patch.object(dof_watch, "fetch", side_effect=fake_fetch):
            notes, source = dof_watch.get_notes(FECHA)
        self.assertEqual(source, "rss")
        self.assertEqual(len(notes), len(dof_watch.parse_rss(self.rss_bytes)))

    def test_rss_fallback_rejects_other_date(self):
        def fake_fetch(url, timeout=30):
            if "sidof.segob.gob.mx" in url:
                raise dof_watch.SourceError(url, "HTTP 503")
            return self.rss_bytes  # dated 23-10-2026

        with mock.patch.object(dof_watch, "fetch", side_effect=fake_fetch):
            with self.assertRaises(dof_watch.SourceError) as ctx:
                dof_watch.get_notes(datetime.date(2026, 10, 22), order=("sidof", "rss"))
        message = str(ctx.exception)
        self.assertIn("https://sidof.segob.gob.mx/dof/sidof/notas/22-10-2026", message)
        self.assertIn("https://dof.gob.mx/sumario.xml", message)
        self.assertIn("no notes dated 22-10-2026", message)

    def test_get_notes_raises_when_all_fail(self):
        def fake_fetch(url, timeout=30):
            if "sidof.segob.gob.mx" in url:
                raise OSError("connection reset")  # not a SourceError: must be wrapped
            raise dof_watch.SourceError(url, "timed out")

        with mock.patch.object(dof_watch, "fetch", side_effect=fake_fetch):
            with self.assertRaises(dof_watch.SourceError) as ctx:
                dof_watch.get_notes(FECHA)
        message = str(ctx.exception)
        self.assertIn("https://sidof.segob.gob.mx/dof/sidof/notas/23-10-2026", message)
        self.assertIn("https://dof.gob.mx/sumario.xml", message)
        self.assertIn("OSError", message)

    # --- Task 5: digest, issues, stats, CLI ---------------------------------

    def run_cli(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = dof_watch.main(list(argv))
        return code, out.getvalue(), err.getvalue()

    def test_digest_has_status_line_and_hit_rows(self):
        hits = [
            dof_watch.Hit("mexico-sat-tax", "resolucion miscelanea", synthetic("RMF 2027")),
            dof_watch.Hit("mexico-imss", "seguro social", synthetic("Ley del Seguro Social")),
        ]
        text = dof_watch.render_digest(FECHA, "sidof", 121, 97, hits, None)
        lines = text.splitlines()
        self.assertEqual(lines[0], "# DOF 2026-10-23")
        self.assertIn("source: sidof · notes read: 121 · excluded: 97 · hits: 2", lines)
        self.assertIn("| skill | edición | organismo | título | patrón | DOF |", lines)
        rows = [l for l in lines if l.startswith("| mexico-")]
        self.assertEqual(len(rows), 2)
        self.assertTrue(rows[0].startswith("| mexico-imss |"))  # sorted by skill
        self.assertIn("(https://dof.gob.mx/nota_detalle.php?codigo=1&fecha=23/10/2026)", rows[1])

    def test_outage_digest_says_outage_and_cli_exits_2(self):
        def fake_fetch(url, timeout=30):
            raise dof_watch.SourceError(url, "HTTP 503")

        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(
            dof_watch, "fetch", side_effect=fake_fetch
        ):
            code, _, _ = self.run_cli(
                "run", "--date", "23-10-2026", "--watchlist", str(WATCHLIST), "--out-dir", tmp
            )
            text = (Path(tmp) / "digest" / "2026-10-23.md").read_text(encoding="utf-8")
        self.assertEqual(code, 2)
        self.assertIn("OUTAGE: ", text)
        self.assertIn("sidof.segob.gob.mx", text)
        self.assertIn("sumario.xml", text)

    def test_zero_notes_is_not_outage(self):
        empty = {"messageCode": 200, "NotasMatutinas": [], "NotasVespertinas": [],
                 "NotasExtraordinarias": []}
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(
            dof_watch, "fetch", return_value=json.dumps(empty).encode()
        ):
            code, out, _ = self.run_cli(
                "run", "--date", "23-10-2026", "--watchlist", str(WATCHLIST), "--out-dir", tmp
            )
            text = (Path(tmp) / "digest" / "2026-10-23.md").read_text(encoding="utf-8")
        self.assertEqual(code, 0)
        self.assertEqual(out, "")
        self.assertIn("source: sidof · notes read: 0 · excluded: 0 · hits: 0", text)
        self.assertNotIn("OUTAGE", text)

    def test_issue_title_contains_dof_code_token(self):
        note = dof_watch.Note("5801708", "Resolución Miscelánea Fiscal para 2027 " * 5,
                              "SHCP", "matutina", FECHA, dof_watch.note_url("5801708", FECHA))
        hit = dof_watch.Hit("mexico-sat-tax", "resolucion miscelanea", note)
        title = dof_watch.issue_title(hit)
        self.assertTrue(title.startswith("[dof-hit][mexico-sat-tax] 2026-10-23 · "))
        self.assertTrue(title.endswith("DOF-5801708"))
        self.assertIn(note.titulo[:80] + " · ", title)
        body = dof_watch.issue_body(hit)
        self.assertIn("https://sidof.segob.gob.mx/dof/sidof/notas/nota/5801708", body)
        self.assertIn("¿Cambia una regla que el skill afirma?", body)
        self.assertIn("outcome:no-op | outcome:patched | outcome:audit", body)

    def test_create_issues_dedupes_on_existing_token(self):
        calls = []

        def fake_run(argv):
            calls.append(argv)
            return '[{"number":7}]' if argv[:3] == ["gh", "issue", "list"] else ""

        hits = [
            dof_watch.Hit("mexico-sat-tax", "codigo fiscal", synthetic("Código Fiscal")),
            dof_watch.Hit("mexico-imss", "seguro social", synthetic("Código Fiscal")),
        ]
        created = dof_watch.create_issues(hits, "owner/repo", fake_run)
        self.assertEqual(created, [])
        self.assertEqual(len(calls), 1)  # one search per distinct cod_nota
        self.assertIn("DOF-1 in:title", calls[0])
        self.assertIn("all", calls[0])

    def test_rerun_same_day_overwrites_digest_and_creates_nothing_new(self):
        payload = {"messageCode": 200, "NotasVespertinas": [], "NotasExtraordinarias": [],
                   "NotasMatutinas": [{"codNota": 5801708,
                                       "titulo": "Resolución Miscelánea Fiscal para 2027",
                                       "codOrgaDos": "SECRETARIA DE HACIENDA Y CREDITO PUBLICO",
                                       "nombreCodOrgaUno": "PODER EJECUTIVO"}]}
        titles = []

        def fake_gh(argv):
            if argv[:3] == ["gh", "issue", "list"]:
                token = argv[argv.index("--search") + 1].split()[0]
                return json.dumps([{"number": 1} for t in titles if t.endswith(token)])
            titles.append(argv[argv.index("--title") + 1])
            return "https://github.com/owner/repo/issues/1\n"

        argv = ("run", "--date", "23-10-2026", "--watchlist", str(WATCHLIST),
                "--create-issues", "owner/repo")
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(
            dof_watch, "fetch", return_value=json.dumps(payload).encode()
        ), mock.patch.object(dof_watch, "run_gh", side_effect=fake_gh):
            digest = Path(tmp) / "digest" / "2026-10-23.md"
            code1, out1, _ = self.run_cli(*argv, "--out-dir", tmp)
            first = digest.read_text(encoding="utf-8")
            digest.write_text("stale", encoding="utf-8")
            code2, out2, _ = self.run_cli(*argv, "--out-dir", tmp)
            second = digest.read_text(encoding="utf-8")
            files = list((Path(tmp) / "digest").iterdir())
        self.assertEqual((code1, code2), (0, 0))
        self.assertEqual(len(titles), 1)
        self.assertTrue(titles[0].endswith("DOF-5801708"))
        self.assertEqual(first, second)
        self.assertEqual(len(files), 1)
        self.assertEqual(json.loads(out1.splitlines()[0])["skill"], "mexico-sat-tax")
        self.assertEqual(out1, out2)

    def test_stats_counts_runs_hits_outages_per_month(self):
        hit = dof_watch.Hit("mexico-sat-tax", "codigo fiscal", synthetic("Código Fiscal"))
        days = [
            (datetime.date(2026, 9, 30), "sidof", 50, 10, [hit], None),
            (datetime.date(2026, 10, 1), "sidof", 70, 4, [hit, hit], None),
            (datetime.date(2026, 10, 2), None, 0, 0, [], "sidof: HTTP 503 | rss: timed out"),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            digest_dir = Path(tmp) / "digest"
            digest_dir.mkdir()
            for fecha, *rest in days:
                (digest_dir / f"{fecha.isoformat()}.md").write_text(
                    dof_watch.render_digest(fecha, *rest), encoding="utf-8")
            text = dof_watch.render_stats(digest_dir, {"outcome:no-op": 2, "outcome:patched": 1})
        lines = text.splitlines()
        self.assertIn("| 2026-09 | 1 | 50 | 1 | 0 |", lines)
        self.assertIn("| 2026-10 | 2 | 70 | 2 | 1 |", lines)
        self.assertIn("| outcome:no-op | 2 |", lines)
        self.assertIn("| outcome:patched | 1 |", lines)


    # --- SAT minisitio (second source) ---------------------------------------

    def sat_run(self, tmp, sat_response, *extra):
        """Run the CLI with an empty SIDOF day and a scripted SAT response."""
        empty = {"messageCode": 200, "NotasMatutinas": [], "NotasVespertinas": [],
                 "NotasExtraordinarias": []}

        def fake_fetch(url, timeout=30):
            if "sat.gob.mx" in url:
                if isinstance(sat_response, Exception):
                    raise sat_response
                return sat_response
            return json.dumps(empty).encode()

        with mock.patch.object(dof_watch, "fetch", side_effect=fake_fetch):
            result = self.run_cli("run", "--date", "23-10-2026", "--watchlist", str(WATCHLIST),
                                  "--out-dir", tmp, *extra)
        return result, (Path(tmp) / "digest" / "2026-10-23.md").read_text(encoding="utf-8")

    def test_parse_sat_rmf_fixture_has_items_with_kinds(self):
        items = dof_watch.parse_sat_rmf(SAT_HTML.read_bytes())
        self.assertGreater(len(items), 100)
        self.assertEqual(len({i.url for i in items}), len(items))
        kinds = {i.kind for i in items}
        self.assertTrue({"anticipada", "publicada", "otro"} <= kinds, kinds)
        base = "https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/"
        for i in items:
            self.assertTrue(i.url.startswith(base), i.url)
            self.assertTrue(i.url.lower().endswith(".pdf"), i.url)
            self.assertTrue(i.title, i.url)
        latest = next(i for i in items if i.url.endswith(
            "4aRM_RMF2026-Tercera_version_anticipada_22102026.pdf"))
        self.assertEqual(latest.kind, "anticipada")
        self.assertEqual(latest.title, "3a Versión Anticipada 4a RMRMF 2026")
        rmf = next(i for i in items if i.url.endswith("RMF_2026-DOF-28122025.pdf"))
        self.assertEqual(rmf.kind, "publicada")
        self.assertEqual(rmf.title, "Resolución Miscelánea Fiscal para 2026")
        self.assertEqual(dof_watch.SatItem("Anexo 1", "u", None, "otro").kind, "otro")

    def test_parse_sat_rmf_dates_parsed(self):
        items = {i.url.rsplit("/", 1)[1]: i for i in dof_watch.parse_sat_rmf(SAT_HTML.read_bytes())}
        self.assertEqual(items["RMF_2026-DOF-28122025.pdf"].fecha, datetime.date(2025, 12, 28))
        self.assertEqual(items["3aRM_RMF2026_DOF_02102026.pdf"].fecha, datetime.date(2026, 10, 2))
        self.assertEqual(items["4aRM_RMF2026-Tercera_version_anticipada_22102026.pdf"].fecha,
                         datetime.date(2026, 10, 22))
        # "6 de agosto" (one digit) and a date with no "publicado el" before it.
        self.assertEqual(items["2aRM_RMF2026-Quinta_version_anticipada_06082026.pdf"].fecha,
                         datetime.date(2026, 8, 6))
        self.assertEqual(items["Anexo1delasRGCEpara2026.pdf"].fecha, datetime.date(2026, 1, 8))
        dated = [i for i in items.values() if i.fecha is not None]
        self.assertGreaterEqual(len(dated), len(items) - 2)
        snippet = (b'<ul><li><a href="documentos2026/x.pdf">Sin fecha</a></li>'
                   b'<li><a href="/y.pdf">Otra</a> (publicada el 31 de febrero de 2026)</li></ul>')
        parsed = dof_watch.parse_sat_rmf(snippet)
        self.assertEqual([i.fecha for i in parsed], [None, None])
        self.assertEqual(parsed[1].url, "https://www.sat.gob.mx/y.pdf")

    def test_new_sat_items_dedupes_with_seen_file(self):
        a = dof_watch.SatItem("A", "https://sat.example/a.pdf", FECHA, "anticipada")
        b = dof_watch.SatItem("B", "https://sat.example/b.pdf", None, "otro")
        with tempfile.TemporaryDirectory() as tmp:
            seen = Path(tmp) / "sat_seen.json"
            self.assertEqual(dof_watch.new_sat_items([a], seen, write=False), [a])
            self.assertFalse(seen.exists())  # dry-run writes nothing
            self.assertEqual(dof_watch.new_sat_items([a], seen), [a])
            self.assertEqual(json.loads(seen.read_text(encoding="utf-8")), [a.url])
            self.assertEqual(dof_watch.new_sat_items([a, b], seen), [b])
            self.assertEqual(dof_watch.new_sat_items([a, b], seen), [])
            self.assertEqual(json.loads(seen.read_text(encoding="utf-8")), [a.url, b.url])

    def test_sat_outage_does_not_fail_run(self):
        for response, reason in ((dof_watch.SourceError(dof_watch.SAT_RMF_URL, "HTTP 503"),
                                  "HTTP 503"),
                                 (b"<html><body>mantenimiento</body></html>", "no PDF links")):
            with tempfile.TemporaryDirectory() as tmp:
                (code, out, err), text = self.sat_run(tmp, response)
                self.assertFalse((Path(tmp) / "sat_seen.json").exists())
            self.assertEqual(code, 0)
            self.assertEqual(out, "")
            self.assertNotIn("OUTAGE", text)
            self.assertIn("source: sidof · notes read: 0 · excluded: 0 · hits: 0 · "
                          f"sat: outage ({reason})", text)
            self.assertIn(f"sat: outage ({reason})", err)
        with tempfile.TemporaryDirectory() as tmp:
            (code, _, _), text = self.sat_run(tmp, OSError("boom"), "--no-sat")
        self.assertEqual(code, 0)
        self.assertNotIn("sat:", text)
        # The stats reader still parses a status line that carries the sat segment.
        self.assertIsNotNone(dof_watch.STATUS_RX.search(
            "source: sidof · notes read: 3 · excluded: 1 · hits: 0 · sat: 2 new"))

    def test_sat_hit_appears_in_digest_and_issue_title(self):
        fixture = SAT_HTML.read_bytes()
        n_items = len(dof_watch.parse_sat_rmf(fixture))
        with tempfile.TemporaryDirectory() as tmp:
            (code, out, err), text = self.sat_run(tmp, fixture, "--dry-run")
            self.assertFalse((Path(tmp) / "sat_seen.json").exists())
            (_, out2, _), text2 = self.sat_run(tmp, fixture, "--dry-run")
        self.assertEqual(code, 0)
        self.assertIn(f"hits: 0 · sat: {n_items} new", text)
        self.assertEqual(text, text2)  # dry-run kept no state
        self.assertEqual(len(out.splitlines()), n_items)
        url = ("https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/"
               "anticipadas/4aRM_RMF2026-Tercera_version_anticipada_22102026.pdf")
        token = "DOF-SAT-" + hashlib.sha1(url.encode()).hexdigest()[:10]
        row = next(l for l in text.splitlines() if token in l)
        self.assertTrue(row.startswith("| mexico-sat-tax | sat | SAT (minisitio RMF) | "
                                       "3a Versión Anticipada 4a RMRMF 2026 | "
                                       "`sat-rmf:anticipada` |"), row)
        self.assertIn(f"[{token}]({url})", row)
        self.assertIn(f"dry-run, would create: [dof-hit][mexico-sat-tax] 2026-10-22 · "
                      f"3a Versión Anticipada 4a RMRMF 2026 · {token}", err)
        hit = dof_watch.sat_hit(dof_watch.SatItem("Sin fecha", url, None, "otro"), FECHA)
        self.assertEqual(dof_watch.issue_title(hit),
                         f"[dof-hit][mexico-sat-tax] 2026-10-23 · Sin fecha · {token}")
        self.assertIn(url, dof_watch.issue_body(hit))
        self.assertNotIn("sidof", dof_watch.issue_body(hit))
        # A real run records the URLs, so the next run reports zero new items.
        titles = []

        def fake_gh(argv):
            if argv[:3] == ["gh", "issue", "list"]:
                return "[]"
            titles.append(argv[argv.index("--title") + 1])
            return ""

        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(
            dof_watch, "run_gh", side_effect=fake_gh
        ):
            self.sat_run(tmp, fixture, "--create-issues", "owner/repo")
            seen = json.loads((Path(tmp) / "sat_seen.json").read_text(encoding="utf-8"))
            (code3, _, _), text3 = self.sat_run(tmp, fixture, "--create-issues", "owner/repo")
        self.assertEqual(len(titles), n_items)
        self.assertEqual(len(seen), n_items)
        self.assertEqual(code3, 0)
        self.assertIn("hits: 0 · sat: 0 new", text3)


if __name__ == "__main__":
    unittest.main()
