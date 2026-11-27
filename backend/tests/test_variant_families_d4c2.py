# SPDX-License-Identifier: AGPL-3.0-only
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

import pytest
import yaml

COURSE = Path(__file__).resolve().parents[2] / "content" / "backend-in-depth"
FAMILIES = {
    "kotlin-sequence-order": "m04-l02-ex-sequence-order",
    "kotlin-sealed-when": "m04-l02-ex-sealed-when",
}


def _variants(family: str) -> list[dict[str, Any]]:
    path = COURSE / "exercises" / f"{FAMILIES[family]}.yaml"
    loaded: dict[str, list[dict[str, Any]]] = yaml.safe_load(path.read_text(encoding="utf-8"))
    return loaded["variants"]


def _runs(family: str) -> list[dict[str, Any]]:
    runs: list[dict[str, Any]] = json.loads(
        (COURSE / "variants" / f"{family}.runs.json").read_text(encoding="utf-8")
    )
    return runs


def _stdout_of(option_text: str) -> str:
    lines = re.findall(r"`(.*?)`(?:, |$)", option_text)
    return "".join(f"{line}\n" for line in lines)


@pytest.mark.parametrize("family", FAMILIES)
def test_keeps_thirty_to_forty_variants(family: str) -> None:
    assert 30 <= len(_runs(family)) <= 40


@pytest.mark.parametrize("family", FAMILIES)
def test_each_variant_has_four_distinct_options_and_one_key(family: str) -> None:
    for variant in _variants(family):
        texts = [option["text"]["en"] for option in variant["options"]]
        assert len(set(texts)) == 4
        assert sum(1 for option in variant["options"] if option.get("correct")) == 1


@pytest.mark.parametrize("family", FAMILIES)
def test_key_text_matches_recorded_stdout(family: str) -> None:
    runs = {run["id"]: run for run in _runs(family)}
    for variant in _variants(family):
        key = next(o for o in variant["options"] if o.get("correct"))["text"]["en"]
        recorded = runs[variant["id"]]["stdout_sha256"]
        assert hashlib.sha256(_stdout_of(key).encode("utf-8")).hexdigest() == recorded


@pytest.mark.parametrize("family", FAMILIES)
def test_ids_are_unique_and_family_is_set(family: str) -> None:
    variants = _variants(family)
    assert len({v["id"] for v in variants}) == len(variants)
    assert {v["family"] for v in variants} == {family}


@pytest.mark.parametrize("family", FAMILIES)
def test_no_placeholder_is_left_in_any_text(family: str) -> None:
    for variant in _variants(family):
        assert "@@" not in variant["explanation"]["en"]
        assert "@@" not in variant["prompt"]["en"]


@pytest.mark.parametrize("family", FAMILIES)
def test_every_variant_cites_an_anchor(family: str) -> None:
    for variant in _variants(family):
        assert re.fullmatch(r"[\w-]+#[^;]+(; [\w-]+#[^;]+)*", variant["citation"])


@pytest.mark.parametrize("family", FAMILIES)
def test_the_stem_has_fifteen_to_forty_words_outside_the_code(family: str) -> None:
    for variant in _variants(family):
        stem = variant["prompt"]["en"].split("\n")[0]
        assert 15 <= len(stem.split()) <= 40, stem


def test_a_sequence_variant_cites_the_sequence_anchor_and_a_list_variant_the_iterable_one() -> None:
    for variant in _variants("kotlin-sequence-order"):
        prompt = variant["prompt"]["en"]
        expected = (
            "kotlin-docs-sequences#sequence"
            if ".asSequence()" in prompt
            else "kotlin-docs-sequences#iterable"
        )
        assert variant["citation"] == expected


def test_the_explanation_of_a_sequence_variant_never_says_the_list_runs_filter_first() -> None:
    for variant in _variants("kotlin-sequence-order"):
        if ".asSequence()" in variant["prompt"]["en"]:
            assert "every element before `map`" not in variant["explanation"]["en"].split(" comes from ")[0]
