# SPDX-License-Identifier: AGPL-3.0-only
"""Coverage audit: every programme bullet not dropped is declared by a written lesson; pending are counted.

uv run python -m scripts.tech_course.check_coverage [--course backend-in-depth]
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass

from scripts.tech_course.lessons import Lesson, add_course_argument, read_lessons, written
from scripts.tech_course.programme import dropped_bullets, lesson_of, programme_bullets


@dataclass(frozen=True)
class Coverage:
    covered: list[str]
    dropped: list[str]
    pending: list[str]
    uncovered: list[str]


def coverage(lessons: list[Lesson], programme: list[str], dropped: set[str]) -> Coverage:
    declared = {
        bullet for lesson in written(lessons) for section in lesson.sections() for bullet in section.bullets
    }
    written_ids = {lesson.id for lesson in written(lessons)}
    result: dict[str, list[str]] = {"covered": [], "dropped": [], "pending": [], "uncovered": []}
    for bullet in programme:
        if bullet in dropped:
            result["dropped"].append(bullet)
        elif bullet in declared:
            result["covered"].append(bullet)
        elif lesson_of(bullet) in written_ids:
            result["uncovered"].append(bullet)
        else:
            result["pending"].append(bullet)
    return Coverage(**result)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_course_argument(parser)
    course = parser.parse_args(argv).course
    programme = programme_bullets(course)
    found = coverage(read_lessons(course), programme, dropped_bullets())
    for bullet in found.uncovered:
        print(f"FAIL {bullet}: its lesson {lesson_of(bullet)} is written but no section declares it")
    print(
        f"check_coverage: {len(programme)} bullets: {len(found.covered)} covered, "
        f"{len(found.dropped)} dropped, "
        f"{len(found.pending)} pending, {len(found.uncovered)} uncovered"
    )
    return 1 if found.uncovered else 0


if __name__ == "__main__":
    sys.exit(main())
