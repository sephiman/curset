# SPDX-License-Identifier: AGPL-3.0-only
"""The web's answer-label and chart-label i18n entries, flattened for the Android app to import."""

from __future__ import annotations

import json
from pathlib import Path

#: Each catalog, and the i18n namespaces it carries. The app's `ExerciseStrings.kt` holds the first
#: and `ChartStrings.kt` the second; `exercise.*` UI copy is adapted there, not transcribed, so it stays out.
CATALOGS: dict[str, tuple[str, ...]] = {
    "exercise-labels": ("chartLabel", "divergence"),
    "chart-labels": ("band", "candle", "chartMarker", "diagonal", "level", "overlay"),
}

LabelCatalog = dict[str, str]


class LabelCatalogError(RuntimeError):
    """An i18n file cannot be exported as a flat catalog both locales agree on."""


def catalog_path(catalog: str, locale: str) -> str:
    return f"{catalog}.{locale}.json"


def flatten(source: dict[str, object], namespaces: tuple[str, ...], origin: str) -> LabelCatalog:
    """`{namespace: {key: text}}` → `{"namespace.key": text}`, the key i18next itself resolves."""
    flat: LabelCatalog = {}
    for namespace in namespaces:
        entries = source.get(namespace)
        if not isinstance(entries, dict) or not entries:
            raise LabelCatalogError(f"{origin} has no `{namespace}` namespace")
        for key, text in entries.items():
            if not isinstance(text, str):
                raise LabelCatalogError(f"{origin} `{namespace}.{key}` is not a string")
            flat[f"{namespace}.{key}"] = text
    return flat


def check_same_keys(catalog: str, by_locale: dict[str, LabelCatalog]) -> None:
    every_key = set().union(*by_locale.values())
    missing = {
        locale: sorted(every_key - set(entries))
        for locale, entries in by_locale.items()
        if every_key - set(entries)
    }
    if missing:
        raise LabelCatalogError(f"`{catalog}` is missing keys: {missing}")


def build_label_catalogs(i18n_dir: Path, locales: tuple[str, ...]) -> dict[str, LabelCatalog]:
    """Every catalog file, by its name under `dist/i18n/`. Refuses a key that only one locale has."""
    sources = {
        locale: json.loads((i18n_dir / f"{locale}.json").read_text(encoding="utf-8")) for locale in locales
    }
    files: dict[str, LabelCatalog] = {}
    for catalog, namespaces in CATALOGS.items():
        by_locale = {
            locale: flatten(source, namespaces, f"{locale}.json") for locale, source in sources.items()
        }
        check_same_keys(catalog, by_locale)
        for locale, entries in by_locale.items():
            files[catalog_path(catalog, locale)] = entries
    return files
