"""records.py <lesson…>: the provenance record of a lesson after the edition step 2 (explanation layer, «Normativa» rebuild).

Keeps every record entry whose sentence is still in the lesson, adds an entry for each new sentence that has a PASS in
`edition/explanation/<lesson>/verify.md` (written here from the verifier verdicts), drops the rest, and rewrites the
count line. A new sentence without a PASS is reported and the record is left as it was. Tags: new sentences go to
`r2d/tags/<lesson>.json` with origin «explanation» (the layer) or «normativa» (rebuilt lines), and the report path.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from functools import cache

import yaml
from pathlib import Path

from explanation import EDITION, LAYER, _normal, parse_draft
from layer import parse as parse_layer
from lesson_model import ROOT
from normativa import COURSE, LESSONS
from scripts.provenance import parse_record, sentence_id, sentences

RECORDS = ROOT / "docs/age-verification/aeat/r2"
TAGS = ROOT / "docs/age-verification/aeat/r2d/tags"
VERDICT_ROW = re.compile(r"^\|\s*`?(?P<key>[^|`]+?)`?\s*\|\s*(?P<verdict>PASS|FAIL|OK|REWRITE|CUT)\b")


def verdicts(lesson: str, pattern: str) -> dict[str, str]:
    """Key → latest verdict over verifier-N.md / verifier-recheck-N.md in reading order (later wins)."""
    found: dict[str, str] = {}
    for path in sorted((LAYER / lesson).glob(pattern), key=lambda p: (len(p.stem), p.stem)):
        for line in path.read_text(encoding="utf-8").splitlines():
            match = VERDICT_ROW.match(line)
            if match:
                found[match["key"].strip()] = match["verdict"]
    return found


def normativa_sentences(text: str) -> list[str]:
    cut = text.find("\n## Normativa")
    return [s.text for s in sentences(text[cut:])] if cut >= 0 else []


def layer_parts(lesson: str) -> list:
    return parse_layer(lesson)[0]


def write_report(lesson: str, normativa_pass: bool) -> tuple[Path, dict[str, str]]:
    """verify.md: one row per new sentence whose paragraph (or «Normativa» line) has a PASS; returns id → origin."""
    text = (LESSONS / f"{lesson}.md").read_text(encoding="utf-8")
    flat = _normal(text)
    marks = verdicts(lesson, "verifier-*.md")
    rows: dict[str, tuple[str, str]] = {}
    draft = LAYER / lesson / "draft.md"
    for entry in parse_draft(draft) if draft.exists() else []:
        if entry.kind == "nc" and _normal("**No confundir.** " + entry.text) in flat:
            # the bullets are lesson sentences with their own records; the block title is fixed text
            for sentence in sentences("**No confundir.**"):
                rows[sentence.id] = ("explanation", entry.key)
            continue
        if entry.kind not in ("overview", "after") or _normal(entry.text) not in flat:
            continue
        if marks.get(entry.key) != "PASS":
            continue
        for sentence in sentences(entry.text):
            rows[sentence.id] = ("explanation", entry.key)
    layer_marks = verdicts(lesson, "layer-verifier-*.md")
    for part in layer_parts(lesson):
        if _normal(part.rendered) not in flat:
            continue
        if part.kind != "pq" and layer_marks.get(part.key) != "PASS":
            continue
        for sentence in sentences(part.rendered):
            rows[sentence.id] = ("explanation", part.key)
    glossary = {t["definition"]["es"].strip() for t in yaml.safe_load((COURSE / "glossary.yaml").read_text(encoding="utf-8"))["terms"]}
    terms_path = LAYER / lesson / "terms.json"
    for item in json.loads(terms_path.read_text(encoding="utf-8")) if terms_path.exists() else []:
        line = f"**Término: {item['term']}.** {item['definition']}"
        if item["definition"] in glossary and _normal(line) in flat:
            for sentence in sentences(line):
                rows[sentence.id] = ("explanation", f"term:{item['term']}")
    if normativa_pass:
        for sentence in normativa_sentences(text):
            rows.setdefault(sentence_id(sentence), ("normativa", "Normativa"))
    path = LAYER / lesson / "verify.md"
    body = [f"# Verification report — explanation layer and «Normativa», `{lesson}`", "",
            "Rows are sentence ids; the verdict is the paragraph's (or line's) blind check, see verifier-*.md and normativa-check/.", "",
            "| id | verdict | origin | part |", "|---|---|---|---|"]
    body += [f"| `{sid}` | PASS | {origin} | {part.replace('|', '/')} |" for sid, (origin, part) in sorted(rows.items())]
    path.write_text("\n".join(body) + "\n", encoding="utf-8")
    return path, {sid: origin for sid, (origin, _) in rows.items()}


@cache
def pool_records(lesson: str) -> dict[str, tuple[str, str]]:
    """Id → (record line, text line) of the R2d pool lesson, from the commit before step 1 (its sentences were all verified)."""
    out = subprocess.run(["git", "show", f"8f5434d:docs/age-verification/aeat/r2/{lesson}.md"], capture_output=True, text=True, cwd=ROOT, check=False)
    lines = out.stdout.splitlines()
    return {m.group(1): (line, lines[i + 1]) for i, line in enumerate(lines) if (m := re.match(r"^- `([0-9a-f]{10})` ·", line))}


@cache
def base_records(lesson: str) -> dict[str, tuple[str, str]]:
    """The same from the pre-R2d commit: esquema rows that R2d dropped and step 2 put back keep the record they had."""
    base = (ROOT / "docs/age-verification/aeat/r2d/base-commit.txt").read_text(encoding="utf-8").split()[0]
    out = subprocess.run(["git", "show", f"{base}:docs/age-verification/aeat/r2/{lesson}.md"], capture_output=True, text=True, cwd=ROOT, check=False)
    lines = out.stdout.splitlines()
    return {m.group(1): (line, lines[i + 1]) for i, line in enumerate(lines) if (m := re.match(r"^- `([0-9a-f]{10})` ·", line))}


def passed_texts(lesson: str) -> set[str]:
    """Sentences a defect-fix verifier passed (one per line in defects/verify/passed-<lesson>.txt)."""
    path = EDITION / "defects/verify" / f"passed-{lesson}.txt"
    return set(path.read_text(encoding="utf-8").splitlines()) if path.exists() else set()


def sync(lesson: str, normativa_pass: bool = True) -> list[str]:
    report, origins = write_report(lesson, normativa_pass)
    rel = str(report.relative_to(ROOT))
    path = RECORDS / f"{lesson}.md"
    old = {r.sentence_id: r for r in parse_record(path.read_text(encoding="utf-8"))}
    text = (LESSONS / f"{lesson}.md").read_text(encoding="utf-8")
    entries: list[str] = []
    problems: list[str] = []
    seen: set[str] = set()
    inherited = verified = 0
    old_lines = path.read_text(encoding="utf-8").splitlines()
    raw = {m.group(1): (line, old_lines[i + 1]) for i, line in enumerate(old_lines) if (m := re.match(r"^- `([0-9a-f]{10})` ·", line))}
    for sentence in sentences(text):
        if sentence.id in seen:
            continue
        seen.add(sentence.id)
        if sentence.id in old and sentence.id in raw and old[sentence.id].text == sentence.text and sentence.text not in passed_texts(lesson):
            entries += list(raw[sentence.id])
            inherited += old[sentence.id].inherited
            verified += not old[sentence.id].inherited
        elif sentence.id in pool_records(lesson):
            entries += list(pool_records(lesson)[sentence.id])
            verified += 1
        elif sentence.text in passed_texts(lesson):
            entries += [f"- `{sentence.id}` · verificado: PASS · docs/age-verification/aeat/edition/defects/verify/verifier-{lesson}.md", f"  > {sentence.text}"]
            verified += 1
        elif sentence.id in base_records(lesson):
            entries += list(base_records(lesson)[sentence.id])
            verified += 1
        elif sentence.id in origins:
            entries += [f"- `{sentence.id}` · verificado: PASS · {rel}", f"  > {sentence.text}"]
            verified += 1
        else:
            problems.append(f"{lesson}: no PASS for line {sentence.first_line}: {sentence.text[:80]}")
    if problems:
        return problems
    head = "\n".join(old_lines[: next(i for i, line in enumerate(old_lines) if line.startswith("Frases:"))])
    path.write_text(f"{head}\nFrases: {inherited + verified} · heredadas: {inherited} · verificadas: {verified}.\n\n" + "\n".join(entries) + "\n", encoding="utf-8")
    tags_path = TAGS / f"{lesson}.json"
    tags = json.loads(tags_path.read_text(encoding="utf-8")) if tags_path.exists() else []
    have = {t["id"] for t in tags}
    for sentence in sentences(text):
        if sentence.id in origins and sentence.id not in have:
            have.add(sentence.id)
            tags.append({"id": sentence.id, "line": sentence.first_line, "kind": sentence.kind, "origin": origins[sentence.id], "report": rel})
    tags_path.write_text(json.dumps(tags, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return []


if __name__ == "__main__":
    for lesson in sys.argv[1:]:
        for problem in sync(lesson) or [f"{lesson}: record synced"]:
            print(problem)
