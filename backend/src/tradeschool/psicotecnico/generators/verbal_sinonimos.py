# SPDX-License-Identifier: AGPL-3.0-only
"""`verbal-sinonimos`: the synonym of a word, or the incorrect pair; distractors come from other clusters."""

from __future__ import annotations

import random
import re
from typing import ClassVar

from tradeschool.psicotecnico import lexicon
from tradeschool.psicotecnico.contract import ItemGenerator, UnsolvableItem, deal, deal_choosing
from tradeschool.psicotecnico.item import Item, Params
from tradeschool.psicotecnico.spanish import sentence_case

_STEMS = (
    "Indique entre las siguientes palabras cuál es el sinónimo o afín de la palabra {word}.",
    "Señale la palabra cuyo significado es más parecido al de {word}.",
)
_PAIR_STEM = "¿Qué pareja de SINÓNIMOS es INCORRECTA?"


def _option(word: str) -> str:
    return sentence_case(word) + "."


def _pair(a: str, b: str) -> str:
    return f"{sentence_case(a)} y {b}."


class SinonimosGenerator(ItemGenerator):
    id: ClassVar[str] = "verbal-sinonimos"
    levels: ClassVar[tuple[int, ...]] = (1, 2)

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        if params.difficulty == 2 and rng.random() < 0.3:
            return self._pair_item(rng, seed)
        pool = [e for e in lexicon.entries() if e.level == params.difficulty]
        entry = rng.choice(pool)
        own = lexicon.cluster_of(entry.word)
        strangers = [
            word
            for other in lexicon.entries()
            if lexicon.cluster_of(other.word) != own
            for word in other.synonyms
            if lexicon.cluster_of(word) != own
        ]
        wrong_pool = [*entry.antonyms, *rng.sample(strangers, 4)]
        options, slot, answer = deal_choosing(
            rng, [_option(w) for w in entry.synonyms], [_option(w) for w in wrong_pool]
        )
        key = answer.rstrip(".").lower()
        wrong = [o.rstrip(".").lower() for o in options if o != answer]
        stem = rng.choice(_STEMS).format(word=entry.word.upper())
        return Item(
            generator=self.id,
            seed=seed,
            difficulty=params.difficulty,
            stem=stem,
            options=options,
            key=slot,
            explanation=f"{sentence_case(key)} significa lo mismo que {entry.word}; "
            f"{wrong[0]} y {wrong[1]} son opuestas o distintas.",
            facts={"word": entry.word, "mode": "single"},
        )

    def _pair_item(self, rng: random.Random, seed: int) -> Item:
        entries = rng.sample(lexicon.entries(), 4)
        good = [_pair(e.word, rng.choice(e.synonyms)) for e in entries[:3]]
        bad_entry = entries[3]
        bad = _pair(bad_entry.word, rng.choice(bad_entry.antonyms))
        options, slot = deal(rng, bad, good)
        return Item(
            generator=self.id,
            seed=seed,
            difficulty=2,
            stem=_PAIR_STEM,
            options=options,
            key=slot,
            explanation=f"«{bad[:-1]}» no es una pareja de sinónimos: son palabras de sentido opuesto.",
            facts={"mode": "pairs"},
        )

    def solve(self, item: Item) -> int:
        if item.facts.get("mode") == "pairs":
            return self._solve_pairs(item)
        match = re.search(r"([A-ZÁÉÍÓÚÑ]{3,})\.$", item.stem)
        if match is None:
            raise UnsolvableItem("no stem word")
        word = match.group(1).lower()
        synonyms = lexicon.synonyms_of(word)
        hits = [i for i, option in enumerate(item.options) if option.rstrip(".").lower() in synonyms]
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options are synonyms of {word}")
        return hits[0]

    @staticmethod
    def _solve_pairs(item: Item) -> int:
        wrong: list[int] = []
        for index, option in enumerate(item.options):
            left, right = option.rstrip(".").lower().split(" y ")
            same = lexicon.cluster_of(left) is not None and lexicon.cluster_of(left) == lexicon.cluster_of(
                right
            )
            if not same:
                wrong.append(index)
        if len(wrong) != 1:
            raise UnsolvableItem(f"{len(wrong)} pairs are not synonyms")
        return wrong[0]

    def check_extra(self, item: Item) -> list[str]:
        return [] if all(o.endswith(".") and o[0].isupper() for o in item.options) else ["option form"]
