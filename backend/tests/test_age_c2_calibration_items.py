# SPDX-License-Identifier: AGPL-3.0-only
"""The 34 stored psicotécnico calibration items of age-auxiliar-c2: one per generator level, never drawn."""

from __future__ import annotations

from pathlib import Path

import pytest

from tradeschool.content.registry import CourseRegistry, load_registry
from tradeschool.exercises.quiz import QuizConfig, QuizGenerator, QuizVariant
from tradeschool.psicotecnico.item import Params
from tradeschool.psicotecnico.registry import load_generator

CONTENT_DIR = Path(__file__).resolve().parent.parent.parent / "content" / "age-auxiliar-c2"


@pytest.fixture(scope="module")
def registry() -> CourseRegistry:
    return load_registry(CONTENT_DIR)


@pytest.fixture(scope="module")
def variants(registry: CourseRegistry) -> list[QuizVariant]:
    config = registry.get_exercise_config("ps-calibracion")
    assert config is not None and isinstance(config[1], QuizConfig)
    return config[1].variants


def _seed(variant: QuizVariant) -> int:
    return int(next(tag for tag in variant.tags if tag.startswith("seed:")).removeprefix("seed:"))


def test_there_is_one_item_per_level_of_every_generator_the_course_declares(
    registry: CourseRegistry, variants: list[QuizVariant]
) -> None:
    expected = {
        (use.generator, level)
        for use in registry.manifest.course.practice_generators
        for level in load_generator(use.generator).levels
    }
    stored = {(v.tags[0], v.difficulty) for v in variants}
    assert len(variants) == len(stored) == len(expected) == 34
    assert stored == expected


def test_each_item_is_the_generator_output_for_its_seed_with_the_solvers_key(
    variants: list[QuizVariant],
) -> None:
    for variant in variants:
        generator = load_generator(variant.tags[0])
        assert variant.difficulty is not None
        item = generator.generate(_seed(variant), Params(variant.difficulty))
        assert variant.prompt.get("es") == item.stem, variant.id
        assert [o.text.get("es") for o in variant.options] == list(item.options), variant.id
        assert [o.correct for o in variant.options].index(True) == generator.solve(item), variant.id
        assert variant.explanation is not None and variant.explanation.get("es") == item.explanation, (
            variant.id
        )
        assert generator.check(item) == [], variant.id


def test_the_items_have_four_options_one_key_and_a_stable_option_order(variants: list[QuizVariant]) -> None:
    config = QuizConfig.model_construct(type="quiz", variants=variants, shuffle=False)
    for variant in variants:
        assert [o.id for o in variant.options] == ["a", "b", "c", "d"]
        assert sum(o.correct for o in variant.options) == 1
        shown = QuizGenerator().generate(config, 0, "es")
        assert shown.payload["options"] is not None
    assert len({v.id for v in variants}) == len(variants)


def test_a_table_item_carries_its_table_into_the_payload(variants: list[QuizVariant]) -> None:
    tables = [v for v in variants if v.table is not None]
    assert {v.tags[0] for v in tables} == {"tablas-lectura", "administrativo-clasificacion"}
    assert sum(v.tags[0] == "tablas-lectura" for v in tables) == 3
    for variant in tables:
        assert variant.table is not None
        config = QuizConfig(type="quiz", shuffle=False, variants=[variant])
        payload = QuizGenerator().generate(config, 1, "es").payload
        assert payload["table"] == variant.table.model_dump()
        assert all(len(row) == len(variant.table.header) for row in variant.table.rows)


def test_a_table_on_a_true_false_question_is_refused() -> None:
    with pytest.raises(ValueError, match="single_choice"):
        QuizVariant.model_validate(
            {
                "id": "x",
                "kind": "true_false",
                "prompt": {"es": "¿Sí?"},
                "answer": True,
                "table": {"title": "T", "header": ["a"], "rows": [["1"]]},
            }
        )


def test_a_ragged_table_is_refused() -> None:
    with pytest.raises(ValueError, match="does not match its header"):
        QuizVariant.model_validate(
            {
                "id": "x",
                "prompt": {"es": "¿Cuál?"},
                "options": [
                    {"id": "a", "text": {"es": "1"}, "correct": True},
                    {"id": "b", "text": {"es": "2"}},
                ],
                "table": {"title": "T", "header": ["a", "b"], "rows": [["1"]]},
            }
        )
