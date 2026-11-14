# SPDX-License-Identifier: AGPL-3.0-only
"""The backend-in-depth generators (requirements 6.3): properties, bias guards, goldens, placeholders."""

from __future__ import annotations

import json
import random
import re
from fractions import Fraction
from pathlib import Path

import pytest

from test_quiz_answer_bias import (
    SIGMA,
    Answered,
    _length_edge,
    _longest_is_correct,
    _position_z,
    _report,
)
from tradeschool.content.registry import load_registry
from tradeschool.exercises.psicotecnico import PsicotecnicoConfig, build_item
from tradeschool.psicotecnico.backend.catalogue import BACKEND_GENERATORS, unfilled_citations
from tradeschool.psicotecnico.contract import verify
from tradeschool.psicotecnico.goldens import fingerprint, golden_items
from tradeschool.psicotecnico.item import Params
from tradeschool.psicotecnico.registry import GENERATORS, is_known

COURSE = Path(__file__).resolve().parents[2] / "content" / "backend-in-depth"
FINGERPRINTS = Path(__file__).resolve().parent / "goldens" / "backend-generators-fingerprints.json"
IDS = sorted(BACKEND_GENERATORS)
ITEMS_PER_GENERATOR = 1_000


def test_the_thirteen_families_of_requirements_6_3_are_registered() -> None:
    assert len(IDS) == 13
    assert all(is_known(generator_id) for generator_id in IDS)


def test_the_age_c2_registry_is_untouched_by_the_backend_generators() -> None:
    assert len(GENERATORS) == 13
    assert not set(GENERATORS) & set(BACKEND_GENERATORS)


def test_the_course_declares_every_generator() -> None:
    registry = load_registry(COURSE, check_excerpts=False)
    assert sorted(use.generator for use in registry.generator_uses()) == IDS
    assert registry.published  # published at the end of S3 (requirements 8.1)


@pytest.mark.parametrize("generator_id", IDS)
def test_property_tests_hold_over_many_seeded_items_at_every_level(generator_id: str) -> None:
    assert verify(BACKEND_GENERATORS[generator_id], per_level=300, base=11) == []


@pytest.mark.parametrize("generator_id", IDS)
def test_the_same_seed_builds_the_same_item(generator_id: str) -> None:
    generator = BACKEND_GENERATORS[generator_id]
    for level in generator.levels:
        assert generator.generate(99, Params(level)) == generator.generate(99, Params(level))


@pytest.mark.parametrize("generator_id", IDS)
def test_every_item_has_four_distinct_options_and_exactly_one_correct(generator_id: str) -> None:
    generator = BACKEND_GENERATORS[generator_id]
    for level in generator.levels:
        for seed in range(150):
            item = generator.generate(seed, Params(level))
            assert len(set(item.options)) == 4
            assert [i for i, _ in enumerate(item.options) if generator.solve(item) == i] == [item.key]


@pytest.mark.parametrize("generator_id", IDS)
def test_the_learner_text_never_shows_a_placeholder_nor_names_an_option_by_letter(generator_id: str) -> None:
    generator = BACKEND_GENERATORS[generator_id]
    for level in generator.levels:
        for seed in range(150):
            item = generator.generate(seed, Params(level))
            text = f"{item.stem} {item.explanation}"
            assert "TODO" not in text
            assert not re.search(r"\b(option|answer|choice) [A-Da-d]\b", text), text
            assert not re.search(r"\b[A-D]\) ", item.explanation)


def test_an_owed_citation_names_its_lesson_and_a_suggestion() -> None:
    owed = unfilled_citations()
    assert all(re.fullmatch(r"m\d\d-l\d\d", citation.lesson) and citation.suggested for _, citation in owed)


@pytest.mark.parametrize("generator", IDS)
def test_a_confirmed_citation_is_cited_by_its_own_lesson(generator: str) -> None:
    citation = BACKEND_GENERATORS[generator].citation
    if citation.confirmed is None:
        pytest.skip("owed by its module session")
    lesson = (COURSE / "en" / "lessons" / f"{citation.lesson}.md").read_text(encoding="utf-8")
    refs = [ref.strip() for ref in citation.confirmed.split(";")]
    # an F citation is inline code; a class J rule is cited as the ref of its judgement block
    assert [ref for ref in refs if f"`{ref}`" not in lesson and f'ref="{ref}"' not in lesson] == []


def _declared() -> list[PsicotecnicoConfig]:
    registry = load_registry(COURSE, check_excerpts=False)
    return [
        PsicotecnicoConfig(type="psicotecnico", generator=use.generator, difficulty=use.difficulty)
        for use in registry.generator_uses()
    ]


def _answered(config: PsicotecnicoConfig) -> list[Answered]:
    rng = random.Random(20261113)
    rows: list[Answered] = []
    for _ in range(ITEMS_PER_GENERATOR):
        item = build_item(config, rng.randrange(2**62))
        rows.append(
            Answered(
                exercise=config.generator,
                variant=str(item.seed),
                lengths=tuple(len(option) for option in item.options),
                correct=frozenset({item.key}),
            )
        )
    return rows


@pytest.mark.parametrize("config", _declared(), ids=lambda c: c.generator)
def test_the_answer_is_dealt_to_every_slot_equally(config: PsicotecnicoConfig) -> None:
    stats = _position_z(_answered(config))
    worst = max(stats, key=lambda s: abs(s[4]))
    detail = ", ".join(f"{chr(97 + slot)}={seen:.0f}/{expected:.0f}" for slot, seen, expected, _, _ in stats)
    assert abs(worst[4]) <= SIGMA, detail


@pytest.mark.parametrize("config", _declared(), ids=lambda c: c.generator)
def test_the_answer_is_not_the_longest_option_more_often_than_chance(config: PsicotecnicoConfig) -> None:
    z, detail = _report("longest-is-correct", _answered(config), _longest_is_correct)
    assert abs(z) <= SIGMA, detail


@pytest.mark.parametrize("config", _declared(), ids=lambda c: c.generator)
def test_the_answer_carries_no_systematic_length_advantage(config: PsicotecnicoConfig) -> None:
    z, detail = _report("length edge", _answered(config), _length_edge)
    assert abs(z) <= SIGMA, detail


def test_the_fifty_goldens_per_generator_are_unchanged() -> None:
    registry = load_registry(COURSE, check_excerpts=False)
    committed = json.loads(FINGERPRINTS.read_text(encoding="utf-8"))
    current = {use.generator: fingerprint(golden_items(use)) for use in registry.generator_uses()}
    moved = sorted(g for g in current if committed.get(g) != current[g])
    assert not moved, f"goldens moved for {moved}: run scripts/export_backend_goldens.py and re-review them"


# --- the rules that the distractors are meant to break --------------------------------------------


def test_a_circuit_breaker_opens_when_the_failure_rate_equals_the_threshold() -> None:
    from tradeschool.psicotecnico.backend.circuit_breaker import Breaker, run_closed

    breaker = Breaker(window=4, minimum=4, threshold=50, calls=(False, True, True, False, False))
    assert run_closed(breaker).tripped_at == 4
    assert run_closed(breaker, strict=True).tripped_at is None


def test_a_committed_kafka_offset_is_the_next_record_to_read() -> None:
    from tradeschool.psicotecnico.backend.kafka_offsets import Partition, replay

    run = Partition("lag", (("produce", 10), ("poll", 4), ("commit", 0), ("poll", 3)))
    reading = replay(run)
    assert (reading.committed, reading.end - reading.committed) == (4, 6)


def test_a_multicolumn_btree_scan_is_bounded_by_equalities_then_one_inequality() -> None:
    from tradeschool.psicotecnico.backend.composite_index import bounding

    assert bounding(("a", "b", "c"), {"a": "=", "b": ">", "c": "="}) == ["a", "b"]
    assert bounding(("a", "b", "c"), {"a": "=", "c": "="}) == ["a"]
    assert bounding(("a", "b"), {"b": "="}) == []


def test_a_sliding_window_request_exactly_one_window_old_has_left_the_window() -> None:
    from tradeschool.psicotecnico.backend.rate_limiter import Limiter, rejected_by_window

    limiter = Limiter("sliding-window", 1, 3, (0, 3))
    assert rejected_by_window(limiter) == []
    assert rejected_by_window(limiter, closed_edge=True) == [2]


NUMBER = re.compile(r"\d[\d,]*(?:\.\d+)?")
MIN_RELATIVE_SEPARATION = Fraction(1, 5)
SEPARATION_SEEDS = 3_000


def _single_numbers(options: tuple[str, ...]) -> list[Fraction] | None:
    found = [NUMBER.findall(option) for option in options]
    if any(len(numbers) != 1 for numbers in found):
        return None
    return [Fraction(numbers[0].replace(",", "")) for numbers in found]


HEDGED_IDS = [i for i in IDS if any("about" in form for form in BACKEND_GENERATORS[i].forms)]


def test_the_hedged_families_are_the_capacity_and_retry_ones() -> None:
    assert HEDGED_IDS == ["capacity-estimation", "retry-backoff-bounds"]


@pytest.mark.parametrize("generator_id", HEDGED_IDS)
def test_no_two_approximate_numeric_options_are_within_the_separation_margin(generator_id: str) -> None:
    generator = BACKEND_GENERATORS[generator_id]
    close = []
    for level in generator.levels:
        for seed in range(SEPARATION_SEEDS):
            values = _single_numbers(generator.generate(seed, Params(level)).options)
            if values is None:
                continue
            for i, a in enumerate(values):
                for b in values[i + 1 :]:
                    if abs(a - b) < MIN_RELATIVE_SEPARATION * max(abs(a), abs(b)):
                        close.append((level, seed))
    assert not close[:5], f"{len(close)} close pairs, first {close[:5]}"
