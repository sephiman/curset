# SPDX-License-Identifier: AGPL-3.0-only
"""Undo the wording form a generator wrapped around an option, to get back the computed text."""

from __future__ import annotations


def plain_option(option: str, forms: tuple[str, ...]) -> str:
    """The longest-wrapper form that fits wins, so `exactly {}` is tried before the bare `{}`."""
    for form in sorted(forms, key=lambda f: len(f) - 2, reverse=True):
        head, _, tail = form.partition("{}")
        if option.startswith(head) and option.endswith(tail) and len(option) >= len(head) + len(tail):
            return option[len(head) : len(option) - len(tail)]
    return option
