# SPDX-License-Identifier: AGPL-3.0-only
"""Pure logic of the presets: the score transform, the per-lesson ranking rule and preset validation."""

from __future__ import annotations

from fractions import Fraction

import pytest
from pydantic import ValidationError

from conftest import FIXTURE_CONTENT
from tradeschool.content.registry import CourseRegistry, load_registry
from tradeschool.exams.presets import ExamPreset, PartScoring
from tradeschool.exams.scoring import Tally, raw_score, transformed_score
from tradeschool.stats.by_lesson import lesson_table

CPS = PartScoring(max=50, pass_minimum=25, minimum_raw=31.67)


def test_raw_is_correct_minus_the_penalty_per_wrong_and_blanks_cost_nothing() -> None:
    assert raw_score(Tally(correct=50, wrong=12, blank=8), Fraction(1, 3), "free") == 46
    assert raw_score(Tally(correct=50, wrong=12, blank=8), Fraction(1, 3), "wrong") == Fraction(130, 3)
    assert raw_score(Tally(correct=10, wrong=10, blank=0), Fraction(0), "free") == 10


def test_the_transform_is_the_cps_formula_of_the_intro_lesson() -> None:
    # m00-l01's own example: M = 31,67, N = 70, d = 46 gives 34,35.
    assert float(transformed_score(Fraction(46), 70, CPS)) == pytest.approx(34.35, abs=0.01)
    assert transformed_score(Fraction("31.67"), 70, CPS) == 25
    assert transformed_score(Fraction(70), 70, CPS) == 50
    assert float(transformed_score(Fraction(10), 70, CPS)) == pytest.approx(25 * 10 / 31.67, abs=1e-6)
    assert transformed_score(Fraction(-3), 70, CPS) == 0


@pytest.fixture(scope="module")
def registry() -> CourseRegistry:
    return load_registry(FIXTURE_CONTENT / "fixture-oposiciones")


def test_no_lesson_is_ranked_on_fewer_than_three_questions(registry: CourseRegistry) -> None:
    outcomes = [("m01-l1", "correct")] * 2 + [("m01-l2", "wrong")] * 5 + [("m02-l1", "correct")] * 5
    outcomes += [("m02-l2", "wrong")] * 4
    table = lesson_table(registry, outcomes, "es")  # type: ignore[arg-type]
    assert table["lists"] is not None
    ranked = [e["lessonId"] for e in table["lists"]["best"] + table["lists"]["worst"]]  # type: ignore[index]
    assert "m01-l1" not in ranked
    assert table["lists"]["level"] == "lesson"  # type: ignore[index]


def test_fewer_than_three_ranked_lessons_fall_back_to_modules_or_to_no_lists(
    registry: CourseRegistry,
) -> None:
    two_lessons = [("m01-l1", "correct")] * 4 + [("m02-l1", "wrong")] * 4
    table = lesson_table(registry, two_lessons, "es")  # type: ignore[arg-type]
    # Two lessons and two modules: neither level reaches three, so only the table shows.
    assert table["lists"] is None
    assert [g["moduleId"] for g in table["groups"]] == ["m01", "m02"]  # type: ignore[index]


def test_the_module_fallback_says_so(registry: CourseRegistry) -> None:
    # A three-module course is needed to rank modules: the fixture's two are not enough, so the rule is
    # shown on a lesson set whose lessons cannot rank but whose modules (copied in) can.
    from dataclasses import replace

    from tradeschool.content.schema import ManifestBlock, ManifestModule

    block = registry.manifest.blocks[0]
    third = ManifestModule.model_validate(
        {
            "id": "m03",
            "title": {"es": "Tercero"},
            "summary": {"es": "Un módulo más."},
            "lessons": [{"id": "m03-l1", "title": {"es": "Uno"}, "summary": {"es": "Uno."}}],
        }
    )
    manifest = registry.manifest.model_copy(
        update={"blocks": [ManifestBlock(id=block.id, title=block.title, modules=[*block.modules, third])]}
    )
    widened = replace(
        registry, manifest=manifest, markdown={"es": {**registry.markdown["es"], "m03-l1": "# Uno"}}
    )
    widened.__post_init__()
    outcomes = [("m01-l1", "correct"), ("m01-l2", "correct"), ("m01-l2", "wrong")]
    outcomes += [("m02-l1", "wrong"), ("m02-l2", "wrong"), ("m02-l2", "correct")]
    outcomes += [("m03-l1", "correct")] * 3
    table = lesson_table(widened, outcomes, "es")  # type: ignore[arg-type]
    lists = table["lists"]
    assert lists is not None and lists["level"] == "module"  # type: ignore[index]
    assert lists["best"][0]["moduleId"] == "m03" and lists["worst"][0]["moduleId"] == "m02"  # type: ignore[index]


@pytest.mark.parametrize(
    ("part", "message"),
    [
        ({"id": "p", "source": "course", "questions": 10, "penalty": "1/2"}, "must be one of 0, 1/4, 1/3"),
        ({"id": "p", "source": "course"}, "a random draw needs `questions`"),
        ({"id": "p", "source": "cases", "questions": 20}, "needs `choose` and `questions`"),
        ({"id": "p", "source": {"block": "a", "module": "m"}, "questions": 1}, "names one of"),
        (
            {"id": "p", "source": "course", "draw": "per-module", "questions": 3},
            "takes its count from the course",
        ),
    ],
)
def test_a_malformed_part_is_refused(part: dict[str, object], message: str) -> None:
    with pytest.raises(ValidationError, match=message):
        ExamPreset.model_validate({"id": "x", "version": 1, "title": {"es": "X"}, "parts": [part]})


def test_a_part_cannot_wait_on_a_part_without_a_pass_minimum() -> None:
    parts = [
        {"id": "a", "source": "course", "questions": 5},
        {"id": "b", "source": "course", "questions": 5, "requires_previous_pass": True},
    ]
    with pytest.raises(ValidationError, match="has no pass minimum"):
        ExamPreset.model_validate({"id": "x", "version": 1, "title": {"es": "X"}, "parts": parts})
