# SPDX-License-Identifier: AGPL-3.0-only
"""PDF export per tema and per bloque (delta N): the scoped export, the questionnaire, the account switch."""

from __future__ import annotations

import asyncio
import json
import os
import uuid
from typing import Any

import pytest
from alembic import command
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from conftest import FIXTURE_CONTENT, REPO_CONTENT, real_course
from tradeschool.config import Settings
from tradeschool.content.registry import CourseRegistry, load_registry
from tradeschool.exams.questionnaire import QUESTIONS_PER_TEMA, build_questionnaire
from tradeschool.migrations import alembic_config

OPOS = "/api/courses/fixture-oposiciones"
PASSWORD = "correcthorse"
BEFORE_SWITCH = "a2b3c4d5e6f7"


@pytest.fixture(scope="module")
def opos() -> CourseRegistry:
    return load_registry(FIXTURE_CONTENT / "fixture-oposiciones")


@pytest.fixture
def c2() -> CourseRegistry:
    return real_course("age-auxiliar-c2")


async def _sign_up(client: AsyncClient, name: str = "reader") -> None:
    email = f"{name}@example.com"
    body = {"email": email, "password": PASSWORD, "locale": "es", "courses": ["fixture-oposiciones"]}
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"email": email, "password": PASSWORD})


def _lesson_ids(doc: dict[str, Any]) -> list[str]:
    return [
        lesson["id"] for block in doc["blocks"] for module in block["modules"] for lesson in module["lessons"]
    ]


async def test_a_bloque_scope_exports_only_that_module_inside_its_block(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client)
    doc = (await multi_client.get(f"{OPOS}/export", params={"lang": "es", "scope": "m02"})).json()
    assert [b["id"] for b in doc["blocks"]] == ["block-a"]
    assert [m["id"] for m in doc["blocks"][0]["modules"]] == ["m02"]
    assert _lesson_ids(doc) == ["m02-l1", "m02-l2"]
    assert (
        doc["glossary"]
        == (await multi_client.get(f"{OPOS}/export", params={"lang": "es"})).json()["glossary"]
    )


async def test_a_tema_scope_exports_only_that_lesson(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client)
    doc = (await multi_client.get(f"{OPOS}/export", params={"lang": "es", "scope": "m01-l2"})).json()
    assert [m["id"] for b in doc["blocks"] for m in b["modules"]] == ["m01"]
    assert _lesson_ids(doc) == ["m01-l2"]
    every = (await multi_client.get(f"{OPOS}/export", params={"lang": "all", "scope": "m01-l2"})).json()
    assert _lesson_ids(every) == ["m01-l2"]


async def test_no_scope_still_exports_the_whole_course(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client)
    doc = (await multi_client.get(f"{OPOS}/export", params={"lang": "es"})).json()
    assert _lesson_ids(doc) == ["m01-l1", "m01-l2", "m02-l1", "m02-l2"]


async def test_an_unknown_scope_is_a_404_naming_it(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client)
    for path in ("/export", "/print/questionnaire"):
        response = await multi_client.get(f"{OPOS}{path}", params={"lang": "es", "scope": "m09-l01"})
        assert response.status_code == 404
        assert response.json()["code"] == "EXPORT_SCOPE_NOT_FOUND"
        assert "m09-l01" in response.json()["message"]


async def test_a_language_the_course_lacks_is_refused_as_today(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client)
    response = await multi_client.get(f"{OPOS}/export", params={"lang": "en", "scope": "m01"})
    assert response.status_code == 404
    assert response.json()["code"] == "LANGUAGE_NOT_AVAILABLE"


async def test_the_questionnaire_returns_its_seed_and_redraws_the_same_paper_from_it(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client)
    first = (
        await multi_client.get(f"{OPOS}/print/questionnaire", params={"lang": "es", "scope": "m01"})
    ).json()
    again = (
        await multi_client.get(
            f"{OPOS}/print/questionnaire", params={"lang": "es", "scope": "m01", "seed": first["seed"]}
        )
    ).json()
    assert again == first
    assert [t["lessonId"] for t in first["temas"]] == ["m01-l1", "m01-l2"]


def test_the_questions_drawn_for_a_seed_are_fixed_and_lettered_in_printed_order(opos: CourseRegistry) -> None:
    paper = build_questionnaire(opos, opos.export_scope("m02-l1"), "es", seed=7)
    assert paper == build_questionnaire(opos, opos.export_scope("m02-l1"), "es", seed=7)
    tema = paper["temas"][0]
    assert tema["lessonId"] == "m02-l1"
    assert [q["number"] for q in tema["questions"]] == [k["number"] for k in tema["keys"]]
    for question, key in zip(tema["questions"], tema["keys"], strict=True):
        letters = [option["letter"] for option in question["options"]]
        assert letters == ["A", "B", "C", "D"][: len(letters)]
        assert key["letter"] in letters


def test_a_tema_prints_the_same_questions_alone_and_inside_its_bloque(opos: CourseRegistry) -> None:
    alone = build_questionnaire(opos, opos.export_scope("m02-l1"), "es", seed=11)["temas"][0]
    bloque = build_questionnaire(opos, opos.export_scope("m02"), "es", seed=11)["temas"]
    assert next(t for t in bloque if t["lessonId"] == "m02-l1") == alone


def test_a_tema_prints_at_most_twenty_questions(c2: CourseRegistry) -> None:
    paper = build_questionnaire(c2, None, "es", seed=3)
    assert paper["temas"]
    assert all(0 < len(t["questions"]) <= QUESTIONS_PER_TEMA for t in paper["temas"])
    assert any(len(t["questions"]) == QUESTIONS_PER_TEMA for t in paper["temas"])
    cited = [k for t in paper["temas"] for k in t["keys"]]
    assert all(k["citation"] for k in cited), "every printed key cites its answer"


def test_official_and_calibration_items_are_never_printed(c2: CourseRegistry) -> None:
    # m00-l01 holds only the official papers, ps-l01 only the calibration items.
    assert c2.is_official("ofi-conv2025-a") and c2.is_official("ps-calibracion")
    assert build_questionnaire(c2, c2.export_scope("m00-l01"), "es", seed=1)["temas"] == []
    assert build_questionnaire(c2, c2.export_scope("ps-l01"), "es", seed=1)["temas"] == []
    printed = {
        q["id"].split("/")[0]
        for t in build_questionnaire(c2, None, "es", seed=1)["temas"]
        for q in t["questions"]
    }
    assert not {e for e in printed if c2.is_official(e)}


async def test_a_new_account_exports_theory_only_until_it_switches_exercises_on(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client)
    assert (await multi_client.get("/api/auth/me")).json()["pdf_exercises"] is False
    switched = await multi_client.patch("/api/auth/me", json={"pdf_exercises": True})
    assert switched.json()["pdf_exercises"] is True
    assert (await multi_client.get("/api/auth/me")).json()["pdf_exercises"] is True


def test_an_account_from_before_the_migration_starts_with_the_switch_off(
    settings: Settings, _migrated: bool
) -> None:
    config = alembic_config(settings.database_url)
    user_id = uuid.uuid4()

    async def run(sql: str, **params: object) -> list[Any]:
        engine = create_async_engine(settings.database_url)
        try:
            async with engine.begin() as conn:
                result = await conn.execute(text(sql), params)
                return list(result.all()) if result.returns_rows else []
        finally:
            await engine.dispose()

    command.downgrade(config, BEFORE_SWITCH)
    try:
        asyncio.run(
            run(
                'INSERT INTO "user" (id, email, hashed_password, is_active, is_superuser, is_verified) '
                "VALUES (:id, 'older@example.com', 'x', true, false, false)",
                id=user_id,
            )
        )
    finally:
        command.upgrade(config, "head")
    try:
        rows = asyncio.run(run('SELECT pdf_exercises FROM "user" WHERE id = :id', id=user_id))
        assert rows == [(False,)]
    finally:
        asyncio.run(run('DELETE FROM "user" WHERE id = :id', id=user_id))


# One tema per oposiciones course, drawn with a fixed seed: the frontend's definition tests print these.
PINNED_SEED = 2026
PINNED_TEMA = "m01-l01"
PINNED_DIR = REPO_CONTENT.parent / "frontend" / "src" / "test" / "fixtures" / "questionnaires"


@pytest.mark.parametrize("slug", ["age-administrativo-c1", "age-auxiliar-c2", "aeat-agentes-hacienda"])
def test_the_pinned_questionnaire_the_frontend_prints_is_this_seeds_draw(slug: str) -> None:
    registry = real_course(slug)
    assert registry.manifest.course.pdf_exercises, f"{slug} must be able to print exercises (N9)"
    paper = build_questionnaire(registry, registry.export_scope(PINNED_TEMA), "es", seed=PINNED_SEED)
    tema = paper["temas"][0]
    assert len(tema["questions"]) == QUESTIONS_PER_TEMA
    assert all(key["citation"] for key in tema["keys"])
    pinned = PINNED_DIR / f"{slug}-{PINNED_TEMA}.json"
    rendered = json.dumps(paper, ensure_ascii=False, indent=2) + "\n"
    if os.environ.get("REGEN_QUESTIONNAIRES"):
        pinned.write_text(rendered, encoding="utf-8")
    assert pinned.read_text(encoding="utf-8") == rendered, (
        f"{pinned.name} is stale: rerun with REGEN_QUESTIONNAIRES=1 and review the diff"
    )


def test_c2_generated_psicotecnicos_are_never_drawn_into_a_tema(c2: CourseRegistry) -> None:
    assert c2.generator_uses(), "C2 declares generated psicotécnicos"
    drawn = {q["id"] for t in build_questionnaire(c2, None, "es", seed=9)["temas"] for q in t["questions"]}
    generated = {use.exercise_id for use in c2.generator_uses()}
    assert not {i for i in drawn if i.split("/")[0] in generated}
    assert all("/" in i for i in drawn), "every printed question is a stored variant"
