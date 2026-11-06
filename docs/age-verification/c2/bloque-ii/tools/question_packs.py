"""Per-tema packs of the official Auxiliar questions (stem, options, definitive key, estado) for bloque II."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]  # bloque II copy of bloque-i/tools/question_packs.py
LEDGER = ROOT / "docs/age-c2-official-exams-ledger.md"
R0A = ROOT / "docs/age-verification/c2/r0a"
OUT = ROOT / "docs/age-verification/c2/bloque-ii/questions"

# ledger section -> (parsed questionnaire, keys file, short label, counts for coverage)
EXAMS = {
    "conv2025_A": ("2026-05-23_conv2025_modeloA_cuestionario", "2026-05-23_conv2025_modeloA_plantilla-definitiva", "2025", True),
    "conv2024_A": ("conv2024_modeloA_cuestionario", "conv2024_modeloA_plantilla-definitiva", "2024", True),
    "conv2024_X": ("conv2024_extraordinario_cuestionario", "conv2024_extraordinario_plantilla-definitiva", "2024X", True),
    "conv2022": ("conv2022_cuestionario", "conv2022_plantilla-definitiva", "2022", True),
    "conv2020": ("conv2020_cuestionario", "conv2020_plantilla-definitiva", "2020", False),
    "conv2020_X": ("conv2020_extraordinario_cuestionario", "conv2020_extraordinario_plantilla-definitiva", "2020X", False),
}
SECTION_OF = {
    "Primera parte": "P1",
    "Primera parte — preguntas de reserva": "R1",
    "Segunda parte": "P2",
    "Segunda parte — preguntas de reserva": "R2",
}
TEMA = re.compile(r"^(I{1,2}\.\d+)(?:\s*\((I{1,2}\.\d+)\))?")


def ledger_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    exam = sec = None
    for line in LEDGER.read_text().splitlines():
        if line.startswith("## "):
            exam = line[3:].split(" — ")[0].strip()
            sec = None
        elif line.startswith("### "):
            sec = SECTION_OF.get(line[4:].strip())
        elif line.startswith("| ") and exam in EXAMS and sec and line[2].isdigit():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            n, tema, estado, clave, nota_clave, nota = cells[:6]
            m = TEMA.match(tema)
            if not m:
                continue
            rows.append({"exam": exam, "sec": sec, "n": n, "tema": m.group(1), "tema2": m.group(2) or "",
                         "estado": estado, "clave": clave, "nota_clave": nota_clave, "nota": nota})
    return rows


def main() -> None:
    lesson_of = {f"II.{i}": f"m02-l{i:02d}" for i in range(1, 13)}
    parsed = {e: {(q["sec"], q["n"]): q for q in json.loads((R0A / "parsed" / f"{p}.json").read_text())}
              for e, (p, _, _, _) in EXAMS.items()}
    packs: dict[str, list[str]] = {t: [] for t in lesson_of}
    for row in ledger_rows():
        for tema, primary in ((row["tema"], True), (row["tema2"], False)):
            if tema not in packs:
                continue
            _, _, label, counts = EXAMS[row["exam"]]
            q = parsed[row["exam"]][(row["sec"], int(row["n"]))]
            qid = f"{label}-{row['sec']}-{row['n']}"
            scope = ("coverage" if counts and primary and row["estado"].startswith("vigente") else
                     "reference")
            head = (f"### {qid} · {scope} · estado: {row['estado']} · clave: {row['clave']}"
                    + ("" if primary else f" · tema principal {row['tema']}"))
            body = [head, "", q["stem"]] + ([q["ctx"]] if q.get("ctx") else [])
            body += [f"- {k}) {v}" for k, v in q["opts"].items()]
            notes = " ".join(x for x in (row["nota_clave"], row["nota"]) if x and not x.startswith("Modelo B"))
            if notes:
                body += ["", f"Nota del ledger: {notes}"]
            packs[tema].append("\n".join(body))
    OUT.mkdir(parents=True, exist_ok=True)
    for tema, items in packs.items():
        cov = sum(" · coverage · " in i for i in items)
        text = (f"# Preguntas oficiales del Auxiliar — tema {tema} (`{lesson_of[tema]}`)\n\n"
                f"Generado por `tools/question_packs.py` desde el ledger y `r0a/parsed`. «coverage»: vigente o "
                f"vigente-con-nota, 2022–2025, tema principal {tema} ({cov}). «reference»: OEP 2020 (programa "
                f"anterior), tema secundario, o excluida.\n\n" + "\n\n".join(items) + "\n")
        (OUT / f"{lesson_of[tema]}.md").write_text(text)
        print(tema, len(items), "coverage", cov, file=sys.stderr)


if __name__ == "__main__":
    main()
