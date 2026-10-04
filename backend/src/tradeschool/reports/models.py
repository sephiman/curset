# SPDX-License-Identifier: AGPL-3.0-only
"""A learner's report that a question is wrong: everything the team needs, frozen when it was sent."""

from __future__ import annotations

import uuid
from datetime import datetime

from fastapi_users_db_sqlalchemy.generics import GUID
from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from tradeschool.db import Base


class QuestionReport(Base):
    """Its own lane: nothing here is read by attempts, progress or statistics."""

    __tablename__ = "question_reports"

    id: Mapped[uuid.UUID] = mapped_column(GUID, primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(GUID, ForeignKey("user.id", ondelete="cascade"), index=True)
    # One report per attempt, enforced here rather than trusted to the client.
    attempt_id: Mapped[uuid.UUID] = mapped_column(
        GUID, ForeignKey("attempts.id", ondelete="cascade"), unique=True
    )
    message: Mapped[str] = mapped_column(Text, nullable=False)
    course_id: Mapped[str] = mapped_column(String, nullable=False)
    module_id: Mapped[str] = mapped_column(String, nullable=False)
    lesson_id: Mapped[str] = mapped_column(String, nullable=False)
    exercise_id: Mapped[str] = mapped_column(String, nullable=False)
    variant_id: Mapped[str] = mapped_column(String, nullable=False)
    seed: Mapped[int] = mapped_column(BigInteger, nullable=False)
    reading_locale: Mapped[str] = mapped_column(String(2), nullable=False)
    prompt: Mapped[str] = mapped_column(Text, nullable=False)
    given_answer: Mapped[str] = mapped_column(Text, nullable=False)
    correct_answer: Mapped[str] = mapped_column(Text, nullable=False)
    username: Mapped[str] = mapped_column(String(32), nullable=False)
    link: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), index=True
    )
    # Null until the mail server accepted it; a pending report is retried, never dropped.
    emailed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    email_attempts: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
