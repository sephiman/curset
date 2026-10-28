# SPDX-License-Identifier: AGPL-3.0-only
"""Who is acting, stamped on every `tradeschool.*` log line (the Python stand-in for an MDC)."""

from __future__ import annotations

import logging
import uuid
from contextvars import ContextVar

from starlette.types import ASGIApp, Receive, Scope, Send

_user_id: ContextVar[str] = ContextVar("log_user_id", default="-")
_course: ContextVar[str] = ContextVar("log_course", default="-")

_FORMAT = "%(asctime)s %(levelname)s %(name)s user=%(user_id)s course=%(course)s %(message)s"


def bind_user(user_id: uuid.UUID) -> None:
    _user_id.set(str(user_id))


def bind_course(slug: str) -> None:
    _course.set(slug)


class RequestContextReset:
    """Clears the bound user and course per request; a task serving several would carry the last ones."""

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "http":
            _user_id.set("-")
            _course.set("-")
        await self.app(scope, receive, send)


class _RequestContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.user_id = _user_id.get()
        record.course = _course.get()
        return True


def configure_logging() -> None:
    """Uvicorn leaves the root at WARNING with no handler, so app info lines need their own; idempotent."""
    logger = logging.getLogger("tradeschool")
    logger.setLevel(logging.INFO)
    if any(isinstance(f, _RequestContextFilter) for h in logger.handlers for f in h.filters):
        return
    handler = logging.StreamHandler()
    handler.addFilter(_RequestContextFilter())
    handler.setFormatter(logging.Formatter(_FORMAT))
    logger.addHandler(handler)
