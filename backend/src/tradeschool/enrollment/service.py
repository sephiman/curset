# SPDX-License-Identifier: AGPL-3.0-only
"""Active courses, the selected course and per-course reading languages (R5, R6.4, R4.3b)."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.content.collation import alphabetical_key
from tradeschool.content.registry import Catalog, CourseRegistry
from tradeschool.enrollment.models import UserCourse
from tradeschool.enrollment.reading import reading_language
from tradeschool.errors import AppError


def course_text_locale(registry: CourseRegistry, locale: str) -> str:
    """The language a course's own title is shown in: the account's if the course has it."""
    return locale if locale in registry.languages else registry.languages[0]


def alphabetical(catalog: Catalog, locale: str) -> list[CourseRegistry]:
    """Published courses by title in `locale`, which is how both the dropdown and settings list them."""

    def title(registry: CourseRegistry) -> str:
        return registry.manifest.course.title.get(course_text_locale(registry, locale))

    return sorted(catalog.published(), key=lambda registry: alphabetical_key(title(registry)))


@dataclass(frozen=True)
class EnrollmentState:
    active: list[str]
    selected: str | None
    # Effective reading language per published course, after the R4.2 fallbacks.
    reading_languages: dict[str, str]


async def _rows(session: AsyncSession, user_id: uuid.UUID) -> dict[str, UserCourse]:
    rows = await session.scalars(select(UserCourse).where(UserCourse.user_id == user_id))
    return {row.course_id: row for row in rows.all()}


def _fallback_selection(
    ordered_active: list[str], previous: str | None, ordered_all: list[str]
) -> str | None:
    """The course after `previous` alphabetically among the active ones, wrapping (R5.6, R6.4)."""
    if not ordered_active:
        return None
    if previous in ordered_all:
        after = ordered_all[ordered_all.index(previous) + 1 :]
        for slug in after:
            if slug in ordered_active:
                return slug
    return ordered_active[0]


async def load_state(
    session: AsyncSession, catalog: Catalog, user_id: uuid.UUID, account_locale: str
) -> EnrollmentState:
    rows = await _rows(session, user_id)
    ordered = [registry.slug for registry in alphabetical(catalog, account_locale)]
    active = [slug for slug in ordered if slug in rows and rows[slug].active]
    stored = next((slug for slug, row in rows.items() if row.selected), None)
    # A selection that is no longer active (or no longer published) falls back to the first active.
    selected = stored if stored in active else (active[0] if active else None)
    reading = {
        registry.slug: reading_language(
            registry.languages,
            rows[registry.slug].reading_locale if registry.slug in rows else None,
            account_locale,
        )
        for registry in catalog.published()
    }
    return EnrollmentState(active=active, selected=selected, reading_languages=reading)


def _validate(catalog: Catalog, active: list[str], reading_choices: Mapping[str, str]) -> None:
    published = catalog.published_slugs()
    unknown = sorted((set(active) | set(reading_choices)) - published)
    if unknown:
        raise AppError("COURSE_NOT_FOUND", f"No course {unknown[0]!r}.", status_code=404)
    for slug, locale in reading_choices.items():
        languages = catalog.courses[slug].languages
        if locale not in languages:
            raise AppError(
                "LANGUAGE_NOT_AVAILABLE",
                f"Course {slug!r} is available in: {', '.join(languages)}.",
                status_code=400,
                extra={"available": languages},
            )


async def save_state(
    session: AsyncSession,
    catalog: Catalog,
    user_id: uuid.UUID,
    account_locale: str,
    active: list[str],
    selected: str | None,
    reading_choices: Mapping[str, str],
) -> EnrollmentState:
    """Replace the user's active set and choices. A selection outside `active` moves on (R5.6)."""
    _validate(catalog, active, reading_choices)
    rows = await _rows(session, user_id)
    ordered = [registry.slug for registry in alphabetical(catalog, account_locale)]
    ordered_active = [slug for slug in ordered if slug in active]
    effective = (
        selected if selected in ordered_active else _fallback_selection(ordered_active, selected, ordered)
    )

    # Clear the old selection first, so the partial unique index never sees two at flush time.
    for row in rows.values():
        if row.selected and row.course_id != effective:
            row.selected = False
    await session.flush()
    for slug in set(rows) | set(active) | set(reading_choices):
        row = rows.get(slug) or UserCourse(user_id=user_id, course_id=slug, active=False, selected=False)
        session.add(row)
        # Courses outside the catalogue (withdrawn, draft) are left as they are: nothing is deleted.
        if slug in catalog.published_slugs():
            row.active = slug in active
        row.selected = slug == effective
        if slug in reading_choices:
            row.reading_locale = reading_choices[slug]
    await session.commit()
    return await load_state(session, catalog, user_id, account_locale)


async def enroll_at_signup(
    session: AsyncSession, catalog: Catalog, user_id: uuid.UUID, account_locale: str, courses: list[str]
) -> None:
    """The courses ticked on the sign-up screen become active; none is a valid answer (R5.4)."""
    if not courses:
        return
    await save_state(session, catalog, user_id, account_locale, courses, None, {})
