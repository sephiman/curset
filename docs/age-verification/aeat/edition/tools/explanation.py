"""explanation.py: the explanation layer (R4.11) of a lesson, from a writer's draft to the lesson file.

Draft (`edition/explanation/<lesson>/draft.md`), one entry per block, headings copied exactly from the lesson:

    === OVERVIEW
    <120–200 words>
    === AFTER ## Heading [#2]
    En pocas palabras. <40–90 words>
    === NC ## Heading
    - <a sentence of the lesson, verbatim>
    === SKIP ## Heading :: reason

Commands: lint <lesson> · apply <lesson> · drop <lesson> <key> · words <lesson>. The literal sentences of a lesson are
never edited: apply only inserts, drop removes an inserted paragraph by its exact text.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

from normativa import COURSE, LESSONS, load_index
from lesson_model import ROOT  # noqa: F401
from scripts.provenance import sentences  # noqa: E402

EDITION = ROOT / "docs/age-verification/aeat/edition"
LAYER = EDITION / "explanation"
LEAD_IN = "En pocas palabras."
HEADING = re.compile(r"^(#{2,3})\s+(.*)$")
FILLERS = (
    "es importante señalar", "cabe destacar", "cabe señalar", "en definitiva", "en este sentido", "no obstante",
    "a la hora de", "en el mundo", "con esto ya", "en resumen", "en conclusión", "sin lugar a dudas",
)
SPLIT_OPENERS = ("Es ", "Eso ", "Son ", "Por eso", "Así,", "Así que", "Y ", "También es", "Esa es la razón", "Para eso sirve")
NUMBER_WORDS = (
    "un|una|uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|quince|veinte|treinta|cuarenta|cincuenta|"
    "sesenta|noventa|cien|ciento|mil|primer[oa]?|segund[oa]|tercer[oa]?|cuart[oa]|quint[oa]|seis"
)
FIGURE = re.compile(rf"\b(\d[\d.,]*|{NUMBER_WORDS})\b", re.I)


@dataclass(frozen=True)
class Entry:
    kind: str  # overview, after, nc, skip
    heading: str
    occurrence: int
    text: str

    @property
    def key(self) -> str:
        return "overview" if self.kind == "overview" else f"{self.kind}:{self.heading}#{self.occurrence}"


def words(text: str) -> int:
    return len(text.split())


def parse_draft(path: Path) -> list[Entry]:
    entries: list[Entry] = []
    for block in re.split(r"^=== ", path.read_text(encoding="utf-8"), flags=re.M)[1:]:
        head, _, body = block.partition("\n")
        text = body.strip()
        if head.strip() == "OVERVIEW":
            entries.append(Entry("overview", "", 1, text))
            continue
        kind, _, rest = head.partition(" ")
        if kind == "SKIP":
            heading, _, reason = rest.partition(" :: ")
            entries.append(Entry("skip", heading.strip(), 1, reason.strip()))
            continue
        match = re.match(r"(?P<h>#{2,3} .*?)(?:\s+\[#(?P<n>\d+)\])?\s*$", rest)
        if kind not in ("AFTER", "NC") or not match:
            raise ValueError(f"unreadable draft block: {head!r}")
        entries.append(Entry(kind.lower(), match["h"], int(match["n"] or 1), text))
    return entries


def section_bodies(lines: list[str]) -> list[tuple[int, str, int, str]]:
    """(heading line index, heading text, occurrence, literal text up to the next heading)."""
    found: list[tuple[int, str, int, str]] = []
    count: dict[str, int] = {}
    heads = [i for i, line in enumerate(lines) if HEADING.match(line) or line.startswith("# ")]
    for n, i in enumerate(heads):
        end = heads[n + 1] if n + 1 < len(heads) else len(lines)
        count[lines[i]] = count.get(lines[i], 0) + 1
        found.append((i, lines[i], count[lines[i]], "\n".join(lines[i + 1 : end])))
    return found


def lesson_text(lesson: str) -> str:
    return (LESSONS / f"{lesson}.md").read_text(encoding="utf-8")


def _normal(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def lint(lesson: str) -> list[str]:
    text = lesson_text(lesson)
    lines = text.split("\n")
    sections = {(h, n): body for _, h, n, body in section_bodies(lines)}
    draft = LAYER / lesson / "draft.md"
    entries = parse_draft(draft)
    index, _ = load_index()
    from tradeschool.citations.lesson import scan_lesson

    lesson_sentences = {_normal(s.text) for s in sentences(text)}
    problems: list[str] = []
    seen: set[str] = set()
    for entry in entries:
        key = entry.key
        if key in seen:
            problems.append(f"{key}: twice in the draft")
        seen.add(key)
        if entry.kind == "skip":
            if (entry.heading, 1) not in sections:
                problems.append(f"{key}: heading not in the lesson")
            continue
        flat = _normal(entry.text)
        if "**" in entry.text:
            problems.append(f"{key}: bold")
        for filler in FILLERS:
            if filler in flat.lower():
                problems.append(f"{key}: filler «{filler}»")
        if "?" in flat or "¿" in flat:
            problems.append(f"{key}: rhetorical question")
        if entry.kind == "overview":
            n = words(flat)
            if not 120 <= n <= 200:
                problems.append(f"{key}: {n} words (120–200)")
            if "Lo que más cae" not in flat:
                problems.append(f"{key}: does not point at «Lo que más cae»")
            continue
        body = sections.get((entry.heading, entry.occurrence))
        if body is None:
            problems.append(f"{key}: heading not in the lesson")
            continue
        if entry.kind == "nc":
            bullets = [b[2:].strip() for b in entry.text.splitlines() if b.startswith("- ")]
            if len(bullets) < 2:
                problems.append(f"{key}: fewer than two bullets")
            problems += [f"{key}: bullet is not a sentence of the lesson: {b[:70]}…" for b in bullets if _normal(b) not in lesson_sentences]
            continue
        n = words(flat)
        if not flat.startswith(LEAD_IN + " "):
            problems.append(f"{key}: does not open with «{LEAD_IN}»")
        if not 40 <= n <= 90:
            problems.append(f"{key}: {n} words (40–90)")
        cited = [c for c in scan_lesson(lesson, flat, index).prose if c.norm is not None]
        if not cited:
            problems.append(f"{key}: no citation that resolves to a norm")
        literal = _normal(body).lower()
        for match in FIGURE.finditer(flat[len(LEAD_IN) :]):
            figure = match[1].lower()
            if figure in ("un", "una", "uno"):
                continue
            if not re.search(rf"\b{re.escape(figure)}\b", literal):
                problems.append(f"{key}: figure «{match[1]}» is not in the section's literal text")
        for sentence in re.split(r"(?<=[.!])\s+", flat):
            if sentence.startswith(SPLIT_OPENERS):
                problems.append(f"{key}: split-sentence opener «{sentence[:25]}…» (voice blacklist)")
    return problems


def _insert_after_heading(lines: list[str], index: int, paragraph: str) -> None:
    lines[index + 1 : index + 1] = ["", *paragraph.split("\n")]


def apply(lesson: str) -> list[str]:
    text = lesson_text(lesson)
    done: list[str] = []
    for entry in parse_draft(LAYER / lesson / "draft.md"):
        if entry.kind == "skip" or entry.key in dropped(lesson):
            continue
        text = text.rstrip("\n") + "\n"
        lines = text.split("\n")
        block = entry.text.strip()
        present = _normal("**No confundir.** " + block) if entry.kind == "nc" else _normal(block)
        if present in _normal(text):
            continue
        sections = section_bodies(lines)
        if entry.kind == "overview":
            _insert_after_heading(lines, 0, block)
        elif entry.kind == "after":
            at = next(i for i, h, n, _ in sections if (h, n) == (entry.heading, entry.occurrence))
            _insert_after_heading(lines, at, block)
        else:
            position = next(k for k, (_, h, n, _b) in enumerate(sections) if (h, n) == (entry.heading, entry.occurrence))
            end = sections[position + 1][0] if position + 1 < len(sections) else len(lines)
            while end > 0 and not lines[end - 1].strip():
                end -= 1
            note = [":::note{type=warning}", "**No confundir.**", "", *block.split("\n"), ":::"]
            lines[end:end] = ["", *note]
        text = "\n".join(lines)
        done.append(entry.key)
    (LESSONS / f"{lesson}.md").write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
    return done


def dropped(lesson: str) -> set[str]:
    path = LAYER / lesson / "dropped.txt"
    return set(path.read_text(encoding="utf-8").splitlines()) if path.exists() else set()


def drop(lesson: str, key: str) -> None:
    entry = next(e for e in parse_draft(LAYER / lesson / "draft.md") if e.key == key)
    text = lesson_text(lesson)
    pattern = re.compile(r"\n?" + re.escape(entry.text.strip()) + r"\n(?:\n)?")
    new = pattern.sub("\n" if entry.kind != "nc" else "", text, count=1)
    (LESSONS / f"{lesson}.md").write_text(re.sub(r"\n{3,}", "\n\n", new), encoding="utf-8")
    with (LAYER / lesson / "dropped.txt").open("a", encoding="utf-8") as handle:
        handle.write(key + "\n")


def replace(lesson: str, key: str, new_text: str) -> None:
    """Swap an inserted paragraph for a rewritten one, in the draft and in the lesson."""
    entry = next(e for e in parse_draft(LAYER / lesson / "draft.md") if e.key == key)
    for path in (LAYER / lesson / "draft.md", LESSONS / f"{lesson}.md"):
        text = path.read_text(encoding="utf-8")
        if entry.text.strip() not in text:
            raise SystemExit(f"{key}: old text not found in {path.name}")
        path.write_text(text.replace(entry.text.strip(), new_text.strip(), 1), encoding="utf-8")


def layer_words(lesson: str) -> int:
    text = lesson_text(lesson)
    return sum(words(e.text) for e in parse_draft(LAYER / lesson / "draft.md") if e.kind in ("overview", "after") and _normal(e.text) in _normal(text))


if __name__ == "__main__":
    command, lesson, *rest = sys.argv[1:]
    if command == "lint":
        for problem in lint(lesson):
            print(problem)
    elif command == "apply":
        print("\n".join(apply(lesson)))
    elif command == "drop":
        drop(lesson, rest[0])
    elif command == "replace":
        replace(lesson, rest[0], Path(rest[1]).read_text(encoding="utf-8"))
    elif command == "words":
        print(layer_words(lesson))
