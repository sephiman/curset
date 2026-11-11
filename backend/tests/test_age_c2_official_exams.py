# SPDX-License-Identifier: AGPL-3.0-only
"""The Auxiliar «Exámenes oficiales» exercises against the ledger, the PDFs and the printed tables."""

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

from scripts.build_c2_official_exams import (  # noqa: E402
    EXAMS,
    EXERCISES_DIR,
    LEDGER_PATH,
    OFFICIAL_DIR,
    Exam,
    Ledger,
    LedgerRow,
    parse_ledger,
)
from scripts.c2_official_exam_tables import TABLE_USES  # noqa: E402
from scripts.verify_c2_official_tables import check_exam  # noqa: E402

from tradeschool.content.registry import CourseRegistry  # noqa: E402
from tradeschool.exercises.quiz import QuizConfig, QuizGenerator, QuizVariant  # noqa: E402

EXAM_IDS = [exam.slug for exam in EXAMS]
BOOKKEEPING = re.compile(r"Modelo B|modelo A|transcrita|plantilla|coordinador", re.IGNORECASE)


@cache
def ledger() -> Ledger:
    return parse_ledger()


@cache
def exercise_text(slug: str) -> str:
    return (EXERCISES_DIR / f"{slug}.yaml").read_text(encoding="utf-8")


@cache
def config(slug: str) -> QuizConfig:
    return QuizConfig.model_validate(yaml.safe_load(exercise_text(slug)))


def tag_of(row: LedgerRow) -> str:
    return f"{row.section}-{row.number}"


def row_for(exam: Exam, variant: QuizVariant) -> LedgerRow:
    code, tag = variant.tags
    assert code == exam.code
    return next(row for row in ledger().exams[exam.code] if tag_of(row) == tag)


def summary_counts() -> dict[str, tuple[int, int]]:
    counts: dict[str, tuple[int, int]] = {}
    for line in LEDGER_PATH.read_text(encoding="utf-8").splitlines():
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if line.startswith("| conv20"):
            counts[cells[0]] = (int(cells[2]), int(cells[3]))
    return counts


@cache
def questionnaire_text(exam: Exam) -> str:
    out = subprocess.run(
        ["pdftotext", "-layout", str(OFFICIAL_DIR / exam.pdf), "-"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    lines = [ln for ln in out.splitlines() if "AUX-L" not in ln and not re.search(r"Página \d+ de \d+", ln)]
    return " ".join(" ".join(lines).split())


@pytest.fixture(params=EXAMS, ids=EXAM_IDS)
def exam(request: pytest.FixtureRequest) -> Exam:
    assert isinstance(request.param, Exam)
    return request.param


def test_variant_count_is_the_ledger_included_count(exam: Exam) -> None:
    rows = ledger().exams[exam.code]
    included = [row for row in rows if row.estado in ("vigente", "vigente-con-nota")]
    vigente, con_nota = summary_counts()[exam.code]
    assert len(config(exam.slug).variants) == len(included) == vigente + con_nota
    assert len(rows) == 120


def test_no_excluded_ledger_row_is_present(exam: Exam) -> None:
    rows = ledger().exams[exam.code]
    excluded = {tag_of(row) for row in rows if row.estado not in ("vigente", "vigente-con-nota")}
    tags = [variant.tags[1] for variant in config(exam.slug).variants]
    assert not excluded & set(tags)
    assert len(set(tags)) == len(tags)
    assert len(tags) + len(excluded) == 120


def test_variants_follow_questionnaire_order_with_consecutive_ids(exam: Exam) -> None:
    included = [tag_of(r) for r in ledger().exams[exam.code] if r.estado in ("vigente", "vigente-con-nota")]
    variants = config(exam.slug).variants
    assert [v.tags[1] for v in variants] == included
    assert [v.id for v in variants] == [f"q{n:03d}" for n in range(1, len(variants) + 1)]


def test_only_vigente_con_nota_questions_carry_an_explanation(exam: Exam) -> None:
    for variant in config(exam.slug).variants:
        row = row_for(exam, variant)
        if row.estado == "vigente-con-nota":
            assert variant.explanation is not None
            note = variant.explanation.get("es")
            assert note.strip()
            assert not BOOKKEEPING.search(note), (variant.tags, note)
        else:
            assert variant.explanation is None


def test_every_variant_has_four_options_and_the_ledger_key(exam: Exam) -> None:
    for variant in config(exam.slug).variants:
        assert [o.id for o in variant.options] == ["a", "b", "c", "d"]
        correct = [o.id for o in variant.options if o.correct]
        assert correct == [row_for(exam, variant).clave.strip()[:1].lower()], variant.tags


def test_stems_carry_no_question_number(exam: Exam) -> None:
    assert not [v.tags for v in config(exam.slug).variants if re.match(r"\d+[.\s]", v.prompt.get("es"))]


def test_questions_are_stored_unshuffled_in_the_printed_option_order(exam: Exam) -> None:
    assert config(exam.slug).shuffle is False
    text = questionnaire_text(exam)
    for variant in config(exam.slug).variants:
        texts = [re.escape(o.text.get("es")) for o in variant.options]
        printed = r"\s+".join(
            f"{letter}\\)\\s+{option}" for letter, option in zip("abcd", texts, strict=True)
        )
        assert re.search(printed, text), f"{variant.tags}: options differ from the printed order"
        assert variant.prompt.get("es") in text, f"{variant.tags}: stem differs from the printed one"


def test_table_questions_are_the_printed_groups(exam: Exam) -> None:
    expected = {
        f"{use.section}-{n}"
        for use in TABLE_USES
        if use.exam_code == exam.code
        for n in range(use.first, use.last + 1)
    }
    with_table = {v.tags[1] for v in config(exam.slug).variants if v.table is not None}
    assert with_table == expected


def test_tables_are_rectangular_text(exam: Exam) -> None:
    text = questionnaire_text(exam).casefold()
    for variant in config(exam.slug).variants:
        table = variant.table
        if table is None:
            continue
        assert table.rows
        assert all(len(row) == len(table.header) for row in table.rows)
        assert all(isinstance(cell, str) for row in table.rows for cell in row)
        if table.title != "Cuadro Laboratorios":
            assert table.title.split(". ")[0].casefold() in text


def test_questions_that_mention_a_table_carry_one(exam: Exam) -> None:
    mentions = re.compile(
        r"\b(tablas?|cuadro)\b (de )?(los datos|Biblioteca|Laboratorios|Academia|Archivos)", re.I
    )
    for variant in config(exam.slug).variants:
        if mentions.search(variant.prompt.get("es")):
            assert variant.table is not None, variant.tags


def test_table_questions_recompute_to_the_official_key(exam: Exam) -> None:
    checks = check_exam(exam.slug)
    assert len(checks) == sum(v.table is not None for v in config(exam.slug).variants)
    assert [c for c in checks if not c.ok] == []


@pytest.mark.parametrize("slug", ["ofi-conv2024-a", "ofi-conv2024-b"])
def test_laboratorios_table_is_the_ledger_transcription(slug: str) -> None:
    tables = [v.table for v in config(slug).variants if v.table and v.table.title == "Cuadro Laboratorios"]
    assert len(tables) == 6
    transcription = ledger().laboratorios
    assert len(transcription) == 10
    for table in tables:
        assert [tuple(row) for row in table.rows] == list(transcription)
        assert table.header == [
            "Profesor",
            "Materia",
            "Día",
            "Hora",
            "Inscritos",
            "Planta",
            "Aula",
            "Capacidad",
        ]


def test_the_files_are_generated_without_yaml_aliases(exam: Exam) -> None:
    text = exercise_text(exam.slug)
    assert text.startswith("# SPDX-License-Identifier: AGPL-3.0-only\n# Generated by")
    assert not re.search(r"[&*]id\d{3}", text)


# --- the presets that serve the sets (course.yaml) ---

_PRESETS = {
    "conv2025-a": "ofi-conv2025-a",
    "conv2025-b": "ofi-conv2025-b",
    "conv2024-a": "ofi-conv2024-a",
    "conv2024-b": "ofi-conv2024-b",
    "conv2024-x": "ofi-conv2024-x",
    "conv2022": "ofi-conv2022",
    "conv2020": "ofi-conv2020",
    "conv2020-x": "ofi-conv2020-x",
}


def _course_registry() -> CourseRegistry:
    from tradeschool.content.registry import load_registry

    return load_registry(Path(__file__).resolve().parents[2] / "content" / "age-auxiliar-c2")


@pytest.mark.parametrize(("preset_id", "exercise_id"), list(_PRESETS.items()))
def test_each_official_preset_serves_its_set_as_printed_with_the_inap_attribution(
    preset_id: str, exercise_id: str
) -> None:
    from tradeschool.exams.draw import DrawnPart, SeededRand, draw_part

    registry = _course_registry()
    preset = next(p for p in registry.manifest.exams if p.id == preset_id)
    assert registry.is_official(exercise_id)
    assert (preset.time_limit_minutes, preset.pause) == (90, "never")
    (part,) = preset.parts
    assert part.draw == "all" and part.penalty == Fraction(1, 3) and part.scoring is None
    config = registry.get_exercise_config(exercise_id)
    assert config is not None and isinstance(config[1], QuizConfig)
    assert config[1].shuffle is False
    drawn: DrawnPart = draw_part(registry, part, None, SeededRand(1))
    assert [q.variant_id for q in drawn.questions] == [v.id for v in config[1].variants]
    description = preset.description.get("es") if preset.description else ""
    assert "Instituto Nacional de Administración Pública (INAP)" in description
    assert f"Se incluyen {len(config[1].variants)} " in description


def test_the_description_counts_the_excluded_questions_the_ledger_lists() -> None:
    registry = _course_registry()
    ledger = parse_ledger()
    for preset_id, exercise_id in _PRESETS.items():
        preset = next(p for p in registry.manifest.exams if p.id == preset_id)
        assert preset.description is not None
        code = next(e.code for e in EXAMS if e.slug == exercise_id)
        excluded = sum(1 for row in ledger.exams[code] if row.estado not in ("vigente", "vigente-con-nota"))
        assert f"se excluyen {excluded}:" in preset.description.get("es"), preset_id


def test_every_note_renders_in_the_sitting_and_the_printed_paper_carries_the_tables() -> None:
    from tradeschool.exams.print_export import build_exam_print

    registry = _course_registry()
    for preset_id, exercise_id in _PRESETS.items():
        config = registry.get_exercise_config(exercise_id)
        assert config is not None and isinstance(config[1], QuizConfig)
        noted = [v for v in config[1].variants if v.explanation is not None]
        generator = QuizGenerator()
        for variant in noted:
            graded = generator.grade(config[1].only(variant.id) or config[1], 0, {"optionId": ""}, "es")
            assert graded.explanation and graded.explanation.strip(), (preset_id, variant.id)
        paper = build_exam_print(registry, preset_id, "es", seed=3)
        printed = paper["parts"][0]["questions"]
        assert len(printed) == len(config[1].variants)
        assert (
            sum("table" in q for q in printed) == sum(v.table is not None for v in config[1].variants) == 12
        )
        assert [o["letter"] for o in printed[0]["options"]] == ["A", "B", "C", "D"]
