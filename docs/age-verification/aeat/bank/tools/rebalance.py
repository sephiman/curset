"""Hold (not drop) kept questions that carry the answer-length tell, so the course passes the platform's bias test.

Run from backend/: `uv run python ../docs/age-verification/aeat/bank/tools/rebalance.py [--apply] [--course-bar 2.5] [--tema-bar 2.5]`.
Greedy on the key's length edge (key length minus the mean distractor length): hold the largest positive edges first, from the
temas furthest above their quota, until the course-level longest and edge |z| are within --course-bar and each tema within --tema-bar
(a tema is never taken below its quota unless it is the only way; common temas are never touched). Held ids go to `held.tsv`
(«bias rebalance»): reserve, never deleted. Without --apply it prints the plan.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from statistics import fmean, pvariance

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path.cwd() / "tests"))
from bias_per_tema import BANK, row, tsv_ids  # noqa: E402
from quotas import quotas  # noqa: E402

QUOTA = quotas()
TEMA_FLOOR = 50


def tema_of(lesson: str) -> str:
    return f"{ {'1': 'I', '2': 'II', '3': 'III'}[lesson[2]] }.{int(lesson[-2:])}"


def edge(q: dict[str, object]) -> float:
    options = q["options"]
    assert isinstance(options, dict)
    lengths = {k: len(str(v)) for k, v in options.items()}
    wrong = [v for k, v in lengths.items() if k != q["correct"]]
    return lengths[str(q["correct"])] - fmean(wrong)


def load() -> dict[str, list[dict[str, object]]]:
    drops = tsv_ids(BANK / "drops.tsv") | tsv_ids(BANK / "held.tsv")
    out: dict[str, list[dict[str, object]]] = {}
    for lesson in sorted({p.name.split(".")[0] for p in BANK.glob("m0?-l??.*.json")}):
        questions: list[dict[str, object]] = []
        if (BANK / f"{lesson}.kept-derived.json").exists():
            questions += json.loads((BANK / f"{lesson}.kept-derived.json").read_text("utf-8"))
        for draft in sorted(BANK.glob(f"{lesson}.authored*.draft.json")):
            questions += json.loads(draft.read_text("utf-8"))
        out[lesson] = [q for q in questions if q["id"] not in drops]
    return out


def variance(q: dict[str, object]) -> float:
    options = q["options"]
    assert isinstance(options, dict)
    return 16 / 9 * pvariance([len(str(v)) for v in options.values()])


def long_flag(q: dict[str, object]) -> int:
    """1 when the key is the (first) longest option in the question's stored order, as the platform counts it."""
    options = q["options"]
    assert isinstance(options, dict)
    lengths = [len(str(options[k])) for k in sorted(options)]
    return int(lengths.index(max(lengths)) == sorted(options).index(str(q["correct"])))


def main(apply: bool, course_bar: float, tema_bar: float, share_floor: float) -> None:
    """Joint greedy on the platform's two length statistics: z_edge = Σedge/√Σ(16/9·var), z_long = (ΣL−N/4)/√(3N/16)."""
    by = load()
    pool = {lesson: list(qs) for lesson, qs in by.items()}
    tax = [k for k in pool if k.startswith("m03")]
    n = sum(len(v) for v in pool.values())
    s_edge = sum(edge(q) for v in pool.values() for q in v)
    v_edge = sum(variance(q) for v in pool.values() for q in v)
    s_long = sum(long_flag(q) for v in pool.values() for q in v)
    tema_s = {k: sum(edge(q) for q in pool[k]) for k in pool}
    tema_v = {k: sum(variance(q) for q in pool[k]) for k in pool}
    holds: list[tuple[str, str]] = []

    def zs_(n_: int, se: float, ve: float, sl: float) -> tuple[float, float]:
        return se / ve**0.5, (sl - n_ / 4) / (3 * n_ / 16) ** 0.5

    def take(lesson: str, q: dict[str, object]) -> None:
        nonlocal n, s_edge, v_edge, s_long
        pool[lesson].remove(q)
        n -= 1
        s_edge -= edge(q)
        v_edge -= variance(q)
        s_long -= long_flag(q)
        tema_s[lesson] -= edge(q)
        tema_v[lesson] -= variance(q)
        holds.append((str(q["id"]), tema_of(lesson)))

    def worst_tema() -> float:
        return max((tema_s[k] / tema_v[k] ** 0.5 for k in tax if tema_v[k] > 1.0), default=0.0)

    while True:
        ze, zl = zs_(n, s_edge, v_edge, s_long)
        if len(holds) % 25 == 0:
            print(f"step {len(holds)}: n={n} edge z {ze:+.2f} longest z {zl:+.2f} worst tema {worst_tema():+.2f}", flush=True)
        if abs(ze) <= course_bar and abs(zl) <= course_bar and worst_tema() <= tema_bar:
            break
        if len(holds) > 1200:
            raise SystemExit("no convergence within 1200 holds")
        best: tuple[float, str, dict[str, object]] | None = None
        over = worst_tema() > tema_bar
        tax_n = sum(len(pool[k]) for k in tax)
        for lesson in pool:
            is_tax = lesson in tax
            if (tax_n - is_tax) / (n - 1) < share_floor:  # a hold is feasible only if Part III keeps its share
                continue
            if len(pool[lesson]) <= TEMA_FLOOR:  # the plan's floor of 50 per tema
                continue
            for q in pool[lesson]:
                e2, l2 = zs_(n - 1, s_edge - edge(q), v_edge - variance(q), s_long - long_flag(q))
                tz = (tema_s[lesson] - edge(q)) / max(tema_v[lesson] - variance(q), 1e-9) ** 0.5 if is_tax else 0.0
                score = max(abs(e2), abs(l2), tz * over)
                if best is None or score < best[0]:
                    best = (score, lesson, q)
        assert best is not None
        take(best[1], best[2])
    # Part III keeps its share: trim the common questions that disturb neither statistic most.
    common = [k for k in pool if not k.startswith("m03")]
    print(f"after the tax holds: {len(holds)} holds")
    while sum(len(pool[k]) for k in tax) / n < share_floor:
        best2: tuple[float, str, dict[str, object]] | None = None
        for lesson in common:
            for q in pool[lesson]:
                e2, l2 = zs_(n - 1, s_edge - edge(q), v_edge - variance(q), s_long - long_flag(q))
                score = max(abs(e2), abs(l2))
                if best2 is None or score < best2[0]:
                    best2 = (score, lesson, q)
        assert best2 is not None
        take(best2[1], best2[2])
    ze, zl = zs_(n, s_edge, v_edge, s_long)
    share = sum(len(pool[k]) for k in tax) / n
    print(f"held {len(holds)}; bank {n}; part III share {100 * share:.1f} %; course edge z {ze:+.2f}, longest z {zl:+.2f}")
    for lesson in sorted(pool):
        if len(pool[lesson]) >= 30:
            print(f"{lesson}: n={len(pool[lesson])} edge z {tema_s[lesson] / tema_v[lesson] ** 0.5:+.2f} (quota {QUOTA[tema_of(lesson)]})")
    if apply:
        with (BANK / "held.tsv").open("a", encoding="utf-8") as handle:
            handle.writelines(f"{q}\t{t}\tbias rebalance\n" for q, t in holds)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--course-bar", type=float, default=2.0)
    parser.add_argument("--tema-bar", type=float, default=2.5)
    parser.add_argument("--share-floor", type=float, default=0.702)
    args = parser.parse_args()
    main(args.apply, args.course_bar, args.tema_bar, args.share_floor)
