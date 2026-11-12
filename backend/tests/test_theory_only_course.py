# SPDX-License-Identifier: AGPL-3.0-only
"""A published course with no exercises and no exams (delta v2.1, section M): loaded, listed, readable."""

from __future__ import annotations

from httpx import AsyncClient

from conftest import FIXTURE_CONTENT
from tradeschool.content.registry import load_registry
from tradeschool.content.schema import CourseStatus

THEORY = "/api/courses/fixture-teoria"
PASSWORD = "correcthorse"


async def _sign_up(client: AsyncClient, name: str, courses: list[str]) -> None:
    body = {
        "email": f"{name}@example.com",
        "name": name,
        "password": PASSWORD,
        "locale": "es",
        "courses": courses,
    }
    assert (await client.post("/api/auth/register", json=body)).status_code == 201
    login = {"email": body["email"], "password": PASSWORD}
    assert (await client.post("/api/auth/login", json=login)).status_code == 200


def test_the_loader_accepts_a_published_course_with_an_empty_exercise_types() -> None:
    registry = load_registry(FIXTURE_CONTENT / "fixture-teoria")
    assert registry.manifest.course.status is CourseStatus.PUBLISHED
    assert registry.manifest.course.exercise_types == []
    assert registry.theory_only


async def test_the_catalogue_lists_it_and_sign_up_accepts_it(multi_client: AsyncClient) -> None:
    catalogue = (await multi_client.get("/api/courses?lang=es")).json()
    assert "fixture-teoria" in [course["slug"] for course in catalogue]
    await _sign_up(multi_client, "reader", ["fixture-teoria"])
    mine = (await multi_client.get("/api/me/courses")).json()
    assert mine["active"] == ["fixture-teoria"]


async def test_its_course_page_says_theory_only_and_has_no_practice(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "reader2", ["fixture-teoria"])
    course = (await multi_client.get(f"{THEORY}?lang=es")).json()
    assert course["course"]["theoryOnly"] is True
    lessons = [lesson for block in course["blocks"] for m in block["modules"] for lesson in m["lessons"]]
    assert len(lessons) == 2
    assert all("practiceQuestions" not in lesson for lesson in lessons)
    assert (await multi_client.get(f"{THEORY}/exams/presets?lang=es")).json() == []
    assert (await multi_client.get(f"{THEORY}/exams/open")).json() == []


async def test_a_course_with_exercises_is_not_theory_only(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "reader3", ["fixture-oposiciones"])
    course = (await multi_client.get("/api/courses/fixture-oposiciones?lang=es")).json()
    assert "theoryOnly" not in course["course"]


async def test_its_progress_counts_reading_only(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "reader4", ["fixture-teoria"])
    stats = (await multi_client.get(f"{THEORY}/stats/me?lang=es")).json()
    assert stats["reading"]["lessonsTotal"] == 2
    assert stats["exercise"]["answered"] == 0
    assert stats["costliestSections"] == []


async def test_its_pdf_data_prints_every_lesson_and_no_exercise(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "reader5", ["fixture-teoria"])
    printed = (await multi_client.get(f"{THEORY}/print/exercises?lang=es")).json()
    assert [lesson["exercises"] for lesson in printed["lessons"]] == [[], []]
