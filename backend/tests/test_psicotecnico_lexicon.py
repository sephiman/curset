# SPDX-License-Identifier: AGPL-3.0-only
"""Every entry of the verbal word banks is backed by a saved DLE page (blind review, 2026-11-07)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from tradeschool.psicotecnico import lexicon

BACKEND = Path(__file__).resolve().parents[1]
OTROS = BACKEND.parent / "content" / "age-auxiliar-c2" / "sources" / "otros"


def _bank_words() -> set[str]:
    words = {w for e in lexicon.entries() for w in (e.word, *e.synonyms, *e.antonyms)}
    words |= {d.word for d in lexicon.definitions()}
    return words | {w for pair in lexicon.spelling() for w in pair} | set(lexicon.wrong_spellings())


def _found(word: str) -> bool:
    page = lexicon.dle_pages()[word]
    return not page["absent"] and bool(page["lemmas"])


def test_the_relations_file_is_built_from_the_saved_pages() -> None:
    check = subprocess.run(
        [sys.executable, str(BACKEND / "scripts" / "dle_relations.py"), "--check"],
        capture_output=True,
        text=True,
    )
    assert check.returncode == 0, check.stdout


def test_every_bank_word_has_its_saved_dle_page_recorded_in_fuentes() -> None:
    recorded = {
        e["file"] for e in yaml.safe_load((OTROS / "fuentes.yaml").read_text(encoding="utf-8"))["fuentes"]
    }
    for word in _bank_words():
        page = lexicon.dle_pages().get(word)
        assert page is not None, f"no saved DLE page for {word}"
        assert page["file"] in recorded and (OTROS / page["file"]).is_file()


@pytest.mark.parametrize("entry", lexicon.entries(), ids=lambda e: e.word)
def test_every_synonym_is_listed_by_the_dle_or_shares_its_definition(entry: lexicon.Entry) -> None:
    assert _found(entry.word)
    for synonym in entry.synonyms:
        cited = (
            lexicon.dle_related(entry.word, synonym, "syn")
            or (entry.word, synonym) in lexicon.JUDGED_SYNONYMS
        )
        assert cited, f"{entry.word} ~ {synonym}"


@pytest.mark.parametrize("entry", lexicon.entries(), ids=lambda e: e.word)
def test_every_antonym_is_listed_by_the_dle_for_the_word_or_one_of_its_synonyms(entry: lexicon.Entry) -> None:
    for antonym in entry.antonyms:
        cited = any(lexicon.dle_related(near, antonym, "ant") for near in (entry.word, *entry.synonyms))
        assert cited or (entry.word, antonym) in lexicon.JUDGED_ANTONYMS, f"{entry.word} ≠ {antonym}"
        assert not lexicon.dle_related(entry.word, antonym, "syn")


def test_every_judged_pair_is_still_in_the_bank() -> None:
    synonyms = {(e.word, s) for e in lexicon.entries() for s in e.synonyms}
    antonyms = {(e.word, a) for e in lexicon.entries() for a in e.antonyms}
    assert set(lexicon.JUDGED_SYNONYMS) <= synonyms
    assert set(lexicon.JUDGED_ANTONYMS) <= antonyms


@pytest.mark.parametrize("definition", lexicon.definitions(), ids=lambda d: d.word)
def test_every_definition_is_the_dle_sense_verbatim(definition: lexicon.Definition) -> None:
    senses = {s["n"]: s["text"] for s in lexicon.dle_pages()[definition.word]["senses"]}
    assert senses.get(definition.sense) == definition.text


@pytest.mark.parametrize(("right", "wrong"), lexicon.spelling(), ids=lambda w: w)
def test_every_spelling_pair_has_a_dle_word_and_a_form_the_dle_does_not_have(right: str, wrong: str) -> None:
    assert _found(right)
    assert lexicon.dle_pages()[wrong]["absent"], f"«{wrong}» is a DLE word or form: both spellings exist"


def test_no_misspelling_in_a_sentence_is_a_dle_word_or_form() -> None:
    accepted = sorted(w for w in lexicon.wrong_spellings() if not lexicon.dle_pages()[w]["absent"])
    assert accepted == []
