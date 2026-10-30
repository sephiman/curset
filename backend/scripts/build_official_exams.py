# SPDX-License-Identifier: AGPL-3.0-only
"""Build the «Exámenes oficiales» exercises for age-administrativo-c1 from official PDFs and the ledger.

Reads all 10 official questionnaires (2020-2025), pairs each question with its definitive status and key
from docs/age-official-exams-ledger.md, and outputs 10 quiz exercises under
content/age-administrativo-c1/exercises/.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CONTENT_DIR = REPO_ROOT / "content" / "age-administrativo-c1"
OFFICIAL_DIR = CONTENT_DIR / "sources" / "examenes-oficiales"
LEDGER_PATH = REPO_ROOT / "docs" / "age-official-exams-ledger.md"
EXERCISES_DIR = CONTENT_DIR / "exercises"

EXAMS = [
    {
        "code": "conv2025_A",
        "slug": "ofi-conv2025-a",
        "pdf": OFFICIAL_DIR / "2026-05-23_conv2025_modeloA_cuestionario.pdf",
        "title": "Convocatoria 2025 · Modelo A",
        "date": "23-05-2026",
    },
    {
        "code": "conv2025_B",
        "slug": "ofi-conv2025-b",
        "pdf": OFFICIAL_DIR / "2026-05-23_conv2025_modeloB_cuestionario.pdf",
        "title": "Convocatoria 2025 · Modelo B",
        "date": "23-05-2026",
    },
    {
        "code": "conv2025_X",
        "slug": "ofi-conv2025-x",
        "pdf": OFFICIAL_DIR / "2026-07-24_conv2025_extraordinario_cuestionario.pdf",
        "title": "Convocatoria 2025 · Extraordinario",
        "date": "24-07-2026",
    },
    {
        "code": "conv2024_A",
        "slug": "ofi-conv2024-a",
        "pdf": OFFICIAL_DIR / "conv2024_modeloA_cuestionario.pdf",
        "title": "Convocatoria 2024 · Modelo A",
        "date": "15-12-2024",
    },
    {
        "code": "conv2024_B",
        "slug": "ofi-conv2024-b",
        "pdf": OFFICIAL_DIR / "conv2024_modeloB_cuestionario.pdf",
        "title": "Convocatoria 2024 · Modelo B",
        "date": "15-12-2024",
    },
    {
        "code": "conv2024_X",
        "slug": "ofi-conv2024-x",
        "pdf": OFFICIAL_DIR / "conv2024_extraordinario_cuestionario.pdf",
        "title": "Convocatoria 2024 · Extraordinario",
        "date": "06-02-2025",
    },
    {
        "code": "conv2022",
        "slug": "ofi-conv2022",
        "pdf": OFFICIAL_DIR / "conv2022_cuestionario.pdf",
        "title": "Convocatoria 2022",
        "date": "24-07-2023",
    },
    {
        "code": "conv2022_X",
        "slug": "ofi-conv2022-x",
        "pdf": OFFICIAL_DIR / "conv2022_extraordinario_cuestionario.pdf",
        "title": "Convocatoria 2022 · Extraordinario",
        "date": "02-11-2023",
    },
    {
        "code": "conv2020",
        "slug": "ofi-conv2020",
        "pdf": OFFICIAL_DIR / "conv2020_cuestionario.pdf",
        "title": "Convocatoria 2020 (OEP 2020)",
        "date": "24-01-2022",
    },
    {
        "code": "conv2020_X",
        "slug": "ofi-conv2020-x",
        "pdf": OFFICIAL_DIR / "conv2020_extraordinario_cuestionario.pdf",
        "title": "Convocatoria 2020 (OEP 2020) · Extraordinario",
        "date": "28-03-2022",
    },
]

SECTIONS = [
    ("P1", 70),
    ("P1_R", 5),
    ("S1", 20),
    ("S1_R", 5),
    ("S2", 20),
    ("S2_R", 5),
]


def clean(s: str) -> str:
    lines = [line.strip() for line in s.splitlines() if line.strip()]
    res: list[str] = []
    for line in lines:
        if (
            re.search(r"Página \d+ de \d+", line, re.IGNORECASE)
            or ("CUESTIONARIO" in line.upper() and len(line) < 40)
            or "Cuerpo General" in line
        ):
            continue
        res.append(line)
    return " ".join(res)


def parse_ledger() -> dict[str, list[dict[str, str]]]:
    """Parse the ledger tables into rows per exam code."""
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


def find_options(block: str) -> tuple[str, str, str, str, str] | None:
    ma = re.search(r"(?:\n|\s|^)a\)\s*", block)
    if not ma:
        return None
    prompt = block[: ma.start()]
    rem = block[ma.end() :]

    mb = re.search(r"(?:\n|\s|^)b\)\s*", rem)
    if not mb:
        return None
    opta = rem[: mb.start()]
    rem = rem[mb.end() :]

    mc = re.search(r"(?:\n|\s|^)c\)\s*", rem)
    if not mc:
        return None
    optb = rem[: mc.start()]
    rem = rem[mc.end() :]

    md = re.search(r"(?:\n|\s|^)d\)\s*", rem)
    if not md:
        return None
    optc = rem[: md.start()]
    optd = rem[md.end() :]

    return prompt, opta, optb, optc, optd


def parse_pdf_questions(pdf_path: Path, code: str) -> list[tuple[str, int, str, str, str, str, str]]:
    raw = subprocess.check_output(["pdftotext", "-layout", str(pdf_path), "-"]).decode(
        "utf-8", errors="replace"
    )
    if "PRIMERA PARTE" in raw:
        raw = raw[raw.find("PRIMERA PARTE") :]
    matches = list(re.finditer(r"(?:^|\n)\s*(\d+)\.\s+", raw))

    sec_idx = 0
    expected_num = 1
    found_questions: list[tuple[str, int, int]] = []

    for m in matches:
        num = int(m.group(1))
        sec_name, sec_total = SECTIONS[sec_idx]

        if code == "conv2025_B" and sec_name == "P1" and expected_num == 65 and num == 66:
            found_questions.append((sec_name, 65, m.start()))
            expected_num = 66
            continue

        if num == expected_num:
            found_questions.append((sec_name, num, m.start()))
            if expected_num == sec_total:
                sec_idx += 1
                expected_num = 1
                if sec_idx >= len(SECTIONS):
                    break
            else:
                expected_num += 1

    results: list[tuple[str, int, str, str, str, str, str]] = []
    for i, (sname, qnum, start) in enumerate(found_questions):
        end = found_questions[i + 1][2] if i + 1 < len(found_questions) else len(raw)
        block = raw[start:end]
        res = find_options(block)
        assert res is not None, f"Failed to find options for {code} {sname} {qnum}"
        prompt, opta, optb, optc, optd = res
        results.append((sname, qnum, clean(prompt), clean(opta), clean(optb), clean(optc), clean(optd)))

    return results


def build_all() -> None:
    ledger_data = parse_ledger()

    for exam in EXAMS:
        code = exam["code"]
        slug = exam["slug"]
        pdf_path = exam["pdf"]
        rows = ledger_data[code]
        assert len(rows) == 125, f"{code} has {len(rows)} ledger rows, expected 125"

        pdf_qs = parse_pdf_questions(pdf_path, code)
        assert len(pdf_qs) == 125, f"{code} has {len(pdf_qs)} pdf questions, expected 125"

        variants: list[dict[str, object]] = []
        excluded_count = 0
        excluded_reasons: dict[str, int] = {}
        idx = 1

        for (_sname, _qnum, prompt, opta, optb, optc, optd), row in zip(pdf_qs, rows, strict=True):
            estado = row["estado"]
            clave_raw = row["clave"]

            # Exclude non-vigente questions
            if estado not in ("vigente", "vigente-con-nota"):
                excluded_count += 1
                cat = (
                    "anulada"
                    if estado == "anulada"
                    else "norma modificada"
                    if estado.startswith("norma modificada")
                    else "función retirada"
                    if estado.startswith("función retirada")
                    else estado
                )
                excluded_reasons[cat] = excluded_reasons.get(cat, 0) + 1
                continue

            clave = clave_raw.split()[0].lower()
            assert clave in ("a", "b", "c", "d"), f"Invalid key {clave_raw!r} in {code} row {row}"

            var_id = f"q{idx:03d}"
            idx += 1

            variant: dict[str, object] = {
                "id": var_id,
                "kind": "single_choice",
                "prompt": {"es": prompt},
                "options": [
                    {"id": "a", "text": {"es": opta}, "correct": clave == "a"},
                    {"id": "b", "text": {"es": optb}, "correct": clave == "b"},
                    {"id": "c", "text": {"es": optc}, "correct": clave == "c"},
                    {"id": "d", "text": {"es": optd}, "correct": clave == "d"},
                ],
            }

            if estado == "vigente-con-nota":
                note = row["nota"]
                if row["nota_clave"]:
                    note = f"{row['nota_clave']} {note}".strip() if note else row["nota_clave"]
                assert note, f"vigente-con-nota question missing note in {code}: {row}"
                variant["explanation"] = {"es": note}

            variants.append(variant)

        out_path = EXERCISES_DIR / f"{slug}.yaml"
        payload = {"type": "quiz", "shuffle": False, "variants": variants}

        with open(out_path, "w", encoding="utf-8") as f:
            yaml.dump(payload, f, allow_unicode=True, sort_keys=False, width=120)

        reasons_msg = f" ({excluded_reasons})" if excluded_reasons else ""
        print(
            f"Wrote {slug}.yaml: {len(variants)} questions included, {excluded_count} excluded{reasons_msg}"
        )


if __name__ == "__main__":
    build_all()
