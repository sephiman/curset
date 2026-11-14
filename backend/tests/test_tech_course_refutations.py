# SPDX-License-Identifier: AGPL-3.0-only
"""The refutation sidecar check, over the real backend-in-depth source index and snippet records."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml
from scripts.tech_course import check_refutations
from scripts.tech_course.anchor_text import AnchorStore
from scripts.tech_course.candidates import candidate_of
from scripts.tech_course.check_refutations import Checker, question_problems
from scripts.tech_course.lessons import course_dir

from tradeschool.citations.tech import TechSourceIndex

COURSE = "backend-in-depth"
ANCHOR = "pg-transaction-iso#XACT-SERIALIZABLE"
STRICTEST = "The Serializable isolation level provides the strictest transaction isolation."
RETRY = "applications using this level must be prepared to retry transactions due to serialization failures"
NO_BLOCKING = "This monitoring does not introduce any blocking beyond that present in repeatable read"
OVERHEAD = "there is some overhead to the monitoring"
SNIPPET = "m01-l01/AccessorFailure.java"
SNIPPET_OUTPUT = "MatchException caused by java.lang.IllegalStateException: sensor offline\ntrue"


@pytest.fixture(scope="module")
def checker() -> Checker:
    index = TechSourceIndex.load(course_dir(COURSE))
    assert index is not None
    return Checker(index, AnchorStore(index, COURSE), course_dir(COURSE) / "snippets")


def question(key: str = "the strictest isolation", snippet: str | None = None) -> dict[str, object]:
    return {
        "id": "m00-l00-q01",
        "stem": "stem",
        "key": key,
        "distractors": ["never retried", "blocks more than repeatable read", "free of overhead"],
        "explanation": "",
        "citation": ANCHOR,
        "extract": None,
        "snippet": snippet,
    }


def cited(sentence: str, **extra: object) -> dict[str, object]:
    return {"anchor": ANCHOR, "sentence": sentence, **extra}


def sidecar(**overrides: object) -> dict[str, object]:
    entry: dict[str, object] = {
        "key": cited(STRICTEST),
        "wrong": [
            {"option": "never retried", **cited(RETRY)},
            {"option": "blocks more than repeatable read", **cited(NO_BLOCKING)},
            {"option": "free of overhead", **cited(OVERHEAD)},
        ],
    }
    return {**entry, **overrides}


def test_accepts_a_map_with_one_literal_sentence_per_option(checker: Checker) -> None:
    assert question_problems(candidate_of(question()), sidecar(), checker) == []


def test_rejects_a_question_without_an_entry(checker: Checker) -> None:
    assert question_problems(candidate_of(question()), None, checker) == ["m00-l00-q01: no refutation entry"]


def test_rejects_a_distractor_without_a_refutation(checker: Checker) -> None:
    wrong = [{"option": "never retried", **cited(RETRY)}, {"option": "free of overhead", **cited(OVERHEAD)}]
    problems = question_problems(candidate_of(question()), sidecar(wrong=wrong), checker)
    assert problems == ["m00-l00-q01: no refutation for 'blocks more than repeatable read'"]


def test_rejects_a_sentence_that_is_not_in_the_anchor(checker: Checker) -> None:
    entry = sidecar(key=cited("Serializable never fails."))
    problems = question_problems(candidate_of(question()), entry, checker)
    assert problems == [f"m00-l00-q01 key: sentence is not a literal substring of {ANCHOR}"]


def test_rejects_two_wrong_options_sharing_a_sentence_unless_both_are_exclusive(checker: Checker) -> None:
    shared = [
        {"option": "never retried", **cited(RETRY)},
        {"option": "blocks more than repeatable read", **cited(RETRY)},
        {"option": "free of overhead", **cited(OVERHEAD)},
    ]
    problems = question_problems(candidate_of(question()), sidecar(wrong=shared), checker)
    assert problems == [f"m00-l00-q01: wrong options share a sentence of {ANCHOR} without exclusive: true"]
    exclusive = [{**item, "exclusive": True} if item["sentence"] == RETRY else item for item in shared]
    assert question_problems(candidate_of(question()), sidecar(wrong=exclusive), checker) == []


def test_execution_key_must_equal_the_recorded_output(checker: Checker) -> None:
    entry = sidecar(key={"execution": SNIPPET})
    assert question_problems(candidate_of(question(SNIPPET_OUTPUT, SNIPPET)), entry, checker) == []
    problems = question_problems(candidate_of(question("true", SNIPPET)), entry, checker)
    assert problems == [f"m00-l00-q01 key: differs from the recorded output of {SNIPPET}"]


def test_execution_wrong_option_must_differ_from_the_recorded_output(checker: Checker) -> None:
    raw = {**question(SNIPPET_OUTPUT, SNIPPET), "distractors": ["true", SNIPPET_OUTPUT.upper(), "false"]}
    wrong = [
        {"option": "true", "execution": SNIPPET, "mistake": "ignores the exception"},
        {"option": SNIPPET_OUTPUT.upper(), "execution": SNIPPET, "mistake": "case"},
        {"option": "false", "execution": SNIPPET, "mistake": "wrong branch"},
    ]
    assert (
        question_problems(candidate_of(raw), sidecar(key={"execution": SNIPPET}, wrong=wrong), checker) == []
    )


def test_main_reports_a_lesson_without_a_sidecar(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    lesson = tmp_path / "m00-l00.questions.json"
    lesson.write_text(json.dumps([question()]), encoding="utf-8")
    assert check_refutations.main([str(lesson)]) == 1
    assert "m00-l00: no m00-l00.refutations.yaml" in capsys.readouterr().out
    (tmp_path / "m00-l00.refutations.yaml").write_text(yaml.safe_dump({"m00-l00-q01": sidecar()}), "utf-8")
    assert check_refutations.main([str(lesson)]) == 0
