# SPDX-License-Identifier: AGPL-3.0-only
"""Reconcile the manifest into the DB skeleton by permanent KEY (§4.2).

Rows absent from the manifest are marked inactive, never hard-deleted, so historical progress
survives. The DB stores keys, never display ids — keys are chosen once and never renamed, so a
display renumbering leaves every row (and every learner's progress) untouched. Order is a plain
attribute. Course and block ids double as their keys. Keys are unique per course, so each course is
reconciled against its own rows only.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.config import Settings
from tradeschool.content.models import (
    Block,
    Course,
    CourseOwnedModel,
    Exercise,
    Lesson,
    Module,
    SkeletonModel,
)
from tradeschool.content.registry import Catalog, load_catalog
from tradeschool.content.schema import Manifest

logger = logging.getLogger("tradeschool.content")


@dataclass
class SyncSummary:
    inserted: int = 0
    updated: int = 0
    deactivated: int = 0

    def __str__(self) -> str:
        return (
            f"Course sync: {self.inserted} inserted, {self.updated} updated, {self.deactivated} deactivated."
        )


async def reconcile(manifest: Manifest, session: AsyncSession, order_index: int = 1) -> SyncSummary:
    """One course's skeleton; another course's rows are never read, let alone deactivated."""
    summary = SyncSummary()
    course_id = manifest.course.id

    async def upsert(
        model: type[SkeletonModel],
        rows: dict[str, dict[str, object]],
    ) -> None:
        scope = model.course_id == course_id if issubclass(model, CourseOwnedModel) else model.id == course_id
        existing = {row.id: row for row in (await session.scalars(select(model).where(scope))).all()}
        for identifier, attrs in rows.items():
            current = existing.get(identifier)
            if current is None:
                session.add(model(id=identifier, active=True, **attrs))
                summary.inserted += 1
            else:
                changed = not current.active
                for key, value in attrs.items():
                    if getattr(current, key) != value:
                        setattr(current, key, value)
                        changed = True
                if not current.active:
                    current.active = True
                if changed:
                    summary.updated += 1
        for identifier, current in existing.items():
            if identifier not in rows and current.active:
                current.active = False
                summary.deactivated += 1

    courses: dict[str, dict[str, object]] = {}
    blocks: dict[str, dict[str, object]] = {}
    modules: dict[str, dict[str, object]] = {}
    lessons: dict[str, dict[str, object]] = {}
    exercises: dict[str, dict[str, object]] = {}

    # `assumes` names modules by display id in the manifest (it is hand-written); the DB stores keys.
    module_key = {m.id: m.key for _, m in manifest.iter_modules()}
    courses[course_id] = {"order_index": order_index}
    for b_index, block in enumerate(manifest.blocks, start=1):
        blocks[block.id] = {"course_id": course_id, "order_index": b_index}
        for m_index, module in enumerate(block.modules, start=1):
            modules[module.key] = {
                "course_id": course_id,
                "block_id": block.id,
                "order_index": m_index,
                "assumes": [module_key[dep] for dep in module.assumes],
            }
            for l_index, lesson in enumerate(module.lessons, start=1):
                lessons[lesson.key] = {
                    "course_id": course_id,
                    "module_id": module.key,
                    "order_index": l_index,
                }
                for e_index, exercise in enumerate(lesson.exercises, start=1):
                    exercises[exercise.key] = {
                        "course_id": course_id,
                        "module_id": module.key,
                        "lesson_id": lesson.key,
                        "type": exercise.type,
                        "order_index": e_index,
                    }

    # Parents before children so foreign keys resolve on insert.
    await upsert(Course, courses)
    await session.flush()
    await upsert(Block, blocks)
    await upsert(Module, modules)
    await session.flush()
    await upsert(Lesson, lessons)
    await session.flush()
    await upsert(Exercise, exercises)
    await session.commit()

    logger.info("%s", summary)
    return summary


async def reconcile_catalog(catalog: Catalog, session: AsyncSession) -> SyncSummary:
    """Every course in the catalogue, drafts included; a course no longer under `content/` goes inactive."""
    total = SyncSummary()
    for index, slug in enumerate(sorted(catalog.courses), start=1):
        summary = await reconcile(catalog.courses[slug].manifest, session, order_index=index)
        total.inserted += summary.inserted
        total.updated += summary.updated
        total.deactivated += summary.deactivated
    for withdrawn in (await session.scalars(select(Course).where(Course.id.not_in(catalog.courses)))).all():
        if withdrawn.active:
            withdrawn.active = False
            total.deactivated += 1
    await session.commit()
    return total


async def sync_content(settings: Settings, session: AsyncSession) -> tuple[Catalog, SyncSummary]:
    """Load + validate every course and reconcile them. Returns the catalogue for serving."""
    catalog = load_catalog(settings.content_dir)
    summary = await reconcile_catalog(catalog, session)
    return catalog, summary


async def sync_content_cli(settings: Settings) -> str:
    from tradeschool.db import dispose_engine, get_sessionmaker, init_engine

    init_engine(settings.database_url)
    try:
        async with get_sessionmaker()() as session:
            _, summary = await sync_content(settings, session)
        return str(summary)
    finally:
        await dispose_engine()
