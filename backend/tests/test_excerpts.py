# SPDX-License-Identifier: AGPL-3.0-only
"""The solution panel's text of the norm (delta F): extraction, the build check, and what the API ships.

`excerpts.json` is built by `scripts/extract_excerpts.py`; the fixture course's is rebuilt here from its
HTML, PDF and saved page and must match the committed file, so extraction is proven end to end.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest
from httpx import AsyncClient
from pypdf import PdfReader
from sqlalchemy import update

from conftest import FIXTURE_CONTENT
from pipeline_courses import REPO_CONTENT, course_dir, pipeline_courses
from tradeschool.attempts.models import Attempt
from tradeschool.citations.excerpt_build import EXCLUSIONS_FILE, SourceTexts, build_excerpts
from tradeschool.citations.excerpt_store import EXCERPTS_FILE, MissingExcerpt
from tradeschool.citations.excerpts import (
    FULL_CAP,
    NO_FACT,
    WORD_CAP,
    Block,
    Excerpt,
    capped,
    html_blocks,
    page_excerpt,
    pdf_blocks,
)
from tradeschool.citations.grammar import Part, cited_parts
from tradeschool.citations.sources import heading_unit, sha256
from tradeschool.content.registry import ContentError, QuestionRef, load_registry
from tradeschool.db import get_sessionmaker
from tradeschool.exercises.quiz import QuizConfig

OPOS = "/api/courses/fixture-oposiciones"
CRYPTO = "/api/courses/crypto-futures"
FIXTURE = FIXTURE_CONTENT / "fixture-oposiciones"
AGE = REPO_CONTENT / "age-administrativo-c1"
PASSWORD = "correcthorse"
# F3: the round that adds the panel brings the AGE course under this share of questions without an excerpt.
NO_EXCERPT_CEILING = 0.01


def _pdf_pages(path: Path) -> list[str]:
    return [page.extract_text() or "" for page in PdfReader(path).pages]


def _questions(course: Path) -> dict[str, dict[str, object]]:
    return dict(json.loads((course / EXCERPTS_FILE).read_text(encoding="utf-8"))["questions"])


# --- the pieces --------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("citation", "parts"),
    [
        ("art. 30.4 LPAC", {"art-30": Part(("4",))}),
        ("art. 94.1.e CE", {"art-94": Part(("1",), (("1", "e"),))}),
        ("art. 14.2.d) y e) LPAC", {"art-14": Part(("2",), (("2", "d"), ("2", "e")))}),
        ("arts. 30.2\u20133 y 68.1 LPAC", {"art-30": Part(("2", "3")), "art-68": Part(("1",))}),
        ("art. 61.ñ TREBEP", {"art-61": Part((), (("", "ñ"),))}),
        ("art. 9.Dos.1 Ley 31/2022", {"art-9": Part(("Dos",))}),
        ("disposición adicional cuarta.1 Ley 19/2013", {"da-cuarta": Part(("1",))}),
        ("art. 67 CE", {}),
    ],
)
def test_a_citation_names_the_apartados_and_letters_it_cites(citation: str, parts: dict[str, Part]) -> None:
    assert cited_parts(citation) == parts


@pytest.mark.parametrize(
    ("line", "slug"),
    [
        ("Artículo treinta y tres.  Régimen", "art-33"),
        ("Artículo veintidós.  ", "art-22"),
        ("Artículo veintinueve bis. Reingreso", "art-29-bis"),
        ("Artículo decimoquinto.", "art-15"),
        ("Disposición transitoria vigésima sexta.  Calificación", "dt-vigesimosexta"),
    ],
)
def test_older_laws_spell_their_article_numbers_and_the_index_reads_them(line: str, slug: str) -> None:
    unit = heading_unit(line)
    assert unit is not None and unit.slug == slug


def test_a_boe_pdf_rejoins_wrapped_lines_and_drops_its_running_footer() -> None:
    page_one = (
        "Artículo 30.  Cómputo de plazos.\n1. Cuando los plazos se señalen por horas, se entiende \n"
        "que éstas son hábiles.\n2. Siempre que por Ley no se exprese otro cómputo, los plazos \n"
        "BOLETÍN OFICIAL DEL ESTADO\nLEGISLACIÓN CONSOLIDADA\nPágina 30"
    )
    page_two = "señalados por días son hábiles.\nArtículo 31.  Cómputo de plazos en los registros.\n"
    texts = [block.text for block in pdf_blocks([page_one, page_two])]
    assert texts == [
        "Artículo 30. Cómputo de plazos.",
        "1. Cuando los plazos se señalen por horas, se entiende que éstas son hábiles.",
        "2. Siempre que por Ley no se exprese otro cómputo, los plazos señalados por días son hábiles.",
        "Artículo 31. Cómputo de plazos en los registros.",
    ]


def test_a_wrapped_line_that_starts_with_an_ordinal_is_not_a_heading() -> None:
    page = "1. Podrá conceder una ampliación si no perjudica derechos de \ntercero. El acuerdo se notifica.\n"
    assert [block.level for block in pdf_blocks([page])] == [0]


def test_a_table_row_is_one_block_with_its_cells_in_order() -> None:
    blocks, title = html_blocks(
        "<html><head><title>Atajos</title></head><body><table><tr><td><p>Ctrl+C</p></td>"
        "<td><p>Copia el elemento.</p></td></tr></table></body></html>"
    )
    assert title == "Atajos"
    assert [block.text for block in blocks] == ["Ctrl+C — Copia el elemento."]


def test_an_excerpt_is_capped_at_a_sentence_end_and_marked() -> None:
    text = " ".join(["Una frase de diez palabras que termina aquí con punto."] * 30)
    cut, was_cut = capped(text)
    assert was_cut and cut.endswith("punto. […]")
    assert len(cut.split()) <= WORD_CAP + 1
    assert capped("Corta.") == ("Corta.", False)
    assert FULL_CAP == 1500


def test_blocks_keep_the_page_they_start_on() -> None:
    assert pdf_blocks(["Artículo 9.  Delegación.\n"]) == [Block("Artículo 9. Delegación.", 1, 1)]


# --- the fixture, end to end --------------------------------------------------------------------------


def test_the_fixture_excerpts_rebuild_from_its_sources_exactly_as_committed() -> None:
    registry = load_registry(FIXTURE, check_excerpts=False)
    built = build_excerpts(registry, SourceTexts(FIXTURE, _pdf_pages))
    assert built == json.loads((FIXTURE / EXCERPTS_FILE).read_text(encoding="utf-8")), (
        "fixture excerpts moved: run scripts/extract_excerpts.py --content tests/fixtures/content"
    )


def test_an_html_norm_gives_the_cited_paragraph_and_the_whole_article() -> None:
    excerpt = _questions(FIXTURE)["plazo-alzada"]["excerpt"]
    first = (
        "1. El plazo para la interposición del recurso de alzada será de un mes, si el acto fuera expreso."
    )
    second = "2. El plazo máximo para dictar y notificar la resolución será de tres meses."
    assert excerpt == {
        "heading": "Art. 122.1 LPAC",
        "text": first,
        "full": f"Artículo 122. Plazos.\n\n{first}\n\n{second}",
        "source": {"file": "sources/normativa/lpac-extracto.html", "fragment": "#a1-22"},
    }


def test_a_pdf_norm_gives_the_cited_paragraph_at_its_page() -> None:
    excerpt = _questions(FIXTURE)["delegacion-01"]["excerpt"]
    assert isinstance(excerpt, dict)
    assert excerpt["heading"] == "Art. 9.4 LRJSP"
    assert excerpt["text"] == (
        "4. Las resoluciones administrativas que se adopten por delegación indicarán expresamente esta "
        "circunstancia y se considerarán dictadas por el órgano delegante."
    )
    assert excerpt["source"] == {"file": "sources/normativa/lrjsp-extracto.pdf", "fragment": "#page=2"}


def test_a_saved_page_gives_the_labelled_paragraph_with_its_title_and_date() -> None:
    excerpt = _questions(FIXTURE)["recursos-19"]["excerpt"]
    assert excerpt == {
        "heading": "Recursos administrativos",
        "text": "El recurso de alzada se dirige al órgano superior jerárquico. "
        "El de reposición, al mismo órgano que dictó el acto.",
        "attribution": "Guía de recursos administrativos (fixture), consultado el 2026-10-28",
        "source": {"file": "sources/otros/guia-recursos.html", "fragment": ""},
    }


def test_a_question_without_an_excerpt_says_why() -> None:
    assert _questions(FIXTURE)["recursos-20"] == {
        "citation": "fuente: `guia-recursos.html`; «Plazos de los recursos»",
        "none": "label not found",
        "source": {"file": "sources/otros/guia-recursos.html", "fragment": ""},
    }


# --- the build check ----------------------------------------------------------------------------------


def _copy(tmp_path: Path) -> Path:
    target = tmp_path / "fixture-oposiciones"
    shutil.copytree(FIXTURE, target)
    return target


def test_a_course_with_norms_and_no_excerpts_file_fails_the_load(tmp_path: Path) -> None:
    course = _copy(tmp_path)
    (course / EXCERPTS_FILE).unlink()
    with pytest.raises(ContentError, match=r"excerpts\.json is missing: run scripts/extract_excerpts\.py"):
        load_registry(course)


def test_a_question_whose_excerpt_was_built_for_another_citation_fails_the_load(tmp_path: Path) -> None:
    course = _copy(tmp_path)
    raw = json.loads((course / EXCERPTS_FILE).read_text(encoding="utf-8"))
    raw["questions"]["plazo-alzada"]["citation"] = "art. 121.1 LPAC"
    del raw["questions"]["delegacion-02"]
    (course / EXCERPTS_FILE).write_text(json.dumps(raw), encoding="utf-8")
    with pytest.raises(ContentError, match=r"stale.*plazo-alzada: built for «art\. 121\.1 LPAC».*"):
        load_registry(course)
    with pytest.raises(ContentError, match=r"delegacion-02 has no entry"):
        load_registry(course)


@pytest.mark.parametrize(
    "course", [c for c in pipeline_courses() if c.excerpts is not None], ids=lambda c: c.slug
)
def test_every_source_an_excerpt_was_read_from_is_unchanged(course: object) -> None:
    root = course_dir(course)  # type: ignore[arg-type]
    digests = json.loads((root / EXCERPTS_FILE).read_text(encoding="utf-8"))["sources"]
    stale = [file for file, digest in digests.items() if sha256(root / file) != digest]
    assert not stale, f"sources changed since the excerpts were built: {stale}"


def test_fewer_than_one_percent_of_age_questions_fail_extraction_and_each_without_an_excerpt_says_why() -> (
    None
):
    questions = _questions(AGE)
    missing = {key: entry for key, entry in questions.items() if "excerpt" not in entry}
    assert all(isinstance(entry.get("none"), str) and entry["none"] for entry in missing.values())
    # F3's ceiling is on extraction; questions a blind verifier sent to «sin extracto» are counted apart.
    failed = [key for key, entry in missing.items() if entry["none"] != NO_FACT]
    assert len(failed) / len(questions) < NO_EXCERPT_CEILING, f"{len(failed)} of {len(questions)}"


def test_a_question_listed_in_the_exclusions_is_built_without_an_excerpt(tmp_path: Path) -> None:
    course = _copy(tmp_path)
    (course / EXCLUSIONS_FILE).write_text(
        "questions:\n- question: plazo-alzada\n  reason: verifier\n", encoding="utf-8"
    )
    built = build_excerpts(load_registry(course, check_excerpts=False), SourceTexts(course, _pdf_pages))
    entry = built["questions"]["plazo-alzada"]  # type: ignore[index]
    assert entry["none"] == NO_FACT
    assert entry["source"] == {"file": "sources/normativa/lpac-extracto.html", "fragment": "#a1-22"}


_PAGE = (
    "<html><head><title>Guía</title></head><body><h2>Formatos</h2><p>Introducción a los formatos.</p>"
    "<table><tr><td>Código</td><td>Nombre</td><td>Uso</td></tr>"
    "<tr><td>dd</td><td>Día</td><td>Dos dígitos</td></tr>"
    "<tr><td>mm</td><td>Mes</td><td>Dos dígitos</td></tr></table>"
    "<h2>Otros</h2><p>Primera frase de relleno. "
    "Para abrir el panel, seleccione Archivo y después Opciones de la página.</p>"
    "</body></html>"
)


def test_a_cited_sentence_shows_its_paragraph_under_the_nearest_heading() -> None:
    blocks, title = html_blocks(_PAGE)
    label = "Para abrir el panel, seleccione Archivo y después Opciones de la página."
    excerpt = page_excerpt(blocks, label, "", "sources/otros/guia.html", None, title)
    assert isinstance(excerpt, Excerpt)
    assert excerpt.heading == "Otros"
    assert excerpt.text == "Primera frase de relleno. " + label


def test_a_cited_table_row_comes_with_the_header_row_that_names_its_columns() -> None:
    blocks, title = html_blocks(_PAGE)
    excerpt = page_excerpt(blocks, "mm — Mes — Dos dígitos", "", "sources/otros/guia.html", None, title)
    assert isinstance(excerpt, Excerpt)
    assert excerpt.text == "Código — Nombre — Uso\n\nmm — Mes — Dos dígitos"
    assert excerpt.heading == "Formatos"


def test_every_age_question_without_an_excerpt_still_has_its_explanation_lesson_link_and_reason() -> None:
    registry = next(course for course in pipeline_courses() if course.slug == "age-administrativo-c1")
    homes = {
        variant.id: exercise_id
        for exercise_id, (_, config) in registry.exercise_configs.items()
        if isinstance(config, QuizConfig)
        for variant in config.variants
    }
    missing = [key for key, entry in _questions(AGE).items() if "none" in entry]
    assert missing
    for key in missing:
        ref = QuestionRef(homes[key], variant_id=key)
        assert isinstance(registry.question_excerpt(ref), MissingExcerpt), key
        link = registry.question_link(ref, "es")
        assert link is not None and link.lesson_id, key
        config = registry.attempt_config(ref)
        assert config is not None and isinstance(config[1], QuizConfig)
        explanation = config[1].variants[0].explanation
        assert explanation is not None and explanation.get("es"), key


# --- what the API ships -------------------------------------------------------------------------------


async def _sign_up(client: AsyncClient, username: str) -> None:
    body = {
        "username": username,
        "password": PASSWORD,
        "locale": "es",
        "courses": ["crypto-futures", "fixture-oposiciones"],
    }
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"username": username, "password": PASSWORD})


async def test_an_answered_question_ships_the_cited_text_and_its_source_link(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "reader")
    opened = (await multi_client.post(f"{OPOS}/exercises/m01-ex-1/attempts")).json()
    # Never before answering: the open attempt's review carries no excerpt.
    assert (await multi_client.get(f"{OPOS}/attempts/{opened['attemptId']}")).json()["excerpt"] is None
    graded = (
        await multi_client.post(
            f"{OPOS}/attempts/{opened['attemptId']}/answer", json={"answer": {"optionId": "b"}}
        )
    ).json()
    excerpt = graded["excerpt"]
    assert excerpt["heading"] == "Art. 122.1 LPAC"
    assert excerpt["text"].startswith(
        "1. El plazo para la interposición del recurso de alzada será de un mes"
    )
    assert excerpt["href"] == f"{OPOS}/sources/normativa/lpac-extracto.html#a1-22"
    assert excerpt["full"].startswith("Artículo 122. Plazos.") and excerpt["fullTooLong"] is False
    review = (await multi_client.get(f"{OPOS}/attempts/{opened['attemptId']}")).json()
    assert review["excerpt"] == excerpt


async def test_a_question_without_an_excerpt_ships_its_reason_with_the_explanation_and_lesson_link(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "unquoted")
    opened = (await multi_client.post(f"{OPOS}/exercises/m02-ex-2/attempts")).json()
    async with get_sessionmaker()() as session:  # pin the attempt to the question whose label the page lacks
        await session.execute(
            update(Attempt).where(Attempt.id == opened["attemptId"]).values(variant_id="recursos-20")
        )
        await session.commit()
    graded = (
        await multi_client.post(
            f"{OPOS}/attempts/{opened['attemptId']}/answer", json={"answer": {"optionId": "a"}}
        )
    ).json()
    assert graded["excerpt"] is None
    assert graded["noExcerpt"] == {"reason": "no-label", "href": f"{OPOS}/sources/otros/guia-recursos.html"}
    assert graded["explanation"]
    assert graded["lessonLink"]["lessonId"] == "m02-l1"
    assert graded["lessonLink"]["anchor"] == "fuente-guia-recursos-html"


async def test_a_course_without_norms_ships_no_excerpt(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "trader")
    opened = (await multi_client.post(f"{CRYPTO}/exercises/m04-ex-1/attempts")).json()
    option = opened["payload"]["options"][0]["id"]
    graded = (
        await multi_client.post(
            f"{CRYPTO}/attempts/{opened['attemptId']}/answer", json={"answer": {"optionId": option}}
        )
    ).json()
    assert graded["excerpt"] is None and graded["noExcerpt"] is None
    assert graded["explanation"]


async def test_an_exam_shows_no_excerpt_until_it_is_submitted(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "sitter")
    started = await multi_client.post(f"{OPOS}/exams", json={"presetId": "simulacro"})
    assert started.status_code == 201, started.text
    exam = started.json()
    assert all(q["excerpt"] is None for q in exam["questions"])
    submitted = (await multi_client.post(f"{OPOS}/exams/{exam['id']}/submit")).json()
    with_text = [q for q in submitted["questions"] if q["excerpt"] is not None]
    # Every question of the fixture has an excerpt but the one whose label its page lacks.
    assert len(with_text) >= len(submitted["questions"]) - 1
    assert all(q["excerpt"]["href"].startswith(f"{OPOS}/sources/") for q in with_text)
