# SPDX-License-Identifier: AGPL-3.0-only
"""`calculo-ecuaciones`: a linear equation with a bracket; the solver parses the printed equation."""

from __future__ import annotations

import random
import re
from fractions import Fraction
from typing import ClassVar

from tradeschool.psicotecnico.contract import ItemGenerator, UnsolvableItem, deal
from tradeschool.psicotecnico.item import Item, Params
from tradeschool.psicotecnico.spanish import number, round_half_up

Linear = tuple[Fraction, Fraction]  # (coefficient of x, constant)

# level -> (coefficient bound, constant bound)
_BOUNDS = {1: (9, 20), 2: (16, 60), 3: (32, 832)}
_TOKEN = re.compile(r"\s*(\d+|x|[-+*()=])")


def _plain(value: Fraction) -> str:
    return str(value.numerator)


def _term(coef: int, *, first: bool) -> str:
    """`coef`·x as written: «x», «-x», «9x», sign spaced unless it opens the expression."""
    body = ("" if abs(coef) == 1 else str(abs(coef))) + "x"
    if first:
        return ("-" if coef < 0 else "") + body
    return ("- " if coef < 0 else "+ ") + body


def _const(value: int, *, first: bool) -> str:
    if first:
        return str(value)
    return ("- " if value < 0 else "+ ") + str(abs(value))


def _linear(coef: int, const: int) -> str:
    """`coef`x + `const`, omitting a zero part."""
    parts: list[str] = []
    if coef:
        parts.append(_term(coef, first=True))
    if const or not parts:
        parts.append(_const(const, first=not parts))
    return " ".join(parts)


class _Parser:
    """Linear expressions with implicit multiplication: `4(x - 4)`, `9x`, `-x`."""

    def __init__(self, text: str) -> None:
        self.tokens: list[str] = []
        position = 0
        while position < len(text):
            match = _TOKEN.match(text, position)
            if match is None:
                raise UnsolvableItem(f"cannot read {text[position:]!r}")
            self.tokens.append(match.group(1))
            position = match.end()
        self.at = 0

    def _peek(self) -> str | None:
        return self.tokens[self.at] if self.at < len(self.tokens) else None

    def _take(self) -> str:
        token = self.tokens[self.at]
        self.at += 1
        return token

    def equation(self) -> tuple[Linear, Linear]:
        left = self.expression()
        if self._peek() != "=":
            raise UnsolvableItem("no «=» in the equation")
        self._take()
        right = self.expression()
        if self._peek() is not None:
            raise UnsolvableItem("trailing text after the equation")
        return left, right

    def expression(self) -> Linear:
        total = self.product()
        while self._peek() in ("+", "-"):
            sign = 1 if self._take() == "+" else -1
            term = self.product()
            total = (total[0] + sign * term[0], total[1] + sign * term[1])
        return total

    def product(self) -> Linear:
        if self._peek() == "-":
            self._take()
            inner = self.product()
            return (-inner[0], -inner[1])
        value = self.atom()
        while (nxt := self._peek()) is not None and (nxt.isdigit() or nxt in ("x", "(", "*")):
            if nxt == "*":
                self._take()
            other = self.atom()
            if value[0] and other[0]:
                raise UnsolvableItem("not linear")
            value = (value[0] * other[1] + value[1] * other[0], value[1] * other[1])
        return value

    def atom(self) -> Linear:
        token = self._take()
        if token.isdigit():
            return Fraction(0), Fraction(int(token))
        if token == "x":
            return Fraction(1), Fraction(0)
        if token == "(":
            inner = self.expression()
            if self._peek() != ")":
                raise UnsolvableItem("unbalanced bracket")
            self._take()
            return inner
        raise UnsolvableItem(f"unexpected {token!r}")


def solve_equation(text: str) -> Fraction:
    left, right = _Parser(text).equation()
    slope = left[0] - right[0]
    if slope == 0:
        raise UnsolvableItem("x cancels out")
    return (right[1] - left[1]) / slope


def _bracket_form(rng: random.Random, level: int) -> tuple[str, list[str]]:
    cb, kb = _BOUNDS[level]
    a = rng.randint(2, cb)
    b = rng.choice([-1, 1]) * rng.randint(1, cb)
    c = rng.choice([-1, 1]) * rng.randint(1, kb)
    d = rng.randint(1, cb)
    e = rng.choice([-1, 1]) * rng.randint(0, kb) if level > 1 else 0
    if level == 1:
        # Pick x first so the equation holds: a(bx + c) = dx + e with e making both sides equal.
        x = rng.choice([-1, 1]) * rng.randint(1, 9)
        e = a * (b * x + c) - d * x
    left = f"{a}({_linear(b, c)})"
    right = _linear(d, e)
    slips = [
        f"{a * b}x {_const(c, first=False)} = {right}",  # forgets to distribute over c
        f"{a}({_linear(b, -c)}) = {right}",  # flips the sign inside the bracket
        f"{left} = {_linear(d, -e)}",  # flips the sign of the constant on the right
    ]
    return f"{left} = {right}", slips


def _swapped_form(rng: random.Random, level: int) -> tuple[str, list[str]]:
    cb, kb = _BOUNDS[level]
    p = rng.randint(2, kb)
    q = rng.randint(1, cb)
    r = rng.randint(2, cb)
    s = rng.randint(1, max(2, kb // 4))
    if level == 1:
        x = rng.choice([-1, 1]) * rng.randint(1, 9)
        p = r * (x - s) + q * x
    left = f"{p} - {'' if q == 1 else q}x"
    right = f"{r}(x - {s})"
    slips = [
        f"{p} - {q}x = {r}x - {s}",
        f"{p} + {q}x = {right}",
        f"{p} - {q}x = {r}(x + {s})",
    ]
    return f"{left} = {right}", slips


class EcuacionesGenerator(ItemGenerator):
    id: ClassVar[str] = "calculo-ecuaciones"

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        level = params.difficulty
        for _ in range(500):
            build = _bracket_form if rng.random() < 0.5 else _swapped_form
            equation, slips = build(rng, level)
            try:
                x = solve_equation(equation)
            except UnsolvableItem:
                continue
            if x == 0 or (level == 1) != (x.denominator == 1):
                continue
            if level > 1 and abs(round_half_up(x, 2)) < Fraction(1, 10):
                continue
            decimals = 0 if level == 1 else 2
            key = number(x, decimals)
            distractors = self._distractors(rng, x, slips, decimals)
            if distractors is None:
                continue
            options, slot = deal(rng, key, distractors)
            return Item(
                generator=self.id,
                seed=seed,
                difficulty=level,
                stem=f"Halla el valor de x en la siguiente ecuación: {equation}",
                options=options,
                key=slot,
                explanation=self._explanation(equation, x, decimals),
                facts={"equation": equation},
            )
        raise RuntimeError(f"no equation found for seed {seed}")

    @staticmethod
    def _distractors(rng: random.Random, x: Fraction, slips: list[str], decimals: int) -> list[str] | None:
        key = number(x, decimals)
        pool: list[str] = []
        if decimals == 0:
            near = [x - 2, x - 1, x + 1, x + 2, -x]
            pool = [number(v, 0) for v in near]
        else:
            for slip in slips:
                try:
                    pool.append(number(solve_equation(slip), decimals))
                except UnsolvableItem, ZeroDivisionError:
                    continue
            pool.append(number(-x, decimals))
            pool += [
                number(x + Fraction(k, 100), decimals) for k in (-12, -9, -7, -5, -3, -2, 2, 3, 5, 7, 9, 12)
            ]
            pool += [number(x + k, decimals) for k in (-2, -1, 1, 2)]
        unique = [v for v in dict.fromkeys(pool) if v != key and v not in ("0", "-0", "0,00")]
        if len(unique) < 3:
            return None
        rng.shuffle(unique)
        return unique

    @staticmethod
    def _explanation(equation: str, x: Fraction, decimals: int) -> str:
        left, right = _Parser(equation).equation()
        slope, const = left[0] - right[0], right[1] - left[1]
        if slope < 0:
            slope, const = -slope, -const
        return (
            f"Se desarrolla el paréntesis y se pasan las x a un lado: {_plain(slope)}x = {_plain(const)}, "
            f"de donde x = {_plain(const)} / {_plain(slope)} = {number(x, decimals)}."
        )

    def solve(self, item: Item) -> int:
        equation = str(item.stem).split(": ", 1)[1]
        x = solve_equation(equation)
        decimals = 0 if item.difficulty == 1 else 2
        expected = number(x, decimals)
        hits = [i for i, option in enumerate(item.options) if option == expected]
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options read {expected}")
        return hits[0]

    def check_extra(self, item: Item) -> list[str]:
        if item.difficulty == 1:
            whole = all(re.fullmatch(r"-?\d+", o) for o in item.options)
            return [] if whole else ["level 1 option is not an integer"]
        decimal = all(re.fullmatch(r"-?[\d.]+,\d\d", o) for o in item.options)
        return [] if decimal else ["option is not a 2-decimal number"]
