"""Hold (not drop) kept questions that carry a tema's answer-length tell, within the tema's surplus.

Run from backend/: `uv run python ../docs/age-verification/c2/bank/tools/rebalance.py bloque-ii [--apply]`.
Greedy: while a tema's longest-is-correct or length-edge |z| is over BAR and the tema stays at or above its floor,
hold the question whose removal lowers the tema's worst |z| most. Floor = quota, or the current count when the tema
is already short. Without --apply it prints the plan; with it, appends the ids to `held.tsv` («bias rebalance»).
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bias_per_tema import BAR, BANK, kept, row  # noqa: E402
from plan_delta import QUOTA  # noqa: E402
from test_quiz_answer_bias import _length_edge, _longest_is_correct, _suite_z  # noqa: E402


def worst(rows: list) -> float:  # type: ignore[type-arg]
    return max(abs(_suite_z(rows, _longest_is_correct)[3]), abs(_suite_z(rows, _length_edge)[3]))


def main(bloque: str, apply: bool) -> None:
    folder = BANK / bloque
    with (folder / "drops.tsv").open(encoding="utf-8") as handle:
        drops = {r["id"] for r in csv.DictReader(handle, delimiter="\t")}
    with (folder / "held.tsv").open(encoding="utf-8") as handle:
        held_already = {r["id"] for r in csv.DictReader(handle, delimiter="\t")}
    holds: list[str] = []
    for derived in sorted(folder.glob("m0?-l??.kept-derived.json")):
        lesson = derived.name.split(".")[0]
        tema = f"{'I' if lesson.startswith('m01') else 'II'}.{int(lesson[-2:])}"
        questions = [q for q in kept(folder, lesson, drops) if q["id"] not in held_already]
        floor = min(QUOTA[tema], len(questions))
        rows = {str(q["id"]): row(q) for q in questions}
        start = worst(list(rows.values()))
        while worst(list(rows.values())) > BAR and len(rows) > floor:
            best_id, best = None, worst(list(rows.values()))
            for qid in rows:
                trial = [r for k, r in rows.items() if k != qid]
                score = worst(trial)
                if score < best:
                    best_id, best = qid, score
            if best_id is None:
                break
            del rows[best_id]
            holds.append(f"{best_id}\t{tema}\tbias rebalance (worst |z| per tema over {BAR})")
        print(f"{lesson}: worst |z| {start:.2f} → {worst(list(rows.values())):.2f}, held {len(questions) - len(rows)}, "
              f"kept {len(rows)} (floor {floor})")
    if apply and holds:
        with (folder / "held.tsv").open("a", encoding="utf-8") as handle:
            handle.writelines(h + "\n" for h in holds)
    print(f"{len(holds)} holds {'applied' if apply else 'planned'}")


if __name__ == "__main__":
    main(sys.argv[1], "--apply" in sys.argv)
