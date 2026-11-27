# SPDX-License-Identifier: AGPL-3.0-only
"""Round D4 part B, writer w2: the Raft vote-by-log family."""

from __future__ import annotations

import pytest

from tradeschool.psicotecnico.backend.qos_class import QosClassGenerator, QosScenario, qos_class
from tradeschool.psicotecnico.backend.raft_vote_log import (
    RaftVoteLogGenerator,
    VoteScenario,
    mistake_logs,
    more_up_to_date,
)
from tradeschool.psicotecnico.contract import verify
from tradeschool.psicotecnico.item import Params

GENERATOR = RaftVoteLogGenerator()
SEEDS = 300

# (level, seed, the keyed option), recomputed by hand from the rule once when written
GOLDENS = [
    (1, 1, "`[2, 4, 4, 4, 4]`"),
    (1, 2, "`[1, 1, 4, 4, 4, 4]`"),
    (2, 1, "`[2, 5, 5]`"),
    (2, 2, "`[1, 1, 5, 5]`"),
]


def test_a_later_last_term_beats_a_longer_log() -> None:
    assert more_up_to_date((1, 2, 3), (1, 1, 1, 2, 2))
    assert not more_up_to_date((1, 1, 1, 2, 2), (1, 2, 3))


def test_with_equal_last_terms_the_longer_log_is_more_up_to_date() -> None:
    assert more_up_to_date((1, 2, 2, 3), (1, 2, 3))
    assert not more_up_to_date((1, 2, 3), (1, 2, 2, 3))


def test_the_voter_denies_exactly_the_candidates_it_is_more_up_to_date_than() -> None:
    for level in GENERATOR.levels:
        for seed in range(SEEDS):
            item = GENERATOR.generate(seed, Params(level))
            scenario = item.facts["scenario"]
            assert isinstance(scenario, VoteScenario)
            denied = [i for i, o in enumerate(item.options) if more_up_to_date(scenario.voter, _parse(o))]
            assert sorted([*denied, item.key]) == [0, 1, 2, 3]
            assert not any(scenario.voter == _parse(o) for o in item.options)


def test_every_distractor_is_a_named_mistake_the_voter_denies() -> None:
    for level in GENERATOR.levels:
        for seed in range(SEEDS):
            scenario = GENERATOR.scenario_for(seed, level)
            for name, log in mistake_logs(scenario).items():
                assert more_up_to_date(scenario.voter, log), name
                assert name in {
                    "longer log, older last term",
                    "same last term, shorter",
                    "older last term, same length",
                }


def test_a_level_two_key_is_shorter_than_the_voter_log() -> None:
    for seed in range(SEEDS):
        scenario = GENERATOR.scenario_for(seed, 2)
        assert len(scenario.ahead) < len(scenario.voter)
        assert scenario.ahead[-1] > scenario.voter[-1]


def test_every_pair_of_logs_obeys_log_matching() -> None:
    for level in GENERATOR.levels:
        for seed in range(SEEDS):
            item = GENERATOR.generate(seed, Params(level))
            scenario = item.facts["scenario"]
            assert isinstance(scenario, VoteScenario)
            logs = [scenario.voter, *(_parse(o) for o in item.options)]
            for first in logs:
                for second in logs:
                    for index in range(min(len(first), len(second))):
                        if first[index] == second[index]:
                            assert first[: index + 1] == second[: index + 1], (first, second)


def test_the_explanation_refutes_each_shown_wrong_log_and_no_other() -> None:
    for level in GENERATOR.levels:
        for seed in range(SEEDS):
            item = GENERATOR.generate(seed, Params(level))
            shown = {_bare(o) for i, o in enumerate(item.options) if i != item.key}
            for log in shown:
                assert f"{log} has last term" in item.explanation
            assert item.explanation.count("Step") == 5
            scenario = item.facts["scenario"]
            assert isinstance(scenario, VoteScenario)
            unshown = [
                log
                for _, log in scenario.behind
                if f"`[{', '.join(map(str, log))}]`" not in [_bare(o) for o in item.options]
            ]
            assert unshown == []


def test_logs_are_non_decreasing_in_term() -> None:
    for level in GENERATOR.levels:
        for seed in range(SEEDS):
            for option in GENERATOR.generate(seed, Params(level)).options:
                log = _parse(option)
                assert list(log) == sorted(log)


def test_property_tests_hold_at_every_level() -> None:
    assert verify(GENERATOR, per_level=300, base=47) == []


def test_the_same_seed_builds_the_same_item() -> None:
    for level in GENERATOR.levels:
        assert GENERATOR.generate(5, Params(level)) == GENERATOR.generate(5, Params(level))


def test_four_distinct_options_one_key_and_a_stem_of_15_to_40_words() -> None:
    for level in GENERATOR.levels:
        for seed in range(120):
            item = GENERATOR.generate(seed, Params(level))
            assert len(set(item.options)) == 4
            assert GENERATOR.solve(item) == item.key
            assert 15 <= len(item.stem.split()) <= 40


def test_the_key_is_dealt_to_every_slot_about_equally() -> None:
    slots = [0, 0, 0, 0]
    for seed in range(600):
        slots[GENERATOR.generate(seed, Params(1 + seed % 2)).key] += 1
    assert min(slots) > 600 / 4 * 0.7, slots


def test_the_key_is_not_the_longest_option_more_often_than_chance() -> None:
    longest = total = 0
    for level in GENERATOR.levels:
        for seed in range(SEEDS):
            item = GENERATOR.generate(seed, Params(level))
            sizes = [len(_parse(o)) for o in item.options]
            longest += sizes[item.key] == max(sizes) and sizes.count(max(sizes)) == 1
            total += 1
    assert longest / total < 0.4


def test_every_explanation_states_each_step_and_ends_with_the_anchor() -> None:
    for level in GENERATOR.levels:
        for seed in range(60):
            text = GENERATOR.generate(seed, Params(level)).explanation
            assert all(f"Step {n}:" in text for n in (1, 2, 3)), text
            assert "Result:" in text
            assert text.endswith("Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.")


def test_the_citation_is_the_anchor_of_the_added_sentence() -> None:
    assert GENERATOR.citation.confirmed == "paper-raft-dissertation#p40; paper-raft-dissertation#p42"


@pytest.mark.parametrize(("level", "seed", "keyed"), GOLDENS)
def test_golden_seeds_keep_their_keyed_option(level: int, seed: int, keyed: str) -> None:
    item = GENERATOR.generate(seed, Params(level))
    assert _bare(item.options[item.key]) == keyed


def _bare(option: str) -> str:
    return option[option.index("`") :]


def _parse(option: str) -> tuple[int, ...]:
    return tuple(int(part) for part in _bare(option).strip("`[]").split(","))


# --- qos-class-pod -----------------------------------------------------------------------------------

QOS = QosClassGenerator()
QOS_GOLDENS = [
    (1, 1, "`cpu 500m/500m, memory 1Gi/1Gi`"),
    (1, 2, "`cpu 1000m/1000m, memory 128Mi/128Mi`"),
]
EQUAL = ("1", "1", "1Gi", "1Gi")
NOTHING = (None, None, None, None)


def test_a_pod_is_guaranteed_only_when_every_container_sets_equal_cpu_and_memory() -> None:
    assert qos_class((EQUAL, EQUAL)) == "Guaranteed"
    assert qos_class((EQUAL, ("1", "2", "1Gi", "1Gi"))) == "Burstable"
    assert qos_class(((None, None, "1Gi", "1Gi"),)) == "Burstable"


def test_a_pod_is_best_effort_only_when_no_container_sets_anything() -> None:
    assert qos_class((NOTHING, NOTHING)) == "BestEffort"
    assert qos_class((EQUAL, NOTHING)) == "Burstable"


def test_a_container_with_a_limit_and_no_request_never_appears() -> None:
    for level in QOS.levels:
        for seed in range(SEEDS):
            scenario = QOS.scenario_for(seed, level)
            for pod in (scenario.key, *(p for _, p in scenario.wrong)):
                for cpu_request, cpu_limit, memory_request, memory_limit in pod:
                    assert not (cpu_request is None and cpu_limit is not None)
                    assert not (memory_request is None and memory_limit is not None)


def test_the_key_has_the_asked_class_and_every_shown_wrong_pod_has_another() -> None:
    for level in QOS.levels:
        for seed in range(SEEDS):
            scenario = QOS.scenario_for(seed, level)
            assert qos_class(scenario.key) == scenario.asked
            assert len(scenario.wrong) == 3
            assert all(qos_class(pod) != scenario.asked and slip for slip, pod in scenario.wrong)


def test_the_qos_explanation_names_the_slip_of_each_shown_wrong_option() -> None:
    for level in QOS.levels:
        for seed in range(SEEDS):
            item = QOS.generate(seed, Params(level))
            scenario = item.facts["scenario"]
            assert isinstance(scenario, QosScenario)
            shown = {o for i, o in enumerate(item.options) if i != item.key}
            assert len(shown) == 3
            assert item.explanation.count("Step") == 4
            for slip, _ in scenario.wrong:
                assert f", because {slip}." in item.explanation


def test_qos_property_tests_hold_at_every_level() -> None:
    assert verify(QOS, per_level=300, base=59) == []


def test_qos_items_have_four_distinct_options_one_key_and_a_stem_of_15_to_40_words() -> None:
    for level in QOS.levels:
        for seed in range(120):
            item = QOS.generate(seed, Params(level))
            assert QOS.generate(seed, Params(level)) == item
            assert len(set(item.options)) == 4
            assert QOS.solve(item) == item.key
            assert 15 <= len(item.stem.split()) <= 40


def test_qos_key_is_dealt_to_every_slot_about_equally() -> None:
    slots = [0, 0, 0, 0]
    for seed in range(600):
        slots[QOS.generate(seed, Params(1)).key] += 1
    assert min(slots) > 600 / 4 * 0.7, slots


def test_qos_explanation_ends_with_its_anchors() -> None:
    assert QOS.citation.confirmed == "k8s-qos#criteria; k8s-qos#criteria-1; k8s-qos#criteria-2"
    text = QOS.generate(1, Params(1)).explanation
    assert text.endswith("Source: `k8s-qos#criteria`; `k8s-qos#criteria-1`; `k8s-qos#criteria-2`.")


@pytest.mark.parametrize(("level", "seed", "keyed"), QOS_GOLDENS)
def test_qos_golden_seeds_keep_their_keyed_option(level: int, seed: int, keyed: str) -> None:
    item = QOS.generate(seed, Params(level))
    assert item.options[item.key] == keyed
