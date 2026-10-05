# SPDX-License-Identifier: AGPL-3.0-only
"""No visible string in the Android bundle may carry an internal value (the store-shots rule, ported)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_BACKEND = Path(__file__).resolve().parent.parent
if str(_BACKEND) not in sys.path:
    sys.path.insert(0, str(_BACKEND))

from scripts.export_bundle import BundleError, main  # noqa: E402
from scripts.leaked_tokens import bundle_leaks, leaked_tokens  # noqa: E402


@pytest.mark.parametrize(
    ("text", "token"),
    [
        ("A range with no false break is just a range (none).", "(none)"),
        ("Es solo un rango (NONE).", "(NONE)"),
        ("The rate is (n/a) today.", "(n/a)"),
        ("The stop sits at (null).", "(null)"),
        ("Your entry was undefined.", "undefined"),
        ("Liquidation at NaN USDT.", "NaN"),
        ("Close at {exit_price}.", "{exit_price}"),
        ("Subtract fee_rate * quantity * (entry + exit).", "fee_rate"),
    ],
)
def test_rejects_an_internal_token_in_visible_text(text: str, token: str) -> None:
    assert leaked_tokens(text) == [token]


@pytest.mark.parametrize(
    "text",
    [
        "Use the margin mode (isolated) so one trade cannot drain the account.",
        "None of them is safe, and the range is neither.",
        "A 4h candle is sixteen 15m candles.",
    ],
)
def test_accepts_prose_that_only_looks_like_a_token(text: str) -> None:
    assert leaked_tokens(text) == []


def test_accepts_the_slots_the_app_fills_but_not_others() -> None:
    template = "Open a **{side}** of **{quantity}** with a fee of **{fee_rate}** at {entry_price}."
    assert leaked_tokens(template, filled=frozenset({"side", "quantity", "fee_rate"})) == ["{entry_price}"]


def test_accepts_snake_case_in_a_code_span_only() -> None:
    formula = "EMA_today = k * close_today + (1 - k) * EMA_yesterday"
    assert leaked_tokens(formula, notation=True) == []
    assert leaked_tokens(formula) == ["close_today"]


def test_the_course_exports_clean_and_a_planted_leak_is_reported_where_it_sits(tmp_path: Path) -> None:
    out = tmp_path / "bundle"
    try:
        main(["--out", str(out), "--skip-ast"])
    except BundleError as error:
        pytest.fail(str(error))
    configs_path = out / "exercises" / "configs.json"
    configs = json.loads(configs_path.read_text(encoding="utf-8"))
    configs["configs"]["m09-ex-1"]["config"]["explanation"]["es"] += " Es solo un rango (none)."
    configs_path.write_text(json.dumps(configs, ensure_ascii=False), encoding="utf-8")

    leaks = bundle_leaks(out, tmp_path / "i18n")

    assert len(leaks) == 1
    assert leaks[0].startswith("m09-ex-1 explanation es: '(none)'")
