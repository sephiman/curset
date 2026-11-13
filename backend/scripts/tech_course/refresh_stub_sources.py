# SPDX-License-Identifier: AGPL-3.0-only
"""Rewrites the `## Sources` block of every stub lesson from the current coverage report.

uv run python -m scripts.tech_course.refresh_stub_sources [--module m02 | --lesson m02-l01] [--check]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from scripts.tech_course.bullet_sources import (
    S0,
    Row,
    Storage,
    default_rule_reasons,
    is_dropped,
    load_rows,
    load_storage,
    rows_of_lesson,
)
from scripts.tech_course.lessons import Lesson, add_course_argument, course_dir, read_lessons

_SOURCES_HEADING = re.compile(r"^## Sources\s*$")
_NEXT_HEADING = re.compile(r"^## ")


def source_line(row: Row, storage: Storage, reasons: dict[str, str]) -> str:
    if is_dropped(row, storage):
        return f"- `{row.bullet}` (dropped): {reasons.get(row.bullet) or row.note or 'no source yet'}"
    entries = ", ".join(f"`{storage.rendered(entry)}`" for entry in row.entries)
    return f"- `{row.bullet}` ({row.kind}): {entries or 'no source yet'}"


def refreshed(lesson: Lesson, rows: dict[str, Row], storage: Storage, reasons: dict[str, str]) -> str:
    lines = lesson.text.split("\n")
    start = next((i for i, line in enumerate(lines) if _SOURCES_HEADING.match(line)), None)
    if start is None:
        return lesson.text
    end = next((i for i in range(start + 1, len(lines)) if _NEXT_HEADING.match(lines[i])), len(lines))
    block = [source_line(row, storage, reasons) for row in rows_of_lesson(rows, lesson.id)]
    head = [*lines[: start + 1], "", *block, ""]
    return "\n".join([*head, *lines[end:]])


def selected(lessons: list[Lesson], module: str | None, lesson: str | None) -> list[Lesson]:
    return [
        item
        for item in lessons
        if item.pending
        and (lesson is None or item.id == lesson)
        and (module is None or item.id.startswith(f"{module}-"))
    ]


def main(argv: list[str] | None = None, s0: Path = S0) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_course_argument(parser)
    parser.add_argument("--module")
    parser.add_argument("--lesson")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    rows, reasons, storage = load_rows(s0), default_rule_reasons(s0), load_storage(args.course, s0)
    folder = course_dir(args.course) / "en" / "lessons"
    changed = 0
    for lesson in selected(read_lessons(args.course), args.module, args.lesson):
        text = refreshed(lesson, rows, storage, reasons)
        if text == lesson.text:
            continue
        changed += 1
        print(f"{'would change' if args.check else 'rewrote'} {lesson.id}")
        if not args.check:
            (folder / f"{lesson.id}.md").write_text(text, encoding="utf-8")
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    sys.exit(main())
