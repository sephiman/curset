# SPDX-License-Identifier: AGPL-3.0-only
"""`calculo-problemas`: short word problems and the operator puzzle, worked left to right."""

from __future__ import annotations

import itertools
import random
import re
from collections.abc import Mapping
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
from tradeschool.psicotecnico.spanish import euros, number

_OPERATORS = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "×": lambda a, b: a * b}
_THINGS = ("unidades", "cajas", "carpetas", "sobres")


def _capacity(rng: random.Random) -> dict[str, object]:
    per_day = rng.choice([40, 65, 75, 80, 120])
    days = rng.randint(8, 25)
    stock = rng.choice([300, 525, 640, 800, 1200])
    return {
        "kind": "capacity",
        "stock": stock,
        "per_day": per_day,
        "days": days,
        "capacity": stock + per_day * days,
    }


def _unit_price(rng: random.Random) -> dict[str, object]:
    each = rng.choice([2, 3, 4, 5, 6, 8])
    return {
        "kind": "unit-price",
        "bought": rng.choice([6, 8, 12, 15]),
        "each": each,
        "wanted": rng.choice([20, 25, 30, 18]),
    }


def _count(rng: random.Random) -> dict[str, object]:
    return {
        "kind": "count",
        "rooms": rng.randint(3, 9),
        "rows": rng.randint(8, 20),
        "seats": rng.randint(6, 14),
    }


def _subgroup(rng: random.Random) -> dict[str, object]:
    chosen = rng.randint(4, 12)
    each = rng.choice([40, 50, 75, 120, 150])
    return {
        "kind": "subgroup",
        "staff": chosen + rng.randint(6, 20),
        "chosen": chosen,
        "total": chosen * each,
    }


def _products(rng: random.Random) -> dict[str, object]:
    return {
        "kind": "products",
        "pens": rng.randint(5, 30),
        "pen_cents": rng.choice([45, 80, 120, 95, 150]),
        "folders": rng.randint(4, 20),
        "folder_cents": rng.choice([210, 325, 480, 150, 260]),
    }


def _ratio(rng: random.Random) -> dict[str, object]:
    small = rng.randint(6, 40)
    factor = rng.choice([2, 3, 4, 5])
    return {"kind": "ratio", "small": small, "factor": factor}


def _operators(rng: random.Random) -> dict[str, object]:
    for _ in range(200):
        numbers = [rng.randint(2, 12) for _ in range(4)]
        ops = [rng.choice(list(_OPERATORS)) for _ in range(3)]
        value = _left_to_right(numbers, ops)
        matches = [
            c for c in itertools.product(_OPERATORS, repeat=3) if _left_to_right(numbers, list(c)) == value
        ]
        if len(matches) == 1 and 0 < value < 200:
            return {"kind": "operators", "numbers": numbers, "ops": ops, "target": value}
    raise RuntimeError("no operator puzzle found")


def _left_to_right(numbers: list[int], ops: list[str]) -> int:
    value = numbers[0]
    for op, nxt in zip(ops, numbers[1:], strict=True):
        value = _OPERATORS[op](value, nxt)
    return value


_BY_LEVEL = {
    1: [_capacity, _unit_price, _count],
    2: [_subgroup, _products, _ratio, _operators],
    3: [_products, _operators, _subgroup, _capacity],
}


def _answer(facts: dict[str, object] | object) -> Fraction | tuple[str, ...]:
    assert isinstance(facts, dict)
    kind = str_fact(facts, "kind")

    def n(name: str) -> int:
        return int_fact(facts, name)

    if kind == "capacity":
        return Fraction(n("capacity") - n("stock"), n("per_day"))
    if kind == "unit-price":
        return Fraction(n("each") * n("wanted"))
    if kind == "count":
        return Fraction(n("rooms") * n("rows") * n("seats"))
    if kind == "subgroup":
        return Fraction(n("total"), n("chosen"))
    if kind == "products":
        return Fraction(n("pens") * n("pen_cents") + n("folders") * n("folder_cents"), 100)
    if kind == "ratio":
        return Fraction(n("small") * n("factor"))
    if kind == "operators":
        numbers = facts["numbers"]
        assert isinstance(numbers, list)
        found = tuple(
            " ".join(c)
            for c in itertools.product(_OPERATORS, repeat=3)
            if _left_to_right(numbers, list(c)) == n("target")
        )
        return found
    raise UnsolvableItem(f"unknown kind {kind!r}")


def _stem_and_why(facts: dict[str, object], answer: Fraction | tuple[str, ...]) -> tuple[str, str]:
    kind = str_fact(facts, "kind")
    shown = answer if isinstance(answer, Fraction) else Fraction(0)

    def n(name: str) -> int:
        return int_fact(facts, name)

    if kind == "capacity":
        stem = (
            f"Un almacén tiene una capacidad de {n('capacity')} unidades. Si el almacén tiene {n('stock')} "
            f"unidades en stock y todos los días se reciben y almacenan {n('per_day')} unidades, "
            "¿cuántos días necesita para alcanzar su máxima capacidad?"
        )
        return (
            stem,
            f"Faltan {n('capacity')} − {n('stock')} = {n('capacity') - n('stock')} unidades; entre "
            f"{n('per_day')} al día son {n('days')} días.",
        )
    if kind == "unit-price":
        total = n("bought") * n("each")
        stem = (
            f"Si {n('bought')} cuadernos cuestan {total} euros y todos tienen el mismo precio, "
            f"¿cuánto costarán {n('wanted')} cuadernos?"
        )
        return (
            stem,
            f"Cada cuaderno cuesta {total} / {n('bought')} = {n('each')} euros; {n('wanted')} × {n('each')} "
            f"= {number(shown)}.",
        )
    if kind == "count":
        stem = (
            f"Un edificio tiene {n('rooms')} salas de formación y cada una tiene {n('rows')} filas de "
            f"{n('seats')} sillas. ¿Cuántas sillas hay en total?"
        )
        return stem, f"{n('rooms')} × {n('rows')} × {n('seats')} = {number(shown)} sillas."
    if kind == "subgroup":
        stem = (
            f"Un departamento de {n('staff')} empleados recibe una gratificación total de "
            f"{number(n('total'))} "
            f"euros. Si se reparte a partes iguales solo entre los {n('chosen')} que han cumplido objetivos, "
            "¿cuántos euros recibe cada uno?"
        )
        return (
            stem,
            f"El reparto es entre {n('chosen')}, no entre {n('staff')}: {number(n('total'))} / "
            f"{n('chosen')} = {number(shown)}.",
        )
    if kind == "products":
        pens, folders = n("pens"), n("folders")
        stem = (
            f"En una papelería se compran {pens} bolígrafos a {euros(Fraction(n('pen_cents'), 100))} cada "
            f"uno "
            f"y {folders} carpetas a {euros(Fraction(n('folder_cents'), 100))} cada una. ¿Cuál es el "
            f"importe total?"
        )
        return stem, (
            f"{pens} × {number(Fraction(n('pen_cents'), 100), 2)} + {folders} × "
            f"{number(Fraction(n('folder_cents'), 100), 2)} = {number(shown, 2)} euros."
        )
    if kind == "ratio":
        total = n("small") * (n("factor") + 1)
        stem = (
            f"La suma de dos números es {total} y uno de ellos es {n('factor')} veces el otro. ¿Cuál "
            f"es el mayor?"
        )
        return (
            stem,
            f"El menor es {total} / {n('factor') + 1} = {n('small')}; el mayor es {n('factor')} × "
            f"{n('small')} = {number(shown)}.",
        )
    numbers = facts["numbers"]
    assert isinstance(numbers, list)
    stem = (
        f"Indique qué operadores, aplicados de izquierda a derecha, hacen cierta la igualdad: "
        f"{numbers[0]} _ {numbers[1]} _ {numbers[2]} _ {numbers[3]} = {n('target')}"
    )
    ops = facts["ops"]
    assert isinstance(ops, list)
    steps, running = [], numbers[0]
    for op, nxt in zip(ops, numbers[1:], strict=True):
        after = _OPERATORS[op](running, nxt)
        steps.append(f"{running} {op} {nxt} = {after}")
        running = after
    return stem, "Se opera de izquierda a derecha: " + "; ".join(steps) + "."


def _render(facts: Mapping[str, object], value: Fraction) -> str:
    kind = str_fact(facts, "kind")
    if kind == "capacity":
        return f"{number(value)} días."
    if kind == "products":
        return euros(value)
    return f"{number(value)}."


class ProblemasGenerator(ItemGenerator):
    id: ClassVar[str] = "calculo-problemas"

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        for _ in range(200):
            facts = rng.choice(_BY_LEVEL[params.difficulty])(rng)
            answer = _answer(facts)
            stem, why = _stem_and_why(facts, answer)
            if isinstance(answer, tuple):
                if len(answer) != 1:
                    continue
                key = answer[0].replace(" ", ", ")
                wrong = self._operator_wrong(rng, facts, answer[0])
            else:
                key = _render(facts, answer)
                kind = str_fact(facts, "kind")
                slips = self._slips(facts)
                if kind in ("capacity",) and answer.denominator != 1:
                    continue
                wrong = [_render(facts, w) for w in pick_wrong(rng, answer, slips)]
            unique = [w for w in dict.fromkeys(wrong) if w != key]
            if len(unique) < 3:
                continue
            options, slot = deal(rng, key, unique[:6])
            return Item(
                generator=self.id,
                seed=seed,
                difficulty=params.difficulty,
                stem=stem,
                options=options,
                key=slot,
                explanation=why,
                facts=facts,
            )
        raise RuntimeError(f"no problem for seed {seed}")

    @staticmethod
    def _slips(facts: dict[str, object]) -> list[Fraction]:
        kind = str_fact(facts, "kind")

        def n(name: str) -> int:
            return int_fact(facts, name)

        if kind == "capacity":
            return [Fraction(n("capacity"), n("per_day")), Fraction(n("capacity") + n("stock"), n("per_day"))]
        if kind == "subgroup":
            return [Fraction(n("total"), n("staff")), Fraction(n("total"), n("staff") - n("chosen"))]
        if kind == "products":
            return [Fraction((n("pens") + n("folders")) * n("pen_cents"), 100)]
        if kind == "ratio":
            return [
                Fraction(n("small") * (n("factor") + 1), 2),
                Fraction(n("small") * (n("factor") + 1) - n("small"), 2),
            ]
        return []

    @staticmethod
    def _operator_wrong(rng: random.Random, facts: dict[str, object], key: str) -> list[str]:
        numbers = facts["numbers"]
        assert isinstance(numbers, list)
        target = int_fact(facts, "target")
        near = [
            ", ".join(c)
            for c in itertools.product(_OPERATORS, repeat=3)
            if " ".join(c) != key and abs(_left_to_right(numbers, list(c)) - target) <= max(12, target // 3)
        ]
        rng.shuffle(near)
        return near

    def solve(self, item: Item) -> int:
        answer = _answer(item.facts)
        if isinstance(answer, tuple):
            if len(answer) != 1:
                raise UnsolvableItem(f"{len(answer)} operator triples reach the target")
            expected = answer[0].replace(" ", ", ")
        else:
            expected = _render(item.facts, answer)
        hits = [i for i, option in enumerate(item.options) if option == expected]
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options read {expected}")
        return hits[0]

    def check_extra(self, item: Item) -> list[str]:
        if str_fact(item.facts, "kind") != "operators":
            return []
        numbers = item.facts["numbers"]
        assert isinstance(numbers, list)
        target = int_fact(item.facts, "target")
        reaching = [o for o in item.options if _left_to_right(numbers, re.findall(r"[+×-]", o)) == target]
        return [] if len(reaching) == 1 else [f"{len(reaching)} operator options reach the target"]
