# SPDX-License-Identifier: AGPL-3.0-only
"""Attempt endpoints (the core exercise flow, §3.1)."""

from __future__ import annotations

import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.attempts import service
from tradeschool.attempts.schemas import (
    AnswerRequest,
    AttemptInstance,
    AttemptReviewResponse,
    AttemptSummary,
    GradeResponse,
)
from tradeschool.auth.backend import current_active_user
from tradeschool.auth.models import User
from tradeschool.content.registry import CourseRegistry
from tradeschool.db import get_async_session
from tradeschool.deps import ReadingLocale, get_registry

router = APIRouter(tags=["attempts"])


@router.post("/exercises/{exercise_id}/attempts", response_model=AttemptInstance, status_code=201)
async def create_attempt(
    exercise_id: str,
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    registry: Annotated[CourseRegistry, Depends(get_registry)],
    locale: ReadingLocale,
) -> AttemptInstance:
    opened = await service.open_attempt(session, registry, user.id, exercise_id, locale)
    return AttemptInstance.from_opened(opened)


@router.post("/attempts/{attempt_id}/answer", response_model=GradeResponse)
async def answer_attempt(
    attempt_id: uuid.UUID,
    payload: AnswerRequest,
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    registry: Annotated[CourseRegistry, Depends(get_registry)],
    locale: ReadingLocale,
) -> GradeResponse:
    attempt, result = await service.submit_answer(
        session, registry, user.id, attempt_id, payload.answer, locale
    )
    return GradeResponse.build(attempt, result)


@router.get("/attempts/{attempt_id}", response_model=AttemptReviewResponse)
async def review_attempt(
    attempt_id: uuid.UUID,
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    registry: Annotated[CourseRegistry, Depends(get_registry)],
    locale: ReadingLocale,
) -> AttemptReviewResponse:
    review = await service.review_attempt(session, registry, user.id, attempt_id, locale)
    return AttemptReviewResponse.build(review)


@router.get("/attempts", response_model=list[AttemptSummary])
async def list_attempts(
    exercise_id: Annotated[str, Query()],
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    registry: Annotated[CourseRegistry, Depends(get_registry)],
) -> list[AttemptSummary]:
    attempts = await service.user_attempts(session, registry, user.id, exercise_id)
    return [AttemptSummary.build(a, exercise_id) for a in attempts]
