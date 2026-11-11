"""Parse the AEAT first-exercise questionnaires and answer sheets into parsed/<exam>.json."""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
SRC = ROOT / "content/aeat-agentes-hacienda/sources/examenes-oficiales"
OUT = ROOT / "docs/age-verification/aeat/r0a/parsed"

# exam id -> (questionnaire, answer sheet)
EXAMS: dict[str, tuple[str, str]] = {
    "conv2020_A": ("2021-09-25_conv2020_tipoA_cuestionario.pdf", "2021-09-25_conv2020_tipoA_plantilla-definitiva.pdf"),
    "conv2020_B": ("2021-09-25_conv2020_tipoB_cuestionario.pdf", "2021-09-25_conv2020_tipoB_plantilla-definitiva.pdf"),
    "conv2021_A": ("2022-05-28_conv2021_tipoA_cuestionario.pdf", "2022-05-28_conv2021_tipoA_plantilla-definitiva.pdf"),
    "conv2021_B": ("2022-05-28_conv2021_tipoB_cuestionario.pdf", "2022-05-28_conv2021_tipoB_plantilla-definitiva.pdf"),
    "conv2022_A": ("2023-04-22_conv2022_tipoA_cuestionario.pdf", "2023-04-22_conv2022_tipoA_plantilla-definitiva.pdf"),
    "conv2022_B": ("2023-04-22_conv2022_tipoB_cuestionario.pdf", "2023-04-22_conv2022_tipoB_plantilla-definitiva.pdf"),
    "conv2022_X": (
        "2023-07-18_conv2022_extraordinario_tipoA_cuestionario.pdf",
        "2023-07-18_conv2022_extraordinario_tipoA_plantilla-provisional.pdf",
    ),
    "conv2023_A": ("2024-04-20_conv2023_tipoA_cuestionario.pdf", "2024-04-20_conv2023_tipoA_plantilla-definitiva.pdf"),
    "conv2023_B": ("2024-04-20_conv2023_tipoB_cuestionario.pdf", "2024-04-20_conv2023_tipoB_plantilla-definitiva.pdf"),
    "conv2024_A": ("2025-04-05_conv2024_tipoA_cuestionario.pdf", "2025-04-05_conv2024_tipoA_plantilla-definitiva.pdf"),
    "conv2024_B": ("2025-04-05_conv2024_tipoB_cuestionario.pdf", "2025-04-05_conv2024_tipoB_plantilla-definitiva.pdf"),
    "conv2025_A": ("2026-03-21_conv2025_tipoA_cuestionario.pdf", "2026-03-21_conv2025_tipoA_plantilla-definitiva.pdf"),
    "conv2025_B": ("2026-03-21_conv2025_tipoB_cuestionario.pdf", "2026-03-21_conv2025_tipoB_plantilla-definitiva.pdf"),
}

NOISE = re.compile(
    r"^\s*(TIPO [AB]|ACCESO LIBRE.*|TURNO LIB.*|TIPO|Agencia Tributaria|AGENCIA TRIBUTARIA|PROCESO SELECTIVO.*|"
    r".*ESPECIALIDAD DE AGENTES.*|.*CONVOCADO POR RESOLUCI.*|ADMINISTRACI[ÓO]N DEL ESTADO.*|DEL ESTADO, ESPECIALIDAD.*|"
    r"-{10,}|P[áa]gina \d+.*|\d{1,2}|\d+ de \d+)\s*$"
)
QUESTION = re.compile(r"^\s{0,8}(\d{1,3})\s*\.\s*-?\s*(\S.*)$")
OPTION = re.compile(r"^\s*([A-D])(?:\s*(?:\.-|\)|-|\.)|\s{2,})\s*(.*)$")  # a bare letter + spaces is a misprint (conv2020 A 9)


def pdf_text(path: Path) -> str:
    return subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True).stdout


def clean(parts: list[str]) -> str:
    text = " ".join(p.strip() for p in parts if p.strip())
    return re.sub(r"\s+", " ", text).strip()


def parse_questionnaire(text: str) -> list[dict[str, object]]:
    lines = [ln for ln in text.splitlines() if not NOISE.match(ln)]
    questions: list[dict[str, object]] = []
    expected = 1
    current: dict[str, list[str]] | None = None
    option_key = ""
    for line in lines:
        q = QUESTION.match(line)
        if q and int(q.group(1)) == expected:
            if current is not None:
                questions.append(current)
            current = {"n": expected, "stem": [q.group(2)], "A": [], "B": [], "C": [], "D": []}  # type: ignore[dict-item]
            option_key = "stem"
            expected += 1
            continue
        if current is None:
            continue
        o = OPTION.match(line)
        next_letter = "ABCD"["ABCD".index(option_key) + 1] if option_key in "ABC" else ("A" if option_key == "stem" else "")
        if o and o.group(1) == next_letter:
            option_key = o.group(1)
            current[option_key].append(o.group(2))
            continue
        current[option_key].append(line)
    if current is not None:
        questions.append(current)
    return [
        {"n": q["n"], "stem": clean(q["stem"]), **{k: clean(q[k]) for k in "ABCD"}}  # type: ignore[arg-type]
        for q in questions
    ]


def parse_key(text: str) -> dict[int, str]:
    keys: dict[int, str] = {}
    for m in re.finditer(r"(?<![\d/.])(\d{1,3})(?:\s+|-)(ANULADA|[A-D])\b", text):
        keys[int(m.group(1))] = m.group(2)
    return keys


def main(only: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for exam, (qfile, kfile) in EXAMS.items():
        if only and exam not in only:
            continue
        questions = parse_questionnaire(pdf_text(SRC / qfile))
        keys = parse_key(pdf_text(SRC / kfile))
        for q in questions:
            q["key"] = keys.get(int(q["n"]), "?")  # type: ignore[arg-type]
        problems = [q["n"] for q in questions if not all(q[k] for k in ("stem", "A", "B", "C", "D"))]
        (OUT / f"{exam}.json").write_text(json.dumps(questions, ensure_ascii=False, indent=1))
        print(exam, "questions", len(questions), "keys", len(keys), "max key", max(keys), "incomplete", problems)


if __name__ == "__main__":
    main(sys.argv[1:])
