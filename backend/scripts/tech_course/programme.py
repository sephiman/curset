# SPDX-License-Identifier: AGPL-3.0-only
"""The locked programme (`programme.md`): its bullet ids, and the ones the source coverage report dropped."""

from __future__ import annotations

import re
from pathlib import Path

from scripts.tech_course.lessons import REPO, course_dir

COVERAGE = REPO / "docs" / "backend-verification" / "s0" / "coverage"
_BULLET = re.compile(r"^\s*- `(?P<id>\d+\.\d+\.[a-z]+)`")


def programme_bullets(course: str) -> list[str]:
    text = (course_dir(course) / "programme.md").read_text(encoding="utf-8")
    return [match["id"] for line in text.splitlines() if (match := _BULLET.match(line))]


def dropped_bullets(coverage: Path = COVERAGE) -> set[str]:
    dropped: set[str] = set()
    for report in sorted(coverage.glob("m*.final.tsv")):
        for row in report.read_text(encoding="utf-8").splitlines()[1:]:
            cells = row.split("\t")
            if len(cells) > 1 and cells[1] == "drop":
                dropped.add(cells[0])
    return dropped


def lesson_of(bullet: str) -> str:
    module, lesson, _ = bullet.split(".")
    return f"m{int(module):02d}-l{int(lesson):02d}"
