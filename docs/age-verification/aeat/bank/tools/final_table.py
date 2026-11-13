"""Final per-tema table of the AEAT bank: kept, quota, gap, reserve, and the part shares.

Run from backend/: `uv run python ../docs/age-verification/aeat/bank/tools/final_table.py`.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path.cwd() / "tests"))
from bias_per_tema import BANK  # noqa: E402
from quotas import quotas  # noqa: E402
from rebalance import load, tema_of  # noqa: E402

QUOTA = quotas()


def main() -> None:
    kept = {tema_of(lesson): len(qs) for lesson, qs in load().items()}
    with (BANK / "held.tsv").open(encoding="utf-8") as handle:
        reserve = Counter(r["tema"] for r in csv.DictReader(handle, delimiter="\t"))
    lines = ["| Tema | Quota | Kept | Gap | Reserve (held) |", "|---|---|---|---|---|"]
    for tema, quota in QUOTA.items():
        gap = quota - kept.get(tema, 0)
        lines.append(f"| {tema} | {quota} | {kept.get(tema, 0)} | {gap if gap > 0 else 0} | {reserve.get(tema, 0)} |")
    total = sum(kept.values())
    parts = {p: sum(v for t, v in kept.items() if t.split('.')[0] == p) for p in ("I", "II", "III")}
    lines += ["", f"Total {total} of 5,000; gap {5000 - total}. Parts: I {parts['I']}, II {parts['II']}, III {parts['III']} "
              f"({100 * parts['III'] / total:.1f} % tax)."]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
