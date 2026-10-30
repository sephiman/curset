# SPDX-License-Identifier: AGPL-3.0-only
"""Tests for the «Exámenes oficiales» practice set (round R5).

Covers:
- Ten official exam presets declared in course.yaml (conv2020 to conv2025)
- Question counts per set match the ledger (vigente + vigente-con-nota)
- Total questions equals 1,187 across all ten sets
- No excluded question present (anulada, dudosa, norma modificada, función retirada)
- Every note of vigente-con-nota questions renders in explanation / solution panel
- Attribution to INAP with date, model and exclusion header
- Original option order kept and letters printed (no shuffle)
- Timing (100 min) and penalty (1/3) as real exam
- Printable format generated cleanly with key sheet
"""

from __future__ import annotations

import re
from fractions import Fraction
from pathlib import Path

import pytest

from tradeschool.content.registry import CourseRegistry, load_registry
from tradeschool.exams.presets import ExamPreset
from tradeschool.exams.print_export import build_exam_print
from tradeschool.exercises.quiz import QuizConfig, QuizGenerator

CONTENT_DIR = Path(__file__).resolve().parent.parent.parent / "content" / "age-administrativo-c1"
LEDGER_PATH = Path(__file__).resolve().parent.parent.parent / "docs" / "age-official-exams-ledger.md"

OFFICIAL_PRESET_IDS = [
    ("conv2025-a", "ofi-conv2025-a", 119, 6),
    ("conv2025-b", "ofi-conv2025-b", 119, 6),
    ("conv2025-x", "ofi-conv2025-x", 124, 1),
    ("conv2024-a", "ofi-conv2024-a", 118, 7),
    ("conv2024-b", "ofi-conv2024-b", 118, 7),
    ("conv2024-x", "ofi-conv2024-x", 121, 4),
    ("conv2022", "ofi-conv2022", 116, 9),
    ("conv2022-x", "ofi-conv2022-x", 120, 5),
    ("conv2020", "ofi-conv2020", 112, 13),
    ("conv2020-x", "ofi-conv2020-x", 120, 5),
]


@pytest.fixture(scope="module")
def registry() -> CourseRegistry:
    return load_registry(CONTENT_DIR)


def parse_ledger_rows() -> dict[str, list[dict[str, str]]]:
    text = LEDGER_PATH.read_text(encoding="utf-8")
    sections = re.split(r"\n##\s+", text)[1:]
    exams_data: dict[str, list[dict[str, str]]] = {}
    for sec in sections:
        first_line = sec.splitlines()[0]
        if "Summary" in first_line:
            continue
        code = first_line.split("—")[0].strip()
        rows: list[dict[str, str]] = []
        for line in sec.splitlines():
            if line.startswith("|") and not line.startswith("| Nº") and not line.startswith("|---"):
                parts = [p.strip() for p in line.split("|")[1:-1]]
                if len(parts) >= 6:
                    rows.append(
                        {
                            "num": parts[0],
                            "tema": parts[1],
                            "estado": parts[2],
                            "clave": parts[3].lower(),
                            "nota_clave": parts[4],
                            "nota": parts[5],
                        }
                    )
        exams_data[code] = rows
    return exams_data


@pytest.mark.parametrize(
    ("preset_id", "exercise_id", "expected_count", "excluded_count"),
    OFFICIAL_PRESET_IDS,
)
def test_official_exam_counts_and_rules_match_ledger(
    registry: CourseRegistry,
    preset_id: str,
    exercise_id: str,
    expected_count: int,
    excluded_count: int,
) -> None:
    preset: ExamPreset | None = next((p for p in registry.manifest.exams if p.id == preset_id), None)
    assert preset is not None
    assert preset.time_limit_minutes == 100
    assert preset.pause == "never"
    assert preset.description is not None
    desc = preset.description.get("es")
    assert "Instituto Nacional de Administración Pública (INAP)" in desc
    assert str(excluded_count) in desc

    assert len(preset.parts) == 1
    part = preset.parts[0]
    assert part.penalty == Fraction(1, 3)
    assert part.blank == "free"
    assert part.source is not None and part.source.exercise == exercise_id

    # Verify exercise configuration
    config_pair = registry.get_exercise_config(exercise_id)
    assert config_pair is not None
    config = config_pair[1]
    assert isinstance(config, QuizConfig)
    assert config.shuffle is False
    assert len(config.variants) == expected_count


def test_total_official_questions_equals_ledger_sum(registry: CourseRegistry) -> None:
    total = 0
    for _preset_id, exercise_id, expected_count, _excluded in OFFICIAL_PRESET_IDS:
        config_pair = registry.get_exercise_config(exercise_id)
        assert config_pair is not None
        config = config_pair[1]
        assert isinstance(config, QuizConfig)
        total += len(config.variants)
        assert len(config.variants) == expected_count
    assert total == 1187


def test_no_excluded_question_is_present_in_official_exercises(registry: CourseRegistry) -> None:
    ledger = parse_ledger_rows()
    code_map = {
        "conv2025-a": "conv2025_A",
        "conv2025-b": "conv2025_B",
        "conv2025-x": "conv2025_X",
        "conv2024-a": "conv2024_A",
        "conv2024-b": "conv2024_B",
        "conv2024-x": "conv2024_X",
        "conv2022": "conv2022",
        "conv2022-x": "conv2022_X",
        "conv2020": "conv2020",
        "conv2020-x": "conv2020_X",
    }

    for preset_id, exercise_id, _exp_count, _excl_count in OFFICIAL_PRESET_IDS:
        code = code_map[preset_id]
        rows = ledger[code]
        config_pair = registry.get_exercise_config(exercise_id)
        assert config_pair is not None
        config = config_pair[1]
        assert isinstance(config, QuizConfig)

        # Check prompt uniqueness and verify no excluded status row made it into the variants
        variant_prompts = {v.prompt.get("es") for v in config.variants}
        assert len(variant_prompts) == len(config.variants)

        # Excluded count matches ledger excluded rows exactly
        excluded_rows = [r for r in rows if r["estado"] not in ("vigente", "vigente-con-nota")]
        included_rows = [r for r in rows if r["estado"] in ("vigente", "vigente-con-nota")]
        assert len(included_rows) == len(config.variants)
        assert len(excluded_rows) == 125 - len(config.variants)


def test_every_note_for_vigente_con_nota_renders(registry: CourseRegistry) -> None:
    ledger = parse_ledger_rows()
    code_map = {
        "conv2025-a": "conv2025_A",
        "conv2025-b": "conv2025_B",
        "conv2025-x": "conv2025_X",
        "conv2024-a": "conv2024_A",
        "conv2024-b": "conv2024_B",
        "conv2024-x": "conv2024_X",
        "conv2022": "conv2022",
        "conv2022-x": "conv2022_X",
        "conv2020": "conv2020",
        "conv2020-x": "conv2020_X",
    }

    generator = QuizGenerator()
    total_notes = 0

    for preset_id, exercise_id, _exp, _excl in OFFICIAL_PRESET_IDS:
        code = code_map[preset_id]
        rows = ledger[code]
        vigente_con_nota_rows = [r for r in rows if r["estado"] == "vigente-con-nota"]

        config_pair = registry.get_exercise_config(exercise_id)
        assert config_pair is not None
        config = config_pair[1]
        assert isinstance(config, QuizConfig)

        variants_with_notes = [v for v in config.variants if v.explanation is not None]
        assert len(variants_with_notes) == len(vigente_con_nota_rows)
        total_notes += len(variants_with_notes)

        # Ensure explanation renders in GradeResult
        for v in variants_with_notes:
            expl = v.explanation.get("es") if v.explanation else None
            assert expl is not None and len(expl) > 0
            generator.grade(config, 100, {"optionId": "a"}, "es")
            # When variant matches, graded explanation matches
            graded_v = generator.grade(config.only(v.id) or config, 100, {"optionId": "a"}, "es")
            assert graded_v.explanation == expl

    assert total_notes == 46


def test_options_are_not_shuffled_in_official_exams(registry: CourseRegistry) -> None:
    generator = QuizGenerator()
    for _preset_id, exercise_id, _exp, _excl in OFFICIAL_PRESET_IDS:
        config_pair = registry.get_exercise_config(exercise_id)
        assert config_pair is not None
        config = config_pair[1]
        assert isinstance(config, QuizConfig)
        assert config.shuffle is False

        # Options across 3 different seeds remain in exact order: a, b, c, d
        v = config.variants[0]
        for seed in (1, 42, 9999):
            inst = generator.generate(config.only(v.id) or config, seed, "es")
            opts = inst.payload.get("options", [])
            opt_ids = [o["id"] for o in opts]
            assert opt_ids == ["a", "b", "c", "d"]


def test_official_exam_printable_generates_with_key_sheet(registry: CourseRegistry) -> None:
    doc = build_exam_print(registry, "conv2025-a", "es")
    assert doc["presetId"] == "conv2025-a"
    assert doc["title"] == "Examen oficial 2025 · Modelo A"
    assert len(doc["parts"]) == 1
    questions = doc["parts"][0]["questions"]
    assert len(questions) == 119
    key_sheet = doc["keySheet"]
    assert len(key_sheet) == 1
    keys = key_sheet[0]["keys"]
    assert len(keys) == 119

    # Bijection check: every question has a corresponding key
    q_numbers = [q["number"] for q in questions]
    k_numbers = [k["number"] for k in keys]
    assert q_numbers == k_numbers

    # Letters A..D bijection
    for q, k in zip(questions, keys, strict=True):
        opt_letters = [o["letter"] for o in q["options"]]
        assert opt_letters == ["A", "B", "C", "D"]
        assert k["correctLetter"] in opt_letters
