# SPDX-License-Identifier: AGPL-3.0-only
"""Build the «Exámenes oficiales» exercises of age-auxiliar-c2 from the official PDFs and the ledger."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

_BACKEND = Path(__file__).resolve().parent.parent
if str(_BACKEND) not in sys.path:
    sys.path.insert(0, str(_BACKEND))

from scripts.c2_official_exam_tables import (  # noqa: E402
    LABORATORIOS_HEADER,
    TABLE_USES,
    TABLES,
    PrintedTable,
    Row,
)

REPO_ROOT = _BACKEND.parent
CONTENT_DIR = REPO_ROOT / "content" / "age-auxiliar-c2"
OFFICIAL_DIR = CONTENT_DIR / "sources" / "examenes-oficiales"
LEDGER_PATH = REPO_ROOT / "docs" / "age-c2-official-exams-ledger.md"
EXERCISES_DIR = CONTENT_DIR / "exercises"
REPORT_DIR = REPO_ROOT / "docs" / "age-verification" / "c2" / "official"

SECTIONS = ("P1", "R1", "P2", "R2")
SECTION_SIZES = {"P1": 60, "R1": 5, "P2": 50, "R2": 5}
LEDGER_SECTION_TITLES = {
    "Primera parte": "P1",
    "Primera parte — preguntas de reserva": "R1",
    "Segunda parte": "P2",
    "Segunda parte — preguntas de reserva": "R2",
}
INCLUDED_STATES = ("vigente", "vigente-con-nota")
LABORATORIOS_TITLE = "Cuadro Laboratorios"


@dataclass(frozen=True)
class Exam:
    code: str
    slug: str
    title: str
    pdf: Path


EXAMS = (
    Exam(
        "conv2025_A",
        "ofi-conv2025-a",
        "Examen oficial 2025 · Modelo A",
        Path("2026-05-23_conv2025_modeloA_cuestionario.pdf"),
    ),
    Exam(
        "conv2025_B",
        "ofi-conv2025-b",
        "Examen oficial 2025 · Modelo B",
        Path("2026-05-23_conv2025_modeloB_cuestionario.pdf"),
    ),
    Exam(
        "conv2024_A",
        "ofi-conv2024-a",
        "Examen oficial 2024 · Modelo A",
        Path("conv2024_modeloA_cuestionario.pdf"),
    ),
    Exam(
        "conv2024_B",
        "ofi-conv2024-b",
        "Examen oficial 2024 · Modelo B",
        Path("conv2024_modeloB_cuestionario.pdf"),
    ),
    Exam(
        "conv2024_X",
        "ofi-conv2024-x",
        "Examen oficial 2024 · Extraordinario",
        Path("conv2024_extraordinario_cuestionario.pdf"),
    ),
    Exam("conv2022", "ofi-conv2022", "Examen oficial 2022", Path("conv2022_cuestionario.pdf")),
    Exam("conv2020", "ofi-conv2020", "Examen oficial 2020", Path("conv2020_cuestionario.pdf")),
    Exam(
        "conv2020_X",
        "ofi-conv2020-x",
        "Examen oficial 2020 · Extraordinario",
        Path("conv2020_extraordinario_cuestionario.pdf"),
    ),
)


# ---------------------------------------------------------------- ledger


@dataclass(frozen=True)
class LedgerRow:
    section: str
    number: int
    estado: str
    clave: str
    nota_clave: str
    nota: str

    @property
    def included(self) -> bool:
        return self.estado in INCLUDED_STATES

    @property
    def status(self) -> str:
        return self.estado.split(":")[0].strip()


@dataclass(frozen=True)
class Ledger:
    exams: dict[str, list[LedgerRow]]
    laboratorios: tuple[Row, ...]


def _table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_ledger(path: Path = LEDGER_PATH) -> Ledger:
    exams: dict[str, list[LedgerRow]] = {}
    laboratorios: list[Row] = []
    code = ""
    section = ""
    in_laboratorios = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            title = line[3:].split(" — ")[0].strip()
            in_laboratorios = title.startswith("Transcription of the image table")
            code = title if title.startswith("conv20") else ""
            section = ""
            if code:
                exams[code] = []
        elif line.startswith("### "):
            section = LEDGER_SECTION_TITLES.get(line[4:].strip(), "")
        elif in_laboratorios and line.startswith("|"):
            cells = _table_cells(line)
            if cells[0] != "Profesor" and not cells[0].startswith("---"):
                laboratorios.append(tuple(cells))
        elif code and section and re.match(r"\| \d+ \|", line):
            cells = _table_cells(line)
            assert len(cells) == 6, f"{code} {section}: unexpected row {line!r}"
            number, _tema, estado, clave, nota_clave, nota = cells
            exams[code].append(LedgerRow(section, int(number), estado, clave, nota_clave, nota))
    return Ledger(exams, tuple(laboratorios))


# ---------------------------------------------------------------- PDF


@dataclass(frozen=True)
class PdfQuestion:
    section: str
    number: int
    stem: str
    options: tuple[str, str, str, str]
    irregular_number: bool


_FOOTER = re.compile(r"^\s*(Página \d+ de \d+)?\s*(\d{4}\s*-?\s*AUX-L[^\n]*?)?\s*(Página \d+ de \d+)?\s*$")
# «5    En Excel…» prints no period in conv2022 R2; the expected number keeps table rows out
_QUESTION_START = re.compile(r"^\s*(\d+)(?:\.(?:\s+|(?=\D))|\s{3,})\S")


def pdf_lines(pdf: Path) -> list[str]:
    text = subprocess.run(
        ["pdftotext", "-layout", str(OFFICIAL_DIR / pdf), "-"], check=True, capture_output=True, text=True
    ).stdout
    return [line.rstrip() for line in text.splitlines() if line.strip() and not _FOOTER.match(line)]


def pdf_flat_text(pdf: Path) -> str:
    return " ".join(" ".join(pdf_lines(pdf)).split())


def _section_blocks(lines: list[str]) -> dict[str, list[str]]:
    blocks: dict[str, list[str]] = {}
    current = ""
    reserve_seen = 0
    for line in lines:
        stripped = line.strip()
        if stripped == "PRIMERA PARTE":
            current = "P1"
        elif stripped == "SEGUNDA PARTE":
            current = "P2"
        elif stripped == "Preguntas de reserva":
            reserve_seen += 1
            current = f"R{reserve_seen}"
        elif current:
            blocks.setdefault(current, []).append(line)
    return blocks


def _question_blocks(section: str, lines: list[str], cut_patterns: list[re.Pattern[str]]) -> list[list[str]]:
    blocks: list[list[str]] = []
    expected = 1
    current: list[str] | None = None
    for line in lines:
        start = _QUESTION_START.match(line)
        if start and int(start.group(1)) == expected:
            current = [line]
            blocks.append(current)
            expected += 1
        elif any(pattern.match(line.strip()) for pattern in cut_patterns):
            current = None
        elif current is not None:
            current.append(line)
    assert len(blocks) == SECTION_SIZES[section], f"{section}: found {len(blocks)} questions"
    return blocks


def _split_block(section: str, number: int, block: list[str]) -> PdfQuestion:
    first = re.sub(r"^\s*\d+(?:\.\s*|\s{3,})", "", block[0])
    body = [first, *block[1:]]
    option_start = next(i for i, line in enumerate(body) if re.match(r"^\s*a\)\s", line))
    stem = " ".join(" ".join(body[:option_start]).split())
    options_text = " ".join(" ".join(body[option_start:]).split())
    parts = re.split(r"(?:^|\s)([abcd])\)\s+", options_text)
    # parts: ['', 'a', text, 'b', text, ...]; a marker inside the text would break the letter sequence
    letters = parts[1::2]
    assert letters == ["a", "b", "c", "d"], f"{section}-{number}: option markers {letters}"
    texts = tuple(text.strip() for text in parts[2::2])
    irregular = not re.match(r"^\s*\d+\.\s+\S", block[0])
    return PdfQuestion(section, number, stem, (texts[0], texts[1], texts[2], texts[3]), irregular)


def parse_pdf(exam: Exam) -> dict[tuple[str, int], PdfQuestion]:
    cut_patterns = [
        re.compile(TABLES[use.table_key].cut_pattern or "(?!)")
        for use in TABLE_USES
        if use.exam_code == exam.code and use.table_key in TABLES
    ]
    blocks_by_section = _section_blocks(pdf_lines(exam.pdf))
    questions: dict[tuple[str, int], PdfQuestion] = {}
    for section in SECTIONS:
        for number, block in enumerate(
            _question_blocks(section, blocks_by_section[section], cut_patterns), 1
        ):
            questions[(section, number)] = _split_block(section, number, block)
    return questions


# ---------------------------------------------------------------- notes

_NOTE_PREFIX = re.compile(r"^(Modelo B: [PR][12] \d+\.|= modelo A [PR][12] \d+\.)\s*")
_SENTENCE_BREAK = re.compile(r"(?<=[.)»])\s+(?=[A-ZÁÉÍÓÚ])")
_DROPPED_SENTENCES = (
    "Tabla «",
    "La plantilla definitiva imprime",
    "La plantilla podría corresponder",
    "Decisión del coordinador",
)


def _kept_sentences(text: str) -> list[str]:
    return [s for s in _SENTENCE_BREAK.split(text) if s and not s.startswith(_DROPPED_SENTENCES)]


def learner_note(row: LedgerRow) -> str:
    sentences = [*_kept_sentences(row.nota_clave), *_kept_sentences(_NOTE_PREFIX.sub("", row.nota))]
    return " ".join(s if s.endswith(".") else f"{s}." for s in sentences)


# ---------------------------------------------------------------- tables


def laboratorios_table(ledger: Ledger) -> PrintedTable:
    return PrintedTable("laboratorios", (LABORATORIOS_TITLE,), LABORATORIOS_HEADER, ledger.laboratorios, None)


def table_title(table: PrintedTable) -> str:
    return ". ".join((*table.title_parts, *([table.side_note] if table.side_note else [])))


def table_payload(table: PrintedTable) -> dict[str, object]:
    return {
        "title": table_title(table),
        "header": list(table.header),
        "rows": [list(row) for row in table.rows],
    }


def assert_table_printed(table: PrintedTable, flat_text: str) -> None:
    folded = flat_text.casefold()
    for part in table.title_parts:
        assert part.casefold() in folded, f"table {table.key}: {part!r} is not in the PDF text"


# ---------------------------------------------------------------- build


def variant_payload(
    variant_id: str, row: LedgerRow, code: str, question: PdfQuestion, table: PrintedTable | None
) -> dict[str, object]:
    key = row.clave.strip()[:1].lower()
    assert key in ("a", "b", "c", "d"), f"{code} {row.section}-{row.number}: key {row.clave!r}"
    variant: dict[str, object] = {
        "id": variant_id,
        "kind": "single_choice",
        "prompt": {"es": question.stem},
        "options": [
            {"id": letter, "text": {"es": text}, "correct": letter == key}
            for letter, text in zip("abcd", question.options, strict=True)
        ],
        "tags": [code, f"{row.section}-{row.number}"],
    }
    if table is not None:
        variant["table"] = table_payload(table)
    if row.estado == "vigente-con-nota":
        note = learner_note(row)
        assert note, f"{code} {row.section}-{row.number}: vigente-con-nota without a note"
        variant["explanation"] = {"es": note}
    return variant


def tables_by_question(exam: Exam, ledger: Ledger) -> dict[tuple[str, int], PrintedTable]:
    flat_text = pdf_flat_text(exam.pdf)
    by_question: dict[tuple[str, int], PrintedTable] = {}
    for use in TABLE_USES:
        if use.exam_code != exam.code:
            continue
        table = laboratorios_table(ledger) if use.table_key == "laboratorios" else TABLES[use.table_key]
        if table.cut_pattern is not None:
            assert_table_printed(table, flat_text)
        for number in range(use.first, use.last + 1):
            by_question[(use.section, number)] = table
    return by_question


def build_exam(exam: Exam, ledger: Ledger) -> dict[str, object]:
    rows = ledger.exams[exam.code]
    assert len(rows) == 120, f"{exam.code}: {len(rows)} ledger rows"
    questions = parse_pdf(exam)
    tables = tables_by_question(exam, ledger)
    variants: list[dict[str, object]] = []
    for row in rows:
        if not row.included:
            continue
        key = (row.section, row.number)
        variants.append(
            variant_payload(f"q{len(variants) + 1:03d}", row, exam.code, questions[key], tables.get(key))
        )
    return {"type": "quiz", "shuffle": False, "variants": variants}


def write_exercise(exam: Exam, payload: dict[str, object]) -> None:
    header = (
        "# SPDX-License-Identifier: AGPL-3.0-only\n"
        "# Generated by backend/scripts/build_c2_official_exams.py from the official PDF and the ledger.\n"
    )
    body = yaml.dump(payload, allow_unicode=True, sort_keys=False, width=110)
    (EXERCISES_DIR / f"{exam.slug}.yaml").write_text(header + body, encoding="utf-8")


def exam_summary(
    exam: Exam, ledger: Ledger, questions: dict[tuple[str, int], PdfQuestion]
) -> dict[str, object]:
    rows = ledger.exams[exam.code]
    excluded: dict[str, list[str]] = {}
    for row in rows:
        if not row.included:
            excluded.setdefault(row.status, []).append(f"{row.section}-{row.number}")
    tables = tables_by_question(exam, ledger)
    return {
        "slug": exam.slug,
        "ledgerCode": exam.code,
        "title": exam.title,
        "total": len(rows),
        "included": sum(row.included for row in rows),
        "vigenteConNota": sum(row.estado == "vigente-con-nota" for row in rows),
        "excluded": excluded,
        "tableQuestions": len(tables),
        "tables": sorted({table.key for table in tables.values()}),
        "irregularNumberPrint": [f"{q.section}-{q.number}" for q in questions.values() if q.irregular_number],
    }


def main() -> None:
    ledger = parse_ledger()
    summaries = []
    for exam in EXAMS:
        write_exercise(exam, build_exam(exam, ledger))
        summaries.append(exam_summary(exam, ledger, parse_pdf(exam)))
        print(f"{exam.slug}: {summaries[-1]['included']} included")
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / "summary.json").write_text(
        json.dumps(summaries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
