# SPDX-License-Identifier: AGPL-3.0-only
"""FastAPI application factory and startup lifespan."""

from __future__ import annotations

import asyncio
import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import APIRouter, Depends, FastAPI
from slowapi.errors import RateLimitExceeded
from starlette.requests import Request
from starlette.responses import JSONResponse

from tradeschool import health
from tradeschool.attempts.router import router as attempts_router
from tradeschool.auth.mail import build_mailer
from tradeschool.auth.router import router as auth_router
from tradeschool.config import Settings, get_settings
from tradeschool.content.router import course_router
from tradeschool.content.router import router as content_router
from tradeschool.db import dispose_engine, init_engine
from tradeschool.deps import get_registry
from tradeschool.enrollment.router import catalogue_router, me_router
from tradeschool.errors import register_exception_handlers
from tradeschool.exams.router import router as exams_router
from tradeschool.ratelimit import limiter
from tradeschool.reports.router import router as reports_router
from tradeschool.stats.router import router as stats_router

logger = logging.getLogger("tradeschool")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    settings: Settings = app.state.settings
    init_engine(settings.database_url)

    if settings.run_migrations_on_startup:
        from tradeschool.migrations import run_migrations

        logger.info("Running database migrations…")
        # Alembic's async env calls asyncio.run internally, which cannot run inside this
        # already-running loop; execute it in a worker thread.
        await asyncio.to_thread(run_migrations, settings.database_url)

    # Load every course (validates each manifest + its content) and expose the catalogue for serving.
    from tradeschool.content.registry import load_catalog

    app.state.catalog = load_catalog(settings.content_dir)

    if settings.sync_content_on_startup:
        from tradeschool.content.sync import reconcile_catalog
        from tradeschool.db import get_sessionmaker

        async with get_sessionmaker()() as session:
            await reconcile_catalog(app.state.catalog, session)

    retry = asyncio.create_task(_retry_report_mail(app))
    yield
    retry.cancel()

    await dispose_engine()


REPORT_MAIL_RETRY_SECONDS = 15 * 60


async def _retry_report_mail(app: FastAPI) -> None:
    """Question reports the mail server did not accept are retried until it does (R8a.4)."""
    from tradeschool.db import get_sessionmaker
    from tradeschool.reports.service import deliver_pending

    settings: Settings = app.state.settings
    while True:
        try:
            await deliver_pending(get_sessionmaker(), app.state.mailer, settings.report_email_to)
        except Exception:
            logger.exception("retrying question-report mail failed")
        await asyncio.sleep(REPORT_MAIL_RETRY_SECONDS)


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or get_settings()

    app = FastAPI(
        title="Curset",
        version="0.1.0",
        lifespan=lifespan,
        docs_url="/api/docs" if settings.dev_mode else None,
        openapi_url="/api/openapi.json" if settings.dev_mode else None,
    )
    app.state.settings = settings
    app.state.mailer = build_mailer(settings)

    # Rate limiting (slowapi). The limiter is a shared singleton; toggle it per app.
    limiter.enabled = settings.rate_limit_enabled
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_handler)

    register_exception_handlers(app)

    api = APIRouter(prefix="/api")
    # Genuinely global: an account is not per-course, and health/version describe the service.
    api.include_router(health.router)
    api.include_router(auth_router, prefix="/auth")

    api.include_router(catalogue_router, prefix="/courses")
    api.include_router(me_router, prefix="/me/courses")

    # Everything whose data belongs to a course hangs off /api/courses/{course}/….
    scoped = APIRouter(prefix="/courses/{course}", dependencies=[Depends(get_registry)])
    for router in (content_router, attempts_router, stats_router, exams_router, reports_router):
        scoped.include_router(router)
    if settings.dev_mode:
        from tradeschool.dev.router import router as dev_router

        # Dev-gated tooling, not a public surface.
        scoped.include_router(dev_router, prefix="/dev")
    api.include_router(scoped)
    # Included with the prefix rather than nested: the course tree's own path is "", and FastAPI
    # rejects an empty path under an empty include-prefix.
    api.include_router(course_router, prefix="/courses/{course}", dependencies=[Depends(get_registry)])
    app.include_router(api)

    return app


async def _rate_limit_handler(_: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, RateLimitExceeded)
    return JSONResponse(
        status_code=429,
        content={"code": "RATE_LIMITED", "message": "Too many requests. Please slow down."},
    )


app = create_app()
