# SPDX-License-Identifier: AGPL-3.0-only
"""`administrativo-ordenacion`: the alphabetical order of four or five words that share a prefix."""

from __future__ import annotations

import random
import unicodedata
from itertools import pairwise
from typing import ClassVar

from tradeschool.psicotecnico.contract import ItemGenerator, UnsolvableItem, deal
from tradeschool.psicotecnico.item import Item, Params
from tradeschool.psicotecnico.spanish import spanish_key

FAMILIES: tuple[tuple[str, ...], ...] = (
    (
        "consejo",
        "consenso",
        "consentir",
        "conserje",
        "conserva",
        "consigna",
        "consistorio",
        "consola",
        "constante",
        "constar",
        "construir",
        "consuelo",
        "consumo",
    ),
    (
        "preámbulo",
        "precepto",
        "precio",
        "precipicio",
        "precisar",
        "predecir",
        "predominio",
        "preferir",
        "pregón",
        "pregunta",
        "prejuicio",
        "premio",
        "prenda",
        "prensa",
        "preparar",
    ),
    (
        "trabajo",
        "trabar",
        "tracción",
        "tractor",
        "tradición",
        "traducir",
        "traer",
        "tráfico",
        "tragar",
        "traición",
        "traje",
        "trama",
        "tramo",
        "trampa",
        "tranquilo",
        "transporte",
        "trastorno",
        "tratado",
        "trato",
    ),
    (
        "archivo",
        "arcilla",
        "arco",
        "arder",
        "ardilla",
        "arduo",
        "área",
        "arena",
        "argolla",
        "argumento",
        "aritmética",
        "armario",
        "armonía",
        "aroma",
        "arqueología",
        "arrabal",
        "arrancar",
        "arreglo",
        "arriba",
        "arroz",
    ),
    (
        "comisión",
        "comité",
        "cómodo",
        "compañía",
        "comparar",
        "compás",
        "compasión",
        "competir",
        "complejo",
        "completo",
        "componer",
        "comprar",
        "comprobar",
        "comunicar",
        "comunidad",
    ),
    (
        "expediente",
        "experiencia",
        "experto",
        "explicar",
        "exponer",
        "exportar",
        "expreso",
        "exprimir",
        "expulsar",
        "exquisito",
        "extender",
        "exterior",
        "extintor",
        "extraer",
        "extraño",
    ),
    (
        "balanza",
        "balcón",
        "baldosa",
        "ballena",
        "bambú",
        "banco",
        "banda",
        "bandera",
        "bandeja",
        "bandido",
        "banquete",
        "bañera",
        "barato",
        "barba",
        "barca",
        "barco",
        "barniz",
        "barrio",
    ),
    (
        "senda",
        "sendero",
        "sensato",
        "sensible",
        "sentar",
        "sentencia",
        "sentido",
        "sentir",
        "señal",
        "señor",
        "separar",
        "septiembre",
        "sequía",
        "serie",
        "serio",
        "servicio",
        "servir",
    ),
    (
        "monedero",
        "monitor",
        "monje",
        "mono",
        "monólogo",
        "monopolio",
        "montaña",
        "montar",
        "monte",
        "montón",
        "monumento",
        "moño",
        "moral",
        "morder",
        "moreno",
    ),
    (
        "gestión",
        "gesto",
        "gigante",
        "gimnasio",
        "girar",
        "giro",
        "gitano",
        "glaciar",
        "globo",
        "gloria",
        "glosario",
        "gobernar",
        "gobierno",
        "golfo",
        "golpe",
        "goma",
    ),
)


def _common_prefix(words: list[str]) -> int:
    keys = [spanish_key(w) for w in words]
    n = 0
    while all(len(k) > n and k[n] == keys[0][n] for k in keys):
        n += 1
    return n


def _fold(word: str) -> str:
    """The word as it is spelt for ordering: accents dropped, ñ kept as a letter of its own."""
    marked = unicodedata.normalize("NFD", word.casefold().replace("ñ", "\x00"))
    return "".join(c for c in marked if unicodedata.category(c) != "Mn").replace("\x00", "ñ")


def _split_at(a: str, b: str) -> int:
    return next((i for i, (x, y) in enumerate(zip(a, b, strict=False)) if x != y), min(len(a), len(b)))


def _explanation(ordered: list[str]) -> str:
    folded = [_fold(w) for w in ordered]
    prefix = min(_split_at(a, b) for a, b in pairwise(folded))
    steps: list[str] = []
    for (a, b), (fa, fb) in zip(pairwise(ordered), pairwise(folded), strict=True):
        at = _split_at(fa, fb)
        letters = f"{fa[at]} y {fb[at]}" if at < len(fa) else f"{fa} termina antes"
        place = f"la {at + 1}.ª letra" if not steps else f"la {at + 1}.ª"
        steps.append(f"{a} va antes que {b} por {place} ({letters})")
    return (
        f"Todas empiezan por «{folded[0][:prefix]}» y se ordenan por la primera letra distinta: "
        f"{', '.join(steps)}."
    )


def _line(words: list[str]) -> str:
    return ", ".join(words) + "."


def _variants(rng: random.Random, ordered: list[str]) -> list[list[str]]:
    """Orders that differ from the right one by a swap or two: the slips of reading the wrong letter."""
    out: list[list[str]] = []
    for _ in range(60):
        order = list(ordered)
        for _ in range(rng.choice([1, 1, 2])):
            i = rng.randrange(len(order) - 1)
            order[i], order[i + 1] = order[i + 1], order[i]
        if order != ordered and order not in out:
            out.append(order)
    return out


class OrdenacionGenerator(ItemGenerator):
    id: ClassVar[str] = "administrativo-ordenacion"
    levels: ClassVar[tuple[int, ...]] = (1, 2)

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        count = 4 if params.difficulty == 1 else 5
        for _ in range(500):
            family = rng.choice(FAMILIES)
            words = rng.sample(family, count)
            ordered = sorted(words, key=spanish_key)
            prefix = _common_prefix(words)
            if (
                prefix < 2
                or (params.difficulty == 1 and prefix != 2)
                or (params.difficulty == 2 and prefix < 3)
            ):
                continue
            wrong = _variants(rng, ordered)
            if len(wrong) < 3:
                continue
            shown = list(words)
            rng.shuffle(shown)
            options, slot = deal(rng, _line(ordered), [_line(w) for w in wrong[:6]])
            return Item(
                generator=self.id,
                seed=seed,
                difficulty=params.difficulty,
                stem="¿Qué serie indica el orden alfabético correcto de las siguientes palabras?",
                options=options,
                key=slot,
                explanation=_explanation(ordered),
                facts={"words": sorted(words)},
            )
        raise RuntimeError(f"no ordering for seed {seed}")

    def solve(self, item: Item) -> int:
        lists = [[w.strip() for w in option.rstrip(".").split(",")] for option in item.options]
        if any(sorted(each) != sorted(lists[0]) for each in lists):
            raise UnsolvableItem("the options do not hold the same words")
        right = sorted(lists[0], key=spanish_key)
        hits = [i for i, each in enumerate(lists) if each == right]
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options are in alphabetical order")
        return hits[0]
