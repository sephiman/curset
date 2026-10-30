# SPDX-License-Identifier: AGPL-3.0-only
"""The attempts table — one row per opened attempt, fully reproducible from its seed."""

from __future__ import annotations

import uuid
from datetime import datetime
from enum import StrEnum

from sqlalchemy import (
    BigInteger,
    Boolean,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    ForeignKeyConstraint,
    Index,
    String,
    func,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from tradeschool.db import Base


class AttemptState(StrEnum):
    OPEN = "open"
    ANSWERED = "answered"
    ABANDONED = "abandoned"


class Attempt(Base):
    __tablename__ = "attempts"
    __table_args__ = (
        ForeignKeyConstraint(["course_id", "exercise_id"], ["exercises.course_id", "exercises.id"]),
        Index("ix_attempts_course_variant", "course_id", "variant_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id", ondelete="cascade"), index=True)
    # Every attempt belongs to one course, so no attempt can surface in another course's numbers.
    course_id: Mapped[str] = mapped_column(String, index=True)
    exercise_id: Mapped[str] = mapped_column(String, index=True)
    # The question inside a case exercise; null for every other exercise. A case's questions are
    # separate attempts, so a stat or a report is about one question, never about the whole case.
    question_id: Mapped[str | None] = mapped_column(String, nullable=True)
    # The quiz question the attempt showed, by its own id: grading, review, reports and stats follow
    # it to whichever exercise holds it today, so a rebuild that rebalances a bank moves nothing.
    # Null only for generated exercises (the seed is the question) and case questions (question_id).
    variant_id: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="the quiz question's own id"
    )
    # The seed fully determines the instantiated scenario (§3.2): any attempt is exactly replayable.
    seed: Mapped[int] = mapped_column(BigInteger, nullable=False)
    # Cached public instance for fast history rendering (regenerable from the seed).
    instance_snapshot: Mapped[dict[str, object]] = mapped_column(JSONB, nullable=False)
    given_answer: Mapped[dict[str, object] | None] = mapped_column(JSONB, nullable=True)
    is_correct: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    state: Mapped[AttemptState] = mapped_column(
        Enum(AttemptState, name="attempt_state"), nullable=False, default=AttemptState.OPEN
    )
    exam_session_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("exam_sessions.id", ondelete="cascade"), nullable=True, index=True
    )
    time_seconds: Mapped[float | None] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    answered_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
