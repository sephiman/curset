# SPDX-License-Identifier: AGPL-3.0-only
"""Pure logic of the presets: the score transform, the per-lesson ranking rule and preset validation."""

from __future__ import annotations

import random
from collections.abc import Sequence
from fractions import Fraction

import pytest
from pydantic import ValidationError

from conftest import FIXTURE_CONTENT
from tradeschool.content.registry import CourseRegistry, load_registry
from tradeschool.exams.draw import DrawnQuestion, counted_questions, draw_part, pool_shortfalls
from tradeschool.exams.presets import ExamPreset, PartScoring
from tradeschool.exams.scoring import Tally, raw_score, transformed_score
from tradeschool.exercises.quiz import QuizConfig, QuizGenerator
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


_COMPOSITE_M01 = {"source": {"module": "m01"}, "questions": 4}
_COMPOSITE_M02 = {"source": {"module": "m02"}, "questions": 3}


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
        ({"id": "p", "source": {"module": "m01"}, "draw": "all", "questions": 3}, "takes every question"),
        ({"id": "p", "source": {"module": "m01"}, "draw": "all", "reserve": 2}, "has no reserve questions"),
        ({"id": "p", "source": {"modules": []}, "questions": 1}, "names one of"),
        (
            {"id": "p", "source": "course", "sources": [_COMPOSITE_M01, _COMPOSITE_M02], "questions": 3},
            "declares `source` or `sources`",
        ),
        ({"id": "p", "sources": [_COMPOSITE_M01]}, "at least 2"),
        ({"id": "p", "sources": [_COMPOSITE_M01, {"source": "cases", "questions": 2}]}, "draws questions"),
        (
            {"id": "p", "sources": [_COMPOSITE_M01, {"source": {"each": "lesson"}, "questions": 2}]},
            "draws questions",
        ),
        (
            {
                "id": "p",
                "sources": [_COMPOSITE_M01, {"source": "course", "draw": "per-module"}],
                "reserve": 1,
            },
            "has no reserve questions",
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


class _Seeded:
    """The two calls a draw makes, from a seeded stream (the service passes `secrets`)."""

    def __init__(self, seed: int) -> None:
        self._rng = random.Random(seed)

    def choice(self, seq: Sequence[str]) -> str:
        return self._rng.choice(seq)

    def randbelow(self, n: int) -> int:
        return self._rng.randrange(n)


def _preset(part: dict[str, object]) -> ExamPreset:
    return ExamPreset.model_validate({"id": "x", "version": 1, "title": {"es": "X"}, "parts": [part]})


def _lesson_counts(registry: CourseRegistry, drawn: list[DrawnQuestion]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for question in drawn:
        lesson_id = registry.question_lesson_id(question.exercise_id, None)
        assert lesson_id is not None
        counts[lesson_id] = counts.get(lesson_id, 0) + 1
    return counts


def test_each_source_of_a_part_draws_its_own_count_in_its_own_mode(registry: CourseRegistry) -> None:
    preset = _preset(
        {
            "id": "p",
            "sources": [
                {"source": {"lesson": "m01-l1"}, "draw": "all"},
                {"source": {"lesson": "m01-l2"}, "questions": 5},
                {"source": {"module": "m02"}, "draw": "per-module"},
            ],
        }
    )
    assert pool_shortfalls(registry, preset, None) == []
    assert counted_questions(registry, preset.parts[0], None) == 21 + 5 + 1
    drawn = draw_part(registry, preset.parts[0], None, _Seeded(7)).questions
    assert _lesson_counts(registry, drawn) == {"m01-l1": 21, "m01-l2": 5, "m02-l1": 1}
    # `all` takes every question of its lesson: each quiz variant exactly once.
    generator = QuizGenerator()
    variants = set()
    for question in drawn:
        config = registry.get_exercise_config(question.exercise_id)
        if registry.question_lesson_id(question.exercise_id, None) == "m01-l1":
            assert config is not None and isinstance(config[1], QuizConfig)
            variants.add((question.exercise_id, generator.variant(config[1], question.seed).id))
    assert len(variants) == 21


def test_a_set_of_modules_draws_from_every_module_in_it(registry: CourseRegistry) -> None:
    preset = _preset({"id": "p", "source": {"modules": ["m02", "m01"]}, "questions": 60})
    drawn = draw_part(registry, preset.parts[0], None, _Seeded(3)).questions
    modules = {question.exercise_id.split("-")[0] for question in drawn}
    assert len(drawn) == 60 and modules == {"m01", "m02"}
    too_many = _preset({"id": "p", "source": {"modules": ["m02", "m01"]}, "questions": 82})
    assert pool_shortfalls(registry, too_many, None) == ["part 'p' needs 82 questions; the pool holds 81"]


def test_a_composite_draw_is_shuffled_and_its_reserves_come_last(registry: CourseRegistry) -> None:
    part = {"id": "p", "sources": [_COMPOSITE_M01, _COMPOSITE_M02], "reserve": 2}
    drawn = draw_part(registry, _preset(part).parts[0], None, _Seeded(11)).questions
    assert [question.reserve for question in drawn] == [False] * 7 + [True] * 2
    modules = [question.exercise_id.split("-")[0] for question in drawn[:7]]
    assert sorted(modules) == ["m01"] * 4 + ["m02"] * 3
    assert modules != sorted(modules)
    assert len({(question.exercise_id, question.seed) for question in drawn}) == 9


def test_composite_sources_that_overlap_or_run_short_fail_the_load_check(registry: CourseRegistry) -> None:
    overlapping = _preset(
        {"id": "p", "sources": [_COMPOSITE_M01, {"source": {"lesson": "m01-l2"}, "questions": 1}]}
    )
    assert pool_shortfalls(registry, overlapping, None) == ["part 'p': sources 1 and 2 share questions"]
    too_many = _preset(
        {"id": "p", "sources": [_COMPOSITE_M02, {"source": {"lesson": "m01-l1"}, "questions": 22}]}
    )
    assert pool_shortfalls(registry, too_many, None) == [
        "part 'p' source 2 needs 22 questions; the pool holds 21"
    ]
