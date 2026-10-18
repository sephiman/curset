# SPDX-License-Identifier: AGPL-3.0-only
"""Citations (delta C): the grammar, the anchors, the source links, the served sources and the checks.

Each course that keeps `sources/normativa.yaml` has a golden, `citations.<locale>.txt`: every citation the
lessons carry, in reading order, with its anchors and where it opens. Reviewed once, then frozen;
regenerate with `UPDATE_CITATIONS=1 uv run pytest tests/test_citations.py` and read the diff. The web
reads the same file to prove it marks every one of them (`lib/citations/annotate.test.ts`).
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

import pytest
import yaml
from httpx import AsyncClient

from conftest import FIXTURE_CONTENT
from pipeline_courses import course_dir, pipeline_courses
from tradeschool.citations.course import CourseCitations
from tradeschool.citations.grammar import parentheticals, parse_segment
from tradeschool.citations.lesson import scan_lesson
from tradeschool.citations.norms import NormIndex
from tradeschool.citations.sources import INDEX_FILE, SourceIndex, index_pdf_pages, sha256
from tradeschool.content.esquema import parse_esquemas
from tradeschool.content.registry import ContentError, CourseRegistry, load_registry

OPOS = "/api/courses/fixture-oposiciones"
CRYPTO = "/api/courses/crypto-futures"
FIXTURE = FIXTURE_CONTENT / "fixture-oposiciones"
UPDATE = os.environ.get("UPDATE_CITATIONS") == "1"
PASSWORD = "correcthorse"


def _linked_courses() -> list[CourseRegistry]:
    return [course for course in pipeline_courses() if course.citations.links]


# --- the grammar -----------------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("written", "units", "norm"),
    [
        ("art. 67 CE", ["art-67"], "CE"),
        ("art. 4.1.b) LPAC", ["art-4"], "LPAC"),
        ("art. 14.2.d)\ny e) LPAC", ["art-14"], "LPAC"),
        ("arts. 74.2, 145.2 y 158.2 CE", ["art-74", "art-145", "art-158"], "CE"),
        ("arts. 14\u201338 CE", ["art-14", "art-38"], "CE"),
        ("art. 610 bis.2 LOPJ", ["art-610-bis"], "LOPJ"),
        ("art. 12.2 bis Ley 50/1997", ["art-12"], "Ley 50/1997"),
        ("art. 148.1.8.ª CE", ["art-148"], "CE"),
        ("art. 44.2 y art. 33.1 LOTC", ["art-44", "art-33"], "LOTC"),
        ("art. 23.Uno.B Ley 31/2022", ["art-23"], "Ley 31/2022"),
        ("art. 205.1.a) y disposición transitoria séptima LGSS", ["art-205", "dt-septima"], "LGSS"),
        ("disposición adicional cuarta Ley 19/2013", ["da-cuarta"], "Ley 19/2013"),
        ("disposición derogatoria única b) y f) TREBEP", ["dd-unica"], "TREBEP"),
        ("disposición final CE", ["df"], "CE"),
        ("anexo I Orden HAC/557/2026", ["anexo-i"], "Orden HAC/557/2026"),
        ("apartado 2.4.a) Resolución de 14-04-2026", ["apartado-2"], "Resolución de 14-04-2026"),
        ("preámbulo CE", ["preambulo"], "CE"),
        ("arts. 137\u2013139", ["art-137", "art-139"], ""),
        ("art. 21.C) RD 1009/2023", ["art-21"], "RD 1009/2023"),
        ("art. 23.Uno.B) Ley 31/2022", ["art-23"], "Ley 31/2022"),
        ("arts. 23.2 y 24.1\u20132 Ley 19/2013", ["art-23", "art-24"], "Ley 19/2013"),
        ("arts. 30.2\u20133 y 68.1 LPAC", ["art-30", "art-68"], "LPAC"),
        ("arts. 24.1\u201324.2 Ley 19/2013", ["art-24"], "Ley 19/2013"),
        ("arts. 23.2, 24.1\u20132 y 25 Ley 19/2013", ["art-23", "art-24", "art-25"], "Ley 19/2013"),
        ("arts. 12.1\u201313.2 LPAC", ["art-12", "art-13"], "LPAC"),
        ("regla 34 IOC", ["regla-34"], "IOC"),
        ("regla 34.II.a.1 IOC", ["regla-34"], "IOC"),
        ("regla 42.2.b) IOC", ["regla-42"], "IOC"),
        ("regla 59 bis IOC", ["regla-59-bis"], "IOC"),
        ("regla 77.1\u20132 IOC", ["regla-77"], "IOC"),
        (
            "apartado sexto.1 Orden de documentos contables",
            ["apartado-sexto"],
            "Orden de documentos contables",
        ),
        (
            "apartado s\u00e9ptimo.1.1\u20131.2 Orden PRE/1576/2002",
            ["apartado-septimo"],
            "Orden PRE/1576/2002",
        ),
        ("apartado d\u00e9cimo Orden PRE/1576/2002", ["apartado-decimo"], "Orden PRE/1576/2002"),
        (
            "nota 34 anexo I Orden de documentos contables",
            ["anexo-i-nota-34"],
            "Orden de documentos contables",
        ),
        (
            "anexo I, nota 34.II.a.1, Orden de documentos contables",
            ["anexo-i-nota-34"],
            ", Orden de documentos contables",
        ),
    ],
)
def test_a_segment_cites_the_units_it_names_as_written(written: str, units: list[str], norm: str) -> None:
    segment = parse_segment(written)
    assert segment is not None
    assert [unit.slug for unit in segment.units] == units
    assert segment.norm_text == norm


def test_a_segment_without_a_lead_is_prose() -> None:
    assert parse_segment("m05-l05") is None
    assert parse_segment("véase el tema anterior") is None
    assert parse_segment("regla general") is None
    assert parse_segment("nota del BOE al art. 29 Ley 30/1984") is None


@pytest.mark.parametrize(
    ("text", "inner"),
    [
        (
            "(art. 21.C) Real Decreto 1009/2023, de 5 de diciembre).",
            "art. 21.C) Real Decreto 1009/2023, de 5 de diciembre",
        ),
        ("(art. 23.Uno.B) Ley 31/2022) y más", "art. 23.Uno.B) Ley 31/2022"),
        ("(art. 23.Uno.B)\u2013D) Ley 31/2022).", "art. 23.Uno.B)\u2013D) Ley 31/2022"),
        ("(art. 159.4.f) LCSP).", "art. 159.4.f) LCSP"),
        ("(art. 8.1.a)\u2013b) RDL 4/2000). Estos", "art. 8.1.a)\u2013b) RDL 4/2000"),
        # A capital after a space is a word, not a paragraph letter: «(… título I) Siguiente».
        ("(art. 2 TUE, título I) Siguiente frase.", "art. 2 TUE, título I"),
    ],
)
def test_a_paragraph_letter_and_its_paren_do_not_close_the_citation(text: str, inner: str) -> None:
    assert [paren.inner for paren in parentheticals(text)] == [inner]


def test_a_list_row_citation_may_end_in_a_letter_paragraph() -> None:
    body = (
        ':::esquema{kind=plazos title="Plazos"}\n'
        "1. Garantía definitiva — siete días hábiles (art. 159.4.f) LCSP)\n"
        "2. Adjudicación (anticipada) — quince días (art. 23.Uno.B) Ley 31/2022)\n"
        ":::\n"
    )
    rows = parse_esquemas(body)[0].rows
    assert [(row.fields, row.citation) for row in rows] == [
        (("Garantía definitiva", "siete días hábiles"), "art. 159.4.f) LCSP"),
        (("Adjudicación (anticipada)", "quince días"), "art. 23.Uno.B) Ley 31/2022"),
    ]


def test_rule_headings_ordinal_apartados_and_annex_notes_are_indexed_by_page() -> None:
    pages = [
        "Primero.  Ámbito de aplicación.\nRegla 34.  Establecimiento del sistema.",
        "Sexto.  Delimitación.\nRegla 59 bis.  Pagos.\nANEXO I\n1. Oficina: el código.\n2. Código: x.",
        "100. «Retención de crédito».\n3. Esta casilla se dejará en blanco.\n4. Signo: positivo.",
        "34. Fecha del gasto: la de realización.\n1. Certificaciones: el día.\nANEXO II\n1. Otra nota.",
    ]
    units = index_pdf_pages(pages)
    assert {
        key: units[key] for key in ("regla-34", "regla-59-bis", "apartado-primero", "apartado-sexto")
    } == {
        "regla-34": 1,
        "regla-59-bis": 2,
        "apartado-primero": 1,
        "apartado-sexto": 2,
    }
    notes = {key: page for key, page in units.items() if "-nota-" in key}
    # Notes run 1, 2, 3, 4 … in order; a gap (5 to 33 here) stops the run, and each annex starts its own.
    assert notes == {
        "anexo-i-nota-1": 2,
        "anexo-i-nota-2": 2,
        "anexo-i-nota-3": 3,
        "anexo-i-nota-4": 3,
        "anexo-ii-nota-1": 4,
    }


def test_a_rule_of_a_non_article_source_opens_its_page_or_else_the_file(tmp_path: Path) -> None:
    normativa = tmp_path / "normativa.yaml"
    normativa.write_text(
        yaml.safe_dump(
            [
                {
                    "short": "Orden de 1 de febrero de 1996 (Instrucción de operatoria contable)",
                    "aliases": ["IOC"],
                    "title": "Orden de 1 de febrero de 1996 por la que se aprueba la Instrucción.",
                    "boe_id": "BOE-A-1996-2627",
                    "file": "sources/normativa/ioc.pdf",
                },
                {
                    "short": "Orden de 1 de febrero de 1996 (documentos contables)",
                    "aliases": ["Orden de documentos contables"],
                    "title": "Orden de 1 de febrero de 1996 por la que se aprueban los documentos contables.",
                    "boe_id": "BOE-A-1996-2749",
                    "file": "sources/normativa/documentos.pdf",
                },
            ],
            allow_unicode=True,
        ),
        encoding="utf-8",
    )
    lesson = (
        "El ACF se establece por regla (regla 34.II.a.1 IOC). El documento es un ADOK "
        "(apartado sexto.1 Orden de documentos contables). La fecha del gasto "
        "(nota 34 anexo I Orden de documentos contables) y su signo (regla 35 IOC)."
    )
    norms = NormIndex.load(normativa, [lesson])
    sources = SourceIndex(
        {
            "sources/normativa/ioc.pdf": {"units": {"regla-34": 16}},
            "sources/normativa/documentos.pdf": {"units": {"apartado-sexto": 3, "anexo-i-nota-34": 15}},
        }
    )
    citations = CourseCitations("c", norms, sources, {"es": {"l": scan_lesson("l", lesson, norms)}})
    shipped = [(item["text"], item["ids"], item["href"]) for item in citations.lesson_payload("l", "es")]
    assert shipped == [
        (
            "regla 34.II.a.1 IOC",
            ["boe-a-1996-2627-regla-34"],
            "/api/courses/c/sources/normativa/ioc.pdf#page=16",
        ),
        (
            "apartado sexto.1 Orden de documentos contables",
            ["boe-a-1996-2749-apartado-sexto"],
            "/api/courses/c/sources/normativa/documentos.pdf#page=3",
        ),
        (
            "nota 34 anexo I Orden de documentos contables",
            ["boe-a-1996-2749-anexo-i-nota-34"],
            "/api/courses/c/sources/normativa/documentos.pdf#page=15",
        ),
        # Not in the page index: the rule still names its norm and opens the file.
        ("regla 35 IOC", ["boe-a-1996-2627-regla-35"], "/api/courses/c/sources/normativa/ioc.pdf"),
    ]


# --- the golden ------------------------------------------------------------------------------------


def _target(course: CourseRegistry, href: object) -> str:
    prefix = f"/api/courses/{course.slug}/"
    return str(href).removeprefix(prefix) if href else "-"


def _report(course: CourseRegistry, locale: str) -> str:
    rows: list[str] = []
    prose = sources = esquema = normativa = unresolved = 0
    anchors: set[str] = set()
    for _module, lesson in course.manifest.iter_lessons():
        found = course.citations.lesson(lesson.id, locale)
        if found is None:
            continue
        payload = course.citations.lesson_payload(lesson.id, locale)
        for item, shipped in zip(found.items, payload, strict=True):
            if item.section == "prose":
                prose += 1
                sources += item.source_file is not None
                anchors.update(item.anchors)
            esquema += item.section == "esquema"
            normativa += item.section == "normativa"
            named = item.norm.slug if item.norm else (f"?{item.norm_slug}" if item.norm_slug else "-")
            if item.source_file is None and item.norm is None:
                unresolved += 1
            rows.append(
                "\t".join(
                    [
                        lesson.key,
                        item.section,
                        ",".join(item.anchors) or "-",
                        ",".join(shipped["ids"]) or "-",  # type: ignore[arg-type]
                        named,
                        _target(course, shipped["href"]),
                        item.text,
                    ]
                )
            )
    header = [
        f"# citations — {locale}",
        "#",
        "# Generated by backend/tests/test_citations.py from content/. Reviewed by hand, then frozen: a",
        "# content change that moves, adds or drops a citation shows up here as a diff. Do not hand-edit —",
        "# fix the lesson (or normativa.yaml) and regenerate with UPDATE_CITATIONS=1.",
        "#",
        f"# {prose} prose citations ({sources} of them a source file) · {len(anchors)} anchors · "
        f"{esquema} esquema rows · {normativa} Normativa norms · "
        f"{unresolved} naming a norm normativa.yaml lacks",
        "#",
        "# Tab-separated: lesson, section, anchors, ids (first prose citation of each anchor), norm",
        "# (?: not in normativa.yaml, -: none), where it opens, the text the web marks.",
    ]
    return "\n".join(header + rows) + "\n"


@pytest.mark.parametrize("course", _linked_courses(), ids=lambda c: c.slug)
def test_every_citation_has_its_anchors_and_target_as_frozen(course: CourseRegistry) -> None:
    for locale in course.languages:
        golden = course_dir(course) / f"citations.{locale}.txt"
        current = _report(course, locale)
        if UPDATE:
            golden.write_text(current, encoding="utf-8")
        assert golden.exists(), f"no golden for {course.slug}: run with UPDATE_CITATIONS=1"
        assert current == golden.read_text(encoding="utf-8"), (
            f"{golden} moved — regenerate and review the diff"
        )


@pytest.mark.parametrize("course", _linked_courses(), ids=lambda c: c.slug)
def test_every_citation_carries_at_least_one_anchor(course: CourseRegistry) -> None:
    for locale, lessons in course.citations.lessons.items():
        for lesson_id, found in lessons.items():
            for item in found.items:
                if item.section != "normativa":
                    assert item.anchors, f"{lesson_id} ({locale}) «{item.text}» has no anchor"


@pytest.mark.parametrize("course", _linked_courses(), ids=lambda c: c.slug)
def test_the_source_index_is_fresh_and_covers_every_norm_file(course: CourseRegistry) -> None:
    root = course_dir(course)
    index = SourceIndex.load(root)
    assert (root / INDEX_FILE).exists(), "run scripts/index_sources.py"
    expected = {
        norm.file for norm in course.citations.norms.norms if norm.file and (root / norm.file).exists()
    }  # type: ignore[union-attr]
    assert set(index.files) == expected
    for file, entry in index.files.items():
        assert entry["sha256"] == sha256(root / file), f"{file} changed since it was indexed"


# --- links and serving ------------------------------------------------------------------------------


async def _sign_up(client: AsyncClient, username: str) -> None:
    courses = ["crypto-futures", "fixture-oposiciones"]
    body = {"username": username, "password": PASSWORD, "locale": "es", "courses": courses}
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"username": username, "password": PASSWORD})


async def test_a_lesson_ships_its_citations_with_anchors_and_source_targets(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "citer")
    lesson = (await multi_client.get(f"{OPOS}/lessons/m02-l1")).json()
    by_text = {c["text"]: c for c in lesson["citations"] if c["section"] == "prose"}
    assert by_text["art. 9.1 LRJSP"]["ids"] == ["boe-a-2015-10566-art-9"]
    assert by_text["art. 9.1 LRJSP"]["href"].endswith("/sources/normativa/lrjsp-extracto.pdf#page=2")
    assert by_text["art. 122.1 LPAC"]["href"].endswith("/sources/normativa/lpac-extracto.html#a1-22")
    assert by_text["guia-recursos.html"]["href"].endswith("/sources/otros/guia-recursos.html")
    # The «Normativa» block links its norms to the whole text.
    norms = [c for c in lesson["citations"] if c["section"] == "normativa"]
    assert [c["text"] for c in norms] == ["Ley 39/2015 (LPAC)", "Ley 40/2015 (LRJSP)"]


async def test_an_answered_question_links_to_the_paragraph_that_cites_its_article(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "linker")
    opened = (await multi_client.post(f"{OPOS}/exercises/m01-ex-1/attempts")).json()
    # Before answering there is no link to ask for: the review of an open attempt carries none.
    assert (await multi_client.get(f"{OPOS}/attempts/{opened['attemptId']}")).json()["lessonLink"] is None
    graded = (
        await multi_client.post(
            f"{OPOS}/attempts/{opened['attemptId']}/answer", json={"answer": {"optionId": "a"}}
        )
    ).json()
    assert graded["lessonLink"] == {
        "lessonId": "m01-l1",
        "anchor": "boe-a-2015-10565-art-122",
        "citation": "art. 122.1 LPAC",
    }


async def test_sources_are_served_as_static_files_and_html_is_sandboxed(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "fetcher")
    pdf = await multi_client.get(f"{OPOS}/sources/normativa/lrjsp-extracto.pdf")
    assert pdf.status_code == 200 and pdf.headers["content-type"] == "application/pdf"
    assert pdf.content.startswith(b"%PDF")
    html = await multi_client.get(f"{OPOS}/sources/otros/guia-recursos.html")
    assert html.status_code == 200 and html.headers["content-security-policy"] == "sandbox"
    for bad in ("normativa/..%2Fnormativa.yaml", "secretos/x.pdf", "normativa/no-existe.pdf"):
        assert (await multi_client.get(f"{OPOS}/sources/{bad}")).status_code == 404


async def test_a_course_without_normativa_has_no_citation_links_and_serves_no_sources(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "trader")
    lesson = (await multi_client.get(f"{CRYPTO}/lessons/m01-l1")).json()
    assert lesson["citations"] == []
    assert (await multi_client.get(f"{CRYPTO}/sources/normativa/x.pdf")).status_code == 404


# --- the cross-reference checks --------------------------------------------------------------------


def _copy(tmp_path: Path) -> Path:
    target = tmp_path / "fixture-oposiciones"
    shutil.copytree(FIXTURE, target)
    return target


def test_a_question_citing_an_article_its_lesson_never_cites_fails_the_load(tmp_path: Path) -> None:
    course = _copy(tmp_path)
    path = course / "exercises" / "m01-ex-2.yaml"
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    raw["variants"][3]["citation"] = "art. 125.1 LPAC"
    path.write_text(yaml.safe_dump(raw, allow_unicode=True), encoding="utf-8")
    with pytest.raises(
        ContentError,
        match=r"question m01-ex-2/alzada-04 cites «art\. 125\.1 LPAC», which its lesson m01-l1 never cites",
    ):
        load_registry(course)


def _cite_in_first_delegacion_question(course: Path, citation: str) -> None:
    path = course / "exercises" / "m02-ex-1.yaml"
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    raw["variants"][0]["citation"] = citation
    path.write_text(yaml.safe_dump(raw, allow_unicode=True), encoding="utf-8")


def test_a_question_citing_a_source_file_its_lesson_cites_opens_at_that_citation(tmp_path: Path) -> None:
    course = _copy(tmp_path)
    _cite_in_first_delegacion_question(course, "fuente: `guia-recursos.html`")
    registry = load_registry(course)
    link = registry.citations.question_link("m02-l1", "fuente: `guia-recursos.html`", "es")
    assert link.anchor == "fuente-guia-recursos-html"


def test_a_question_citing_a_source_file_its_lesson_never_cites_fails_the_load(tmp_path: Path) -> None:
    course = _copy(tmp_path)
    _cite_in_first_delegacion_question(course, "fuente: `otra-guia.html`")
    with pytest.raises(
        ContentError,
        match=(
            r"question m02-ex-1/delegacion-01 cites «fuente: `otra-guia\.html`», "
            r"which its lesson m02-l1 never cites"
        ),
    ):
        load_registry(course)


def test_an_esquema_row_citing_what_the_prose_does_not_fails_the_load_naming_the_row(tmp_path: Path) -> None:
    course = _copy(tmp_path)
    lesson = course / "es" / "lessons" / "m02-l1.md"
    text = lesson.read_text(encoding="utf-8").replace(
        "2. Resolución — tres meses (art. 122.2 LPAC)", "2. Resolución — tres meses (art. 125.2 LPAC)"
    )
    lesson.write_text(text, encoding="utf-8")
    with pytest.raises(
        ContentError,
        match=(
            r"m02-l1 line \d+, esquema «Plazos del recurso de alzada», row «Resolución — tres meses»: "
            r"cites «art\. 125\.2 LPAC»"
        ),
    ):
        load_registry(course)


def test_an_esquema_row_without_a_citation_fails_the_load(tmp_path: Path) -> None:
    course = _copy(tmp_path)
    lesson = course / "es" / "lessons" / "m02-l1.md"
    text = lesson.read_text(encoding="utf-8").replace(
        "1. Interposición — un mes (art. 122.1 LPAC)", "1. Interposición — un mes"
    )
    lesson.write_text(text, encoding="utf-8")
    with pytest.raises(ContentError, match="row «Interposición — un mes»: no citation"):
        load_registry(course)
