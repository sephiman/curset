# SPDX-License-Identifier: AGPL-3.0-only
"""`verbal-antonimos`: the antonym of a word in capitals; the three distractors are its synonyms, as in the "
"exams."""

from __future__ import annotations

import random
import re
from typing import ClassVar

from tradeschool.psicotecnico import lexicon
from tradeschool.psicotecnico.contract import ItemGenerator, UnsolvableItem, deal_choosing
from tradeschool.psicotecnico.item import Item, Params
from tradeschool.psicotecnico.spanish import sentence_case

_STEM = "Indique entre las siguientes palabras cuál es el antónimo u opuesto de la palabra {word}."


def _option(word: str) -> str:
    return sentence_case(word) + "."


class AntonimosGenerator(ItemGenerator):
    id: ClassVar[str] = "verbal-antonimos"
    levels: ClassVar[tuple[int, ...]] = (1, 2)

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        pool = [
            e
            for e in lexicon.entries()
            if e.level == params.difficulty and len(e.synonyms) >= 3 and e.antonyms
        ]
        entry = rng.choice(pool)
        options, slot, answer = deal_choosing(
            rng, [_option(a) for a in entry.antonyms], [_option(w) for w in entry.synonyms]
        )
        key = answer.rstrip(".").lower()
        return Item(
            generator=self.id,
            seed=seed,
            difficulty=params.difficulty,
            stem=_STEM.format(word=entry.word.upper()),
            options=options,
            key=slot,
            explanation=f"{sentence_case(key)} es lo contrario de {entry.word}; "
            f"las otras tres palabras significan lo mismo que {entry.word}.",
            facts={"word": entry.word},
        )

    def solve(self, item: Item) -> int:
        match = re.search(r"palabra ([^.]+)\.", item.stem)
        if match is None:
            raise UnsolvableItem("no stem word")
        word = match.group(1).lower()
        antonyms = lexicon.antonyms_of(word)
        hits = [i for i, option in enumerate(item.options) if option.rstrip(".").lower() in antonyms]
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options are antonyms of {word}")
        return hits[0]

    def check_extra(self, item: Item) -> list[str]:
        word = str(item.facts["word"])
        shown = [o.rstrip(".").lower() for o in item.options]
        problems = [] if word not in shown else ["the stem word is among the options"]
        key = shown[item.key]
        return problems + [
            f"the DLE lists distractor {option} as an antonym"
            for option in shown
            if option != key and lexicon.dle_related(word, option, "ant")
        ]
