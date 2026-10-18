# SPDX-License-Identifier: AGPL-3.0-only
"""The `:::esquema` block (delta E): its four kinds as written, its format errors, and its words read."""

from __future__ import annotations

import pytest

from conftest import FIXTURE_CONTENT
from tradeschool.content.esquema import EsquemaError, parse_esquemas
from tradeschool.content.reading import prose_word_count
from tradeschool.content.registry import ContentError, _check_summaries_never_coin, load_registry

LESSON = (FIXTURE_CONTENT / "fixture-oposiciones" / "es" / "lessons" / "m02-l1.md").read_text(
    encoding="utf-8"
)


def test_the_fixture_lesson_holds_one_esquema_of_each_kind_with_its_rows() -> None:
    esquemas = parse_esquemas(LESSON)
    assert [e.kind for e in esquemas] == ["arbol", "tabla", "plazos", "pasos"]
    arbol, tabla, plazos, pasos = esquemas
    assert [(r.fields, r.parent) for r in arbol.rows] == [
        (("Órgano delegante",), None),
        (("Órgano delegado", "sus resoluciones se consideran dictadas por el delegante"), 0),
        (("Órgano superior", "puede avocar un asunto de un órgano dependiente"), None),
    ]
    assert tabla.header == ("Recurso", "Ante quién se presenta", "Plazo con acto expreso", "Artículo")
    assert [r.citation for r in tabla.rows] == ["art. 122.1 LPAC", "art. 124.1 LPAC"]
    assert [r.fields for r in plazos.rows] == [("Interposición", "un mes"), ("Resolución", "tres meses")]
    assert pasos.rows[0].fields == (
        "Presentación",
        "escrito de recurso",
        "órgano que dictó el acto o el que debe resolverlo",
    )
    assert all(r.citation for e in esquemas for r in e.rows)


@pytest.mark.parametrize(
    ("block", "message"),
    [
        (':::esquema{kind=mapa title="X"}\n- a (art. 1 CE)\n:::', "kind must be one of"),
        (":::esquema{kind=plazos}\n1. a — b (art. 1 CE)\n:::", "needs a title"),
        (':::esquema{kind=plazos title="X"}\nTexto libre.\n:::', "no free prose"),
        (':::esquema{kind=pasos title="X"}\n1. solo dos — campos (art. 1 CE)\n:::', "row has 3 to 3 fields"),
        (
            ':::esquema{kind=plazos title="X"}\n1. a — b (art. 1 CE)\n  1. c — d (art. 2 CE)\n:::',
            "only an arbol",
        ),
        (':::esquema{kind=tabla title="X"}\n| a | b |\n|---|---|\n| 1 |\n:::', "1 cells under a 2-column"),
        (':::esquema{kind=plazos title="X"}\n1. a — b (art. 1 CE)\n', "never closed"),
    ],
)
def test_a_malformed_esquema_is_refused_with_its_line(block: str, message: str) -> None:
    with pytest.raises(EsquemaError, match=message):
        parse_esquemas(block)


def test_reading_time_counts_the_words_of_an_esquema() -> None:
    without = prose_word_count("Texto.")
    with_esquema = prose_word_count(
        'Texto.\n\n:::esquema{kind=plazos title="X"}\n1. Interposición — un mes (art. 122.1 LPAC)\n:::'
    )
    # The rows' words (Interposición, un, mes, art., 122.1, LPAC) count; the fence and the dash do not.
    assert with_esquema - without == 6


def test_never_coins_reads_esquema_text_as_lesson_text() -> None:
    """A summary may use a glossary term its lesson carries only inside an esquema, and not one it lacks."""
    registry = load_registry(FIXTURE_CONTENT / "fixture-oposiciones")
    lesson = next(lesson for _, lesson in registry.manifest.iter_lessons() if lesson.id == "m02-l2")
    summary = lesson.summary.model_copy(update={"es": "Dos supuestos sobre el recurso de alzada."})
    manifest = registry.manifest.model_copy(deep=True)
    next(lsn for _, lsn in manifest.iter_lessons() if lsn.id == "m02-l2").summary = summary
    markdown = {"es": dict(registry.markdown["es"])}
    with pytest.raises(ContentError, match="m02-l2"):
        _check_summaries_never_coin(manifest, registry.glossary, markdown)
    markdown["es"]["m02-l2"] += (
        '\n\n:::esquema{kind=plazos title="X"}\n1. Recurso de alzada — un mes (art. 122.1 LPAC)\n:::'
    )
    _check_summaries_never_coin(manifest, registry.glossary, markdown)
