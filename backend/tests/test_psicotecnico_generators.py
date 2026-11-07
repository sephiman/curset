# SPDX-License-Identifier: AGPL-3.0-only
"""The psicotécnico generators: property tests, answer-bias guards, goldens and the load gate."""

from __future__ import annotations

import json
import random
import re
from fractions import Fraction
from pathlib import Path
from typing import ClassVar, cast

import pytest

from test_quiz_answer_bias import (
    SIGMA,
    Answered,
    _length_edge,
    _longest_is_correct,
    _position_z,
    _report,
)
from tradeschool.content.registry import load_registry
from tradeschool.exercises.psicotecnico import PsicotecnicoConfig, build_item
from tradeschool.psicotecnico.contract import GeneratorLoadError, ItemGenerator, int_fact, verify
from tradeschool.psicotecnico.goldens import fingerprint, golden_items
from tradeschool.psicotecnico.item import Item, Params
from tradeschool.psicotecnico.registry import GENERATORS, load_generator
from tradeschool.psicotecnico.weights import apportion

COURSE = Path(__file__).resolve().parents[2] / "content" / "age-auxiliar-c2"
FINGERPRINTS = Path(__file__).resolve().parent / "goldens" / "psicotecnico-fingerprints.json"
IDS = sorted(GENERATORS)
ITEMS_PER_GENERATOR = 1_000
TIMES = "\N{MULTIPLICATION SIGN}"


def test_the_first_batch_is_the_thirteen_recurring_types() -> None:
    assert len(IDS) == 13


@pytest.mark.parametrize("generator_id", IDS)
def test_property_tests_hold_over_many_seeded_items_at_every_level(generator_id: str) -> None:
    assert verify(GENERATORS[generator_id], per_level=300, base=7) == []


@pytest.mark.parametrize("generator_id", IDS)
def test_the_same_seed_builds_the_same_item(generator_id: str) -> None:
    generator = GENERATORS[generator_id]
    for level in generator.levels:
        assert generator.generate(99, Params(level)) == generator.generate(99, Params(level))


class _WrongKey(ItemGenerator):
    id: ClassVar[str] = "wrong-key"

    def build(self, seed: int, params: Params) -> Item:
        return Item(self.id, seed, 1, "¿2 + 2?", ("3", "4", "5", "6"), 0, "Dos y dos son cuatro.")

    def solve(self, item: Item) -> int:
        return 1


def test_a_generator_with_a_failing_property_test_does_not_load() -> None:
    with pytest.raises(GeneratorLoadError, match="solver says option 1"):
        load_generator("wrong-key", {"wrong-key": _WrongKey()})


def test_weights_are_split_exactly_by_largest_remainder() -> None:
    assert apportion([1, 2], 6) == [2, 4]
    assert apportion([62, 16, 14, 10, 9, 11, 9, 9, 9, 9, 9, 4, 4], 30) == [
        11,
        3,
        2,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
    ]
    for total in range(0, 40):
        assert sum(apportion([3, 1, 4, 1, 5], total)) == total


def _declared() -> list[PsicotecnicoConfig]:
    registry = load_registry(COURSE, check_excerpts=False)
    return [
        PsicotecnicoConfig(type="psicotecnico", generator=use.generator, difficulty=use.difficulty)
        for use in registry.generator_uses()
    ]


def test_age_auxiliar_declares_the_thirteen_generators_and_stays_a_draft() -> None:
    registry = load_registry(COURSE, check_excerpts=False)
    assert sorted(use.generator for use in registry.generator_uses()) == IDS
    assert not registry.published


# --- answer-bias guards over 1,000 seeded items per generator -------------------------------------


def _answered(config: PsicotecnicoConfig) -> list[Answered]:
    rng = random.Random(20261107)
    rows: list[Answered] = []
    for _ in range(ITEMS_PER_GENERATOR):
        item = build_item(config, rng.randrange(2**62))
        rows.append(
            Answered(
                exercise=config.generator,
                variant=str(item.seed),
                lengths=tuple(len(option) for option in item.options),
                correct=frozenset({item.key}),
            )
        )
    return rows


@pytest.mark.parametrize("config", _declared(), ids=lambda c: c.generator)
def test_the_answer_is_dealt_to_every_slot_equally(config: PsicotecnicoConfig) -> None:
    stats = _position_z(_answered(config))
    worst = max(stats, key=lambda s: abs(s[4]))
    detail = ", ".join(
        f"{chr(97 + slot)}={observed:.0f}/{expected:.0f}" for slot, observed, expected, _, _ in stats
    )
    assert abs(worst[4]) <= SIGMA, detail


@pytest.mark.parametrize("config", _declared(), ids=lambda c: c.generator)
def test_the_answer_is_not_the_longest_option_more_often_than_chance(config: PsicotecnicoConfig) -> None:
    z, detail = _report("longest-is-correct", _answered(config), _longest_is_correct)
    assert abs(z) <= SIGMA, detail


@pytest.mark.parametrize("config", _declared(), ids=lambda c: c.generator)
def test_the_answer_carries_no_systematic_length_advantage(config: PsicotecnicoConfig) -> None:
    z, detail = _report("length edge", _answered(config), _length_edge)
    assert abs(z) <= SIGMA, detail


# --- goldens: the 50 items per generator that the blind review reads ------------------------------


def test_the_fifty_goldens_per_generator_are_unchanged() -> None:
    registry = load_registry(COURSE, check_excerpts=False)
    committed = json.loads(FINGERPRINTS.read_text(encoding="utf-8"))
    current = {use.generator: fingerprint(golden_items(use)) for use in registry.generator_uses()}
    moved = sorted(g for g in current if committed.get(g) != current[g])
    assert not moved, (
        f"goldens moved for {moved}: run scripts/export_psicotecnico_goldens.py and re-review them"
    )


# --- blind-review fixes (2026-11-07): each was a FAIL family of the golden read ---------------------


@pytest.mark.parametrize(
    ("terms", "answer", "rule"),
    [
        ([2, 6, 18, 54, 162, 486], 1458, "cada término es el anterior multiplicado por 3"),
        ([96, 48, 24, 12, 6], 3, "cada término es el anterior dividido entre 2"),
        ([15, 24, 33, 42, 51], 60, "cada término suma 9 al anterior"),
        ([4, 11, 25, 53, 109, 221], 445, "cada término es el anterior multiplicado por 2 más 3"),
        ([3, 5, 9, 17, 33], 65, "cada término es el anterior multiplicado por 2 menos 1"),
        ([19, 21, 25, 27, 31, 33], 37, "se suman alternativamente 2 y 4"),
        (
            [1, 7, 4, 14, 7, 21],
            10,
            "son dos series intercaladas: la de los lugares impares (1, 4, 7) suma 3 "
            "y la de los pares (7, 14, 21) suma 7",
        ),
        (
            [5, 3, 15, 4, 60, 5],
            300,
            "cada término de lugar impar es el producto de los dos anteriores "
            f"(5 {TIMES} 3 = 15, 15 {TIMES} 4 = 60)",
        ),
    ],
)
def test_the_series_explanation_names_the_simplest_rule_with_its_constants(
    terms: list[int], answer: int, rule: str
) -> None:
    from tradeschool.psicotecnico.generators.serie_numerica import _rule_text

    assert _rule_text(terms, answer) == f"En {', '.join(map(str, terms))}, {rule}; el que sigue es {answer}."


def test_the_ordering_explanation_names_each_deciding_letter() -> None:
    from tradeschool.psicotecnico.generators.administrativo_ordenacion import _explanation

    assert _explanation(["consenso", "conserva", "consola", "consuelo", "consumo"]) == (
        "Todas empiezan por «cons» y se ordenan por la primera letra distinta: "
        "consenso va antes que conserva por la 6.ª letra (n y r), conserva va antes que consola por la 5.ª "
        "(e y o), consola va antes que consuelo por la 5.ª (o y u), consuelo va antes que consumo por la 6.ª "
        "(e y m)."
    )
    assert _explanation(["cómodo", "compás"]).startswith("Todas empiezan por «com»")


def _many(generator_id: str, level: int, count: int = 400) -> list[Item]:
    return [GENERATORS[generator_id].generate(seed, Params(level)) for seed in range(count)]


def test_every_filing_drawer_spans_several_surnames_and_every_material_is_a_noun_in_a_roll() -> None:
    items = [i for level in (1, 2) for i in _many("administrativo-clasificacion", level)]
    for item in items:
        assert "bobina" not in item.stem
        for lo, hi in re.findall(r"cajón \d: de (\w+) a (\w+)", item.stem):
            assert lo != hi, item.stem
        for adjective in ("Trenzad", "Plano", "Flexible", "Apantallado", "Coaxial", "Rígido", "Paralelo"):
            assert adjective not in item.stem


def test_the_proportional_explanation_agrees_in_number_and_spells_the_fraction() -> None:
    for item in [i for level in (1, 2) for i in _many("calculo-fracciones-proporciones", level)]:
        assert " 1 partes" not in item.explanation
        assert not re.search(r"\d\.º", item.explanation), item.explanation


def _euros(option: str) -> Fraction:
    return Fraction(option.removesuffix(" €").replace(".", "").replace(",", "."))


def test_a_discount_or_increase_offers_at_most_the_sign_slip_on_the_wrong_side_of_the_price() -> None:
    for item in [i for level in (1, 2, 3) for i in _many("calculo-porcentajes", level)]:
        assert "material de oficina" not in item.stem
        kind = item.facts["kind"]
        if kind not in ("discount", "increase"):
            continue
        assert item.difficulty == 1, "one multiplication is level 1"
        price = Fraction(int_fact(item.facts, "price"))
        wrong_side = [o for o in item.options if (_euros(o) >= price) == (kind == "discount")]
        assert len(wrong_side) <= 1, item.options


_TABLES = [i for level in (1, 2, 3) for i in _many("tablas-lectura", level, 300)]


def _query(item: Item) -> dict[str, object]:
    query = item.facts["query"]
    assert isinstance(query, dict)
    return query


def test_table_conditions_agree_with_plural_columns_and_stay_inside_the_column() -> None:
    for item in _TABLES:
        assert item.table is not None
        for cond in cast(list[dict[str, object]], _query(item).get("conds", [])):
            if cond["op"] == "=":
                continue
            col = int(cast(int, cond["col"]))
            header = re.sub(r"\s*\(.*\)", "", item.table.header[col]).lower()
            if header.split()[0].endswith("s"):
                assert f"{header} superior" not in item.stem and f"{header} inferior" not in item.stem
            values = [Fraction(r[col].replace(".", "").replace(",", ".")) for r in item.table.rows]
            assert min(values) <= Fraction(str(cond["value"]).replace(".", "")) <= max(values), item.stem


_NOT_ADDITIVE = {"Año de publicación", "Edad", "Precio por persona (€)"}


def test_tables_add_only_additive_columns_and_divide_only_meaningful_pairs() -> None:
    from tradeschool.psicotecnico.generators.tablas_lectura import THEMES

    pairs = {(t.title, a, b) for t in THEMES for a, b in t.ratios}
    for item in _TABLES:
        assert item.table is not None
        query, header = _query(item), item.table.header
        if query["kind"] in ("filter_sum", "share") or query.get("agg") == "sum":
            assert header[int(cast(int, query["col"]))] not in _NOT_ADDITIVE, item.stem
        if query["kind"] == "ratio_extreme":
            num, den = header[int(cast(int, query["num"]))], header[int(cast(int, query["den"]))]
            assert (item.table.title, num, den) in pairs, item.stem
            assert "(0,00)" not in item.explanation
        assert not re.search(r"\bsus \w+ suman", item.explanation)
        if query["kind"] == "filter_sum" and item.difficulty == 3:
            assert int(item.explanation.split("Pasan el filtro ")[1].split()[0]) >= 3


_KMH = {"Tren": (90, 260), "Avión": (250, 750), "Coche": (60, 120), "Autobús": (50, 100)}


def test_trips_have_speeds_their_means_of_transport_allow_and_excursions_go_by_land() -> None:
    for item in _TABLES:
        assert item.table is not None
        header = item.table.header
        if item.table.title == "Excursiones":
            assert all("Barco" not in row for row in item.table.rows)
        if item.table.title != "Desplazamientos":
            continue
        medio, km, minutes = (
            header.index("Medio"),
            header.index("Distancia (km)"),
            header.index("Tiempo (min)"),
        )
        for row in item.table.rows:
            speed = Fraction(int(row[km].replace(".", "")) * 60, int(row[minutes].replace(".", "")))
            low, high = _KMH[row[medio]]
            assert low <= speed <= high, row


def test_coded_words_keep_their_tildes_and_no_option_gives_itself_away_as_the_only_real_word() -> None:
    for item in [i for level in (1, 2) for i in _many("atencion-codificacion", level)]:
        text = " ".join((item.stem, *item.options)).lower()
        for bare in ("tramite", "gestion", "martinez", "almacen"):
            assert not re.search(rf"\b{bare}", text), item.stem
        if item.facts["kind"] == "digits":
            assert all(re.search(r"\d", option) for option in item.options), item.options


def test_the_word_to_code_has_eight_letters_like_the_official_ones() -> None:
    items = [i for i in _many("atencion-codificacion", 1) if i.facts["kind"] == "digits"]
    assert items
    assert {len(str(i.facts["word"])) for i in items} == {8}


def test_the_binary_table_lists_the_letters_a_to_f_in_order_like_the_official_one() -> None:
    items = [i for i in _many("atencion-codificacion", 1) if i.facts["kind"] == "binary"]
    assert items
    for item in items:
        assert re.findall(r"\b([a-z])=[01]{4}", item.stem) == list("abcdef"), item.stem


def test_filing_items_carry_the_index_level_of_the_official_decodes_true_or_false() -> None:
    # 2024X-P1-55, 58, 59 (FALSO) and P1-60 (CIERTO) are all nivel 2 in the psicotécnico index.
    filing = [i for level in (1, 2) for i in _many("atencion-codificacion", level) if i.facts["kind"] == "filing"]
    assert {i.difficulty for i in filing} == {2}
    assert {i.facts["asks"] for i in filing} == {"CIERTA", "FALSA"}


def test_the_filing_code_has_six_positions_like_the_official_one() -> None:
    items = [i for i in _many("atencion-codificacion", 2) if i.facts["kind"] == "filing"]
    assert items
    for item in items:
        assert item.table is not None and len(item.table.rows) == 6, item.table
        assert "seis cifras" in item.stem and re.search(r"clave \d{6},", item.stem), item.stem
        for position, (_, field, values) in enumerate(item.table.rows, start=1):
            digit = re.search(r"clave (\d{6}),", item.stem)
            assert digit is not None
            value = dict(v.split("=") for v in values.split(", "))[digit[1][position - 1]]
            assert f"{position} ({field}) = {digit[1][position - 1]}, {value}" in item.explanation, (
                item.explanation
            )


def test_a_sentence_spelling_item_has_four_to_six_errors_like_the_official_ones() -> None:
    errors = [int(i.options[i.key].rstrip(".")) for i in _many("verbal-ortografia", 2)]
    assert set(errors) == {4, 5, 6}, sorted(set(errors))


def test_stationery_totals_offer_only_amounts_the_prices_can_add_up_to() -> None:
    items = [
        i for level in (1, 2) for i in _many("calculo-problemas", level) if i.facts["kind"] == "products"
    ]
    assert items
    for item in items:
        for option in item.options:
            assert _euros(option.rstrip(".").replace(" euros", " €")) * 20 % 1 == 0, item.options


def test_text_conditions_quote_the_table_value_after_a_list_of_conditions() -> None:
    for item in _TABLES:
        assert item.table is not None
        for cond in cast(list[dict[str, object]], _query(item).get("conds", [])):
            if cond["op"] == "=":
                assert f"«{cond['value']}»" in item.stem, item.stem
        if _query(item).get("conds"):
            assert re.search(r"(esta condición|estas condiciones): ", item.stem), item.stem


def _folded(word: str) -> str:
    from tradeschool.psicotecnico.generators.administrativo_ordenacion import _fold

    return _fold(word)


def _word_options(item: Item) -> list[str]:
    return [o.rstrip(".").lower() for o in item.options]


def test_verbal_distractors_share_the_part_of_speech_of_the_key() -> None:
    from tradeschool.psicotecnico import lexicon

    for item in _many("verbal-sinonimos", 1) + _many("verbal-sinonimos", 2):
        if item.facts["mode"] == "single":
            stem = lexicon.part_of_speech(str(item.facts["word"]))
            assert {lexicon.part_of_speech(w) for w in _word_options(item)} == {stem}, item.options
    for level in (1, 2, 3):
        for item in _many("verbal-definicion", level):
            word = str(item.facts["word"])
            assert next(d for d in lexicon.definitions() if d.word == word).level == level
            if item.stem.startswith("Señale qué palabra"):
                parts = {lexicon.part_of_speech(w) for w in _word_options(item)}
                assert parts == {lexicon.part_of_speech(word)}, item.options


def test_verbal_explanations_name_every_distractor_or_error() -> None:
    for item in _many("verbal-sinonimos", 1) + _many("verbal-sinonimos", 2):
        if item.facts["mode"] == "single":
            for option in _word_options(item):
                assert option in item.explanation.lower(), (option, item.explanation)
    for item in _many("verbal-ortografia", 1):
        if "correctamente escrita" in item.stem:
            for option in _word_options(item):
                assert f"«{option}»" in item.explanation.lower(), item.explanation


def test_the_ordering_explanation_places_every_word_by_its_deciding_letter() -> None:
    for item in _many("administrativo-ordenacion", 1) + _many("administrativo-ordenacion", 2):
        words = cast(list[str], item.facts["words"])
        assert "consiste," not in item.stem and "consiste." not in item.stem
        prefix = re.search(r"empiezan por «([^»]+)»", item.explanation)
        assert prefix is not None and all(_folded(w).startswith(prefix[1]) for w in words), item.explanation
        assert item.explanation.count(" va antes que ") == len(words) - 1, item.explanation


def test_the_larger_of_two_numbers_is_offered_only_between_half_the_sum_and_the_sum() -> None:
    for item in [i for level in (1, 2, 3) for i in _many("calculo-problemas", level)]:
        if item.facts["kind"] != "ratio":
            continue
        total = int_fact(item.facts, "small") * (int_fact(item.facts, "factor") + 1)
        for option in item.options:
            assert total / 2 < int(option.rstrip(".").replace(".", "")) < total, (total, item.options)


def test_share_questions_name_the_group_with_its_article() -> None:
    for item in _TABLES:
        if _query(item)["kind"] == "share":
            assert re.search(r"corresponde a los \w+ con ", item.stem), item.stem


def test_no_three_synonym_distractors_share_a_meaning() -> None:
    from tradeschool.psicotecnico import lexicon

    for item in _many("verbal-sinonimos", 1) + _many("verbal-sinonimos", 2):
        if item.facts["mode"] != "single":
            continue
        options = _word_options(item)
        wrong = [w for i, w in enumerate(options) if i != item.key]
        antonyms = lexicon.antonyms_of(str(item.facts["word"]))
        assert sum(w in antonyms for w in wrong) <= 2, options
        clusters = [lexicon.cluster_of(w) for w in wrong if w not in antonyms]
        assert len(clusters) == len(set(clusters)), options


def test_no_synonym_distractor_comes_from_a_cluster_the_dle_ties_to_the_stem() -> None:
    from tradeschool.psicotecnico import lexicon

    for item in _many("verbal-sinonimos", 1) + _many("verbal-sinonimos", 2):
        if item.facts["mode"] != "single":
            continue
        stem = str(item.facts["word"])
        options = _word_options(item)
        for i, word in enumerate(options):
            if i == item.key:
                continue
            cluster = lexicon.synonyms_of(word) | {word}
            assert not any(lexicon.dle_related(stem, w, "syn") for w in cluster), (stem, word)
