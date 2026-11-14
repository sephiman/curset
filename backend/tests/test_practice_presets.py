# SPDX-License-Identifier: AGPL-3.0-only
"""Requirements 6.6 of backend-in-depth: each practice preset draws exactly its own questions."""

from __future__ import annotations

from functools import cache
from pathlib import Path

import pytest
from httpx import AsyncClient
from pydantic import ValidationError

from tradeschool.content.registry import CourseRegistry, load_registry
from tradeschool.content.schema import ManifestCourse
from tradeschool.exercises.quiz import QuizConfig

BACKEND = "/api/courses/backend-in-depth"
OPOS = "/api/courses/fixture-oposiciones"


@cache
def _registry() -> CourseRegistry:
    return load_registry(Path(__file__).resolve().parents[2] / "content" / "backend-in-depth")


def _keys(questions: list[dict[str, str]]) -> list[tuple[str, str]]:
    return [(q["exerciseId"], q["questionId"]) for q in questions]


def _snippet(registry: CourseRegistry, exercise_id: str, question_id: str) -> str | None:
    config = registry.exercise_configs[exercise_id][1]
    assert isinstance(config, QuizConfig)
    return next(v.snippet for v in config.variants if v.id == question_id)


async def _sign_up(client: AsyncClient, name: str, course: str = "backend-in-depth") -> None:
    email = f"{name}@example.com"
    body = {"email": email, "name": name, "password": "correcthorse", "locale": "en", "courses": [course]}
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"email": email, "password": "correcthorse"})


async def _answer_right(client: AsyncClient, exercise_id: str, question_id: str) -> None:
    config = _registry().exercise_configs[exercise_id][1]
    assert isinstance(config, QuizConfig)
    variant = next(v for v in config.variants if v.id == question_id)
    option = next(o.id for o in variant.options if o.correct)
    opened = await client.post(f"{BACKEND}/exercises/{exercise_id}/attempts", json={"variantId": question_id})
    attempt_id = opened.json()["attemptId"]
    await client.post(f"{BACKEND}/attempts/{attempt_id}/answer", json={"answer": {"optionId": option}})


async def test_the_course_page_lists_the_five_presets_in_order(backend_client: AsyncClient) -> None:
    await _sign_up(backend_client, "lista")
    course = (await backend_client.get(BACKEND)).json()["course"]
    assert course["practicePresets"] == ["lesson", "module", "review", "code-reading", "generators"]
    assert course["practiceScheduler"] == "spaced"


async def test_by_lesson_draws_every_question_of_that_lesson(backend_client: AsyncClient) -> None:
    await _sign_up(backend_client, "leccion")
    drawn = await backend_client.post(f"{BACKEND}/lessons/m01-l02/practice", json={"all": True})
    expected = {(q.exercise_id, q.variant_id) for q in _registry().lesson_questions("m01-l02")}
    assert drawn.status_code == 200
    assert sorted(_keys(drawn.json()["questions"])) == sorted(expected)


async def test_by_module_draws_every_question_of_its_lessons_and_twenty_by_default(
    backend_client: AsyncClient,
) -> None:
    await _sign_up(backend_client, "modulo")
    registry = _registry()
    expected = {
        (q.exercise_id, q.variant_id)
        for lesson in registry.module_lesson_ids("m01")
        for q in registry.lesson_questions(lesson)
    }
    every = await backend_client.post(f"{BACKEND}/modules/m01/practice", json={"all": True})
    assert every.json()["moduleId"] == "m01"
    assert sorted(_keys(every.json()["questions"])) == sorted(expected)
    assert len({lesson for lesson, _ in expected}) > 1
    twenty = _keys((await backend_client.post(f"{BACKEND}/modules/m01/practice")).json()["questions"])
    assert len(twenty) == len(set(twenty)) == 20 and set(twenty) <= expected


async def test_by_module_refuses_a_module_without_questions_and_an_unknown_one(
    backend_client: AsyncClient,
) -> None:
    await _sign_up(backend_client, "vacio")
    empty = await backend_client.post(f"{BACKEND}/modules/m00/practice")
    assert empty.status_code == 409 and empty.json()["code"] == "PRACTICE_EMPTY"
    unknown = await backend_client.post(f"{BACKEND}/modules/m99/practice")
    assert unknown.status_code == 404 and unknown.json()["code"] == "MODULE_NOT_FOUND"


async def test_the_mixed_review_draws_across_modules_from_the_whole_bank(backend_client: AsyncClient) -> None:
    await _sign_up(backend_client, "repaso")
    registry = _registry()
    bank = {
        (q.exercise_id, q.variant_id)
        for _, lesson in registry.manifest.iter_lessons()
        for q in registry.lesson_questions(lesson.id)
    }
    review = _keys(
        (await backend_client.post(f"{BACKEND}/practice/review", json={"count": 100})).json()["questions"]
    )
    assert len(review) == len(set(review)) == 100 and set(review) <= bank
    assert len({registry.exercise_location(exercise) for exercise, _ in review}) > 1


async def test_code_reading_draws_only_and_all_the_questions_that_rest_on_a_snippet(
    backend_client: AsyncClient,
) -> None:
    await _sign_up(backend_client, "codigo")
    registry = _registry()
    expected = {(q.exercise_id, q.variant_id) for q in registry.code_reading_questions()}
    assert 20 < len(expected) <= 100
    drawn = _keys(
        (await backend_client.post(f"{BACKEND}/practice/code-reading", json={"count": 100})).json()[
            "questions"
        ]
    )
    assert sorted(drawn) == sorted(expected)
    assert all(_snippet(registry, exercise, question) for exercise, question in drawn)
    default = _keys((await backend_client.post(f"{BACKEND}/practice/code-reading")).json()["questions"])
    assert len(default) == 20 and set(default) <= expected


async def test_code_reading_follows_the_scheduler_unseen_questions_first(backend_client: AsyncClient) -> None:
    await _sign_up(backend_client, "planificado")
    first = (await backend_client.post(f"{BACKEND}/practice/code-reading", json={"count": 100})).json()[
        "questions"
    ][0]
    await _answer_right(backend_client, first["exerciseId"], first["questionId"])
    again = _keys(
        (await backend_client.post(f"{BACKEND}/practice/code-reading", json={"count": 100})).json()[
            "questions"
        ]
    )
    assert again[-1] == (first["exerciseId"], first["questionId"])


async def test_generators_only_draws_generated_items_of_the_course_generators(
    backend_client: AsyncClient,
) -> None:
    await _sign_up(backend_client, "generadores")
    drawn = (await backend_client.post(f"{BACKEND}/practice/psicotecnicos", json={"count": 26})).json()[
        "exerciseIds"
    ]
    generators = {use.exercise_id for use in _registry().generator_uses()}
    assert len(generators) == 13
    assert len(drawn) == 26 and set(drawn) == generators


async def test_a_course_that_declares_no_presets_refuses_the_new_rounds(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "sinpresets", course="fixture-oposiciones")
    for url in (f"{OPOS}/modules/m01/practice", f"{OPOS}/practice/code-reading"):
        refused = await multi_client.post(url)
        assert refused.status_code == 409 and refused.json()["code"] == "PRACTICE_NOT_AVAILABLE"
    assert "practicePresets" not in (await multi_client.get(OPOS)).json()["course"]


@pytest.mark.parametrize(
    ("preset", "missing"),
    [("lesson", "lesson_practice"), ("review", "practice_scheduler"), ("generators", "practice_generators")],
)
def test_a_preset_without_what_backs_it_is_a_manifest_error(preset: str, missing: str) -> None:
    raw = {
        "id": "x",
        "title": {"en": "X"},
        "subtitle": {"en": "X"},
        "description": {"en": "X"},
        "languages": ["en"],
        "status": "draft",
        "exercise_types": ["quiz"],
        "practice_presets": [preset],
    }
    with pytest.raises(ValidationError, match=missing):
        ManifestCourse.model_validate(raw)


async def test_lesson_practice_is_on_and_every_lesson_with_a_bank_counts_its_questions(
    backend_client: AsyncClient,
) -> None:
    await _sign_up(backend_client, "contadas")
    tree = (await backend_client.get(BACKEND)).json()
    assert tree["course"]["lessonPractice"] is True
    counts = {
        lesson["id"]: lesson["practiceQuestions"]
        for block in tree["blocks"]
        for module in block["modules"]
        for lesson in module["lessons"]
    }
    registry = _registry()
    assert counts == {
        lesson.id: len(registry.lesson_questions(lesson.id)) for _, lesson in registry.manifest.iter_lessons()
    }


async def test_the_design_cases_stay_out_of_every_preset_round(backend_client: AsyncClient) -> None:
    await _sign_up(backend_client, "casos")
    registry = _registry()
    cases = {e for e in registry.scope_exercise_ids("module", "m09") if registry.case_config(e) is not None}
    assert len(cases) == 7  # one per blueprint of programme 9.4
    rounds = [
        await backend_client.post(f"{BACKEND}/lessons/m09-l04/practice", json={"all": True}),
        await backend_client.post(f"{BACKEND}/modules/m09/practice", json={"all": True}),
        await backend_client.post(f"{BACKEND}/practice/review", json={"count": 100}),
        await backend_client.post(f"{BACKEND}/practice/code-reading", json={"count": 100}),
    ]
    assert all(r.status_code == 200 for r in rounds)
    drawn = {q["exerciseId"] for r in rounds for q in r.json()["questions"]}
    assert drawn and not drawn & cases
