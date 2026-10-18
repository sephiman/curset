# SPDX-License-Identifier: AGPL-3.0-only
"""Results by lesson: one row per lesson with questions in it, grouped by module, and the two short lists.

The lists («Donde más brillas», «Donde más tienes que preparar») rank lessons with at least
`MIN_QUESTIONS_TO_RANK` questions. Fewer than three such lessons and they rank modules instead (said
so in `level`); fewer than three such modules either and there are no lists, only the table. Each list
holds up to three entries and the two never share one. A blank is not a correct answer, and it is
counted apart because with a penalty leaving a question blank is a decision.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Literal

from tradeschool.content.registry import CourseRegistry

#: The progress honesty rule: nothing is ranked on one or two questions.
MIN_QUESTIONS_TO_RANK = 3
#: Ranking needs this many qualifying lessons (or modules): fewer cannot say where one is better.
MIN_RANKED = 3
LIST_LENGTH = 3

Outcome = Literal["correct", "wrong", "blank"]


@dataclass
class _Row:
    id: str
    title: str
    correct: int = 0
    wrong: int = 0
    blank: int = 0
    order: int = 0

    @property
    def questions(self) -> int:
        return self.correct + self.wrong + self.blank

    def add(self, outcome: Outcome) -> None:
        setattr(self, outcome, getattr(self, outcome) + 1)

    def out(self, key: str) -> dict[str, object]:
        return {
            key: self.id,
            "title": self.title,
            "questions": self.questions,
            "correct": self.correct,
            "wrong": self.wrong,
            "blank": self.blank,
            "pct": round(self.correct / self.questions, 4) if self.questions else None,
        }


@dataclass
class _Group:
    module: _Row
    lessons: list[_Row] = field(default_factory=list)


def _ranked(rows: list[_Row], key: str) -> dict[str, object] | None:
    qualifying = [row for row in rows if row.questions >= MIN_QUESTIONS_TO_RANK]
    if len(qualifying) < MIN_RANKED:
        return None
    size = min(LIST_LENGTH, len(qualifying) // 2)
    best_first = sorted(qualifying, key=lambda r: (-r.correct / r.questions, -r.questions, r.order))
    worst_first = sorted(qualifying, key=lambda r: (r.correct / r.questions, -r.questions, r.order))
    return {
        "best": [r.out(key) for r in best_first[:size]],
        "worst": [r.out(key) for r in worst_first[:size]],
    }


def lesson_table(
    registry: CourseRegistry, outcomes: Iterable[tuple[str, Outcome]], locale: str
) -> dict[str, object]:
    """`outcomes` is (lesson id, outcome) per counted question; rows follow course order."""
    lessons: dict[str, _Row] = {}
    for lesson_id, outcome in outcomes:
        location = registry.lesson_location(lesson_id)
        if location is None:
            continue
        lessons.setdefault(lesson_id, _Row(lesson_id, location.lesson.title.get(locale))).add(outcome)

    groups: list[_Group] = []
    for order, (module, lesson) in enumerate(registry.manifest.iter_lessons()):
        found = lessons.get(lesson.id)
        if found is None:
            continue
        found.order = order
        if not groups or groups[-1].module.id != module.id:
            groups.append(_Group(_Row(module.id, module.title.get(locale), order=order)))
        group = groups[-1]
        group.lessons.append(found)
        for outcome in ("correct", "wrong", "blank"):
            setattr(group.module, outcome, getattr(group.module, outcome) + getattr(found, outcome))

    lists = _ranked([row for group in groups for row in group.lessons], "lessonId")
    level: Literal["lesson", "module"] | None = "lesson" if lists else None
    if lists is None:
        lists = _ranked([group.module for group in groups], "moduleId")
        level = "module" if lists else None
    return {
        "threshold": MIN_QUESTIONS_TO_RANK,
        "groups": [
            {**group.module.out("moduleId"), "lessons": [row.out("lessonId") for row in group.lessons]}
            for group in groups
        ],
        "lists": {"level": level, **lists} if lists else None,
    }
