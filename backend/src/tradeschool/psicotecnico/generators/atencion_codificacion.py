# SPDX-License-Identifier: AGPL-3.0-only
"""`atencion-codificacion`: binary blocks, digit words, letter-class values, the filing code."""

from __future__ import annotations

import random
import re
from typing import ClassVar

from tradeschool.psicotecnico.contract import ItemGenerator, UnsolvableItem, deal, str_fact
from tradeschool.psicotecnico.item import Item, Params, Table

_WORDS = (
    "cartera",
    "almacen",
    "archivo",
    "carpeta",
    "oficina",
    "registro",
    "informe",
    "tramite",
    "gestion",
    "mensaje",
    "factura",
    "formato",
    "ventana",
    "teclado",
    "sellado",
    "ordenar",
    "usuario",
    "decreto",
)
_VALUE_WORDS = (
    "Martinez",
    "Archivos",
    "Registro",
    "Gestion",
    "Informes",
    "Carmelo",
    "Sellado",
    "Oficina",
    "Tramites",
)
_CLASSES = (
    ("consonante mayúscula", True, False),
    ("consonante minúscula", False, False),
    ("vocal mayúscula", True, True),
    ("vocal minúscula", False, True),
)
_VOWELS = set("aeiou")
_DEPARTMENTS = ("Compras", "Ventas", "Personal", "Informática")
_FIELDS = (
    ("departamento", ("Compras", "Ventas", "Personal", "Informática")),
    ("sede", ("Norte", "Sur", "Este", "Oeste")),
    ("año", ("2021", "2022", "2023", "2024")),
    ("soporte", ("papel", "disco", "cinta", "nube")),
    ("urgencia", ("baja", "media", "alta", "máxima")),
    ("custodia", ("archivo", "oficina", "almacén", "sótano")),
)


def _letters(rng: random.Random, count: int) -> list[str]:
    return rng.sample("abcdefghijklmnopqrstuvwxyz"[:20], count)


def _binary(rng: random.Random) -> dict[str, object]:
    letters = rng.sample("abcdefg", 6)
    codes = rng.sample(["0001", "0010", "0100", "1000", "0011", "0101", "0110", "1001", "1010", "1100"], 6)
    table = dict(zip(letters, codes, strict=True))
    message = [rng.choice(letters) for _ in range(4)]
    return {"kind": "binary", "table": table, "message": message}


def _digits(rng: random.Random) -> dict[str, object]:
    word = rng.choice(_WORDS)
    chosen = sorted(set(rng.sample(sorted(set(word)), 4)))
    digits = rng.sample("123456789", len(chosen))
    return {"kind": "digits", "map": dict(zip(digits, chosen, strict=True)), "word": word}


def _values(rng: random.Random) -> dict[str, object]:
    values = rng.sample(range(1, 9), 4)
    word = rng.choice(_VALUE_WORDS)
    shown = "".join(c.upper() if rng.random() < 0.5 else c.lower() for c in word)
    return {"kind": "values", "values": values, "word": shown}


def _filing(rng: random.Random) -> dict[str, object]:
    fields = rng.sample(range(len(_FIELDS)), 4)
    code = [rng.randrange(4) for _ in fields]
    return {"kind": "filing", "fields": fields, "code": code, "asks": rng.choice(["FALSA", "CIERTA"])}


def _value_of(word: str, values: list[int]) -> int:
    total = 0
    for ch in word:
        vowel = ch.lower() in _VOWELS
        upper = ch.isupper()
        for index, (_, up, vow) in enumerate(_CLASSES):
            if up == upper and vow == vowel:
                total += values[index]
    return total


def _decode_binary(table: dict[str, str], blocks: list[str]) -> str:
    inverse = {code: letter for letter, code in table.items()}
    return "".join(inverse[block] for block in blocks)


class CodificacionGenerator(ItemGenerator):
    id: ClassVar[str] = "atencion-codificacion"
    levels: ClassVar[tuple[int, ...]] = (1, 2)

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        builders = {1: (self._binary_item, self._digits_item), 2: (self._values_item, self._filing_item)}
        return rng.choice(builders[params.difficulty])(rng, seed, params.difficulty)

    def _item(
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
        if len(unique) < 3:
            raise RuntimeError("not enough distractors")
        options, slot = deal(rng, key, unique[:6])
        return Item(self.id, seed, level, stem, options, slot, why, table, facts)

    def _binary_item(self, rng: random.Random, seed: int, level: int) -> Item:
        for _ in range(100):
            facts = _binary(rng)
            table = facts["table"]
            message = facts["message"]
            assert isinstance(table, dict) and isinstance(message, list)
            blocks = [table[ch] for ch in message]
            key = "".join(message)
            wrong: list[str] = []
            for _ in range(40):
                variant = list(message)
                for pos in rng.sample(range(4), rng.choice([1, 2])):
                    near = [
                        letter
                        for letter, code in table.items()
                        if letter != variant[pos]
                        and sum(a != b for a, b in zip(code, table[variant[pos]], strict=True)) <= 2
                    ]
                    if near:
                        variant[pos] = rng.choice(near)
                text = "".join(variant)
                if text != key:
                    wrong.append(text)
            if len(set(wrong)) < 3:
                continue
            eq = ", ".join(f"{letter}={code}" for letter, code in table.items())
            stem = (
                f"Dadas las siguientes equivalencias: {eq} ¿Qué serie de letras corresponde a la siguiente "
                f"serie de números?: {''.join(blocks)}"
            )
            why = (
                "Se separan bloques de cuatro cifras ("
                + " ".join(blocks)
                + ") y se busca cada uno en la tabla: "
                + key
                + "."
            )
            return self._item(rng, seed, level, stem, key, wrong, why, facts)
        raise RuntimeError("no binary item")

    def _digits_item(self, rng: random.Random, seed: int, level: int) -> Item:
        for _ in range(100):
            facts = _digits(rng)
            mapping = facts["map"]
            word = facts["word"]
            assert isinstance(mapping, dict) and isinstance(word, str)
            inverse = {letter: digit for digit, letter in mapping.items()}
            coded = "".join(inverse.get(ch, ch) for ch in word)
            wrong: list[str] = []
            digits = list(mapping)
            for _ in range(40):
                a, b = rng.sample(digits, 2)
                swapped = {**mapping, a: mapping[b], b: mapping[a]}
                text = "".join(swapped.get(ch, ch) for ch in coded)
                wrong.append(text)
            eq = ", ".join(f"{d}={letter}" for d, letter in sorted(mapping.items()))
            stem = (
                f"Dadas las siguientes equivalencias: {eq}. ¿Qué palabra se obtiene al descodificar "
                f"«{coded}»?"
            )
            why = (
                f"Cada cifra se sustituye por su letra ({eq}) y las letras que no son cifras se "
                f"mantienen: {word}."
            )
            try:
                return self._item(rng, seed, level, stem, word, wrong, why, facts)
            except RuntimeError:
                continue
        raise RuntimeError("no digit item")

    def _values_item(self, rng: random.Random, seed: int, level: int) -> Item:
        facts = _values(rng)
        values = facts["values"]
        word = facts["word"]
        assert isinstance(values, list) and isinstance(word, str)
        total = _value_of(word, values)
        classes = ", ".join(f"cada {name} vale {v}" for (name, _, _), v in zip(_CLASSES, values, strict=True))
        stem = f"En un sistema de codificación {classes}. ¿Cuál es el valor de la palabra «{word}»?"
        wrong = [total + d for d in (-3, -2, -1, 1, 2, 3, 4)]
        rng.shuffle(wrong)
        letters = ", ".join(f"{ch}={_value_of(ch, values)}" for ch in word)
        why = f"Se suma el valor de cada letra según su clase ({letters}): {total}."
        return self._item(rng, seed, level, stem, str(total), [str(w) for w in wrong if w > 0], why, facts)

    def _filing_item(self, rng: random.Random, seed: int, level: int) -> Item:
        facts = _filing(rng)
        fields = facts["fields"]
        code = facts["code"]
        asks = facts["asks"]
        assert isinstance(fields, list) and isinstance(code, list) and isinstance(asks, str)
        rows = tuple(
            (str(i + 1), _FIELDS[f][0], ", ".join(f"{v}={name}" for v, name in enumerate(_FIELDS[f][1])))
            for i, f in enumerate(fields)
        )
        table = Table("Clave de archivo", ("Posición", "Indica", "Valores"), rows)
        true_claims = [(i, code[i]) for i in range(4)]
        false_claims = [(i, (code[i] + rng.randint(1, 3)) % 4) for i in range(4)]
        want_true = asks == "CIERTA"
        picked = rng.sample(range(4), 4)
        target = picked[0]
        claims = [(target, true_claims[target][1] if want_true else false_claims[target][1])]
        for i in picked[1:]:
            claims.append((i, false_claims[i][1] if want_true else true_claims[i][1]))
        facts = {**facts, "claims": [list(c) for c in claims], "target": 0}
        texts = [
            f"La posición {i + 1} ({_FIELDS[fields[i]][0]}) es {_FIELDS[fields[i]][1][v]}" + "."
            for i, v in claims
        ]
        stem = (
            "Una clave de archivo tiene cuatro cifras, cada una con el significado de la tabla. "
            f"Para la clave {''.join(str(c) for c in code)}, ¿cuál de las siguientes afirmaciones es {asks}?"
        )
        why = (
            "Se lee cada cifra de la clave en su fila de la tabla y se comprueba cada afirmación; "
            f"la única {asks.lower()} es: {texts[0][:-1]}."
        )
        return self._item(rng, seed, level, stem, texts[0], texts[1:], why, facts, table)

    def solve(self, item: Item) -> int:
        kind = str_fact(item.facts, "kind")
        if kind == "binary":
            equivalences = dict(re.findall(r"([a-g])=([01]{4})", item.stem))
            digits = item.stem.rsplit(": ", 1)[1]
            blocks = [digits[i : i + 4] for i in range(0, len(digits), 4)]
            expected = _decode_binary(equivalences, blocks)
        elif kind == "digits":
            pairs = dict(re.findall(r"(\d)=([a-z])", item.stem))
            coded = re.search(r"«([^»]+)»", item.stem)
            if coded is None:
                raise UnsolvableItem("no coded word")
            expected = "".join(pairs.get(ch, ch) for ch in coded.group(1))
        elif kind == "values":
            values = [int(v) for v in re.findall(r"vale (\d)", item.stem)]
            word_match = re.search(r"«([^»]+)»", item.stem)
            if word_match is None or len(values) != 4:
                raise UnsolvableItem("cannot read the value rule")
            expected = str(_value_of(word_match.group(1), values))
        else:
            return self._solve_filing(item)
        hits = [i for i, option in enumerate(item.options) if option == expected]
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options read {expected}")
        return hits[0]

    @staticmethod
    def _solve_filing(item: Item) -> int:
        code_match = re.search(r"clave (\d{4}),", item.stem)
        if code_match is None or item.table is None:
            raise UnsolvableItem("no code or table")
        code = [int(c) for c in code_match.group(1)]
        wants_true = "CIERTA" in item.stem
        holding: list[int] = []
        for index, option in enumerate(item.options):
            m = re.fullmatch(r"La posición (\d) \(([^)]+)\) es (.+)\.", option)
            if m is None:
                raise UnsolvableItem(f"cannot read {option!r}")
            position = int(m.group(1)) - 1
            values = {name: int(v) for v, name in re.findall(r"(\d)=([^,]+)", item.table.rows[position][2])}
            if values.get(m.group(3)) is None:
                raise UnsolvableItem(f"unknown value in {option!r}")
            if (values[m.group(3)] == code[position]) == wants_true:
                holding.append(index)
        if len(holding) != 1:
            raise UnsolvableItem(f"{len(holding)} options are {'true' if wants_true else 'false'}")
        return holding[0]
