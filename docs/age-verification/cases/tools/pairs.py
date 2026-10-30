"""Pair the cases for the simulation's «choose one of two»: ten pairs of similar difficulty and tema mix.

Usage (from the repo root): python3 docs/age-verification/cases/tools/pairs.py [sp-01 …]. Each case is reduced to its
kept questions' mean difficulty, computation count and share per bloque and per engine tema; the pairing minimises the
summed distance over all pairs (exact, by dynamic programming over subsets). Prints the pairs and their profiles.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from functools import cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from case_check import CASES, kept  # noqa: E402

BLOQUES = ("II", "III", "IV", "V")
ENGINES = ("III.3", "III.4", "IV.4", "IV.5", "IV.6", "V.2", "V.3")


def profile(case_id: str) -> dict[str, float]:
    case = json.loads((CASES / f"{case_id}.draft.json").read_text(encoding="utf-8"))
    questions = kept(case)
    n = len(questions)
    bloques = Counter(q["bloque"] for q in questions)
    temas = Counter(q["tema"] for q in questions)
    return {
        "difficulty": sum(q["difficulty"] for q in questions) / n,
        "computes": sum(q["computes"] in ("date", "amount") for q in questions) / n,
        **{f"b:{b}": bloques[b] / n for b in BLOQUES},
        **{f"t:{t}": temas[t] / n for t in ENGINES},
    }


def distance(a: dict[str, float], b: dict[str, float]) -> float:
    # Difficulty weighs most: a candidate choosing between the two must not be choosing an easier case.
    return 4 * abs(a["difficulty"] - b["difficulty"]) + abs(a["computes"] - b["computes"]) + sum(
        abs(a[k] - b[k]) for k in a if k.startswith(("b:", "t:"))
    )


def main(case_ids: list[str]) -> None:
    profiles = [profile(c) for c in case_ids]
    n = len(case_ids)

    @cache
    def best(mask: int) -> tuple[float, tuple[tuple[int, int], ...]]:
        if mask == (1 << n) - 1:
            return 0.0, ()
        i = next(k for k in range(n) if not mask >> k & 1)
        options = []
        for j in range(i + 1, n):
            if not mask >> j & 1:
                cost, rest = best(mask | 1 << i | 1 << j)
                options.append((cost + distance(profiles[i], profiles[j]), ((i, j), *rest)))
        return min(options)

    total, pairs = best(0)
    print(f"total distance {total:.2f}")
    for i, j in pairs:
        a, b = profiles[i], profiles[j]
        print(
            f"{case_ids[i]} + {case_ids[j]}  distance {distance(a, b):.2f}  "
            f"difficulty {a['difficulty']:.2f}/{b['difficulty']:.2f}  "
            f"computes {a['computes']:.0%}/{b['computes']:.0%}  "
            + "  ".join(f"{k[2:]} {a[k]:.0%}/{b[k]:.0%}" for k in a if k.startswith("b:"))
        )


if __name__ == "__main__":
    ids = sys.argv[1:] or sorted(p.name.split(".")[0] for p in CASES.glob("sp-[0-9][0-9].draft.json"))
    if len(ids) % 2:
        sys.exit(f"{len(ids)} cases: pairing needs an even number")
    main(ids)
