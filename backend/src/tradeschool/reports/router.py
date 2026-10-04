# SPDX-License-Identifier: AGPL-3.0-only
"""POST a report on an answered multiple-choice question; the learner gets no status back, by design."""

from __future__ import annotations

import uuid
from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends
from pydantic import BaseModel, ConfigDict, StringConstraints
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.auth.backend import current_active_user
from tradeschool.auth.mail import Mailer
from tradeschool.auth.models import User
from tradeschool.config import Settings
from tradeschool.content.registry import CourseRegistry
from tradeschool.db import get_async_session, get_sessionmaker
from tradeschool.deps import ReadingLocale, app_mailer, app_settings, get_registry
from tradeschool.reports import service

router = APIRouter(tags=["reports"])


class ReportRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    message: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True, min_length=service.MESSAGE_MIN, max_length=service.MESSAGE_MAX
        ),
    ]


@router.post("/attempts/{attempt_id}/report", status_code=202)
async def report_question(
    attempt_id: uuid.UUID,
    payload: ReportRequest,
    background: BackgroundTasks,
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[AsyncSession, Depends(get_async_session)],
    registry: Annotated[CourseRegistry, Depends(get_registry)],
    settings: Annotated[Settings, Depends(app_settings)],
    mailer: Annotated[Mailer, Depends(app_mailer)],
    locale: ReadingLocale,
) -> dict[str, str]:
    await service.file_report(
        session, registry, user, attempt_id, payload.message, locale, settings.app_public_url
    )
    # Stored already; mailing it (and any earlier one still pending) happens after the response.
    background.add_task(service.deliver_pending, get_sessionmaker(), mailer, settings.report_email_to)
    return {"status": "received"}
