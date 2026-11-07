# SPDX-License-Identifier: AGPL-3.0-only
"""How the exam prints numbers and sorts words: decimal comma, thousands point, ñ after n."""

from __future__ import annotations

import unicodedata
from fractions import Fraction


def round_half_up(value: Fraction, decimals: int) -> Fraction:
    scale = 10**decimals
    scaled = abs(value) * scale
    floor = scaled.numerator // scaled.denominator
    if scaled - floor >= Fraction(1, 2):
        floor += 1
    return Fraction(floor if value >= 0 else -floor, scale)


def number(value: Fraction | int, decimals: int = 0) -> str:
    rounded = round_half_up(Fraction(value), decimals)
    negative = rounded < 0
    scaled = abs(rounded) * 10**decimals
    digits = str(scaled.numerator // scaled.denominator).rjust(decimals + 1, "0")
    whole, fraction = digits[: len(digits) - decimals], digits[len(digits) - decimals :]
    if len(whole) >= 5:
        whole = f"{int(whole):,}".replace(",", ".")
    text = whole + ("," + fraction if decimals else "")
    return ("-" if negative and rounded != 0 else "") + text


def euros(value: Fraction | int, decimals: int = 2) -> str:
    return f"{number(value, decimals)} €"


def percent(value: Fraction | int, decimals: int = 2) -> str:
    return f"{number(value, decimals)} %"


def spanish_key(word: str) -> str:
    """Alphabetical sort key: accents folded, ñ between n and o."""
    lowered = word.casefold().replace("ñ", "n\U0010ffff")
    stripped = unicodedata.normalize("NFD", lowered)
    return "".join(c for c in stripped if unicodedata.category(c) != "Mn")


def sentence_case(text: str) -> str:
    return text[:1].upper() + text[1:]
