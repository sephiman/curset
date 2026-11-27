# SPDX-License-Identifier: AGPL-3.0-only
"""Question families: a practice set serves at most two of one family, seen variant by variant."""

from __future__ import annotations

import random
import shutil
from collections import Counter
from pathlib import Path

import pytest
from httpx import AsyncClient

from conftest import FIXTURE_CONTENT
from tradeschool.content.registry import CourseRegistry, load_registry
from tradeschool.exercises.quiz import QuizConfig
from tradeschool.practice import service

FAMILIES = "/api/courses/fixture-familias"
OPOS = "/api/courses/fixture-oposiciones"
STORED_FAMILY = {
    "iso-a": "iso",
    "iso-b": "iso",
    "iso-c": "iso",
    "trace-a": "tracing",
    "trace-b": "tracing",
    "trace-c": "tracing",
}
DRAWS = 12


def _family(question: dict[str, str]) -> str | None:
    if question["exerciseId"].startswith("gen:"):
        return question["exerciseId"].removeprefix("gen:")
    return STORED_FAMILY.get(question["questionId"])


def _per_family(questions: list[dict[str, str]]) -> Counter[str]:
    return Counter(family for q in questions if (family := _family(q)) is not None)


async def _sign_up(client: AsyncClient, name: str) -> None:
    email = f"{name}@example.com"
    body = {
        "email": email,
        "name": name,
        "password": "correcthorse",
        "locale": "en",
        "courses": ["fixture-familias"],
    }
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"email": email, "password": "correcthorse"})


async def _draw(
    client: AsyncClient, path: str, body: dict[str, object] | None = None
) -> list[dict[str, str]]:
    response = await client.post(f"{FAMILIES}{path}", json=body or {})
    assert response.status_code == 200, response.text
    return response.json()["questions"]


@pytest.fixture(scope="module")
def registry() -> CourseRegistry:
    return load_registry(FIXTURE_CONTENT / "fixture-familias")


def test_a_variant_carries_its_family_and_the_dump_leaves_it_out(registry: CourseRegistry) -> None:
    config = registry.exercise_configs["m01-ex-1"][1]
    assert isinstance(config, QuizConfig)
    assert {v.id: v.family for v in config.variants}["iso-b"] == "iso"
    assert all(
        "family" not in v and "code_reading" not in v for v in config.model_dump(mode="json")["variants"]
    )
    assert {q.variant_id: q.family for q in registry.lesson_questions("m01-l1")}["trace-c"] == "tracing"


async def test_a_lesson_set_holds_at_most_two_of_a_family_and_mixes_stored_and_generated(
    families_client: AsyncClient,
) -> None:
    await _sign_up(families_client, "leccion")
    for _ in range(DRAWS):
        drawn = await _draw(families_client, "/lessons/m01-l1/practice", {"all": True})
        counts = _per_family(drawn)
        assert counts == {"iso": 2, "tracing": 2, "capacity-estimation": 2, "loop-complexity": 2}
        assert sum(q["questionId"] == "plain-a" for q in drawn) == 1
        assert len(drawn) == 9


async def test_a_family_is_seen_per_variant_so_unseen_variants_come_before_a_seen_one(
    families_client: AsyncClient,
) -> None:
    await _sign_up(families_client, "vistas")
    opened = await families_client.post(
        f"{FAMILIES}/exercises/m01-ex-1/attempts", json={"variantId": "iso-a"}
    )
    await families_client.post(
        f"{FAMILIES}/attempts/{opened.json()['attemptId']}/answer",
        json={"answer": {"optionId": "a"}},
    )
    for _ in range(DRAWS):
        drawn = await _draw(families_client, "/lessons/m01-l1/practice", {"all": True})
        ids = {q["questionId"] for q in drawn}
        assert {"iso-b", "iso-c"} <= ids and "iso-a" not in ids


async def test_module_and_review_sets_cap_each_family_and_still_mix_the_three_kinds(
    families_client: AsyncClient,
) -> None:
    await _sign_up(families_client, "mezcla")
    for path, body in (("/modules/m01/practice", {"all": True}), ("/practice/review", {"count": 100})):
        drawn = await _draw(families_client, path, body)
        assert max(_per_family(drawn).values()) == 2
        assert any(q["exerciseId"].startswith("gen:") for q in drawn)
        assert any(q["questionId"] in STORED_FAMILY for q in drawn)
        assert any(q["questionId"] == "plain-a" for q in drawn)


async def test_code_reading_takes_a_flagged_family_whole_and_the_generated_family_flagged_for_it(
    families_client: AsyncClient,
) -> None:
    await _sign_up(families_client, "codigo")
    for _ in range(DRAWS):
        drawn = await _draw(families_client, "/practice/code-reading", {"count": 100})
        assert _per_family(drawn) == {"tracing": 2, "loop-complexity": 2}
        assert {q["questionId"] for q in drawn if q["exerciseId"] == "m01-ex-1"} <= {
            "trace-a",
            "trace-b",
            "trace-c",
        }


async def test_a_generators_set_caps_each_family_but_a_chosen_type_is_not_capped(
    families_client: AsyncClient,
) -> None:
    await _sign_up(families_client, "generadores")
    every = (await families_client.post(f"{FAMILIES}/practice/psicotecnicos", json={"count": 20})).json()
    assert Counter(every["exerciseIds"]) == {"gen:capacity-estimation": 2, "gen:loop-complexity": 2}
    one = await families_client.post(
        f"{FAMILIES}/practice/psicotecnicos", json={"count": 5, "generator": "loop-complexity"}
    )
    assert one.json()["exerciseIds"] == ["gen:loop-complexity"] * 5


def test_the_generators_preset_draws_from_every_declared_generator_not_a_fixed_thirteen(
    tmp_path: Path,
) -> None:
    course = shutil.copytree(FIXTURE_CONTENT / "fixture-familias", tmp_path / "fixture-familias")
    manifest = course / "course.yaml"
    manifest.write_text(
        manifest.read_text().replace(
            "blocks:\n",
            "  - generator: quorum-reads\n    title:\n      en: Quorums\n    weight: 1\n"
            "    difficulty: {1: 1, 2: 1}\nblocks:\n",
            1,
        )
    )
    grown = load_registry(course)
    drawn = service.draw_generated_round(grown, None, 30, random.Random(1))
    assert Counter(drawn) == {"gen:capacity-estimation": 2, "gen:loop-complexity": 2, "gen:quorum-reads": 2}


async def test_the_lesson_page_names_the_generated_families_that_practise_it(
    families_client: AsyncClient,
) -> None:
    await _sign_up(families_client, "pagina")
    lesson = (await families_client.get(f"{FAMILIES}/lessons/m01-l1")).json()
    assert lesson["generatedFamilies"] == [
        {"id": "capacity-estimation", "title": "Capacity estimation"},
        {"id": "loop-complexity", "title": "Loop complexity"},
    ]


async def test_a_course_without_the_generators_preset_serves_no_generated_families(
    client: AsyncClient,
) -> None:
    body = {
        "email": "sin@example.com",
        "name": "sin",
        "password": "correcthorse",
        "locale": "es",
        "courses": ["fixture-oposiciones"],
    }
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"email": "sin@example.com", "password": "correcthorse"})
    assert "generatedFamilies" not in (await client.get(f"{OPOS}/lessons/m02-l1")).json()
