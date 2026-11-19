"""anchors.py: repair loop against the registry's citation cross-reference check (the oracle).

Questions that cite an article the lesson's prose no longer cites get the shortest pool sentence that cites it back;
an esquema row that cites an article the prose never cites gets the pool sentence that cites it (nearest before the
esquema in the pool), or the esquema is dropped when no sentence does. Cumulative in edition/restore/<lesson>.anchors.json.
Loops: write lessons, ask the registry, repair, until the check is clean or stops improving.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import select_lesson  # noqa: E402
from lesson_model import ROOT, parse  # noqa: E402

COURSE = ROOT / "content/aeat-agentes-hacienda"
AEAT = ROOT / "docs/age-verification/aeat"
EDITION = AEAT / "edition"
WORK = ROOT / "docs/_work/age-verification/aeat/edition"
QUESTION = re.compile(r"question (\S+)/(\S+) cites «(.+?)», which its lesson (\S+) never cites")
ESQUEMA = re.compile(r"lesson (m\d\d-l\d\d) line (\d+), esquema «(.*?)», row «(.*?)»: cites «(.+?)», which the lesson's prose never cites")


def oracle() -> str:
    from tradeschool.content.registry import ContentError, load_registry

    try:
        load_registry(COURSE, check_excerpts=False)
    except ContentError as exc:
        return str(exc)
    return ""


PAREN = re.compile(r"\(((?:[^()]|\([^()]*\))*)\)")


def parenthetical(text: str) -> str:
    """The parenthesised citations of a sentence: the only ones the registry counts as prose citations."""
    return " ".join(p for p in PAREN.findall(text) if re.search(r"\b(?:arts?\.|apartado|disposición|título|capítulo)", p))


def cover(model, cite: str, tags: dict[str, str], before: int | None = None) -> tuple[list, list[str]]:
    """One pool sentence per unit of the citation, with the norm in its parenthesised citations; units no sentence covers."""
    flat = " ".join(cite.split())
    m = re.match(r"^arts?\.\s+(.*?)\s+([A-ZÁÉÍÓÚ].*)$", flat)
    if m:
        unit_text, norm = m.group(1), m.group(2)
        units = re.findall(r"\d+(?: bis| ter| quater)?(?:\.\d+)?(?:\.[a-z]\))?", unit_text)
    else:
        units, norm = [flat], flat
    sentences = [(b, s, parenthetical(s.text)) for b in model.blocks for s in b.sentences]
    chosen: list = []
    missing: list[str] = []
    for unit in units or [flat]:
        pattern = re.compile(r"(?<![\d.])" + re.escape(unit) + r"(?!\d|\.\d)") if m else None
        found = [
            (b, s) for b, s, p in sentences
            if p and (norm in p) and (pattern.search(p) if pattern else flat in p)
        ]
        if not found and m is not None:
            loose = re.compile(r"(?<![\d.])" + re.escape(unit) + r"(?!\d)")
            found = [(b, s) for b, s, p in sentences if p and norm in p and loose.search(p)]
        if not found and m is None:
            found = [(b, s) for b, s, p in sentences if flat in p]
        if not found:
            missing.append(unit)
            continue
        if before is not None:
            found.sort(key=lambda bs: (abs(before - bs[0].last) if bs[0].last < before else 10_000 + bs[0].first, len(bs[1].text)))
        else:
            found.sort(key=lambda bs: (tags.get(bs[1].id) != "HEAD", len(bs[1].text)))
        chosen.append(found[0])
    return chosen, missing


def load(lesson: str) -> dict:
    path = WORK / "restore" / f"{lesson}.anchors.json"
    return json.loads(path.read_text()) if path.exists() else {"sentences": [], "drop_esquemas": []}


def save(lesson: str, data: dict) -> None:
    data["sentences"] = sorted(set(data["sentences"]))
    data["drop_esquemas"] = sorted(set(data["drop_esquemas"]))
    (WORK / "restore" / f"{lesson}.anchors.json").write_text(json.dumps(data, indent=1) + "\n")


def repair(message: str) -> set[str]:
    touched: set[str] = set()
    pools: dict[str, tuple] = {}

    def pool(lesson: str):
        if lesson not in pools:
            model = parse((AEAT / "pool" / f"{lesson}.md").read_text())
            tags = {r["id"]: r["origin"] for r in json.loads((AEAT / "r2d/tags" / f"{lesson}.json").read_text())}
            pools[lesson] = (model, tags)
        return pools[lesson]

    state: dict[str, dict] = {}
    for _ex, _qid, cite, lesson in QUESTION.findall(message):
        model, tags = pool(lesson)
        data = state.setdefault(lesson, load(lesson))
        chosen, missing = cover(model, cite, tags)
        if missing:
            print("no pool sentence for question citation", lesson, cite, missing)
        data["sentences"] += [x[1].id for x in chosen]
        touched.add(lesson)
    for lesson, _line, title, row, cite in ESQUEMA.findall(message):
        model, tags = pool(lesson)
        data = state.setdefault(lesson, load(lesson))
        index = next(
            (i for i, e in enumerate(model.esquemas) if e.title == title and any(row in s.text for s in e.sentences)), None
        )
        esq = model.esquemas[index] if index is not None else None
        chosen, missing = cover(model, cite, tags, before=esq.first if esq else None)
        data["sentences"] += [x[1].id for x in chosen]
        if missing and index is not None:
            data["drop_esquemas"].append(index)
            print("esquema dropped, no sentence cites", lesson, title[:50], missing)
        touched.add(lesson)
    for lesson, data in state.items():
        save(lesson, data)
    return touched


def main() -> int:
    previous = None
    for round_ in range(1, 9):
        message = oracle()
        problems = len(QUESTION.findall(message)) + len(ESQUEMA.findall(message))
        other = [p for p in message.split("; ") if p and not QUESTION.search(p) and not ESQUEMA.search(p)]
        print(f"round {round_}: {problems} citation problems (+{len(other)} other)")
        if not message:
            print("clean")
            return 0
        if problems == 0 or problems == previous:
            print("stopped:", "\n".join(o[:200] for o in other[:8]))
            return 1
        previous = problems
        touched = repair(message)
        subprocess.run(
            ["uv", "run", "python", str(HERE / "finalize.py"), "--write", *sorted(touched)],
            cwd=ROOT / "backend", check=True, capture_output=True,
        )
    return 1


if __name__ == "__main__":
    sys.exit(main())
