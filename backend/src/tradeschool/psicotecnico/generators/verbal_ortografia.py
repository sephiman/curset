# SPDX-License-Identifier: AGPL-3.0-only
"""`verbal-ortografia`: the misspelt or right word, or a sentence's error count, from the spelling bank."""

from __future__ import annotations

import random
import re
from typing import ClassVar

from tradeschool.psicotecnico import lexicon
from tradeschool.psicotecnico.contract import ItemGenerator, UnsolvableItem, deal
from tradeschool.psicotecnico.item import Item, Params
from tradeschool.psicotecnico.spanish import sentence_case

_SLOT = re.compile(r"\[([^|\]]+)\|([^\]]+)\]")
_WORD_STEM = "Indique cuál de las siguientes palabras contiene un error ortográfico:"
_RIGHT_STEM = "Indique cuál de las siguientes palabras está correctamente escrita:"
_COUNT_STEM = "¿Cuántos errores ortográficos contiene la siguiente frase?"
_WORDS = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+")


def _option(word: str) -> str:
    return sentence_case(word) + "."


def _render(sentence: str, wrong_slots: set[int]) -> str:
    counter = iter(range(100))
    return _SLOT.sub(lambda m: m.group(2) if next(counter) in wrong_slots else m.group(1), sentence)


class OrtografiaGenerator(ItemGenerator):
    id: ClassVar[str] = "verbal-ortografia"
    levels: ClassVar[tuple[int, ...]] = (1, 2)

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        if params.difficulty == 2:
            return self._count_item(rng, seed)
        pairs = lexicon.spelling()
        chosen = rng.sample(pairs, 10)
        if rng.random() < 0.8:
            (right_one, wrong_one), rest = chosen[0], chosen[1:]
            options, slot = deal(rng, _option(wrong_one), [_option(r) for r, _ in rest])
            stem = _WORD_STEM
            why = f"Se escribe «{right_one}», no «{wrong_one}»."
        else:
            (right_one, _), rest = chosen[0], chosen[1:]
            options, slot = deal(rng, _option(right_one), [_option(w) for _, w in rest])
            stem = _RIGHT_STEM
            why = f"Solo «{right_one}» está bien escrita; las otras tres llevan un error."
        return Item(
            generator=self.id,
            seed=seed,
            difficulty=1,
            stem=stem,
            options=options,
            key=slot,
            explanation=why,
            facts={"mode": "word"},
        )

    def _count_item(self, rng: random.Random, seed: int) -> Item:
        sentence = rng.choice(lexicon.SENTENCES)
        slots = len(_SLOT.findall(sentence))
        errors = rng.randint(2, min(5, slots))
        wrong_slots = set(rng.sample(range(slots), errors))
        text = _render(sentence, wrong_slots)
        spread = [n for n in range(max(1, errors - 3), errors + 4) if n != errors]
        rng.shuffle(spread)
        options, slot = deal(rng, f"{errors}.", [f"{n}." for n in spread[:6]])
        found = [m.group(2) for i, m in enumerate(_SLOT.finditer(sentence)) if i in wrong_slots]
        return Item(
            generator=self.id,
            seed=seed,
            difficulty=2,
            stem=f"{_COUNT_STEM} {text}",
            options=options,
            key=slot,
            explanation=f"Tiene {errors} errores: " + ", ".join(found) + ".",
            facts={"mode": "count"},
        )

    def solve(self, item: Item) -> int:
        wrong, right = lexicon.wrong_spellings(), lexicon.right_spellings()
        if item.facts.get("mode") == "count":
            sentence = item.stem.split("? ", 1)[1]
            words = _WORDS.findall(sentence)
            unknown = [w for w in words if w.lower() in wrong and w.lower() in right]
            if unknown:
                raise UnsolvableItem(f"{unknown} are in both banks")
            expected = f"{sum(1 for w in words if w.lower() in wrong)}."
            hits = [i for i, o in enumerate(item.options) if o == expected]
        else:
            wanted_wrong = item.stem == _WORD_STEM
            hits = []
            for index, option in enumerate(item.options):
                word = option.rstrip(".").lower()
                if word not in wrong and word not in right:
                    raise UnsolvableItem(f"{word!r} is in neither bank")
                if (word in wrong) == wanted_wrong:
                    hits.append(index)
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options answer the stem")
        return hits[0]
