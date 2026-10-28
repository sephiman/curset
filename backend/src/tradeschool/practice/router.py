# SPDX-License-Identifier: AGPL-3.0-only
"""`POST /lessons/{id}/practice`: the questions of one practice round, in the order to serve them."""

from __future__ import annotations

import random
from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.auth.backend import current_active_user
from tradeschool.auth.models import User
from tradeschool.content.registry import CourseRegistry
from tradeschool.db import get_async_session
from tradeschool.deps import get_registry
from tradeschool.practice import service
from tradeschool.practice.order import Rand

router = APIRouter(tags=["practice"])


def practice_rand() -> Rand:
    """Overridden in tests to make a round reproducible."""
    return random.SystemRandom()


class RoundRequest(BaseModel):
    #: «Todas»: every question of the lesson; otherwise «20 al azar».
    all: bool = False


class RoundQuestion(BaseModel):
    exerciseId: str
    questionId: str


class RoundResponse(BaseModel):
    lessonId: str
    questions: list[RoundQuestion]


@router.post("/lessons/{lesson_id}/practice", response_model=RoundResponse)
async def draw_round(
    lesson_id: str,
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    registry: Annotated[CourseRegistry, Depends(get_registry)],
    rand: Annotated[Rand, Depends(practice_rand)],
    payload: RoundRequest | None = None,
) -> RoundResponse:
    drawn = await service.draw_round(
        session, registry, user.id, lesson_id, bool(payload and payload.all), rand
    )
    return RoundResponse(
        lessonId=lesson_id,
        questions=[RoundQuestion(exerciseId=q.exercise_id, questionId=q.variant_id or "") for q in drawn],
    )
