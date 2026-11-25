# SPDX-License-Identifier: AGPL-3.0-only
"""Diagram audit: every `:::diagram` block of a lesson file is valid (amendment 12, contracts.md).

uv run python -m scripts.tech_course.check_diagrams [--course backend-in-depth]

Reads only the lesson files: syntax, node limit, caption and description. Whether each node restates a
verified sentence is the round's blind check, not this script's.
"""

from __future__ import annotations

import argparse
import sys

from scripts.tech_course.lessons import Lesson, add_course_argument, read_lessons
from tradeschool.content import diagram


def diagram_problems(lessons: list[Lesson]) -> list[str]:
    return [problem for lesson in lessons for problem in diagram.problems_in(lesson.id, lesson.text)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_course_argument(parser)
    lessons = read_lessons(parser.parse_args(argv).course)
    problems = diagram_problems(lessons)
    for problem in problems:
        print(f"FAIL {problem}")
    blocks = sum(len(diagram.blocks_of(lesson.text)) for lesson in lessons)
    print(f"check_diagrams: {blocks} diagrams in {len(lessons)} lessons, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
