# SPDX-License-Identifier: AGPL-3.0-only
"""The course catalogue (public, for sign-up) and the signed-in user's course choices."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.auth.backend import current_active_user
from tradeschool.auth.models import User
from tradeschool.content.registry import Catalog
from tradeschool.db import get_async_session
from tradeschool.deps import app_catalog
from tradeschool.enrollment import service
from tradeschool.enrollment.schemas import CatalogueCourse, MyCourses, MyCoursesUpdate

catalogue_router = APIRouter(tags=["courses"])
me_router = APIRouter(tags=["courses"])


@catalogue_router.get("", response_model=list[CatalogueCourse])
async def catalogue(
    catalog: Annotated[Catalog, Depends(app_catalog)],
    lang: Annotated[str, Query(pattern="^(en|es)$")] = "en",
) -> list[CatalogueCourse]:
    """Published courses, alphabetical by title in `lang` — the interface language."""
    return [CatalogueCourse.build(registry, lang) for registry in service.alphabetical(catalog, lang)]


@me_router.get("", response_model=MyCourses)
async def my_courses(
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    catalog: Annotated[Catalog, Depends(app_catalog)],
) -> MyCourses:
    return MyCourses.build(await service.load_state(session, catalog, user.id, user.locale))


@me_router.put("", response_model=MyCourses)
async def update_my_courses(
    payload: MyCoursesUpdate,
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    catalog: Annotated[Catalog, Depends(app_catalog)],
) -> MyCourses:
    state = await service.save_state(
        session, catalog, user.id, user.locale, payload.active, payload.selected, payload.readingLanguages
    )
    return MyCourses.build(state)
