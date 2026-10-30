"""Print one built case as Markdown for the ledger: scenario, then each question with its options, key, explanation.

Usage (repo root): python3 docs/age-verification/cases/tools/case_markdown.py sp-03 >> docs/age-cases-ledger.md
Reads the built exercise (content/age-administrativo-c1/exercises/sp-NN.yaml), so it shows exactly what learners get.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
EXERCISES = ROOT / "content" / "age-administrativo-c1" / "exercises"


def main(case_id: str) -> None:
    case = yaml.safe_load((EXERCISES / f"{case_id}.yaml").read_text(encoding="utf-8"))
    out = [f"### {case_id} — {case['title']['es']}", "", case["scenario"]["es"].replace("\n\n", "\n\n"), ""]
    for n, q in enumerate(case["questions"], start=1):
        out.append(f"**{n}.** {q['prompt']['es']}  ")
        for option in q["options"]:
            mark = " **(clave)**" if option.get("correct") else ""
            out.append(f"{option['id']}) {option['text']['es']}{mark}  ")
        out += ["", f"*Explicación.* {q['explanation']['es']}", "",
                f"*Cita:* {q['citation']} · *tema* `{q['lesson']}` · *id* `{q['id']}` · *dificultad* {q['difficulty']}", ""]
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1])
