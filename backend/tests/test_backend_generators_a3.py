# SPDX-License-Identifier: AGPL-3.0-only
"""Round D3 part A, writer a3: the m08 and m10 generators, tested directly (the coordinator "
"registers them)."""

from __future__ import annotations

import re
from typing import Any

import pytest

from test_quiz_answer_bias import SIGMA, Answered, _length_edge, _longest_is_correct, _position_z, _report
from tradeschool.psicotecnico.backend.base import CitedGenerator
from tradeschool.psicotecnico.backend.error_budget import ErrorBudgetGenerator, budget_minutes
from tradeschool.psicotecnico.backend.hpa_replicas import HpaReplicasGenerator
from tradeschool.psicotecnico.backend.kafka_write_acceptance import KafkaWriteAcceptanceGenerator
from tradeschool.psicotecnico.backend.raft_commit import RaftCommitIndexGenerator
from tradeschool.psicotecnico.backend.raft_election import RaftElectionVotesGenerator
from tradeschool.psicotecnico.backend.rolling_update import RollingUpdateBoundsGenerator
from tradeschool.psicotecnico.backend.window_grace import WindowGraceGenerator
from tradeschool.psicotecnico.contract import verify
from tradeschool.psicotecnico.item import Item, Params

GENERATORS: list[CitedGenerator] = [
    KafkaWriteAcceptanceGenerator(),
    RaftElectionVotesGenerator(),
    RaftCommitIndexGenerator(),
    WindowGraceGenerator(),
    HpaReplicasGenerator(),
    RollingUpdateBoundsGenerator(),
    ErrorBudgetGenerator(),
]
SEEDS = range(200)


def _each(generator: CitedGenerator) -> list[tuple[int, int]]:
    return [(level, seed) for level in generator.levels for seed in SEEDS]


@pytest.mark.parametrize("generator", GENERATORS, ids=lambda g: g.id)
def test_property_tests_hold_over_many_seeded_items_at_every_level(generator: CitedGenerator) -> None:
    assert verify(generator, per_level=300, base=31) == []


@pytest.mark.parametrize("generator", GENERATORS, ids=lambda g: g.id)
def test_the_same_seed_builds_the_same_item(generator: CitedGenerator) -> None:
    for level, seed in _each(generator):
        assert generator.generate(seed, Params(level)) == generator.generate(seed, Params(level))


@pytest.mark.parametrize("generator", GENERATORS, ids=lambda g: g.id)
def test_four_distinct_options_and_the_key_is_the_only_one_the_solver_accepts(
    generator: CitedGenerator,
) -> None:
    for level, seed in _each(generator):
        item = generator.generate(seed, Params(level))
        assert len(set(item.options)) == 4
        assert generator.solve(item) == item.key


@pytest.mark.parametrize("generator", GENERATORS, ids=lambda g: g.id)
def test_the_stem_is_fifteen_to_forty_words(generator: CitedGenerator) -> None:
    for level, seed in _each(generator):
        words = len(generator.generate(seed, Params(level)).stem.split())
        assert 15 <= words <= 40, (level, seed, words)


@pytest.mark.parametrize("generator", GENERATORS, ids=lambda g: g.id)
def test_the_explanation_states_a_formula_numbers_every_step_and_ends_on_the_result(
    generator: CitedGenerator,
) -> None:
    for level, seed in _each(generator):
        item = generator.generate(seed, Params(level))
        steps = re.findall(r"Step (\d+):", item.explanation)
        assert steps and steps == [str(i) for i in range(1, len(steps) + 1)], item.explanation
        assert item.explanation.startswith("Rule:")
        assert "Result:" in item.explanation.split(f"Step {len(steps)}:")[1]


@pytest.mark.parametrize("generator", GENERATORS, ids=lambda g: g.id)
def test_the_learner_text_names_no_option_by_letter_and_keeps_no_placeholder(
    generator: CitedGenerator,
) -> None:
    for level, seed in _each(generator):
        item = generator.generate(seed, Params(level))
        text = f"{item.stem} {item.explanation}"
        assert "TODO" not in text
        assert not re.search(r"\b(option|answer|choice) [A-Da-d]\b", text)


@pytest.mark.parametrize("generator", GENERATORS, ids=lambda g: g.id)
def test_the_citation_is_confirmed(generator: CitedGenerator) -> None:
    assert generator.citation.confirmed is not None
    assert re.fullmatch(r"m\d\d-l\d\d", generator.citation.lesson)


def _facts(generator: CitedGenerator, level: int, seed: int) -> tuple[Item, Any]:
    item = generator.generate(seed, Params(level))
    return item, item.facts["scenario"]


def _by_id(generator_id: str) -> CitedGenerator:
    return next(g for g in GENERATORS if g.id == generator_id)


@pytest.mark.parametrize("generator", GENERATORS, ids=lambda g: g.id)
def test_the_explanation_ends_with_its_citation_as_inline_code(generator: CitedGenerator) -> None:
    assert generator.citation.confirmed is not None
    anchors = [a.strip() for a in generator.citation.confirmed.split(";")]
    expected = "Source: " + "; ".join(f"`{a}`" for a in anchors) + "."
    for level, seed in _each(generator):
        assert generator.generate(seed, Params(level)).explanation.endswith(expected)


def test_a_kafka_distractor_always_has_the_opposite_outcome_and_good_grammar() -> None:
    generator = _by_id("kafka-write-acceptance")
    for level, seed in _each(generator):
        item = generator.generate(seed, Params(level))
        text = " ".join(item.options)
        assert not re.search(r"\b1 (in-sync )?replicas\b|\b1 replica in sync are\b", f"{text} {item.stem}")
        if level == 1:
            verdicts = {option.split(":")[0] for option in item.options}
            assert len(verdicts) == 2
            assert [o.split(":")[0] for i, o in enumerate(item.options) if i != item.key] == [
                [o.split(":")[0] for o in item.options][(item.key + 1) % 4]
            ] * 3


def test_every_raft_candidate_holds_its_own_vote() -> None:
    generator = _by_id("raft-election-votes")
    for seed in SEEDS:
        _, scenario = _facts(generator, 1, seed)
        assert min(scenario.votes) >= 1


def test_a_window_option_never_contradicts_the_stream_time_of_the_stem() -> None:
    generator = _by_id("stream-window-grace")
    for seed in SEEDS:
        item, scenario = _facts(generator, 2, seed)
        for option in item.options:
            found = re.fullmatch(r"(Accepted|Rejected): the .* window closes at (\d\d):(\d\d)", option)
            assert found, option
            closes = int(found[2]) * 60 + int(found[3])
            assert (found[1] == "Accepted") == (scenario.stream_time < closes), (option, item.stem)


def test_the_autoscaler_scales_up_so_the_stabilization_window_cannot_keep_the_old_count() -> None:
    generator = _by_id("hpa-desired-replicas")
    for level, seed in _each(generator):
        _, scenario = _facts(generator, level, seed)
        assert scenario.current > scenario.target


def test_a_rollout_question_uses_one_option_shape_and_correct_plurals() -> None:
    generator = _by_id("rolling-update-bounds")
    for level, seed in _each(generator):
        item = generator.generate(seed, Params(level))
        assert all(re.fullmatch(r"\d+ Pods", option) for option in item.options), item.options
        assert not any(option.startswith("1 Pods") for option in item.options)


def test_the_raft_question_names_the_candidate_and_never_prints_one_more_votes() -> None:
    generator = _by_id("raft-election-votes")
    for level, seed in _each(generator):
        item = generator.generate(seed, Params(level))
        assert "leading" not in item.stem
        assert "1 more votes" not in item.explanation
        assert re.search(r"does candidate [ABC] need", item.stem)


def test_the_autoscaler_has_no_tolerance_case() -> None:
    generator = _by_id("hpa-desired-replicas")
    for level, seed in _each(generator):
        item = generator.generate(seed, Params(level))
        assert "tolerance" not in item.stem
        assert not re.search(r"\b1 replicas", item.explanation)


def test_a_rollout_explanation_never_prints_1_pods() -> None:
    generator = _by_id("rolling-update-bounds")
    for level, seed in _each(generator):
        assert not re.search(r"\b1 Pods\b", generator.generate(seed, Params(level)).explanation)


def test_the_error_budget_is_a_whole_number_of_minutes() -> None:
    generator = _by_id("error-budget-minutes")
    for level, seed in _each(generator):
        _, scenario = _facts(generator, level, seed)
        assert budget_minutes(scenario).denominator == 1


def test_the_error_budget_rule_is_attributed_to_the_workbook() -> None:
    item = _by_id("error-budget-minutes").generate(5, Params(1))
    assert "Site Reliability Workbook" in item.explanation


def _answered(generator: CitedGenerator, count: int = 1_000) -> list[Answered]:
    rows: list[Answered] = []
    for level in generator.levels:
        for seed in range(count):
            item = generator.generate(seed * 7919 + level, Params(level))
            lengths = tuple(len(option) for option in item.options)
            rows.append(Answered(generator.id, f"{level}:{seed}", lengths, frozenset({item.key})))
    return rows


@pytest.mark.parametrize("generator", GENERATORS, ids=lambda g: g.id)
def test_the_key_is_dealt_to_every_slot_equally(generator: CitedGenerator) -> None:
    worst = max(_position_z(_answered(generator)), key=lambda s: abs(s[4]))
    assert abs(worst[4]) <= SIGMA


@pytest.mark.parametrize("generator", GENERATORS, ids=lambda g: g.id)
def test_the_key_carries_no_systematic_length_advantage(generator: CitedGenerator) -> None:
    for name, stat in (("length edge", _length_edge), ("longest-is-correct", _longest_is_correct)):
        z, detail = _report(name, _answered(generator), stat)
        assert abs(z) <= SIGMA, detail


# (generator id, level, seed, the key as the learner reads it)
GOLDEN_KEYS: list[tuple[str, int, int, str]] = [
    ("kafka-write-acceptance", 1, 11, "The write is accepted without `NotEnough"),
    ("kafka-write-acceptance", 1, 2026, "The write is rejected with `NotEnoughRep"),
    ("kafka-write-acceptance", 2, 11, "1"),
    ("kafka-write-acceptance", 2, 2026, "1"),
    ("raft-election-votes", 1, 11, "2"),
    ("raft-election-votes", 1, 2026, "3"),
    ("raft-commit-index", 1, 11, "8"),
    ("raft-commit-index", 1, 2026, "4"),
    ("raft-commit-index", 2, 11, "8"),
    ("raft-commit-index", 2, 2026, "7"),
    ("stream-window-grace", 1, 11, "15:00 to 15:30"),
    ("stream-window-grace", 1, 2026, "10:40 to 10:45"),
    ("stream-window-grace", 2, 11, "Rejected: the 14:30 to 15:00 window clos"),
    ("stream-window-grace", 2, 2026, "Rejected: the 10:40 to 10:45 window clos"),
    ("hpa-desired-replicas", 1, 11, "9"),
    ("hpa-desired-replicas", 1, 2026, "4"),
    ("rolling-update-bounds", 1, 11, "15 Pods"),
    ("rolling-update-bounds", 1, 2026, "17 Pods"),
    ("rolling-update-bounds", 2, 11, "32 Pods"),
    ("rolling-update-bounds", 2, 2026, "26 Pods"),
    ("error-budget-minutes", 1, 11, "108 minutes"),
    ("error-budget-minutes", 1, 2026, "about 432 minutes"),
    ("error-budget-minutes", 2, 11, "648 minutes"),
    ("error-budget-minutes", 2, 2026, "about 1,296 minutes"),
]


@pytest.mark.parametrize(("generator_id", "level", "seed", "key"), GOLDEN_KEYS)
def test_golden_seeds_keep_their_key(generator_id: str, level: int, seed: int, key: str) -> None:
    generator = next(g for g in GENERATORS if g.id == generator_id)
    item = generator.generate(seed, Params(level))
    assert item.options[item.key].startswith(key)
