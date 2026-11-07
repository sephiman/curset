# SPDX-License-Identifier: AGPL-3.0-only
"""`calculo-fracciones-proporciones`: what remains of a total, proportional sharing, nested fractions."""

from __future__ import annotations

import random
from fractions import Fraction
from typing import ClassVar

from tradeschool.psicotecnico.contract import (
    ItemGenerator,
    UnsolvableItem,
    deal,
    int_fact,
    pick_wrong,
    str_fact,
)
from tradeschool.psicotecnico.item import Item, Params
from tradeschool.psicotecnico.spanish import number, sentence_case

_ORDINAL = {2: "segundo", 3: "tercer"}
_WORD = {2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"}
_PARTS_WORDS = {2: "dos", 3: "tres", 5: "cinco", 4: "cuatro", 6: "seis"}


def _fraction_word(num: int, den: int) -> str:
    names = {2: "medio", 3: "tercio", 4: "cuarto", 5: "quinto", 6: "sexto", 8: "octavo", 9: "noveno"}
    if num == 1:
        return f"un {names[den]}"
    return f"{_WORD[num]} {names[den]}s"


def _remaining(rng: random.Random) -> dict[str, object]:
    den = rng.choice([8, 9, 6, 5])
    first, second = rng.randint(1, den // 2 - 1 or 1), rng.randint(1, den // 3 + 1)
    if first + second >= den:
        second = 1
    total = den * rng.randint(20, 90)
    return {"kind": "remaining", "total": total, "den": den, "first": first, "second": second}


def _proportional(rng: random.Random) -> dict[str, object]:
    ratios = rng.choice([[2, 3, 5], [1, 2, 3], [2, 3, 4], [1, 3, 5], [3, 4, 5], [1, 2, 3, 4]])
    amount = sum(ratios) * rng.randint(20, 150)
    asked = rng.randrange(len(ratios))
    return {"kind": "proportional", "amount": amount, "ratios": ratios, "asked": asked}


def _fraction_of_fraction(rng: random.Random) -> dict[str, object]:
    den = rng.choice([4, 5, 6, 8])
    full = rng.randint(2, den - 1)
    outer = rng.choice([(1, 2), (1, 3), (2, 3), (1, 4)])
    return {"kind": "nested", "full": full, "den": den, "used_num": outer[0], "used_den": outer[1]}


def _answer(facts: dict[str, object] | object) -> Fraction:
    assert isinstance(facts, dict)
    kind = str_fact(facts, "kind")
    if kind == "remaining":
        total, den = int_fact(facts, "total"), int_fact(facts, "den")
        return Fraction(total) - Fraction(total, den) * (int_fact(facts, "first") + int_fact(facts, "second"))
    if kind == "proportional":
        ratios = facts["ratios"]
        assert isinstance(ratios, list)
        return Fraction(int_fact(facts, "amount") * ratios[int_fact(facts, "asked")], sum(ratios))
    if kind == "nested":
        held = Fraction(int_fact(facts, "full"), int_fact(facts, "den"))
        return held * (1 - Fraction(int_fact(facts, "used_num"), int_fact(facts, "used_den")))
    raise UnsolvableItem(f"unknown kind {kind!r}")


def _fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}."


class FraccionesGenerator(ItemGenerator):
    id: ClassVar[str] = "calculo-fracciones-proporciones"

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        level = params.difficulty
        for _ in range(300):
            facts = {1: _remaining, 2: _proportional, 3: _fraction_of_fraction}[level](rng)
            answer = _answer(facts)
            stem, why = self._text(facts, answer)
            if level == 3:
                if answer.denominator == 1 or answer == Fraction(
                    int_fact(facts, "full"), int_fact(facts, "den")
                ):
                    continue
                key = _fraction_text(answer)
                wrong = self._nested_wrong(facts, answer)
            else:
                decimals = 0
                key = number(answer, decimals) + "."
                if answer.denominator != 1:
                    continue
                wrong = [
                    number(w, decimals) + "." for w in pick_wrong(rng, answer, self._slips(facts, answer))
                ]
            unique = [w for w in dict.fromkeys(wrong) if w != key]
            if len(unique) < 3:
                continue
            options, slot = deal(rng, key, unique[:6])
            return Item(
                generator=self.id,
                seed=seed,
                difficulty=level,
                stem=stem,
                options=options,
                key=slot,
                explanation=why,
                facts=facts,
            )
        raise RuntimeError(f"no fraction item for seed {seed}")

    @staticmethod
    def _slips(facts: dict[str, object], answer: Fraction) -> list[Fraction]:
        kind = str_fact(facts, "kind")
        if kind == "remaining":
            total, den = int_fact(facts, "total"), int_fact(facts, "den")
            used = Fraction(total, den) * (int_fact(facts, "first") + int_fact(facts, "second"))
            return [used, Fraction(total, den) * (int_fact(facts, "first") + int_fact(facts, "second") + 1)]
        ratios = facts["ratios"]
        assert isinstance(ratios, list)
        amount = int_fact(facts, "amount")
        asked = int_fact(facts, "asked")
        return [Fraction(amount, len(ratios)), Fraction(amount * ratios[asked], sum(ratios) + 1)]

    @staticmethod
    def _nested_wrong(facts: dict[str, object], answer: Fraction) -> list[str]:
        held = Fraction(int_fact(facts, "full"), int_fact(facts, "den"))
        used = Fraction(int_fact(facts, "used_num"), int_fact(facts, "used_den"))
        candidates = [
            held * used,
            held - used,
            held + used if held + used < 1 else held / 2,
            held * (1 - used) + Fraction(1, 10),
        ]
        return [_fraction_text(c) for c in candidates if c > 0 and c != answer and c.denominator != 1]

    @staticmethod
    def _text(facts: dict[str, object], answer: Fraction) -> tuple[str, str]:
        kind = str_fact(facts, "kind")
        if kind == "remaining":
            total, den = int_fact(facts, "total"), int_fact(facts, "den")
            first, second = int_fact(facts, "first"), int_fact(facts, "second")
            stem = (
                f"Tenemos que preparar {number(total)} paquetes de bienvenida. El primer día preparamos "
                f"{_fraction_word(first, den)} del total de paquetes y el segundo día preparamos "
                f"{_fraction_word(second, den)} del total. ¿Cuántos paquetes nos quedan por preparar?"
            )
            why = (
                f"{sentence_case(_fraction_word(1, den))} son {number(total // den)} paquetes; "
                f"se han preparado {first} + {second} = "
                f"{first + second} de esas partes, así que quedan {number(answer)}."
            )
            return stem, why
        if kind == "proportional":
            amount = int_fact(facts, "amount")
            ratios = facts["ratios"]
            assert isinstance(ratios, list)
            asked = int_fact(facts, "asked")
            names = ["la primera", "la segunda", "la tercera", "la cuarta"]
            parts = ", ".join(str(r) for r in ratios[:-1]) + f" y {ratios[-1]}"
            stem = (
                f"Un premio de {number(amount)} euros se reparte entre {_WORD[len(ratios)]} personas de "
                f"forma "
                f"directamente proporcional a {parts}. ¿Cuántos euros recibe {names[asked]}?"
            )
            why = (
                f"El total son {sum(ratios)} partes y cada parte vale "
                f"{number(Fraction(amount, sum(ratios)))}; "
                f"la persona pedida tiene {ratios[asked]} {'parte' if ratios[asked] == 1 else 'partes'}: "
                f"{number(answer)}."
            )
            return stem, why
        full, den = int_fact(facts, "full"), int_fact(facts, "den")
        un, ud = int_fact(facts, "used_num"), int_fact(facts, "used_den")
        stem = (
            f"Un depósito está lleno en {full}/{den} de su capacidad. Se utiliza {un}/{ud} de lo que "
            f"contiene. "
            "¿Qué fracción de la capacidad del depósito queda ocupada?"
        )
        why = (
            f"Queda {ud - un}/{ud} de {full}/{den}: ({ud - un} × {full}) / ({ud} × {den}) = "
            f"{answer.numerator}/{answer.denominator}."
        )
        return stem, why

    def solve(self, item: Item) -> int:
        answer = _answer(item.facts)
        expected = _fraction_text(answer) if item.difficulty == 3 else number(answer, 0) + "."
        hits = [i for i, option in enumerate(item.options) if option == expected]
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options read {expected}")
        return hits[0]
