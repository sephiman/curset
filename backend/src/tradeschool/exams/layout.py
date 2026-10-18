# SPDX-License-Identifier: AGPL-3.0-only
"""How a sitting is laid out, read back from its `rules`: parts, reserves, offered and marked cases."""

from __future__ import annotations

from tradeschool.exams.models import ExamSession
from tradeschool.exams.presets import ExamPreset


def attempt_layout(exam: ExamSession, preset: ExamPreset) -> dict[str, tuple[str, bool]]:
    """attempt id → (part id, reserve). A legacy session is one part holding every attempt."""
    parts = exam.rules.get("parts")
    layout: dict[str, tuple[str, bool]] = {}
    if isinstance(parts, list):
        for part in parts:
            if not isinstance(part, dict):
                continue
            for attempt_id in part.get("attempts", []):
                layout[str(attempt_id)] = (str(part["id"]), False)
            for attempt_id in part.get("reserve", []):
                layout[str(attempt_id)] = (str(part["id"]), True)
    return layout


def offered_cases(exam: ExamSession) -> dict[str, list[str]]:
    """part id → the case KEYS it offered, in the order shown."""
    parts = exam.rules.get("parts")
    if not isinstance(parts, list):
        return {}
    return {str(p["id"]): [str(c) for c in p.get("cases", [])] for p in parts if isinstance(p, dict)}


def case_marks(exam: ExamSession) -> dict[str, list[str]]:
    """part id → the case KEYS the learner marked."""
    marks = exam.rules.get("caseMarks")
    if not isinstance(marks, dict):
        return {}
    return {str(k): [str(c) for c in v] for k, v in marks.items() if isinstance(v, list)}
