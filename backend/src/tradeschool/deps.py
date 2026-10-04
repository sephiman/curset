# SPDX-License-Identifier: AGPL-3.0-only
"""Shared FastAPI dependencies."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, Query, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.auth.backend import current_active_user
from tradeschool.auth.mail import Mailer
from tradeschool.auth.models import User
from tradeschool.config import Settings
from tradeschool.content.registry import Catalog, CourseRegistry
from tradeschool.db import get_async_session
from tradeschool.enrollment.models import UserCourse
from tradeschool.enrollment.reading import reading_language
from tradeschool.errors import AppError


def app_settings(request: Request) -> Settings:
    """The Settings bound to the running app (tests inject their own)."""
    settings: Settings = request.app.state.settings
    return settings


def app_mailer(request: Request) -> Mailer:
    """The Mailer bound to the running app (tests swap in a recording one)."""
    mailer: Mailer = request.app.state.mailer
    return mailer


def app_catalog(request: Request) -> Catalog:
    catalog: Catalog = request.app.state.catalog
    return catalog


def get_registry(request: Request) -> CourseRegistry:
    """The published course named by `/api/courses/{course}/…`; a draft is as absent as an unknown slug.

    Read off `request.path_params` so the routers it serves need not declare the segment themselves.
    """
    slug = str(request.path_params.get("course", ""))
    registry = app_catalog(request).get(slug)
    if registry is None or not registry.published:
        raise AppError("COURSE_NOT_FOUND", f"No course {slug!r}.", status_code=404)
    return registry


def current_course(registry: Annotated[CourseRegistry, Depends(get_registry)]) -> str:
    return registry.slug


CourseId = Annotated[str, Depends(current_course)]


async def reading_locale(
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    registry: Annotated[CourseRegistry, Depends(get_registry)],
    lang: Annotated[str | None, Query(pattern="^(en|es)$")] = None,
) -> str:
    """The language this course is read in: `?lang` if the course has it, else the user's choice."""
    if lang is not None:
        if lang not in registry.languages:
            raise language_not_available(registry, lang)
        return lang
    chosen = await session.scalar(
        select(UserCourse.reading_locale).where(
            UserCourse.user_id == user.id, UserCourse.course_id == registry.slug
        )
    )
    return reading_language(registry.languages, chosen, user.locale)


def language_not_available(registry: CourseRegistry, lang: str) -> AppError:
    available = ", ".join(registry.languages)
    return AppError(
        "LANGUAGE_NOT_AVAILABLE",
        f"Course {registry.slug!r} is not available in {lang!r}; it is available in: {available}.",
        status_code=404,
        extra={"available": registry.languages},
    )


ReadingLocale = Annotated[str, Depends(reading_locale)]
