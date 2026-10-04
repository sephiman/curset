# SPDX-License-Identifier: AGPL-3.0-only
"""Alphabetical order as a reader expects it, shared by the glossary and the course catalogue."""

from __future__ import annotations

import unicodedata


def alphabetical_key(value: str) -> str:
    """Fold case and accents so `emisión` sorts with `e`, not after `z`."""
    lowered = value.casefold()
    stripped = unicodedata.normalize("NFD", lowered)
    return "".join(c for c in stripped if unicodedata.category(c) != "Mn")
