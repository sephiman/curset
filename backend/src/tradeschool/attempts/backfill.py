# SPDX-License-Identifier: AGPL-3.0-only
"""Name the quiz question of every attempt written before attempts stored it (revision f8a9b0c1d2e3).

The stored instance is what the learner saw, so it decides, in this order: the question that lays out
exactly that instance from the attempt's seed (anywhere in the course, so a question a rebuild moved is
still found); else the one question of the attempt's exercise with that prompt (its options were reworded
since); else the one with those option texts (its prompt was reworded). Only a snapshot none of these
identifies is pinned to what the seed draws in its exercise, which is how it has been graded until now.
Idempotent: it reads only rows still unnamed.
"""

from __future__ import annotations

import logging
from collections import defaultdict
from collections.abc import Iterable, Mapping
from dataclasses import dataclass

from sqlalchemy import and_, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.attempts.models import Attempt
from tradeschool.content.models import Exercise
from tradeschool.content.registry import Catalog, CourseRegistry
from tradeschool.exercises.quiz import QuizConfig, QuizGenerator, QuizVariant
from tradeschool.exercises.types import ExerciseType

logger = logging.getLogger("tradeschool.attempts")

#: Where the laid-out payload keeps the texts a question shows besides its prompt, per sub-kind.
_SHOWN_TEXTS = ("options", "items", "lefts")


@dataclass
class BackfillSummary:
    by_instance: int = 0
    by_prompt: int = 0
    by_options: int = 0
    by_seed: int = 0
    unresolved: int = 0

    def __str__(self) -> str:
        return (
            f"Question ids: {self.by_instance} by the exact instance shown, {self.by_prompt} by prompt, "
            f"{self.by_options} by option texts, {self.by_seed} by seed (text reworded beyond matching), "
            f"{self.unresolved} left unnamed (exercise gone)."
        )


def _variant_texts(variant: QuizVariant, locale: str) -> list[str]:
    texts = variant.options or variant.items
    if texts:
        return sorted(t.text.get(locale) for t in texts)
    return sorted(pair.left.get(locale) for pair in variant.pairs)


def _snapshot_texts(payload: object) -> list[str] | None:
    if not isinstance(payload, Mapping):
        return None
    for field in _SHOWN_TEXTS:
        shown = payload.get(field)
        if isinstance(shown, list):
            return sorted(str(entry.get("text")) for entry in shown if isinstance(entry, Mapping))
    return None


class _ShownQuestions:
    """Every quiz question of one course, to recognise the one a stored instance showed."""

    def __init__(self, registry: CourseRegistry) -> None:
        self.registry = registry
        self.by_prompt: dict[str, list[QuizConfig]] = defaultdict(list)
        for _, config in registry.exercise_configs.values():
            if not isinstance(config, QuizConfig):
                continue
            for variant in config.variants:
                single = config.only(variant.id)
                assert single is not None
                for prompt in {variant.prompt.get(locale) for locale in registry.languages}:
                    self.by_prompt[prompt].append(single)

    def exact(self, snapshot: Mapping[str, object], seed: int) -> str | None:
        generator = QuizGenerator()
        for single in self.by_prompt.get(str(snapshot.get("prompt")), []):
            for locale in self.registry.languages:
                instance = generator.generate(single, seed, locale)
                if instance.prompt == snapshot.get("prompt") and instance.payload == snapshot.get("payload"):
                    return single.variants[0].id
        return None

    def by_prompt_in(self, exercise_id: str, snapshot: Mapping[str, object]) -> str | None:
        prompt = snapshot.get("prompt")
        return _one(
            v
            for v in self._variants(exercise_id)
            if prompt in {v.prompt.get(locale) for locale in self.registry.languages}
        )

    def by_options_in(self, exercise_id: str, snapshot: Mapping[str, object]) -> str | None:
        texts = _snapshot_texts(snapshot.get("payload"))
        if not texts:
            return None
        return _one(
            v
            for v in self._variants(exercise_id)
            if texts in [_variant_texts(v, locale) for locale in self.registry.languages]
        )

    def _variants(self, exercise_id: str) -> list[QuizVariant]:
        config = self.registry.exercise_configs.get(exercise_id, (None, None))[1]
        return config.variants if isinstance(config, QuizConfig) else []


def _one(found: Iterable[QuizVariant]) -> str | None:
    """The id of the single match; two or more is no identification."""
    matches = list(found)
    return matches[0].id if len(matches) == 1 else None


async def backfill_variant_ids(catalog: Catalog, session: AsyncSession) -> BackfillSummary:
    summary = BackfillSummary()
    for slug, registry in sorted(catalog.courses.items()):
        rows = await session.execute(
            select(Attempt.id, Attempt.exercise_id, Attempt.seed, Attempt.instance_snapshot)
            .join(Exercise, and_(Exercise.course_id == Attempt.course_id, Exercise.id == Attempt.exercise_id))
            .where(
                Attempt.course_id == slug,
                Attempt.variant_id.is_(None),
                Attempt.question_id.is_(None),
                Exercise.type == ExerciseType.QUIZ,
            )
        )
        pending = rows.all()
        if not pending:
            continue
        questions = _ShownQuestions(registry)
        named: list[dict[str, object]] = []
        for attempt_id, exercise_key, seed, snapshot in pending:
            variant_id = _identify(registry, questions, summary, exercise_key, seed, snapshot)
            if variant_id is not None:
                named.append({"id": attempt_id, "variant_id": variant_id})
        if named:
            await session.execute(update(Attempt), named)
    await session.commit()
    logger.info("%s", summary)
    return summary


def _identify(
    registry: CourseRegistry,
    questions: _ShownQuestions,
    summary: BackfillSummary,
    exercise_key: str,
    seed: int,
    snapshot: Mapping[str, object],
) -> str | None:
    if found := questions.exact(snapshot, seed):
        summary.by_instance += 1
        return found
    exercise_id = registry.exercise_id_for_key(exercise_key)
    if exercise_id is None:
        summary.unresolved += 1
        return None
    if found := questions.by_prompt_in(exercise_id, snapshot):
        summary.by_prompt += 1
        return found
    if found := questions.by_options_in(exercise_id, snapshot):
        summary.by_options += 1
        return found
    if found := registry.drawn_variant_id(exercise_id, seed):
        summary.by_seed += 1
        return found
    summary.unresolved += 1
    return None
