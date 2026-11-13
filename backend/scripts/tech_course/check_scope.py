# SPDX-License-Identifier: AGPL-3.0-only
"""Scope audit: each audited section of a written lesson declares programme bullets of its own subsection.

uv run python -m scripts.tech_course.check_scope [--course backend-in-depth]
"""

from __future__ import annotations

import argparse
import re
import sys

from scripts.tech_course.lessons import EXEMPT_FROM_SCOPE, Lesson, add_course_argument, read_lessons, written
from scripts.tech_course.programme import lesson_of, programme_bullets

_LESSON_ID = re.compile(r"^m\d{2}-l\d{2}$")


def scope_problems(lessons: list[Lesson], programme: set[str]) -> list[str]:
    problems: list[str] = []
    for lesson in written(lessons):
        if lesson.id not in EXEMPT_FROM_SCOPE:
            problems += _lesson_problems(lesson, programme)
    return problems


def _lesson_problems(lesson: Lesson, programme: set[str]) -> list[str]:
    if not _LESSON_ID.match(lesson.id):
        return [f"lesson {lesson.id}: not a programme lesson id (mNN-lMM)"]
    sections = [section for section in lesson.sections() if section.audited]
    if not sections:
        return [f"lesson {lesson.id}: no audited section"]
    problems: list[str] = []
    for section in sections:
        where = f"lesson {lesson.id} line {section.line} «{section.title}»"
        if not section.bullets:
            problems.append(f"{where}: declares no bullet")
        for bullet in section.bullets:
            if bullet not in programme:
                problems.append(f"{where}: {bullet} is not in the programme")
            elif lesson_of(bullet) != lesson.id:
                problems.append(f"{where}: {bullet} belongs to {lesson_of(bullet)}")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_course_argument(parser)
    course = parser.parse_args(argv).course
    lessons = read_lessons(course)
    problems = scope_problems(lessons, set(programme_bullets(course)))
    for problem in problems:
        print(f"FAIL {problem}")
    audited = [lesson for lesson in written(lessons) if lesson.id not in EXEMPT_FROM_SCOPE]
    print(
        f"check_scope: {len(audited)} written lessons audited "
        f"({len(lessons) - len(written(lessons))} pending skipped), {len(problems)} problems"
    )
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
