# SPDX-License-Identifier: AGPL-3.0-only
"""User, session-token and mailed-link tables; identity is the **email**, name is optional.

Deliberately not inheriting ``SQLAlchemyBaseUserTableUUID``: that base brings default assumptions
about email indexing that curset spells out directly. See ``auth/manager.py``.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTableUUID
from fastapi_users_db_sqlalchemy.generics import GUID
from sqlalchemy import Boolean, DateTime, ForeignKey, String, false, func
from sqlalchemy.orm import Mapped, mapped_column

from tradeschool.db import Base


class User(Base):
    # Table name is "user" (fastapi-users default; the access-token FK targets it).
    __tablename__ = "user"

    id: Mapped[uuid.UUID] = mapped_column(GUID, primary_key=True, default=uuid.uuid4)
    # Primary identifier. Case-insensitive uniqueness + lookups are served by a functional UNIQUE index
    # on lower(email), created in the migration (expression indexes aren't modelled here).
    email: Mapped[str] = mapped_column(String(254), nullable=False)
    name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    hashed_password: Mapped[str] = mapped_column(String(1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    # Whether `email` is verified; any change of address resets it.
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    locale: Mapped[str] = mapped_column(String(2), nullable=False, default="en", server_default="en")
    # «Incluir ejercicios al exportar PDF»: one switch for every course and scope.
    pdf_exercises: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False, server_default=false()
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    # Opaque, server-stored, revocable session token (database strategy). Table: "accesstoken".
    pass


class EmailToken(Base):
    """A mailed single-use link; only the SHA-256 of the token is stored."""

    __tablename__ = "email_token"

    id: Mapped[uuid.UUID] = mapped_column(GUID, primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(
        GUID, ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True
    )
    purpose: Mapped[str] = mapped_column(String(32), nullable=False)
    # The address the link went to: a verification link dies when the user changes address.
    email: Mapped[str] = mapped_column(String(254), nullable=False)
    token_hash: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    used_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
