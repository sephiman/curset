# SPDX-License-Identifier: AGPL-3.0-only
"""The psicotécnico generators: property tests, answer-bias guards, goldens and the load gate."""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import ClassVar

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
from tradeschool.psicotecnico.contract import GeneratorLoadError, ItemGenerator, verify
from tradeschool.psicotecnico.goldens import fingerprint, golden_items
from tradeschool.psicotecnico.item import Item, Params
from tradeschool.psicotecnico.registry import GENERATORS, load_generator
from tradeschool.psicotecnico.weights import apportion

COURSE = Path(__file__).resolve().parents[2] / "content" / "age-auxiliar-c2"
FINGERPRINTS = Path(__file__).resolve().parent / "goldens" / "psicotecnico-fingerprints.json"
IDS = sorted(GENERATORS)
ITEMS_PER_GENERATOR = 1_000


def test_the_first_batch_is_the_thirteen_recurring_types() -> None:
    assert len(IDS) == 13


@pytest.mark.parametrize("generator_id", IDS)
def test_property_tests_hold_over_many_seeded_items_at_every_level(generator_id: str) -> None:
    assert verify(GENERATORS[generator_id], per_level=300, base=7) == []


@pytest.mark.parametrize("generator_id", IDS)
def test_the_same_seed_builds_the_same_item(generator_id: str) -> None:
    generator = GENERATORS[generator_id]
    for level in generator.levels:
        assert generator.generate(99, Params(level)) == generator.generate(99, Params(level))


class _WrongKey(ItemGenerator):
    id: ClassVar[str] = "wrong-key"

    def build(self, seed: int, params: Params) -> Item:
        return Item(self.id, seed, 1, "¿2 + 2?", ("3", "4", "5", "6"), 0, "Dos y dos son cuatro.")

    def solve(self, item: Item) -> int:
        return 1


def test_a_generator_with_a_failing_property_test_does_not_load() -> None:
    with pytest.raises(GeneratorLoadError, match="solver says option 1"):
        load_generator("wrong-key", {"wrong-key": _WrongKey()})


def test_weights_are_split_exactly_by_largest_remainder() -> None:
    assert apportion([1, 2], 6) == [2, 4]
    assert apportion([62, 16, 14, 10, 9, 11, 9, 9, 9, 9, 9, 4, 4], 30) == [
        11,
        3,
        2,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
    ]
    for total in range(0, 40):
        assert sum(apportion([3, 1, 4, 1, 5], total)) == total


def _declared() -> list[PsicotecnicoConfig]:
    registry = load_registry(COURSE, check_excerpts=False)
    return [
        PsicotecnicoConfig(type="psicotecnico", generator=use.generator, difficulty=use.difficulty)
        for use in registry.generator_uses()
    ]


def test_age_auxiliar_declares_the_thirteen_generators_and_stays_a_draft() -> None:
    registry = load_registry(COURSE, check_excerpts=False)
    assert sorted(use.generator for use in registry.generator_uses()) == IDS
    assert not registry.published


# --- answer-bias guards over 1,000 seeded items per generator -------------------------------------


def _answered(config: PsicotecnicoConfig) -> list[Answered]:
    rng = random.Random(20261107)
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
    detail = ", ".join(
        f"{chr(97 + slot)}={observed:.0f}/{expected:.0f}" for slot, observed, expected, _, _ in stats
    )
    assert abs(worst[4]) <= SIGMA, detail


@pytest.mark.parametrize("config", _declared(), ids=lambda c: c.generator)
def test_the_answer_is_not_the_longest_option_more_often_than_chance(config: PsicotecnicoConfig) -> None:
    z, detail = _report("longest-is-correct", _answered(config), _longest_is_correct)
    assert abs(z) <= SIGMA, detail


@pytest.mark.parametrize("config", _declared(), ids=lambda c: c.generator)
def test_the_answer_carries_no_systematic_length_advantage(config: PsicotecnicoConfig) -> None:
    z, detail = _report("length edge", _answered(config), _length_edge)
    assert abs(z) <= SIGMA, detail


# --- goldens: the 50 items per generator that the blind review reads ------------------------------


def test_the_fifty_goldens_per_generator_are_unchanged() -> None:
    registry = load_registry(COURSE, check_excerpts=False)
    committed = json.loads(FINGERPRINTS.read_text(encoding="utf-8"))
    current = {use.generator: fingerprint(golden_items(use)) for use in registry.generator_uses()}
    moved = sorted(g for g in current if committed.get(g) != current[g])
    assert not moved, (
        f"goldens moved for {moved}: run scripts/export_psicotecnico_goldens.py and re-review them"
    )
