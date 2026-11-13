# SPDX-License-Identifier: AGPL-3.0-only
"""Each question `extract` is a literal substring of its first cited anchor (the one the panel credits).

uv run python -m scripts.tech_course.check_extracts [--course backend-in-depth]
"""

from __future__ import annotations

import argparse
import sys

from scripts.tech_course.anchor_text import AnchorStore, collapse
from scripts.tech_course.lessons import add_course_argument, course_dir
from scripts.tech_course.questions import Question, read_questions
from tradeschool.citations.tech import TechSourceIndex


def extract_problems(questions: list[Question], index: TechSourceIndex, store: AnchorStore) -> list[str]:
    problems: list[str] = []
    for question in questions:
        if question.extract is not None:
            problems += _problems_of(question, question.extract, index, store)
    return problems


def _problems_of(question: Question, extract: str, index: TechSourceIndex, store: AnchorStore) -> list[str]:
    cited = question.refs()
    first = cited[0] if cited else None
    if first is None:
        return [f"question {question.label}: an extract needs a source_id#anchor first citation"]
    if first.source_id in index.sources and not index.sources[first.source_id].extract_allowed:
        return [f"question {question.label}: {first.source_id} does not allow extracts"]
    if index.problem(first):
        return [f"question {question.label}: {first} does not resolve"]
    anchor = store.anchor(first)
    if anchor is None:
        return []
    if collapse(extract) in collapse(anchor.text):
        return []
    return [f"question {question.label}: the extract is not a literal substring of {first}"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_course_argument(parser)
    course = parser.parse_args(argv).course
    index = TechSourceIndex.load(course_dir(course))
    if index is None:
        raise SystemExit(f"{course} has no sources/sources.yaml")
    questions = read_questions(course)
    problems = extract_problems(questions, index, AnchorStore(index, course))
    for problem in problems:
        print(f"FAIL {problem}")
    print(
        f"check_extracts: {sum(q.extract is not None for q in questions)} extracts in "
        f"{len(questions)} questions, {len(problems)} problems"
    )
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
