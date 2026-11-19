"""bank_anchors.py [--lesson-dir DIR]: questions of the bank whose cited article is no longer cited in their lesson.

A question's anchor is its `citation:` (article keys «N NORM»). It holds when every key is cited in the lesson text
(prose or esquema rows). Prints per lesson: questions, held, lost; writes edition/bank-anchors.json (lost ids per lesson).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import select_lesson  # noqa: E402
from lesson_model import ROOT  # noqa: E402

COURSE = ROOT / "content/aeat-agentes-hacienda"
EDITION = ROOT / "docs/age-verification/aeat/edition"
WORK = ROOT / "docs/_work/age-verification/aeat/edition"


def norm_key(key: str) -> str:
    return key


def lesson_keys(text: str) -> set[str]:
    return select_lesson.cite_keys(text)


def main(argv: list[str]) -> int:
    lessons_dir = Path(argv[argv.index("--lesson-dir") + 1]) if "--lesson-dir" in argv else COURSE / "es/lessons"
    out: dict[str, list[str]] = {}
    summary = []
    for path in sorted(lessons_dir.glob("m0*.md")):
        lesson = path.stem
        keys = lesson_keys(path.read_text())
        total = held = 0
        lost: list[str] = []
        for ex in sorted((COURSE / "exercises").glob(f"{lesson}-ex-*.yaml")):
            data = yaml.safe_load(ex.read_text())
            for q in data.get("variants", []):
                total += 1
                cite = str(q.get("citation", ""))
                need = lesson_keys(cite if cite.startswith("art") else "arts. " + cite) if cite else set()
                if not need or need <= keys:
                    held += 1
                else:
                    lost.append(q["id"])
        out[lesson] = lost
        summary.append((lesson, total, held, len(lost)))
    (EDITION / "bank-anchors.json").write_text(json.dumps(out, indent=1) + "\n")
    for row in summary:
        print(*row)
    print("total", sum(r[1] for r in summary), "held", sum(r[2] for r in summary), "lost", sum(r[3] for r in summary))
    return 0




def restore_plan() -> None:
    """edition/restore/<lesson>.bank.json: pool sentences and esquemas that carry the lost questions' articles."""
    from lesson_model import key, parse  # noqa: E402

    lost = json.loads((EDITION / "bank-anchors.json").read_text())
    (WORK / "restore").mkdir(exist_ok=True)
    for lesson, ids in lost.items():
        if not ids:
            continue
        pool_text = (ROOT / "docs/age-verification/aeat/pool" / f"{lesson}.md").read_text()
        model = parse(pool_text)
        tags = {r["id"]: r["origin"] for r in json.loads((ROOT / "docs/age-verification/aeat/r2d/tags" / f"{lesson}.json").read_text())}
        units = [("s", s.id, s.text, tags.get(s.id, "")) for b in model.blocks for s in b.sentences
                 if model.sections[b.section].title not in ("Lo que más cae", "Normativa")]
        units += [("e", str(i), " ".join(s.text for s in e.sentences), "") for i, e in enumerate(model.esquemas)]
        sentences: set[str] = set()
        esquemas: set[int] = set()
        by_id = {}
        for ex in sorted((COURSE / "exercises").glob(f"{lesson}-ex-*.yaml")):
            for q in yaml.safe_load(ex.read_text()).get("variants", []):
                by_id[q["id"]] = str(q.get("citation", ""))
        for qid in ids:
            cite = by_id[qid]
            need = select_lesson.cite_keys(cite if cite.startswith("art") else "arts. " + cite)
            for k in sorted(need):
                holders = [u for u in units if k in select_lesson.cite_keys(u[2])]
                if not holders:
                    continue
                holders.sort(key=lambda u: (u[0] == "e", u[3] != "HEAD", len(u[2])))
                kind, ident, _, _ = holders[0]
                if kind == "s":
                    sentences.add(ident)
                else:
                    esquemas.add(int(ident))
        target = WORK / "restore" / f"{lesson}.bank.json"
        if target.exists():
            before = json.loads(target.read_text())
            sentences |= set(before.get("sentences", []))
            esquemas |= set(before.get("esquemas", []))
            ids = sorted(set(ids) | set(before.get("questions", [])))
        target.write_text(json.dumps({"sentences": sorted(sentences), "esquemas": sorted(esquemas), "questions": ids}, indent=1) + "\n")
        print(lesson, "restore", len(sentences), "sentences", len(esquemas), "esquemas for", len(ids), "questions")


if __name__ == "__main__":
    code = main(sys.argv[1:])
    if "--restore" in sys.argv:
        restore_plan()
    sys.exit(code)
