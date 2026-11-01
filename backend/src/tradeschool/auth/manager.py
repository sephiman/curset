# SPDX-License-Identifier: AGPL-3.0-only
"""User manager: Argon2 hashing, password policy, email-keyed identity."""

from __future__ import annotations

import logging
import uuid
from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends, Request, Response
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users.exceptions import InvalidPasswordException, UserAlreadyExists
from fastapi_users.password import PasswordHelper
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.auth.models import User
from tradeschool.auth.schemas import Locale, derive_name_from_email, normalize_email
from tradeschool.config import get_settings
from tradeschool.db import get_async_session

logger = logging.getLogger("tradeschool.auth")

# House requirement: Argon2 password hashing.
password_helper = PasswordHelper(PasswordHash((Argon2Hasher(),)))

MIN_PASSWORD_LENGTH = 8


class UserDatabase(SQLAlchemyUserDatabase[User, uuid.UUID]):  # type: ignore[type-var]
    """SQLAlchemy adapter keyed on case-insensitive ``email``."""

    async def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(func.lower(User.email) == func.lower(email))
        return await self._get_user(statement)


async def get_user_db(
    session: Annotated[AsyncSession, Depends(get_async_session)],
) -> AsyncGenerator[UserDatabase]:
    yield UserDatabase(session, User)


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):  # type: ignore[type-var]
    reset_password_token_secret = get_settings().auth_secret
    verification_token_secret = get_settings().auth_secret

    async def validate_password(self, password: str, user: object = None) -> None:
        if len(password) < MIN_PASSWORD_LENGTH:
            raise InvalidPasswordException(f"Password must be at least {MIN_PASSWORD_LENGTH} characters.")

    async def on_after_register(self, user: User, request: Request | None = None) -> None:
        logger.info("user_registered user=%s", user.id)

    async def on_after_login(
        self, user: User, request: Request | None = None, response: Response | None = None
    ) -> None:
        logger.info("auth_login user=%s", user.id)

    async def register(self, email: str, password: str, locale: Locale, name: str | None = None) -> User:
        """Create a user by email. Raises InvalidPasswordException / UserAlreadyExists / ValueError."""
        await self.validate_password(password)
        addr = normalize_email(email)
        display_name = name or derive_name_from_email(addr)
        db = self._user_db()
        if await db.get_by_email(addr) is not None:
            raise UserAlreadyExists()
        user = await db.create(
            {
                "email": addr,
                "name": display_name,
                "hashed_password": self.password_helper.hash(password),
                "locale": locale,
                "is_active": True,
                "is_superuser": False,
                "is_verified": False,
            }
        )
        await self.on_after_register(user)
        return user

    async def set_locale(self, user: User, locale: str) -> User:
        locale_before = user.locale
        updated = await self._user_db().update(user, {"locale": locale})
        logger.info("user_locale_changed locale=%s->%s", locale_before, locale)
        return updated

    async def set_name(self, user: User, name: str | None) -> User:
        name_before = user.name
        updated = await self._user_db().update(user, {"name": name})
        logger.info("user_name_changed name=%s->%s", name_before, name)
        return updated

    async def set_password(self, user: User, new_password: str) -> User:
        await self.validate_password(new_password)
        return await self._user_db().update(
            user, {"hashed_password": self.password_helper.hash(new_password)}
        )

    def _user_db(self) -> UserDatabase:
        assert isinstance(self.user_db, UserDatabase)
        return self.user_db


async def get_user_manager(
    user_db: Annotated[UserDatabase, Depends(get_user_db)],
) -> AsyncGenerator[UserManager]:
    yield UserManager(user_db, password_helper)
