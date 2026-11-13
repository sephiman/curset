# SPDX-License-Identifier: AGPL-3.0-only
"""Judgement callouts and licensed extracts (platform deltas N2, N3) of a technical-source course."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
from httpx import AsyncClient

from conftest import FIXTURE_CONTENT
from tradeschool.content.registry import ContentError, load_registry

TECH = "/api/courses/fixture-tecnico"
PASSWORD = "correcthorse"
LESSON = "en/lessons/m01-l1.md"
JUDGEMENT = '{source="Google, Site Reliability Engineering, ch. 17" ref="sre-book#ch17"}'


@pytest.fixture
def course(tmp_path: Path) -> Path:
    copy = tmp_path / "fixture-tecnico"
    shutil.copytree(FIXTURE_CONTENT / "fixture-tecnico", copy)
    return copy


def _replace(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    assert old in text
    path.write_text(text.replace(old, new), encoding="utf-8")


def test_the_fixture_course_loads(course: Path) -> None:
    assert load_registry(course).tech is not None


@pytest.mark.parametrize(
    ("attributes", "problem"),
    [
        ('{ref="sre-book#ch17"}', "`source` is required"),
        ('{source=" "}', "`source` is required"),
        ("", "`source` is required"),
        ('{source="Someone" mood="grim"}', "unknown attribute mood"),
        ('{source="Someone" ref="not a citation"}', "is not source_id#anchor"),
        ('{source="Someone" ref="sre-book#nope"}', "no anchor «nope» in sre-book"),
        ('{source="Someone" ref="unknown#x"}', "unknown source «unknown»"),
        ("{source=Someone}", 'name="value" pairs'),
    ],
)
def test_a_malformed_judgement_stops_the_load(course: Path, attributes: str, problem: str) -> None:
    _replace(course / LESSON, f":::judgement{JUDGEMENT}", f":::judgement{attributes}")
    with pytest.raises(ContentError, match="lesson m01-l1, judgement") as raised:
        load_registry(course)
    assert problem in str(raised.value)


def test_a_judgement_without_a_ref_is_valid(course: Path) -> None:
    _replace(course / LESSON, f":::judgement{JUDGEMENT}", ':::judgement{source="Google, SRE"}')
    load_registry(course)


def test_a_judgement_shown_inside_a_code_block_is_not_checked(course: Path) -> None:
    _replace(course / LESSON, "```yaml", "```text\n:::judgement\n```\n\n```yaml")
    load_registry(course)


def test_an_extract_on_a_source_that_allows_none_stops_the_load(course: Path) -> None:
    exercise = course / "exercises" / "m01-ex-1.yaml"
    _replace(
        exercise, 'citation: "sre-book#ch17"', 'citation: "sre-book#ch17"\n    extract:\n      en: "quoted"'
    )
    with pytest.raises(ContentError, match=r"m01-ex-1/tests-that-fail quotes sre-book.*CC BY-NC-ND 4.0"):
        load_registry(course)


def test_an_extract_whose_citation_names_no_registered_source_stops_the_load(course: Path) -> None:
    _replace(
        course / "exercises" / "m01-ex-1.yaml", 'citation: "pg-iso#XACT-READ-COMMITTED"', 'citation: "gone#a"'
    )
    with pytest.raises(ContentError, match="names no registered source"):
        load_registry(course)


def test_a_snippet_that_is_not_a_file_of_the_course_stops_the_load(course: Path) -> None:
    _replace(
        course / "exercises" / "m01-ex-1.yaml",
        "    extract:",
        "    snippet: m01-l1/LostUpdate.java\n    extract:",
    )
    with pytest.raises(ContentError, match=r"snippet m01-l1/LostUpdate\.java, which is not in snippets/"):
        load_registry(course)
    snippets = course / "snippets" / "m01-l1"
    snippets.mkdir(parents=True)
    (snippets / "LostUpdate.java").write_text("class LostUpdate {}\n", encoding="utf-8")
    load_registry(course)


async def _sign_up(client: AsyncClient, name: str) -> None:
    body = {
        "email": f"{name}@example.com",
        "name": name,
        "password": PASSWORD,
        "locale": "en",
        "courses": ["fixture-tecnico"],
    }
    assert (await client.post("/api/auth/register", json=body)).status_code == 201
    login = {"email": body["email"], "password": PASSWORD}
    assert (await client.post("/api/auth/login", json=login)).status_code == 200


async def _solved(client: AsyncClient, variant_id: str) -> dict[str, object]:
    opened = await client.post(f"{TECH}/exercises/m01-ex-1/attempts", json={"variantId": variant_id})
    assert opened.status_code == 201, opened.text
    graded = await client.post(
        f"{TECH}/attempts/{opened.json()['attemptId']}/answer", json={"answer": {"optionId": "a"}}
    )
    assert graded.status_code == 200, graded.text
    body: dict[str, object] = graded.json()
    return body


async def test_the_solution_quotes_a_source_whose_licence_allows_it(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "quoter")
    graded = await _solved(multi_client, "isolation-quote")
    assert graded["noExcerpt"] is None
    assert graded["excerpt"] == {
        "heading": "PostgreSQL transaction isolation (XACT-READ-COMMITTED)",
        "text": "Read Committed is the default isolation level in PostgreSQL.",
        "full": None,
        "fullTooLong": False,
        "href": "https://www.postgresql.org/docs/current/transaction-iso.html",
        "attribution": "Licence: PostgreSQL",
    }


async def test_the_solution_quotes_nothing_from_a_source_whose_licence_forbids_it(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "abstainer")
    graded = await _solved(multi_client, "tests-that-fail")
    assert graded["excerpt"] is None
    assert graded["noExcerpt"] == {
        "reason": "licence",
        "href": "https://sre.google/sre-book/table-of-contents/",
        "detail": "CC BY-NC-ND 4.0",
    }


async def test_other_courses_keep_their_payload_without_a_detail(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "bystander")
    opened = await multi_client.post("/api/courses/fixture-oposiciones/exercises/m01-ex-1/attempts")
    graded = await multi_client.post(
        f"/api/courses/fixture-oposiciones/attempts/{opened.json()['attemptId']}/answer",
        json={"answer": {"optionId": "a"}},
    )
    body = graded.json()
    assert "detail" not in (body["noExcerpt"] or {})
    assert "extract" not in body and "snippet" not in body
