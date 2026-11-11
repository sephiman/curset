"""Choose a tema's kept derived questions from its whole surviving pool so the mix and the answer-bias guards hold.

Run from backend/: `uv run python ../docs/age-verification/c2/bank/tools/select_derived.py bloque-i m01-l13 [--apply]`.
Starts from `<lesson>.kept-derived.json` and swaps one kept question for one surviving held one while that lowers the
penalty: stem forms beyond ±9 points of 2025, article share beyond ±9, longest/edge/slot z beyond ±1.4, more
negatives than one per 20, or fewer cited units covered. Authored drafts count in the statistics but are never moved.
With --apply it rewrites the kept file and the lesson's «over quota» rows of `held.tsv`. Do not rerun
`plan_delta.py` on the lesson afterwards: its trim would undo the choice.
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bias_per_tema import BANK, row  # noqa: E402
from c2_stats import ARTICLE, ARTICLE_SHARE, NEGATIVE, TARGET, set_of, stem_form  # noqa: E402
from derive_candidates import tema  # noqa: E402
from test_quiz_answer_bias import _length_edge, _longest_is_correct, _position_z, _suite_z  # noqa: E402

Question = dict[str, object]
SLACK, Z_BAR = 9, 1.4


def penalty(qs: list[Question], kind: str, anchors: int) -> float:
    n = len(qs)
    forms = Counter(stem_form(str(q["prompt"]), kind) for q in qs)
    out = sum(max(0.0, abs(100 * forms.get(f, 0) / n - t) - SLACK) ** 2 for f, t in TARGET[kind].items())
    article = 100 * sum(1 for q in qs if ARTICLE.search(str(q["prompt"]))) / n
    out += max(0.0, abs(article - ARTICLE_SHARE[kind]) - SLACK) ** 2
    rows = [row(q) for q in qs]
    zs = [_suite_z(rows, _longest_is_correct)[3], _suite_z(rows, _length_edge)[3]]
    zs += [s[4] for s in _position_z(rows)]
    out += 100 * sum(max(0.0, abs(z) - Z_BAR) ** 2 for z in zs)
    out += 100 * max(0, sum(1 for q in qs if NEGATIVE.search(str(q["prompt"]))) - n // 20)
    out += 100 * max(0, anchors - len({q.get("anchor") for q in qs}))
    return out


def main(bloque: str, lesson: str, apply: bool) -> None:
    folder = BANK / bloque
    with (folder / "drops.tsv").open(encoding="utf-8") as handle:
        drops = {r["id"] for r in csv.DictReader(handle, delimiter="\t")}
    derived: list[Question] = json.loads((folder / f"{lesson}.derived.json").read_text("utf-8"))
    kept_ids = {q["id"] for q in json.loads((folder / f"{lesson}.kept-derived.json").read_text("utf-8"))}
    authored = [
        q for d in sorted(folder.glob(f"{lesson}.authored*.draft.json"))
        for q in json.loads(d.read_text("utf-8")) if q["id"] not in drops
    ]
    kept = [q for q in derived if q["id"] in kept_ids]
    pool = [q for q in derived if q["id"] not in kept_ids and q["id"] not in drops]
    kind = set_of(tema(lesson))
    anchors = len({q.get("anchor") for q in kept + authored})
    score = penalty(kept + authored, kind, anchors)
    print(f"{lesson}: start penalty {score:.1f}, kept {len(kept)}, pool {len(pool)}")
    while score > 0:
        best: tuple[float, int, int] | None = None
        # Shortlist: the removals and the additions that help most alone; full pairwise search is too slow.
        outs = sorted(range(len(kept)), key=lambda i: penalty(kept[:i] + kept[i + 1:] + authored, kind, anchors))[:15]
        ins = sorted(range(len(pool)), key=lambda j: penalty(kept + [pool[j]] + authored, kind, anchors))[:25]
        for i in outs:
            for j in ins:
                trial = kept[:i] + kept[i + 1:] + [pool[j]]
                s = penalty(trial + authored, kind, anchors)
                if s < score - 1e-9 and (best is None or s < best[0]):
                    best = (s, i, j)
        if best is None:
            break
        score, i, j = best
        kept[i], pool[j] = pool[j], kept[i]
        print(f"  swap out {pool[j]['id']} in {kept[i]['id']} → penalty {score:.1f}")
    print(f"{lesson}: end penalty {score:.1f}")
    if not apply:
        return
    kept.sort(key=lambda q: str(q["id"]))
    (folder / f"{lesson}.kept-derived.json").write_text(json.dumps(kept, ensure_ascii=False, indent=1) + "\n", "utf-8")
    held_path = folder / "held.tsv"
    lines = held_path.read_text("utf-8").splitlines()
    t = tema(lesson)
    others = [r for r in lines[1:] if r and not r.startswith(f"{lesson}-q")]
    mine = [f"{q['id']}\t{t}\tover quota (selected out for mix and bias)" for q in sorted(pool, key=lambda q: str(q["id"]))]
    held_path.write_text("\n".join([lines[0], *others, *mine]) + "\n", "utf-8")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], "--apply" in sys.argv)
