"""layer.py: the explanation layer of edition step 2 (R4.11, second design): questions, case, purpose, terms.

Draft `edition/explanation/<lesson>/layer.md`, headings copied exactly from the lesson:

    === SECTION ## Heading [#2]
    PQ: ¿…? ¿…?
    CASO: <40–80 words>
    PARA: <one sentence that quotes or follows the norm's preámbulo, with its citation>
    === SKIP ## Heading :: reason

Commands: lint · apply · strip · drop <lesson> <key> · replace <lesson> <key> <file> · terms <lesson> · words.
Keys: `pq:`, `caso:`, `para:`, `term:` + heading#n. The literal sentences are never edited.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

from explanation import FILLERS, HEADING, LAYER, LESSONS, _normal, dropped, section_bodies, words
from lesson_model import ROOT
from normativa import COURSE, load_index

LEADS = {"pq": "**Preguntas que responde:**", "caso": "**Caso.**", "para": "**Para qué sirve.**"}
FIELDS = ("PQ", "CASO", "PARA")
CITATION = re.compile(r"\((?:[^()]*\b(?:art|arts|disposición|apartado|preámbulo|exposición)\b[^()]*)\)", re.I)
LAYER_LINE = re.compile(r"^\*\*(Preguntas que responde:|Caso\.|Para qué sirve\.|Término[^*]*[.:])\*\*")


@dataclass(frozen=True)
class Part:
    kind: str  # pq, caso, para
    heading: str
    occurrence: int
    text: str

    @property
    def key(self) -> str:
        return f"{self.kind}:{self.heading}#{self.occurrence}"

    @property
    def rendered(self) -> str:
        return f"{LEADS[self.kind]} {self.text}"


def parse(lesson: str) -> tuple[list[Part], list[str]]:
    path = LAYER / lesson / "layer.md"
    parts: list[Part] = []
    skips: list[str] = []
    if not path.exists():
        return parts, skips
    for block in re.split(r"^=== ", path.read_text(encoding="utf-8"), flags=re.M)[1:]:
        head, _, body = block.partition("\n")
        kind, _, rest = head.partition(" ")
        if kind == "SKIP":
            skips.append(rest.partition(" :: ")[0].strip())
            continue
        match = re.match(r"(?P<h>#{2,3} .*?)(?:\s+\[#(?P<n>\d+)\])?\s*$", rest)
        if kind != "SECTION" or not match:
            raise ValueError(f"unreadable layer block: {head!r}")
        current: str | None = None
        buffer: dict[str, list[str]] = {}
        for line in body.splitlines():
            field = re.match(r"^(PQ|CASO|PARA):\s*(.*)$", line)
            if field:
                current = field[1]
                buffer[current] = [field[2]]
            elif current and line.strip():
                buffer[current].append(line.strip())
        for name, chunks in buffer.items():
            parts.append(Part(name.lower(), match["h"], int(match["n"] or 1), " ".join(chunks).strip()))
    return parts, skips


def lint(lesson: str) -> list[str]:
    from tradeschool.citations.lesson import scan_lesson

    text = (LESSONS / f"{lesson}.md").read_text(encoding="utf-8")
    sections = {(h, n): body for _, h, n, body in section_bodies(text.split("\n"))}
    index, _ = load_index()
    problems: list[str] = []
    parts, _skips = parse(lesson)
    seen: set[str] = set()
    for part in parts:
        flat = _normal(part.text)
        if part.key in seen:
            problems.append(f"{part.key}: twice")
        seen.add(part.key)
        if (part.heading, part.occurrence) not in sections:
            problems.append(f"{part.key}: heading not in the lesson")
            continue
        if "**" in flat:
            problems.append(f"{part.key}: bold")
        problems += [f"{part.key}: filler «{f}»" for f in FILLERS if f in flat.lower()]
        if part.kind == "pq":
            questions = re.findall(r"¿[^?]*\?", flat)
            if not 2 <= len(questions) <= 4:
                problems.append(f"{part.key}: {len(questions)} questions (2–4)")
            if re.sub(r"¿[^?]*\?", "", flat).strip():
                problems.append(f"{part.key}: text outside the questions")
            continue
        cited = [c for c in scan_lesson(lesson, flat, index).prose if c.norm is not None]
        if not cited:
            problems.append(f"{part.key}: no citation that resolves to a norm")
        if "¿" in flat:
            problems.append(f"{part.key}: question")
        if part.kind == "caso":
            n = words(flat)
            if not 40 <= n <= 80:
                problems.append(f"{part.key}: {n} words (40–80)")
            if len(cited) < 2:
                problems.append(f"{part.key}: fewer than two citations (each step carries its own)")
        if part.kind == "para":
            if len(re.findall(r"[.!?](?:\s|$)", flat)) > 1:
                problems.append(f"{part.key}: more than one sentence")
            if not re.search(r"preámbulo|exposición de motivos", flat, re.I):
                problems.append(f"{part.key}: citation does not name the preámbulo or exposición de motivos")
    return problems


def _insert_end(lines: list[str], sections: list[tuple[int, str, int, str]], heading: str, occurrence: int, block: str) -> None:
    position = next(k for k, (_, h, n, _b) in enumerate(sections) if (h, n) == (heading, occurrence))
    end = sections[position + 1][0] if position + 1 < len(sections) else len(lines)
    while end > 0 and not lines[end - 1].strip():
        end -= 1
    _insert_line(lines, end, block)


def _insert_line(lines: list[str], index: int, block: str) -> None:
    """Insert a layer line at index with a blank before it and a blank after it unless one follows already."""
    after = [] if index < len(lines) and not lines[index].strip() else [""]
    lines[index:index] = ["", block, *after]


def _top_end(lines: list[str], heading_index: int) -> int:
    """Index of the last layer line (questions, purpose, term) right under a heading, or the heading itself."""
    last = heading_index
    for number in range(heading_index + 1, len(lines)):
        line = lines[number]
        if not line.strip():
            continue
        if LAYER_LINE.match(line) and not line.startswith(LEADS["caso"]):
            last = number
            continue
        break
    return last


def apply_terms(lesson: str, cap: int = 5) -> list[str]:
    """Insert up to `cap` «Término.» lines (glossary definition verbatim) under the section of each term's first use."""
    text = (LESSONS / f"{lesson}.md").read_text(encoding="utf-8").rstrip("\n") + "\n"
    from budget import prose_words

    limit = json.loads((LAYER / "budget-v2.json").read_text(encoding="utf-8"))[lesson]
    ceiling = limit["cap"] * limit["pre"]
    picked = []
    done: list[str] = []
    for heading, term, definition in [t for t in terms(lesson, 99) if len(t[2].split()) <= 45][:cap]:
        line = f"**Término: {term}.** {definition}"
        if _normal(line) in _normal(text):
            picked.append((heading, term, definition))
            continue
        if prose_words(text) + len(line.split()) > ceiling:
            continue
        picked.append((heading, term, definition))
        lines = text.split("\n")
        at = next(i for i, h, n, _ in section_bodies(lines) if h == heading)
        _insert_line(lines, _top_end(lines, at) + 1, line)
        text = "\n".join(lines)
        done.append(f"{heading} :: {term}")
    (LESSONS / f"{lesson}.md").write_text(text, encoding="utf-8")
    (LAYER / lesson / "terms.json").write_text(json.dumps([{"heading": h, "term": t, "definition": d} for h, t, d in picked], ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return done


def apply(lesson: str) -> list[str]:
    text = (LESSONS / f"{lesson}.md").read_text(encoding="utf-8").rstrip("\n") + "\n"
    done: list[str] = []
    gone = dropped(lesson)
    parts, _ = parse(lesson)
    for part in parts:
        if part.key in gone or _normal(part.rendered) in _normal(text):
            continue
        lines = text.split("\n")
        sections = section_bodies(lines)
        if part.kind == "caso":
            _insert_end(lines, sections, part.heading, part.occurrence, part.rendered)
        else:
            at = next(i for i, h, n, _ in sections if (h, n) == (part.heading, part.occurrence))
            _insert_line(lines, _top_end(lines, at) + 1, part.rendered)
        text = "\n".join(lines)
        done.append(part.key)
    (LESSONS / f"{lesson}.md").write_text(text, encoding="utf-8")
    return done


def strip(lesson: str) -> int:
    """Remove every layer line (questions, case, purpose, term) so the lesson is its literal self plus overview and notes."""
    path = LESSONS / f"{lesson}.md"
    lines = path.read_text(encoding="utf-8").split("\n")
    out: list[str] = []
    removed = 0
    for line in lines:
        if LAYER_LINE.match(line):
            removed += 1
            continue
        out.append(line)
    path.write_text(re.sub(r"\n{3,}", "\n\n", "\n".join(out)), encoding="utf-8")
    return removed


def drop(lesson: str, key: str) -> None:
    part = next(p for p in parse(lesson)[0] if p.key == key)
    path = LESSONS / f"{lesson}.md"
    text = path.read_text(encoding="utf-8")
    new = re.sub(r"\n?" + re.escape(part.rendered) + r"\n(?:\n)?", "\n", text, count=1)
    path.write_text(re.sub(r"\n{3,}", "\n\n", new), encoding="utf-8")
    with (LAYER / lesson / "dropped.txt").open("a", encoding="utf-8") as handle:
        handle.write(key + "\n")


def replace(lesson: str, key: str, new_text: str) -> None:
    part = next(p for p in parse(lesson)[0] if p.key == key)
    for path in (LAYER / lesson / "layer.md", LESSONS / f"{lesson}.md"):
        old = part.text if path.name == "layer.md" else part.rendered
        new = new_text.strip() if path.name == "layer.md" else f"{LEADS[part.kind]} {new_text.strip()}"
        body = path.read_text(encoding="utf-8")
        if old not in body:
            # the draft may wrap lines: match on the flattened draft instead
            if path.name == "layer.md":
                raise SystemExit(f"{key}: old text not found in layer.md (keep one line per field)")
            raise SystemExit(f"{key}: old text not found in the lesson")
        path.write_text(body.replace(old, new, 1), encoding="utf-8")


def terms(lesson: str, cap: int = 8) -> list[tuple[str, str, str]]:
    """(section heading, term, definition) for glossary terms this lesson uses but does not teach, at their first section."""
    glossary = yaml.safe_load((COURSE / "glossary.yaml").read_text(encoding="utf-8"))["terms"]
    marks = (COURSE / "glossary-links.es.txt").read_text(encoding="utf-8").splitlines()
    ids = [m.split()[2] for m in marks if m.startswith(f"{lesson} ")]
    by_id = {t["id"]: t for t in glossary}
    text = (LESSONS / f"{lesson}.md").read_text(encoding="utf-8")
    sections = section_bodies(text.split("\n"))
    found: list[tuple[str, str, str]] = []
    for term_id in dict.fromkeys(ids):
        entry = by_id.get(term_id)
        if not entry or entry.get("origin") == lesson:
            continue
        for _, heading, _n, body in sections:
            if re.search(re.escape(entry["es"]), body, re.I) and HEADING.match(heading):
                found.append((heading, entry["es"], entry["definition"]["es"].strip()))
                break
    return found[:cap]


if __name__ == "__main__":
    command, lesson, *rest = sys.argv[1:]
    if command == "lint":
        print("\n".join(lint(lesson)))
    elif command == "apply":
        print("\n".join(apply(lesson)))
    elif command == "strip":
        print(strip(lesson))
    elif command == "drop":
        drop(lesson, rest[0])
    elif command == "replace":
        replace(lesson, rest[0], Path(rest[1]).read_text(encoding="utf-8"))
    elif command == "apply-terms":
        print("\n".join(apply_terms(lesson)))
    elif command == "terms":
        for heading, term, definition in terms(lesson):
            print(f"{heading} :: {term} :: {definition}")
    elif command == "words":
        parts, _ = parse(lesson)
        print(sum(words(p.rendered) for p in parts))
