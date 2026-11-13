# SPDX-License-Identifier: AGPL-3.0-only
"""The solution panel of a course built on technical sources: the question's `extract` when the cited
source's licence allows quoting it, else «no extract» with the licence and the source's link."""

from __future__ import annotations

from pydantic import BaseModel

from tradeschool.citations.excerpt_store import MissingExcerpt, SolutionExcerpt, SolutionText
from tradeschool.citations.tech import TechSource, TechSourceIndex, parse_ref
from tradeschool.exercises.quiz import QuizConfig, QuizVariant
from tradeschool.exercises.types import ExerciseType

LICENCE = "licence"
NO_EXTRACT = "no-extract"


def first_source(index: TechSourceIndex, citation: str | None) -> tuple[TechSource, str] | None:
    """The source (and anchor) of a question's first citation; None when absent or not registered."""
    ref = parse_ref(citation.split(";")[0]) if citation else None
    source = index.sources.get(ref.source_id) if ref else None
    return (source, ref.anchor) if source and ref else None


def tech_solution(index: TechSourceIndex, variant: QuizVariant, locale: str) -> SolutionText | None:
    cited = first_source(index, variant.citation)
    if cited is None:
        return None
    source, anchor = cited
    if not source.extract_allowed:
        return MissingExcerpt(LICENCE, source.url, source.licence)
    text = variant.extract.get(locale) if variant.extract else None
    if not text:
        return MissingExcerpt(NO_EXTRACT, source.url)
    return SolutionExcerpt(
        heading=f"{source.title} ({anchor})",
        text=text,
        full=None,
        full_too_long=False,
        href=source.url,
        attribution=f"Licence: {source.licence}",
    )


def question_problems(
    index: TechSourceIndex, exercise_configs: dict[str, tuple[ExerciseType, BaseModel]]
) -> list[str]:
    """Extracts the licence forbids, and snippets that are not files of the course."""
    problems: list[str] = []
    for exercise_id, (_, config) in exercise_configs.items():
        if not isinstance(config, QuizConfig):
            continue
        for variant in config.variants:
            label = f"question {exercise_id}/{variant.id}"
            if variant.extract:
                cited = first_source(index, variant.citation)
                if cited is None:
                    problems.append(f"{label} has an extract but its citation names no registered source")
                elif not cited[0].extract_allowed:
                    problems.append(
                        f"{label} quotes {cited[0].id}, whose licence ({cited[0].licence}) allows no extract"
                    )
            if variant.snippet and not (index.course_dir / "snippets" / variant.snippet).is_file():
                problems.append(f"{label} names snippet {variant.snippet}, which is not in snippets/")
    return problems
