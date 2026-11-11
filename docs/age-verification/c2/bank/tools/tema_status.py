"""One line per lesson: kept derived, authored, verify drops, kept, quota; then the mix and bias of the kept set.

Run from backend/: `PYTHONPATH=tests uv run python ../docs/age-verification/c2/bank/tools/tema_status.py bloque-i [lesson …]`.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bias_per_tema import BANK, row  # noqa: E402
from c2_stats import report  # noqa: E402
from derive_candidates import tema  # noqa: E402
from plan_delta import QUOTA  # noqa: E402
from test_quiz_answer_bias import _length_edge, _longest_is_correct, _position_z, _suite_z  # noqa: E402


def main(bloque: str, only: list[str]) -> None:
    folder = BANK / bloque
    with (folder / "drops.tsv").open(encoding="utf-8") as handle:
        drops = {r["id"] for r in csv.DictReader(handle, delimiter="\t")}
    with (folder / "held.tsv").open(encoding="utf-8") as handle:
        held = {r["id"] for r in csv.DictReader(handle, delimiter="\t")}
    for path in sorted(folder.glob("m0?-l??.kept-derived.json")):
        lesson = path.name.split(".")[0]
        if only and lesson not in only:
            continue
        derived = [q for q in json.loads(path.read_text("utf-8")) if q["id"] not in held]
        authored = [q for d in sorted(folder.glob(f"{lesson}.authored*.draft.json")) for q in json.loads(d.read_text("utf-8"))]
        kept_authored = [q for q in authored if q["id"] not in drops and q["id"] not in held]
        kept = derived + kept_authored
        rows = [row(q) for q in kept]
        z = (_suite_z(rows, _longest_is_correct)[3], _suite_z(rows, _length_edge)[3],
             max(abs(s[4]) for s in _position_z(rows)))
        t = tema(lesson)
        print(f"{t} {lesson}: derived {len(derived)} · authored {len(authored)} · dropped "
              f"{sum(1 for q in authored if q['id'] in drops)} · kept {len(kept)} / quota {QUOTA[t]} · "
              f"longest z {z[0]:+.2f} · edge z {z[1]:+.2f} · slot {z[2]:.2f}")
        for q in kept:
            q["tema"] = t
        print("  " + report(kept)[0])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
