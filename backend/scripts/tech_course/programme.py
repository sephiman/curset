# SPDX-License-Identifier: AGPL-3.0-only
"""The locked programme (`programme.md`): its bullet ids and the lesson each belongs to."""

from __future__ import annotations

import re

from scripts.tech_course.lessons import course_dir

_BULLET = re.compile(r"^\s*- `(?P<id>\d+\.\d+\.[a-z]+)`")


def programme_bullets(course: str) -> list[str]:
    text = (course_dir(course) / "programme.md").read_text(encoding="utf-8")
    return [match["id"] for line in text.splitlines() if (match := _BULLET.match(line))]


def lesson_of(bullet: str) -> str:
    module, lesson, _ = bullet.split(".")
    return f"m{int(module):02d}-l{int(lesson):02d}"
