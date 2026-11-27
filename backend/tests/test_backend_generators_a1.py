# SPDX-License-Identifier: AGPL-3.0-only
"""Round D3 part A, writer a1: properties, rule checks and golden seeds of the six new families."""

from __future__ import annotations

import re

import pytest

from tradeschool.psicotecnico.backend.base import CitedGenerator
from tradeschool.psicotecnico.backend.graph_traversal import GraphTraversalGenerator, bfs_order, dfs_order
from tradeschool.psicotecnico.backend.hashmap_resize import HashMapResizeGenerator, buckets_after
from tradeschool.psicotecnico.backend.partition_owner import PartitionOwnerGenerator, range_owner
from tradeschool.psicotecnico.backend.thread_pool_state import ThreadPoolStateGenerator, pool_state
from tradeschool.psicotecnico.backend.topological_order import TopologicalOrderGenerator, is_topological
from tradeschool.psicotecnico.backend.union_find_sets import UnionFindGenerator, merge_all
from tradeschool.psicotecnico.contract import verify
from tradeschool.psicotecnico.item import Params

GENERATORS: list[CitedGenerator] = [
    GraphTraversalGenerator(),
    TopologicalOrderGenerator(),
    UnionFindGenerator(),
    HashMapResizeGenerator(),
    ThreadPoolStateGenerator(),
    PartitionOwnerGenerator(),
]
IDS = [generator.id for generator in GENERATORS]
BY_ID = {generator.id: generator for generator in GENERATORS}
SLOT_SEEDS = 600

# (generator, level, seed, the keyed option), each recomputed by hand from the rule once when written
GOLDENS = [
    ("graph-traversal-order", 1, 1, "`0, 2, 5, 3, 4`"),
    ("graph-traversal-order", 1, 2, "`0, 3, 4, 5, 1`"),
    ("graph-traversal-order", 2, 1, "`0, 3, 4, 1, 5`"),
    ("graph-traversal-order", 2, 2, "`0, 1, 2, 6, 3, 4`"),
    ("topological-order-valid", 1, 1, "`4, 3, 1, 0, 2`"),
    ("topological-order-valid", 1, 2, "`1, 0, 4, 3, 2`"),
    ("topological-order-valid", 2, 1, "`1, 4, 5, 0, 3, 2`"),
    ("topological-order-valid", 2, 2, "`4, 0, 5, 1, 3, 2`"),
    ("union-find-sets", 1, 1, "3"),
    ("union-find-sets", 1, 2, "3"),
    ("union-find-sets", 2, 1, "6"),
    ("union-find-sets", 2, 2, "5"),
    ("hashmap-resize-point", 1, 1, "9"),
    ("hashmap-resize-point", 1, 2, "insert number 5"),
    ("hashmap-resize-point", 2, 1, "54"),
    ("hashmap-resize-point", 2, 2, "bucket number 52"),
    ("thread-pool-state", 1, 1, "threads 4, queued 2, rejected 0"),
    ("thread-pool-state", 1, 2, "threads 2, queued 2, rejected 2"),
    ("thread-pool-state", 2, 1, "6"),
    ("thread-pool-state", 2, 2, "call number 5"),
    ("partition-owner", 1, 1, "`p2`"),
    ("partition-owner", 1, 2, "`p2`"),
    ("partition-owner", 2, 1, "`p0`"),
    ("partition-owner", 2, 2, "`p2`"),
]


@pytest.mark.parametrize("generator", GENERATORS, ids=IDS)
def test_property_tests_hold_over_many_seeded_items_at_every_level(generator: CitedGenerator) -> None:
    assert verify(generator, per_level=300, base=31) == []


@pytest.mark.parametrize("generator", GENERATORS, ids=IDS)
def test_the_same_seed_builds_the_same_item(generator: CitedGenerator) -> None:
    for level in generator.levels:
        assert generator.generate(7, Params(level)) == generator.generate(7, Params(level))


@pytest.mark.parametrize("generator", GENERATORS, ids=IDS)
def test_four_distinct_options_and_exactly_one_key(generator: CitedGenerator) -> None:
    for level in generator.levels:
        for seed in range(120):
            item = generator.generate(seed, Params(level))
            assert len(set(item.options)) == 4
            assert generator.solve(item) == item.key
            assert 15 <= len(item.stem.split()) <= 40


@pytest.mark.parametrize("generator", GENERATORS, ids=IDS)
def test_the_citation_is_a_source_anchor_of_its_lesson(generator: CitedGenerator) -> None:
    assert generator.citation.confirmed is not None
    assert "#" in generator.citation.confirmed


def test_bfs_takes_neighbours_in_listed_order_through_a_queue() -> None:
    adjacency = ((1, 2), (0, 3), (0, 3), (1, 2, 4), (3,), (6,), (5,))
    assert bfs_order(adjacency, 0) == [0, 1, 2, 3, 4]
    assert dfs_order(adjacency, 0) == [0, 1, 3, 2, 4]


def test_a_topological_ordering_puts_every_edge_tail_before_its_head() -> None:
    edges = ((0, 1), (0, 2), (1, 3), (2, 3), (3, 4))
    assert is_topological(edges, (0, 2, 1, 3, 4))
    assert not is_topological(edges, (0, 3, 1, 2, 4))


def test_a_redundant_union_does_not_lower_the_set_count() -> None:
    assert len(merge_all(6, ((0, 1), (1, 2), (0, 2), (4, 5)))) == 3


def test_a_table_doubles_only_once_entries_exceed_the_load_factor_times_capacity() -> None:
    assert buckets_after(16, 3, 4, 12) == 16
    assert buckets_after(16, 3, 4, 13) == 32


def test_a_pool_queues_before_it_grows_beyond_the_core_size() -> None:
    assert pool_state(2, 4, 3, 10) == (4, 3, 3)
    assert pool_state(2, 4, 3, 4) == (2, 2, 0)


def test_a_range_upper_bound_is_exclusive() -> None:
    assert range_owner((0, 10, 20, 30), 10) == 1
    assert range_owner((0, 10, 20, 30), 9) == 0


@pytest.mark.parametrize(("generator", "level", "seed", "keyed"), GOLDENS)
def test_golden_seeds_keep_their_keyed_option(generator: str, level: int, seed: int, keyed: str) -> None:
    item = BY_ID[generator].generate(seed, Params(level))
    assert item.options[item.key] == keyed


@pytest.mark.parametrize("generator", GENERATORS, ids=IDS)
def test_the_key_is_dealt_to_every_slot_about_equally(generator: CitedGenerator) -> None:
    slots = [0, 0, 0, 0]
    for seed in range(SLOT_SEEDS):
        slots[generator.generate(seed, Params(generator.levels[seed % len(generator.levels)])).key] += 1
    assert min(slots) > SLOT_SEEDS / 4 * 0.7, slots


@pytest.mark.parametrize("generator", GENERATORS, ids=IDS)
def test_every_explanation_ends_with_the_anchor_it_rests_on(generator: CitedGenerator) -> None:
    anchors = [ref.strip() for ref in (generator.citation.confirmed or "").split(";")]
    for level in generator.levels:
        for seed in range(40):
            explanation = generator.generate(seed, Params(level)).explanation
            assert any(explanation.endswith(f"Source: `{anchor}`.") for anchor in anchors), explanation


def test_a_traversal_item_cites_the_anchor_of_its_own_traversal() -> None:
    generator = GraphTraversalGenerator()
    for seed in range(60):
        item = generator.generate(seed, Params(1))
        walk = "SECTION001531" if "queue-based" in item.stem else "SECTION001532"
        assert item.explanation.endswith(f"#{walk}000000000000000`.")


def test_a_pool_explanation_counts_only_the_threads_that_start() -> None:
    from tradeschool.psicotecnico.backend.thread_pool_state import Pool

    text = ThreadPoolStateGenerator().explanation(Pool("state", 1, 4, 5, 7))
    assert "Extra threads started: 1" in text
    assert "up to 4" not in text and "1 threads" not in text and "to 1." not in text


def test_every_pool_mistake_keeps_its_totals_within_the_calls() -> None:
    generator = ThreadPoolStateGenerator()
    for seed in range(200):
        item = generator.generate(seed, Params(1))
        calls = int(item.stem.split(" After ")[1].split(" calls")[0])
        for option in item.options:
            assert sum(int(part.split()[-1]) for part in option.split(", ")) == calls, option


def test_a_first_resize_distractor_is_a_named_mistake() -> None:
    from tradeschool.psicotecnico.backend.hashmap_resize import Table

    wrong = HashMapResizeGenerator().mistakes(Table("first-resize", 16, 3, 4, 0, 40))
    assert [int(w.split()[-1]) for w in wrong] == [12, 16, 17, 25, 9]


def test_no_explanation_prints_a_python_list_or_a_semicolon_before_a_capital() -> None:
    for generator in (GraphTraversalGenerator(), HashMapResizeGenerator(), ThreadPoolStateGenerator()):
        for level in generator.levels:
            for seed in range(150):
                text = generator.generate(seed, Params(level)).explanation
                assert "[" not in text and "];" not in text, text
                assert not re.search(r"; [A-Z]", text), text
                assert not re.search(r"\b(first|next) 1 calls?\b", text), text


def test_a_breadth_first_step_lists_new_neighbours_in_words() -> None:
    from tradeschool.psicotecnico.backend.graph_traversal import Traversal

    text = GraphTraversalGenerator().explanation(Traversal("bfs", ((0, 1), (0, 2), (0, 3)), 4))
    assert "then add 1, 2 and 3" in text


def test_a_depth_first_distractor_is_the_postorder() -> None:
    from tradeschool.psicotecnico.backend.graph_traversal import Traversal

    wrong = GraphTraversalGenerator().mistakes(Traversal("dfs", ((0, 1), (0, 2), (1, 3), (2, 3)), 4))
    assert "`2, 3, 1, 0`" in wrong
    assert "`0, 1, 2, 3`" in wrong


def test_a_first_rejection_distractor_counts_the_core_threads_again() -> None:
    from tradeschool.psicotecnico.backend.thread_pool_state import Pool

    wrong = ThreadPoolStateGenerator().mistakes(Pool("first-rejection", 2, 4, 3, 0))
    assert [int(w.split()[-1]) for w in wrong][-1] == 2 + 4 + 3 + 1
