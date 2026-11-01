# SPDX-License-Identifier: AGPL-3.0-only
"""Email verification: send and confirm 48-hour single-use links."""

from __future__ import annotations

import logging
import uuid
from datetime import timedelta

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.auth import email_tokens
from tradeschool.auth.email_tokens import TokenPurpose
from tradeschool.auth.mail import Mailer
from tradeschool.auth.mail_texts import verification_mail
from tradeschool.auth.models import User
from tradeschool.errors import AppError

logger = logging.getLogger("tradeschool.auth")

VERIFY_TTL = timedelta(hours=48)


def _invalid() -> AppError:
    return AppError("VERIFY_TOKEN_INVALID", "This confirmation link is not valid.", status_code=400)


def link(public_url: str, token: str) -> str:
    return f"{public_url.rstrip('/')}/verify-email?token={token}"


async def ensure_available(session: AsyncSession, email: str, user_id: uuid.UUID | None = None) -> None:
    """Only an un-taken address can be registered or changed to."""
    holder = await session.scalar(
        select(User.id).where(func.lower(User.email) == email.lower(), User.id != user_id)
    )
    if holder is not None:
        raise AppError("EMAIL_ALREADY_USED", "That email belongs to another account.", status_code=409)


async def change_email(
    session: AsyncSession, user: User, email: str, *, mailer: Mailer, public_url: str
) -> User:
    normalized = email.strip().lower()
    if normalized == user.email.lower():
        return user
    await ensure_available(session, normalized, user.id)
    user.email = normalized
    user.is_verified = False
    await session.commit()
    logger.info("user_email_changed user=%s", user.id)
    await send_link(session, user, mailer=mailer, public_url=public_url)
    return user


async def send_link(session: AsyncSession, user: User, *, mailer: Mailer, public_url: str) -> None:
    """Silent no-op when mail is off, user is verified, or a link just went out."""
    if not mailer.enabled or user.is_verified:
        return
    if await email_tokens.issued_recently(session, user.id, TokenPurpose.EMAIL_VERIFICATION):
        return
    token = await email_tokens.issue(
        session, user.id, TokenPurpose.EMAIL_VERIFICATION, user.email, VERIFY_TTL
    )
    hours = int(VERIFY_TTL.total_seconds() // 3600)
    display_name = user.name or user.email.split("@")[0]
    subject, body = verification_mail(user.locale, display_name, link(public_url, token), hours)
    mailer.send(user.email, subject, body)
    logger.info("email_verification_sent user=%s", user.id)


async def confirm(session: AsyncSession, token: str) -> None:
    row = await email_tokens.find_active(session, token, TokenPurpose.EMAIL_VERIFICATION)
    if row is None:
        raise _invalid()
    user = await session.get(User, row.user_id)
    if user is None or not user.is_active or user.email != row.email:
        raise _invalid()
    await ensure_available(session, row.email, user.id)
    user.is_verified = True
    email_tokens.mark_used(row)
    await session.commit()
    logger.info("email_verified user=%s", user.id)
