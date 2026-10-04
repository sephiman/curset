# SPDX-License-Identifier: AGPL-3.0-only
"""Statistics endpoints: per-user (`/stats/me`) and anonymous aggregate (`/stats/global`)."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.auth.backend import current_active_user
from tradeschool.auth.models import User
from tradeschool.content.registry import CourseRegistry
from tradeschool.db import get_async_session
from tradeschool.deps import ReadingLocale, get_registry
from tradeschool.stats import service

router = APIRouter(tags=["stats"])


@router.get("/stats/me")
async def stats_me(
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    registry: Annotated[CourseRegistry, Depends(get_registry)],
    locale: ReadingLocale,
) -> dict[str, object]:
    return await service.me_stats(session, registry, user.id, locale)


@router.get("/stats/global")
async def stats_global(
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    registry: Annotated[CourseRegistry, Depends(get_registry)],
    locale: ReadingLocale,
) -> dict[str, object]:
    # Aggregated and anonymous: no user identifiers cross this boundary (§5.3).
    return await service.global_stats(session, registry, locale)
