# SPDX-License-Identifier: AGPL-3.0-only
"""Question quota per lesson: max(10, min(30, F + X)); F cited sentences and esquema rows, X snippet blocks.

uv run python -m scripts.tech_course.lesson_quota [--course backend-in-depth]
"""

from __future__ import annotations

import argparse
import sys

from scripts.tech_course.lessons import Lesson, add_course_argument, read_lessons
from scripts.tech_course.questions import read_questions

MINIMUM, MAXIMUM = 10, 30


def quota(facts: int, executable: int) -> int:
    return max(MINIMUM, min(MAXIMUM, facts + executable))


def quota_row(lesson: Lesson, questions: int) -> list[str]:
    if lesson.pending:
        return [lesson.id, "pending", "-", "-", "-", str(questions)]
    facts, executable = lesson.fact_sentences(), lesson.snippet_count()
    return [lesson.id, "written", str(facts), str(executable), str(quota(facts, executable)), str(questions)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_course_argument(parser)
    course = parser.parse_args(argv).course
    asked = [question.lesson_id for question in read_questions(course)]
    print("lesson\tstatus\tF\tX\tquota\tquestions")
    for lesson in read_lessons(course):
        print("\t".join(quota_row(lesson, asked.count(lesson.id))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
