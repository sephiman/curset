# SPDX-License-Identifier: AGPL-3.0-only
"""The questionnaire a PDF export prints after each tema: up to 20 of its questions, drawn from a seed.

The draw per tema depends only on (seed, the tema's key), so a tema prints the same questions in its own
PDF and inside its bloque's. Official and calibration items never print here: they are drawn only by the
presets that reproduce them.
"""

from __future__ import annotations

import random
import secrets
from typing import Any

from tradeschool.content.registry import CourseRegistry, ExportScope
from tradeschool.exams.draw import SEED_SPACE, PoolQuestion, Scope, question_pool
from tradeschool.exams.print_export import letter_quiz
from tradeschool.exercises.quiz import QuizConfig, QuizGenerator, QuizKind

QUESTIONS_PER_TEMA = 20
SEED_LIMIT = 2**32


def build_questionnaire(
    registry: CourseRegistry, scope: ExportScope | None, locale: str, seed: int | None = None
) -> dict[str, Any]:
    seed = seed if seed is not None else secrets.randbelow(SEED_LIMIT)
    generator = QuizGenerator()
    temas: list[dict[str, Any]] = []
    for block in registry.manifest.blocks:
        for module in block.modules:
            for lesson in module.lessons:
                if scope is not None and not scope.includes(module.id, lesson.id):
                    continue
                questions = _tema_questions(registry, generator, lesson.id, lesson.key, seed, locale)
                if questions:
                    temas.append({"lessonId": lesson.id, "title": lesson.title.get(locale), **questions})
    return {"seed": seed, "locale": locale, "temas": temas}


def _tema_questions(
    registry: CourseRegistry,
    generator: QuizGenerator,
    lesson_id: str,
    lesson_key: str,
    seed: int,
    locale: str,
) -> dict[str, list[dict[str, Any]]] | None:
    in_tema = question_pool(registry, Scope("lesson", frozenset({lesson_id})))
    pool = [q for q in in_tema if _printable(registry, q)]
    if not pool:
        return None
    rng = random.Random(f"{seed}:{lesson_key}")
    drawn = rng.sample(pool, min(QUESTIONS_PER_TEMA, len(pool)))
    printed: list[dict[str, Any]] = []
    keys: list[dict[str, Any]] = []
    for number, question in enumerate(drawn, start=1):
        item_seed = rng.randrange(SEED_SPACE)
        config = registry.get_exercise_config(question.exercise_id)
        assert config is not None and isinstance(config[1], QuizConfig)
        variant = next(v for v in config[1].variants if v.id == question.variant_id)
        lettered = letter_quiz(generator, config[1], variant, item_seed, locale)
        entry_out: dict[str, Any] = {
            "id": f"{question.exercise_id}/{variant.id}",
            "number": str(number),
            "prompt": lettered.prompt,
            "options": [{"letter": o["letter"], "text": o["text"]} for o in lettered.options],
        }
        if lettered.table is not None:
            entry_out["table"] = lettered.table
        printed.append(entry_out)
        keys.append({"number": str(number), "letter": lettered.correct_letter, "citation": variant.citation})
    return {"questions": printed, "keys": keys}


def _printable(registry: CourseRegistry, question: PoolQuestion) -> bool:
    """Stored single-choice questions: what letters A-D and a key citing its article can print.

    Generated items (C2's psicotécnicos) belong to no tema and carry no citation, so none is drawn here.
    """
    if question.variant_id is None:
        return False
    config = registry.get_exercise_config(question.exercise_id)
    if config is None or not isinstance(config[1], QuizConfig):
        return False
    variant = next(v for v in config[1].variants if v.id == question.variant_id)
    return variant.kind is QuizKind.SINGLE_CHOICE
