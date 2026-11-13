# SPDX-License-Identifier: AGPL-3.0-only
"""The questions of a technical course's exercise files, as the scripts read their evidence fields."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

from scripts.tech_course.lessons import LOCALE, course_dir
from tradeschool.citations.tech import SourceRef, parse_ref


@dataclass(frozen=True)
class Question:
    label: str
    lesson_id: str
    citation: str | None
    extract: str | None
    snippet: str | None

    def refs(self) -> list[SourceRef | None]:
        """Each `;`-separated citation; None for one that is not `source_id#anchor`."""
        pieces = [piece for piece in (self.citation or "").split(";") if piece.strip()]
        return [parse_ref(piece) for piece in pieces]


def _text(value: object) -> str | None:
    if isinstance(value, dict):
        value = value.get(LOCALE)
    return value if isinstance(value, str) and value.strip() else None


def lesson_of_exercise(exercise_id: str) -> str:
    return re.split(r"-ex-?", exercise_id, maxsplit=1)[0]


def read_questions(course: str) -> list[Question]:
    questions: list[Question] = []
    for path in sorted((course_dir(course) / "exercises").glob("*.yaml")):
        questions += _questions_of(path)
    return questions


def _questions_of(path: Path) -> list[Question]:
    loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    lesson = lesson_of_exercise(path.stem)
    return [
        Question(
            f"{path.stem}/{variant.get('id', '?')}",
            lesson,
            variant.get("citation") if isinstance(variant.get("citation"), str) else None,
            _text(variant.get("extract")),
            variant.get("snippet") if isinstance(variant.get("snippet"), str) else None,
        )
        for variant in loaded.get("variants", [])
        if isinstance(variant, dict)
    ]
