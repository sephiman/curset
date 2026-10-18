# SPDX-License-Identifier: AGPL-3.0-only
"""Pydantic schema for `course.yaml` (the manifest) plus structural validation.

The canonical structure and order; prose and generator configs live elsewhere, loaded by the registry.
"""

from __future__ import annotations

from collections.abc import Iterator
from enum import StrEnum
from pathlib import Path
from typing import Self

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator

from tradeschool.content.text import Locale, LocalizedText
from tradeschool.exams.presets import ExamPreset
from tradeschool.exercises.types import ExerciseType


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
    #: What the course calls a lesson where results are listed per lesson («tema»); absent: «lección».
    lesson_noun: LocalizedText | None = None

    @model_validator(mode="after")
    def _distinct_languages(self) -> Self:
        if len(set(self.languages)) != len(self.languages):
            raise ValueError(f"course {self.id!r}: duplicate language in {self.languages}")
        return self


class Manifest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    course: ManifestCourse
    blocks: list[ManifestBlock]
    #: The course's exams; none declared means the Exams tab offers nothing.
    exams: list[ExamPreset] = Field(default_factory=list)

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
        self._validate_exams()
        return self

    def _validate_exams(self) -> None:
        """Preset ids are unique and every source names something this course has."""
        ids = [preset.id for preset in self.exams]
        if len(set(ids)) != len(ids):
            raise ValueError(f"duplicate exam preset id in {ids}")
        known = {
            "block": {b.id for b in self.blocks},
            "module": self.module_ids(),
            "lesson": {lesson.id for _, lesson in self.iter_lessons()},
        }
        for preset in self.exams:
            for part in preset.parts:
                sources = [entry.source for entry in part.sources] if part.sources else [part.source]
                for source in sources:
                    assert source is not None
                    named_modules = [(m, "module") for m in source.modules or []]
                    for named, level in [(getattr(source, level), level) for level in known] + named_modules:
                        if named is not None and named not in known[level]:
                            raise ValueError(
                                f"exam {preset.id!r} part {part.id!r}: unknown {level} {named!r}"
                            )
                if part.cases and ExerciseType.CASE not in self.course.exercise_types:
                    raise ValueError(
                        f"exam {preset.id!r} part {part.id!r} draws cases; the course declares no case type"
                    )


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
