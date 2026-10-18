# SPDX-License-Identifier: AGPL-3.0-only
"""What an exam part draws: the pool its source names, the draw itself, and the load-time pool check.

The randomness is handed in (`Rand`), so the engine's one source of it — `secrets` — stays the thing a
test pins, and a draw is a pure function of that stream and the course.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol

from tradeschool.exams.presets import ExamPreset, PresetPart
from tradeschool.exercises.case import CaseConfig, question_seeds
from tradeschool.exercises.quiz import QuizConfig, QuizGenerator
from tradeschool.exercises.types import ExerciseType

if TYPE_CHECKING:
    from tradeschool.content.registry import CourseRegistry

SEED_SPACE = 2**62
# A variant is found by drawing seeds until one selects it; a bank this many times larger than its
# variant count without a hit means the selection rule changed under the draw.
_SEED_SEARCH_FACTOR = 10_000


class Rand(Protocol):
    def choice(self, seq: Sequence[str]) -> str: ...

    def randbelow(self, n: int) -> int: ...


class DrawError(RuntimeError):
    """The pool cannot supply the part as declared."""


@dataclass(frozen=True)
class PoolQuestion:
    """One distinct question: a quiz variant, or a generated exercise (any seed is a fresh question)."""

    exercise_id: str
    variant_id: str | None = None


@dataclass(frozen=True)
class DrawnQuestion:
    exercise_id: str
    seed: int
    #: Set on a case question: the exercise is the case, this names the question inside it.
    question_id: str | None = None
    reserve: bool = False


@dataclass(frozen=True)
class DrawnPart:
    part_id: str
    questions: list[DrawnQuestion]
    #: Case parts: the cases offered, in the order shown.
    cases: list[str]


def source_level(part: PresetPart, target: str | None) -> tuple[str | None, str | None]:
    """(level, id) of a non-case source: the whole course, or one block, module or lesson."""
    source = part.source
    if source.each is not None:
        return source.each, target
    for level in ("block", "module", "lesson"):
        named = getattr(source, level)
        if named is not None:
            return level, named
    return None, None


def per_module_scope(registry: CourseRegistry, level: str | None, target: str | None) -> list[str]:
    """Modules with a playable bank, in course order, inside the source (a per-module draw's rows)."""
    out: list[str] = []
    for block, module in registry.manifest.iter_modules():
        if level == "block" and block.id != target:
            continue
        if level == "module" and module.id != target:
            continue
        if registry.playable_module_exercises(module.id):
            out.append(module.id)
    return out


def question_pool(registry: CourseRegistry, level: str | None, target: str | None) -> list[PoolQuestion]:
    """Every distinct question under the source, in course order; cases are drawn only by a case part."""
    pool: list[PoolQuestion] = []
    for exercise_id in registry.scope_exercise_ids(level, target):
        config = registry.get_exercise_config(exercise_id)
        if config is None or config[0] is ExerciseType.CASE:
            continue
        if isinstance(config[1], QuizConfig):
            pool.extend(PoolQuestion(exercise_id, variant.id) for variant in config[1].variants)
        else:
            pool.append(PoolQuestion(exercise_id))
    return pool


def case_pool(registry: CourseRegistry) -> list[str]:
    return [
        exercise_id
        for exercise_id in registry.scope_exercise_ids(None, None)
        if registry.case_config(exercise_id) is not None
    ]


def _sample(rand: Rand, population: int, k: int) -> list[int]:
    """k distinct indices, kept in draw order (a partial Fisher-Yates over `randbelow`)."""
    indices = list(range(population))
    for i in range(k):
        j = i + rand.randbelow(population - i)
        indices[i], indices[j] = indices[j], indices[i]
    return indices[:k]


def _seed_for(registry: CourseRegistry, question: PoolQuestion, rand: Rand) -> int:
    seed = rand.randbelow(SEED_SPACE)
    if question.variant_id is None:
        return seed
    config = registry.get_exercise_config(question.exercise_id)
    assert config is not None and isinstance(config[1], QuizConfig)
    generator = QuizGenerator()
    for _ in range(_SEED_SEARCH_FACTOR * len(config[1].variants)):
        if generator.variant(config[1], seed).id == question.variant_id:
            return seed
        seed = rand.randbelow(SEED_SPACE)
    raise DrawError(f"no seed selects variant {question.variant_id!r} of {question.exercise_id!r}")


def draw_per_module(registry: CourseRegistry, modules: list[str], rand: Rand) -> list[DrawnQuestion]:
    """One exercise per module, each with a fresh seed — choice then seed, module by module."""
    drawn: list[DrawnQuestion] = []
    for module_id in modules:
        exercise_id = rand.choice(registry.playable_module_exercises(module_id))
        drawn.append(DrawnQuestion(exercise_id, rand.randbelow(SEED_SPACE)))
    return drawn


def draw_random(
    registry: CourseRegistry, pool: list[PoolQuestion], counted: int, reserve: int, rand: Rand
) -> list[DrawnQuestion]:
    """`counted` distinct questions in course order, then `reserve` more, also in course order."""
    if len(pool) < counted + reserve:
        raise DrawError(f"the pool holds {len(pool)} questions; the part needs {counted + reserve}")
    picked = _sample(rand, len(pool), counted + reserve)
    main, extra = sorted(picked[:counted]), sorted(picked[counted:])
    return [DrawnQuestion(pool[i].exercise_id, _seed_for(registry, pool[i], rand)) for i in main] + [
        DrawnQuestion(pool[i].exercise_id, _seed_for(registry, pool[i], rand), reserve=True) for i in extra
    ]


def draw_cases(
    registry: CourseRegistry, pool: list[str], offered: int, counted: int, reserve: int, rand: Rand
) -> tuple[list[str], list[DrawnQuestion]]:
    """`offered` distinct cases, each whole: its first `counted` questions, then `reserve` more."""
    if len(pool) < offered:
        raise DrawError(f"the course has {len(pool)} cases; the part offers {offered}")
    cases = [pool[i] for i in _sample(rand, len(pool), offered)]
    drawn: list[DrawnQuestion] = []
    for case_id in cases:
        config = registry.case_config(case_id)
        assert config is not None
        seeds = question_seeds(rand.randbelow(SEED_SPACE), len(config.questions))
        for index, (question, seed) in enumerate(zip(config.questions, seeds, strict=True)):
            if index >= counted + reserve:
                break
            drawn.append(DrawnQuestion(case_id, seed, question.id, reserve=index >= counted))
    return cases, drawn


def draw_part(registry: CourseRegistry, part: PresetPart, target: str | None, rand: Rand) -> DrawnPart:
    if part.source.cases:
        assert part.choose is not None and part.questions is not None
        cases, questions = draw_cases(
            registry, case_pool(registry), part.choose, part.questions, part.reserve, rand
        )
        return DrawnPart(part.id, questions, cases)
    level, named = source_level(part, target)
    if part.draw == "per-module":
        return DrawnPart(
            part.id, draw_per_module(registry, per_module_scope(registry, level, named), rand), []
        )
    assert part.questions is not None
    pool = question_pool(registry, level, named)
    return DrawnPart(part.id, draw_random(registry, pool, part.questions, part.reserve, rand), [])


def counted_questions(registry: CourseRegistry, part: PresetPart, target: str | None) -> int:
    """How many questions the part counts: declared, or one per module with a bank for a per-module draw."""
    if part.draw == "per-module":
        return len(per_module_scope(registry, *source_level(part, target)))
    assert part.questions is not None
    return part.questions


def preset_targets(registry: CourseRegistry, preset: ExamPreset) -> list[str]:
    """The blocks, modules or lessons a parametric preset can be sat on: those whose pool is enough."""
    level = preset.parametric
    if level is None:
        return []
    candidates = {
        "block": [block.id for block in registry.manifest.blocks],
        "module": [module.id for _, module in registry.manifest.iter_modules()],
        "lesson": [lesson.id for _, lesson in registry.manifest.iter_lessons()],
    }[level]
    return [target for target in candidates if not pool_shortfalls(registry, preset, target)]


def pool_shortfalls(registry: CourseRegistry, preset: ExamPreset, target: str | None) -> list[str]:
    """Why the course cannot supply this preset (for `target`, if parametric); empty when it can."""
    problems: list[str] = []
    for part in preset.parts:
        if part.source.cases:
            assert part.choose is not None and part.questions is not None
            cases = case_pool(registry)
            if len(cases) < part.choose:
                problems.append(f"part {part.id!r} offers {part.choose} cases; the course has {len(cases)}")
            needed = part.questions + part.reserve
            for case_id in cases:
                config: CaseConfig | None = registry.case_config(case_id)
                if config is not None and len(config.questions) < needed:
                    problems.append(
                        f"case {case_id!r} has {len(config.questions)} questions; "
                        f"part {part.id!r} needs {needed}"
                    )
            continue
        level, named = source_level(part, target)
        if part.draw == "per-module":
            if not per_module_scope(registry, level, named):
                problems.append(f"part {part.id!r} has no module with a bank")
            continue
        assert part.questions is not None
        available = len(question_pool(registry, level, named))
        if available < part.questions + part.reserve:
            problems.append(
                f"part {part.id!r} needs {part.questions + part.reserve} questions; "
                f"the pool holds {available}"
            )
        if part.scoring is not None and part.scoring.minimum_raw >= part.questions:
            problems.append(
                f"part {part.id!r}: minimum_raw must be below the maximum raw score {part.questions}"
            )
    return problems


def check_presets(registry: CourseRegistry) -> list[str]:
    """Load-time check: every fixed preset can be drawn, every parametric one on at least one target."""
    problems: list[str] = []
    for preset in registry.manifest.exams:
        if preset.parametric is None:
            problems += [f"exam {preset.id!r}: {p}" for p in pool_shortfalls(registry, preset, None)]
        elif not preset_targets(registry, preset):
            problems.append(f"exam {preset.id!r}: no {preset.parametric} has the questions it needs")
    return problems
