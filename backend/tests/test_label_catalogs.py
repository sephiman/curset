# SPDX-License-Identifier: AGPL-3.0-only
"""The answer-label and chart-label catalogs the export writes to `dist/i18n/` for the Android app."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_BACKEND = Path(__file__).resolve().parent.parent
if str(_BACKEND) not in sys.path:
    sys.path.insert(0, str(_BACKEND))

from scripts.export_bundle import I18N_DIR, main  # noqa: E402
from scripts.label_catalogs import LabelCatalogError, build_label_catalogs  # noqa: E402

LOCALES = ("en", "es")
EXPECTED_FILES = {
    "chart-labels.en.json",
    "chart-labels.es.json",
    "exercise-labels.en.json",
    "exercise-labels.es.json",
}


def _i18n_copy(tmp_path: Path) -> Path:
    target = tmp_path / "i18n-src"
    target.mkdir()
    for locale in LOCALES:
        (target / f"{locale}.json").write_bytes((I18N_DIR / f"{locale}.json").read_bytes())
    return target


def test_the_catalogs_are_flat_and_name_the_same_keys_in_both_locales() -> None:
    catalogs = build_label_catalogs(I18N_DIR, LOCALES)

    assert set(catalogs) == EXPECTED_FILES
    for catalog in ("exercise-labels", "chart-labels"):
        en, es = catalogs[f"{catalog}.en.json"], catalogs[f"{catalog}.es.json"]
        assert en.keys() == es.keys()
        assert all(isinstance(text, str) for text in [*en.values(), *es.values()])


def test_the_catalogs_carry_the_current_web_wording() -> None:
    """The 1.1.0 app import offered "Origin zone respected" under a prompt about an order block."""
    catalogs = build_label_catalogs(I18N_DIR, LOCALES)

    assert catalogs["exercise-labels.en.json"]["chartLabel.zone_respected"] == "Order block respected"
    assert catalogs["exercise-labels.es.json"]["chartLabel.overrun_at_level"].startswith("Envolvente")
    assert catalogs["chart-labels.en.json"]["band.origin"] == "Order block"
    assert catalogs["chart-labels.es.json"]["level.shelf"] == "Nivel"


def test_rejects_a_label_present_in_only_one_locale(tmp_path: Path) -> None:
    source = _i18n_copy(tmp_path)
    es = json.loads((source / "es.json").read_text(encoding="utf-8"))
    del es["level"]["shelf"]
    (source / "es.json").write_text(json.dumps(es, ensure_ascii=False), encoding="utf-8")

    with pytest.raises(LabelCatalogError, match=r"chart-labels.*'es': \['level\.shelf'\]"):
        build_label_catalogs(source, LOCALES)


def test_rejects_a_namespace_that_is_not_flat_strings(tmp_path: Path) -> None:
    source = _i18n_copy(tmp_path)
    en = json.loads((source / "en.json").read_text(encoding="utf-8"))
    en["divergence"]["bullish"] = {"nested": "no"}
    (source / "en.json").write_text(json.dumps(en), encoding="utf-8")

    with pytest.raises(LabelCatalogError, match=r"divergence\.bullish"):
        build_label_catalogs(source, LOCALES)


def test_the_export_writes_the_catalogs_beside_the_bundle_sorted(tmp_path: Path) -> None:
    out = tmp_path / "dist" / "bundle"

    assert main(["--out", str(out), "--skip-ast"]) == 0

    written = tmp_path / "dist" / "i18n"
    assert {path.name for path in written.iterdir()} == EXPECTED_FILES
    for path in written.iterdir():
        entries = json.loads(path.read_text(encoding="utf-8"))
        assert list(entries) == sorted(entries)
    assert not (out / "i18n").exists()  # outside the bundle, so outside its fingerprint
