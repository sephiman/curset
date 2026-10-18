# SPDX-License-Identifier: AGPL-3.0-only
"""crypto-futures' exams, frozen before they became presets: what is drawn, how it scores, what review says.

Randomness is pinned (the exam service draws through `secrets`), so a sitting is a pure function of the
course. Regenerate with `UPDATE_EXAM_GOLDEN=1 uv run pytest tests/test_exam_crypto_golden.py` only for a
deliberate change, and say why in the commit.
"""

from __future__ import annotations

import json
import os
import random
from pathlib import Path

import pytest
from httpx import AsyncClient

from tradeschool.exams import service

API = "/api/courses/crypto-futures"
GOLDEN = Path(__file__).resolve().parent / "goldens" / "crypto-exam-results.json"
UPDATE = os.environ.get("UPDATE_EXAM_GOLDEN") == "1"


class _PinnedSecrets:
    """The two calls the exam service makes, from a seeded stream."""

    def __init__(self, seed: int) -> None:
        self._rng = random.Random(seed)

    def choice(self, seq: list[str]) -> str:
        return self._rng.choice(seq)

    def randbelow(self, n: int) -> int:
        return self._rng.randrange(n)


def _answer_for(index: int, question: dict[str, object]) -> dict[str, object] | None:
    """Every third question blank; quiz and calculation take the first option shown; charts a wrong label."""
    if index % 3 == 2:
        return None
    payload = question["payload"]
    assert isinstance(payload, dict)
    options = payload.get("options")
    kind = payload.get("kind")
    if question["type"] == "pattern_chart":
        return {"label": ""}
    if question["type"] in ("synthetic_chart", "fixture_chart"):
        return {"divergence": ""}
    if kind == "true_false":
        return {"value": index % 2 == 0}
    if kind == "multi_select" and isinstance(options, list):
        return {"optionIds": [options[0]["id"]]}
    if kind == "ordering":
        return {"order": [item["id"] for item in payload["items"]]}  # type: ignore[index]
    if kind == "matching":
        lefts, rights = payload["lefts"], payload["rights"]  # type: ignore[index]
        return {"pairs": {left["id"]: right["id"] for left, right in zip(lefts, rights, strict=True)}}
    assert isinstance(options, list)
    return {"optionId": options[0]["id"]}


async def _sit(client: AsyncClient, start: dict[str, object]) -> dict[str, object]:
    exam = (await client.post(f"{API}/exams", json=start)).json()
    for index, question in enumerate(exam["questions"]):
        answer = _answer_for(index, question)
        if answer is not None:
            url = f"{API}/exams/{exam['id']}/questions/{question['attemptId']}/answer"
            assert (await client.post(url, json={"answer": answer})).status_code == 204
    reviewed = (await client.post(f"{API}/exams/{exam['id']}/submit")).json()
    return {
        "questions": [[q["exerciseId"], q["moduleId"], q["blockId"]] for q in reviewed["questions"]],
        "review": [[q["isCorrect"], q["unanswered"], q["correctAnswer"]] for q in reviewed["questions"]],
        "result": reviewed["result"],
    }


async def test_crypto_exams_draw_and_score_exactly_as_frozen(
    content_client: AsyncClient, monkeypatch: pytest.MonkeyPatch
) -> None:
    creds = {"username": "goldentaker", "password": "correcthorse"}
    await content_client.post("/api/auth/register", json={**creds, "locale": "es"})
    await content_client.post("/api/auth/login", json=creds)

    current: dict[str, object] = {}
    for name, start, seed in (
        ("global", {"scope": "global"}, 11),
        ("block-a", {"scope": "block", "blockId": "block-a"}, 12),
        ("block-c", {"scope": "block", "blockId": "block-c"}, 13),
    ):
        monkeypatch.setattr(service, "secrets", _PinnedSecrets(seed))
        current[name] = await _sit(content_client, start)

    rendered = json.dumps(current, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    if UPDATE:
        GOLDEN.parent.mkdir(exist_ok=True)
        GOLDEN.write_text(rendered, encoding="utf-8")
    assert GOLDEN.exists(), "no golden yet: run with UPDATE_EXAM_GOLDEN=1"
    assert rendered == GOLDEN.read_text(encoding="utf-8"), (
        "crypto-futures exams changed — presets must keep them byte for byte (delta A5)"
    )
