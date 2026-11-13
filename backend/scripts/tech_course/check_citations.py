# SPDX-License-Identifier: AGPL-3.0-only
"""Every `source_id#anchor` of the lessons and questions resolves, and its anchor still hashes as recorded.

uv run python -m scripts.tech_course.check_citations [--course backend-in-depth]
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field

from scripts.tech_course.anchor_text import AnchorStore
from scripts.tech_course.lessons import add_course_argument, course_dir, read_lessons
from scripts.tech_course.questions import read_questions
from tradeschool.citations.tech import SourceRef, TechSourceIndex


@dataclass
class Audit:
    problems: list[str] = field(default_factory=list)
    cited: dict[SourceRef, list[str]] = field(default_factory=dict)
    skipped: int = 0


def cited_refs(course: str) -> tuple[dict[SourceRef, list[str]], list[str]]:
    """Every distinct citation with the places that cite it, and the ones that are not `source_id#anchor`."""
    places: dict[SourceRef, list[str]] = {}
    malformed: list[str] = []
    for lesson in read_lessons(course):
        for cited in lesson.citations():
            places.setdefault(cited.ref, []).append(f"lesson {lesson.id} line {cited.line}")
        malformed += [
            f"lesson {lesson.id} line {line}: «{text}» is not source_id#anchor"
            for line, text in lesson.malformed_citations()
        ]
    for question in read_questions(course):
        for ref in question.refs():
            if ref is None:
                malformed.append(f"question {question.label}: «{question.citation}» is not source_id#anchor")
            else:
                places.setdefault(ref, []).append(f"question {question.label}")
    return places, malformed


def audit(course: str) -> Audit:
    index = TechSourceIndex.load(course_dir(course))
    if index is None:
        raise SystemExit(f"{course} has no sources/sources.yaml")
    places, malformed = cited_refs(course)
    result = Audit(list(malformed), places)
    store = AnchorStore(index, course)
    for ref, where in sorted(places.items(), key=lambda item: str(item[0])):
        if why := index.problem(ref):
            result.problems.append(f"{where[0]}: {ref}: {why}")
            continue
        result.problems += _version_problems(store, ref, where[0])
    result.skipped = store.skipped_local
    return result


def _version_problems(store: AnchorStore, ref: SourceRef, where: str) -> list[str]:
    try:
        stored = store.anchor(ref)
    except (FileNotFoundError, KeyError) as exc:
        return [f"{where}: {exc}"]
    if stored is None:
        return []
    recorded = store.recorded_digest(ref)
    if recorded != stored.digest:
        return [f"{where}: {ref}: stored text {stored.digest[:12]}, anchors file {str(recorded)[:12]}"]
    return []


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_course_argument(parser)
    result = audit(parser.parse_args(argv).course)
    for problem in result.problems:
        print(f"FAIL {problem}")
    print(
        f"check_citations: {len(result.cited)} distinct citations, {len(result.problems)} problems, "
        f"{result.skipped} local-source checks skipped"
    )
    return 1 if result.problems else 0


if __name__ == "__main__":
    sys.exit(main())
