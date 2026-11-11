"""Write docs/aeat-official-exams-ledger.md from parsed/master.json, the classifier outputs and the coordinator's overrides."""

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
R0A = ROOT / "docs/age-verification/aeat/r0a"
OUT = ROOT / "docs/aeat-official-exams-ledger.md"

EXAMS = ["2025", "2024", "2023", "2022", "2022X", "2021", "2020"]
LAST_FOUR = {"2025", "2024", "2023", "2022", "2022X"}
LABEL = {
    "2025": "OEP 2025, 21-03-2026", "2024": "OEP 2024, 05-04-2025", "2023": "OEP 2023, 20-04-2024",
    "2022": "OEP 2022, 22-04-2023", "2022X": "OEP 2022 extraordinario, 18-07-2023",
    "2021": "OEP 2021, 28-05-2022", "2020": "OEP 2020, 25-09-2021",
}
STATUSES = ["vigente", "vigente-con-nota", "anulada", "norma modificada", "fuera de temario", "dudosa"]
TEMAS = [f"I.{i}" for i in range(1, 8)] + [f"II.{i}" for i in range(1, 6)] + [f"III.{i}" for i in range(1, 21)]


def status_family(status: str) -> str:
    return "norma modificada" if status.startswith("norma modificada") else status


def cell(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def load() -> list[dict[str, object]]:
    master = {q["id"]: q for q in json.loads((R0A / "parsed/master.json").read_text())}
    rows: dict[str, dict[str, object]] = {}
    for name in ("class_set1.json", "class_set2.json"):
        for c in json.loads((R0A / "classification" / name).read_text()):
            rows[c["id"]] = {**master[c["id"]], **c}
    overrides_path = R0A / "classification/overrides.json"
    overrides = json.loads(overrides_path.read_text()) if overrides_path.exists() else {}
    for qid, change in overrides.items():
        if not qid.startswith("_"):
            rows[qid].update(change)
    missing = set(master) - set(rows)
    if missing:
        raise SystemExit(f"unclassified: {sorted(missing)[:10]} … ({len(missing)})")
    return [rows[qid] for qid in master]


def summary_table(rows: list[dict[str, object]]) -> list[str]:
    lines = ["| Questionnaire | Questions | " + " | ".join(STATUSES) + " |", "|---" * (len(STATUSES) + 2) + "|"]
    total = Counter()
    for exam in EXAMS:
        counts = Counter(status_family(str(r["status"])) for r in rows if r["exam"] == exam)
        total.update(counts)
        n = sum(counts.values())
        lines.append(f"| {LABEL[exam]} | {n} | " + " | ".join(str(counts[s]) for s in STATUSES) + " |")
    lines.append(f"| **Total** | {sum(total.values())} | " + " | ".join(str(total[s]) for s in STATUSES) + " |")
    return lines


def tema_table(rows: list[dict[str, object]]) -> list[str]:
    head = "| Tema | " + " | ".join(EXAMS) + " | Total 2022–2025 |"
    lines = [head, "|---" * (len(EXAMS) + 2) + "|"]
    for tema in TEMAS + ["(fuera de temario)"]:
        counts = []
        for exam in EXAMS:
            if tema.startswith("("):
                n = sum(1 for r in rows if r["exam"] == exam and status_family(str(r["status"])) == "fuera de temario")
            else:
                n = sum(1 for r in rows if r["exam"] == exam and r["tema"] == tema
                        and status_family(str(r["status"])) != "fuera de temario")
            counts.append(n)
        total = sum(n for exam, n in zip(EXAMS, counts) if exam in LAST_FOUR)
        lines.append(f"| {tema} | " + " | ".join(str(n) for n in counts) + f" | {total} |")
    return lines


def exam_table(rows: list[dict[str, object]], exam: str) -> list[str]:
    lines = ["| Nº | Tipo B | Tema | Estado | Clave | Nota de clave | Nota |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        if r["exam"] != exam:
            continue
        tema = str(r["tema"] or "—") + (f" [{r['tema_alt']}]" if r.get("tema_alt") else "")
        b = ", ".join(str(x) for x in r["tipoB"]) if r.get("tipoB") else "—"
        note = "; ".join(x for x in (str(r.get("tribunal") or ""), str(r.get("nota") or "")) if x)
        lines.append(f"| {r['n']} | {b} | {tema} | {cell(str(r['status']))} | {r['key']} | {cell(str(r.get('nota_clave') or ''))} | {cell(note)} |")
    return lines


def main() -> None:
    rows = load()
    header = (R0A / "scripts/ledger_header.md").read_text()
    parts = [header.rstrip(), "", "## Summary", "", *summary_table(rows), "", "## Questions per tema per exam", "",
             "Counts by the first tema; questions marked `fuera de temario` are counted only in the last row. Annulled "
             "questions are counted under their tema. The last column sums the last four convocatorias (OEP 2022–2025, "
             "the extraordinario of 2022 included), the set of requirement R4.6.", "", *tema_table(rows)]
    for exam in EXAMS:
        parts += ["", f"## {LABEL[exam]}", "", *exam_table(rows, exam)]
    OUT.write_text("\n".join(parts) + "\n")
    print("ledger rows", len(rows))


if __name__ == "__main__":
    main()
