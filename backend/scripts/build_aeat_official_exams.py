# SPDX-License-Identifier: AGPL-3.0-only
"""Build the «Exámenes oficiales» of aeat-agentes-hacienda from the parsed papers, key sheets and ledger."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path

import yaml

_BACKEND = Path(__file__).resolve().parent.parent
REPO_ROOT = _BACKEND.parent
CONTENT_DIR = REPO_ROOT / "content" / "aeat-agentes-hacienda"
EXERCISES_DIR = CONTENT_DIR / "exercises"
LEDGER_PATH = REPO_ROOT / "docs" / "aeat-official-exams-ledger.md"
R0A_DIR = REPO_ROOT / "docs" / "age-verification" / "aeat" / "r0a"
REPORT_DIR = REPO_ROOT / "docs" / "age-verification" / "aeat" / "official"

INCLUDED_STATES = ("vigente", "vigente-con-nota")
LETTERS = "ABCD"


@dataclass(frozen=True)
class Exam:
    code: str
    slug: str
    ledger_heading: str
    tipo: str
    title: str
    minutes: int


def _exam(year: str, tipo: str, heading: str, minutes: int, name: str | None = None) -> Exam:
    suffix = tipo.lower()
    label = name or f"OEP {year}"
    return Exam(
        f"conv{year}_{tipo}",
        f"ofi-conv{year}-{suffix}",
        heading,
        tipo,
        f"{label} · Tipo {tipo}" if tipo != "X" else label,
        minutes,
    )


EXAMS = (
    _exam("2025", "A", "OEP 2025, 21-03-2026", 90),
    _exam("2025", "B", "OEP 2025, 21-03-2026", 90),
    _exam("2024", "A", "OEP 2024, 05-04-2025", 100),
    _exam("2024", "B", "OEP 2024, 05-04-2025", 100),
    _exam("2023", "A", "OEP 2023, 20-04-2024", 100),
    _exam("2023", "B", "OEP 2023, 20-04-2024", 100),
    _exam("2022", "A", "OEP 2022, 22-04-2023", 100),
    _exam("2022", "B", "OEP 2022, 22-04-2023", 100),
    _exam("2022", "X", "OEP 2022 extraordinario, 18-07-2023", 100, "OEP 2022 · Extraordinario"),
    _exam("2021", "A", "OEP 2021, 28-05-2022", 60),
    _exam("2021", "B", "OEP 2021, 28-05-2022", 60),
    _exam("2020", "A", "OEP 2020, 25-09-2021", 60),
    _exam("2020", "B", "OEP 2020, 25-09-2021", 60),
)


@dataclass(frozen=True)
class LedgerRow:
    number: int
    tipo_b: tuple[int, ...]
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


def parse_ledger(path: Path = LEDGER_PATH) -> dict[str, list[LedgerRow]]:
    sections: dict[str, list[LedgerRow]] = {}
    heading = ""
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            heading = line[3:].strip()
            if heading.startswith("OEP "):
                sections[heading] = []
            continue
        if heading in sections and re.match(r"\| \d+ \|", line):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            assert len(cells) == 7, f"{heading}: unexpected row {line!r}"
            number, tipo_b, _tema, estado, clave, nota_clave, nota = cells
            twins = tuple(int(n) for n in re.findall(r"\d+", tipo_b))
            sections[heading].append(LedgerRow(int(number), twins, estado, clave, nota_clave, nota))
    return sections


def _questionnaire(exam: Exam) -> list[dict[str, object]]:
    parsed: list[dict[str, object]] = json.loads(
        (R0A_DIR / "parsed" / f"{exam.code}.json").read_text(encoding="utf-8")
    )
    return parsed


def _key_sheet(exam: Exam) -> dict[str, str]:
    keys: dict[str, str] = json.loads((R0A_DIR / "keys" / f"{exam.code}.json").read_text(encoding="utf-8"))
    return keys


_SENTENCE_BREAK = re.compile(r"(?<=[.)»])\s+(?=[A-ZÁÉÍÓÚ])")
_BOOKKEEPING = ("Texto descargado",)


def _sentences(text: str) -> list[str]:
    return [s for s in _SENTENCE_BREAK.split(text.strip()) if s and not s.startswith(_BOOKKEEPING)]


def learner_note(row: LedgerRow) -> str:
    errata = [s for s in _sentences(row.nota) if s.startswith("Errata")]
    sentences = [*_sentences(row.nota_clave), *errata]
    return " ".join(s if s.endswith(".") else f"{s}." for s in sentences)


_LINE_BREAK_HYPHEN = re.compile(r"(\w)- (\w)")


def _printed(text: object) -> str:
    """The paper's text with the hyphen of a compound split at a line end closed up again."""
    return _LINE_BREAK_HYPHEN.sub(r"\1-\2", str(text))


@dataclass(frozen=True)
class PrintedQuestion:
    printed: int
    ledger: LedgerRow
    stem: str
    options: tuple[str, str, str, str]
    key: str


def printed_questions(exam: Exam, rows: list[LedgerRow]) -> list[PrintedQuestion]:
    """Every question of the questionnaire in printed order, with the ledger row of its tipo A twin."""
    by_a = {row.number: row for row in rows}
    keys = _key_sheet(exam)
    twin_of: dict[int, LedgerRow] = {}
    if exam.tipo == "B":
        for row in rows:
            for b in row.tipo_b:
                twin_of[b] = row
    out: list[PrintedQuestion] = []
    for item in _questionnaire(exam):
        n = int(str(item["n"]))
        row = twin_of[n] if exam.tipo == "B" else by_a[n]
        options = (_printed(item["A"]), _printed(item["B"]), _printed(item["C"]), _printed(item["D"]))
        key = keys[str(n)]
        if row.included:
            assert key in LETTERS, f"{exam.code} {n}: key {key!r}"
            assert key == str(item["key"]), f"{exam.code} {n}: parsed key and sheet differ"
            if exam.tipo != "B":
                assert key == row.clave.strip()[:1], f"{exam.code} {n}: ledger key {row.clave!r}"
        out.append(PrintedQuestion(n, row, _printed(item["stem"]), options, key))
    return out


def _words(texts: tuple[str, ...]) -> list[str]:
    return [re.sub(r"\W+", " ", text).strip().casefold() for text in texts]


def check_twins(exam: Exam, rows: list[LedgerRow]) -> None:
    """A tipo B question keys its tipo A twin's option in the same letter, a printed typo aside."""
    if exam.tipo != "B":
        return
    a = next(e for e in EXAMS if e.code == exam.code.replace("_B", "_A"))
    a_by_number = {q.printed: q for q in printed_questions(a, rows)}
    for q in printed_questions(exam, rows):
        if not q.ledger.included:
            continue
        twin = a_by_number[q.ledger.number]
        for mine, theirs in zip(_words(q.options), _words(twin.options), strict=True):
            assert SequenceMatcher(None, mine, theirs).ratio() > 0.97, (
                f"{exam.code} {q.printed}: options differ from tipo A"
            )
        assert q.key == twin.key, f"{exam.code} {q.printed}: key differs from tipo A"


def variant_payload(variant_id: str, exam: Exam, question: PrintedQuestion) -> dict[str, object]:
    variant: dict[str, object] = {
        "id": variant_id,
        "kind": "single_choice",
        "prompt": {"es": question.stem},
        "options": [
            {"id": letter.lower(), "text": {"es": text}, "correct": letter == question.key}
            for letter, text in zip(LETTERS, question.options, strict=True)
        ],
        "tags": [exam.code, f"Q{question.printed}"],
    }
    if question.ledger.estado == "vigente-con-nota":
        note = learner_note(question.ledger)
        assert note, f"{exam.code} {question.printed}: vigente-con-nota without a note"
        variant["explanation"] = {"es": note}
    return variant


def build_exam(exam: Exam, sections: dict[str, list[LedgerRow]]) -> dict[str, object]:
    rows = sections[exam.ledger_heading]
    check_twins(exam, rows)
    included = [q for q in printed_questions(exam, rows) if q.ledger.included]
    variants = [variant_payload(f"q{number:03d}", exam, q) for number, q in enumerate(included, start=1)]
    return {"type": "quiz", "shuffle": False, "variants": variants}


def exam_summary(exam: Exam, sections: dict[str, list[LedgerRow]]) -> dict[str, object]:
    questions = printed_questions(exam, sections[exam.ledger_heading])
    excluded: dict[str, list[int]] = {}
    for question in questions:
        if not question.ledger.included:
            excluded.setdefault(question.ledger.status, []).append(question.printed)
    return {
        "slug": exam.slug,
        "code": exam.code,
        "title": exam.title,
        "minutes": exam.minutes,
        "printed": len(questions),
        "included": sum(q.ledger.included for q in questions),
        "withNote": sum(q.ledger.estado == "vigente-con-nota" for q in questions),
        "excluded": {status: len(numbers) for status, numbers in excluded.items()},
    }


def write_exercise(exam: Exam, payload: dict[str, object]) -> None:
    header = (
        "# SPDX-License-Identifier: AGPL-3.0-only\n"
        "# Generated by backend/scripts/build_aeat_official_exams.py from the parsed questionnaire, the\n"
        "# definitive answer sheet and docs/aeat-official-exams-ledger.md.\n"
    )
    body = yaml.dump(payload, allow_unicode=True, sort_keys=False, width=110)
    (EXERCISES_DIR / f"{exam.slug}.yaml").write_text(header + body, encoding="utf-8")


def main() -> None:
    sections = parse_ledger()
    summaries = []
    for exam in EXAMS:
        write_exercise(exam, build_exam(exam, sections))
        summaries.append(exam_summary(exam, sections))
        print(f"{exam.slug}: {summaries[-1]['included']} of {summaries[-1]['printed']} included")
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / "summary.json").write_text(
        json.dumps(summaries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
