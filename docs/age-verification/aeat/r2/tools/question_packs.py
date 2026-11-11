"""Per-tema packs of the official AEAT first-exercise questions (stem, options, key, estado, R0a evidence) for R2."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
R0A = ROOT / "docs/age-verification/aeat/r0a"
OUT = ROOT / "docs/age-verification/aeat/r2/questions"
LAST_FOUR = {"2025", "2024", "2023", "2022", "2022X"}
FILES = {"2025": "conv2025_A", "2024": "conv2024_A", "2023": "conv2023_A", "2022": "conv2022_A",
         "2022X": "conv2022_X", "2021": "conv2021_A", "2020": "conv2020_A"}
ORDER = ["2025", "2024", "2023", "2022", "2022X", "2021", "2020"]


def lesson_of(tema: str) -> str:
    part, n = tema.split(".")
    return f"m{ {'I': 1, 'II': 2, 'III': 3}[part]:02d}-l{int(n):02d}"


def classified() -> dict[str, dict[str, object]]:
    rows: dict[str, dict[str, object]] = {}
    for name in ("class_set1.json", "class_set2.json"):
        for row in json.loads((R0A / "classification" / name).read_text()):
            rows[str(row["id"])] = row
    for qid, change in json.loads((R0A / "classification/overrides.json").read_text()).items():
        if not qid.startswith("_"):
            rows[qid].update(change)
    return rows


def questions() -> dict[str, dict[str, object]]:
    out: dict[str, dict[str, object]] = {}
    for exam, stem in FILES.items():
        for q in json.loads((R0A / "parsed" / f"{stem}.json").read_text()):
            out[f"{exam}-{q['n']}"] = q
    return out


def main(temas: list[str]) -> None:
    rows, texts = classified(), questions()
    OUT.mkdir(parents=True, exist_ok=True)
    for tema in temas:
        items: list[tuple[int, str, str]] = []
        for qid, row in rows.items():
            primary = row["tema"] == tema
            if not primary and row.get("tema_alt") != tema:
                continue
            exam = qid.rsplit("-", 1)[0]
            status = str(row["status"])
            scope = ("coverage" if primary and exam in LAST_FOUR and status.startswith("vigente") else "reference")
            q = texts[qid]
            head = (f"### {qid} · {scope} · estado: {status} · clave: {q['key']}"
                    + ("" if primary else f" · tema principal {row['tema']}"))
            body = [head, "", str(q["stem"])] + [f"- {k.lower()}) {q[k]}" for k in "ABCD"]
            body += ["", f"Norma: {row.get('norma')} {row.get('articulo')} · evidencia R0a: {row.get('evidence')}"]
            notes = " ".join(str(x) for x in (row.get("nota_clave"), row.get("nota")) if x)
            if notes:
                body.append(f"Nota del ledger: {notes}")
            items.append((ORDER.index(exam), qid, "\n".join(body)))
        items.sort(key=lambda t: (t[0], int(t[1].rsplit("-", 1)[1])))
        cov = sum(" · coverage · " in i[2] for i in items)
        text = (f"# Preguntas oficiales de Agentes de la Hacienda Pública — tema {tema} (`{lesson_of(tema)}`)\n\n"
                f"Generado por `docs/age-verification/aeat/r2/tools/question_packs.py` desde la clasificación de R0a y "
                f"`r0a/parsed`. «coverage»: vigente o vigente-con-nota, OEP 2022–2025 (con el extraordinario), tema "
                f"principal {tema} ({cov}). «reference»: OEP 2020–2021, segundo tema, o excluida.\n\n"
                + "\n\n".join(i[2] for i in items) + "\n")
        (OUT / f"{lesson_of(tema)}.md").write_text(text)
        print(f"{tema}: {len(items)} questions, {cov} coverage", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1:] or [f"I.{i}" for i in range(1, 8)] + [f"II.{i}" for i in range(1, 6)])
