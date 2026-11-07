# SPDX-License-Identifier: AGPL-3.0-only
"""Generated items on the fixture course: practice, attempts, a mixed exam part and its results."""

from __future__ import annotations

from collections import Counter

from httpx import AsyncClient

from conftest import FIXTURE_CONTENT
from tradeschool.content.registry import CourseRegistry, load_registry
from tradeschool.exercises.psicotecnico import PsicotecnicoGenerator
from tradeschool.exercises.types import ExerciseType

API = "/api/courses/fixture-oposiciones"
PASSWORD = "correcthorse"


async def _sign_up(client: AsyncClient, name: str) -> None:
    body = {
        "email": f"{name}@example.com",
        "name": name,
        "password": PASSWORD,
        "locale": "es",
        "courses": ["fixture-oposiciones"],
    }
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"email": f"{name}@example.com", "password": PASSWORD})


def _registry() -> CourseRegistry:
    return load_registry(FIXTURE_CONTENT / "fixture-oposiciones")


def _generated(exam: dict[str, object]) -> list[dict[str, object]]:
    questions = exam["questions"]
    assert isinstance(questions, list)
    return [q for q in questions if str(q["exerciseId"]).startswith("gen:")]


async def _start_mixto(client: AsyncClient, seed: int | None = None) -> dict[str, object]:
    response = await client.post(f"{API}/exams", json={"presetId": "mixto", "seed": seed})
    assert response.status_code == 201, response.text
    return dict(response.json())


async def test_the_course_lists_its_psicotecnico_types(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "typelister")
    meta = (await multi_client.get(API)).json()["course"]
    assert [t["generator"] for t in meta["psicotecnicos"]] == ["calculo-ecuaciones", "serie-numerica"]
    assert [t["exerciseId"] for t in meta["psicotecnicos"]] == [
        "gen:calculo-ecuaciones",
        "gen:serie-numerica",
    ]


async def test_a_practice_round_is_one_type_or_every_type_in_the_course_weights(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "roundsman")
    one = await multi_client.post(
        f"{API}/practice/psicotecnicos", json={"generator": "serie-numerica", "count": 3}
    )
    assert one.json()["exerciseIds"] == ["gen:serie-numerica"] * 3
    every = await multi_client.post(f"{API}/practice/psicotecnicos", json={"count": 6})
    assert Counter(every.json()["exerciseIds"]) == {"gen:calculo-ecuaciones": 2, "gen:serie-numerica": 4}
    unknown = await multi_client.post(f"{API}/practice/psicotecnicos", json={"generator": "nope"})
    assert unknown.status_code == 404


async def test_a_generated_attempt_has_a_stable_id_and_reveals_the_rule_after_answering(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "attempter")
    opened = await multi_client.post(f"{API}/exercises/gen:calculo-ecuaciones/attempts")
    assert opened.status_code == 201, opened.text
    attempt = opened.json()
    prefix, generator, seed = attempt["questionId"].split(":")
    assert (prefix, generator) == ("gen", "calculo-ecuaciones") and seed.isdigit()
    assert attempt["type"] == "psicotecnico" and len(attempt["payload"]["options"]) == 4
    assert "correct" not in str(attempt).lower()
    answered = await multi_client.post(
        f"{API}/attempts/{attempt['attemptId']}/answer", json={"answer": {"optionId": "o0"}}
    )
    result = answered.json()
    assert result["correctAnswer"]["optionId"] in {"o0", "o1", "o2", "o3"}
    assert "x =" in result["explanation"]
    replay = (await multi_client.get(f"{API}/attempts/{attempt['attemptId']}")).json()
    assert replay["prompt"] == attempt["prompt"]


async def test_a_mixed_part_draws_stored_and_generated_items_with_one_score_and_types_as_rows(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "mixer")
    exam = await _start_mixto(multi_client, seed=11)
    questions = exam["questions"]
    assert isinstance(questions, list) and len(questions) == 10
    generated = _generated(exam)
    assert Counter(q["exerciseId"] for q in generated) == {
        "gen:calculo-ecuaciones": 2,
        "gen:serie-numerica": 4,
    }
    assert all(q["lessonId"] is None and q["typeTitle"] for q in generated)

    registry = _registry()
    generator = PsicotecnicoGenerator()
    for question in generated:
        config = registry.get_exercise_config(str(question["exerciseId"]))
        assert config is not None and config[0] is ExerciseType.PSICOTECNICO
        seed = int(str(question["questionId"]).rsplit(":", 1)[1])
        correct = generator.grade(config[1], seed, {"optionId": ""}, "es").correct_answer
        assert isinstance(correct, dict)
        await multi_client.post(
            f"{API}/exams/{exam['id']}/questions/{question['attemptId']}/answer",
            json={"answer": {"optionId": correct["optionId"]}},
        )
    submitted = await multi_client.post(f"{API}/exams/{exam['id']}/submit")
    result = submitted.json()
    assert result["result"]["parts"][0]["correct"] == 6
    assert result["result"]["parts"][0]["blank"] == 4
    rows = {
        row["lessonId"]: row
        for group in result["byLesson"]["groups"]
        for row in group["lessons"]
        if row.get("kind") == "type"
    }
    assert {k: (r["title"], r["questions"], r["correct"]) for k, r in rows.items()} == {
        "gen:calculo-ecuaciones": ("Ecuaciones", 2, 2),
        "gen:serie-numerica": ("Series numéricas", 4, 4),
    }
    review = (await multi_client.get(f"{API}/exams/{exam['id']}/review")).json()
    assert all(q["correctAnswer"] and q["explanation"] for q in _generated(review))


async def test_the_same_seed_regenerates_the_same_mixed_paper(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "replayer")
    first = _generated(await _start_mixto(multi_client, seed=3))
    again = _generated(await _start_mixto(multi_client, seed=3))
    assert [(q["exerciseId"], q["prompt"], q["payload"]) for q in first] == [
        (q["exerciseId"], q["prompt"], q["payload"]) for q in again
    ]


async def test_progress_counts_practised_items_per_type(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "practiser")
    for _ in range(3):
        opened = (await multi_client.post(f"{API}/exercises/gen:serie-numerica/attempts")).json()
        await multi_client.post(
            f"{API}/attempts/{opened['attemptId']}/answer", json={"answer": {"optionId": "o0"}}
        )
    table = (await multi_client.get(f"{API}/stats/me/by-lesson")).json()
    group = next(g for g in table["groups"] if g["moduleId"] == "psicotecnicos")
    assert group["title"] == "Psicotécnicos"
    (row,) = group["lessons"]
    assert (row["lessonId"], row["title"], row["questions"], row["kind"]) == (
        "gen:serie-numerica",
        "Series numéricas",
        3,
        "type",
    )
    assert table["lists"] is None  # one type is no ranking
