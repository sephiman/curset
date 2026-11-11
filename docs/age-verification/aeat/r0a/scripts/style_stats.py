"""Counts of the classifier's style fields per exam and per programme part, for docs/aeat-exam-style.md."""

import json
from collections import Counter
from pathlib import Path

R0A = Path(__file__).resolve().parents[1]
EXAMS = ["2025", "2024", "2023", "2022", "2022X", "2021", "2020"]


def main() -> None:
    master = {q["id"]: q for q in json.loads((R0A / "parsed/master.json").read_text())}
    rows = [{**master[c["id"]], **c} for f in ("class_set1.json", "class_set2.json")
            for c in json.loads((R0A / "classification" / f).read_text())]
    out: dict[str, dict[str, object]] = {}
    for exam in EXAMS:
        rs = [r for r in rows if r["exam"] == exam]
        out[exam] = {
            "n": len(rs),
            "part": dict(Counter(str(r["tema"]).split(".")[0] for r in rs)),
            "stem_form": dict(Counter(str(r["stem_form"]).strip("«»") for r in rs).most_common()),
            "option_type": dict(Counter(str(r["option_type"]).strip("«»") for r in rs).most_common()),
            "distractor": dict(Counter(str(r["distractor"]).strip("«»") for r in rs).most_common()),
            "negative": sum(1 for r in rs if r["negative"]),
            "cites_article": sum(1 for r in rs if r["cites_article"]),
            "ninguna_todas": sum(1 for r in rs for v in r["opts"].values()
                                 if v.lower().startswith(("ninguna", "todas", "todas las anteriores"))),
            "combined": sum(1 for r in rs for v in r["opts"].values() if " y b) " in v.lower() or "son correctas" in v.lower()),
        }
    (R0A / "checks/style_stats.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    for exam, row in out.items():
        print(exam, json.dumps(row, ensure_ascii=False))


if __name__ == "__main__":
    main()
