# SPDX-License-Identifier: AGPL-3.0-only
"""Mechanical checks of question candidates (docs/backend-question-style.md sections 1 and 7).

uv run python -m scripts.tech_course.lint_questions [--exclude-failed] [--lesson ID | --module mNN | FILE ...]

One tab-separated failure per line, a `key-longest` line per lesson; exit 1 on a failure.
With `--exclude-failed`, questions that failed verification (`<lesson>.verdicts.tsv`) are not linted.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from scripts.tech_course.candidates import (
    S2_DIR,
    Candidate,
    add_selection_arguments,
    lesson_of,
    read_candidates,
    select_files,
)
from scripts.tech_course.lessons import add_course_argument, course_dir
from tradeschool.citations.tech import TechSourceIndex, parse_ref

STEM_WORDS = (15, 40)
KEY_LONGEST_LIMIT = 0.40
ACCEPTED_FILE = S2_DIR / "lint-accepted.tsv"
MIN_CONTENT_WORD = 4
PREFIX = 5

#: Proper nouns and brand names that look like identifiers but are ordinary prose.
PROSE_NAMES = frozenset(
    {
        "PostgreSQL",
        "JavaScript",
        "TypeScript",
        "GitHub",
        "GitLab",
        "OpenAPI",
        "OAuth",
        "GraphQL",
        "MySQL",
        "IntelliJ",
        "JUnit",
        "YouTube",
        "LinkedIn",
        "PgBouncer",
        "HikariCP",
        "OpenTelemetry",
        "OpenFeature",
        "OpenID",
        "OpenGitOps",
        "OpenAI",
        "RabbitMQ",
        "MongoDB",
        "DynamoDB",
        "BigQuery",
        "InfluxDB",
        "ClickHouse",
        "CockroachDB",
        "ElasticSearch",
        "ZooKeeper",
        "GraalVM",
        "SonarQube",
        "WireMock",
        "ArchUnit",
        "MockK",
        "AssertJ",
        "NoSQL",
        "DevOps",
        "GitOps",
        "WebSocket",
        "WebSockets",
        "WebFlux",
        "PagerDuty",
        "MapStruct",
        "ShedLock",
        "CycloneDX",
        "SpringBoot",
        "VMware",
        "FreeBSD",
        "NetBSD",
        "OpenBSD",
        "OpenSSL",
        "OpenSSH",
        "OpenJDK",
        "AsyncAPI",
        "SpiceDB",
        "DuckDB",
        "SQLite",
        "MariaDB",
        "TimescaleDB",
        "PostGIS",
        "OpenShift",
        "ArgoCD",
        "TestContainers",
        "iOS",
        "macOS",
        "iPhone",
        "gRPC",
        "mTLS",
        "eBPF",
        "tRPC",
        "jOOQ",
        "eBay",
        "Node.js",
        "Vue.js",
        "Next.js",
        "React.js",
        "Spring.io",
        "ASP.NET",
        "Kotlin.js",
        "e.g",
        "i.e",
        "etc",
        "vs",
        "IPsec",
        "OpenMetrics",
        "SIRead",
        "GiST",
        "HashiCorp",
        "SpringDoc",
        "DockerHub",
        "FluentBit",
        "InfoQ",
        "StackOverflow",
        "ThoughtWorks",
        "PostgREST",
        "OpenSearch",
    }
)

_FENCE = re.compile(r"```.*?```", re.DOTALL)
_INLINE = re.compile(r"`[^`\n]*`")
_SQL = re.compile(
    r"\b(?:SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|VACUUM|ANALYZE|EXPLAIN|WHERE|JOIN|GROUP BY|ORDER BY"
    r"|COMMIT|ROLLBACK|BEGIN|LOCK)\b"
)
_CODE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("annotation", re.compile(r"(?<![\w.])@[A-Za-z]\w*")),
    ("call", re.compile(r"\b\w+\(\)")),
    ("camelCase", re.compile(r"\b[a-z]+(?:[A-Z][a-z0-9]*)+\b")),
    ("PascalCase", re.compile(r"\b[A-Z][a-z][a-z0-9]*(?:[A-Z][a-z0-9]*)+\b|\b[A-Z]{2,}[a-z]{3,}\w*")),
    (
        "file",
        re.compile(
            r"\b[\w-]+\.(?:java|kt|kts|py|js|ts|tsx|xml|yml|yaml|json|sql|properties|gradle|toml|sh|conf)\b"
        ),
    ),
    ("dotted", re.compile(r"\b[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)+")),
    ("snake_case", re.compile(r"\b[A-Za-z]+(?:_[A-Za-z0-9]+)+\b")),
    ("flag", re.compile(r"(?<![\w-])--[a-z][\w-]*")),
    ("jvm-option", re.compile(r"(?<![\w-])-X[A-Za-z:]\w*")),
)

_STOP_WORDS = frozenset(
    (
        "about",
        "above",
        "after",
        "again",
        "against",
        "also",
        "because",
        "been",
        "before",
        "being",
        "below",
        "between",
        "both",
        "cannot",
        "could",
        "does",
        "doing",
        "down",
        "during",
        "each",
        "either",
        "else",
        "even",
        "ever",
        "from",
        "further",
        "have",
        "having",
        "here",
        "hers",
        "herself",
        "himself",
        "into",
        "itself",
        "just",
        "less",
        "like",
        "made",
        "make",
        "many",
        "might",
        "more",
        "most",
        "much",
        "must",
        "never",
        "none",
        "once",
        "only",
        "other",
        "ours",
        "ourselves",
        "over",
        "same",
        "should",
        "since",
        "some",
        "such",
        "than",
        "that",
        "their",
        "theirs",
        "them",
        "themselves",
        "then",
        "there",
        "these",
        "they",
        "this",
        "those",
        "through",
        "under",
        "until",
        "upon",
        "very",
        "want",
        "were",
        "what",
        "when",
        "where",
        "whether",
        "which",
        "while",
        "whom",
        "will",
        "with",
        "within",
        "without",
        "would",
        "your",
        "yours",
        "yourself",
    )
)
_LETTER_REFERENCE = re.compile(
    r"\b(?i:options?|answers?|choices?|distractors?)\s+\(?[A-D1-4]\)?(?!\w)"
    r"|\([a-dA-D]\)"
    r"|\b(?i:first|second|third|fourth|last)\s+(?i:option|answer|choice|distractor)\b"
)
_DENIAL = re.compile(
    r"\bnothing (?:in|says|indicates|suggests|mentions|states)\b"
    r"|\b(?:is|are) not (?:stated|described|mentioned|specified|documented|what is described)\b"
    r"|\bno \w+(?: \w+)? (?:is|are) (?:described|stated|mentioned)\b"
    r"|\b(?:documentation|guide|source|text|docs?|manual|section|page|description) "
    r"(?:does|do) not (?:say|state|mention|describe)\b"
    r"|\b(?:describes|states|mentions|says|gives) no\b"
    r"|\bnot what (?:the \w+ )?(?:describes|says|states)\b"
    r"|\b(?:no requirement|does not require|not (?:limited|restricted|applied|stated))\b"
    r"|\b(?:javadoc|documentation|guide|anchor|reference|source) "
    r"(?:gives|lists|names|describes) (?:no|nothing)\b"
    r"|^(?:It|This|That) is not (?:the|a|an) [^,;]{0,60}\.?$",
    re.IGNORECASE,
)
_DISMISSES_TOGETHER = re.compile(
    r"\bcontradicts? (?:that|this)\b|\b(?:same|one) (?:statement|sentence|fact)\b"
    r"|\b(?:both|all|each|neither) (?:are |is )?(?:wrong|ruled out|false|contradicted|incorrect)\b",
    re.IGNORECASE,
)
_REFUTATION_WORDS = (
    "wrong claim because correct incorrect answer option statement false true instead rather ruled"
)
_SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z`\"'(])")
_WORD = re.compile(r"[a-z0-9]+")


@dataclass(frozen=True)
class Failure:
    subject: str
    rule: str
    detail: str

    def line(self) -> str:
        return f"{self.subject}\t{self.rule}\t{self.detail}"


def prose_of(text: str) -> str:
    return _INLINE.sub(" ", _FENCE.sub(" ", text))


def stem_words(stem: str) -> int:
    return len(_FENCE.sub(" ", stem).split())


def code_tokens(text: str) -> list[str]:
    """Identifiers, SQL, flags and files left outside code formatting in `text`."""
    prose = prose_of(text)
    found = [m.group(0) for m in _SQL.finditer(prose)]
    for _, pattern in _CODE_PATTERNS:
        found += [m.group(0) for m in pattern.finditer(prose)]
    return sorted({token for token in found if token not in PROSE_NAMES})


# --- per-question rules ------------------------------------------------------------------------------------


def stem_length_failures(q: Candidate) -> list[Failure]:
    words = stem_words(q.stem)
    low, high = STEM_WORDS
    if low <= words <= high:
        return []
    return [Failure(q.id, "stem-length", f"{words} words, allowed {low} to {high}")]


def code_format_failures(q: Candidate) -> list[Failure]:
    fields = [("stem", q.stem), ("key", q.key)]
    fields += [(f"distractor {n}", d) for n, d in enumerate(q.distractors, 1)]
    fields.append(("explanation", q.explanation))
    return [
        Failure(q.id, "code-format", f"{where}: {', '.join(tokens)}")
        for where, text in fields
        if (tokens := code_tokens(text))
    ]


def _stem(word: str) -> str:
    for suffix in ("ing", "ed", "es", "s", "e", "ly"):
        if word.endswith(suffix) and len(word) - len(suffix) >= MIN_CONTENT_WORD - 1:
            stem = word[: -len(suffix)]
            return stem[:-1] if len(stem) > MIN_CONTENT_WORD and stem[-1] == stem[-2] else stem
    return word


def content_stems(text: str) -> frozenset[str]:
    words = _WORD.findall(text.lower())
    kept = (w for w in words if (len(w) >= MIN_CONTENT_WORD or w.isdigit()) and w not in _STOP_WORDS)
    return frozenset(_stem(w) for w in kept)


def _same_stem(left: str, right: str) -> bool:
    return left == right or (
        min(len(left), len(right)) >= MIN_CONTENT_WORD and left[:PREFIX] == right[:PREFIX]
    )


def _share_stem(left: frozenset[str], right: frozenset[str]) -> bool:
    return any(_same_stem(a, b) for a in left for b in right)


def _squash(text: str) -> str:
    return " ".join(text.lower().split())


def _spans(text: str) -> list[str]:
    return [_squash(span.strip("`")) for span in _INLINE.findall(text) if span.strip("`").strip()]


def _names_distractor(distractor: str, key: str, sentence: str) -> bool:
    """A sentence names a distractor by its text, a code span of it, or a stem that the key does not share."""
    squashed = _squash(sentence)
    if _squash(distractor) in squashed or any(span in squashed for span in _spans(distractor)):
        return True
    wanted = content_stems(distractor)
    distinctive = wanted
    return _share_stem(distinctive, content_stems(sentence))


def _novel_stems(sentence: str, key: str, distractor: str) -> list[str]:
    known = content_stems(key) | content_stems(distractor) | content_stems(_REFUTATION_WORDS)
    return [w for w in content_stems(sentence) if not any(_same_stem(w, k) for k in known)]


def explanation_failures(q: Candidate) -> list[Failure]:
    sentences = _SENTENCE_END.split(q.explanation.strip())
    failures: list[Failure] = []
    by_sentence: dict[int, list[int]] = {}
    for number, distractor in enumerate(q.distractors, 1):
        hits = [i for i, sentence in enumerate(sentences) if _names_distractor(distractor, q.key, sentence)]
        if not hits:
            failures.append(Failure(q.id, "explanation-coverage", f"distractor {number} is not addressed"))
        elif all(not _novel_stems(sentences[i], q.key, distractor) for i in hits):
            failures.append(Failure(q.id, "explanation-coverage", f"distractor {number} only restates key"))
        for index in hits:
            by_sentence.setdefault(index, []).append(number)
    for index, sentence in enumerate(sentences):
        if _DENIAL.search(sentence):
            failures.append(Failure(q.id, "explanation-coverage", f"silence or bare denial: {sentence[:60]}"))
        numbers = by_sentence.get(index, [])
        if len(numbers) > 1 and _DISMISSES_TOGETHER.search(sentence):
            which = " and ".join(map(str, numbers))
            failures.append(Failure(q.id, "explanation-shared-sentence", f"distractors {which}"))
    if _LETTER_REFERENCE.search(q.explanation):
        failures.append(Failure(q.id, "explanation-letter", "the explanation names an option by letter"))
    return failures


def citation_failures(q: Candidate) -> list[Failure]:
    pieces = [piece.strip() for piece in q.citation.split(";")]
    if not q.citation.strip():
        return [Failure(q.id, "citation", "missing")]
    bad = [piece for piece in pieces if parse_ref(piece) is None]
    return [Failure(q.id, "citation", f"not source_id#anchor: {piece!r}") for piece in bad]


def extract_failures(q: Candidate, extract_allowed: dict[str, bool]) -> list[Failure]:
    if not q.has_extract:
        return [Failure(q.id, "extract", "field absent (null is allowed)")]
    first = parse_ref(q.citation.split(";")[0])
    if first is None or first.source_id not in extract_allowed:
        return []
    if extract_allowed[first.source_id]:
        empty = not (q.extract and q.extract.strip())
        return [Failure(q.id, "extract-warning", f"{first.source_id} allows extracts; null")] if empty else []
    if q.extract is None:
        return []
    return [Failure(q.id, "extract", f"{first.source_id} does not allow extracts; must be null")]


def key_failures(q: Candidate) -> list[Failure]:
    failures: list[Failure] = []
    if not q.key.strip() and q.snippet is None:
        failures.append(Failure(q.id, "key-empty", "no key and no snippet"))
    squashed = [" ".join(d.split()) for d in q.distractors]
    key = " ".join(q.key.split())
    if key and key in squashed:
        failures.append(Failure(q.id, "distractor-equals-key", "a distractor equals the key"))
    if len(set(squashed)) != len(squashed):
        failures.append(Failure(q.id, "distractor-equals-key", "duplicate distractors"))
    return failures


def question_failures(q: Candidate, extract_allowed: dict[str, bool]) -> list[Failure]:
    return [
        *stem_length_failures(q),
        *code_format_failures(q),
        *explanation_failures(q),
        *citation_failures(q),
        *extract_failures(q, extract_allowed),
        *key_failures(q),
    ]


# --- per-lesson rule ---------------------------------------------------------------------------------------


def key_is_longest(q: Candidate) -> bool:
    return bool(q.key.strip()) and all(len(q.key) > len(d) for d in q.distractors)


def key_longest_share(questions: list[Candidate]) -> tuple[int, int]:
    keyed = [q for q in questions if q.key.strip()]
    return sum(key_is_longest(q) for q in keyed), len(keyed)


def failed_ids(verdicts: Path) -> frozenset[str]:
    if not verdicts.is_file():
        return frozenset()
    final: dict[str, str] = {}
    for line in verdicts.read_text(encoding="utf-8").splitlines():
        row = [cell.strip() for cell in line.split("\t")]
        # a `recheck` line, written after a re-verification, replaces the first verdict
        verdict = row[2] if len(row) > 2 and row[1] == "recheck" else row[1] if len(row) > 1 else ""
        if verdict in ("pass", "fail"):
            final[row[0]] = verdict
    return frozenset(qid for qid, verdict in final.items() if verdict == "fail")


@dataclass(frozen=True)
class LessonLint:
    failures: list[Failure]
    warnings: list[Failure]
    accepted: int
    report: str
    over: bool


def accepted_hits(path: Path = ACCEPTED_FILE) -> frozenset[tuple[str, str]]:
    """The `(question, rule)` pairs of `lint-accepted.tsv`: hits on passed questions that stay as they are."""
    if not path.is_file():
        return frozenset()
    rows = (line.split("\t") for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
    return frozenset((row[0], row[1]) for row in rows if len(row) >= 2 and not row[0].startswith("#"))


def lint_lesson(
    lesson: str,
    questions: list[Candidate],
    extract_allowed: dict[str, bool],
    accepted: frozenset[tuple[str, str]] = frozenset(),
) -> LessonLint:
    found = [f for q in questions for f in question_failures(q, extract_allowed)]
    honoured = [f for f in found if (f.subject, f.rule) in accepted]
    open_hits = [f for f in found if f not in honoured]
    failures = [f for f in open_hits if not f.rule.endswith("-warning")]
    warnings = [f for f in open_hits if f.rule.endswith("-warning")]
    longest, total = key_longest_share(questions)
    share = longest / total if total else 0.0
    over = share > KEY_LONGEST_LIMIT
    if over:
        failures.append(Failure(lesson, "key-longest-share", f"{share:.0%} of keys are the longest option"))
    return LessonLint(
        failures, warnings, len(honoured), f"{lesson}\tkey-longest\t{longest}/{total}\t{share:.0%}", over
    )


def _extract_policy(course: str) -> dict[str, bool]:
    index = TechSourceIndex.load(course_dir(course))
    if index is None:
        raise SystemExit(f"{course} has no sources/sources.yaml")
    return {sid: source.extract_allowed for sid, source in index.sources.items()}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_course_argument(parser)
    add_selection_arguments(parser)
    parser.add_argument("--exclude-failed", action="store_true", help="skip questions with a fail verdict")
    args = parser.parse_args(argv)
    policy = _extract_policy(args.course)
    accepted = accepted_hits()
    questions_seen = failures_seen = lessons_over = accepted_seen = 0
    for path in select_files(args.lesson, args.module, args.paths):
        lesson = lesson_of(path)
        skipped = failed_ids(path.with_name(f"{lesson}.verdicts.tsv")) if args.exclude_failed else frozenset()
        questions = [q for q in read_candidates(path) if q.id not in skipped]
        result = lint_lesson(lesson, questions, policy, accepted)
        for line in [*(f.line() for f in result.failures), *(f"warn {w.line()}" for w in result.warnings)]:
            print(line)
        print(result.report)
        questions_seen += len(questions)
        failures_seen += len(result.failures)
        lessons_over += result.over
        accepted_seen += result.accepted
    print(
        f"# questions {questions_seen}, failures {failures_seen}, lessons over 40 %: {lessons_over}, "
        f"accepted {accepted_seen}"
    )
    return 1 if failures_seen else 0


if __name__ == "__main__":
    sys.exit(main())
