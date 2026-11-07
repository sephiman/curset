# SPDX-License-Identifier: AGPL-3.0-only
"""`administrativo-clasificacion`: cabinet and drawer, drawer by surname range, shelf by topic."""

from __future__ import annotations

import random
import re
from itertools import pairwise
from typing import ClassVar

from tradeschool.psicotecnico.contract import ItemGenerator, UnsolvableItem, deal
from tradeschool.psicotecnico.item import Item, Params, Table
from tradeschool.psicotecnico.spanish import spanish_key

_MATERIALS = (
    ("tela", "rollo", ("Batista", "Tweed", "Gabardina", "Lino", "Franela", "Crepé", "Encaje", "Raso")),
    (
        "cuerda",
        "rollo",
        ("Esparto", "Nailon", "Cáñamo", "Yute", "Sisal", "Algodón", "Poliéster", "Polipropileno"),
    ),
)
_SIZES = ((10, "A"), (15, "B"), (25, "C"))
_SURNAMES = (
    "Abad",
    "Aguirre",
    "Alonso",
    "Álvarez",
    "Aranda",
    "Barrios",
    "Benítez",
    "Blanco",
    "Bravo",
    "Cabrera",
    "Calvo",
    "Campos",
    "Cano",
    "Castro",
    "Cortés",
    "Crespo",
    "Delgado",
    "Díaz",
    "Domínguez",
    "Durán",
    "Escudero",
    "Espinosa",
    "Fernández",
    "Ferrer",
    "Flores",
    "Fuentes",
    "Gallego",
    "García",
    "Gil",
    "Gómez",
    "Guerrero",
    "Herrera",
    "Hidalgo",
    "Ibáñez",
    "Iglesias",
    "Jiménez",
    "Jover",
    "Lara",
    "León",
    "López",
    "Lozano",
    "Marín",
    "Mateos",
    "Molina",
    "Moreno",
    "Navarro",
    "Nieto",
    "Ortega",
    "Ortiz",
    "Pardo",
    "Peña",
    "Prieto",
    "Quintero",
    "Ramos",
    "Rey",
    "Rojas",
    "Romero",
    "Ruiz",
    "Salas",
    "Santos",
    "Serrano",
    "Soto",
    "Torres",
    "Ureña",
    "Valdés",
    "Vega",
    "Vidal",
    "Zamora",
)
_TOPICS = (
    ("Historia", "H"),
    ("Ciencia", "C"),
    ("Derecho", "D"),
    ("Arte", "A"),
    ("Novela", "N"),
    ("Viajes", "V"),
)
_TITLES = {
    "Historia": (
        "Roma imperial",
        "La Edad Media",
        "Guerra civil",
        "Átomos de guerra",
        "Cartas de Indias",
        "El siglo XX",
        "Reyes y reinos",
    ),
    "Ciencia": (
        "Astronomía hoy",
        "Biología marina",
        "Química básica",
        "Átomo y energía",
        "Geología",
        "Física para todos",
        "Matemáticas",
    ),
    "Derecho": (
        "Código civil",
        "Derecho penal",
        "Contratos",
        "Administración y ley",
        "Procesal",
        "Mercantil",
        "Constitución",
    ),
    "Arte": ("Barroco", "Pintura moderna", "Escultura", "Arquitectura", "Cine mudo", "Fotografía", "Grabado"),
    "Novela": (
        "La colmena",
        "Cien noches",
        "El bosque",
        "Ruido de fondo",
        "Las olas",
        "Tierra baja",
        "Mar abierto",
    ),
    "Viajes": (
        "Camino de Santiago",
        "Rutas del norte",
        "Islas",
        "Por el Danubio",
        "Costa norte",
        "Trenes",
        "Selvas",
    ),
}


def _cabinet(rng: random.Random) -> dict[str, object]:
    kind, thing, names = rng.choice(_MATERIALS)
    chosen = rng.sample(names, rng.randint(6, 8))
    return {
        "kind": "cabinet",
        "material": kind,
        "thing": thing,
        "names": chosen,
        "name": rng.choice(chosen),
        "size": rng.choice(_SIZES)[0],
    }


def _ranges(rng: random.Random, level_bound: bool) -> dict[str, object]:
    ordered = sorted(_SURNAMES, key=spanish_key)
    cut = sorted(rng.sample(range(8, len(ordered) - 8), 5))
    while any(b - a < 3 for a, b in pairwise([-1, *cut, len(ordered) - 1])):  # 3+ surnames per drawer
        cut = sorted(rng.sample(range(8, len(ordered) - 8), 5))
    bounds: list[list[str]] = []
    start = 0
    for end in [*cut, len(ordered) - 1]:
        bounds.append([ordered[start], ordered[end]])
        start = end + 1
    interior = [
        name for lo, hi in bounds for name in ordered if spanish_key(lo) < spanish_key(name) < spanish_key(hi)
    ]
    return {"kind": "ranges", "bounds": bounds, "name": rng.choice(interior)}


def _shelves(rng: random.Random) -> dict[str, object]:
    topics = rng.sample(_TOPICS, 3)
    rows = []
    shelf = 1
    for topic, _ in topics:
        for lo, hi in (("A", "H"), ("I", "P"), ("Q", "Z")):
            rows.append([topic, f"{lo}–{hi}", str(shelf)])
            shelf += 1
    topic = rng.choice(topics)[0]
    title = rng.choice(_TITLES[topic])
    return {"kind": "shelves", "rows": rows, "topic": topic, "title": title}


def _drawer(facts: dict[str, object]) -> str:
    names = facts["names"]
    assert isinstance(names, list)
    size = facts["size"]
    letter = next(code for metres, code in _SIZES if metres == size)
    return f"{names.index(facts['name']) + 1}{letter}"


def _range_index(bounds: list[list[str]], name: str) -> int:
    for i, (lo, hi) in enumerate(bounds):
        if spanish_key(lo) <= spanish_key(name) <= spanish_key(hi):
            return i
    raise UnsolvableItem(f"{name} is in no range")


def _shelf(rows: list[list[str]], topic: str, title: str) -> str:
    initial = spanish_key(title)[0].upper()
    for t, span, shelf in rows:
        lo, hi = span.split("–")
        if t == topic and lo <= initial <= hi:
            return shelf
    raise UnsolvableItem(f"no shelf for {title}")


class ClasificacionGenerator(ItemGenerator):
    id: ClassVar[str] = "administrativo-clasificacion"

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        build = {1: self._cabinet_item, 2: self._ranges_item, 3: self._shelf_item}[params.difficulty]
        return build(rng, seed, params.difficulty)

    def _make(
        self,
        rng: random.Random,
        seed: int,
        level: int,
        stem: str,
        key: str,
        wrong: list[str],
        why: str,
        facts: dict[str, object],
        table: Table | None = None,
    ) -> Item:
        unique = [w for w in dict.fromkeys(wrong) if w != key]
        options, slot = deal(rng, key, unique[:6])
        return Item(self.id, seed, level, stem, options, slot, why, table, facts)

    def _cabinet_item(self, rng: random.Random, seed: int, level: int) -> Item:
        facts = _cabinet(rng)
        names = facts["names"]
        assert isinstance(names, list)
        listing = ", ".join(f"{n} en el número {i + 1}" for i, n in enumerate(names))
        sizes = ", ".join(f"el cajón {code} para {metres} metros" for metres, code in _SIZES)
        stem = (
            f"En un almacén guardan cada tipo de {facts['material']} en un armario: {listing}. Cada armario "
            f"tiene tres cajones para los distintos tamaños de {facts['thing']}s: {sizes}. "
            f"¿En qué ubicación guardarán un {facts['thing']} de {facts['size']} metros de {facts['name']}?"
        )
        key = _drawer(facts)
        number = names.index(facts["name"]) + 1
        letters = [code for _, code in _SIZES]
        letter = key[-1]
        wrong = [f"{number}{x}" for x in letters if x != letter]
        wrong += [f"{n}{letter}" for n in (number - 1, number + 1) if 1 <= n <= len(names)]
        rng.shuffle(wrong)
        why = (
            f"{facts['name']} está en el armario {number} y {facts['size']} metros van al cajón "
            f"{letter}: {key}."
        )
        return self._make(rng, seed, level, stem, key, wrong, why, facts)

    def _ranges_item(self, rng: random.Random, seed: int, level: int) -> Item:
        facts = _ranges(rng, True)
        bounds = facts["bounds"]
        assert isinstance(bounds, list)
        listing = "; ".join(f"cajón {i + 1}: de {lo} a {hi}" for i, (lo, hi) in enumerate(bounds))
        stem = (
            f"Un archivo ordena los expedientes por apellido en seis cajones: {listing}. "
            f"¿En qué cajón se archivará el expediente de {facts['name']}?"
        )
        index = _range_index(bounds, str(facts["name"]))
        key = f"Cajón {index + 1}."
        others = [n for n in range(6) if n != index]
        rng.shuffle(others)
        wrong = [f"Cajón {n + 1}." for n in sorted(others, key=lambda n: abs(n - index))[:2] + others[:3]]
        why = (
            f"Por orden alfabético, {facts['name']} queda entre {bounds[index][0]} y "
            f"{bounds[index][1]}: cajón {index + 1}."
        )
        return self._make(rng, seed, level, stem, key, wrong, why, facts)

    def _shelf_item(self, rng: random.Random, seed: int, level: int) -> Item:
        facts = _shelves(rng)
        rows = facts["rows"]
        assert isinstance(rows, list)
        table = Table(
            "Biblioteca", ("Tema", "Inicial del título", "Estantería"), tuple(tuple(r) for r in rows)
        )
        stem = (
            "Según la tabla de clasificación llamada Biblioteca, que ordena los libros por tema y por "
            "inicial "
            f"del título, ¿en qué estantería se colocará el libro «{facts['title']}» del tema "
            f"{facts['topic']}?"
        )
        key = f"Estantería {_shelf(rows, str(facts['topic']), str(facts['title']))}."
        number = int(key.split()[1].rstrip("."))
        near = [n for n in range(1, 10) if n != number]
        rng.shuffle(near)
        wrong = [f"Estantería {n}." for n in near]
        why = (
            f"El tema es {facts['topic']} y el título empieza por "
            f"{spanish_key(str(facts['title']))[0].upper()}: {key[:-1].lower()}."
        )
        return self._make(rng, seed, level, stem, key, wrong, why, facts, table)

    def solve(self, item: Item) -> int:
        kind = item.facts["kind"]
        if kind == "cabinet":
            matches = re.findall(r"([A-ZÁÉÍÓÚa-záéíóúñ]+) en el número (\d+)", item.stem)
            sizes = {
                int(m): letter for letter, m in re.findall(r"el cajón ([A-Z]) para (\d+) metros", item.stem)
            }
            ask = re.search(r"de (\d+) metros de (.+)\?$", item.stem)
            if ask is None:
                raise UnsolvableItem("cannot read the question")
            cabinet = next(num for name, num in matches if name == ask.group(2))
            expected = f"{cabinet}{sizes[int(ask.group(1))]}"
        elif kind == "ranges":
            bounds = [(lo, hi) for lo, hi in re.findall(r"cajón \d+: de (\S+) a (\S+?)(?:;|\. )", item.stem)]
            name = re.search(r"expediente de (\S+)\?$", item.stem)
            if name is None or len(bounds) != 6:
                raise UnsolvableItem("cannot read the ranges")
            expected = f"Cajón {_range_index([list(b) for b in bounds], name.group(1)) + 1}."
        else:
            if item.table is None:
                raise UnsolvableItem("no table")
            ask = re.search(r"«([^»]+)» del tema (\w+)\?$", item.stem)
            if ask is None:
                raise UnsolvableItem("cannot read the question")
            expected = f"Estantería {_shelf([list(r) for r in item.table.rows], ask.group(2), ask.group(1))}."
        hits = [i for i, o in enumerate(item.options) if o == expected]
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options read {expected}")
        return hits[0]
