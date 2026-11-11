# SPDX-License-Identifier: AGPL-3.0-only
"""Provenance of a course's lesson sentences against the courses it was derived from (R2.3, C2 and AEAT).

A sentence inherits a source course's verification when its text is identical, the citations that govern
it are the same, and every file they cite has the same sha256 in both snapshots. C2 inherits from C1; the
AEAT course from C1 or C2, and a C2 origin also needs its PASS in the C2 report the record names. Every other
sentence needs its own PASS in a verifier report. A lesson's record lists each sentence once.

Text identity is compared after joining the hard-wrapped lines of a block with single spaces: the wrap is
not part of the text a reader sees.
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass, field
from functools import cache, cached_property
from pathlib import Path

from tradeschool.citations.lesson import LessonCitation, LessonCitations, scan_lesson
from tradeschool.citations.norms import NormIndex
from tradeschool.content.registry import CourseRegistry

INHERITED = "verificado en C1"
INHERITED_C2 = "verificado en C2"
#: C2 module → folder of its provenance records under docs/age-verification/c2/.
BLOQUE_DIRS = {"m01": "bloque-i", "m02": "bloque-ii"}
VERIFIED = "verificado"

_HEADING = re.compile(r"^#{1,6}\s")
_FENCE = re.compile(r"^(```|~~~|:{2,})")
_LIST_ITEM = re.compile(r"^(?:[-*]|\d+\.)\s+")
_TABLE_SEPARATOR = re.compile(r"^\|?\s*:?-{3,}")
# A sentence ends at . ? ! (optionally closed by » ” or a parenthesis) followed by a capitalised start.
_SENTENCE_END = re.compile(r"(?<=[.?!])([»”)]*)\s+(?=[¿¡«(A-ZÁÉÍÓÚÑ])")
_ABBREVIATIONS = ("art.", "arts.", "núm.", "apdo.", "apdos.", "Sr.", "Sra.", "D.", "Dña.", "pág.", "págs.")


@dataclass(frozen=True)
class Sentence:
    text: str
    first_line: int
    last_line: int
    block: int
    kind: str  # paragraph, item, row

    @property
    def id(self) -> str:
        return sentence_id(self.text)


def sentence_id(text: str) -> str:
    return hashlib.sha1(text.encode()).hexdigest()[:10]


def _collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _split(text: str) -> list[str]:
    pieces: list[str] = []
    start = 0
    for match in _SENTENCE_END.finditer(text):
        head = text[start : match.start(1) if match.group(1) else match.start()]
        if head.split(" ")[-1] in _ABBREVIATIONS:
            continue
        end = match.end(1) if match.group(1) else match.start()
        pieces.append(text[start:end].strip())
        start = match.end()
    pieces.append(text[start:].strip())
    return [piece for piece in pieces if piece]


def _blocks(lines: list[str]) -> list[tuple[str, list[tuple[int, str]]]]:
    """(kind, [(line number, text)]) for each paragraph, list item and table row; headings, fences and the
    title are not text."""
    blocks: list[tuple[str, list[tuple[int, str]]]] = []
    current: list[tuple[int, str]] = []
    kind = ""
    in_code = False

    def flush() -> None:
        if current:
            blocks.append((kind, list(current)))
            current.clear()

    for number, raw in enumerate(lines, start=1):
        line = raw.rstrip()
        stripped = _collapse(line)
        if stripped.startswith(("```", "~~~")):
            in_code = not in_code
            flush()
            continue
        if in_code or not stripped or _HEADING.match(line) or _FENCE.match(stripped):
            flush()
            continue
        if stripped.startswith("|"):
            flush()
            if not _TABLE_SEPARATOR.match(stripped):
                blocks.append(("row", [(number, stripped)]))
            continue
        if _LIST_ITEM.match(stripped) and not line.startswith(" "):
            flush()
            kind = "item"
            current.append((number, _LIST_ITEM.sub("", stripped, count=1)))
            continue
        if not current:
            kind = "paragraph"
        current.append((number, stripped))
    flush()
    return blocks


def sentences(markdown: str) -> list[Sentence]:
    """The lesson's sentences in reading order: paragraphs and list items split at sentence ends, one per
    table row. Each sentence spans the source lines its text sits on."""
    found: list[Sentence] = []
    for block, (kind, lines) in enumerate(_blocks(markdown.splitlines())):
        text = " ".join(t for _, t in lines)
        starts: list[tuple[int, int]] = []
        offset = 0
        for number, line_text in lines:
            starts.append((offset, number))
            offset += len(line_text) + 1
        cursor = 0
        for part in [text] if kind == "row" else _split(text):
            begin = text.index(part, cursor)
            end = begin + len(part) - 1
            cursor = begin + len(part)
            first = max(n for o, n in starts if o <= begin)
            last = max(n for o, n in starts if o <= end)
            found.append(Sentence(part, first, last, block, kind))
    return found


CitationKey = tuple[str, str]


def _strip_ticks(text: str) -> str:
    return text.replace("`", "")


def _own_citations(sentence: Sentence, citations: Iterable[LessonCitation]) -> list[LessonCitation]:
    text = _strip_ticks(sentence.text)
    return [c for c in citations if sentence.first_line <= c.line <= sentence.last_line and c.text in text]


def governing(lesson: list[Sentence], citations: LessonCitations) -> dict[int, list[LessonCitation]]:
    """Per sentence index, the citations that govern it: its own; else the next cited sentence of its block,
    else the previous one; a list item or row without any takes the last citation of the paragraph before
    its list or table."""
    own = {i: _own_citations(s, citations.items) for i, s in enumerate(lesson)}
    result: dict[int, list[LessonCitation]] = {}
    for i, sentence in enumerate(lesson):
        if own[i]:
            result[i] = own[i]
            continue
        same_block = [j for j, s in enumerate(lesson) if s.block == sentence.block and own[j]]
        after = [j for j in same_block if j > i]
        before = [j for j in same_block if j < i]
        if after:
            result[i] = own[after[0]]
        elif before:
            result[i] = own[before[-1]]
        elif sentence.kind in ("item", "row"):
            result[i] = _lead_in(lesson, own, i)
        else:
            result[i] = []
    return result


def _lead_in(lesson: list[Sentence], own: Mapping[int, list[LessonCitation]], i: int) -> list[LessonCitation]:
    kind = lesson[i].kind
    j = i - 1
    while j >= 0 and lesson[j].kind == kind:
        j -= 1
    if j < 0 or lesson[j].kind != "paragraph":
        return []
    paragraph = [k for k in range(j + 1) if lesson[k].block == lesson[j].block and own[k]]
    return own[paragraph[-1]][-1:] if paragraph else []


def file_sha256(path: Path) -> str:
    stat = path.stat()
    return _sha256(path, stat.st_size, stat.st_mtime_ns)


@cache
def _sha256(path: Path, size: int, mtime_ns: int) -> str:
    # size and mtime are in the key so a file rewritten in place is hashed again
    return hashlib.sha256(path.read_bytes()).hexdigest()


def citation_keys(cited: list[LessonCitation], course_root: Path) -> frozenset[CitationKey] | None:
    """(citation text, sha256 of the cited file) per citation; None when one resolves to no file on disk."""
    keys: set[CitationKey] = set()
    for citation in cited:
        relative = citation.source_file or (citation.norm.file if citation.norm else None)
        if relative is None or not (course_root / relative).is_file():
            return None
        keys.add((citation.text, file_sha256(course_root / relative)))
    return frozenset(keys)


@dataclass(frozen=True)
class LessonText:
    lesson_id: str
    markdown: str
    citations: LessonCitations
    course_root: Path

    @cached_property
    def _keyed(self) -> list[tuple[Sentence, frozenset[CitationKey] | None]]:
        lesson = sentences(self.markdown)
        rule = governing(lesson, self.citations)
        return [(s, citation_keys(rule[i], self.course_root)) for i, s in enumerate(lesson)]

    def keyed(self) -> list[tuple[Sentence, frozenset[CitationKey] | None]]:
        return self._keyed


@dataclass(frozen=True)
class Origin:
    lesson_id: str
    first_line: int
    last_line: int


def find_origin(
    sentence: Sentence, keys: frozenset[CitationKey] | None, sources: Iterable[LessonText]
) -> Origin | None:
    """The source lesson sentence this one inherits from: same text, same governing citations, same files."""
    if keys is None:
        return None
    for source in sources:
        for candidate, candidate_keys in source.keyed():
            if candidate.text == sentence.text and candidate_keys == keys:
                return Origin(source.lesson_id, candidate.first_line, candidate.last_line)
    return None


# ----------------------------------------------------------------------------------------------- records

_ENTRY = re.compile(r"^- `(?P<id>[0-9a-f]{10})` · (?P<kind>verificado en C[12]|verificado): (?P<rest>.+)$")


@dataclass(frozen=True)
class Record:
    sentence_id: str
    inherited: bool
    report: str
    #: Inherited: the source lesson id. Verified: the verdict.
    detail: str
    text: str
    #: Inherited: the source course, «C1» or «C2». Verified: empty.
    origin: str = ""


def parse_record(text: str) -> list[Record]:
    records: list[Record] = []
    lines = text.splitlines()
    for number, line in enumerate(lines):
        match = _ENTRY.match(line)
        if match is None:
            continue
        quote = lines[number + 1] if number + 1 < len(lines) else ""
        if not quote.startswith("  > "):
            raise ValueError(f"record entry {match['id']} has no quoted sentence on the next line")
        fields = [part.strip() for part in match["rest"].split(" · ")]
        inherited = match["kind"] != VERIFIED
        origin = match["kind"][-2:] if inherited else ""
        if inherited:
            report, detail = fields[0], fields[1].removeprefix(f"{origin} ").split(" ")[0]
        else:
            detail, report = fields[0], fields[1]
        records.append(Record(match["id"], inherited, report, detail, quote[4:], origin))
    return records


_VERDICT_ROW = re.compile(r"^\|\s*`?(?P<id>[0-9a-f]{10}|g-[a-z0-9-]+)`?\s*\|\s*(?P<verdict>PASS|FAIL)\b")


def report_verdicts(report: Path) -> dict[str, str]:
    """Sentence id → verdict, as a verifier report's table rows give them."""
    verdicts: dict[str, str] = {}
    for line in report.read_text().splitlines():
        match = _VERDICT_ROW.match(line)
        if match:
            verdicts[match["id"]] = match["verdict"]
    return verdicts


@dataclass
class Audit:
    problems: list[str] = field(default_factory=list)
    inherited: int = 0
    verified: int = 0

    def fail(self, message: str) -> None:
        self.problems.append(message)


def audit_lesson(
    lesson: LessonText,
    records: list[Record],
    source_lesson: Callable[[str, str], LessonText | None],
    repo_root: Path,
) -> Audit:
    """Every sentence of the lesson carries exactly one record, and each record holds: an inherited sentence
    has a byte-identical counterpart with the same citations and file hashes (and, from C2, the C2 PASS); a
    verified one has a PASS."""
    audit = Audit()
    keyed = lesson.keyed()
    by_id: dict[str, list[tuple[Sentence, frozenset[CitationKey] | None]]] = {}
    for sentence, keys in keyed:
        by_id.setdefault(sentence.id, []).append((sentence, keys))
    seen: set[str] = set()
    for record in records:
        if record.sentence_id in seen:
            audit.fail(f"{lesson.lesson_id}: {record.sentence_id} has more than one record")
            continue
        seen.add(record.sentence_id)
        if sentence_id(record.text) != record.sentence_id:
            audit.fail(f"{lesson.lesson_id}: {record.sentence_id} quotes a different sentence")
            continue
        occurrences = by_id.get(record.sentence_id)
        if not occurrences:
            audit.fail(f"{lesson.lesson_id}: {record.sentence_id} is not a sentence of the lesson")
            continue
        if not (repo_root / record.report).exists():
            audit.fail(f"{lesson.lesson_id}: {record.sentence_id} names a missing report: {record.report}")
            continue
        if record.inherited:
            source = source_lesson(record.origin, record.detail)
            if source is None:
                audit.fail(
                    f"{lesson.lesson_id}: {record.sentence_id} names an unknown source lesson {record.detail}"
                )
                continue
            for sentence, keys in occurrences:
                if find_origin(sentence, keys, [source]) is None:
                    audit.fail(
                        f"{lesson.lesson_id}: {record.sentence_id} (line {sentence.first_line}) has no "
                        f"identical counterpart with the same citations and file hashes in {record.detail}"
                    )
                    break
            else:
                if record.origin == "C2" and (
                    report_verdicts(repo_root / record.report).get(record.sentence_id) != "PASS"
                ):
                    audit.fail(
                        f"{lesson.lesson_id}: {record.sentence_id} has no PASS for the C2 origin in "
                        f"{record.report}"
                    )
                    continue
                audit.inherited += 1
        else:
            verdict = report_verdicts(repo_root / record.report).get(record.sentence_id)
            if record.detail != "PASS" or verdict != "PASS":
                audit.fail(f"{lesson.lesson_id}: {record.sentence_id} has no PASS in {record.report}")
                continue
            audit.verified += 1
    for missing in sorted(set(by_id) - seen):
        line = by_id[missing][0][0].first_line
        audit.fail(f"{lesson.lesson_id}: sentence {missing} (line {line}) has no record")
    return audit


# ------------------------------------------------------------------------------------------- glossary

_GLOSSARY_ENTRY = re.compile(
    r"^- `(?P<id>g-[a-z0-9-]+)` · (?P<kind>verificado en C[12]|verificado): (?P<rest>.+)$"
)


@dataclass(frozen=True)
class GlossaryEntry:
    id: str
    #: The term and every definition text, in file order.
    texts: tuple[str, ...]
    keys: frozenset[CitationKey] | None

    @classmethod
    def of(cls, raw: Mapping[str, object], index: NormIndex, course_root: Path) -> GlossaryEntry:
        texts = [str(raw.get("es", ""))]
        senses = raw.get("senses")
        for holder in [raw, *(senses if isinstance(senses, list) else [])]:
            definition = holder.get("definition") if isinstance(holder, Mapping) else None
            if isinstance(definition, Mapping) and definition.get("es"):
                texts.append(_collapse(str(definition["es"])))
        cited = [c for text in texts[1:] for c in scan_lesson("glossary", text, index).items]
        return cls(str(raw["id"]), tuple(texts), citation_keys(cited, course_root))


def parse_glossary_record(text: str) -> list[Record]:
    records: list[Record] = []
    for line in text.splitlines():
        match = _GLOSSARY_ENTRY.match(line)
        if match is None:
            continue
        fields = [part.strip() for part in match["rest"].split(" · ")]
        inherited = match["kind"] != VERIFIED
        report, detail = (fields[0], fields[1]) if inherited else (fields[1], fields[0])
        records.append(
            Record(match["id"], inherited, report, detail, "", match["kind"][-2:] if inherited else "")
        )
    return records


def audit_glossary(
    entries: list[GlossaryEntry],
    sources: Mapping[str, Mapping[str, GlossaryEntry]],
    records: list[Record],
    repo_root: Path,
) -> Audit:
    """Each glossary entry carries one record: an inherited entry has the same term, definitions, citations
    and cited-file hashes as the entry of the same id in the course its record names; a verified one has a
    PASS row in its report."""
    audit = Audit()
    by_id = {record.sentence_id: record for record in records}
    for entry in entries:
        record = by_id.pop(entry.id, None)
        if record is None:
            audit.fail(f"glossary: {entry.id} has no record")
            continue
        if not (repo_root / record.report).exists():
            audit.fail(f"glossary: {entry.id} names a report that does not exist: {record.report}")
            continue
        if record.inherited:
            source = sources.get(record.origin, {}).get(entry.id)
            same = source is not None and entry.keys is not None
            if not same or source is None or (source.texts, source.keys) != (entry.texts, entry.keys):
                audit.fail(
                    f"glossary: {entry.id} differs from {record.origin} (text, citation or cited file)"
                )
                continue
            audit.inherited += 1
        else:
            if record.detail != "PASS" or report_verdicts(repo_root / record.report).get(entry.id) != "PASS":
                audit.fail(f"glossary: {entry.id} has no PASS in {record.report}")
                continue
            audit.verified += 1
    for stale in sorted(by_id):
        audit.fail(f"glossary: record {stale} names no entry")
    return audit


# ------------------------------------------------------------------------------------------------ CLI
# uv run python -m scripts.provenance plan|record <c2 lesson id> <c1 lesson id>...
# uv run python -m scripts.provenance --course aeat-agentes-hacienda plan|record <lesson> c1:<id> c2:<id>...

# Which C1 report verified a line, by the summary of the commit that last changed it (git blame). The R2
# per-sentence tables were not kept; the theory ledger is their record.
_C1_REPORTS = (
    ("currency audit (R2b part C", "docs/age-verification/audit-2026-11"),
    ("November currency audit follow-ups", "docs/age-verification/audit-2026-11/followup"),
    ("round R4 for supuestos", "docs/age-cases-ledger.md"),
    ("schemas", "docs/age-verification/{bloque}/esquemas"),
    ("AGE-C1: r2c", "docs/age-verification/{bloque}/esquemas"),
    ("AGE-C1: r2b fixes", "docs/age-theory-ledger.md"),
    ("AGE-C1: r2b", "docs/age-scope-audit.md"),
    ("AGE-C1:", "docs/age-theory-ledger.md"),
)
_C2_COMMIT = "Course age-auxiliar-c2"
# C1 sentences changed outside a C1 round, by sentence id: their report, whatever commit carries them.
_C1_SENTENCE_REPORTS = {
    "63c0778e88": "docs/age-verification/bloque-i/m01-l11-intro-2026-11-06.md",
}
_BLOQUE = {
    "m01": "bloque-i",
    "m02": "bloque-ii",
    "m03": "bloque-iii",
    "m04": "bloque-iv",
    "m05": "bloque-v",
    "m06": "bloque-vi",
}


def c1_report(repo: Path, file: Path, sentence: Sentence) -> tuple[str, str]:
    """(report path, commit) for the newest commit among a C1 sentence's lines; a sentence moved only by a
    neighbour's edit (uncommitted, or carried by a C2 commit) is looked up before that edit."""
    import subprocess

    def blame(first: int, last: int, *revision: str) -> tuple[str, str]:
        out = subprocess.run(
            ["git", "blame", "--line-porcelain", *revision, "-L", f"{first},{last}", "--", str(file)],
            cwd=repo,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        commits: dict[str, tuple[int, str]] = {}
        sha = ""
        for line in out.splitlines():
            if re.match(r"^[0-9a-f]{40} ", line):
                sha = line[:40]
            elif line.startswith("committer-time "):
                commits.setdefault(sha, (int(line.split()[1]), ""))
            elif line.startswith("summary "):
                commits[sha] = (commits[sha][0], line[8:])
        sha, (_, summary) = max(commits.items(), key=lambda item: item[1][0])
        return sha, summary

    def blame_before(revision: str) -> tuple[str, str]:
        text = subprocess.run(
            ["git", "show", f"{revision}:{file.relative_to(repo)}"],
            cwd=repo,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        before = next((s for s in sentences(text) if s.text == sentence.text), None)
        if before is None:
            raise LookupError(
                f"{file.stem}: «{sentence.text[:60]}» is new in C1; give it a _C1_SENTENCE_REPORTS entry"
            )
        return blame(before.first_line, before.last_line, revision)

    sha, summary = blame(sentence.first_line, sentence.last_line)
    if set(sha) == {"0"}:
        sha, summary = blame_before("HEAD")
    # A C2 commit carries C1 edits only as authorised single sentences (_C1_SENTENCE_REPORTS); their re-flowed
    # neighbours keep the report of the commit before it.
    while summary.startswith(_C2_COMMIT):
        sha, summary = blame_before(f"{sha}^")
    for marker, report in _C1_REPORTS:
        if marker in summary:
            return report.format(bloque=_BLOQUE[file.stem[:3]]), sha[:7]
    raise LookupError(f"no C1 report known for commit {sha[:7]} «{summary}»")


def _latest_verdicts(reports_dir: Path) -> dict[str, tuple[str, str]]:
    """Sentence id → (verdict, report path) over every verifier report; a report's re-checks win over it, the
    highest number last."""

    def order(report: Path) -> tuple[str, int]:
        base, _, number = report.stem.partition("-recheck-")
        return base, int(number) if number.isdigit() else 0

    verdicts: dict[str, tuple[str, str]] = {}
    for report in sorted(reports_dir.glob("*.md"), key=order):
        for sid, verdict in report_verdicts(report).items():
            verdicts[sid] = (verdict, str(report.relative_to(reports_dir.parents[4])))
    return verdicts


def _c2_record(repo: Path, lesson_id: str, sid: str) -> Record | None:
    path = repo / "docs" / "age-verification" / "c2" / BLOQUE_DIRS[lesson_id[:3]] / f"{lesson_id}.md"
    return (
        next((r for r in parse_record(path.read_text()) if r.sentence_id == sid), None)
        if path.exists()
        else None
    )


def main(argv: list[str]) -> int:
    import sys

    from tests.pipeline_courses import REPO_CONTENT, course_dir, pipeline_courses

    target_slug = "age-auxiliar-c2"
    if argv[0] == "--course":
        target_slug, argv = argv[1], argv[2:]
    command, lesson_id, *source_ids = argv
    repo = REPO_CONTENT.parent
    aeat = target_slug == "aeat-agentes-hacienda"
    verification = repo / "docs" / "age-verification"
    out = verification / "aeat" / "r2" if aeat else verification / "c2" / BLOQUE_DIRS[lesson_id[:3]]
    courses = {c.slug: c for c in pipeline_courses()}
    target, c1, c2 = courses[target_slug], courses["age-administrativo-c1"], courses["age-auxiliar-c2"]

    def text_of(course: CourseRegistry, lid: str) -> LessonText:
        root = course_dir(course)
        path = root / "es" / "lessons" / f"{lid}.md"
        citations = course.citations.lesson(lid, "es")
        if citations is None:
            raise LookupError(f"{course.slug} has no lesson {lid}")
        return LessonText(lid, path.read_text(), citations, root)

    tagged = [s.split(":", 1) if ":" in s else ["c1", s] for s in source_ids]
    c1_sources = [text_of(c1, lid) for tag, lid in tagged if tag == "c1"]
    c2_sources = [text_of(c2, lid) for tag, lid in tagged if tag == "c2"]
    lesson = text_of(target, lesson_id)

    def from_c1(sentence: Sentence, origin: Origin) -> str:
        c1_file = course_dir(c1) / "es" / "lessons" / f"{origin.lesson_id}.md"
        if sentence.id in _C1_SENTENCE_REPORTS:
            report, sha = _C1_SENTENCE_REPORTS[sentence.id], "override"
        else:
            report, sha = c1_report(
                repo, c1_file, Sentence(sentence.text, origin.first_line, origin.last_line, 0, "")
            )
        where = f"C1 {origin.lesson_id} l.{origin.first_line}"
        return f"- `{sentence.id}` · {INHERITED}: {report} · {where} · {sha}"

    def from_c2(sentence: Sentence, keys: frozenset[CitationKey] | None) -> str | None:
        origin = find_origin(sentence, keys, c2_sources)
        if origin is None:
            return None
        record = _c2_record(repo, origin.lesson_id, sentence.id)
        if record is None:
            return None
        if record.inherited:
            c1_origin = find_origin(sentence, keys, [text_of(c1, record.detail)])
            return from_c1(sentence, c1_origin) if c1_origin else None
        if record.detail != "PASS":
            return None
        where = f"C2 {origin.lesson_id} l.{origin.first_line}"
        return f"- `{sentence.id}` · {INHERITED_C2}: {record.report} · {where}"

    verdicts = _latest_verdicts(out / "verify")
    entries: list[str] = []
    pending: list[str] = []
    seen: set[str] = set()
    inherited = verified = 0
    for sentence, keys in lesson.keyed():
        if sentence.id in seen:
            continue
        seen.add(sentence.id)
        c1_origin = find_origin(sentence, keys, c1_sources)
        entry = from_c1(sentence, c1_origin) if c1_origin is not None else from_c2(sentence, keys)
        if entry is not None:
            entries.append(entry)
            inherited += 1
        elif verdicts.get(sentence.id, ("", ""))[0] == "PASS":
            entries.append(f"- `{sentence.id}` · {VERIFIED}: PASS · {verdicts[sentence.id][1]}")
            verified += 1
        else:
            cited = (
                ", ".join(sorted({t for t, _ in keys}))
                if keys
                else ("—" if keys is not None else "sin fichero")
            )
            pending.append(
                f"| `{sentence.id}` | {sentence.first_line} | {sentence.text.replace('|', '\\|')} | {cited} |"
            )
            continue
        entries.append(f"  > {sentence.text}")
    if command == "plan":
        (out / "pending").mkdir(parents=True, exist_ok=True)
        header = "| id | line | sentence | governing citations |\n|---|---|---|---|\n"
        (out / "pending" / f"{lesson_id}.md").write_text(
            f"# Pending sentences — `{lesson_id}`\n\n{len(pending)} to verify; {inherited} inherited "
            f"({', '.join(source_ids)}); {verified} already PASS.\n\n" + header + "\n".join(pending) + "\n"
        )
        print(
            f"{lesson_id}: {inherited} inherited, {verified} verified, {len(pending)} pending",
            file=sys.stderr,
        )
        return 0
    if pending:
        print(f"{lesson_id}: {len(pending)} sentences have neither provenance nor a PASS", file=sys.stderr)
        return 1
    kinds = f"«{INHERITED}» o «{INHERITED_C2}»" if aeat else f"«{INHERITED}»"
    origin_note = "idéntica a C1 o a C2" if aeat else "idéntica a C1"
    (out / f"{lesson_id}.md").write_text(
        f"# Registro de procedencia — `{lesson_id}`\n\nR2.3: cada frase lleva {kinds}: <informe> "
        f"({origin_note}, misma cita, mismo sha256) o «{VERIFIED}: PASS · <informe>». Generado por "
        f"`backend/scripts/provenance.py`; lo comprueba `backend/tests/test_provenance.py`.\n\n"
        f"Frases: {inherited + verified} · heredadas: {inherited} · verificadas: {verified}.\n\n"
        + "\n".join(entries)
        + "\n"
    )
    print(f"{lesson_id}: record written ({inherited} inherited, {verified} verified)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    import sys

    raise SystemExit(main(sys.argv[1:]))
