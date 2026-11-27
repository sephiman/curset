# SPDX-License-Identifier: AGPL-3.0-only
"""Round D3 part A, writer a2: the m05, m06 and m07 runtime generators."""

from __future__ import annotations

import re
from typing import cast

import pytest

from tradeschool.psicotecnico.backend.base import CitedGenerator
from tradeschool.psicotecnico.backend.http_freshness import HttpFreshnessGenerator
from tradeschool.psicotecnico.backend.http_method_properties import HttpMethodPropertiesGenerator
from tradeschool.psicotecnico.backend.property_source import PropertySourceGenerator
from tradeschool.psicotecnico.backend.proxy_annotation import ProxyAnnotationGenerator
from tradeschool.psicotecnico.backend.row_lock_conflict import RowLockConflictGenerator
from tradeschool.psicotecnico.contract import verify
from tradeschool.psicotecnico.item import Item, Params

GENERATORS: list[CitedGenerator] = [
    PropertySourceGenerator(),
    ProxyAnnotationGenerator(),
    RowLockConflictGenerator(),
    HttpFreshnessGenerator(),
    HttpMethodPropertiesGenerator(),
]
SEEDS = range(200)


def _ids() -> list[str]:
    return [generator.id for generator in GENERATORS]


@pytest.mark.parametrize("generator", GENERATORS, ids=_ids())
def test_property_tests_hold_over_many_seeded_items_at_every_level(generator: CitedGenerator) -> None:
    assert verify(generator, per_level=300, base=17) == []


@pytest.mark.parametrize("generator", GENERATORS, ids=_ids())
def test_the_same_seed_builds_the_same_item(generator: CitedGenerator) -> None:
    for level in generator.levels:
        assert generator.generate(7, Params(level)) == generator.generate(7, Params(level))


@pytest.mark.parametrize("generator", GENERATORS, ids=_ids())
def test_four_distinct_options_and_the_key_is_none_of_the_distractors(generator: CitedGenerator) -> None:
    for level in generator.levels:
        for seed in SEEDS:
            item = generator.generate(seed, Params(level))
            assert len(set(item.options)) == 4
            assert [i for i, _ in enumerate(item.options) if generator.solve(item) == i] == [item.key]


@pytest.mark.parametrize("generator", GENERATORS, ids=_ids())
def test_the_stem_has_fifteen_to_forty_words_as_the_linter_counts_them(generator: CitedGenerator) -> None:
    for level in generator.levels:
        for seed in SEEDS:
            stem = generator.generate(seed, Params(level)).stem
            assert 15 <= len(stem.split()) <= 40, (level, seed, stem)


@pytest.mark.parametrize("generator", GENERATORS, ids=_ids())
def test_the_explanation_gives_inputs_the_rule_numbered_steps_and_the_result(
    generator: CitedGenerator,
) -> None:
    for level in generator.levels:
        for seed in SEEDS:
            text = generator.generate(seed, Params(level)).explanation
            for label in ("Inputs:", "Rule:", "Step 1:", "Step 2:", "Result:"):
                assert label in text, (level, seed, label)


@pytest.mark.parametrize("generator", GENERATORS, ids=_ids())
def test_the_citation_names_a_lesson_and_anchors(generator: CitedGenerator) -> None:
    assert re.fullmatch(r"m0[567]-l\d\d", generator.citation.lesson)
    assert generator.citation.confirmed
    assert all("#" in ref for ref in generator.citation.confirmed.split("; "))


GOLDEN_KEYS = [
    ("property-source-winner", 1, 11, "`5`"),
    ("property-source-winner", 2, 12, "`25`"),
    (
        "proxy-annotation-applies",
        1,
        11,
        "No: a call on `this` bypasses the proxy, so the interceptor chain does not run it",
    ),
    (
        "proxy-annotation-applies",
        2,
        12,
        "Yes: AspectJ weaving puts the advice in the bytecode, so no proxy is left to skip",
    ),
    ("row-lock-conflicts", 1, 11, "plain `SELECT`"),
    ("row-lock-conflicts", 2, 12, "`SELECT ... FOR SHARE`"),
    ("http-response-freshness", 1, 11, "135 seconds"),
    ("http-response-freshness", 2, 12, "255 seconds"),
    ("http-method-properties", 1, 11, "`TRACE /items/12`"),
    ("http-method-properties", 2, 12, "`POST /books/405`"),
]


@pytest.mark.parametrize(("generator_id", "level", "seed", "key"), GOLDEN_KEYS)
def test_the_golden_seeds_keep_their_reviewed_key(generator_id: str, level: int, seed: int, key: str) -> None:
    generator = next(g for g in GENERATORS if g.id == generator_id)
    item = generator.generate(seed, Params(level))
    assert item.options[item.key] == key


# --- the rules that the distractors are meant to break ----------------------------------------------


def test_the_highest_property_source_wins_and_a_properties_file_beats_yaml_in_the_same_place() -> None:
    from tradeschool.psicotecnico.backend.property_source import Definitions, winner

    assert winner(Definitions((("env", 1), ("sysprop", 2), ("cli", 3)))) == 3
    assert winner(Definitions((("env", 1), ("sysprop", 2)))) == 2
    assert winner(Definitions((("yaml-jar", 1), ("props-jar", 2)))) == 2
    assert winner(Definitions((("props-outside", 1), ("profile-jar", 2)))) == 1


def test_only_calls_through_the_proxy_and_overridable_methods_are_advised() -> None:
    from tradeschool.psicotecnico.backend.proxy_annotation import APPLIES

    assert [shape for shape, applies in APPLIES.items() if not applies] == [
        "self-invocation",
        "final",
        "private",
    ]


def test_a_shared_row_lock_lets_shared_locks_and_plain_reads_through_but_not_writers() -> None:
    from tradeschool.psicotecnico.backend.row_lock_conflict import waits

    assert [waits("FOR SHARE", s) for s in ("FOR SHARE", "FOR KEY SHARE", "plain")] == [False, False, False]
    assert [waits("FOR SHARE", s) for s in ("FOR UPDATE", "FOR NO KEY UPDATE", "UPDATE", "DELETE")] == [
        True
    ] * 4
    assert waits("FOR UPDATE", "FOR KEY SHARE") and not waits("FOR UPDATE", "plain")


def test_a_shared_cache_takes_the_lifetime_from_s_maxage_when_it_is_present() -> None:
    from tradeschool.psicotecnico.backend.http_freshness import Cached, lifetime

    assert lifetime(Cached("until-stale", 600, 120, 30)) == 120
    assert lifetime(Cached("until-stale", 600, None, 30)) == 600


def test_post_is_neither_safe_nor_idempotent_and_put_is_idempotent_but_not_safe() -> None:
    from tradeschool.psicotecnico.backend.http_method_properties import is_idempotent, is_safe

    assert (is_safe("POST"), is_idempotent("POST")) == (False, False)
    assert (is_safe("PUT"), is_idempotent("PUT")) == (False, True)
    assert (is_safe("TRACE"), is_idempotent("TRACE")) == (True, True)


# --- blind-check fixes ------------------------------------------------------------------------------


def _items(generator: CitedGenerator, count: int = 150) -> list[tuple[int, Item]]:
    return [
        (level, generator.generate(seed, Params(level)))
        for level in generator.levels
        for seed in range(count)
    ]


@pytest.mark.parametrize("generator", GENERATORS, ids=_ids())
def test_the_explanation_ends_with_its_citation_as_inline_code(generator: CitedGenerator) -> None:
    assert generator.citation.confirmed
    refs = "; ".join(f"`{ref}`" for ref in generator.citation.confirmed.split("; "))
    for _, item in _items(generator, 40):
        assert item.explanation.endswith(f"Source: {refs}."), item.explanation


def test_every_wrong_property_option_is_the_value_of_a_named_misreading_and_the_stem_names_boot_4() -> None:
    from tradeschool.psicotecnico.backend.property_source import MISREADINGS, Definitions, winner

    generator = PropertySourceGenerator()
    for _, item in _items(generator):
        scenario = cast(Definitions, item.facts["scenario"])
        named = {f"`{winner(scenario, order)}`" for order in MISREADINGS.values()}
        wrong = {o for i, o in enumerate(item.options) if i != item.key}
        assert wrong <= named
        assert "Spring Boot 4" in item.stem


def test_a_for_update_item_never_offers_a_write_as_the_statement_that_does_not_wait() -> None:
    generator = RowLockConflictGenerator()
    for _, item in _items(generator):
        if "`SELECT ... FOR UPDATE` on one row" in item.stem:
            assert not {"`UPDATE`", "`DELETE`"} & set(item.options)


def test_the_method_explanation_names_methods_as_code_and_the_keys_vary() -> None:
    generator = HttpMethodPropertiesGenerator()
    keys = set()
    for _, item in _items(generator):
        assert not re.search(
            r"(?<!`)\b(GET|HEAD|OPTIONS|TRACE|PUT|DELETE|POST)\b(?!`)",
            item.explanation.split("Source:")[0].replace("RFC 9110", ""),
        )
        keys.add(item.options[item.key].split()[0])
    assert len(keys) >= 6


def test_the_proxy_stem_names_spring_framework_7_for_the_package_visible_shape() -> None:
    generator = ProxyAnnotationGenerator()
    for _, item in _items(generator):
        if "package-visible" in item.stem:
            assert "Spring Framework 7" in item.stem


def test_every_wrong_proxy_option_is_a_misreading_that_applies_to_that_stems_call_shape() -> None:
    from tradeschool.psicotecnico.backend.proxy_annotation import MISREADINGS, CallShape, _verdict

    generator = ProxyAnnotationGenerator()
    for _, item in _items(generator):
        shape = cast(CallShape, item.facts["scenario"]).shape
        named = {_verdict(applies, reason) for applies, reason in MISREADINGS[shape]}
        wrong = {o for i, o in enumerate(item.options) if i != item.key}
        assert wrong == named, shape
        if shape not in ("final", "private"):
            assert not any("`final`" in o or "`private`" in o for o in wrong)
        if shape == "final":
            assert not any("injected proxy" in o for o in wrong)
