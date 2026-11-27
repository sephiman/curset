# SPDX-License-Identifier: AGPL-3.0-only
"""Round D4 part C, writer c2: the m05-l04 and m07-l04 generators, checked against hand-written tables."""

from __future__ import annotations

import re

import pytest

from tradeschool.psicotecnico.backend.base import CitedGenerator
from tradeschool.psicotecnico.backend.conditional_request_outcome import ConditionalRequestOutcomeGenerator
from tradeschool.psicotecnico.contract import verify
from tradeschool.psicotecnico.item import Item, Params

CONDITIONAL = ConditionalRequestOutcomeGenerator()
GENERATORS: list[CitedGenerator] = [CONDITIONAL]
SEEDS = range(200)
LEVELS = (1, 2)


def _items(generator: CitedGenerator, count: int = 200) -> list[tuple[int, int, Item]]:
    return [
        (level, seed, generator.generate(seed, Params(level))) for level in LEVELS for seed in range(count)
    ]


def _ids() -> list[str]:
    return [g.id for g in GENERATORS]


@pytest.mark.parametrize("generator", GENERATORS, ids=_ids())
def test_property_tests_hold_over_many_seeded_items_at_every_level(generator: CitedGenerator) -> None:
    assert verify(generator, per_level=300, base=17) == []


@pytest.mark.parametrize("generator", GENERATORS, ids=_ids())
def test_the_same_seed_builds_the_same_item(generator: CitedGenerator) -> None:
    for level in generator.levels:
        assert generator.generate(7, Params(level)) == generator.generate(7, Params(level))


@pytest.mark.parametrize("generator", GENERATORS, ids=_ids())
def test_four_distinct_options_and_the_key_is_none_of_the_distractors(generator: CitedGenerator) -> None:
    for _, _, item in _items(generator):
        assert len(set(item.options)) == 4
        assert generator.solve(item) == item.key


@pytest.mark.parametrize("generator", GENERATORS, ids=_ids())
def test_the_stem_has_fifteen_to_forty_words_as_the_linter_counts_them(generator: CitedGenerator) -> None:
    for level, seed, item in _items(generator):
        assert 15 <= len(item.stem.split()) <= 40, (level, seed, item.stem)


@pytest.mark.parametrize("generator", GENERATORS, ids=_ids())
def test_the_explanation_gives_inputs_the_rule_numbered_steps_and_the_result(
    generator: CitedGenerator,
) -> None:
    for level, seed, item in _items(generator, 60):
        for label in ("Inputs:", "Rule:", "Step 1:", "Step 2:", "Result:"):
            assert label in item.explanation, (level, seed, label)


@pytest.mark.parametrize("generator", GENERATORS, ids=_ids())
def test_the_explanation_ends_with_its_citation_as_inline_code(generator: CitedGenerator) -> None:
    assert generator.citation.confirmed
    refs = "; ".join(f"`{ref}`" for ref in generator.citation.confirmed.split("; "))
    for _, _, item in _items(generator, 40):
        assert item.explanation.endswith(f"Source: {refs}."), item.explanation


def _conditional_facts(stem: str) -> tuple[str, bool]:
    method = re.search(r"sends `(GET|HEAD|PUT|DELETE) ", stem)
    assert method
    return method[1], "If-None-Match: *" in stem


def test_the_conditional_key_is_304_for_get_and_head_and_412_otherwise_and_never_performs_the_method() -> (
    None
):
    for level, seed, item in _items(CONDITIONAL):
        method, _ = _conditional_facts(item.stem)
        status = "304 Not Modified" if method in ("GET", "HEAD") else "412 Precondition Failed"
        assert item.options[item.key].endswith(f" answers `{status}` and does not perform the method"), (
            level,
            seed,
        )


def test_each_conditional_wrong_option_is_one_named_mistake_and_the_explanation_names_all_three() -> None:
    for _, _, item in _items(CONDITIONAL):
        method, _ = _conditional_facts(item.stem)
        assert item.explanation.count(" comes from ") == 3 and "In fact" not in item.explanation
        compound = [o for o in item.options if "does not perform" in o and "then" in o]
        assert not compound
        assert (method in ("GET", "HEAD")) == (
            "to a `GET`" in item.explanation or "to a `HEAD`" in item.explanation
        )


def test_step_1_names_a_current_representation_for_star_and_a_listed_tag_otherwise() -> None:
    for _, _, item in _items(CONDITIONAL):
        step_1 = item.explanation.split("Step 1: ")[1].split(" Step 2:")[0]
        _, star = _conditional_facts(item.stem)
        assert ("current representation" in step_1) == star
        assert ("listed tag" in step_1) == (not star)


def test_both_levels_are_covered_and_level_two_draws_every_method_and_the_star_form() -> None:
    drawn = {
        level: {_conditional_facts(item.stem) for lvl, _, item in _items(CONDITIONAL) if lvl == level}
        for level in LEVELS
    }
    assert {m for m, _ in drawn[1]} == {"GET", "PUT"}
    assert {s for _, s in drawn[1]} == {False}
    assert {m for m, _ in drawn[2]} == {"GET", "HEAD", "PUT", "DELETE"}
    assert {s for _, s in drawn[2]} == {True, False}


GOLDEN_KEYS = [
    ("conditional-request-outcome", 1, 11, "It answers `304 Not Modified` and does not perform the method"),
    (
        "conditional-request-outcome",
        2,
        12,
        "It answers `412 Precondition Failed` and does not perform the method",
    ),
]


@pytest.mark.parametrize(("generator_id", "level", "seed", "key"), GOLDEN_KEYS)
def test_the_golden_seeds_keep_their_reviewed_key(generator_id: str, level: int, seed: int, key: str) -> None:
    generator = next(g for g in GENERATORS if g.id == generator_id)
    item = generator.generate(seed, Params(level))
    assert re.sub(r"^(It|The server|The origin server) ", "", item.options[item.key]) == key.removeprefix(
        "It "
    )
