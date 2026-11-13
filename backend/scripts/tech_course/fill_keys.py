# SPDX-License-Identifier: AGPL-3.0-only
"""Fill the empty `key` of code-reading candidates from the recorded run of their snippet.

uv run python -m scripts.tech_course.fill_keys [--course C] [--lesson ID | --module mNN | FILE ...]

The key is the recorded stdout without its trailing newline; for a run that failed, the stderr line that names
the exception or error.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from scripts.tech_course.candidates import (
    add_selection_arguments,
    lesson_of,
    read_raw,
    select_files,
    write_raw,
)
from scripts.tech_course.lessons import add_course_argument, course_dir
from scripts.tech_course.run_snippets import record_path

_EXCEPTION_LINE = re.compile(r"(?:Exception in thread \"[^\"]*\" )?(?P<line>[\w.$]*(?:Exception|Error)\b.*)")


class MissingRecordError(RuntimeError):
    pass


def error_line(stderr: str) -> str:
    lines = [line.strip() for line in stderr.splitlines() if line.strip()]
    for line in lines:
        match = _EXCEPTION_LINE.match(line)
        if match:
            return match["line"]
    return lines[0] if lines else ""


def recorded_key(snippets_root: Path, snippet: str) -> str:
    path = record_path(snippets_root / snippet)
    if not path.is_file():
        raise MissingRecordError(f"{snippet}: no run record ({path.name})")
    record = json.loads(path.read_text(encoding="utf-8"))
    if record.get("exit_code") != 0:
        return error_line(str(record.get("stderr", "")))
    return str(record.get("stdout", "")).removesuffix("\n")


def filled(entries: list[dict[str, object]], snippets_root: Path) -> list[dict[str, object]]:
    return [_with_key(entry, snippets_root) for entry in entries]


def _with_key(entry: dict[str, object], snippets_root: Path) -> dict[str, object]:
    snippet, key = entry.get("snippet"), entry.get("key")
    if not isinstance(snippet, str) or not snippet.strip() or (isinstance(key, str) and key):
        return entry
    return {**entry, "key": recorded_key(snippets_root, snippet)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_course_argument(parser)
    add_selection_arguments(parser)
    args = parser.parse_args(argv)
    root = course_dir(args.course) / "snippets"
    count = 0
    for path in select_files(args.lesson, args.module, args.paths):
        before = read_raw(path)
        try:
            after = filled(before, root)
        except MissingRecordError as exc:
            print(f"FAIL {lesson_of(path)}: {exc}")
            return 1
        write_raw(path, after)
        count += sum(a != b for a, b in zip(before, after, strict=True))
    print(f"fill_keys: {count} keys filled")
    return 0


if __name__ == "__main__":
    sys.exit(main())
