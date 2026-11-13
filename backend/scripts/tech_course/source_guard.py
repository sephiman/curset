# SPDX-License-Identifier: AGPL-3.0-only
"""Per pending lesson: how many programme bullets have no stored source, and whether to write or skip it.

uv run python -m scripts.tech_course.source_guard [--module m02 | --lesson m02-l01]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from scripts.tech_course.bullet_sources import S0, Row, Storage, has_stored_source, load_rows, load_storage
from scripts.tech_course.lessons import add_course_argument, read_lessons
from scripts.tech_course.programme import lesson_of, programme_bullets
from scripts.tech_course.refresh_stub_sources import selected


def verdict(bullets: int, unsourced: int) -> str:
    return "skip" if unsourced * 5 > bullets else "write"


def report_line(lesson: str, bullets: list[str], rows: dict[str, Row], storage: Storage) -> str:
    unsourced = [bullet for bullet in bullets if not has_stored_source(rows.get(bullet), storage)]
    share = 100 * len(unsourced) / len(bullets)
    cells = [
        lesson,
        str(len(bullets)),
        str(len(unsourced)),
        f"{share:.0f}",
        verdict(len(bullets), len(unsourced)),
    ]
    return "\t".join([*cells, " ".join(unsourced)])


def main(argv: list[str] | None = None, s0: Path = S0) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_course_argument(parser)
    parser.add_argument("--module")
    parser.add_argument("--lesson")
    args = parser.parse_args(argv)
    rows, storage = load_rows(s0), load_storage(args.course, s0)
    by_lesson: dict[str, list[str]] = {}
    for bullet in programme_bullets(args.course):
        by_lesson.setdefault(lesson_of(bullet), []).append(bullet)
    for lesson in selected(read_lessons(args.course), args.module, args.lesson):
        if lesson.id in by_lesson:
            print(report_line(lesson.id, by_lesson[lesson.id], rows, storage))
    return 0


if __name__ == "__main__":
    sys.exit(main())
