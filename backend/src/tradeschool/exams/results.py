# SPDX-License-Identifier: AGPL-3.0-only
"""The stored result of a submitted sitting.

Every sitting gets the original blob (`score`, `correct`, `total`, `blocks`, `modules`) over the
questions that count. A scored preset — penalties, transformed scores, cases, reserves or several parts —
adds `parts` and the raw and transformed totals. An unscored preset's blob is byte-identical to the one
exams stored before presets existed.
"""

from __future__ import annotations

from fractions import Fraction

from tradeschool.attempts.models import Attempt
from tradeschool.attempts.service import question_ref
from tradeschool.content.registry import CourseRegistry
from tradeschool.exams.layout import attempt_layout, case_marks
from tradeschool.exams.models import ExamSession
from tradeschool.exams.presets import ExamPreset, PresetPart
from tradeschool.exams.scoring import NotGraded, Tally, raw_score, rounded, transformed_score
from tradeschool.stats.by_lesson import Outcome


def _ratio(num: int, den: int) -> float | None:
    return round(num / den, 4) if den else None


def is_scored(preset: ExamPreset) -> bool:
    return len(preset.parts) > 1 or any(
        part.penalty or part.scoring or part.cases or part.reserve or part.blank != "free"
        for part in preset.parts
    )


def _location(registry: CourseRegistry, attempt: Attempt) -> tuple[str, str]:
    exercise_id = question_ref(registry, attempt).exercise_id
    if attempt.question_id is not None:
        lesson_id = registry.question_lesson_id(exercise_id, attempt.question_id)
        location = registry.lesson_location(lesson_id) if lesson_id else None
        if location is not None:
            return location.block.id, location.module.id
    return registry.exercise_location(exercise_id) or ("", "")


def _legacy_blob(registry: CourseRegistry, counted: list[Attempt], locale: str) -> dict[str, object]:
    """Overall + per-block + per-module, in canonical module order — unchanged since before presets."""
    order = {module.id: i for i, (_, module) in enumerate(registry.manifest.iter_modules())}
    per_module: list[dict[str, object]] = []
    correct_total = 0
    block_order: list[str] = []
    block_title: dict[str, str] = {}
    block_correct: dict[str, int] = {}
    block_total: dict[str, int] = {}
    for attempt in sorted(counted, key=lambda a: order.get(_location(registry, a)[1], 10_000)):
        is_correct = bool(attempt.is_correct)
        b_id, m_id = _location(registry, attempt)
        per_module.append(
            {
                # Stored in the session's rules blob, so this is a KEY — display ids are resolved
                # at view time, which is also what keeps pre-renumber exams true.
                "moduleId": registry.module_key(m_id) if m_id else m_id,
                "title": registry.module_title(m_id, locale) or m_id,
                "blockId": b_id,
                "correct": is_correct,
                "unanswered": attempt.given_answer is None,
            }
        )
        if b_id not in block_total:
            block_order.append(b_id)
            block_title[b_id] = registry.block_title(b_id, locale) or b_id
            block_correct[b_id] = 0
            block_total[b_id] = 0
        block_total[b_id] += 1
        block_correct[b_id] += 1 if is_correct else 0
        correct_total += 1 if is_correct else 0
    total = len(per_module)
    return {
        "score": _ratio(correct_total, total),
        "correct": correct_total,
        "total": total,
        "blocks": [
            {
                "blockId": b,
                "title": block_title[b],
                "correct": block_correct[b],
                "total": block_total[b],
                "score": _ratio(block_correct[b], block_total[b]),
            }
            for b in block_order
        ],
        "modules": per_module,
    }


def _tally(attempts: list[Attempt]) -> Tally:
    blank = sum(1 for a in attempts if a.given_answer is None)
    correct = sum(1 for a in attempts if a.given_answer is not None and a.is_correct)
    return Tally(correct=correct, wrong=len(attempts) - blank - correct, blank=blank)


def _case_choice(part: PresetPart, marks: list[str]) -> tuple[str | None, NotGraded | None]:
    """The one marked case, or why the part cannot be graded."""
    if not part.cases:
        return None, None
    if not marks:
        return None, "no-case-marked"
    if len(marks) > 1:
        return None, "several-cases-marked"
    return marks[0], None


def counted_attempts(
    exam: ExamSession, preset: ExamPreset, attempts: list[Attempt]
) -> dict[str, tuple[list[Attempt], NotGraded | None, str | None]]:
    """part id → (attempts that count, why the part is not graded, the marked case key).

    Reserves never count (the platform voids nothing); in a case part only the marked case counts; a
    part waiting on the one before is not graded when that one did not pass.
    """
    layout = attempt_layout(exam, preset)
    marks = case_marks(exam)
    by_part: dict[str, list[Attempt]] = {part.id: [] for part in preset.parts}
    for attempt in attempts:
        part_id, reserve = layout.get(str(attempt.id), (preset.parts[0].id, False))
        if not reserve and part_id in by_part:
            by_part[part_id].append(attempt)
    out: dict[str, tuple[list[Attempt], NotGraded | None, str | None]] = {}
    for part in preset.parts:
        case, reason = _case_choice(part, marks.get(part.id, []))
        chosen = [a for a in by_part[part.id] if case is None or a.exercise_id == case]
        out[part.id] = ([] if reason else chosen, reason, case)
    return out


def counted_outcomes(
    registry: CourseRegistry, exam: ExamSession, preset: ExamPreset, attempts: list[Attempt]
) -> list[tuple[str, Outcome, float | None]]:
    """(lesson, outcome, time_seconds) for counted questions: graded parts, no reserves."""
    result = exam.rules.get("result")
    stored_parts = result.get("parts") if isinstance(result, dict) else None
    graded = (
        {str(p["id"]) for p in stored_parts if isinstance(p, dict) and p.get("graded")}
        if isinstance(stored_parts, list)
        else {part.id for part in preset.parts}
    )
    outcomes: list[tuple[str, Outcome, float | None]] = []
    for part_id, (counted, _reason, _case) in counted_attempts(exam, preset, attempts).items():
        if part_id not in graded:
            continue
        for attempt in counted:
            lesson_id = registry.question_lesson_id(
                question_ref(registry, attempt).exercise_id, attempt.question_id
            )
            if lesson_id is None:
                continue
            outcome: Outcome = (
                "blank" if attempt.given_answer is None else "correct" if attempt.is_correct else "wrong"
            )
            outcomes.append((lesson_id, outcome, attempt.time_seconds))
    return outcomes


def grade_session(
    registry: CourseRegistry, exam: ExamSession, preset: ExamPreset, attempts: list[Attempt], locale: str
) -> dict[str, object]:
    by_part = counted_attempts(exam, preset, attempts)
    parts: list[dict[str, object]] = []
    graded: list[Attempt] = []
    previous_passed = True
    raw_total = Fraction(0)
    transformed_total = Fraction(0)
    for part in preset.parts:
        counted, reason, case = by_part[part.id]
        if reason is None and part.requires_previous_pass and not previous_passed:
            reason = "previous-part-not-passed"
        tally = _tally(counted)
        part_seconds = round(sum(a.time_seconds for a in counted if a.time_seconds is not None), 1)
        entry: dict[str, object] = {
            "id": part.id,
            "graded": reason is None,
            "reason": reason,
            "case": case,
            "activeSeconds": part_seconds,
        }
        passed = False
        if reason is None:
            graded.extend(counted)
            raw = raw_score(tally, part.penalty, part.blank)
            max_raw = len(counted)
            raw_total += raw
            entry.update(
                correct=tally.correct,
                wrong=tally.wrong,
                blank=tally.blank,
                questions=max_raw,
                raw=rounded(raw),
            )
            if part.scoring is not None:
                score = transformed_score(raw, max_raw, part.scoring)
                transformed_total += score
                passed = score >= Fraction(str(part.scoring.pass_minimum))
                entry.update(transformed=rounded(score), max=part.scoring.max, passed=passed)
        parts.append(entry)
        previous_passed = passed

    result = _legacy_blob(registry, graded, locale)
    if not is_scored(preset):
        return result
    every_part_scored = all(part.scoring is not None for part in preset.parts)
    clock = exam.rules.get("clock")
    total_active = (
        round(float(clock.get("activeSeconds", 0.0)), 1)
        if isinstance(clock, dict) and "activeSeconds" in clock
        else round(sum(a.time_seconds for a in attempts if a.time_seconds is not None), 1)
    )
    result.update(
        parts=parts,
        raw=rounded(raw_total),
        transformed=rounded(transformed_total) if every_part_scored else None,
        max=sum(part.scoring.max for part in preset.parts if part.scoring) if every_part_scored else None,
        totalActiveSeconds=total_active,
    )
    if exam.rules.get("autoSubmitted"):
        result["autoSubmitted"] = True
    return result
