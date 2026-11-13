# SPDX-License-Identifier: AGPL-3.0-only
"""The mechanical question lint and the key filler of the backend-in-depth course (style guide 1, 3, 7)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from scripts.tech_course import fill_keys, lint_questions
from scripts.tech_course.candidates import Candidate, candidate_of, select_files
from scripts.tech_course.lint_questions import (
    citation_failures,
    code_format_failures,
    code_tokens,
    explanation_failures,
    extract_failures,
    failed_ids,
    key_failures,
    key_longest_share,
    lint_lesson,
    stem_length_failures,
)

STEM = "In PostgreSQL 18, which statement about the lock a plain `CREATE INDEX` takes on a table is correct?"
EXPLANATION = (
    "Writers block while readers continue. Readers block as well is wrong because reads continue. "
    "No lock is taken is wrong because a lock is taken. The lock lasts one second is wrong because "
    "it lasts until the build ends."
)


def make(**overrides: object) -> Candidate:
    raw: dict[str, object] = {
        "id": "m00-l00-q01",
        "stem": STEM,
        "key": "Writers block while readers continue",
        "distractors": ["Readers block as well", "No lock is taken", "The lock lasts one second"],
        "explanation": EXPLANATION,
        "citation": "pg-sql-createindex#SQL-CREATEINDEX",
        "extract": None,
        "snippet": None,
    }
    return candidate_of({**raw, **overrides})


def rules(failures: list[lint_questions.Failure]) -> list[str]:
    return [f.rule for f in failures]


# --- stem length -------------------------------------------------------------------------------------------


def test_stem_under_fifteen_words_fails() -> None:
    assert rules(stem_length_failures(make(stem="Which lock does `VACUUM` take?"))) == ["stem-length"]


def test_stem_over_forty_words_fails() -> None:
    assert rules(stem_length_failures(make(stem=" ".join(["word"] * 41)))) == ["stem-length"]


def test_fenced_block_in_stem_does_not_count_words() -> None:
    code = "int a = 1; " * 30
    question = "What does this snippet print when it runs on Java 25 with the default settings?"
    stem = f"{question}\n```java\n{code}\n```"
    assert stem_length_failures(make(stem=stem)) == []


def test_stem_of_fifteen_words_passes() -> None:
    assert stem_length_failures(make(stem=" ".join(["word"] * 15))) == []


# --- code format -------------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    "text",
    [
        "Run VACUUM on the table",
        "the SELECT statement waits",
        "Use @Transactional on the service",
        "call commit() before returning",
        "a ConcurrentHashMap is used",
        "the maxPoolSize setting",
        "see java.util.List for details",
        "set spring.datasource.url first",
        "raise max_connections to 200",
        "pass --release 25 to the compiler",
        "set -Xmx512m for the heap",
        "edit application.yml by hand",
        "ORDER BY puts rows in order",
    ],
)
def test_code_outside_backticks_is_flagged(text: str) -> None:
    assert code_tokens(text)


@pytest.mark.parametrize(
    "text",
    [
        "In Java 25 the JVM starts faster",
        "PostgreSQL 18 supports it over HTTP and TLS",
        "The API returns JSON for the REST client and the CPU after a GC pause",
        "Use OpenTelemetry with HikariCP and PgBouncer, e.g. in GitHub Actions",
        "OAuth and GraphQL are used in JavaScript and TypeScript",
        "It reads READ COMMITTED data under SERIALIZABLE isolation",
        "The APIs and CPUs of the VMs are listed.",
        "Run `VACUUM` and `@Transactional` and `max_connections` and `HashMap`",
        "```sql\nSELECT 1;\n```",
        "Version 2.5 of the plan costs 3.1 units.",
    ],
)
def test_prose_and_formatted_code_are_not_flagged(text: str) -> None:
    assert code_tokens(text) == []


def test_code_format_names_the_field_with_the_stray_token() -> None:
    failures = code_format_failures(make(explanation="Writers block while a VACUUM runs."))
    assert [f.detail for f in failures] == ["explanation: VACUUM"]


# --- explanation coverage ----------------------------------------------------------------------------------


def test_explanation_naming_every_distractor_passes() -> None:
    assert explanation_failures(make()) == []


def test_unaddressed_distractor_fails() -> None:
    q = make(explanation="Writers wait for the build. Nothing else matters here.")
    assert rules(explanation_failures(q)).count("explanation-coverage") == 3


def test_distractor_matched_by_half_its_content_words_passes() -> None:
    q = make(
        distractors=[
            "Autovacuum rewrites every table nightly",
            "No lock is taken",
            "The lock lasts one second",
        ],
        explanation="Writers block while readers continue. Nightly rewrites never happen because autovacuum "
        "reclaims space only. No lock is taken is wrong. The lock lasts one second is wrong.",
    )
    assert explanation_failures(q) == []


def test_distractor_with_inline_code_spans_in_the_explanation_passes() -> None:
    q = make(
        distractors=["It runs `ANALYZE` first", "No lock is taken", "The lock lasts one second"],
        explanation="Writers block while readers continue. Statistics come from `ANALYZE` later. "
        "No lock is taken is wrong. The lock lasts one second is wrong.",
    )
    assert explanation_failures(q) == []


def test_two_distractors_ruled_out_by_one_sentence_fail() -> None:
    q = make(
        key="Writers wait until the index build ends",
        explanation="Writers wait until the index build ends. Readers block as well and no lock is taken, "
        "both wrong. It lasts one second is wrong because the build ends later.",
    )
    assert "explanation-shared-sentence" in rules(explanation_failures(q))


@pytest.mark.parametrize(
    "text", ["Option A is wrong.", "The first option is wrong.", "Answer C is wrong.", "Wrong (b) here."]
)
def test_explanation_naming_options_by_letter_fails(text: str) -> None:
    assert "explanation-letter" in rules(explanation_failures(make(explanation=f"{EXPLANATION} {text}")))


def test_answer_as_article_is_not_a_letter_reference() -> None:
    q = make(explanation=f"{EXPLANATION} The answer a reader expects is wrong.")
    assert "explanation-letter" not in rules(explanation_failures(q))


# --- citation, extract, key --------------------------------------------------------------------------------


def test_missing_citation_fails() -> None:
    assert rules(citation_failures(make(citation=""))) == ["citation"]


def test_citation_without_anchor_fails() -> None:
    assert rules(citation_failures(make(citation="pg-sql-createindex"))) == ["citation"]


def test_several_citations_joined_by_semicolons_pass() -> None:
    assert citation_failures(make(citation="a-src#one; b-src#two")) == []


def test_absent_extract_field_fails_but_null_passes() -> None:
    raw: dict[str, object] = {"id": "x", "citation": "a-src#one"}
    assert rules(extract_failures(candidate_of(raw), {"a-src": False})) == ["extract"]
    assert extract_failures(candidate_of({**raw, "extract": None}), {"a-src": False}) == []


def test_null_extract_on_a_source_that_allows_extracts_is_only_a_warning() -> None:
    q = make(citation="a-src#one", extract=None)
    assert rules(extract_failures(q, {"a-src": True})) == ["extract-warning"]
    result = lint_lesson("m00-l00", [make(citation="a-src#one", stem=" ".join(["w"] * 20))], {"a-src": True})
    assert [w.rule for w in result.warnings] == ["extract-warning"]
    assert "extract-warning" not in rules(result.failures)


def test_accepted_hit_is_skipped_for_that_question_and_rule_and_counted(tmp_path: Path) -> None:
    file = tmp_path / "lint-accepted.tsv"
    file.write_text("m00-l00-q01\tstem-length\tpassed blind verification\n", encoding="utf-8")
    short = make(stem="Too short a stem?")
    policy = {"pg-sql-createindex": False}
    assert "stem-length" in rules(lint_lesson("m00-l00", [short], policy).failures)
    result = lint_lesson("m00-l00", [short], policy, lint_questions.accepted_hits(file))
    assert "stem-length" not in rules(result.failures)
    assert result.accepted == 1
    assert extract_failures(make(citation="a-src#one", extract="A sentence."), {"a-src": True}) == []


def test_extract_forbidden_when_source_does_not_allow_it() -> None:
    q = make(citation="a-src#one", extract="A sentence.")
    assert rules(extract_failures(q, {"a-src": False})) == ["extract"]


def test_empty_key_without_snippet_fails_but_with_snippet_passes() -> None:
    assert rules(key_failures(make(key=""))) == ["key-empty"]
    assert key_failures(make(key="", snippet="m06-l02/Lock.java")) == []


def test_distractor_equal_to_key_after_whitespace_normalisation_fails() -> None:
    q = make(distractors=["Writers  block while readers\ncontinue", "b", "c"])
    assert rules(key_failures(q)) == ["distractor-equals-key"]


def test_duplicate_distractors_fail() -> None:
    assert rules(key_failures(make(distractors=["same", "same", "other"]))) == ["distractor-equals-key"]


# --- key-longest share -------------------------------------------------------------------------------------


def test_tied_key_is_not_longest_and_empty_keys_are_skipped() -> None:
    questions = [
        make(key="longest key here", distractors=["short", "tiny", "wee"]),
        make(key="same", distractors=["same", "no", "yes"]),
        make(key="", distractors=["a", "b", "c"]),
    ]
    assert key_longest_share(questions) == (1, 2)


def test_lesson_over_forty_percent_fails() -> None:
    longest = make(key="the long key", distractors=["a", "b", "c"])
    result = lint_lesson("m00-l00", [longest, longest], {"pg-sql-createindex": False})
    assert result.over
    assert "key-longest-share" in rules(result.failures)
    assert result.report == "m00-l00\tkey-longest\t2/2\t100%"


def test_failed_ids_reads_only_fail_rows(tmp_path: Path) -> None:
    verdicts = tmp_path / "m00-l00.verdicts.tsv"
    verdicts.write_text("q1\tpass\nq2\tfail\tstem short\nq3\tpass\n", encoding="utf-8")
    assert failed_ids(verdicts) == {"q2"}
    assert failed_ids(tmp_path / "missing.tsv") == frozenset()


# --- candidate selection -----------------------------------------------------------------------------------


def test_select_files_by_lesson_and_module(tmp_path: Path) -> None:
    (tmp_path / "m01").mkdir()
    (tmp_path / "m02").mkdir()
    for name in ("m01/m01-l01", "m01/m01-l02", "m02/m02-l01"):
        (tmp_path / f"{name}.questions.json").write_text("[]", encoding="utf-8")
    assert [p.name for p in select_files(None, "m01", [], tmp_path)] == [
        "m01-l01.questions.json",
        "m01-l02.questions.json",
    ]
    assert [p.name for p in select_files("m02-l01", "m02", [], tmp_path)] == ["m02-l01.questions.json"]
    assert len(select_files(None, None, [], tmp_path)) == 3


# --- fill_keys ---------------------------------------------------------------------------------------------


def record(root: Path, snippet: str, **fields: object) -> None:
    path = root / snippet
    path.parent.mkdir(parents=True, exist_ok=True)
    body = {"exit_code": 0, "stderr": "", **fields}
    path.with_suffix(".run.json").write_text(json.dumps(body), encoding="utf-8")


def test_key_is_the_recorded_stdout_without_trailing_newline(tmp_path: Path) -> None:
    record(tmp_path, "m06-l02/Lock.java", stdout="1\n2\n")
    assert fill_keys.recorded_key(tmp_path, "m06-l02/Lock.java") == "1\n2"


def test_key_of_a_failed_run_is_the_exception_line(tmp_path: Path) -> None:
    stderr = 'Exception in thread "main" java.lang.IllegalStateException: boom\n\tat Main.main(Main.java:3)\n'
    record(tmp_path, "m06-l02/Lock.java", exit_code=1, stdout="", stderr=stderr)
    assert fill_keys.recorded_key(tmp_path, "m06-l02/Lock.java") == "java.lang.IllegalStateException: boom"


def test_missing_run_record_raises(tmp_path: Path) -> None:
    with pytest.raises(fill_keys.MissingRecordError):
        fill_keys.recorded_key(tmp_path, "m06-l02/Lock.java")


def test_only_empty_keys_with_a_snippet_are_filled(tmp_path: Path) -> None:
    record(tmp_path, "m06-l02/Lock.java", stdout="42\n")
    entries: list[dict[str, object]] = [
        {"id": "a", "key": "", "snippet": "m06-l02/Lock.java"},
        {"id": "b", "key": "kept", "snippet": "m06-l02/Lock.java"},
        {"id": "c", "key": "", "snippet": None},
    ]
    assert [e["key"] for e in fill_keys.filled(entries, tmp_path)] == ["42", "kept", ""]


# --- calibration: real m06 questions (copied), verdicts by a blind verifier -------------------------------

Fixture = tuple[str, list[str], str]

VERIFIED_PASS: dict[str, Fixture] = {
    "m06-l01-q04": (
        "`t_xmin`",
        [
            "`t_xmax`",
            "`t_ctid`",
            "`t_hoff`",
        ],
        (
            "`t_xmin` holds the insert XID stamp. `t_xmax` holds the delete XID stamp, "
            "`t_ctid` holds the current TID of this or a newer row version, and `t_hoff` "
            "holds the offset to the user data."
        ),
    ),
    "m06-l01-q05": (
        "23 bytes",
        [
            "8 bytes",
            "16 bytes",
            "40 bytes",
        ],
        (
            "The fixed-size header occupies 23 bytes on most machines, so the smaller sizes "
            "of 8 and 16 bytes and the larger size of 40 bytes do not match the documented "
            "size."
        ),
    ),
    "m06-l01-q34": (
        ("It needs extra disk space for a new copy of the table until the operation completes"),
        [
            (
                "It compacts the table file in place, so it needs no disk space beyond what the "
                "table already uses"
            ),
            ("It lets `SELECT`, `INSERT`, `UPDATE` and `DELETE` run normally on the table while it works"),
            "Autovacuum issues it automatically whenever a table has become bloated",
        ],
        (
            "`VACUUM FULL` requires extra disk space for the new copy of the table until the "
            "operation completes. Compacting in place is wrong because it works by writing a "
            "complete new version of the table file with no dead space. Normal concurrent use"
            " is wrong because `VACUUM FULL` requires an `ACCESS EXCLUSIVE` lock on the table"
            " and therefore cannot be done in parallel with other use of the table. Automatic"
            " runs are wrong because the autovacuum daemon will never issue `VACUUM FULL`."
        ),
    ),
    "m06-l02-q14": (
        "Throw an `OptimisticLockException`",
        [
            "Overwrite the database state with the detached state",
            "Refresh the instance from the database and merge anyway",
            "Ignore the version, because version checks apply only to managed instances",
        ],
        (
            "The provider must throw an `OptimisticLockException` if the merged instance "
            "holds a stale revision. Overwriting would lose the updates that optimistic "
            "verification prevents. Refreshing and merging anyway is not allowed when the "
            "entity was updated since the instance became detached. The provider must examine"
            " the version of a detached instance when it is merged."
        ),
    ),
    "m06-l04-q14": (
        "Reads continue, but inserts, updates and deletes block",
        [
            "They are blocked from reading as well as from writing",
            "The lock is only taken when the table is large enough",
            "It takes no lock at all and scans the table twice in a row",
        ],
        (
            "A standard build locks the table against writes while other transactions can "
            "still read it. Reads are therefore not blocked. Even for smaller tables, a build"
            " can lock out writers for unacceptably long periods, so the lock does not depend"
            " on size. A standard build performs the entire build with a single scan under "
            "that lock."
        ),
    ),
    "m06-l03-q37": (
        ("It actually executes the query and shows the true row counts and run times of each plan node"),
        [
            ("It only plans the query and shows more precise cost estimates, without executing it"),
            ("Nothing changes, because the `ANALYZE` option defaults to `TRUE` and is already active"),
            ("It executes the query but leaves out buffer usage unless the `BUFFERS` option is also given"),
        ],
        (
            "With `ANALYZE`, `EXPLAIN` actually executes the query and then displays the true"
            " row counts and true run time accumulated within each plan node (`pg-using-"
            "explain#USING-EXPLAIN-ANALYZE`). Planning only is ruled out because the option "
            "is described as carrying out the command and showing actual run times and other "
            "statistics (`pg-sql-explain#id-1.9.3.148.8`). Being already active is ruled out "
            "because the `ANALYZE` parameter defaults to `FALSE` (`pg-sql-"
            "explain#id-1.9.3.148.8`). Missing buffer usage is ruled out because buffers "
            "information is automatically included when `ANALYZE` is used (`pg-sql-"
            "explain#id-1.9.3.148.8`)."
        ),
    ),
    "m06-l03-q09": (
        "`SELECT x FROM tab WHERE x = 'key' AND y < 42`",
        [
            "`SELECT x, z FROM tab WHERE x = 'key'`",
            "`SELECT x FROM tab WHERE x = 'key' AND z < 42`",
            "`SELECT z FROM tab WHERE x = 'key' AND y < 42`",
        ],
        (
            "The query that references only `x` and `y` uses columns stored in the index. "
            "Selecting `z` needs a column the index does not store. Filtering on `z` "
            "references an unstored column as well. The last query selects `z` too, so it "
            "cannot be answered from the index alone."
        ),
    ),
    "m01-l02-q03": (
        "`InvocationHandler`",
        [
            "`java.lang.reflect.Proxy`",
            "`java.lang.reflect.Method`",
            "`java.lang.Runnable`",
        ],
        (
            "The handler object implements the interface `InvocationHandler`. The class "
            "`java.lang.reflect.Proxy` is wrong because it is the class every proxy class "
            "extends, not what the handler implements. The class `java.lang.reflect.Method` "
            "is wrong because a `Method` object identifies the invoked method and is passed "
            "to `invoke`. The interface `java.lang.Runnable` is wrong because dispatching "
            "goes through the `invoke` method of `InvocationHandler`."
        ),
    ),
    "m01-l03-q03": (
        "Annotate the `package-info.java` of that package with `@NamedInterface`",
        [
            (
                "Annotate the `package-info.java` of that package with "
                "`@ApplicationModule(allowedDependencies = …)`"
            ),
            ("Annotate the types of that package with `@Service` so other modules can inject them"),
            'Write `"order :: *"` in a `@NamedInterface` annotation on that package',
        ],
        (
            "Exposing an additional package means annotating its `package-info.java`, or a "
            "`@PackageInfo` type, with `@NamedInterface`. The `allowedDependencies` attribute"
            " is declared by the consuming module to name what it may depend on, so it does "
            "not expose a package. By default the base package is the only package that "
            "allows incoming dependencies, so a `@Service` annotation exposes nothing more. "
            "The asterisk form `order :: *` is a value of `allowedDependencies` for all "
            "declared named interfaces, not of `@NamedInterface`."
        ),
    ),
    "m01-l03-q11": (
        "Once it has completed the state transitions on the primary aggregate",
        [
            "Before the state transitions, so listeners can veto them",
            "After the transaction commits, because publication is asynchronous by default",
            "Only after `InventoryManagement.updateStockFor` has returned",
        ],
        (
            "The event is published once the state transitions on the primary aggregate are "
            "complete. Publishing before the state transitions so that listeners can veto "
            "them is not what the example does, because it publishes after they are complete."
            " Publication is synchronous by default, so it does not wait for the commit. The "
            "example replaces the direct call to `InventoryManagement` with the event, so no "
            "such call exists."
        ),
    ),
    "m01-l03-q22": (
        (
            "It can return a single event instance or a collection of events, and it must not"
            " take any arguments"
        ),
        [
            (
                "It must return a `Collection<Object>` of events and it takes the aggregate root "
                "as its only argument"
            ),
            "It must return `void` and publish through `ApplicationEventPublisher` itself",
            "It is called only when `save(…)` is called on the repository",
        ],
        (
            "The method can return a single event instance or a collection and must not take "
            "arguments. It does not take the aggregate root, because it takes no arguments, "
            "and a single instance is allowed as well as a collection. It returns the events "
            "to publish rather than publishing them itself. It is called for `save(…)`, "
            "`saveAll(…)` and the delete methods listed, not for `save(…)` alone."
        ),
    ),
}

VERIFIED_FAIL_BY_SILENCE_OR_SHARING: dict[str, Fixture] = {
    "m06-l01-q02": (
        ("They do not conflict, so reading never blocks writing and writing never blocks reading"),
        [
            "Reading blocks writing on the same row until the reading statement has finished",
            "Writing blocks reading on the same row until the writing transaction commits",
            ("They conflict only at the Serializable level, where readers wait for concurrent writers"),
        ],
        (
            "Read locks and write locks do not conflict under MVCC. A reader holding up a "
            "writer and a writer holding up a reader are both ruled out by the same "
            "statement. The Serializable exception is ruled out because PostgreSQL maintains "
            "the guarantee even when providing the strictest level of transaction isolation."
        ),
    ),
    "m06-l03-q17": (
        "It includes buffers information automatically",
        [
            "It omits buffers information until `BUFFERS` is written",
            "It includes shared blocks only",
            "It raises an error that asks for `BUFFERS`",
        ],
        (
            "Buffers information is automatically included when `ANALYZE` is used. The output"
            " therefore does not wait for `BUFFERS`. Shared, local and temp blocks are all "
            "reported, so shared blocks alone is wrong. Nothing in the option description "
            "makes the command fail without `BUFFERS`."
        ),
    ),
    "m06-l03-q21": (
        "The skipped rows still have to be computed in the server",
        [
            "`OFFSET` locks the table until the page is returned",
            "`OFFSET` disables every index on the table",
            "The skipped rows are sent to the client and discarded there",
        ],
        (
            "The skipped rows still have to be computed inside the server. No table lock is "
            "described. Nothing says that indexes are disabled. Offset scrolling is also "
            "meant to avoid large results being sent to the client application, so the "
            "skipped rows are not sent."
        ),
    ),
    "m06-l03-q15": (
        "The number of rows emitted by the node",
        [
            "The number of rows scanned by the node",
            "The number of rows in the whole table",
            "The number of rows read from disk pages",
        ],
        (
            "The value is the number of rows emitted by the node, which is often less than "
            "the number scanned because of `WHERE` filtering. It is not the scanned count. It"
            " is not the size of the whole table. It is not a count of rows read from disk "
            "pages either."
        ),
    ),
    "m06-l01-q27": (
        "It still launches autovacuum to prevent wraparound",
        [
            "It waits for an administrator to run VACUUM by hand",
            "It shuts down the server until the table is vacuumed",
            "It starts only the launcher and leaves the workers stopped",
        ],
        (
            "The system launches autovacuum processes to prevent wraparound even when "
            "autovacuum is disabled. Waiting for an administrator, shutting down and leaving "
            "workers stopped contradict that."
        ),
    ),
    "m01-l02-q09": (
        ("It is dispatched to the handler's `invoke` method, like an interface method invocation"),
        [
            "It runs the `Object` implementation directly, without involving the handler",
            "It is forwarded to the target object's own method, bypassing the handler",
            ("It throws an `UnsupportedOperationException` unless the proxy interface redeclares it"),
        ],
        (
            "These invocations are encoded and dispatched to the handler's `invoke` method in"
            " the same manner as interface method invocations. The claim that the `Object` "
            "implementation runs directly is wrong because the handler sees the call. The "
            "claim of bypassing the handler is wrong because the handler is the only place "
            "the call goes. The claim about `UnsupportedOperationException` is wrong because "
            "the Javadoc describes dispatch to `invoke` with no requirement that the "
            "interface redeclare the methods."
        ),
    ),
    "m01-l02-q10": (
        ("It is a common open-source class definition library repackaged into `spring-core`"),
        [
            "It is built into the JDK, next to the dynamic proxies of `java.lang.reflect`",
            "It is an annotation processor that generates proxy classes at compile time",
            ("It is an optional aspect weaving module that is added to the class path by `spring-aop`"),
        ],
        (
            "CGLIB is a common open-source class definition library repackaged into `spring-"
            "core`. The claim that it is built into the JDK is wrong because it is JDK "
            "dynamic proxies that are built into the JDK. The claim of a compile-time "
            "annotation processor is wrong because a CGLIB proxy is a runtime-generated "
            "subclass. The aspect weaving module claim is wrong because the library is "
            "repackaged into `spring-core` itself."
        ),
    ),
    "m01-l03-q08": (
        (
            "When the module defines allowed dependencies via "
            "`@ApplicationModule(allowedDependencies = …)` and the target is not among them"
        ),
        [
            (
                "Always, for every module in the application, because each module has an empty "
                "list of allowed dependencies by default"
            ),
            "Only when the `jMolecules` ArchUnit library is on the classpath",
            "Only when the module is checked by a Maven plugin instead of calling `verify()`",
        ],
        (
            "The rule is optional: a module can define allowed dependencies, and when it "
            "does, dependencies to other modules are rejected. The rule is not applied by "
            "default to every module, because it is optional. The `jMolecules` integration is"
            " a separate, optional addition that triggers its own DDD rules when present. "
            "Verification runs by calling `verify()` on an `ApplicationModules` instance, not"
            " through a plugin."
        ),
    ),
}


def from_fixture(question_id: str, fixture: Fixture) -> Candidate:
    key, distractors, explanation = fixture
    return make(id=question_id, key=key, distractors=distractors, explanation=explanation)


@pytest.mark.parametrize("question_id", sorted(VERIFIED_PASS))
def test_explanation_the_verifier_passed_lints_clean(question_id: str) -> None:
    q = from_fixture(question_id, VERIFIED_PASS[question_id])
    assert explanation_failures(q) == []


@pytest.mark.parametrize("question_id", sorted(VERIFIED_FAIL_BY_SILENCE_OR_SHARING))
def test_explanation_the_verifier_failed_for_silence_or_sharing_is_flagged(question_id: str) -> None:
    q = from_fixture(question_id, VERIFIED_FAIL_BY_SILENCE_OR_SHARING[question_id])
    assert explanation_failures(q)
