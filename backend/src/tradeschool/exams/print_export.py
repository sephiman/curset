# SPDX-License-Identifier: AGPL-3.0-only
"""Printable exam document generator for simulation and official exam presets (delta A, B, H).

Generates a complete printable exam session with:
- Part 1: counted questions + reserve questions
- Part 2: both offered cases of the pair (scenario + 20 questions each)
- Key sheet: answer keys with bijection against printed questions and lettered options
"""

from __future__ import annotations

import secrets
from collections.abc import Sequence
from typing import Any

from tradeschool.content.registry import CourseRegistry
from tradeschool.exams.draw import DrawError, draw_part
from tradeschool.exams.presets import ExamPreset
from tradeschool.exercises.quiz import QuizConfig, QuizGenerator


class ExamPrintRand:
    def __init__(self, seed: int = 42) -> None:
        import random

        self._rng = random.Random(seed)

    def choice(self, seq: Sequence[str]) -> str:
        return self._rng.choice(seq)

    def randbelow(self, n: int) -> int:
        return self._rng.randrange(n)


def build_exam_print(
    registry: CourseRegistry, preset_id: str, locale: str = "es", seed: int | None = None
) -> dict[str, Any]:
    preset: ExamPreset | None = next((p for p in registry.manifest.exams if p.id == preset_id), None)
    if preset is None:
        raise DrawError(f"No preset {preset_id!r} in course {registry.slug!r}")

    rand = ExamPrintRand(seed if seed is not None else secrets.randbelow(2**32))
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
                config_pair = registry.get_exercise_config(dq.exercise_id)
                assert config_pair is not None
                quiz_config = config_pair[1]
                assert isinstance(quiz_config, QuizConfig)
                variant = (
                    next((v for v in quiz_config.variants if v.id == dq.variant_id), quiz_config.variants[0])
                    if dq.variant_id
                    else quiz_config.variants[0]
                )

                # Option letters
                instance = quiz_gen.generate(quiz_config.only(variant.id) or quiz_config, dq.seed, locale)
                raw_opts = instance.payload.get("options", [])
                assert isinstance(raw_opts, list)
                payload_opts: list[dict[str, Any]] = [o for o in raw_opts if isinstance(o, dict)]
                opts_with_letters = [
                    {"id": str(o["id"]), "letter": chr(65 + i), "text": o["text"]}
                    for i, o in enumerate(payload_opts)
                ]

                correct_opt = next(o for o in variant.options if o.correct)
                correct_idx = next(i for i, o in enumerate(payload_opts) if o["id"] == correct_opt.id)
                correct_letter = chr(65 + correct_idx)

                q_num = str(index)
                part_questions.append(
                    {
                        "id": f"{dq.exercise_id}/{variant.id}",
                        "number": q_num,
                        "reserve": dq.reserve,
                        "prompt": instance.prompt,
                        "options": opts_with_letters,
                    }
                )
                part_keys.append(
                    {
                        "number": q_num,
                        "reserve": dq.reserve,
                        "correctOptionId": correct_opt.id,
                        "correctLetter": correct_letter,
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
        "title": preset.title.get(locale),
        "description": preset.description.get(locale) if preset.description else None,
        "timeLimitMinutes": preset.time_limit_minutes,
        "pause": preset.pause,
        "parts": parts_out,
        "keySheet": key_sheet,
    }
