# SPDX-License-Identifier: AGPL-3.0-only
"""Every error the API can return has a message in both interface languages, so the web never shows the
backend's English text (a Spanish reader once got «This exam is not in progress.»)."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

SRC = Path(__file__).resolve().parents[1] / "src" / "tradeschool"
I18N = Path(__file__).resolve().parents[2] / "frontend" / "src" / "i18n"
_RAISED = re.compile(r'AppError\(\s*"([A-Z_]+)"')


def _codes() -> set[str]:
    return {code for path in SRC.rglob("*.py") for code in _RAISED.findall(path.read_text(encoding="utf-8"))}


def test_the_scan_finds_the_errors_it_guards() -> None:
    assert {"EXAM_NOT_OPEN", "PRACTICE_NOT_AVAILABLE", "QUESTION_NOT_FOUND"} <= _codes()


@pytest.mark.parametrize("locale", ["es", "en"])
def test_every_error_code_has_an_interface_message(locale: str) -> None:
    messages = json.loads((I18N / f"{locale}.json").read_text(encoding="utf-8"))["errors"]
    assert sorted(_codes() - set(messages)) == []
