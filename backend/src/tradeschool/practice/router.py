# SPDX-License-Identifier: AGPL-3.0-only
"""`POST /lessons/{id}/practice`: the questions of one practice round, in the order to serve them."""

from __future__ import annotations

import random
from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
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


class ReviewRequest(BaseModel):
    count: int = Field(default=20, ge=1, le=100)


class ReviewResponse(BaseModel):
    questions: list[RoundQuestion]


@router.post("/practice/review", response_model=ReviewResponse)
async def draw_review_round(
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    registry: Annotated[CourseRegistry, Depends(get_registry)],
    rand: Annotated[Rand, Depends(practice_rand)],
    payload: ReviewRequest | None = None,
) -> ReviewResponse:
    drawn = await service.draw_review_round(
        session, registry, user.id, (payload or ReviewRequest()).count, rand
    )
    return ReviewResponse(
        questions=[RoundQuestion(exerciseId=q.exercise_id, questionId=q.variant_id or "") for q in drawn]
    )


class GeneratedRoundRequest(BaseModel):
    #: One psicotécnico type; absent: every type in the course's weights.
    generator: str | None = None
    count: int = Field(default=20, ge=1, le=100)


class GeneratedRoundResponse(BaseModel):
    #: Generated exercise ids, in the order to serve them; each opens as an attempt of its own.
    exerciseIds: list[str]


@router.post("/practice/psicotecnicos", response_model=GeneratedRoundResponse)
async def draw_generated_round(
    registry: Annotated[CourseRegistry, Depends(get_registry)],
    rand: Annotated[Rand, Depends(practice_rand)],
    payload: GeneratedRoundRequest | None = None,
) -> GeneratedRoundResponse:
    request = payload or GeneratedRoundRequest()
    return GeneratedRoundResponse(
        exerciseIds=service.draw_generated_round(registry, request.generator, request.count, rand)
    )
