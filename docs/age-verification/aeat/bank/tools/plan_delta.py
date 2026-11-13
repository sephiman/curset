"""Pool, trim and delta sheets for the AEAT bank.

Run from backend/: `uv run python ../docs/age-verification/aeat/bank/tools/plan_delta.py pool|kept [lesson …]`.
- `pool`: mechanical drops go to `drops.tsv`; per common lesson, up to POOL × quota survivors are chosen (round-robin
  across anchors, each stem form up to its 2025 share + 10, keys-not-longest first) into `<lesson>.pool.json` for the
  Sonnet style check. The rest stay in `held.tsv` («not pooled»), not dropped.
- `kept`: style-check drops applied, the pool trimmed to quota into `<lesson>.kept-derived.json` (surplus → `held.tsv`
  «over quota»); every lesson, tax ones included, gets `delta/<lesson>.md` for the writers.
"""

from __future__ import annotations

import csv
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from aeat_stats import ARTICLE, TARGET, form_of, longest_is_key  # noqa: E402
from mechanical_style import failures  # noqa: E402
from quotas import quotas  # noqa: E402

BANK = Path(__file__).resolve().parents[1]
ROOT = BANK.parents[3]
LESSONS = ROOT / "content" / "aeat-agentes-hacienda" / "es" / "lessons"
POOL = 1.3
QUOTA = quotas()
DOUBTFUL = ["2024-43", "2022X-69", "2025-20", "2025-24", "2023-80", "2022X-88"]


def lesson_of(tema: str) -> str:
    part, n = tema.split(".")
    return f"m0{ {'I': 1, 'II': 2, 'III': 3}[part] }-l{int(n):02d}"


def tema_of(lesson: str) -> str:
    return f"{ {'1': 'I', '2': 'II', '3': 'III'}[lesson[2]] }.{int(lesson[-2:])}"


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def trim(qs: list[dict[str, object]], size: int) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    if len(qs) <= size:
        return qs, []
    ceiling = {f: math.floor(size * (share + 10) / 100) for f, share in TARGET.items()}
    by_anchor: dict[str, list[dict[str, object]]] = defaultdict(list)
    for q in sorted(qs, key=lambda q: (longest_is_key(q), str(q["id"]))):
        by_anchor[str(q["anchor"])].append(q)
    kept: list[dict[str, object]] = []
    forms: Counter[str] = Counter()
    while len(kept) < size and any(by_anchor.values()):
        progressed = False
        for queue in by_anchor.values():
            while queue:
                q = queue.pop(0)
                form = form_of(q)
                if forms[form] < ceiling.get(form, 0):
                    kept.append(q)
                    forms[form] += 1
                    progressed = True
                    break
            if len(kept) >= size:
                break
        if not progressed:
            break
    ids = {q["id"] for q in kept}
    return sorted(kept, key=lambda q: str(q["id"])), [q for q in qs if q["id"] not in ids]


def lmc_lines(markdown: str) -> list[str]:
    block = re.search(r"^## Lo que más cae\n(.*?)(?=^## )", markdown, re.M | re.S)
    items = re.split(r"\n(?=- )", block.group(1).strip()) if block else []
    return [" ".join(i.split()).removeprefix("- ") for i in items if i.strip()]


def delta_sheet(lesson: str, kept: list[dict[str, object]], next_id: int) -> str:
    t = tema_of(lesson)
    quota, need = QUOTA[t], max(0, QUOTA[t] - len(kept))
    forms = Counter(form_of(q) for q in kept)
    lines = [
        f"# Delta sheet — {t} (`{lesson}`)",
        "",
        f"Quota {quota}. Kept so far {len(kept)}. **To author: {need}** (write about {math.ceil(need * 1.15)} to absorb "
        f"drops). Ids start at `{lesson}-q{next_id:04d}`. Then, beyond the quota need, one question for every «Lo que más "
        "cae» line and every fact of the official pack no kept question tests (never a fact from the six doubtful keys: "
        f"{', '.join(DOUBTFUL)}).",
        "",
        "## Stem forms the tema still needs",
        "",
        "Target = 2025 share × quota (±10 points allowed). A negative «need» means write none of that form.",
        "",
        "| Form | 2025 % | Target | Kept | Need |",
        "|---|---|---|---|---|",
    ]
    for form, share in TARGET.items():
        target = round(quota * share / 100)
        lines.append(f"| {form} | {share} | {target} | {forms.get(form, 0)} | {target - forms.get(form, 0)} |")
    lines += ["", "## «Lo que más cae» lines", ""]
    lines += [f"{n}. {line}" for n, line in enumerate(lmc_lines((LESSONS / f"{lesson}.md").read_text(encoding="utf-8")), 1)]
    lines += ["", "## Kept questions by cited unit (do not duplicate their fact and angle)", ""]
    by_anchor: dict[str, list[dict[str, object]]] = defaultdict(list)
    for q in kept:
        by_anchor[str(q.get("anchor") or q.get("lesson_anchor") or "authored")].append(q)
    for anchor in sorted(by_anchor):
        lines.append(f"### `{anchor}` ({len(by_anchor[anchor])})")
        for q in by_anchor[anchor]:
            options = q["options"]
            assert isinstance(options, dict)
            lines.append(f"- {q['id']}: {q['prompt']} → {options[str(q['correct'])]}")
        lines.append("")
    return "\n".join(lines)


def write_tsv(path: Path, header: str, rows: list[str]) -> None:
    path.write_text(header + "\n" + "\n".join(rows) + ("\n" if rows else ""), encoding="utf-8")


def main(mode: str, only: list[str]) -> None:
    (BANK / "delta").mkdir(exist_ok=True)
    drops_path, held_path = BANK / "drops.tsv", BANK / "held.tsv"
    if not drops_path.exists():
        write_tsv(drops_path, "id\ttema\tbatch\tcheck\treason", [])
    drops = {r["id"] for r in read_tsv(drops_path)}
    held_rows = [r for r in read_tsv(held_path)]
    for lesson in sorted(p.name.split(".")[0] for p in (BANK / "derived").glob("*.derived.json")) if mode == "pool" else []:
        if only and lesson not in only:
            continue
        t = tema_of(lesson)
        derived = json.loads((BANK / "derived" / f"{lesson}.derived.json").read_text(encoding="utf-8"))
        mech = [(q, failures(q)) for q in derived]
        new_drops = [f"{q['id']}\t{t}\tmechanical\t{','.join(sorted({i for i, _ in f}))}\t{'; '.join(d for _, d in f)}"
                     for q, f in mech if f and q["id"] not in drops]
        with drops_path.open("a", encoding="utf-8") as handle:
            handle.writelines(r + "\n" for r in new_drops)
        drops |= {r.split("\t")[0] for r in new_drops}
        survivors = [q for q in derived if q["id"] not in drops]
        pool, rest = trim(survivors, math.ceil(POOL * QUOTA[t]))
        (BANK / f"{lesson}.pool.json").write_text(json.dumps(pool, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        held_rows = [r for r in held_rows if not r["id"].startswith(f"{lesson}-q") or r["reason"] == "over quota"]
        held_rows += [{"id": str(q["id"]), "tema": t, "reason": "not pooled"} for q in rest]
        print(f"{t}: derived {len(derived)}, mechanical drops {len(new_drops)}, pool {len(pool)}, not pooled {len(rest)}")
    if mode == "kept":
        for lesson in sorted(LESSONS_OF):
            if only and lesson not in only:
                continue
            t = tema_of(lesson)
            pool_path = BANK / f"{lesson}.pool.json"
            pool = json.loads(pool_path.read_text(encoding="utf-8")) if pool_path.exists() else []
            survivors = [q for q in pool if q["id"] not in drops]
            kept, over = trim(survivors, QUOTA[t])
            held_rows = [r for r in held_rows if not (r["id"].startswith(f"{lesson}-q") and r["reason"] == "over quota")]
            held_rows += [{"id": str(q["id"]), "tema": t, "reason": "over quota"} for q in over]
            (BANK / f"{lesson}.kept-derived.json").write_text(json.dumps(kept, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            authored = [q for d in sorted(BANK.glob(f"{lesson}.authored*.draft.json")) for q in json.loads(d.read_text(encoding="utf-8"))]
            kept_authored = [q for q in authored if q["id"] not in drops]
            all_ids = [int(str(q["id"]).rsplit("-q", 1)[1]) for q in [*pool, *authored]] or [0]
            (BANK / "delta" / f"{lesson}.md").write_text(delta_sheet(lesson, kept + kept_authored, max(all_ids) + 1) + "\n", encoding="utf-8")
            print(f"{t}: pool {len(pool)}, survive {len(survivors)}, kept {len(kept)}, held {len(over)}, "
                  f"authored kept {len(kept_authored)}, to author {max(0, QUOTA[t] - len(kept) - len(kept_authored))}")
    write_tsv(held_path, "id\ttema\treason", ["\t".join((r["id"], r["tema"], r["reason"])) for r in held_rows])


LESSONS_OF = [lesson_of(t) for t in QUOTA]

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
