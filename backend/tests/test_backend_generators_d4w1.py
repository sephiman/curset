# SPDX-License-Identifier: AGPL-3.0-only
"""Round D4 part B, writer w1: properties, rules and golden seeds of three families."""

from __future__ import annotations

import re
from typing import cast

import pytest

from tradeschool.psicotecnico.backend.base import CitedGenerator
from tradeschool.psicotecnico.backend.keyset_next_page import (
    KeysetNextPageGenerator,
    Page,
    ids_after,
    next_page_rows,
)
from tradeschool.psicotecnico.backend.option_forms import plain_option
from tradeschool.psicotecnico.backend.snowflake_layout import SnowflakeLayoutGenerator
from tradeschool.psicotecnico.backend.xfast_probe import XFastProbeGenerator, final_l, probe_levels
from tradeschool.psicotecnico.contract import verify
from tradeschool.psicotecnico.item import Params

GENERATORS: list[CitedGenerator] = [
    KeysetNextPageGenerator(),
    SnowflakeLayoutGenerator(),
    XFastProbeGenerator(),
]
IDS = [generator.id for generator in GENERATORS]
BY_ID = {generator.id: generator for generator in GENERATORS}
SLOT_SEEDS = 600

GOLDENS: list[tuple[str, int, int, str]] = [
    ("keyset-next-page", 2, 1, "`65, 10`"),
    ("keyset-next-page", 2, 2, "`96, 33`"),
    ("snowflake-layout", 1, 1, "24,576"),
    ("snowflake-layout", 1, 2, "28,672 distinct ids per millisecond"),
    ("xfast-level-probes", 2, 1, "levels `4, 6, 5`, in order"),
    ("xfast-level-probes", 2, 2, "the levels `6, 9, 7, 8`"),
]


@pytest.mark.parametrize("generator", GENERATORS, ids=IDS)
def test_property_tests_hold_over_many_seeded_items_at_every_level(generator: CitedGenerator) -> None:
    assert verify(generator, per_level=300, base=41) == []


@pytest.mark.parametrize("generator", GENERATORS, ids=IDS)
def test_the_same_seed_builds_the_same_item(generator: CitedGenerator) -> None:
    for level in generator.levels:
        assert generator.generate(7, Params(level)) == generator.generate(7, Params(level))


@pytest.mark.parametrize("generator", GENERATORS, ids=IDS)
def test_four_distinct_options_one_key_and_a_stem_of_15_to_40_words(generator: CitedGenerator) -> None:
    for level in generator.levels:
        for seed in range(120):
            item = generator.generate(seed, Params(level))
            assert len(set(item.options)) == 4
            assert generator.solve(item) == item.key
            assert 15 <= len(item.stem.split()) <= 40, item.stem


@pytest.mark.parametrize("generator", GENERATORS, ids=IDS)
def test_every_explanation_ends_with_the_anchor_it_rests_on(generator: CitedGenerator) -> None:
    assert generator.citation.confirmed is not None
    for level in generator.levels:
        for seed in range(40):
            explanation = generator.generate(seed, Params(level)).explanation
            assert explanation.endswith(f"Source: `{generator.citation.confirmed}`."), explanation


@pytest.mark.parametrize("generator", GENERATORS, ids=IDS)
def test_the_key_is_dealt_to_every_slot_about_equally(generator: CitedGenerator) -> None:
    slots = [0, 0, 0, 0]
    for seed in range(SLOT_SEEDS):
        slots[generator.generate(seed, Params(generator.levels[seed % len(generator.levels)])).key] += 1
    assert min(slots) > SLOT_SEEDS / 4 * 0.7, slots


@pytest.mark.parametrize(("generator", "level", "seed", "keyed"), GOLDENS)
def test_golden_seeds_keep_their_keyed_option(generator: str, level: int, seed: int, keyed: str) -> None:
    item = BY_ID[generator].generate(seed, Params(level))
    assert item.options[item.key] == keyed


def test_a_row_comparison_falls_to_the_id_only_when_the_scores_are_equal() -> None:
    rows = ((50, 4), (50, 9), (70, 2), (70, 11), (90, 6))
    assert next_page_rows(rows, (70, 2)) == ((70, 11), (90, 6))
    assert next_page_rows(rows, (50, 9)) == ((70, 2), (70, 11), (90, 6))


def test_the_row_comparison_keeps_a_later_score_with_a_smaller_id() -> None:
    assert (90, 1) in next_page_rows(((50, 7), (90, 1)), (50, 7))


def test_limit_takes_the_first_rows_in_sort_order() -> None:
    rows = ((50, 4), (70, 2), (70, 11), (90, 6))
    assert ids_after(rows, (50, 4), 2) == (2, 11)


@pytest.mark.parametrize("generator", GENERATORS, ids=IDS)
def test_the_explanation_names_every_wrong_option_dealt_and_never_the_key(generator: CitedGenerator) -> None:
    for level in generator.levels:
        for seed in range(80):
            item = generator.generate(seed, Params(level))
            wrong_part = item.explanation.split("Wrong options:")[1]
            for slot, shown in enumerate(item.options):
                option = plain_option(shown, generator.forms)
                named = re.search(rf"(?<![\d,]){re.escape(option)}(?![\d,])", wrong_part) is not None
                assert named == (slot != item.key), (option, item.explanation)


def test_a_snowflake_item_multiplies_the_machines_by_the_sequence_range() -> None:
    generator = SnowflakeLayoutGenerator()
    for seed in range(40):
        item = generator.generate(seed, Params(1))
        machines = int(item.stem.split()[0])
        assert plain_option(item.options[item.key], generator.forms) == f"{machines * 4096:,}"


def test_the_probe_loop_follows_the_listing_of_the_x_fast_trie() -> None:
    assert probe_levels(11, 5) == (6, 3, 4, 5)
    assert probe_levels(7, 0) == (4, 2, 1)
    assert final_l(11, 5) == 5
    assert final_l(7, 7) == 7


def test_the_final_l_is_the_deepest_matching_level() -> None:
    for w in (7, 8, 11, 12, 15):
        for depth in range(w + 1):
            assert final_l(w, depth) == depth
            assert all(0 < i <= w for i in probe_levels(w, depth))


def test_a_probe_item_names_the_x_fast_trie_and_never_mentions_the_leaf_list() -> None:
    generator = XFastProbeGenerator()
    for level in generator.levels:
        for seed in range(60):
            item = generator.generate(seed, Params(level))
            assert "X-fast trie" in item.stem
            assert "jump" not in item.explanation and "leaf" not in item.explanation


@pytest.mark.parametrize("generator", GENERATORS, ids=IDS)
def test_no_option_is_empty_or_an_empty_code_span(generator: CitedGenerator) -> None:
    for level in generator.levels:
        for seed in range(200):
            for option in generator.generate(seed, Params(level)).options:
                assert plain_option(option, generator.forms).strip("` ") != "", (seed, option)


def test_each_wrong_keyset_option_is_what_its_named_filter_returns() -> None:
    generator = KeysetNextPageGenerator()
    for seed in range(300):
        item = generator.generate(seed, Params(2))
        page = cast(Page, item.facts["scenario"])
        for slot, option in enumerate(item.options):
            if slot == item.key:
                continue
            sentence = re.search(re.escape(option) + r" is what `WHERE (.+?)` returns", item.explanation)
            assert sentence is not None, (seed, option)
            condition = sentence.group(1).replace(" AND ", " and ")
            kept = [row for row in page.rows if eval(condition, {}, {"score": row[0], "id": row[1]})]
            assert option == "`" + ", ".join(str(r[1]) for r in kept[: page.limit]) + "`", (
                seed,
                option,
                condition,
            )


def test_no_two_keyset_options_come_from_the_same_ids() -> None:
    generator = KeysetNextPageGenerator()
    for seed in range(300):
        item = generator.generate(seed, Params(2))
        assert item.explanation.count(" is what ") == 3
