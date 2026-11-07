# SPDX-License-Identifier: AGPL-3.0-only
"""`calculo-porcentajes`: discounts, increases, shares, probabilities and remainders, to two decimals."""

from __future__ import annotations

import random
from collections.abc import Callable, Mapping
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
from tradeschool.psicotecnico.spanish import euros, number, percent, round_half_up

Render = Callable[[Fraction], str]
_PRODUCTS = ("un producto", "un artículo", "un electrodoméstico", "un mueble de oficina")


def _eur(value: Fraction) -> str:
    return euros(value)


def _pct(value: Fraction) -> str:
    return percent(value)


def _count(value: Fraction) -> str:
    return number(value, 0)


class _Case:
    def __init__(
        self,
        stem: str,
        render: Render,
        wrong: list[Fraction],
        why: str,
        facts: dict[str, object],
        plausible: Callable[[Fraction], bool] = lambda _: True,
    ) -> None:
        self.stem, self.render, self.wrong, self.why, self.facts = stem, render, wrong, why, facts
        self.plausible = plausible  # a near miss outside it reads as absurd; the named slips in `wrong` stay


def _discount(rng: random.Random, level: int) -> _Case:
    price = rng.choice([40, 45, 60, 80, 120, 150, 36, 75, 90])
    rate = rng.choice([5, 8, 12, 15, 18, 20, 25, 30])
    stem = (
        f"Si hay un {rate} % de descuento en {rng.choice(_PRODUCTS)} cuyo precio original es de {price} €, "
        "¿qué importe se pagará una vez aplicado el descuento?"
    )
    p, r = Fraction(price), Fraction(rate, 100)
    wrong = [p * (1 + r), p * (1 - r) + 1, p * (1 - r) - 2, p - r * 100]
    why = (
        f"El descuento es el {rate} % de {price}; se paga el {100 - rate} % del precio: {price} × "
        f"{100 - rate} / 100."
    )
    return _Case(stem, _eur, wrong, why, {"kind": "discount", "price": price, "rate": rate}, lambda w: w < p)


def _increase(rng: random.Random, level: int) -> _Case:
    price = rng.choice([30, 48, 64, 85, 120, 250, 36])
    rate = rng.choice([4, 6, 10, 12, 15, 21, 25])
    stem = f"El precio de un artículo es de {price} € y sube un {rate} %. ¿Cuál es su nuevo precio?"
    p, r = Fraction(price), Fraction(rate, 100)
    wrong = [p * (1 - r), p * (1 + r) - 1, p * (1 + r) + 2, p + r * 100]
    why = f"El nuevo precio es el {100 + rate} % del anterior: {price} × {100 + rate} / 100."
    return _Case(stem, _eur, wrong, why, {"kind": "increase", "price": price, "rate": rate}, lambda w: w > p)


def _of_quantity(rng: random.Random, level: int) -> _Case:
    total = rng.choice([240, 360, 480, 520, 640, 1200, 840])
    rate = rng.choice([15, 20, 35, 40, 45, 60, 25])
    stem = (
        f"En una unidad administrativa trabajan {total} personas y el {rate} % lo hace en horario de tarde. "
        "¿Cuántas personas trabajan por la tarde?"
    )
    t, r = Fraction(total), Fraction(rate, 100)
    wrong = [t * (1 - r), t * r + 10, t * r - 10, t * r + 20]
    why = f"Se calcula el {rate} % de {total}: {total} × {rate} / 100."
    return _Case(stem, _count, wrong, why, {"kind": "of-quantity", "total": total, "rate": rate})


def _share(rng: random.Random, level: int) -> _Case:
    total = rng.choice([80, 120, 150, 240, 360, 75, 90])
    part = rng.randint(total // 6, total // 2)
    stem = (
        f"De {total} solicitudes recibidas se han resuelto {part}. ¿Qué porcentaje de solicitudes se "
        f"ha resuelto?"
    )
    t, a = Fraction(total), Fraction(part)
    wrong = [(t - a) / t * 100, a / (t - a) * 100, a / t * 100 + 5, a / t * 100 - 5]
    why = f"El porcentaje es {part} / {total} × 100."
    return _Case(stem, _pct, wrong, why, {"kind": "share", "total": total, "part": part})


def _complement(rng: random.Random, level: int) -> _Case:
    total = rng.choice([120, 150, 180, 240, 300, 64])
    part = rng.randint(total // 5, total * 3 // 5)
    stem = (
        f"En un curso hay {total} alumnos y {part} de ellos son mujeres. "
        "¿Qué porcentaje del total no son mujeres?"
    )
    t, a = Fraction(total), Fraction(part)
    wrong = [a / t * 100, (t - a) / a * 100, (t - a) / t * 100 + 4, (t - a) / t * 100 - 4]
    why = f"No son mujeres {total} − {part} alumnos; ({total} − {part}) / {total} × 100."
    return _Case(stem, _pct, wrong, why, {"kind": "complement", "total": total, "part": part})


def _probability(rng: random.Random, level: int) -> _Case:
    red, blue, green = rng.randint(2, 9), rng.randint(2, 9), rng.randint(2, 9)
    stem = (
        f"En una urna hay {red} bolas rojas, {blue} azules y {green} verdes. "
        "Si se extrae una al azar, ¿qué probabilidad, en porcentaje, hay de que sea azul?"
    )
    total = Fraction(red + blue + green)
    wrong = [Fraction(blue, red + green) * 100, Fraction(red + green) / total * 100]
    wrong.append(Fraction(blue, red + blue) * 100)
    wrong.append(Fraction(blue, 10) * 10)
    why = (
        f"Casos favorables {blue} entre casos posibles {red + blue + green}: {blue} / "
        f"{red + blue + green} × 100."
    )
    return _Case(stem, _pct, wrong, why, {"kind": "probability", "red": red, "blue": blue, "green": green})


def _remainder(rng: random.Random, level: int) -> _Case:
    budget = rng.choice([4500, 7200, 12000, 8400, 25000, 36000])
    rate = rng.choice([15, 35, 42, 55, 64, 28])
    stem = (
        f"De un presupuesto de {number(budget)} € se ha gastado el {rate} %. ¿Cuántos euros quedan "
        f"por gastar?"
    )
    b, r = Fraction(budget), Fraction(rate, 100)
    wrong = [b * r, b * (1 - r) + 100, b * (1 - r) - 100, b * (1 - r) + 250]
    why = f"Queda el {100 - rate} % del presupuesto: {number(budget)} × {100 - rate} / 100."
    return _Case(stem, _eur, wrong, why, {"kind": "remainder", "budget": budget, "rate": rate})


def _discount_then_increase(rng: random.Random, level: int) -> _Case:
    price = rng.choice([1250, 2400, 3600, 18500, 47000])
    down, up = rng.choice([10, 15, 20, 25]), rng.choice([5, 8, 12, 20])
    stem = (
        f"Un equipo informático cuesta {number(price)} €. Se le aplica un descuento del {down} % y, "
        f"sobre el precio resultante, un recargo de envío del {up} %. ¿Cuánto se paga en total?"
    )
    p = Fraction(price)
    wrong = [p * (1 - Fraction(down - up, 100)), p * (1 - Fraction(down, 100)) + p * Fraction(up, 100)]
    wrong += [p * (1 + Fraction(up, 100)) * (1 - Fraction(down, 100)) + 10]
    wrong += [p * (1 - Fraction(down, 100))]
    why = (
        f"Tras el descuento se paga el {100 - down} % ({number(price)} × {100 - down} / 100) "
        f"y a eso se le suma el {up} %: × {100 + up} / 100."
    )
    return _Case(stem, _eur, wrong, why, {"kind": "two-step", "price": price, "down": down, "up": up})


_BY_LEVEL: dict[int, list[Callable[[random.Random, int], _Case]]] = {
    1: [_discount, _increase, _of_quantity, _share],
    2: [_complement, _probability, _remainder],
    3: [_discount_then_increase, _remainder, _complement],
}


def _value(facts: Mapping[str, object]) -> tuple[Fraction, Render]:
    def n(name: str) -> int:
        return int_fact(facts, name)

    kind = str_fact(facts, "kind")
    if kind == "discount":
        return Fraction(n("price") * (100 - n("rate")), 100), _eur
    if kind == "increase":
        return Fraction(n("price") * (100 + n("rate")), 100), _eur
    if kind == "of-quantity":
        return Fraction(n("total") * n("rate"), 100), _count
    if kind == "share":
        return Fraction(n("part") * 100, n("total")), _pct
    if kind == "complement":
        return Fraction((n("total") - n("part")) * 100, n("total")), _pct
    if kind == "probability":
        return Fraction(n("blue") * 100, n("red") + n("blue") + n("green")), _pct
    if kind == "remainder":
        return Fraction(n("budget") * (100 - n("rate")), 100), _eur
    if kind == "two-step":
        after = Fraction(n("price") * (100 - n("down")), 100)
        return after * (100 + n("up")) / 100, _eur
    raise UnsolvableItem(f"unknown kind {kind!r}")


class PorcentajesGenerator(ItemGenerator):
    id: ClassVar[str] = "calculo-porcentajes"

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        for _ in range(200):
            case = rng.choice(_BY_LEVEL[params.difficulty])(rng, params.difficulty)
            value, render = _value(case.facts)
            key = render(value)
            decimals = 0 if render is _count else 2
            cap = Fraction(100) if render is _pct else None
            if render is _count and value.denominator != 1:
                continue
            candidates = [
                w for w in pick_wrong(rng, value, case.wrong, cap=cap) if w in case.wrong or case.plausible(w)
            ]
            wrong = [render(round_half_up(w, decimals)) for w in candidates]
            unique = [w for w in dict.fromkeys(wrong) if w != key]
            if len(unique) < 3:
                continue
            options, slot = deal(rng, key, unique[:6])
            return Item(
                generator=self.id,
                seed=seed,
                difficulty=params.difficulty,
                stem=case.stem,
                options=options,
                key=slot,
                explanation=case.why + f" Resultado: {key}.",
                facts=case.facts,
            )
        raise RuntimeError(f"no percentage item for seed {seed}")

    def solve(self, item: Item) -> int:
        value, render = _value(item.facts)
        expected = render(value)
        hits = [i for i, option in enumerate(item.options) if option == expected]
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options read {expected}")
        return hits[0]

    def check_extra(self, item: Item) -> list[str]:
        value, _ = _value(item.facts)
        problems: list[str] = []
        for option in item.options:
            amount = Fraction(option.replace(".", "").replace(",", ".").split()[0])
            if not value / 3 <= abs(amount) <= value * 3:
                problems.append(f"option {option} is far from the key")
            if option.endswith("%") and abs(amount) > 100:
                problems.append(f"option {option} is a percentage above 100")
        return problems
