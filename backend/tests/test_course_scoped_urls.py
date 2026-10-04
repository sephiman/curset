# SPDX-License-Identifier: AGPL-3.0-only
"""Course-scoped URLs: the only scheme, the retired unscoped aliases, and an unknown slug."""

from __future__ import annotations

import pytest
from httpx import AsyncClient

COURSE = "crypto-futures"
CREDS = {"username": "scoped", "password": "correcthorse"}

# Every unscoped alias the previous version served, retired in this one (R9.3).
RETIRED_ALIASES = [
    "/api/course",
    "/api/course/export?lang=es",
    "/api/course/print/exercises?lang=es",
    "/api/glossary?lang=es",
    "/api/lessons/m01-l1",
    "/api/modules/m01",
    "/api/exams",
    "/api/exams/open",
    "/api/stats/me",
    "/api/stats/global",
]


async def _auth(client: AsyncClient) -> None:
    await client.post("/api/auth/register", json={**CREDS, "locale": "en"})
    await client.post("/api/auth/login", json=CREDS)


@pytest.mark.parametrize("alias", RETIRED_ALIASES)
async def test_retired_unscoped_alias_is_gone(content_client: AsyncClient, alias: str) -> None:
    await _auth(content_client)
    assert (await content_client.get(alias)).status_code == 404


async def test_scoped_urls_require_auth_like_everything_else(content_client: AsyncClient) -> None:
    assert (await content_client.get(f"/api/courses/{COURSE}/glossary")).status_code == 401


async def test_unknown_course_slug_404s_cleanly(content_client: AsyncClient) -> None:
    await _auth(content_client)
    for path in ("", "/glossary", "/lessons/m01-l1", "/export", "/exams", "/stats/me"):
        response = await content_client.get(f"/api/courses/no-such-course{path}")
        assert response.status_code == 404, path
        assert response.json()["code"] == "COURSE_NOT_FOUND", path


async def test_an_unknown_slug_404s_before_the_resource_is_even_looked_up(
    content_client: AsyncClient,
) -> None:
    """A wrong course plus a wrong lesson is a course miss, not a lesson miss — the scope resolves first."""
    await _auth(content_client)
    response = await content_client.get("/api/courses/no-such-course/lessons/no-such-lesson")
    assert response.json()["code"] == "COURSE_NOT_FOUND"


async def test_course_owned_paths_are_all_scoped(content_client: AsyncClient) -> None:
    schema = (await content_client.get("/api/openapi.json")).json()
    global_prefixes = ("/api/auth", "/api/health", "/api/version", "/api/me/courses")
    course_owned = [p for p in schema["paths"] if not p.startswith(global_prefixes) and p != "/api/courses"]
    assert course_owned, "no course-owned paths in the schema"
    assert all(p.startswith("/api/courses/{course}") for p in course_owned), course_owned
