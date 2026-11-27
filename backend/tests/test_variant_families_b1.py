# SPDX-License-Identifier: AGPL-3.0-only
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import pytest
import yaml

COURSE = Path(__file__).resolve().parents[2] / "content" / "backend-in-depth"
FAMILIES = {
    "collectors-grouping": "m11-l01-ex-collectors-grouping",
    "collectors-tomap": "m11-l01-ex-collectors-tomap",
    "collectors-teeing": "m11-l01-ex-collectors-teeing",
    "takewhile": "m11-l01-ex-takewhile",
    "dropwhile": "m11-l01-ex-dropwhile",
    "gatherers-windowfixed": "m11-l01-ex-gatherers-windowfixed",
    "gatherers-windowsliding": "m11-l01-ex-gatherers-windowsliding",
    "gatherers-fold": "m11-l01-ex-gatherers-fold",
    "gatherers-scan": "m11-l01-ex-gatherers-scan",
    "comparators": "m11-l01-ex-comparators",
}


def _variants(family: str) -> list[dict[str, object]]:
    path = COURSE / "exercises" / f"{FAMILIES[family]}.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))["variants"]


def _runs(family: str) -> list[dict[str, object]]:
    return json.loads((COURSE / "variants" / f"{family}.runs.json").read_text(encoding="utf-8"))


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
        assert len(texts) == 4
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
