# SPDX-License-Identifier: AGPL-3.0-only
"""Printable exam document generator for simulation and official exam presets (delta A, B, H).

Generates a complete printable exam session with:
- Part 1: counted questions + reserve questions
- Part 2: both offered cases of the pair (scenario + 20 questions each)
- Key sheet: answer keys with bijection against printed questions and lettered options
"""

from __future__ import annotations

import secrets
from dataclasses import dataclass
from typing import Any

from tradeschool.content.registry import CourseRegistry
from tradeschool.exams.draw import DrawError, SeededRand, draw_part
from tradeschool.exams.presets import ExamPreset
from tradeschool.exercises.psicotecnico import PsicotecnicoConfig, build_item, option_id
from tradeschool.exercises.quiz import QuizConfig, QuizGenerator, QuizVariant
from tradeschool.psicotecnico.registry import load_generator


@dataclass(frozen=True)
class LetteredQuestion:
    """A single-choice question as printed: options lettered A-D in the order the seed shuffled them."""

    prompt: str
    options: list[dict[str, Any]]
    table: object | None
    correct_option_id: str
    correct_letter: str


def letter_quiz(
    generator: QuizGenerator, config: QuizConfig, variant: QuizVariant, seed: int, locale: str
) -> LetteredQuestion:
    instance = generator.generate(config.only(variant.id) or config, seed, locale)
    raw_opts = instance.payload.get("options", [])
    assert isinstance(raw_opts, list)
    shown: list[dict[str, Any]] = [o for o in raw_opts if isinstance(o, dict)]
    correct = next(o for o in variant.options if o.correct)
    correct_idx = next(i for i, o in enumerate(shown) if o["id"] == correct.id)
    return LetteredQuestion(
        prompt=instance.prompt,
        options=[{"id": str(o["id"]), "letter": chr(65 + i), "text": o["text"]} for i, o in enumerate(shown)],
        table=instance.payload.get("table"),
        correct_option_id=correct.id,
        correct_letter=chr(65 + correct_idx),
    )


def build_exam_print(
    registry: CourseRegistry, preset_id: str, locale: str = "es", seed: int | None = None
) -> dict[str, Any]:
    preset: ExamPreset | None = next((p for p in registry.manifest.exams if p.id == preset_id), None)
    if preset is None:
        raise DrawError(f"No preset {preset_id!r} in course {registry.slug!r}")

    seed = seed if seed is not None else secrets.randbelow(2**32)
    rand = SeededRand(seed)
    quiz_gen = QuizGenerator()

    parts_out: list[dict[str, Any]] = []
    key_sheet: list[dict[str, Any]] = []

    for part in preset.parts:
        if part.cases:
            # Case part: draw the cases of the pair
            drawn_part = draw_part(registry, part, None, rand)
            offered_cases = drawn_part.cases
            cases_data: list[dict[str, Any]] = []

            for case_idx, case_id in enumerate(offered_cases, start=1):
                config = registry.case_config(case_id)
                assert config is not None
                case_title = config.title.get(locale)
                scenario = config.scenario.get(locale)
                questions_data: list[dict[str, Any]] = []
                case_keys: list[dict[str, Any]] = []

                for q_idx, q in enumerate(config.questions, start=1):
                    # We preserve exact option order (A, B, C, D)
                    q_num = f"S{case_idx}.{q_idx}"
                    q_options = [
                        {"id": opt.id, "letter": chr(65 + i), "text": opt.text.get(locale)}
                        for i, opt in enumerate(q.options)
                    ]
                    correct_opt = next(opt for opt in q.options if opt.correct)
                    correct_idx = next(i for i, opt in enumerate(q.options) if opt.correct)
                    correct_letter = chr(65 + correct_idx)

                    questions_data.append(
                        {
                            "id": q.id,
                            "number": q_num,
                            "prompt": q.prompt.get(locale),
                            "options": q_options,
                        }
                    )
                    case_keys.append(
                        {
                            "number": q_num,
                            "correctOptionId": correct_opt.id,
                            "correctLetter": correct_letter,
                            "explanation": q.explanation.get(locale) if q.explanation else None,
                        }
                    )

                cases_data.append(
                    {
                        "id": case_id,
                        "title": case_title,
                        "scenario": scenario,
                        "questions": questions_data,
                    }
                )
                key_sheet.append(
                    {
                        "partId": part.id,
                        "title": f"Supuesto {case_idx}: {case_title}",
                        "keys": case_keys,
                    }
                )

            parts_out.append(
                {
                    "id": part.id,
                    "title": part.title.get(locale) if part.title else "Segunda parte",
                    "kind": "cases",
                    "cases": cases_data,
                }
            )

        else:
            # Question part (composite or all)
            drawn_part = draw_part(registry, part, None, rand)
            part_questions: list[dict[str, Any]] = []
            part_keys: list[dict[str, Any]] = []

            for index, dq in enumerate(drawn_part.questions, start=1):
                if registry.generator_use(dq.exercise_id) is not None:
                    printed, keyed = _generated_entry(registry, dq.exercise_id, dq.seed, index, dq.reserve)
                    part_questions.append(printed)
                    part_keys.append(keyed)
                    continue
                config_pair = registry.get_exercise_config(dq.exercise_id)
                assert config_pair is not None
                quiz_config = config_pair[1]
                assert isinstance(quiz_config, QuizConfig)
                variant = (
                    next((v for v in quiz_config.variants if v.id == dq.variant_id), quiz_config.variants[0])
                    if dq.variant_id
                    else quiz_config.variants[0]
                )

                lettered = letter_quiz(quiz_gen, quiz_config, variant, dq.seed, locale)
                q_num = str(index)
                printed_question: dict[str, Any] = {
                    "id": f"{dq.exercise_id}/{variant.id}",
                    "number": q_num,
                    "reserve": dq.reserve,
                    "prompt": lettered.prompt,
                    "options": lettered.options,
                }
                if lettered.table is not None:
                    printed_question["table"] = lettered.table
                part_questions.append(printed_question)
                part_keys.append(
                    {
                        "number": q_num,
                        "reserve": dq.reserve,
                        "correctOptionId": lettered.correct_option_id,
                        "correctLetter": lettered.correct_letter,
                        "explanation": variant.explanation.get(locale) if variant.explanation else None,
                    }
                )

            key_sheet.append(
                {
                    "partId": part.id,
                    "title": part.title.get(locale) if part.title else "Primera parte",
                    "keys": part_keys,
                }
            )
            parts_out.append(
                {
                    "id": part.id,
                    "title": part.title.get(locale) if part.title else "Primera parte",
                    "kind": "questions",
                    "questions": part_questions,
                }
            )

    return {
        "presetId": preset.id,
        # The paper regenerates from this seed: it is printed in the footer.
        "seed": seed,
        "title": preset.title.get(locale),
        "description": preset.description.get(locale) if preset.description else None,
        "timeLimitMinutes": preset.time_limit_minutes,
        "pause": preset.pause,
        "parts": parts_out,
        "keySheet": key_sheet,
    }


def _generated_entry(
    registry: CourseRegistry, exercise_id: str, seed: int, number: int, reserve: bool
) -> tuple[dict[str, Any], dict[str, Any]]:
    """A generated item as printed (stem, table, lettered options) and its key-sheet line, key from the "
    "solver."""
    config_pair = registry.get_exercise_config(exercise_id)
    assert config_pair is not None and isinstance(config_pair[1], PsicotecnicoConfig)
    item = build_item(config_pair[1], seed)
    key = load_generator(config_pair[1].generator).solve(item)
    options = [
        {"id": option_id(i), "letter": chr(65 + i), "text": text} for i, text in enumerate(item.options)
    ]
    printed: dict[str, Any] = {
        "id": f"{exercise_id}:{seed}",
        "number": str(number),
        "reserve": reserve,
        "prompt": item.stem,
        "options": options,
    }
    if item.table is not None:
        printed["table"] = {
            "title": item.table.title,
            "header": list(item.table.header),
            "rows": [list(row) for row in item.table.rows],
        }
    keyed = {
        "number": str(number),
        "reserve": reserve,
        "correctOptionId": option_id(key),
        "correctLetter": chr(65 + key),
        "explanation": item.explanation,
    }
    return printed, keyed
