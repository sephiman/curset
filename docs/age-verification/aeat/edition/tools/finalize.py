"""finalize.py [--write] [lesson…]: assemble, rebuild «Normativa», write the lesson and its reserve.

Without --write the assembled text goes to edition/selection/<lesson>.text only. With --write the lesson is replaced in
content/ and reserve/<lesson>.md is written (every sentence, row and esquema not kept, with origin tag and report).
Always writes edition/selection/<lesson>.json (counts by class and by origin tag, words, overrun).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import normativa  # noqa: E402
import select_lesson  # noqa: E402
from lesson_model import ROOT, key, section_path, words  # noqa: E402

AEAT = ROOT / "docs/age-verification/aeat"
EDITION = AEAT / "edition"
CONTENT = ROOT / "content/aeat-agentes-hacienda/es/lessons"


# List-marker artifacts that render as literal text (frontend/src/lib/refs/listShape.ts): fixed in the table rows only.
MARKER_RULES = [
    (re.compile(r"(?<=[:;.] )- (?=\d+\.º)"), ""),  # «: - 1.º Número…» flattened sub-list
    (re.compile(r"(?<=[:;.] )(\d+)\.(?=\s*\|)"), r"\1"),  # a cell that ends «: 5.»
    (re.compile(r"\| ([a-z]\)) - \|"), r"| \1 |"),  # a cell that is only «e) -»
]


def fix_markers(text: str) -> tuple[str, list[str]]:
    changes: list[str] = []
    out = []
    for line in text.split("\n"):
        new = line
        if line.startswith("|"):
            for rule, repl in MARKER_RULES:
                new = rule.sub(repl, new)
        if new != line:
            changes.append(f"{line[:110]} → {new[:110]}")
        out.append(new)
    return "\n".join(out), changes


def apply_patches(lesson: str, text: str) -> tuple[str, list[str]]:
    """Verifier replacements (edition/patches.json): whole-sentence swaps or drops, matched by their words."""
    path = EDITION / "patches.json"
    done: list[str] = []
    if not path.exists():
        return text, done
    for patch in json.loads(path.read_text()).get(lesson, []):
        pattern = r"\s+".join(re.escape(w) for w in patch["old"].split())
        if patch["old"].startswith("|"):
            new = re.sub(rf"^{pattern}$", lambda _m: patch["new"], text, count=1, flags=re.M)
        elif patch["new"]:
            new = re.sub(pattern, lambda _m: patch["new"], text, count=1)
        else:
            new = re.sub(rf"^(?:- )?{pattern}\.?\n(?:\n(?=\n))?", "", text, count=1, flags=re.M)
            if new == text:
                new = re.sub(rf"\s?{pattern}", "", text, count=1)
        done.append(("applied " if new != text else "NOT FOUND ") + patch["old"][:80])
        text = new
    return text, done


def pool_normativa(text: str) -> list[str]:
    start = text.find("\n## Normativa")
    return [x for x in text[start:].splitlines() if x.startswith("- ")] if start >= 0 else []


def finalize(lesson: str, budget: int, write: bool) -> dict[str, object]:
    sel, text, derived = select_lesson.assemble(lesson, budget)
    model = sel.model
    body = text
    lines = normativa.derive(body, pool_normativa(sel.text))
    if lines:
        text = body.rstrip("\n") + "\n\n## Normativa\n\n" + "\n".join(lines) + "\n"
    text, marker_fixes = fix_markers(text)
    text, patched = apply_patches(lesson, text)
    (EDITION / "selection" / f"{lesson}.text").write_text(text)
    keep = set(sel.cls) | derived
    tags = sel.tags
    by_origin: dict[str, int] = {}
    by_origin_words: dict[str, int] = {}
    kept_words = 0
    for b in model.blocks:
        for s in b.sentences:
            if key(s) in keep:
                o = tags.get(s.id, {}).get("origin", "reworded")
                by_origin[o] = by_origin.get(o, 0) + 1
                by_origin_words[o] = by_origin_words.get(o, 0) + words(s.text)
                kept_words += words(s.text)
    esq_rows_kept = sum(len(model.esquemas[i].sentences) for i in sel.esq_cls)
    esq_rows_total = sum(len(e.sentences) for e in model.esquemas)
    for i in sel.esq_cls:
        for s in model.esquemas[i].sentences:
            o = tags.get(s.id, {}).get("origin", "reworded")
            by_origin[f"row:{o}"] = by_origin.get(f"row:{o}", 0) + 1
    normativa_words = sum(words(x) for x in lines)
    prose_total = sum(words(s.text) for b in model.blocks for s in b.sentences)
    if write:
        (CONTENT / f"{lesson}.md").write_text(text)
        write_reserve(lesson, sel, keep, pool_normativa(sel.text), lines)
    gaps = [c for c, n in (("a", 0),)]
    del gaps
    info = {
        "lesson": lesson,
        "budget": budget,
        "prose_words_now": kept_words,
        "normativa_words": normativa_words,
        "overrun": max(kept_words - budget, 0),
        "pool_prose_words": prose_total,
        "sentences_kept": sum(by_origin.get(o, 0) for o in by_origin if not o.startswith("row:")),
        "sentences_total": len(sel.all) + sum(1 for b in model.blocks if b.section in sel.derived_sections for _ in b.sentences),
        "kept_by_origin": by_origin,
        "kept_words_by_origin": by_origin_words,
        "by_class_sentences": {c: sum(1 for v in sel.cls.values() if v == c) for c in set(sel.cls.values())},
        "by_class_words": {
            c: sum(words(s.text) for b, s in sel.all if sel.cls.get(key(s)) == c) for c in set(sel.cls.values())
        },
        "esquemas_kept": len(sel.esq_cls),
        "esquemas_total": len(model.esquemas),
        "esquema_rows_kept": esq_rows_kept,
        "esquema_rows_total": esq_rows_total,
        "derived_kept": len(derived),
        "normativa_lines": len(lines),
        "marker_fixes": marker_fixes,
        "patches": patched,
    }
    (EDITION / "selection" / f"{lesson}.json").write_text(json.dumps(info, ensure_ascii=False, indent=1) + "\n")
    return info


def write_reserve(lesson: str, sel, keep: set, old_normativa: list[str], new_normativa: list[str]) -> None:
    model = sel.model
    out = [
        f"# Reserve — {lesson}",
        "",
        "Verified sentences and esquemas of the R2d lesson that the edition left out. Not loaded by the course. Each "
        "line: `sentence id` · origin tag · report.",
        "",
    ]
    last: tuple[str, ...] = ()
    items: list[tuple[int, str, tuple[str, ...]]] = []
    for b in model.blocks:
        path = tuple(section_path(model, b.section)) if b.section >= 0 else ()
        for s in b.sentences:
            if key(s) in keep:
                continue
            tag = sel.tags.get(s.id, {})
            items.append((s.first_line, f"- `{s.id}` · {tag.get('origin', 'reworded')} · {tag.get('report', '')} — {s.text}", path))
    for i, e in enumerate(model.esquemas):
        if i in sel.esq_cls:
            continue
        path = tuple(section_path(model, e.section)) if e.section >= 0 else ()
        rows = [f"- esquema {e.kind} «{e.title}» ({len(e.sentences)} rows)"]
        for s in e.sentences:
            tag = sel.tags.get(s.id, {})
            rows.append(f"  - `{s.id}` · {tag.get('origin', 'reworded')} · {tag.get('report', '')} — {s.text}")
        items.append((e.first, "\n".join(rows), path))
    items.sort(key=lambda x: x[0])
    for _, text, path in items:
        if path != last:
            out += ["", f"## {' › '.join(path) if path else '(before the first heading)'}", ""]
            last = path
        out.append(text)
    dropped = [l for l in old_normativa if not any(l.split(":")[0] == n.split(":")[0] for n in new_normativa)]
    if dropped:
        out += ["", "## Normativa lines left out", ""] + dropped
    (AEAT / "reserve" / f"{lesson}.md").write_text("\n".join(out) + "\n")


def main(argv: list[str]) -> int:
    write = "--write" in argv
    names = [a for a in argv if not a.startswith("--")]
    table = json.loads((EDITION / "budget.json").read_text())
    for lesson in names or [x for x in table if x != "m00-l01"]:
        info = finalize(lesson, int(table[lesson]["budget"]), write)
        print(
            lesson,
            f"budget {info['budget']} prose {info['prose_words_now']} (+normativa {info['normativa_words']}) "
            f"overrun {info['overrun']} sentences {info['sentences_kept']}/{info['sentences_total']} "
            f"esq {info['esquemas_kept']}/{info['esquemas_total']}",
            info["by_class_words"],
        )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
