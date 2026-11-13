# SPDX-License-Identifier: AGPL-3.0-only
"""The AEAT «Exámenes oficiales» exercises against the ledger, the definitive answer sheets and the PDFs."""

from __future__ import annotations

import re
import subprocess
import sys
from fractions import Fraction
from functools import cache
from pathlib import Path

import pytest
import yaml

_BACKEND = Path(__file__).resolve().parent.parent
if str(_BACKEND) not in sys.path:
    sys.path.insert(0, str(_BACKEND))

from scripts.build_aeat_official_exams import (  # noqa: E402
    CONTENT_DIR,
    EXAMS,
    EXERCISES_DIR,
    Exam,
    LedgerRow,
    parse_ledger,
    printed_questions,
)

from tradeschool.content.registry import CourseRegistry, load_registry  # noqa: E402
from tradeschool.exams.draw import DrawnPart, SeededRand, draw_part, pool_shortfalls  # noqa: E402
from tradeschool.exams.print_export import build_exam_print  # noqa: E402
from tradeschool.exercises.quiz import QuizConfig  # noqa: E402

OFFICIAL_DIR = CONTENT_DIR / "sources" / "examenes-oficiales"
EXAM_IDS = [exam.slug for exam in EXAMS]
BOOKKEEPING = re.compile(r"cobertura discutible|plantilla|coordinador|Texto descargado", re.IGNORECASE)


@cache
def ledger_rows(exam: Exam) -> list[LedgerRow]:
    return parse_ledger()[exam.ledger_heading]


@cache
def exercise_text(slug: str) -> str:
    return (EXERCISES_DIR / f"{slug}.yaml").read_text(encoding="utf-8")


@cache
def config(slug: str) -> QuizConfig:
    return QuizConfig.model_validate(yaml.safe_load(exercise_text(slug)))


def _pdf(exam: Exam, kind: str) -> Path:
    stem = "tipo" + exam.tipo if exam.tipo != "X" else "tipoA"
    year = exam.code.removeprefix("conv")[:4]
    middle = "_extraordinario" if exam.tipo == "X" else ""
    (found,) = OFFICIAL_DIR.glob(f"*_conv{year}{middle}_{stem}_{kind}.pdf")
    return found


def _flat(pdf: Path) -> str:
    text = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"], check=True, capture_output=True, text=True
    ).stdout
    return "".join(text.replace("­", "").split())


@cache
def questionnaire_text(exam: Exam) -> str:
    return _flat(_pdf(exam, "cuestionario"))


def _squeezed(text: str) -> str:
    return "".join(text.split())


@cache
def printed_sheet(exam: Exam) -> dict[int, str]:
    """The answer sheet read from its own PDF, in its two layouts: «1 C» columns or «1-C» columns."""
    kind = "plantilla-provisional" if exam.tipo == "X" else "plantilla-definitiva"
    text = subprocess.run(
        ["pdftotext", "-layout", str(_pdf(exam, kind)), "-"], check=True, capture_output=True, text=True
    ).stdout
    sheet: dict[int, str] = {}
    for line in text.splitlines():
        for number, letter in re.findall(r"(?<!\d)(\d{1,3})(?:\s+|\s*-\s*)(ANULADA|[ABCD])\b", line):
            sheet[int(number)] = letter
    return sheet


@pytest.fixture(params=EXAMS, ids=EXAM_IDS)
def exam(request: pytest.FixtureRequest) -> Exam:
    assert isinstance(request.param, Exam)
    return request.param


def _included(exam: Exam) -> list[tuple[int, LedgerRow]]:
    return [(q.printed, q.ledger) for q in printed_questions(exam, ledger_rows(exam)) if q.ledger.included]


def test_variant_count_is_the_ledger_included_count(exam: Exam) -> None:
    rows = ledger_rows(exam)
    tipo_a_included = sum(row.included for row in rows)
    assert len(config(exam.slug).variants) == tipo_a_included
    assert len(printed_questions(exam, rows)) in (80, 100)


def test_no_excluded_question_is_present_and_every_printed_one_is_accounted_for(exam: Exam) -> None:
    printed = printed_questions(exam, ledger_rows(exam))
    excluded = {f"Q{q.printed}" for q in printed if not q.ledger.included}
    tags = [variant.tags[1] for variant in config(exam.slug).variants]
    assert not excluded & set(tags)
    assert len(set(tags)) == len(tags)
    assert len(tags) + len(excluded) == len(printed)


def test_variants_follow_the_printed_order_with_consecutive_ids(exam: Exam) -> None:
    variants = config(exam.slug).variants
    assert [v.tags[1] for v in variants] == [f"Q{n}" for n, _ in _included(exam)]
    assert [v.id for v in variants] == [f"q{n:03d}" for n in range(1, len(variants) + 1)]


def test_only_vigente_con_nota_questions_carry_an_explanation(exam: Exam) -> None:
    by_tag = {f"Q{n}": row for n, row in _included(exam)}
    for variant in config(exam.slug).variants:
        row = by_tag[variant.tags[1]]
        if row.estado == "vigente-con-nota":
            assert variant.explanation is not None
            note = variant.explanation.get("es")
            assert note.startswith(("Clave oficial discutida", "Denominación actual"))
            assert not BOOKKEEPING.search(note), (variant.tags, note)
        else:
            assert variant.explanation is None


def test_every_variant_has_four_options_and_the_key_of_the_definitive_sheet(exam: Exam) -> None:
    sheet = printed_sheet(exam)
    assert len(sheet) == len(printed_questions(exam, ledger_rows(exam)))
    for variant in config(exam.slug).variants:
        assert [o.id for o in variant.options] == ["a", "b", "c", "d"]
        correct = [o.id for o in variant.options if o.correct]
        number = int(variant.tags[1].removeprefix("Q"))
        assert correct == [sheet[number].lower()], variant.tags


def test_tipo_a_keys_are_the_ledger_keys(exam: Exam) -> None:
    if exam.tipo == "B":
        pytest.skip("the ledger lists tipo A")
    by_tag = {f"Q{n}": row for n, row in _included(exam)}
    for variant in config(exam.slug).variants:
        correct = next(o.id for o in variant.options if o.correct)
        assert correct == by_tag[variant.tags[1]].clave.strip()[:1].lower(), variant.tags


def test_stems_carry_no_question_number(exam: Exam) -> None:
    assert not [v.tags for v in config(exam.slug).variants if re.match(r"\d+[.\s-]", v.prompt.get("es"))]


def test_questions_are_stored_unshuffled_exactly_as_printed(exam: Exam) -> None:
    assert config(exam.slug).shuffle is False
    text = questionnaire_text(exam)
    position = 0
    for variant in config(exam.slug).variants:
        stem = _squeezed(variant.prompt.get("es"))
        options = [_squeezed(o.text.get("es")) for o in variant.options]
        # The papers print the letters as «A)», «A.-» or «a)» depending on the year.
        printed = "".join(
            f"(?i:{letter})[).-]*{re.escape(option)}" for letter, option in zip("ABCD", options, strict=True)
        )
        start = text.find(stem, position)
        assert start >= 0, f"{variant.tags}: stem is not in the PDF after the previous question"
        assert re.compile(printed).search(text, start), (
            f"{variant.tags}: options differ from the printed order"
        )
        position = start + len(stem)


def test_no_hyphen_split_at_a_line_end_is_left_open(exam: Exam) -> None:
    for variant in config(exam.slug).variants:
        texts = [variant.prompt.get("es"), *(o.text.get("es") for o in variant.options)]
        assert not [t for t in texts if re.search(r"\w- \w", t)], variant.tags


def test_the_files_are_generated_without_yaml_aliases(exam: Exam) -> None:
    text = exercise_text(exam.slug)
    assert text.startswith("# SPDX-License-Identifier: AGPL-3.0-only\n# Generated by")
    assert not re.search(r"[&*]id\d{3}", text)


def test_tipo_b_is_the_tipo_a_set_in_its_own_order(exam: Exam) -> None:
    if exam.tipo != "B":
        pytest.skip("tipo A is the reference")
    a = next(e for e in EXAMS if e.code == exam.code.replace("_B", "_A"))

    def keyed_text(slug: str) -> set[str]:
        return {
            re.sub(r"\W+", "", next(o.text.get("es") for o in v.options if o.correct)).casefold()
            for v in config(slug).variants
        }

    assert len(config(exam.slug).variants) == len(config(a.slug).variants)
    overlap = keyed_text(exam.slug) & keyed_text(a.slug)
    assert len(overlap) >= len(config(a.slug).variants) - 3


# --- the presets that serve the sets (course.yaml) ---

_PRESET_OF = {exam.slug: exam.slug.removeprefix("ofi-") for exam in EXAMS}
_DROPPED_TOPICS = "sobre un tema que el programa de 2025 ya no incluye"


@cache
def course_registry() -> CourseRegistry:
    return load_registry(CONTENT_DIR)


def test_each_official_preset_serves_its_set_as_printed_with_the_aeat_attribution(exam: Exam) -> None:
    registry = course_registry()
    preset = next(p for p in registry.manifest.exams if p.id == _PRESET_OF[exam.slug])
    assert registry.is_official(exam.slug)
    assert (preset.time_limit_minutes, preset.pause) == (exam.minutes, "never")
    (part,) = preset.parts
    assert part.draw == "all" and part.penalty == Fraction(1, 4) and part.scoring is None
    assert pool_shortfalls(registry, preset, None) == []
    found = registry.get_exercise_config(exam.slug)
    assert found is not None and isinstance(found[1], QuizConfig)
    drawn: DrawnPart = draw_part(registry, part, None, SeededRand(1))
    assert [q.variant_id for q in drawn.questions] == [v.id for v in found[1].variants]
    description = preset.description.get("es") if preset.description else ""
    assert description.startswith("Agencia Estatal de Administración Tributaria · Tribunal Calificador")
    assert (
        f"Cuestionario original de {len(printed_questions(exam, ledger_rows(exam)))} preguntas" in description
    )
    assert f"{exam.minutes} minutos" in description


def test_the_description_counts_what_is_excluded_and_why(exam: Exam) -> None:
    registry = course_registry()
    preset = next(p for p in registry.manifest.exams if p.id == _PRESET_OF[exam.slug])
    assert preset.description is not None
    text = preset.description.get("es")
    printed = printed_questions(exam, ledger_rows(exam))
    excluded = [q for q in printed if not q.ledger.included]
    assert f"Se incluyen {len(printed) - len(excluded)} con la clave" in text
    assert f"se {'excluye' if len(excluded) == 1 else 'excluyen'} {len(excluded)}:" in text
    for status, phrase in (
        ("anulada", "anulada"),
        ("norma modificada", "reforma de la norma"),
        ("fuera de temario", "programa de 2025 ya no incluye"),
    ):
        count = sum(q.ledger.status == status for q in excluded)
        assert (phrase in text) == bool(count), (exam.slug, status)
        if count:
            assert re.search(rf"\b{count} [^,.]*?{re.escape(phrase)}", text), (exam.slug, status, count)


def test_the_28_questions_on_dropped_topics_are_all_left_out_of_the_tipo_a_sets() -> None:
    dropped = 0
    for exam in EXAMS:
        if exam.tipo == "B":
            continue
        rows = ledger_rows(exam)
        dropped += sum(row.status == "fuera de temario" for row in rows)
        by_tag = {variant.tags[1] for variant in config(exam.slug).variants}
        assert not {f"Q{r.number}" for r in rows if r.status == "fuera de temario"} & by_tag
    assert dropped == 28


def test_the_exercises_sit_under_the_intro_lesson_and_never_enter_the_bank_draws() -> None:
    registry = course_registry()
    for exam in EXAMS:
        assert registry.exercise_lesson_id(exam.slug) == "m00-l01"
        assert registry.is_official(exam.slug)
    primer = next(p for p in registry.manifest.exams if p.id == "primer-ejercicio")
    for seed in range(5):
        drawn = draw_part(registry, primer.parts[0], None, SeededRand(seed)).questions
        assert not any(registry.is_official(q.exercise_id) for q in drawn)


def test_a_printed_paper_keeps_the_letters_and_carries_a_key_sheet() -> None:
    registry = course_registry()
    exam = EXAMS[0]
    paper = build_exam_print(registry, _PRESET_OF[exam.slug], "es", seed=3)
    printed = paper["parts"][0]["questions"]
    variants = config(exam.slug).variants
    assert len(printed) == len(paper["keySheet"][0]["keys"]) == len(variants) == 79
    assert [o["letter"] for o in printed[0]["options"]] == ["A", "B", "C", "D"]
    sheet = printed_sheet(exam)
    keys = [k["correctLetter"] for k in paper["keySheet"][0]["keys"]]
    assert keys == [sheet[int(v.tags[1].removeprefix("Q"))] for v in variants]
