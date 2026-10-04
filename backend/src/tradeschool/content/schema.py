# SPDX-License-Identifier: AGPL-3.0-only
"""Pydantic schema for `course.yaml` (the manifest) plus structural validation.

The canonical structure and order; prose and generator configs live elsewhere, loaded by the registry.
"""

from __future__ import annotations

from collections.abc import Iterator
from enum import StrEnum
from pathlib import Path
from typing import Literal, Self

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator

from tradeschool.exercises.types import ExerciseType

#: Every language the platform can serve; a course declares the subset it is written in.
LOCALES = ("en", "es")
Locale = Literal["en", "es"]


class LocalizedText(BaseModel):
    """Text in the languages its course declares; which ones must be present is checked per course."""

    model_config = ConfigDict(extra="forbid")
    en: str | None = None
    es: str | None = None

    @model_validator(mode="after")
    def _not_empty(self) -> Self:
        if self.en is None and self.es is None:
            raise ValueError("localized text needs at least one language")
        return self

    def get(self, locale: str) -> str:
        value = self.es if locale == "es" else self.en
        if value is None:
            raise LookupError(f"no {locale!r} text in {self!r}")
        return value

    def languages(self) -> set[str]:
        return {locale for locale in LOCALES if getattr(self, locale) is not None}


class KeyedEntity(BaseModel):
    """An entity with a display id and a permanent `key` (defaults to the id at creation).

    The key is chosen once and NEVER renamed: seeds, stored progress and glossary origins hang off
    it, so display ids can be reorganized without a data migration. See content/README.md.
    """

    id: str
    key: str = ""

    @model_validator(mode="after")
    def _default_key(self) -> Self:
        if not self.key:
            self.key = self.id
        return self


class ManifestExercise(KeyedEntity):
    model_config = ConfigDict(extra="forbid")
    type: ExerciseType


class ManifestLesson(KeyedEntity):
    model_config = ConfigDict(extra="forbid")
    title: LocalizedText
    #: Two or three sentences of what this lesson teaches, in the lesson's own words. Required, and
    #: bound by the same never-coins rule as the glossary: a summary may not use a term its own
    #: lesson's prose never uses (`registry._check_summaries_never_coin`).
    summary: LocalizedText
    exercises: list[ManifestExercise] = Field(default_factory=list)


class ManifestModule(KeyedEntity):
    model_config = ConfigDict(extra="forbid")
    title: LocalizedText
    summary: LocalizedText
    assumes: list[str] = Field(default_factory=list)
    lessons: list[ManifestLesson] = Field(default_factory=list)


class ManifestBlock(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    title: LocalizedText
    modules: list[ManifestModule] = Field(default_factory=list)


class CourseStatus(StrEnum):
    #: Loaded and verified by the pipeline, never offered to users.
    DRAFT = "draft"
    PUBLISHED = "published"


class ManifestCourse(BaseModel):
    """The root course entity; its blocks live at the manifest's top level."""

    model_config = ConfigDict(extra="forbid")
    #: The course's permanent slug, equal to its directory under `content/`.
    id: str
    title: LocalizedText
    #: The book's short name, for surfaces the full title is too long for (the PDF's running footer).
    subtitle: LocalizedText
    description: LocalizedText
    #: The languages the course is written in, in preference order: the first is the fallback reading
    #: language for an account whose language the course lacks.
    languages: list[Locale] = Field(min_length=1)
    status: CourseStatus
    #: The exercise kinds this course uses; an exercise of any other kind is a manifest error.
    exercise_types: list[ExerciseType] = Field(min_length=1)

    @model_validator(mode="after")
    def _distinct_languages(self) -> Self:
        if len(set(self.languages)) != len(self.languages):
            raise ValueError(f"course {self.id!r}: duplicate language in {self.languages}")
        return self


class Manifest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    course: ManifestCourse
    blocks: list[ManifestBlock]

    # --- Derived views ---
    def iter_modules(self) -> list[tuple[ManifestBlock, ManifestModule]]:
        return [(b, m) for b in self.blocks for m in b.modules]

    def iter_lessons(self) -> list[tuple[ManifestModule, ManifestLesson]]:
        return [(m, lesson) for _, m in self.iter_modules() for lesson in m.lessons]

    def iter_exercises(self) -> list[tuple[ManifestModule, ManifestLesson, ManifestExercise]]:
        return [(m, lesson, ex) for m, lesson in self.iter_lessons() for ex in lesson.exercises]

    def module_ids(self) -> set[str]:
        return {m.id for _, m in self.iter_modules()}

    @model_validator(mode="after")
    def _validate_structure(self) -> Self:
        seen: set[str] = set()
        # IDs are unique across every level of ONE course; another course may reuse any of them.
        for level in (
            [self.course.id],
            [b.id for b in self.blocks],
            [m.id for _, m in self.iter_modules()],
            [lesson.id for _, lesson in self.iter_lessons()],
            [ex.id for _, _, ex in self.iter_exercises()],
        ):
            for identifier in level:
                if identifier in seen:
                    raise ValueError(f"duplicate stable id: {identifier!r}")
                seen.add(identifier)

        # Keys form their own global namespace (course and block ids double as their keys). Ids and
        # keys may overlap in VALUE across entities — the 2026-08-10 renumbering reused the id range —
        # so the two sets are checked apart, never merged.
        seen_keys: set[str] = set()
        for level in (
            [self.course.id],
            [b.id for b in self.blocks],
            [m.key for _, m in self.iter_modules()],
            [lesson.key for _, lesson in self.iter_lessons()],
            [ex.key for _, _, ex in self.iter_exercises()],
        ):
            for key in level:
                if key in seen_keys:
                    raise ValueError(f"duplicate stable key: {key!r}")
                seen_keys.add(key)

        declared = set(self.course.exercise_types)
        for _, _, exercise in self.iter_exercises():
            if exercise.type not in declared:
                raise ValueError(
                    f"exercise {exercise.id!r} is a {exercise.type.value}, which course "
                    f"{self.course.id!r} does not declare in exercise_types"
                )

        module_ids = self.module_ids()
        for _, module in self.iter_modules():
            for dep in module.assumes:
                if dep not in module_ids:
                    raise ValueError(f"module {module.id!r} assumes unknown module {dep!r}")
                if dep == module.id:
                    raise ValueError(f"module {module.id!r} cannot assume itself")
        return self


def missing_languages(node: object, languages: set[str], path: str = "") -> Iterator[str]:
    """Where a localized text lacks one of `languages` or carries one the course does not declare."""
    if isinstance(node, LocalizedText):
        if node.languages() != languages:
            yield f"{path or '<root>'} has {sorted(node.languages())}"
        return
    if isinstance(node, BaseModel):
        for name in type(node).model_fields:
            yield from missing_languages(getattr(node, name), languages, f"{path}.{name}" if path else name)
    elif isinstance(node, list | tuple):
        for index, item in enumerate(node):
            yield from missing_languages(item, languages, f"{path}[{index}]")
    elif isinstance(node, dict):
        for key, item in node.items():
            yield from missing_languages(item, languages, f"{path}.{key}")


def parse_manifest(path: Path) -> Manifest:
    with path.open(encoding="utf-8") as fh:
        raw = yaml.safe_load(fh)
    return Manifest.model_validate(raw)
