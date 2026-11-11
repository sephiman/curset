"""Trim style-checked candidates to quota and write each lesson's delta sheet for the writers.

Run from backend/: `uv run python ../docs/age-verification/c2/bank/tools/plan_delta.py bloque-ii [lesson …]`.
Kept = derived minus `drops.tsv` (mechanical and style). Over quota, candidates are kept round-robin across anchors,
each stem form only up to its 2025 share + 10, keys-not-longest first; the rest go to `held.tsv` (not dropped).
Writes `<bloque>/<lesson>.kept-derived.json` and `<bloque>/delta/<lesson>.md`.
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
from c2_stats import TARGET, longest_is_key, set_of, stem_form  # noqa: E402
from derive_candidates import C2, citations_of, tema  # noqa: E402

BANK = Path(__file__).resolve().parents[1]
QUOTA = {
    "I.1": 136, "I.2": 174, "I.3": 116, "I.4": 135, "I.5": 194, "I.6": 97, "I.7": 135, "I.8": 213, "I.9": 116,
    "I.10": 155, "I.11": 290, "I.12": 58, "I.13": 205, "I.14": 229, "I.15": 155, "I.16": 174,
    "II.1": 100, "II.2": 123, "II.3": 122, "II.4": 178, "II.5": 256, "II.6": 156, "II.7": 267, "II.8": 234,
    "II.9": 290, "II.10": 223, "II.11": 223, "II.12": 278,
}


def dropped(folder: Path) -> set[str]:
    with (folder / "drops.tsv").open(encoding="utf-8") as handle:
        return {row["id"] for row in csv.DictReader(handle, delimiter="\t")}


def trim(qs: list[dict[str, object]], quota: int, kind: str) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    if len(qs) <= quota:
        return qs, []
    ceiling = {f: math.floor(quota * (share + 10) / 100) for f, share in TARGET[kind].items()}
    by_anchor: dict[str, list[dict[str, object]]] = defaultdict(list)
    for q in sorted(qs, key=lambda q: (longest_is_key(q), str(q["id"]))):
        by_anchor[str(q["anchor"])].append(q)
    kept: list[dict[str, object]] = []
    forms: Counter[str] = Counter()
    while len(kept) < quota and any(by_anchor.values()):
        progressed = False
        for anchor in list(by_anchor):
            queue = by_anchor[anchor]
            while queue:
                q = queue.pop(0)
                form = stem_form(str(q["prompt"]), kind)
                if forms[form] < ceiling.get(form, 0):
                    kept.append(q)
                    forms[form] += 1
                    progressed = True
                    break
            if len(kept) >= quota:
                break
        if not progressed:
            break
    kept_ids = {q["id"] for q in kept}
    return sorted(kept, key=lambda q: str(q["id"])), [q for q in qs if q["id"] not in kept_ids]


def lesson_lines(markdown: str) -> tuple[list[str], list[str]]:
    """(«Lo que más cae» lines, list items and paragraphs of the body) as flat text."""
    lqmc = re.search(r"^## Lo que más cae\n(.*?)(?=^## )", markdown, re.M | re.S)
    items = re.split(r"\n(?=- )", lqmc.group(1).strip()) if lqmc else []
    return [" ".join(i.split()) for i in items if i.strip()], []


def delta_sheet(lesson: str, kept: list[dict[str, object]], markdown: str, next_id: int) -> str:
    t = tema(lesson)
    kind = set_of(t)
    quota = QUOTA[t]
    need = max(0, quota - len(kept))
    forms = Counter(stem_form(str(q["prompt"]), kind) for q in kept)
    lines = [
        f"# Delta sheet — {t} (`{lesson}`)",
        "",
        f"Quota {quota}. Kept questions {len(kept)} (kept derived `{lesson}.kept-derived.json` plus kept authored drafts). **To author: {need} to reach "
        f"the quota** (write about {math.ceil(need * 1.15)} to absorb drops), **plus** one question for every fact the "
        f"lesson states that no kept candidate tests, every «Lo que más cae» line no kept candidate tests, and every "
        f"coverage question of the official pack (`questions/{lesson}.md`) whose fact no kept candidate tests. "
        f"Ids start at `{lesson}-q{next_id:03d}`.",
        "",
        "## Stem forms the tema still needs",
        "",
        "Target = 2025 share × quota (style guide § 3 of the plan; ±10 points allowed). «Need» = target − kept, "
        "the forms to favour; a negative «need» means kept already exceeds the target, so write none of that form.",
        "",
        "| Form | 2025 % | Target | Kept | Need |",
        "|---|---|---|---|---|",
    ]
    for form, share in TARGET[kind].items():
        target = round(quota * share / 100)
        lines.append(f"| {form} | {share} | {target} | {forms.get(form, 0)} | {target - forms.get(form, 0)} |")
    lqmc, _ = lesson_lines(markdown)
    lines += [
        "",
        "## «Lo que más cae» lines",
        "",
        "Every line must be tested by at least one question at the end. In your notes, map each line to a kept id "
        "below that tests it or to a question you write.",
        "",
        *[f"{n}. {line[2:] if line.startswith('- ') else line}" for n, line in enumerate(lqmc, start=1)],
        "",
        "## Kept candidates by cited unit (do not duplicate their facts and angles)",
        "",
    ]
    by_anchor: dict[str, list[dict[str, object]]] = defaultdict(list)
    for q in kept:
        by_anchor[str(q["anchor"])].append(q)
    for anchor in sorted(by_anchor):
        lines.append(f"### `{anchor}` ({len(by_anchor[anchor])})")
        for q in by_anchor[anchor]:
            options = q["options"]
            assert isinstance(options, dict)
            lines.append(f"- {q['id']}: {q['prompt']} → {options[str(q['correct'])]}")
        lines.append("")
    return "\n".join(lines)


def main(bloque: str, only: list[str]) -> None:
    folder = BANK / bloque
    drops = dropped(folder)
    held_path = folder / "held.tsv"
    existing = [r for r in (held_path.read_text(encoding="utf-8").splitlines()[1:] if held_path.exists() else []) if r]
    pretrim = [r for r in existing if r.split("\t")[2].startswith("pre-trim")]
    drops |= {r.split("\t")[0] for r in pretrim}  # held before the style check: never candidates here
    _, markdown = citations_of(C2)
    (folder / "delta").mkdir(exist_ok=True)
    held_rows: list[str] = []
    for path in sorted(folder.glob("*.derived.json")):
        lesson = path.name.split(".")[0]
        if only and lesson not in only:
            continue
        derived = json.loads(path.read_text(encoding="utf-8"))
        survivors = [q for q in derived if q["id"] not in drops]
        t = tema(lesson)
        kept, held = trim(survivors, QUOTA[t], set_of(t))
        held_rows += [f"{q['id']}\t{t}\tover quota" for q in held]
        (folder / f"{lesson}.kept-derived.json").write_text(
            json.dumps(kept, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
        )
        authored = [
            q
            for draft in sorted(folder.glob(f"{lesson}.authored*.draft.json"))
            for q in json.loads(draft.read_text(encoding="utf-8"))
        ]
        kept_authored = [q for q in authored if q["id"] not in drops]
        for q in kept_authored:
            q.setdefault("anchor", str(q.get("lesson_anchor") or "authored"))
        all_ids = [int(str(q["id"]).rsplit("-q", 1)[1]) for q in derived + authored]
        next_id = max(all_ids) + 1
        (folder / "delta" / f"{lesson}.md").write_text(
            delta_sheet(lesson, kept + kept_authored, markdown[lesson], next_id) + "\n", encoding="utf-8"
        )
        print(f"{t} {lesson}: derived {len(derived)}, survive {len(survivors)}, kept {len(kept)}, held {len(held)}, "
              f"to author {max(0, QUOTA[t] - len(kept) - len(kept_authored))} (kept authored {len(kept_authored)})")
    lessons_done = {r.split("\t")[0].rsplit("-q", 1)[0] for r in held_rows} | set(only)
    keep_rows = [
        r for r in existing if r in pretrim or r.split("\t")[0].rsplit("-q", 1)[0] not in lessons_done
    ]
    held_path.write_text("id\ttema\treason\n" + "\n".join(keep_rows + held_rows) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
