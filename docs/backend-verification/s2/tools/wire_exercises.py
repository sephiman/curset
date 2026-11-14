# SPDX-License-Identifier: AGPL-3.0-only
"""Declare each built exercise file (`exercises/<lesson>-ex-1.yaml`, `exercises/m09-case-*.yaml`) under its lesson in
course.yaml; the registry only loads exercises a lesson declares. Idempotent.

    python wire_exercises.py [--course-dir content/backend-in-depth] [--case m09-l04=case-rate-limiter ...]
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

_LESSON = re.compile(r"^    - id: (m\d{2}-l\d{2})$")
# requirements 6.4: one case per blueprint of programme section 9.4, so every built case belongs to lesson 9.4
CASE_LESSON = "m09-l04"


def declared_block(exercises: list[tuple[str, str]]) -> list[str]:
    rows = [line for eid, etype in exercises for line in (f"      - id: {eid}", f"        type: {etype}")]
    return ["      exercises:", *rows]


def wire(text: str, wanted: dict[str, list[tuple[str, str]]]) -> str:
    lines = text.split("\n")
    out: list[str] = []
    index = 0
    while index < len(lines):
        match = _LESSON.match(lines[index])
        if not match:
            out.append(lines[index])
            index += 1
            continue
        # a lesson's own fields are indented six or more; its block ends at the first shallower line
        end = index + 1
        while end < len(lines) and (lines[end].startswith("      ") or not lines[end].strip()):
            end += 1
        while end > index + 1 and not lines[end - 1].strip():
            end -= 1
        block = lines[index:end]
        lesson = match.group(1)
        requested = dict.fromkeys(wanted.get(lesson, []))
        missing = [(eid, et) for eid, et in requested if f"      - id: {eid}" not in block]
        if missing and "      exercises:" in block:
            block += [line for eid, et in missing for line in (f"      - id: {eid}", f"        type: {et}")]
        elif missing:
            block += declared_block(missing)
        out += block
        index = end
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--course-dir", type=Path, default=Path("content/backend-in-depth"))
    parser.add_argument("--case", action="append", default=[], help="LESSON=CASE_ID")
    args = parser.parse_args()
    wanted: dict[str, list[tuple[str, str]]] = {}
    for path in sorted((args.course_dir / "exercises").glob("m*-l*-ex-1.yaml")):
        lesson = path.name.removesuffix("-ex-1.yaml")
        wanted.setdefault(lesson, []).append((path.stem, "quiz"))
    for path in sorted((args.course_dir / "exercises").glob("m09-case-*.yaml")):
        wanted.setdefault(CASE_LESSON, []).append((path.stem, "case"))
    for pair in args.case:
        lesson, case = pair.split("=", 1)
        wanted.setdefault(lesson, []).append((case, "case"))
    manifest = args.course_dir / "course.yaml"
    before = manifest.read_text(encoding="utf-8")
    after = wire(before, wanted)
    manifest.write_text(after, encoding="utf-8")
    print(f"wired {sum(len(v) for v in wanted.values())} exercises in {len(wanted)} lessons; changed: {before != after}")


if __name__ == "__main__":
    main()
