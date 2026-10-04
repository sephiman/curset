# SPDX-License-Identifier: AGPL-3.0-only
"""Which courses a user has active, and the language they read each one in."""

from __future__ import annotations

import uuid

from fastapi_users_db_sqlalchemy.generics import GUID
from sqlalchemy import Boolean, ForeignKey, Index, String, text
from sqlalchemy.orm import Mapped, mapped_column

from tradeschool.db import Base


class UserCourse(Base):
    """One row per course the user has ever activated; disabling keeps the row and every progress row."""

    __tablename__ = "user_courses"
    # At most one selected course per user: the one the whole web is showing.
    __table_args__ = (
        Index("uq_user_courses_selected", "user_id", unique=True, postgresql_where=text("selected")),
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        GUID, ForeignKey("user.id", ondelete="cascade"), primary_key=True
    )
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), primary_key=True)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default="true")
    # The course last viewed; only meaningful while active (the service falls back otherwise).
    selected: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default="false")
    # The reading language the user picked for this course; null = follow the account language.
    reading_locale: Mapped[str | None] = mapped_column(String(2), nullable=True)
