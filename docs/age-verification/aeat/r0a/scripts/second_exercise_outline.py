"""Outline every second-exercise paper: supuestos, number of questions, statement length, the «Se pide» text."""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
SRC = ROOT / "content/aeat-agentes-hacienda/sources/examenes-oficiales"


def outline(path: Path, width: int) -> None:
    t = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True).stdout
    pages = t.count("\f") + 1
    blocks = re.split(r"\n\s*(SUPUESTO(?: PRÁCTICO)?(?: N[ºo°]\.?)? *\d+|CASO PRÁCTICO *\d+)\s*[.:]?\s*\n", t, flags=re.I)
    questions = len(re.findall(r"\bPREGUNTA\s*(?:N[ºo°]\.?\s*)?\d+", t, flags=re.I))
    print(f"===== {path.name}: {pages} pages, {len(blocks) // 2} supuestos found, {questions} «PREGUNTA n» labels")
    print("  preamble:", " ".join(blocks[0].split())[:width])
    for i in range(1, len(blocks), 2):
        body = blocks[i + 1]
        statement, _, asked = body.partition("Se pide")
        print(f"  -- {blocks[i].strip()} ({len(statement.split())} words): {' '.join((asked or body[-900:]).split())[:width]}")


if __name__ == "__main__":
    for name in sorted(SRC.glob("*2ej*cuestionario*.pdf")) + sorted(SRC.glob("*2ej_supuesto*.pdf")):
        outline(name, int(sys.argv[1]) if len(sys.argv) > 1 else 400)
