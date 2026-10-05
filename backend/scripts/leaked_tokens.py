# SPDX-License-Identifier: AGPL-3.0-only
"""Text a reader should never see: an internal value that leaked into a visible string of the bundle.

The port of `INTERNAL_TOKENS` in the Android repo's `tools/store-shots/store-shots.py`, run over every
visible string instead of the few a screenshot frames.
"""

from __future__ import annotations

import json
import re
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from tradeschool.content.schema import LOCALES

#: A sentinel in parentheses. Only these words: a parenthesised term such as "(isolated)" is prose.
PARENTHESISED_SENTINEL = re.compile(r"\((?:none|null|undefined|nan|n/a)\)", re.IGNORECASE)
BARE_SENTINEL = re.compile(r"\b(?:null|undefined|NaN)\b")
PLACEHOLDER = re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*)\}")
SNAKE_CASE = re.compile(r"\b[a-z]+(?:_[a-z0-9]+)+\b")

#: The slots the app fills in `error-phrases.json`'s sentences before drawing them.
ERROR_SENTENCE_SLOTS = frozenset({"value", "mistake"})

#: The glossary fields a reader sees; `match` and `linkExcept` are patterns, never drawn.
GLOSSARY_VISIBLE_FIELDS = frozenset({"term", "definition", "originTitle"})


def leaked_tokens(text: str, *, filled: frozenset[str] = frozenset(), notation: bool = False) -> list[str]:
    """`filled`: slots the app fills; `notation`: a code span, where snake_case is authored."""
    found = [match[0] for match in PARENTHESISED_SENTINEL.finditer(text)]
    unbracketed = PARENTHESISED_SENTINEL.sub(" ", text)  # "(null)" is one leak, not two
    found += [match[0] for match in BARE_SENTINEL.finditer(unbracketed)]
    found += [match[0] for match in PLACEHOLDER.finditer(text) if match[1] not in filled]
    without_placeholders = PLACEHOLDER.sub(" ", text)  # a filled slot's name is not text a reader sees
    if not notation:
        found += [match[0] for match in SNAKE_CASE.finditer(without_placeholders)]
    return found


def _localized_pairs(node: object, path: str = "") -> Iterator[tuple[str, str, str]]:
    if isinstance(node, dict):
        if set(node) == set(LOCALES) and all(isinstance(value, str) for value in node.values()):
            for locale in LOCALES:
                yield path, locale, node[locale]
            return
        for key, value in node.items():
            yield from _localized_pairs(value, f"{path}.{key}" if path else str(key))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from _localized_pairs(value, f"{path}[{index}]")


def _glossary_texts(node: object, path: str) -> Iterator[tuple[str, str]]:
    if isinstance(node, dict):
        for key, value in node.items():
            if key in GLOSSARY_VISIBLE_FIELDS and isinstance(value, str):
                yield f"{path}.{key}", value
            else:
                yield from _glossary_texts(value, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from _glossary_texts(value, f"{path}[{index}]")


def _ast_texts(node: dict[str, Any], path: str) -> Iterator[tuple[str, str, bool]]:
    if node.get("type") in ("text", "inlineCode"):
        yield path, node["value"], node["type"] == "inlineCode"
    for index, child in enumerate(node.get("children") or []):
        yield from _ast_texts(child, f"{path}/{index}")


def _read(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def bundle_leaks(out: Path, label_catalogs: Path) -> list[str]:
    """Every leaked token in the bundle at `out` and its label catalogs, as `where: token in «…»`."""
    found: list[str] = []

    def check(where: str, text: str, **options: Any) -> None:
        found.extend(f"{where}: {token!r} in «{text}»" for token in leaked_tokens(text, **options))

    for path, locale, text in _localized_pairs(_read(out / "manifest.json")):
        check(f"manifest {path} {locale}", text)
    for path, locale, text in _localized_pairs(_read(out / "figures" / "specs.json")):
        check(f"figures {path} {locale}", text)
    for exercise_id, entry in _read(out / "exercises" / "configs.json")["configs"].items():
        config = entry["config"]
        params = frozenset(param["name"] for param in config.get("params") or [])
        for path, locale, text in _localized_pairs(config):
            # Only a calculation's prompt is formatted with its params (`calculation.py`).
            filled = params if entry["type"] == "calculation" and path == "prompt" else frozenset()
            check(f"{exercise_id} {path} {locale}", text, filled=filled)
    phrases = _read(out / "error-phrases.json")
    for locale, sentence in phrases["sentences"].items():
        check(f"error-phrases sentences {locale}", sentence, filled=ERROR_SENTENCE_SLOTS)
    for phrase in phrases["phrases"]:
        for locale in LOCALES:
            check(f"error-phrases {phrase['key']!r} {locale}", phrase[locale])
    for glossary in sorted((out / "glossary").glob("*.json")):
        for path, text in _glossary_texts(_read(glossary)["entries"], glossary.stem):
            check(path, text)
    for lesson in sorted((out / "ast").glob("*/*.json")):
        document = _read(lesson)
        where = f"{document['locale']}/{document['lessonId']}"
        for path, text, notation in _ast_texts(document["ast"], where):
            check(path, text, notation=notation)
    for catalog in sorted(label_catalogs.glob("*.json")):
        for key, text in _read(catalog).items():
            check(f"{catalog.name} {key}", text)
    return found
