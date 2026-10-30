# SPDX-License-Identifier: AGPL-3.0-only
"""Exam lifecycle under the course's presets: draw, deferred answers, case marks, the clock, grading.

Exam attempts live in their own lane (``exam_session_id`` set) and never touch practice stats. The
practice generators are reused verbatim, so charts get the exercise-mode series, cut before resolution.
Every rule comes from the preset (`exams/presets.py`); a session stores the preset it was taken with.
"""

from __future__ import annotations

import logging
import secrets
import uuid
from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.attempts.models import Attempt, AttemptState
from tradeschool.attempts.service import question_ref
from tradeschool.citations.excerpt_store import SolutionText
from tradeschool.content.registry import CourseRegistry, QuestionRef
from tradeschool.content.text import LocalizedText
from tradeschool.errors import AppError
from tradeschool.exams.draw import DrawError, draw_part, preset_targets
from tradeschool.exams.layout import attempt_layout, case_marks, offered_cases
from tradeschool.exams.models import ExamSession
from tradeschool.exams.presets import ExamPreset, PresetPart, PresetSource
from tradeschool.exams.results import counted_outcomes, grade_session
from tradeschool.exercises.base import GeneratedInstance, GradeResult
from tradeschool.exercises.registry import get_generator
from tradeschool.exercises.types import ExerciseType
from tradeschool.stats.by_lesson import lesson_table

#: Answers sent this long after the clock ran out still land: the request left before it did.
logger = logging.getLogger("tradeschool.exams")

ANSWER_GRACE = timedelta(seconds=15)

#: Legacy (before presets): the frozen question order as exercise KEYS, one per module.
QUESTION_ORDER = "questionOrder"
#: The frozen question order as attempt ids — a case or a variant draw repeats an exercise key.
ATTEMPT_ORDER = "attemptOrder"


# --- sentinel answers: let review reveal the correct answer + solution for an UNANSWERED question ---
# grade() computes the correct answer from the seed regardless of the input, but guards the input's
# shape first, so a structurally-valid (wrong) answer is enough to extract the solution.
def _sentinel_answer(exercise_type: ExerciseType, payload: Mapping[str, object]) -> dict[str, object]:
    if exercise_type is ExerciseType.PATTERN_CHART:
        return {"label": ""}
    if exercise_type in (ExerciseType.SYNTHETIC_CHART, ExerciseType.FIXTURE_CHART):
        return {"divergence": ""}
    if exercise_type is ExerciseType.QUIZ:
        kind = payload.get("kind")
        if kind == "multi_select":
            return {"optionIds": []}
        if kind == "true_false":
            return {"value": False}
        if kind == "ordering":
            return {"order": []}
        if kind == "matching":
            return {"pairs": {}}
        return {"optionId": ""}  # single_choice
    return {"optionId": ""}  # calculation


# --- view models handed to the router/schemas ---
@dataclass
class ExamQuestionView:
    index: int
    attempt_id: uuid.UUID
    module_id: str
    module_title: str
    block_id: str
    block_title: str
    exercise_id: str
    exercise_type: ExerciseType
    instance: GeneratedInstance
    given_answer: dict[str, object] | None
    answered: bool
    part_id: str = ""
    lesson_id: str | None = None
    #: A case question: the case is `exercise_id`, this is the question inside it.
    question_id: str | None = None
    reserve: bool = False
    # Reveal-only (submitted session review):
    lesson_anchor: str | None = None
    citation: str | None = None
    time_seconds: float | None = None
    excerpt: SolutionText | None = None
    is_correct: bool | None = None
    unanswered: bool = False
    result: GradeResult | None = None


@dataclass
class ExamCaseView:
    exercise_id: str
    title: str
    scenario: str


@dataclass
class ExamPartView:
    id: str
    title: str | None
    kind: str  # "questions" | "cases"
    counted: int
    reserve: int
    choose: int | None
    penalty: str
    cases: list[ExamCaseView] = field(default_factory=list)
    marked: list[str] = field(default_factory=list)


@dataclass
class ExamView:
    id: uuid.UUID
    preset_id: str
    preset_version: int
    preset_title: str
    target: str | None
    target_title: str | None
    status: str
    created_at: datetime
    finished_at: datetime | None
    deadline: datetime | None
    pause: str = "between-questions"
    paused: bool = False
    active_seconds: float = 0.0
    parts: list[ExamPartView] = field(default_factory=list)
    questions: list[ExamQuestionView] = field(default_factory=list)
    result: dict[str, object] | None = None
    #: Revealed only: the «Por tema» table and lists, computed from the stored answers (so past exams too).
    by_lesson: dict[str, object] | None = None


# --- the preset a session runs under ---
def _preset_id(exam: ExamSession) -> str:
    """Sessions from before presets stored a scope; its name is the crypto preset that replaced it."""
    return str(exam.rules.get("presetId") or exam.rules.get("scope") or "global")


def target_of(exam: ExamSession) -> str | None:
    target = exam.rules.get("target") if "presetId" in exam.rules else exam.rules.get("blockId")
    return target if isinstance(target, str) else None


def _find_preset(registry: CourseRegistry, preset_id: str) -> ExamPreset | None:
    return next((p for p in registry.manifest.exams if p.id == preset_id), None)


def session_preset(registry: CourseRegistry, exam: ExamSession) -> ExamPreset:
    """The rules this sitting was taken under: its own snapshot, else (legacy) the course's preset by id."""
    snapshot = exam.rules.get("preset")
    if isinstance(snapshot, dict):
        return ExamPreset.model_validate(snapshot)
    found = _find_preset(registry, _preset_id(exam))
    if found is not None:
        return found
    name = _preset_id(exam)
    return ExamPreset(
        id=name,
        version=1,
        title=LocalizedText(en=name, es=name),
        parts=[PresetPart(id="main", source=PresetSource(course=True), draw="per-module")],
    )


def target_title(registry: CourseRegistry, preset: ExamPreset, target: str | None, locale: str) -> str | None:
    if target is None:
        return None
    if preset.parametric == "module":
        return registry.module_title(target, locale)
    if preset.parametric == "lesson":
        location = registry.lesson_location(target)
        return location.lesson.title.get(locale) if location else None
    return registry.block_title(target, locale)


def deadline_of(preset: ExamPreset, exam: ExamSession) -> datetime | None:
    if preset.time_limit_minutes is None:
        return None
    if preset.pause == "never":
        return exam.created_at + timedelta(minutes=preset.time_limit_minutes)
    clock = exam.rules.get("clock")
    if not isinstance(clock, dict):
        return exam.created_at + timedelta(minutes=preset.time_limit_minutes)
    active = float(clock.get("activeSeconds", 0.0))
    now = datetime.now(UTC)
    if not clock.get("paused") and clock.get("lastResumedAt"):
        resumed_dt = datetime.fromisoformat(clock["lastResumedAt"])
        active += (now - resumed_dt).total_seconds()
    remaining = max(0.0, preset.time_limit_minutes * 60 - active)
    return now + timedelta(seconds=remaining)


async def _load_owned(
    session: AsyncSession, user_id: uuid.UUID, exam_id: uuid.UUID, course_id: str
) -> ExamSession:
    """The user's exam, IN this course. A course-scoped URL naming another course's exam is a miss,
    not a leak: it 404s exactly as an unknown id does, so the URL can never lie about what it holds."""
    exam = await session.get(ExamSession, exam_id)
    if exam is None or exam.user_id != user_id or exam.course_id != course_id:
        raise AppError("EXAM_NOT_FOUND", "No such exam session.", status_code=404)
    return exam


async def _open_sessions(session: AsyncSession, user_id: uuid.UUID, course_id: str) -> list[ExamSession]:
    rows = await session.scalars(
        select(ExamSession)
        .where(
            ExamSession.user_id == user_id,
            ExamSession.course_id == course_id,
            ExamSession.finished_at.is_(None),
        )
        .order_by(ExamSession.created_at.desc())
    )
    return [s for s in rows.all() if s.rules.get("status") == "open"]


async def _attempts_of(session: AsyncSession, exam_id: uuid.UUID) -> list[Attempt]:
    """Ordered by id so the fallback path below is deterministic. The database has no inherent row
    order, and an unordered fetch made two renders of one exam disagree wherever the sort key tied."""
    rows = await session.scalars(
        select(Attempt).where(Attempt.exam_session_id == exam_id).order_by(Attempt.id)
    )
    return list(rows.all())


async def _abandon(session: AsyncSession, exam: ExamSession) -> None:
    exam.finished_at = datetime.now(UTC)
    exam.rules = {**exam.rules, "status": "abandoned"}
    await session.execute(
        update(Attempt).where(Attempt.exam_session_id == exam.id).values(state=AttemptState.ABANDONED)
    )


def _canonical_order(registry: CourseRegistry) -> dict[str, int]:
    return {module.id: i for i, (_, module) in enumerate(registry.manifest.iter_modules())}


def _frozen_order(exam: ExamSession) -> dict[str, int] | None:
    """The order this exam was assembled in, or `None` for a session written before it was frozen."""
    order = exam.rules.get(QUESTION_ORDER)
    if not isinstance(order, list) or not order:
        return None
    return {str(key): index for index, key in enumerate(order)}


def _result_for_view(registry: CourseRegistry, result: dict[str, object]) -> dict[str, object]:
    """A stored result blob speaks keys (`moduleId`, a part's `case`); the view speaks display ids."""
    out = dict(result)
    modules = result.get("modules")
    if isinstance(modules, list):
        out["modules"] = [
            {**m, "moduleId": registry.module_id_for_key(str(m.get("moduleId"))) or m.get("moduleId")}
            if isinstance(m, dict)
            else m
            for m in modules
        ]
    parts = result.get("parts")
    if isinstance(parts, list):
        out["parts"] = [
            {**p, "case": registry.exercise_id_for_key(str(p["case"])) or p["case"]}
            if isinstance(p, dict) and p.get("case")
            else p
            for p in parts
        ]
    return out


def _sorter(exam: ExamSession, registry: CourseRegistry) -> dict[str, int] | None:
    order = exam.rules.get(ATTEMPT_ORDER)
    if isinstance(order, list) and order:
        return {str(attempt_id): index for index, attempt_id in enumerate(order)}
    return None


def _question_location(
    registry: CourseRegistry, exercise_id: str, question_id: str | None
) -> tuple[str, str]:
    """(block, module) the question counts under — for a case question, the lesson it names."""
    if question_id is not None:
        lesson_id = registry.question_lesson_id(exercise_id, question_id)
        location = registry.lesson_location(lesson_id) if lesson_id else None
        if location is not None:
            return location.block.id, location.module.id
    return registry.exercise_location(exercise_id) or ("", "")


def _ordered(exam: ExamSession, registry: CourseRegistry, attempts: list[Attempt]) -> list[Attempt]:
    # The order is FROZEN at assembly and read back here, rather than re-derived from today's manifest.
    # Re-deriving made an exam disagree with itself: the sort ran over the CURRENT module order, so a
    # display renumbering — which this repo supports on purpose, keys being permanent and ids not —
    # reordered the questions of an exam already sitting in review, and the `index` the UI paginates
    # by moved under it. Attempt ids and keys are permanent, so a frozen list survives a renumbering.
    by_attempt = _sorter(exam, registry)
    if by_attempt is not None:
        return sorted(attempts, key=lambda a: by_attempt.get(str(a.id), len(by_attempt)))
    frozen = _frozen_order(exam)
    if frozen is not None:
        return sorted(attempts, key=lambda a: frozen.get(a.exercise_id, len(frozen)))
    # Sessions assembled before the order was frozen. Same derivation as before, and `_attempts_of`
    # orders by id so the ties this produces resolve the same way on every render.
    canonical = _canonical_order(registry)

    def legacy_key(a: Attempt) -> int:
        loc = registry.exercise_location(question_ref(registry, a).exercise_id)
        return canonical.get(loc[1], 10_000) if loc else 10_000

    return sorted(attempts, key=legacy_key)


def _parts_view(
    registry: CourseRegistry,
    exam: ExamSession,
    preset: ExamPreset,
    layout: dict[str, tuple[str, bool]],
    locale: str,
) -> list[ExamPartView]:
    offered = offered_cases(exam)
    marks = case_marks(exam)
    views: list[ExamPartView] = []
    for part in preset.parts:
        placed = [reserve for part_id, reserve in layout.values() if part_id == part.id]
        cases: list[ExamCaseView] = []
        for key in offered.get(part.id, []):
            exercise_id = registry.exercise_id_for_key(key) or key
            config = registry.case_config(exercise_id)
            if config is not None:
                cases.append(ExamCaseView(exercise_id, config.title.get(locale), config.scenario.get(locale)))
        counted = part.questions if part.cases else sum(1 for reserve in placed if not reserve)
        views.append(
            ExamPartView(
                id=part.id,
                title=part.title.get(locale) if part.title else None,
                kind="cases" if part.cases else "questions",
                counted=counted or 0,
                reserve=part.reserve,
                choose=part.choose,
                penalty=str(part.penalty),
                cases=cases,
                marked=[registry.exercise_id_for_key(k) or k for k in marks.get(part.id, [])],
            )
        )
    return views


def _build_view(
    session_obj: ExamSession,
    registry: CourseRegistry,
    attempts: list[Attempt],
    locale: str,
    reveal: bool,
) -> ExamView:
    preset = session_preset(registry, session_obj)
    layout = attempt_layout(session_obj, preset)
    default_part = preset.parts[0].id
    questions: list[ExamQuestionView] = []
    for index, attempt in enumerate(_ordered(session_obj, registry, attempts)):
        ref = question_ref(registry, attempt)
        exercise_id = ref.exercise_id
        config = registry.attempt_config(ref)
        if config is None:
            continue  # exercise deactivated since the exam ran — skip defensively
        exercise_type, cfg = config
        generator = get_generator(exercise_type)
        instance = generator.generate(cfg, attempt.seed, locale)
        b_id, m_id = _question_location(registry, exercise_id, attempt.question_id)
        part_id, reserve = layout.get(str(attempt.id), (default_part, False))
        answered = attempt.given_answer is not None
        q = ExamQuestionView(
            index=index,
            attempt_id=attempt.id,
            module_id=m_id,
            module_title=registry.module_title(m_id, locale) or m_id,
            block_id=b_id,
            block_title=registry.block_title(b_id, locale) or b_id,
            exercise_id=exercise_id,
            exercise_type=exercise_type,
            instance=instance,
            given_answer=attempt.given_answer,
            answered=answered,
            part_id=part_id,
            lesson_id=registry.question_lesson_id(exercise_id, attempt.question_id),
            question_id=attempt.question_id,
            reserve=reserve,
        )
        if reveal:
            sentinel = _sentinel_answer(exercise_type, instance.payload)
            reveal_answer = attempt.given_answer if attempt.given_answer is not None else sentinel
            try:
                q.result = generator.grade(cfg, attempt.seed, reveal_answer, locale)
            except Exception:
                # A malformed stored answer can't be graded; still reveal the correct answer + solution.
                q.result = generator.grade(cfg, attempt.seed, sentinel, locale)
            q.unanswered = not answered
            q.is_correct = bool(attempt.is_correct) and answered
            q.time_seconds = attempt.time_seconds
            link = registry.question_link(ref, locale)
            q.lesson_anchor, q.citation = (link.anchor, link.citation) if link else (None, None)
            q.excerpt = registry.question_excerpt(ref)
        questions.append(q)

    target = target_of(session_obj)
    result = session_obj.rules.get("result")
    clock = session_obj.rules.get("clock")
    paused = False
    active_seconds = 0.0
    now = datetime.now(UTC)
    if isinstance(clock, dict):
        paused = bool(clock.get("paused", False))
        active_seconds = float(clock.get("activeSeconds", 0.0))
        if preset.pause == "never":
            started = clock.get("startedAt")
            if started:
                started_dt = datetime.fromisoformat(started)
                end_time = session_obj.finished_at or now
                active_seconds = max(0.0, (end_time - started_dt).total_seconds())
        elif not paused and session_obj.rules.get("status") == "open":
            last_resumed = clock.get("lastResumedAt")
            if last_resumed:
                resumed_dt = datetime.fromisoformat(last_resumed)
                active_seconds += max(0.0, (now - resumed_dt).total_seconds())
    return ExamView(
        id=session_obj.id,
        preset_id=preset.id,
        preset_version=preset.version,
        preset_title=preset.title.get(locale),
        target=target,
        target_title=target_title(registry, preset, target, locale),
        status=str(session_obj.rules.get("status", "open")),
        created_at=session_obj.created_at,
        finished_at=session_obj.finished_at,
        deadline=deadline_of(preset, session_obj),
        pause=preset.pause or "between-questions",
        paused=paused,
        active_seconds=round(active_seconds, 1),
        parts=_parts_view(registry, session_obj, preset, layout, locale),
        questions=questions,
        result=_result_for_view(registry, result) if isinstance(result, dict) else None,
        by_lesson=lesson_table(registry, counted_outcomes(registry, session_obj, preset, attempts), locale)
        if reveal
        else None,
    )


# --- lifecycle ---
def _resolve_start(
    registry: CourseRegistry, preset_id: str, target: str | None
) -> tuple[ExamPreset, str | None]:
    preset = _find_preset(registry, preset_id)
    if preset is None:
        raise AppError("EXAM_BAD_SCOPE", f"Unknown exam {preset_id!r}.", status_code=400)
    if preset.parametric is None:
        return preset, None
    known = {
        "block": {b.id for b in registry.manifest.blocks},
        "module": registry.manifest.module_ids(),
        "lesson": {lesson.id for _, lesson in registry.manifest.iter_lessons()},
    }[preset.parametric]
    if target not in known:
        raise AppError("EXAM_BAD_SCOPE", f"Unknown {preset.parametric} {target!r}.", status_code=400)
    if target not in preset_targets(registry, preset):
        raise AppError("EXAM_EMPTY", f"Nothing to examine in {target!r}.", status_code=409)
    return preset, target


async def start_exam(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    course_id: str,
    preset_id: str,
    target: str | None,
    locale: str,
) -> ExamView:
    preset, target = _resolve_start(registry, preset_id, target)

    # Starting a sitting of a preset (and target) closes any open one of the same.
    replaced: list[uuid.UUID] = []
    for existing in await _open_sessions(session, user_id, course_id):
        if _preset_id(existing) == preset.id and target_of(existing) == target:
            await _abandon(session, existing)
            replaced.append(existing.id)

    exam = ExamSession(
        user_id=user_id,
        course_id=course_id,
        rules={
            "presetId": preset.id,
            "presetVersion": preset.version,
            "target": target,
            "status": "open",
            # The rules as they were when the sitting began: grading and review never read a later edit.
            "preset": preset.model_dump(mode="json"),
        },
    )
    session.add(exam)
    await session.flush()  # assign exam.id for the attempt FK

    order: list[str] = []
    parts: list[dict[str, object]] = []
    for part in preset.parts:
        try:
            drawn = draw_part(registry, part, target, secrets)
        except DrawError as exc:
            raise AppError("EXAM_EMPTY", str(exc), status_code=409) from exc
        counted: list[str] = []
        reserve: list[str] = []
        for question in drawn.questions:
            config = registry.attempt_config(
                QuestionRef(question.exercise_id, question.question_id, question.variant_id)
            )
            assert config is not None  # the draw only names playable questions
            exercise_type, cfg = config
            instance = get_generator(exercise_type).generate(cfg, question.seed, locale)
            attempt = Attempt(
                id=uuid.uuid4(),
                user_id=user_id,
                course_id=course_id,
                exercise_id=registry.exercise_key(question.exercise_id),  # rows store the permanent key
                question_id=question.question_id,
                variant_id=question.variant_id,
                seed=question.seed,
                instance_snapshot={
                    "type": exercise_type.value,
                    "prompt": instance.prompt,
                    "payload": instance.payload,
                },
                state=AttemptState.OPEN,
                exam_session_id=exam.id,
            )
            session.add(attempt)
            (reserve if question.reserve else counted).append(str(attempt.id))
            order.append(str(attempt.id))
        parts.append(
            {
                "id": part.id,
                "attempts": counted,
                "reserve": reserve,
                "cases": [registry.exercise_key(case_id) for case_id in drawn.cases],
            }
        )
    # Recorded now rather than re-derived at every render. Additive: it goes in the `rules` JSONB the
    # session already has, so no schema migration.
    now = datetime.now(UTC)
    clock = {
        "activeSeconds": 0.0,
        "paused": False,
        "lastResumedAt": now.isoformat(),
        "startedAt": now.isoformat(),
    }
    exam.rules = {**exam.rules, ATTEMPT_ORDER: order, "parts": parts, "clock": clock}
    await session.commit()
    logger.info(
        "exam_started exam=%s preset=%s target=%s questions=%d replaced=%s",
        exam.id,
        preset.id,
        target,
        len(order),
        ",".join(map(str, replaced)) or "none",
    )
    return _build_view(exam, registry, await _attempts_of(session, exam.id), locale, reveal=False)


async def open_exams(
    session: AsyncSession, registry: CourseRegistry, user_id: uuid.UUID, course_id: str, locale: str
) -> list[ExamView]:
    """EVERY open sitting, newest first — not just the most recent one.

    Starting an exam closes an open one of the same preset and target only, so two sittings can be open
    at once; each needs a route to be resumed or abandoned. The Android app lists every open sitting too.
    """
    return [
        _build_view(exam, registry, await _attempts_of(session, exam.id), locale, reveal=False)
        for exam in await _open_sessions(session, user_id, course_id)
    ]


async def render_exam(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    exam_id: uuid.UUID,
    course_id: str,
    locale: str,
) -> ExamView:
    exam = await _load_owned(session, user_id, exam_id, course_id)
    if exam.rules.get("status") != "open":
        raise AppError("EXAM_NOT_OPEN", "This exam is not in progress.", status_code=409)
    return _build_view(exam, registry, await _attempts_of(session, exam.id), locale, reveal=False)


def _exam_clock(exam: ExamSession) -> dict[str, object]:
    clock = exam.rules.get("clock")
    if isinstance(clock, dict):
        return dict(clock)
    return {}


def _active_seconds(clock: Mapping[str, object]) -> float:
    val = clock.get("activeSeconds")
    return float(val) if isinstance(val, (int, float, str)) else 0.0


def _check_writable(registry: CourseRegistry, exam: ExamSession) -> None:
    if exam.rules.get("status") != "open":
        raise AppError("EXAM_NOT_OPEN", "This exam is not in progress.", status_code=409)
    if _exam_clock(exam).get("paused"):
        raise AppError("EXAM_PAUSED", "This exam is currently paused.", status_code=409)
    deadline = deadline_of(session_preset(registry, exam), exam)
    if deadline is not None and datetime.now(UTC) > deadline + ANSWER_GRACE:
        raise AppError("EXAM_TIME_UP", "The time for this exam is over.", status_code=409)


async def answer_question(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    exam_id: uuid.UUID,
    course_id: str,
    attempt_id: uuid.UUID,
    answer: Mapping[str, object] | None = None,
    time_seconds: float | None = None,
    clock_used_seconds: float | None = None,
) -> None:
    """Store (or replace) an answer. No grading, no reveal — feedback comes only at submission."""
    exam = await _load_owned(session, user_id, exam_id, course_id)
    _check_writable(registry, exam)
    attempt = await session.get(Attempt, attempt_id)
    if attempt is None or attempt.exam_session_id != exam_id:
        raise AppError("EXAM_QUESTION_NOT_FOUND", "No such question in this exam.", status_code=404)
    if answer is not None:
        attempt.given_answer = dict(answer)
    if time_seconds is not None:
        attempt.time_seconds = time_seconds
    now = datetime.now(UTC)
    clock = _exam_clock(exam)
    if clock:
        if clock_used_seconds is not None:
            clock["activeSeconds"] = clock_used_seconds
            clock["lastResumedAt"] = now.isoformat()
        elif not clock.get("paused") and clock.get("lastResumedAt"):
            resumed_dt = datetime.fromisoformat(str(clock["lastResumedAt"]))
            active = _active_seconds(clock) + (now - resumed_dt).total_seconds()
            clock["activeSeconds"] = active
            clock["lastResumedAt"] = now.isoformat()
        exam.rules = {**exam.rules, "clock": clock}
    await session.commit()
    logger.info("exam_answer_saved exam=%s attempt=%s", exam_id, attempt_id)


async def pause_exam(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    exam_id: uuid.UUID,
    course_id: str,
    attempt_id: uuid.UUID | None = None,
) -> None:
    exam = await _load_owned(session, user_id, exam_id, course_id)
    if exam.rules.get("status") != "open":
        raise AppError("EXAM_NOT_OPEN", "This exam is not in progress.", status_code=409)
    preset = session_preset(registry, exam)
    if preset.pause != "between-questions":
        raise AppError("EXAM_PAUSE_NOT_ALLOWED", "This exam cannot be paused.", status_code=409)
    if attempt_id is not None:
        attempt = await session.get(Attempt, attempt_id)
        if attempt is None or attempt.exam_session_id != exam_id:
            raise AppError("EXAM_QUESTION_NOT_FOUND", "No such question in this exam.", status_code=404)
        if attempt.given_answer is None:
            raise AppError(
                "EXAM_PAUSE_NOT_ANSWERED",
                "You can only pause after answering the current question.",
                status_code=409,
            )
    else:
        attempts = await _attempts_of(session, exam_id)
        answered = [a for a in attempts if a.given_answer is not None]
        if not answered:
            raise AppError(
                "EXAM_PAUSE_NOT_ANSWERED",
                "You can only pause after answering the current question.",
                status_code=409,
            )

    clock = _exam_clock(exam)
    now = datetime.now(UTC)
    active = _active_seconds(clock)
    if not clock.get("paused") and clock.get("lastResumedAt"):
        resumed_dt = datetime.fromisoformat(str(clock["lastResumedAt"]))
        active += (now - resumed_dt).total_seconds()
    clock["activeSeconds"] = round(active, 1)
    clock["paused"] = True
    clock["lastResumedAt"] = None
    exam.rules = {**exam.rules, "clock": clock}
    await session.commit()
    logger.info("exam_paused exam=%s activeSeconds=%.1f", exam_id, active)


async def resume_exam(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    exam_id: uuid.UUID,
    course_id: str,
) -> None:
    exam = await _load_owned(session, user_id, exam_id, course_id)
    if exam.rules.get("status") != "open":
        raise AppError("EXAM_NOT_OPEN", "This exam is not in progress.", status_code=409)
    clock = _exam_clock(exam)
    if not clock.get("paused"):
        raise AppError("EXAM_NOT_PAUSED", "Exam is not paused.", status_code=409)
    now = datetime.now(UTC)
    clock["paused"] = False
    clock["lastResumedAt"] = now.isoformat()
    exam.rules = {**exam.rules, "clock": clock}
    await session.commit()
    logger.info("exam_resumed exam=%s", exam_id)


async def mark_cases(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    exam_id: uuid.UUID,
    course_id: str,
    part_id: str,
    exercise_ids: list[str],
) -> None:
    """Which cases of a part the learner marked. Any number is stored; grading takes exactly one."""
    exam = await _load_owned(session, user_id, exam_id, course_id)
    _check_writable(registry, exam)
    offered = offered_cases(exam).get(part_id)
    if not offered:
        raise AppError("EXAM_PART_NOT_FOUND", f"No case part {part_id!r} in this exam.", status_code=404)
    keys = [registry.exercise_key(eid) for eid in exercise_ids if eid in registry.exercise_configs]
    if len(keys) != len(exercise_ids) or not set(keys) <= set(offered):
        raise AppError(
            "EXAM_CASE_NOT_OFFERED", "Only the cases this part offers can be marked.", status_code=400
        )
    marks = case_marks(exam)
    marks[part_id] = sorted(set(keys), key=offered.index)
    exam.rules = {**exam.rules, "caseMarks": marks}
    await session.commit()
    logger.info("exam_cases_marked exam=%s part=%s marked=%d", exam_id, part_id, len(marks[part_id]))


async def submit_exam(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    exam_id: uuid.UUID,
    course_id: str,
    locale: str,
) -> ExamView:
    exam = await _load_owned(session, user_id, exam_id, course_id)
    if exam.rules.get("status") != "open":
        raise AppError("EXAM_NOT_OPEN", "This exam is not in progress.", status_code=409)

    attempts = await _attempts_of(session, exam_id)
    now = datetime.now(UTC)
    preset = session_preset(registry, exam)
    deadline = deadline_of(preset, exam)
    if deadline is not None and now >= deadline:
        exam.rules = {**exam.rules, "autoSubmitted": True}
    clock = _exam_clock(exam)
    if clock:
        active = _active_seconds(clock)
        if preset.pause == "never":
            started = clock.get("startedAt")
            if started:
                started_dt = datetime.fromisoformat(str(started))
                active = max(0.0, (now - started_dt).total_seconds())
        elif not clock.get("paused") and clock.get("lastResumedAt"):
            resumed_dt = datetime.fromisoformat(str(clock["lastResumedAt"]))
            active += (now - resumed_dt).total_seconds()
        clock["activeSeconds"] = round(active, 1)
        clock["paused"] = True
        clock["lastResumedAt"] = None
        exam.rules = {**exam.rules, "clock": clock}
    for attempt in attempts:
        config = registry.attempt_config(question_ref(registry, attempt))
        answered = attempt.given_answer is not None
        is_correct = False
        if answered and config is not None:
            exercise_type, cfg = config
            try:
                is_correct = (
                    get_generator(exercise_type)
                    .grade(cfg, attempt.seed, attempt.given_answer or {}, locale)
                    .correct
                )
            except Exception:
                is_correct = False
        # Unanswered (or ungradeable) → incorrect, but kept distinct in review via given_answer is None.
        attempt.is_correct = is_correct
        attempt.state = AttemptState.ANSWERED
        attempt.answered_at = now

    result = grade_session(registry, exam, preset, attempts, locale)
    exam.finished_at = now
    exam.rules = {**exam.rules, "status": "submitted", "result": result}
    await session.commit()
    logger.info(
        "exam_submitted exam=%s preset=%s questions=%d answered=%d correct=%d",
        exam_id,
        preset.id,
        len(attempts),
        sum(a.given_answer is not None for a in attempts),
        sum(bool(a.is_correct) for a in attempts),
    )
    return _build_view(exam, registry, await _attempts_of(session, exam_id), locale, reveal=True)


async def abandon_exam(session: AsyncSession, user_id: uuid.UUID, exam_id: uuid.UUID, course_id: str) -> None:
    exam = await _load_owned(session, user_id, exam_id, course_id)
    if exam.rules.get("status") == "open":
        await _abandon(session, exam)
        await session.commit()
        logger.info("exam_abandoned exam=%s", exam_id)


async def review_exam(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    exam_id: uuid.UUID,
    course_id: str,
    locale: str,
) -> ExamView:
    exam = await _load_owned(session, user_id, exam_id, course_id)
    if exam.rules.get("status") != "submitted":
        raise AppError("EXAM_NOT_SUBMITTED", "This exam has no results to review.", status_code=409)
    return _build_view(exam, registry, await _attempts_of(session, exam_id), locale, reveal=True)


async def exam_history(session: AsyncSession, user_id: uuid.UUID, course_id: str) -> list[ExamSession]:
    """Submitted sessions, newest first (abandoned/open excluded — they count toward nothing)."""
    rows = await session.scalars(
        select(ExamSession)
        .where(
            ExamSession.user_id == user_id,
            ExamSession.course_id == course_id,
            ExamSession.finished_at.is_not(None),
        )
        .order_by(ExamSession.finished_at.desc())
    )
    return [s for s in rows.all() if s.rules.get("status") == "submitted"]
