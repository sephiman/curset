"""Check that every copied paragraph of programa.md occurs verbatim in the BOE convocatoria or the AEAT criteria PDF."""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
SRC = ROOT / "content/aeat-agentes-hacienda/sources"
BOE = SRC / "convocatorias/2025-12-30_BOE-A-2025-27056_convocatoria.pdf"
CRITERIA = SRC / "examenes-oficiales/2026-03-21_conv2025_criterios-correccion.pdf"

# Lines that are the course's own (headings, notes, tables, quotes of other files), not copied text.
OWN = re.compile(r"^(#|Fuente:|\*\*|\||>|\[…\]|Se copia para|t\(d\)|La fórmula|Primer ejercicio \(fichero|Segundo ejercicio \(fichero|No se publicaron|ejercicio \(30\)|10 de julio|`examenes|Por qué|Convocatoria anterior|Comunes|Materias específicas: 22|Convocatorias anteriores|Sus normas|OEP 20)")


def normalise(text: str) -> str:
    text = re.sub(r"cve: BOE-A-\S+|Verificable en https://www\.boe\.es|BOLETÍN OFICIAL DEL ESTADO|Núm\. \d+|"
                  r"(?:Lunes|Martes|Miércoles|Jueves|Viernes|Sábado|Domingo) \d+ de \w+ de 2025|Sec\. II\.B\. Pág\. \d+", " ", text)
    text = re.sub(r"-\s*\n\s*", "-", text)  # BOE line-end hyphen kept as a hyphen
    text = text.replace("•", " ").replace("–", "-").replace("«", "\"").replace("»", "\"")
    return re.sub(r"\s+", " ", text).strip()


def pdf_text(path: Path) -> str:
    return subprocess.run(["pdftotext", str(path), "-"], capture_output=True, text=True, check=True).stdout


def copied_paragraphs(markdown: str) -> list[str]:
    body = markdown.split("## Base 6 — Procesos selectivos (acceso libre)", 1)[1]
    body = body.split("### Notas informativas de puntuaciones", 1)[0]
    paragraphs = []
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block or block == "---" or OWN.match(block):
            continue
        block = re.sub(r"^(- |\d+\. )", "", block, flags=re.M)  # list markers added in markdown
        paragraphs.append(block)
    return paragraphs


def main() -> None:
    sources = normalise(pdf_text(BOE)) + " " + normalise(pdf_text(CRITERIA))
    # the BOE also splits «contencioso-administrativo» as «contencioso-\nadministrativo»; the raw text drops the hyphen
    sources = sources.replace("contenciosoadministrativo", "contencioso-administrativo")
    paragraphs = copied_paragraphs((SRC / "programa.md").read_text())
    missing = []
    for p in paragraphs:
        sentences = [s for s in re.split(r"(?<=[.:;])\s+(?=[A-ZÁÉÍÓÚ«\d])", normalise(p)) if len(s) > 3]
        for s in sentences:
            if s not in sources:
                missing.append(s)
    print(f"{len(paragraphs)} copied paragraphs checked; {len(missing)} sentences not found verbatim")
    for s in missing:
        print("  NOT FOUND:", s[:200])
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
