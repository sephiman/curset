# SPDX-License-Identifier: AGPL-3.0-only
"""Several courses side by side: catalogue, active/selected courses, reading language, isolation.

The fixture course `fixture-oposiciones` is Spanish-only and reuses crypto-futures' ids (m01, m01-l1,
m01-ex-1), so any leak between courses shows up as the wrong course's row.
"""

from __future__ import annotations

from httpx import AsyncClient

CRYPTO = "/api/courses/crypto-futures"
OPOS = "/api/courses/fixture-oposiciones"
PASSWORD = "correcthorse"


async def _sign_up(
    client: AsyncClient, username: str, locale: str = "en", courses: list[str] | None = None
) -> None:
    body = {"username": username, "password": PASSWORD, "locale": locale, "courses": courses or []}
    assert (await client.post("/api/auth/register", json=body)).status_code == 201
    assert (
        await client.post("/api/auth/login", json={"username": username, "password": PASSWORD})
    ).status_code == 200


async def _answer_opos_quiz(client: AsyncClient, correct: bool) -> str:
    opened = (await client.post(f"{OPOS}/exercises/m01-ex-1/attempts")).json()
    option = "a" if correct else "b"
    graded = await client.post(
        f"{OPOS}/attempts/{opened['attemptId']}/answer", json={"answer": {"optionId": option}}
    )
    assert graded.json()["correct"] is correct
    return str(opened["attemptId"])


async def test_catalogue_lists_published_courses_alphabetically_and_hides_drafts(
    multi_client: AsyncClient,
) -> None:
    catalogue = (await multi_client.get("/api/courses?lang=en")).json()
    assert [course["slug"] for course in catalogue] == ["fixture-oposiciones", "crypto-futures"]
    spanish_only = catalogue[0]
    assert spanish_only["languages"] == ["es"]
    # The account is English, the course has no English: its own title comes in Spanish, and says so.
    assert spanish_only["textLocale"] == "es"
    assert spanish_only["title"] == "Administración pública de prueba"


async def test_a_draft_course_is_served_to_nobody(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "drafty")
    response = await multi_client.get("/api/courses/fixture-borrador")
    assert response.status_code == 404
    assert response.json()["code"] == "COURSE_NOT_FOUND"
    signup = await multi_client.post(
        "/api/auth/register",
        json={"username": "drafty2", "password": PASSWORD, "courses": ["fixture-borrador"]},
    )
    assert signup.status_code == 404


async def test_sign_up_activates_the_ticked_courses_and_none_is_allowed(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "none-ticked")
    mine = (await multi_client.get("/api/me/courses")).json()
    assert mine["active"] == [] and mine["selected"] is None

    await _sign_up(multi_client, "both-ticked", courses=["crypto-futures", "fixture-oposiciones"])
    mine = (await multi_client.get("/api/me/courses")).json()
    assert mine["active"] == ["fixture-oposiciones", "crypto-futures"]
    assert mine["selected"] == "fixture-oposiciones"  # the first active course alphabetically


async def test_disabling_the_viewed_course_moves_to_the_next_and_then_to_none(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "switcher", courses=["crypto-futures", "fixture-oposiciones"])
    both = {"active": ["crypto-futures", "fixture-oposiciones"], "selected": "fixture-oposiciones"}
    assert (await multi_client.put("/api/me/courses", json=both)).json()["selected"] == "fixture-oposiciones"

    only_crypto = {"active": ["crypto-futures"], "selected": "fixture-oposiciones"}
    moved = (await multi_client.put("/api/me/courses", json=only_crypto)).json()
    assert moved["active"] == ["crypto-futures"] and moved["selected"] == "crypto-futures"

    nothing = (
        await multi_client.put("/api/me/courses", json={"active": [], "selected": "crypto-futures"})
    ).json()
    assert nothing["active"] == [] and nothing["selected"] is None


async def test_disabling_and_re_enabling_keeps_progress_attempts_and_exams(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "returner", courses=["fixture-oposiciones"])
    assert (await multi_client.post(f"{OPOS}/lessons/m01-l1/complete")).status_code == 200
    await _answer_opos_quiz(multi_client, correct=True)
    exam = (await multi_client.post(f"{OPOS}/exams", json={"scope": "global"})).json()

    await multi_client.put("/api/me/courses", json={"active": []})
    await multi_client.put("/api/me/courses", json={"active": ["fixture-oposiciones"]})

    course = (await multi_client.get(OPOS)).json()
    lesson = course["blocks"][0]["modules"][0]["lessons"][0]
    assert lesson["completed"] is True
    assert course["blocks"][0]["modules"][0]["exercisesPassed"] == 1
    assert [e["id"] for e in (await multi_client.get(f"{OPOS}/exams/open")).json()] == [exam["id"]]


async def test_an_english_account_reads_a_spanish_only_course_in_spanish(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "reader", locale="en", courses=["fixture-oposiciones"])
    lesson = (await multi_client.get(f"{OPOS}/lessons/m01-l1")).json()
    assert lesson["title"] == "El recurso de alzada"
    course = (await multi_client.get(OPOS)).json()
    assert course["locale"] == "es" and course["languages"] == ["es"]
    assert (await multi_client.get("/api/me/courses")).json()["readingLanguages"][
        "fixture-oposiciones"
    ] == "es"


async def test_asking_for_a_language_the_course_lacks_names_the_ones_it_has(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "polyglot", courses=["fixture-oposiciones"])
    for path in ("", "/glossary", "/lessons/m01-l1", "/export", "/print/exercises", "/stats/me"):
        response = await multi_client.get(f"{OPOS}{path}?lang=en")
        assert response.status_code == 404, path
        body = response.json()
        assert body["code"] == "LANGUAGE_NOT_AVAILABLE", path
        assert body["available"] == ["es"], path
        assert "es" in body["message"], path


async def test_the_export_of_a_one_language_course_carries_only_that_language(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "exporter", courses=["fixture-oposiciones"])
    every = (await multi_client.get(f"{OPOS}/export")).json()
    assert every["locales"] == ["es"]
    assert list(every["glossary"]) == ["es"]


async def test_a_chosen_reading_language_is_remembered_per_course(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "chooser", locale="en", courses=["crypto-futures"])
    assert (await multi_client.get(CRYPTO)).json()["locale"] == "en"
    chosen = await multi_client.put(
        "/api/me/courses", json={"active": ["crypto-futures"], "readingLanguages": {"crypto-futures": "es"}}
    )
    assert chosen.json()["readingLanguages"]["crypto-futures"] == "es"
    assert (await multi_client.get(CRYPTO)).json()["locale"] == "es"

    refused = await multi_client.put(
        "/api/me/courses",
        json={"active": ["fixture-oposiciones"], "readingLanguages": {"fixture-oposiciones": "en"}},
    )
    assert refused.status_code == 400 and refused.json()["available"] == ["es"]


async def test_the_same_ids_in_two_courses_never_share_progress(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "isolated", courses=["crypto-futures", "fixture-oposiciones"])
    attempt_id = await _answer_opos_quiz(multi_client, correct=False)
    await multi_client.post(f"{OPOS}/lessons/m01-l1/complete")

    # crypto-futures has an m01-ex-1 and an m01-l1 too; neither may show the other course's rows.
    assert (await multi_client.get(f"{CRYPTO}/attempts?exercise_id=m01-ex-1")).json() == []
    assert (await multi_client.get(f"{CRYPTO}/attempts/{attempt_id}")).status_code == 404
    crypto_stats = (await multi_client.get(f"{CRYPTO}/stats/me")).json()
    assert crypto_stats["exercise"]["answered"] == 0
    assert crypto_stats["reading"]["lessonsCompleted"] == 0
    crypto_course = (await multi_client.get(CRYPTO)).json()
    assert crypto_course["started"] is False

    opos_stats = (await multi_client.get(f"{OPOS}/stats/me")).json()
    assert opos_stats["exercise"]["answered"] == 1


async def test_an_exam_belongs_to_its_course(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "examinee", courses=["crypto-futures", "fixture-oposiciones"])
    exam = (await multi_client.post(f"{OPOS}/exams", json={"scope": "global"})).json()
    assert (await multi_client.get(f"{CRYPTO}/exams/open")).json() == []
    assert (await multi_client.get(f"{CRYPTO}/exams/{exam['id']}")).status_code == 404
    assert [e["id"] for e in (await multi_client.get(f"{OPOS}/exams/open")).json()] == [exam["id"]]


async def test_a_course_without_figures_has_none_to_serve(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "figureless", courses=["fixture-oposiciones"])
    response = await multi_client.get(f"{OPOS}/figures/fig-m03-candle-anatomy")
    assert response.status_code == 404
    assert response.json()["code"] == "FIGURE_NOT_FOUND"
