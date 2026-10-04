# SPDX-License-Identifier: AGPL-3.0-only
"""Catalogue and per-user course-choice payloads."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from tradeschool.content.registry import CourseRegistry
from tradeschool.content.schema import Locale
from tradeschool.enrollment.service import EnrollmentState, course_text_locale


class CatalogueCourse(BaseModel):
    slug: str
    title: str
    subtitle: str
    description: str
    #: The language `title`, `subtitle` and `description` are in: the account's when the course has it.
    textLocale: str
    languages: list[str]

    @classmethod
    def build(cls, registry: CourseRegistry, locale: str) -> CatalogueCourse:
        course = registry.manifest.course
        text_locale = course_text_locale(registry, locale)
        return cls(
            slug=registry.slug,
            title=course.title.get(text_locale),
            subtitle=course.subtitle.get(text_locale),
            description=course.description.get(text_locale),
            textLocale=text_locale,
            languages=registry.languages,
        )


class MyCourses(BaseModel):
    active: list[str]
    selected: str | None
    readingLanguages: dict[str, str]

    @classmethod
    def build(cls, state: EnrollmentState) -> MyCourses:
        return cls(active=state.active, selected=state.selected, readingLanguages=state.reading_languages)


class MyCoursesUpdate(BaseModel):
    """The whole choice set; `readingLanguages` holds only the courses whose language the user picked."""

    model_config = ConfigDict(extra="forbid")
    active: list[str]
    selected: str | None = None
    readingLanguages: dict[str, Locale] = Field(default_factory=dict)
