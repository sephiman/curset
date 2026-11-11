"""Build parsed/master.json: one row per distinct first-exercise question (tipo A, and the 2022 extraordinario)."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
R0A = ROOT / "docs/age-verification/aeat/r0a"

EXAMS = {
    "2020": ("conv2020", "2021-09-25"),
    "2021": ("conv2021", "2022-05-28"),
    "2022": ("conv2022", "2023-04-22"),
    "2022X": ("conv2022", "2023-07-18"),
    "2023": ("conv2023", "2024-04-20"),
    "2024": ("conv2024", "2025-04-05"),
    "2025": ("conv2025", "2026-03-21"),
}

# Tribunal decisions on the provisional sheets (res-aprobados-1ej PDFs), numbered as tipo A.
TRIBUNAL: dict[str, dict[int, str]] = {
    "2020": {4: "Anulada: «no están correctamente planteadas»", 89: "Anulada: «no están correctamente planteadas»",
             97: "Clave modificada por el Tribunal (plantilla provisional → definitiva)"},
    "2021": {80: "Anulada: «no está correctamente planteada» (ya figuraba anulada en la plantilla provisional)", 27: "Clave modificada por el Tribunal: «estableciendo como correcta la opción C»"},
    "2022": {43: "Anulada: «no está correctamente planteadas»",
             82: "Anulada en la plantilla definitiva (B-81). La resolución del Tribunal dice «preguntas 43 y 80 del Tipo de examen A y las correspondientes preguntas 40 y 81 del Tipo de examen B»: B-81 es A-82, así que «80» es errata de la resolución",
             42: "Clave modificada por el Tribunal: C", 46: "Clave modificada por el Tribunal: A", 47: "Clave modificada por el Tribunal: C"},
    "2023": {20: "Anulada: «no está correctamente planteada y tener dos respuestas correctas»",
             24: "Anulada: «no está correctamente planteada y no tener una respuesta correcta»",
             25: "Anulada: «al no tener la pregunta B-69 un texto idéntico a la pregunta A-25»",
             30: "Anulada: «dada la duplicidad en el ejercicio Tipo B de las preguntas 62 y 66»",
             42: "Anulada: «dada la duplicidad en el ejercicio Tipo B de las preguntas 62 y 66»"},
    "2024": {73: "Anulada: «no está correctamente planteada, dando lugar a dos respuestas correctas, la opción A y la opción D»",
             18: "Clave modificada por el Tribunal: B", 68: "Clave modificada por el Tribunal: C"},
    "2025": {},
    "2022X": {},
}


def main() -> None:
    pairing = json.loads((R0A / "checks/pairing.json").read_text())
    master = []
    for exam, (conv, date) in EXAMS.items():
        suffix = "X" if exam.endswith("X") else "A"
        questions = json.loads((R0A / f"parsed/{conv}_{suffix}.json").read_text())
        b_of_a: dict[int, list[int]] = {}
        if suffix == "A":
            for p in pairing[conv]["pairs"]:
                b_of_a.setdefault(p["A"], []).append(p["B"])
        for q in questions:
            master.append({
                "id": f"{exam}-{q['n']}",
                "exam": exam,
                "date": date,
                "n": q["n"],
                "tipoB": b_of_a.get(q["n"]),
                "stem": q["stem"],
                "opts": {k.lower(): q[k] for k in "ABCD"},
                "key": q["key"],
                "tribunal": TRIBUNAL[exam].get(q["n"], ""),
            })
    (R0A / "parsed/master.json").write_text(json.dumps(master, ensure_ascii=False, indent=1))
    print(len(master), "questions")


if __name__ == "__main__":
    main()
