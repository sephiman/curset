# SPDX-License-Identifier: AGPL-3.0-only
"""Every built exercise file of backend-in-depth is declared by a lesson; the registry loads no other."""

from __future__ import annotations

from pathlib import Path

import yaml

COURSE = Path(__file__).resolve().parents[2] / "content" / "backend-in-depth"


def _declared_exercise_ids() -> set[str]:
    manifest = yaml.safe_load((COURSE / "course.yaml").read_text(encoding="utf-8"))
    return {
        exercise["id"]
        for block in manifest["blocks"]
        for module in block["modules"]
        for lesson in module["lessons"]
        for exercise in lesson.get("exercises", [])
    }


def test_every_exercise_file_is_declared_in_course_yaml() -> None:
    files = {path.stem for path in (COURSE / "exercises").glob("*.yaml")}
    undeclared = sorted(files - _declared_exercise_ids())
    assert undeclared == [], f"run docs/backend-verification/s2/tools/wire_exercises.py: {undeclared}"
