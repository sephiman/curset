# SPDX-License-Identifier: AGPL-3.0-only
"""Auth endpoints: thin wrappers over fastapi-users plus the mailed links (email verification, reset)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Annotated, cast

from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_users.exceptions import InvalidPasswordException, UserAlreadyExists
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse, Response

from tradeschool.auth import email_verification, password_reset
from tradeschool.auth.backend import (
    SessionStrategy,
    clear_session_cookie,
    current_active_user,
    get_database_strategy,
    set_session_cookie,
)
from tradeschool.auth.mail import Mailer
from tradeschool.auth.manager import UserManager, get_user_manager
from tradeschool.auth.models import User
from tradeschool.auth.schemas import (
    EmailTokenBody,
    Features,
    LoginRequest,
    PasswordResetConfirm,
    PasswordResetRequest,
    UserCreate,
    UserRead,
    UserUpdate,
)
from tradeschool.config import Settings, get_settings
from tradeschool.db import get_async_session
from tradeschool.deps import app_mailer, app_settings
from tradeschool.errors import AppError
from tradeschool.ratelimit import limiter

router = APIRouter(tags=["auth"])


@dataclass
class _Credentials:
    username: str
    password: str


def _register_limit() -> str:
    return get_settings().register_rate_limit


def _login_limit() -> str:
    return get_settings().login_rate_limit


def _mail_limit() -> str:
    return get_settings().mail_rate_limit


def _invalid_password(exc: InvalidPasswordException) -> AppError:
    return AppError("INVALID_PASSWORD", str(exc.reason), status_code=400)


def _require_mail(mailer: Mailer) -> None:
    if not mailer.enabled:
        raise AppError("NOT_FOUND", "Email is not configured on this server.", status_code=404)


@router.post("/register", response_model=UserRead, status_code=201)
@limiter.limit(_register_limit)
async def register(
    request: Request,
    payload: UserCreate,
    user_manager: Annotated[UserManager, Depends(get_user_manager)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    mailer: Annotated[Mailer, Depends(app_mailer)],
    settings: Annotated[Settings, Depends(app_settings)],
) -> UserRead:
    if payload.email is not None:
        await email_verification.ensure_available(session, payload.email)
    try:
        user = await user_manager.register(payload.username, payload.password, payload.locale)
    except UserAlreadyExists as exc:
        raise AppError("USER_ALREADY_EXISTS", "That username is already taken.", status_code=400) from exc
    except InvalidPasswordException as exc:
        raise _invalid_password(exc) from exc
    if payload.email is not None:
        user = await email_verification.change_email(
            session, user, payload.email, mailer=mailer, public_url=settings.app_public_url
        )
    return UserRead.model_validate(user)


@router.post("/login")
@limiter.limit(_login_limit)
async def login(
    request: Request,
    payload: LoginRequest,
    user_manager: Annotated[UserManager, Depends(get_user_manager)],
    strategy: Annotated[SessionStrategy, Depends(get_database_strategy)],
    settings: Annotated[Settings, Depends(app_settings)],
) -> Response:
    creds = _Credentials(username=payload.username.strip(), password=payload.password)
    user = await user_manager.authenticate(cast(OAuth2PasswordRequestForm, creds))
    if user is None or not user.is_active:
        raise AppError("LOGIN_BAD_CREDENTIALS", "Invalid username or password.", status_code=400)

    token = await strategy.write_token(user)
    response = JSONResponse(UserRead.model_validate(user).model_dump(mode="json"))
    set_session_cookie(response, token, settings)
    await user_manager.on_after_login(user, request, response)
    return response


@router.post("/logout", status_code=204)
async def logout(
    request: Request,
    user: Annotated[User, Depends(current_active_user)],
    strategy: Annotated[SessionStrategy, Depends(get_database_strategy)],
    settings: Annotated[Settings, Depends(app_settings)],
) -> Response:
    token = request.cookies.get(settings.session_cookie_name)
    if token:
        await strategy.destroy_token(token, user)
    response = Response(status_code=204)
    clear_session_cookie(response, settings)
    return response


@router.get("/me", response_model=UserRead)
async def me(user: Annotated[User, Depends(current_active_user)]) -> User:
    return user


@router.patch("/me", response_model=UserRead)
async def update_me(
    payload: UserUpdate,
    user: Annotated[User, Depends(current_active_user)],
    user_manager: Annotated[UserManager, Depends(get_user_manager)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    mailer: Annotated[Mailer, Depends(app_mailer)],
    settings: Annotated[Settings, Depends(app_settings)],
) -> User:
    if payload.locale is not None:
        user = await user_manager.set_locale(user, payload.locale)
    if "email" in payload.model_fields_set:
        user = await email_verification.change_email(
            session, user, payload.email, mailer=mailer, public_url=settings.app_public_url
        )
    return user


@router.get("/features", response_model=Features)
async def features(mailer: Annotated[Mailer, Depends(app_mailer)]) -> Features:
    return Features(mail=mailer.enabled)


@router.post("/email/verification", status_code=202)
@limiter.limit(_mail_limit)
async def resend_verification(
    request: Request,
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    mailer: Annotated[Mailer, Depends(app_mailer)],
    settings: Annotated[Settings, Depends(app_settings)],
) -> dict[str, str]:
    _require_mail(mailer)
    if user.email is None:
        raise AppError("EMAIL_MISSING", "Add an email address first.", status_code=400)
    await email_verification.send_link(session, user, mailer=mailer, public_url=settings.app_public_url)
    return {"status": "accepted"}


@router.post("/email/verification/confirm")
async def confirm_verification(
    payload: EmailTokenBody,
    session: Annotated[AsyncSession, Depends(get_async_session)],
) -> dict[str, str]:
    await email_verification.confirm(session, payload.token)
    return {"status": "ok"}


@router.post("/password-reset", status_code=202)
@limiter.limit(_mail_limit)
async def request_password_reset(
    request: Request,
    payload: PasswordResetRequest,
    session: Annotated[AsyncSession, Depends(get_async_session)],
    mailer: Annotated[Mailer, Depends(app_mailer)],
    settings: Annotated[Settings, Depends(app_settings)],
) -> dict[str, str]:
    _require_mail(mailer)
    await password_reset.request_for_email(
        session, payload.email, mailer=mailer, public_url=settings.app_public_url
    )
    return {"status": "accepted"}


@router.post("/password-reset/validate")
async def validate_password_reset(
    payload: EmailTokenBody,
    session: Annotated[AsyncSession, Depends(get_async_session)],
) -> dict[str, str]:
    await password_reset.validate(session, payload.token)
    return {"status": "valid"}


@router.post("/password-reset/confirm")
async def confirm_password_reset(
    payload: PasswordResetConfirm,
    session: Annotated[AsyncSession, Depends(get_async_session)],
    user_manager: Annotated[UserManager, Depends(get_user_manager)],
) -> dict[str, str]:
    try:
        await password_reset.confirm(session, payload.token, payload.new_password, user_manager=user_manager)
    except InvalidPasswordException as exc:
        raise _invalid_password(exc) from exc
    return {"status": "ok"}
