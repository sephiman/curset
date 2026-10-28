# SPDX-License-Identifier: AGPL-3.0-only
"""A course's `excerpts.json`, as serving reads it: the norm's text per question, built at generation time."""

from __future__ import annotations

import json
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path

from pydantic import BaseModel

from tradeschool.citations.excerpts import (
    NO_CITATION,
    NO_FACT,
    NO_FILE,
    NO_HEADING,
    NO_LABEL,
    NO_MATCH,
    NO_NORM,
    NO_PARSE,
    NOT_TEXT,
)
from tradeschool.citations.sources import source_url
from tradeschool.content.schema import Manifest
from tradeschool.exercises.case import CaseConfig
from tradeschool.exercises.quiz import QuizConfig
from tradeschool.exercises.types import ExerciseType

EXCERPTS_FILE = "excerpts.json"


def question_key(question_id: str, case_key: str | None = None) -> str:
    """A question's permanent name: a quiz question's own id, which no rebuild or rebalancing changes; a case
    question's id under its case's key, since those ids are unique only inside the case."""
    return question_id if case_key is None else f"{case_key}/{question_id}"


@dataclass(frozen=True)
class SolvedQuestion:
    key: str
    citation: str | None
    explanation: str


def solved_questions(
    manifest: Manifest, exercise_configs: dict[str, tuple[ExerciseType, BaseModel]], locale: str
) -> list[SolvedQuestion]:
    """Every multiple-choice question of the course: quiz variants and case questions, in course order."""
    found: list[SolvedQuestion] = []
    for _module, _lesson, exercise in manifest.iter_exercises():
        config = exercise_configs.get(exercise.id)
        cfg = config[1] if config else None
        if isinstance(cfg, QuizConfig):
            items = [(question_key(v.id), v.citation, v.explanation) for v in cfg.variants]
        elif isinstance(cfg, CaseConfig):
            items = [(question_key(q.id, exercise.key), q.citation, q.explanation) for q in cfg.questions]
        else:
            continue
        found += [
            SolvedQuestion(key, citation, text.get(locale) if text else "") for key, citation, text in items
        ]
    return found


@dataclass(frozen=True)
class SolutionExcerpt:
    """The cited text a solution panel shows, and where «Texto consolidado» opens the source."""

    heading: str
    text: str
    full: str | None
    full_too_long: bool
    href: str
    #: A saved documentation page's title and date; None for a norm.
    attribution: str | None

    @classmethod
    def from_json(cls, course: str, raw: dict[str, object]) -> SolutionExcerpt:
        source = raw["source"]
        assert isinstance(source, dict)
        return cls(
            heading=str(raw["heading"]),
            text=str(raw["text"]),
            full=str(raw["full"]) if raw.get("full") else None,
            full_too_long=bool(raw.get("fullTooLong")),
            href=source_url(course, str(source["file"])) + str(source.get("fragment") or ""),
            attribution=str(raw["attribution"]) if raw.get("attribution") else None,
        )


# The reasons as the web names them («Sin extracto: …» per code, in the i18n bundles).
REASON_CODES = {
    NO_CITATION: "no-citation",
    NO_NORM: "no-norm",
    NO_FILE: "no-file",
    NOT_TEXT: "not-text",
    NO_HEADING: "no-heading",
    NO_LABEL: "no-label",
    NO_MATCH: "no-match",
    NO_PARSE: "no-parse",
    NO_FACT: "no-fact",
}


@dataclass(frozen=True)
class MissingExcerpt:
    """A question the build found no text for: the panel says so, with the reason's code, and still links
    the source it looked in."""

    reason: str
    href: str | None = None


SolutionText = SolutionExcerpt | MissingExcerpt


@dataclass(frozen=True)
class ExcerptStore:
    course: str
    #: question key → {"citation", "excerpt"} or {"citation", "none"}.
    questions: dict[str, dict[str, object]] = field(default_factory=dict)
    sources: dict[str, str] = field(default_factory=dict)

    @classmethod
    def load(cls, course_dir: Path) -> ExcerptStore | None:
        path = course_dir / EXCERPTS_FILE
        if not path.exists():
            return None
        raw = json.loads(path.read_text(encoding="utf-8"))
        return cls(course_dir.name, dict(raw.get("questions", {})), dict(raw.get("sources", {})))

    def excerpt(self, key: str) -> SolutionText | None:
        entry = self.questions.get(key, {})
        found = entry.get("excerpt")
        if isinstance(found, dict):
            return SolutionExcerpt.from_json(self.course, found)
        reason = entry.get("none")
        if not reason:
            return None
        source = entry.get("source")
        href = (
            source_url(self.course, str(source["file"])) + str(source.get("fragment") or "")
            if isinstance(source, dict)
            else None
        )
        return MissingExcerpt(REASON_CODES.get(str(reason), "no-match"), href)

    def problems(self, questions: Iterable[SolvedQuestion]) -> list[str]:
        """Questions with no entry, or whose entry was built for another citation: the file is stale."""
        problems: list[str] = []
        listed = list(questions)
        counts = Counter(question.key for question in listed)
        problems += [f"{key} names {n} questions" for key, n in counts.items() if n > 1]
        for question in listed:
            entry = self.questions.get(question.key)
            citation = " ".join((question.citation or "").split())
            if entry is None:
                problems.append(f"{question.key} has no entry")
            elif entry.get("citation") != citation:
                problems.append(
                    f"{question.key}: built for «{entry.get('citation')}», the question cites «{citation}»"
                )
        return problems
