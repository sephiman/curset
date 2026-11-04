# SPDX-License-Identifier: AGPL-3.0-only
"""A seeded exam start: the same seed draws the same sitting, and only a dev-mode server takes one."""

from __future__ import annotations

from collections.abc import AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient

from conftest import _build_client
from tradeschool.config import Settings

API = "/api/courses/crypto-futures"
CREDS = {"email": "seeded@example.com", "password": "correcthorse"}


async def _auth(client: AsyncClient) -> None:
    await client.post("/api/auth/register", json={**CREDS, "locale": "en"})
    await client.post("/api/auth/login", json=CREDS)


def _drawn(exam: dict[str, object]) -> list[tuple[object, object, object]]:
    questions = exam["questions"]
    assert isinstance(questions, list)
    return [(q["exerciseId"], q["prompt"], q["payload"]) for q in questions]


async def _start(client: AsyncClient, seed: int) -> dict[str, object]:
    response = await client.post(f"{API}/exams", json={"presetId": "global", "seed": seed})
    assert response.status_code == 201, response.text
    body = response.json()
    assert isinstance(body, dict)
    return body


async def test_the_same_seed_draws_the_same_sitting(content_client: AsyncClient) -> None:
    await _auth(content_client)
    first = await _start(content_client, 7)
    again = await _start(content_client, 7)
    assert first["id"] != again["id"]
    assert _drawn(first) == _drawn(again)


async def test_another_seed_draws_another_sitting(content_client: AsyncClient) -> None:
    await _auth(content_client)
    assert _drawn(await _start(content_client, 7)) != _drawn(await _start(content_client, 8))


@pytest_asyncio.fixture
async def production_client(settings: Settings, _migrated: bool) -> AsyncGenerator[AsyncClient]:
    async with _build_client(settings.model_copy(update={"dev_mode": False}), reconcile_content=True) as http:
        yield http


async def test_a_seed_is_refused_outside_dev_mode(production_client: AsyncClient) -> None:
    await _auth(production_client)
    response = await production_client.post(f"{API}/exams", json={"presetId": "global", "seed": 7})
    assert response.status_code == 403
    assert response.json()["code"] == "EXAM_SEED_DEV_ONLY"
