# SPDX-License-Identifier: AGPL-3.0-only
"""`verbal-definicion`: the word for a definition or the definition for a word, from the bank."""

from __future__ import annotations

import random
import re
from typing import ClassVar

from tradeschool.psicotecnico import lexicon
from tradeschool.psicotecnico.contract import ItemGenerator, UnsolvableItem, deal
from tradeschool.psicotecnico.item import Item, Params
from tradeschool.psicotecnico.spanish import sentence_case


class DefinicionGenerator(ItemGenerator):
    id: ClassVar[str] = "verbal-definicion"

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        bank = lexicon.definitions()
        pool = [d for d in bank if d.level <= params.difficulty] if params.difficulty < 3 else list(bank)
        target = rng.choice([d for d in pool if d.level >= params.difficulty - 1] or pool)
        others = rng.sample([d for d in bank if d.word != target.word], 9)
        word_to_definition = rng.random() < 0.5
        if word_to_definition:
            stem = f'Señale qué palabra corresponde a la siguiente definición: "{target.text.rstrip(".")}".'
            key, wrong = sentence_case(target.word) + ".", [sentence_case(o.word) + "." for o in others]
        else:
            stem = f'Señale la definición que corresponde a la palabra "{target.word}".'
            key, wrong = target.text, [o.text for o in others]
        options, slot = deal(rng, key, wrong)
        return Item(
            generator=self.id,
            seed=seed,
            difficulty=params.difficulty,
            stem=stem,
            options=options,
            key=slot,
            explanation=f"{sentence_case(target.word)}: {target.text[0].lower() + target.text[1:]}",
            facts={"word": target.word},
        )

    def solve(self, item: Item) -> int:
        by_word = {d.word: d.text for d in lexicon.definitions()}
        quoted = re.search(r'"([^"]+)"', item.stem)
        if quoted is None:
            raise UnsolvableItem("no quoted text")
        text = quoted.group(1)
        if item.stem.startswith("Señale la definición"):
            expected = by_word.get(text)
            hits = [i for i, o in enumerate(item.options) if o == expected]
        else:
            hits = [
                i
                for i, o in enumerate(item.options)
                if by_word.get(o.rstrip(".").lower(), "").rstrip(".") == text
            ]
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options match the stem")
        return hits[0]
