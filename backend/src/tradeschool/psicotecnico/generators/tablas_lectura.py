# SPDX-License-Identifier: AGPL-3.0-only
"""`tablas-lectura`: nine question kinds over a generated table; the solver re-reads the printed cells."""

from __future__ import annotations

import random
import re
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction
from typing import ClassVar, cast

from tradeschool.psicotecnico.contract import ItemGenerator, UnsolvableItem, deal, pick_wrong
from tradeschool.psicotecnico.item import Item, Params, Table
from tradeschool.psicotecnico.spanish import number, percent, round_half_up


@dataclass(frozen=True)
class NumCol:
    header: str
    low: int
    high: int
    decimals: int = 0
    additive: bool = True  # a total of the column means something (not a year, an age, a unit price)


@dataclass(frozen=True)
class CatCol:
    header: str
    values: tuple[str, ...]


Cells = dict[str, Fraction]
Derive = Callable[[random.Random, Mapping[str, str], Cells], Cells]


def _travel(rng: random.Random, cats: Mapping[str, str], nums: Cells) -> Cells:
    """Time and cost follow from the distance and the means of transport, as on a real expense sheet."""
    kmh, per_km = {
        "Tren": ((100, 220), (8, 18)),
        "Avión": ((300, 650), (10, 25)),
        "Coche": ((70, 110), (20, 30)),
        "Autobús": ((60, 90), (5, 10)),
    }[cats["Medio"]]
    km = max(nums["Distancia (km)"], Fraction(350)) if cats["Medio"] == "Avión" else nums["Distancia (km)"]
    minutes = round(km * 60 / rng.randint(*kmh))
    cost = round(km * rng.randint(*per_km) / 100)
    return {
        **nums,
        "Distancia (km)": km,
        "Tiempo (min)": Fraction(minutes),
        "Coste (€)": Fraction(max(cost, 5)),
    }


@dataclass(frozen=True)
class Theme:
    title: str
    singular: str
    plural: str
    label_header: str
    labels: tuple[str, ...]
    cats: tuple[CatCol, ...]
    nums: tuple[NumCol, ...]
    ratios: tuple[tuple[str, str], ...]  # (numerator, denominator) headers whose quotient means something
    derive: Derive | None = None


_NAMES = (
    "Marta Ríos",
    "Luis Parra",
    "Ana Cortés",
    "Pablo Vera",
    "Elena Soler",
    "Jorge Luna",
    "Irene Pons",
    "Raúl Mena",
    "Carla Nieto",
    "Hugo Beltrán",
    "Sara Ortiz",
    "Diego Rubio",
    "Lucía Costa",
    "Iván Duarte",
    "Nuria Salas",
    "Óscar Lara",
    "Paula Giner",
    "Andrés Peña",
    "Rocío Mora",
    "Víctor Ibarra",
)
_BOOKS = (
    "Aranmanoth",
    "Contra vosotros",
    "Mano de sombra",
    "Adiós a las novias",
    "La temporada de caza",
    "El equipaje del viajero",
    "El amante lesbiano",
    "Entre visillos",
    "Un calor tan cercano",
    "Hija de la fortuna",
    "La casa del lago",
    "Noches de invierno",
    "El último tren",
    "Cuaderno de bitácora",
    "La isla vacía",
    "Los días azules",
    "Tiempo de ceniza",
    "El jardín cerrado",
)
_CITIES = (
    "Madrid",
    "Barcelona",
    "Valencia",
    "Sevilla",
    "Bilbao",
    "Zaragoza",
    "Málaga",
    "Granada",
    "Burgos",
    "Vigo",
)
_PLACES = (
    "Toledo",
    "Segovia",
    "Cuenca",
    "Ávila",
    "Soria",
    "León",
    "Mérida",
    "Teruel",
    "Úbeda",
    "Ronda",
    "Jaca",
    "Lugo",
)
_LABS = (
    "Alfa",
    "Beta",
    "Gamma",
    "Delta",
    "Épsilon",
    "Sigma",
    "Omega",
    "Kappa",
    "Lambda",
    "Zeta",
    "Theta",
    "Iota",
)

THEMES: tuple[Theme, ...] = (
    Theme(
        "Préstamos",
        "título",
        "títulos",
        "Título",
        _BOOKS,
        (
            CatCol("Lugar de edición", ("Madrid", "Barcelona", "Valencia", "Sevilla")),
            CatCol("Editorial", ("Destino", "Alfaguara", "Santillana", "Anagrama", "Planeta")),
        ),
        (
            NumCol("Año de publicación", 1995, 2005, additive=False),
            NumCol("Ejemplares disponibles", 3, 20),
            NumCol("Ejemplares prestados", 1, 9),
            NumCol("Préstamos realizados", 100, 350),
        ),
        (
            ("Préstamos realizados", "Ejemplares disponibles"),
            ("Ejemplares prestados", "Ejemplares disponibles"),
        ),
    ),
    Theme(
        "Academia",
        "alumno",
        "alumnos",
        "Alumno",
        _NAMES,
        (
            CatCol("Curso", ("Inglés", "Francés", "Alemán", "Informática")),
            CatCol("Turno", ("Mañana", "Tarde", "Noche")),
        ),
        (
            NumCol("Edad", 18, 55, additive=False),
            NumCol("Horas semanales", 2, 12),
            NumCol("Cuota mensual", 30, 120),
            NumCol("Faltas de asistencia", 0, 15),
        ),
        (("Cuota mensual", "Horas semanales"), ("Faltas de asistencia", "Horas semanales")),
    ),
    Theme(
        "Desplazamientos",
        "empleado",
        "empleados",
        "Empleado",
        _NAMES,
        (CatCol("Destino", _CITIES[:5]), CatCol("Medio", ("Tren", "Avión", "Coche", "Autobús"))),
        (
            NumCol("Distancia (km)", 80, 900),
            NumCol("Tiempo (min)", 60, 540),
            NumCol("Coste (€)", 20, 260),
            NumCol("Viajes al año", 1, 14),
        ),
        (("Coste (€)", "Distancia (km)"), ("Distancia (km)", "Tiempo (min)")),
        _travel,
    ),
    Theme(
        "Excursiones",
        "destino",
        "destinos",
        "Destino",
        _PLACES,
        (
            CatCol("Tipo", ("Cultural", "Deportiva", "Naturaleza", "Gastronómica")),
            CatCol("Transporte", ("Autobús", "Tren", "Minibús")),
        ),
        (
            NumCol("Participantes", 12, 60),
            NumCol("Precio por persona (€)", 15, 95, additive=False),
            NumCol("Duración (horas)", 4, 30),
            NumCol("Kilómetros", 40, 480),
        ),
        (("Precio por persona (€)", "Duración (horas)"), ("Kilómetros", "Duración (horas)")),
    ),
    Theme(
        "Laboratorios",
        "laboratorio",
        "laboratorios",
        "Laboratorio",
        _LABS,
        (CatCol("Ciudad", _CITIES[:5]), CatCol("Titularidad", ("Pública", "Privada", "Mixta"))),
        (
            NumCol("Muestras analizadas", 120, 980),
            NumCol("Técnicos", 3, 24),
            NumCol("Presupuesto (miles de €)", 40, 400),
            NumCol("Informes emitidos", 30, 300),
        ),
        (
            ("Muestras analizadas", "Técnicos"),
            ("Informes emitidos", "Técnicos"),
            ("Presupuesto (miles de €)", "Técnicos"),
        ),
    ),
)

# --- reading the printed cells --------------------------------------------------------------------


def parse_cell(text: str) -> Fraction:
    return Fraction(text.replace(".", "").replace(",", "."))


@dataclass(frozen=True)
class Grid:
    header: tuple[str, ...]
    kinds: tuple[str, ...]  # "label" | "cat" | "num"
    rows: tuple[tuple[str, ...], ...]

    def num(self, row: int, col: int) -> Fraction:
        return parse_cell(self.rows[row][col])

    def decimals(self, col: int) -> int:
        return max((len(r[col].split(",")[1]) if "," in r[col] else 0) for r in self.rows)


Condition = Mapping[str, object]
Query = Mapping[str, object]


def _passes(grid: Grid, row: int, cond: Condition) -> bool:
    col = int(cast(int, cond["col"]))
    value, op = str(cond["value"]), str(cond["op"])
    if op == "=":
        return grid.rows[row][col] == value
    amount, threshold = grid.num(row, col), parse_cell(value)
    return amount > threshold if op == ">" else amount < threshold


def _matching(grid: Grid, conds: Sequence[Condition]) -> list[int]:
    return [r for r in range(len(grid.rows)) if all(_passes(grid, r, c) for c in conds)]


def _unique_extreme(scores: Mapping[int | str, Fraction], extreme: str) -> int | str:
    best = max(scores.values()) if extreme == "max" else min(scores.values())
    holders = [k for k, v in scores.items() if v == best]
    if len(holders) != 1:
        raise UnsolvableItem(f"{len(holders)} rows tie for the {extreme}")
    return holders[0]


def _conds(query: Query) -> list[Condition]:
    return cast(list[Condition], query["conds"])


def _group_scores(grid: Grid, query: Query) -> dict[int | str, Fraction]:
    group, col = int(cast(int, query["group"])), int(cast(int, query["col"]))
    sums: dict[int | str, Fraction] = {}
    counts: dict[int | str, int] = {}
    for r in range(len(grid.rows)):
        key = grid.rows[r][group]
        sums[key] = sums.get(key, Fraction(0)) + grid.num(r, col)
        counts[key] = counts.get(key, 0) + 1
    if query["agg"] == "mean":
        return {k: sums[k] / counts[k] for k in sums}
    return dict(sums)


def answer_text(grid: Grid, query: Query) -> str:
    """The printed answer to a query over the printed cells; raises when the question has no single answer."""
    kind = str(query["kind"])
    if kind == "filter_name":
        rows = _matching(grid, _conds(query))
        if len(rows) != 1:
            raise UnsolvableItem(f"{len(rows)} rows pass the conditions")
        return grid.rows[rows[0]][0] + "."
    if kind == "filter_extreme":
        rows = _matching(grid, _conds(query))
        if len(rows) < 2:
            raise UnsolvableItem("fewer than two rows pass")
        col = int(cast(int, query["col"]))
        winner = _unique_extreme({r: grid.num(r, col) for r in rows}, str(query["extreme"]))
        return grid.rows[int(winner)][0] + "."
    if kind == "ratio_extreme":
        a, b = int(cast(int, query["num"])), int(cast(int, query["den"]))
        if any(grid.num(r, b) == 0 for r in range(len(grid.rows))):
            raise UnsolvableItem("a ratio divides by zero")
        winner = _unique_extreme(
            {r: grid.num(r, a) / grid.num(r, b) for r in range(len(grid.rows))}, str(query["extreme"])
        )
        return grid.rows[int(winner)][0] + "."
    if kind == "group_extreme":
        return str(_unique_extreme(_group_scores(grid, query), str(query["extreme"]))) + "."
    if kind == "count":
        return number(len(_matching(grid, _conds(query))))
    if kind == "filter_sum":
        col = int(cast(int, query["col"]))
        total = sum((grid.num(r, col) for r in _matching(grid, _conds(query))), Fraction(0))
        return number(total, grid.decimals(col))
    if kind == "share":
        group, col = int(cast(int, query["group"])), int(cast(int, query["col"]))
        part = sum(
            (grid.num(r, col) for r in range(len(grid.rows)) if grid.rows[r][group] == query["value"]),
            Fraction(0),
        )
        whole = sum((grid.num(r, col) for r in range(len(grid.rows))), Fraction(0))
        return percent(part / whole * 100)
    if kind == "column_mean":
        col = int(cast(int, query["col"]))
        return number(sum((grid.num(r, col) for r in range(len(grid.rows))), Fraction(0)) / len(grid.rows), 2)
    raise UnsolvableItem(f"unknown question kind {kind!r}")


# --- building a table -----------------------------------------------------------------------------


def _build(rng: random.Random, theme: Theme, rows: int) -> Grid:
    labels = rng.sample(theme.labels, rows)
    cats = [rng.choices(col.values, k=rows) for col in theme.cats]
    # Every value shows at least once, so a group question has all its groups.
    for col, picked in zip(theme.cats, cats, strict=True):
        for slot, value in zip(rng.sample(range(rows), min(len(col.values), rows)), col.values, strict=False):
            picked[slot] = value
    values: list[Cells] = []
    for r in range(rows):
        cells = {
            column.header: Fraction(
                rng.randint(column.low * 10**column.decimals, column.high * 10**column.decimals),
                10**column.decimals,
            )
            for column in theme.nums
        }
        if theme.derive is not None:
            cells = theme.derive(
                rng, {c.header: picked[r] for c, picked in zip(theme.cats, cats, strict=True)}, cells
            )
        values.append(cells)
    nums = [[number(values[r][column.header], column.decimals) for r in range(rows)] for column in theme.nums]
    header = (theme.label_header, *(c.header for c in theme.cats), *(c.header for c in theme.nums))
    kinds = ("label", *("cat" for _ in theme.cats), *("num" for _ in theme.nums))
    table_rows = tuple((labels[r], *(c[r] for c in cats), *(n[r] for n in nums)) for r in range(rows))
    return Grid(header, kinds, table_rows)


def _cols(grid: Grid, kind: str) -> list[int]:
    return [i for i, k in enumerate(grid.kinds) if k == kind]


def _additive(theme: Theme, grid: Grid) -> list[int]:
    return [grid.header.index(c.header) for c in theme.nums if c.additive]


def _condition_for(rng: random.Random, grid: Grid, row: int, col: int) -> dict[str, object]:
    if grid.kinds[col] == "cat":
        return {"col": col, "op": "=", "value": grid.rows[row][col]}
    target = grid.num(row, col)
    values = [grid.num(r, col) for r in range(len(grid.rows))]
    margin = Fraction(max(1, (max(values) - min(values)) // 8))
    below, above = target - margin, target + margin
    greater = rng.random() < 0.5
    if (greater and below < min(values)) or (not greater and above > max(values)):
        greater = not greater
    if greater:
        return {"col": col, "op": ">", "value": number(below, 0)}
    return {"col": col, "op": "<", "value": number(above, 0)}


def _random_conditions(rng: random.Random, grid: Grid, row: int, count: int) -> list[dict[str, object]]:
    columns = rng.sample(_cols(grid, "cat") + _cols(grid, "num"), count)
    return [_condition_for(rng, grid, row, c) for c in columns]


def _plain(header: str) -> str:
    """A column header as running text: lower case, without its unit in brackets."""
    return re.sub(r"\s*\(.*\)", "", header).lower()


def _cond_text(grid: Grid, cond: Condition) -> str:
    col = int(cast(int, cond["col"]))
    name = _plain(grid.header[col])
    if cond["op"] == "=":
        return f"{name} «{cond['value']}»"
    if name.split()[0].endswith("s"):  # a count: «más de 10 técnicos», not «técnicos superior a 10»
        return f"{'más' if cond['op'] == '>' else 'menos'} de {cond['value']} {name}"
    return f"{name} {'superior' if cond['op'] == '>' else 'inferior'} a {cond['value']}"


def _conditions(grid: Grid, conds: Sequence[Condition]) -> str:
    """«estas condiciones: a, b y c», cells quoted as printed: no value sits capitalised mid-sentence."""
    head = "esta condición" if len(conds) == 1 else "estas condiciones"
    return f"{head}: {_join([_cond_text(grid, c) for c in conds])}"


def _join(parts: Sequence[str]) -> str:
    return parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + " y " + parts[-1]


@dataclass(frozen=True)
class Built:
    query: dict[str, object]
    question: str
    wrong: list[str]
    why: str


def _near_rows(grid: Grid, conds: Sequence[Condition], answer: int) -> list[str]:
    """Rows that fail exactly one condition first: the plausible wrong picks."""
    scored = []
    for r in range(len(grid.rows)):
        if r == answer:
            continue
        failed = sum(1 for c in conds if not _passes(grid, r, c))
        scored.append((failed, r))
    scored.sort()
    return [grid.rows[r][0] + "." for _, r in scored]


def _q_filter_name(rng: random.Random, theme: Theme, grid: Grid, level: int) -> Built | None:
    k = {1: rng.choice([2, 3]), 2: rng.choice([3, 4]), 3: rng.choice([4, 5])}[level]
    row = rng.randrange(len(grid.rows))
    conds = _random_conditions(rng, grid, row, k)
    if _matching(grid, conds) != [row]:
        return None
    text = _join([_cond_text(grid, c) for c in conds])
    return Built(
        {"kind": "filter_name", "conds": conds},
        f"¿Cuál de los siguientes {theme.plural} cumple {_conditions(grid, conds)}?",
        _near_rows(grid, conds, row),
        f"Solo «{grid.rows[row][0]}» cumple las {k} condiciones: {text}.",
    )


def _q_filter_extreme(rng: random.Random, theme: Theme, grid: Grid, level: int) -> Built | None:
    k = {1: 1, 2: 2, 3: 3}[level]
    anchor = rng.randrange(len(grid.rows))
    conds = _random_conditions(rng, grid, anchor, k)
    rows = _matching(grid, conds)
    if not 3 <= len(rows) <= 6:
        return None
    col = rng.choice(_cols(grid, "num"))
    extreme = rng.choice(["max", "min"])
    query = {"kind": "filter_extreme", "conds": conds, "col": col, "extreme": extreme}
    try:
        winner = answer_text(grid, query)
    except UnsolvableItem:
        return None
    others = [
        grid.rows[r][0] + "."
        for r in sorted(rows, key=lambda r: grid.num(r, col), reverse=extreme == "max")
        if grid.rows[r][0] + "." != winner
    ]
    outside = [grid.rows[r][0] + "." for r in range(len(grid.rows)) if r not in rows]
    return Built(
        query,
        f"Entre los {theme.plural} que cumplen {_conditions(grid, conds)}, ¿cuál tiene el valor "
        f"{'más alto' if extreme == 'max' else 'más bajo'} de {_plain(grid.header[col])}?",
        others + outside,
        f"Pasan el filtro {len(rows)} {theme.plural}; entre ellos, «{winner[:-1]}» tiene el valor "
        f"{'más alto' if extreme == 'max' else 'más bajo'} de {_plain(grid.header[col])}.",
    )


def _q_ratio(rng: random.Random, theme: Theme, grid: Grid, level: int) -> Built | None:
    a, b = (grid.header.index(h) for h in rng.choice(theme.ratios))
    if any(grid.num(r, b) == 0 for r in range(len(grid.rows))):
        return None
    extreme = rng.choice(["max", "min"])
    ratios = sorted(
        ((grid.num(r, a) / grid.num(r, b), r) for r in range(len(grid.rows))), reverse=extreme == "max"
    )
    gap = {1: Fraction(1, 4), 2: Fraction(1, 12), 3: Fraction(1, 50)}[level]
    best, second = ratios[0][0], ratios[1][0]
    if best == second or abs(best - second) / best < gap:
        return None
    if level == 1 and abs(best - second) / best < Fraction(1, 6):
        return None
    word = "mayor" if extreme == "max" else "menor"
    winner = grid.rows[ratios[0][1]][0]
    return Built(
        {"kind": "ratio_extreme", "num": a, "den": b, "extreme": extreme},
        f"¿Qué {theme.singular} tiene el {word} cociente entre {_plain(grid.header[a])} y "
        f"{_plain(grid.header[b])}?",
        [grid.rows[r][0] + "." for _, r in ratios[1:]],
        f"Se divide {_plain(grid.header[a])} entre {_plain(grid.header[b])} en cada fila: el {word} cociente "
        f"es el de «{winner}» ({number(ratios[0][0], 2 if ratios[0][0] >= 1 else 3)}).",
    )


def _q_group(rng: random.Random, theme: Theme, grid: Grid, level: int) -> Built | None:
    group = rng.choice(_cols(grid, "cat"))
    agg = "sum" if level < 3 else rng.choice(["sum", "mean"])
    col = rng.choice(_additive(theme, grid) if agg == "sum" else _cols(grid, "num"))
    extreme = rng.choice(["max", "min"])
    query = {"kind": "group_extreme", "group": group, "col": col, "agg": agg, "extreme": extreme}
    scores = _group_scores(grid, query)
    if len(scores) < 4:
        return None
    ordered = sorted(scores.items(), key=lambda kv: kv[1], reverse=extreme == "max")
    if ordered[0][1] == ordered[1][1] or abs(ordered[0][1] - ordered[1][1]) / ordered[0][1] < Fraction(1, 30):
        return None
    word = "mayor" if extreme == "max" else "menor"
    name = _plain(grid.header[group])
    if agg == "sum":
        question = f"Sumando {_plain(grid.header[col])} por {name}, ¿qué {name} obtiene el {word} total?"
    else:
        question = (
            f"Calculando la media de {_plain(grid.header[col])} por {name}, ¿qué {name} obtiene "
            f"la {'mayor' if extreme == 'max' else 'menor'} media?"
        )
    return Built(
        query,
        question,
        [f"{k}." for k, _ in ordered[1:]],
        f"Los valores por {name} son "
        + ", ".join(f"{k} {number(v, 2 if agg == 'mean' else 0)}" for k, v in sorted(scores.items()))
        + f"; el {word} es {ordered[0][0]}.",
    )


def _q_count(rng: random.Random, theme: Theme, grid: Grid, level: int) -> Built | None:
    k = rng.choice([2, 3]) if level < 3 else rng.choice([3, 4])
    anchor = rng.randrange(len(grid.rows))
    conds = _random_conditions(rng, grid, anchor, k)
    total = len(_matching(grid, conds))
    if not 2 <= total <= 5:
        return None
    text = _join([_cond_text(grid, c) for c in conds])
    wrong = [str(total + d) for d in (1, -1, 2, -2, 3) if total + d >= 0]
    return Built(
        {"kind": "count", "conds": conds},
        f"¿Cuántos {theme.plural} cumplen {_conditions(grid, conds)}?",
        wrong,
        f"Cumplen las condiciones ({text}) exactamente {total}.",
    )


def _q_filter_sum(rng: random.Random, theme: Theme, grid: Grid, level: int) -> Built | None:
    k = 1 if level == 1 else 2
    anchor = rng.randrange(len(grid.rows))
    conds = _random_conditions(rng, grid, anchor, k)
    rows = _matching(grid, conds)
    if not (3 if level == 3 else 2) <= len(rows) <= (5 if level == 3 else 4):
        return None
    candidates = [c for c in _additive(theme, grid) if all(int(cast(int, cc["col"])) != c for cc in conds)]
    if not candidates:
        return None
    col = rng.choice(candidates)
    total = sum((grid.num(r, col) for r in rows), Fraction(0))
    decimals = grid.decimals(col)
    slips = [
        total - grid.num(rows[0], col),
        total + grid.num(next(r for r in range(len(grid.rows)) if r not in rows), col),
    ]
    wrong = [number(w, decimals) for w in pick_wrong(rng, total, slips) if w > 0]
    return Built(
        {"kind": "filter_sum", "conds": conds, "col": col},
        f"¿Cuál es el total de {_plain(grid.header[col])} de los {theme.plural} que cumplen "
        f"{_conditions(grid, conds)}?",
        wrong,
        f"Pasan el filtro {len(rows)} filas; en ellas, la columna «{grid.header[col]}» suma "
        f"{number(total, decimals)}.",
    )


def _q_share(rng: random.Random, theme: Theme, grid: Grid, level: int) -> Built | None:
    group = rng.choice(_cols(grid, "cat"))
    col = rng.choice(_additive(theme, grid))
    value = rng.choice(sorted({r[group] for r in grid.rows}))
    part = sum((grid.num(r, col) for r in range(len(grid.rows)) if grid.rows[r][group] == value), Fraction(0))
    whole = sum((grid.num(r, col) for r in range(len(grid.rows))), Fraction(0))
    share = part / whole * 100
    rest = (whole - part) / whole * 100
    slips = [
        rest,
        part / whole * 10 + 5,
        Fraction(sum(1 for r in grid.rows if r[group] == value), len(grid.rows)) * 100,
    ]
    wrong = [percent(round_half_up(w, 2)) for w in pick_wrong(rng, share, slips, cap=Fraction(100)) if w > 0]
    name = _plain(grid.header[group])
    return Built(
        {"kind": "share", "group": group, "value": value, "col": col},
        f"¿Qué porcentaje del total de {_plain(grid.header[col])} corresponde a los {theme.plural} con "
        f"{name} «{value}»?",
        wrong,
        f"Los {theme.plural} con {name} «{value}» suman {number(part, 0)} de un total de {number(whole, 0)}: "
        f"{percent(share)}.",
    )


def _q_mean(rng: random.Random, theme: Theme, grid: Grid, level: int) -> Built | None:
    col = rng.choice(_cols(grid, "num"))
    values = [grid.num(r, col) for r in range(len(grid.rows))]
    mean = sum(values, Fraction(0)) / len(values)
    if mean.denominator == 1 or round_half_up(mean, 2) == round_half_up(mean, 1):
        return None
    median = sorted(values)[len(values) // 2]
    slips = [
        median,
        sum(values, Fraction(0)) / (len(values) - 1),
        sum(values[:-1], Fraction(0)) / (len(values) - 1),
    ]
    wrong = [number(w, 2) for w in pick_wrong(rng, mean, slips) if w > 0]
    return Built(
        {"kind": "column_mean", "col": col},
        f"¿Cuál es la media de {_plain(grid.header[col])} de todos los {theme.plural}?",
        wrong,
        f"La suma de la columna es {number(sum(values, Fraction(0)), 2)} y hay {len(values)} filas: "
        f"{number(mean, 2)}.",
    )


Builder = Callable[[random.Random, Theme, Grid, int], Built | None]
_BY_LEVEL: dict[int, list[Builder]] = {
    1: [_q_filter_name, _q_filter_name, _q_filter_extreme, _q_count, _q_ratio],
    2: [_q_filter_extreme, _q_ratio, _q_group, _q_count, _q_filter_sum, _q_filter_name],
    3: [_q_ratio, _q_group, _q_share, _q_filter_name, _q_mean, _q_filter_sum, _q_filter_extreme],
}
_ROWS = {1: (7, 8), 2: (9, 10), 3: (11, 12)}


def _grid_of(item: Item) -> Grid:
    if item.table is None:
        raise UnsolvableItem("no table")
    kinds = item.facts["kinds"]
    assert isinstance(kinds, list)
    return Grid(item.table.header, tuple(str(k) for k in kinds), item.table.rows)


class TablasLecturaGenerator(ItemGenerator):
    id: ClassVar[str] = "tablas-lectura"

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        level = params.difficulty
        for _ in range(2000):
            theme = rng.choice(THEMES)
            grid = _build(rng, theme, rng.randint(*_ROWS[level]))
            try:
                built = rng.choice(_BY_LEVEL[level])(rng, theme, grid, level)
            except ZeroDivisionError:
                continue
            if built is None:
                continue
            try:
                key = answer_text(grid, built.query)
            except UnsolvableItem:
                continue
            wrong = [w for w in dict.fromkeys(built.wrong) if w != key]
            if len(wrong) < 3:
                continue
            options, slot = deal(rng, key, wrong[:6])
            return Item(
                generator=self.id,
                seed=seed,
                difficulty=level,
                stem=f"Responda a la siguiente pregunta según la tabla llamada {theme.title}: "
                f"{built.question}",
                options=options,
                key=slot,
                explanation=built.why,
                table=Table(theme.title, grid.header, grid.rows),
                facts={"query": built.query, "kinds": list(grid.kinds)},
            )
        raise RuntimeError(f"no table question for seed {seed}")

    def solve(self, item: Item) -> int:
        query = item.facts["query"]
        assert isinstance(query, dict)
        expected = answer_text(_grid_of(item), query)
        hits = [i for i, option in enumerate(item.options) if option == expected]
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options read {expected}")
        return hits[0]

    def check_extra(self, item: Item) -> list[str]:
        grid = _grid_of(item)
        problems = [] if len({r[0] for r in grid.rows}) == len(grid.rows) else ["duplicate row labels"]
        if item.options[0].endswith(".") != all(o.endswith(".") for o in item.options):
            problems.append("options mix forms")
        return problems
