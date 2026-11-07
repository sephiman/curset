"""Per-tema answer-bias guards on a bloque's kept set, with the platform test's own statistics.

Run from backend/: `uv run python ../docs/age-verification/c2/bank/tools/bias_per_tema.py bloque-ii`.
Kept = `<lesson>.kept-derived.json` + every `<lesson>.authored*.draft.json`, minus `drops.tsv` and `held.tsv`. Prints, per tema,
the longest-is-correct z, the length-edge z and the worst slot z; flags any beyond ±1.5 (C1's per-tema bar; the
course-level test allows ±3).
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / "tests"))
from test_quiz_answer_bias import Answered, _length_edge, _longest_is_correct, _position_z, _suite_z  # noqa: E402

BANK = Path(__file__).resolve().parents[1]
BAR = 1.5


def kept(folder: Path, lesson: str, drops: set[str]) -> list[dict[str, object]]:
    questions: list[dict[str, object]] = json.loads((folder / f"{lesson}.kept-derived.json").read_text("utf-8"))
    for draft in sorted(folder.glob(f"{lesson}.authored*.draft.json")):
        questions += json.loads(draft.read_text("utf-8"))
    return [q for q in questions if q["id"] not in drops]


def row(q: dict[str, object]) -> Answered:
    options = q["options"]
    assert isinstance(options, dict)
    keys = sorted(options)
    return Answered(
        "", str(q["id"]), tuple(len(str(options[k])) for k in keys), frozenset({keys.index(str(q["correct"]))})
    )


def main(bloque: str) -> int:
    folder = BANK / bloque
    with (folder / "drops.tsv").open(encoding="utf-8") as handle:
        drops = {r["id"] for r in csv.DictReader(handle, delimiter="\t")}
    with (folder / "held.tsv").open(encoding="utf-8") as handle:
        drops |= {r["id"] for r in csv.DictReader(handle, delimiter="\t")}  # held: not in the kept set
    worst = 0.0
    for derived in sorted(folder.glob("m0?-l??.kept-derived.json")):
        lesson = derived.name.split(".")[0]
        rows = [row(q) for q in kept(folder, lesson, drops)]
        z_long = _suite_z(rows, _longest_is_correct)[3]
        z_edge = _suite_z(rows, _length_edge)[3]
        z_slot = max((abs(s[4]) for s in _position_z(rows)), default=0.0)
        flags = [n for n, z in (("longest", z_long), ("edge", z_edge), ("slot", z_slot)) if abs(z) > BAR]
        worst = max(worst, abs(z_long), abs(z_edge), z_slot)
        print(f"{lesson}: n={len(rows)} longest z {z_long:+.2f} · edge z {z_edge:+.2f} · worst slot |z| {z_slot:.2f}"
              + (f" · OVER ±{BAR}: {', '.join(flags)}" if flags else ""))
    return 0 if worst <= BAR else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
