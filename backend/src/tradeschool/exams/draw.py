# SPDX-License-Identifier: AGPL-3.0-only
"""What an exam part draws: the pool its source names, the draw itself, and the load-time pool check.

The randomness is handed in (`Rand`), so the engine's one source of it — `secrets` — stays the thing a
test pins, and a draw is a pure function of that stream and the course.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from itertools import combinations
from typing import TYPE_CHECKING, Protocol

from tradeschool.exams.presets import ExamPreset, PartSource, PresetPart, PresetSource
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
    #: The quiz question drawn, stored on the attempt; None for a case or a generated exercise.
    variant_id: str | None = None


@dataclass(frozen=True)
class DrawnPart:
    part_id: str
    questions: list[DrawnQuestion]
    #: Case parts: the cases offered, in the order shown.
    cases: list[str]


@dataclass(frozen=True)
class Scope:
    """What a source covers: the whole course (`level` None), or the named blocks, modules or lesson."""

    level: str | None
    ids: frozenset[str] = frozenset()


def source_scope(source: PresetSource, target: str | None) -> Scope:
    """The scope of a non-case source; a parametric one (`each`) covers the target picked at start."""
    if source.each is not None:
        return Scope(source.each, frozenset({target}) if target else frozenset())
    if source.exercise is not None:
        return Scope("exercise", frozenset({source.exercise}))
    if source.modules:
        return Scope("module", frozenset(source.modules))
    for level in ("block", "module", "lesson"):
        named = getattr(source, level)
        if named is not None:
            return Scope(level, frozenset({named}))
    return Scope(None)


def _exercise_ids(registry: CourseRegistry, scope: Scope) -> list[str]:
    if scope.level == "exercise":
        return sorted(scope.ids)
    targets: list[str | None] = [*sorted(scope.ids)] or [None]
    if len(targets) == 1:
        return registry.scope_exercise_ids(scope.level, targets[0])
    inside = {exercise for target in targets for exercise in registry.scope_exercise_ids(scope.level, target)}
    return [exercise for exercise in registry.scope_exercise_ids(None, None) if exercise in inside]


def per_module_scope(registry: CourseRegistry, scope: Scope) -> list[str]:
    """Modules with a playable bank, in course order, inside the scope (a per-module draw's rows)."""
    out: list[str] = []
    for block, module in registry.manifest.iter_modules():
        if scope.level == "block" and block.id not in scope.ids:
            continue
        if scope.level == "module" and module.id not in scope.ids:
            continue
        if _module_questions(registry, module.id):
            out.append(module.id)
    return out


def _module_questions(registry: CourseRegistry, module_id: str) -> list[str]:
    """The module's playable exercises a question draw may pick: all but its cases and official exams."""
    return [
        e
        for e in registry.playable_module_exercises(module_id)
        if registry.case_config(e) is None and not registry.is_official(e)
    ]


def question_pool(registry: CourseRegistry, scope: Scope) -> list[PoolQuestion]:
    """Every distinct question under the scope, in course order; cases are drawn only by a case part."""
    pool: list[PoolQuestion] = []
    for exercise_id in _exercise_ids(registry, scope):
        config = registry.get_exercise_config(exercise_id)
        if config is None or config[0] is ExerciseType.CASE:
            continue
        if scope.level != "exercise" and registry.is_official(exercise_id):
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


def _drawn(
    registry: CourseRegistry, question: PoolQuestion, rand: Rand, *, reserve: bool = False
) -> DrawnQuestion:
    seed = _seed_for(registry, question, rand)
    return DrawnQuestion(question.exercise_id, seed, reserve=reserve, variant_id=question.variant_id)


def draw_per_module(registry: CourseRegistry, modules: list[str], rand: Rand) -> list[DrawnQuestion]:
    """One exercise per module, each with a fresh seed — choice then seed, module by module."""
    drawn: list[DrawnQuestion] = []
    for module_id in modules:
        exercise_id = rand.choice(_module_questions(registry, module_id))
        seed = rand.randbelow(SEED_SPACE)
        drawn.append(
            DrawnQuestion(exercise_id, seed, variant_id=registry.drawn_variant_id(exercise_id, seed))
        )
    return drawn


def draw_random(
    registry: CourseRegistry, pool: list[PoolQuestion], counted: int, reserve: int, rand: Rand
) -> list[DrawnQuestion]:
    """`counted` distinct questions in course order, then `reserve` more, also in course order."""
    if len(pool) < counted + reserve:
        raise DrawError(f"the pool holds {len(pool)} questions; the part needs {counted + reserve}")
    picked = _sample(rand, len(pool), counted + reserve)
    main, extra = sorted(picked[:counted]), sorted(picked[counted:])
    return [_drawn(registry, pool[i], rand) for i in main] + [
        _drawn(registry, pool[i], rand, reserve=True) for i in extra
    ]


def draw_all(registry: CourseRegistry, pool: list[PoolQuestion], rand: Rand) -> list[DrawnQuestion]:
    """Every question of the pool, in course order."""
    return [_drawn(registry, question, rand) for question in pool]


def draw_composite(
    registry: CourseRegistry, part: PresetPart, target: str | None, rand: Rand
) -> list[DrawnQuestion]:
    """Each source's questions, shuffled together; then `reserve` more from what the random sources left."""
    counted: list[DrawnQuestion] = []
    spare: list[PoolQuestion] = []
    for number, entry in enumerate(part.draws, start=1):
        scope = source_scope(entry.source, target)
        if entry.draw == "per-module":
            counted += draw_per_module(registry, per_module_scope(registry, scope), rand)
            continue
        pool = question_pool(registry, scope)
        if entry.draw == "all":
            counted += draw_all(registry, pool, rand)
            continue
        assert entry.questions is not None
        if len(pool) < entry.questions:
            raise DrawError(f"source {number} holds {len(pool)} questions; it needs {entry.questions}")
        picked = _sample(rand, len(pool), entry.questions)
        counted += [_drawn(registry, pool[i], rand) for i in sorted(picked)]
        chosen = set(picked)
        spare += [question for i, question in enumerate(pool) if i not in chosen]
    shuffled = [counted[i] for i in _sample(rand, len(counted), len(counted))]
    if len(spare) < part.reserve:
        raise DrawError(f"the sources leave {len(spare)} questions; the part needs {part.reserve} in reserve")
    extra = sorted(_sample(rand, len(spare), part.reserve))
    return shuffled + [_drawn(registry, spare[i], rand, reserve=True) for i in extra]


def draw_cases(
    registry: CourseRegistry,
    pool: list[str],
    offered: int,
    counted: int,
    reserve: int,
    rand: Rand,
    pairs: list[list[str]] | None = None,
) -> tuple[list[str], list[DrawnQuestion]]:
    """`offered` distinct cases, each whole: its first `counted` questions, then `reserve` more."""
    if pairs:
        pair_idx = rand.randbelow(len(pairs))
        cases = list(pairs[pair_idx])
    else:
        if len(pool) < offered:
            raise DrawError(f"the course has {len(pool)} cases; the part offers {offered}")
        cases = [pool[i] for i in _sample(rand, len(pool), offered)]
    drawn: list[DrawnQuestion] = []
    for case_id in cases:
        config = registry.case_config(case_id)
        assert config is not None
        seeds = question_seeds(rand.randbelow(SEED_SPACE), len(config.questions))
        for index, (question, seed) in enumerate(zip(config.questions, seeds, strict=False)):
            if index >= counted + reserve:
                break
            drawn.append(DrawnQuestion(case_id, seed, question.id, reserve=index >= counted))
    return cases, drawn


def draw_part(registry: CourseRegistry, part: PresetPart, target: str | None, rand: Rand) -> DrawnPart:
    if part.cases:
        assert part.choose is not None and part.questions is not None
        cases, questions = draw_cases(
            registry,
            case_pool(registry),
            part.choose,
            part.questions,
            part.reserve,
            rand,
            pairs=part.case_pairs,
        )
        return DrawnPart(part.id, questions, cases)
    if part.sources is not None:
        return DrawnPart(part.id, draw_composite(registry, part, target, rand), [])
    entry = part.draws[0]
    scope = source_scope(entry.source, target)
    if entry.draw == "per-module":
        return DrawnPart(part.id, draw_per_module(registry, per_module_scope(registry, scope), rand), [])
    pool = question_pool(registry, scope)
    if entry.draw == "all":
        return DrawnPart(part.id, draw_all(registry, pool, rand), [])
    assert entry.questions is not None
    return DrawnPart(part.id, draw_random(registry, pool, entry.questions, part.reserve, rand), [])


def _source_count(registry: CourseRegistry, entry: PartSource, target: str | None) -> int:
    scope = source_scope(entry.source, target)
    if entry.draw == "per-module":
        return len(per_module_scope(registry, scope))
    if entry.draw == "all":
        return len(question_pool(registry, scope))
    assert entry.questions is not None
    return entry.questions


def counted_questions(registry: CourseRegistry, part: PresetPart, target: str | None) -> int:
    """How many questions the part counts: declared, or what each source's draw mode takes, summed."""
    if part.cases:
        assert part.questions is not None
        return part.questions
    return sum(_source_count(registry, entry, target) for entry in part.draws)


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
        if part.cases:
            assert part.choose is not None and part.questions is not None
            if part.case_pairs is not None:
                if not part.case_pairs:
                    problems.append(f"part {part.id!r}: case_pairs is empty")
                cases_to_check = {c for pair in part.case_pairs for c in pair}
            else:
                cases = case_pool(registry)
                if len(cases) < part.choose:
                    problems.append(
                        f"part {part.id!r} offers {part.choose} cases; the course has {len(cases)}"
                    )
                cases_to_check = set(cases)
            for case_id in sorted(cases_to_check):
                config: CaseConfig | None = registry.case_config(case_id)
                if config is None:
                    problems.append(f"case {case_id!r} not found in course")
                elif len(config.questions) < part.questions:
                    problems.append(
                        f"case {case_id!r} has {len(config.questions)} questions; "
                        f"part {part.id!r} needs {part.questions}"
                    )
            continue
        problems += _source_shortfalls(registry, part, target)
        counted = counted_questions(registry, part, target)
        if part.scoring is not None and counted and part.scoring.minimum_raw >= counted:
            problems.append(f"part {part.id!r}: minimum_raw must be below the maximum raw score {counted}")
    return problems


def _source_shortfalls(registry: CourseRegistry, part: PresetPart, target: str | None) -> list[str]:
    """Why a question part's sources cannot supply it: a short pool, two sources sharing questions, or
    too little left over for the reserve."""
    problems: list[str] = []
    composite = part.sources is not None
    pools: list[set[PoolQuestion]] = []
    spare = 0
    for number, entry in enumerate(part.draws, start=1):
        label = f"part {part.id!r}" + (f" source {number}" if composite else "")
        scope = source_scope(entry.source, target)
        pool = question_pool(registry, scope)
        pools.append(set(pool))
        if entry.draw == "per-module":
            if not per_module_scope(registry, scope):
                problems.append(f"{label} has no module with a bank")
            continue
        if entry.draw == "all":
            if not pool:
                problems.append(f"{label} draws every question of an empty pool")
            continue
        assert entry.questions is not None
        needed = entry.questions + (0 if composite else part.reserve)
        if len(pool) < needed:
            problems.append(f"{label} needs {needed} questions; the pool holds {len(pool)}")
        spare += max(len(pool) - entry.questions, 0)
    for first, second in combinations(range(len(pools)), 2):
        if pools[first] & pools[second]:
            problems.append(f"part {part.id!r}: sources {first + 1} and {second + 1} share questions")
    if composite and spare < part.reserve:
        problems.append(f"part {part.id!r} needs {part.reserve} reserve questions; its sources leave {spare}")
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
