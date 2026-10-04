# SPDX-License-Identifier: AGPL-3.0-only
"""256-bit single-use mailed tokens; only the SHA-256 is stored, and only the newest per purpose works."""

from __future__ import annotations

import base64
import hashlib
import secrets
import uuid
from datetime import UTC, datetime, timedelta
from enum import StrEnum

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.auth.models import EmailToken


class TokenPurpose(StrEnum):
    PASSWORD_RESET = "password_reset"
    EMAIL_VERIFICATION = "email_verification"


# A second link inside this window is silently skipped: a per-account cap on mail to one inbox.
RESEND_COOLDOWN = timedelta(seconds=60)


def _now() -> datetime:
    return datetime.now(UTC)


def _hash(token: str) -> str:
    return base64.urlsafe_b64encode(hashlib.sha256(token.encode()).digest()).rstrip(b"=").decode()


async def issued_recently(session: AsyncSession, user_id: uuid.UUID, purpose: TokenPurpose) -> bool:
    newest = await session.scalar(
        select(EmailToken.created_at)
        .where(EmailToken.user_id == user_id, EmailToken.purpose == purpose)
        .order_by(EmailToken.created_at.desc())
        .limit(1)
    )
    return newest is not None and newest > _now() - RESEND_COOLDOWN


async def issue(
    session: AsyncSession, user_id: uuid.UUID, purpose: TokenPurpose, email: str, ttl: timedelta
) -> str:
    await session.execute(
        delete(EmailToken).where(EmailToken.user_id == user_id, EmailToken.purpose == purpose)
    )
    token = base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b"=").decode()
    session.add(
        EmailToken(
            user_id=user_id,
            purpose=purpose,
            email=email,
            token_hash=_hash(token),
            expires_at=_now() + ttl,
        )
    )
    await session.commit()
    return token


async def find_active(session: AsyncSession, token: str, purpose: TokenPurpose) -> EmailToken | None:
    row = await session.scalar(
        select(EmailToken).where(EmailToken.token_hash == _hash(token), EmailToken.purpose == purpose)
    )
    if row is None or row.used_at is not None or row.expires_at <= _now():
        return None
    return row


def mark_used(row: EmailToken) -> None:
    row.used_at = _now()
