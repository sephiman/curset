# SPDX-License-Identifier: AGPL-3.0-only
"""Password reset by verified email: single-use 60-minute link, every session dies on use."""

from __future__ import annotations

from datetime import timedelta

from sqlalchemy import delete, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.auth import email_tokens
from tradeschool.auth.email_tokens import TokenPurpose
from tradeschool.auth.mail import Mailer
from tradeschool.auth.mail_texts import password_reset_mail
from tradeschool.auth.manager import UserManager
from tradeschool.auth.models import AccessToken, EmailToken, User
from tradeschool.errors import AppError

RESET_TTL = timedelta(minutes=60)


def _invalid() -> AppError:
    # One code for unknown, expired and used alike: which of the three it was is nobody's business.
    return AppError("RESET_TOKEN_INVALID", "This reset link is not valid.", status_code=400)


def link(public_url: str, token: str) -> str:
    return f"{public_url.rstrip('/')}/reset-password?token={token}"


async def request_for_email(session: AsyncSession, email: str, *, mailer: Mailer, public_url: str) -> None:
    """Silent for unknown or unverified addresses; the caller answers 202 either way."""
    user = await session.scalar(
        select(User).where(func.lower(User.email) == email, User.is_verified, User.is_active)
    )
    if user is None or user.email is None:
        return
    if await email_tokens.issued_recently(session, user.id, TokenPurpose.PASSWORD_RESET):
        return
    token = await email_tokens.issue(session, user.id, TokenPurpose.PASSWORD_RESET, user.email, RESET_TTL)
    minutes = int(RESET_TTL.total_seconds() // 60)
    subject, body = password_reset_mail(user.locale, user.username, link(public_url, token), minutes)
    mailer.send(user.email, subject, body)


async def _target(session: AsyncSession, token: str) -> tuple[EmailToken, User]:
    row = await email_tokens.find_active(session, token, TokenPurpose.PASSWORD_RESET)
    if row is None:
        raise _invalid()
    user = await session.get(User, row.user_id)
    if user is None or not user.is_active or user.email != row.email:
        raise _invalid()
    return row, user


async def validate(session: AsyncSession, token: str) -> None:
    await _target(session, token)


async def confirm(session: AsyncSession, token: str, new_password: str, *, user_manager: UserManager) -> None:
    row, user = await _target(session, token)
    await user_manager.set_password(user, new_password)  # InvalidPasswordException before any write
    email_tokens.mark_used(row)
    await session.execute(delete(AccessToken).where(AccessToken.__table__.c.user_id == user.id))
    await session.commit()
