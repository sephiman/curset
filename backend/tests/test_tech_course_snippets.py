# SPDX-License-Identifier: AGPL-3.0-only
"""Running lesson snippets on the pinned toolchain, offline; the record check; variant families end to end."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest
import yaml
from scripts.tech_course import build_variants, lessons, run_snippets, toolchain
from scripts.tech_course.run_snippets import Toolchain

from tradeschool.content.reading import prose_word_count
from tradeschool.exercises.quiz import QuizVariant

FIXTURE_FAMILY = Path(__file__).parent / "fixtures" / "variants" / "loop-sum.yaml"
PINS = toolchain.pinned("backend-in-depth")


def _runnable() -> bool:
    if shutil.which("java") is None or shutil.which("unshare") is None:
        return False
    try:
        run_snippets.require_isolation()
        toolchain.checked_java(PINS)
    except run_snippets.IsolationError, toolchain.ToolchainError:
        return False
    return True


needs_jdk = pytest.mark.skipif(not _runnable(), reason="needs the pinned JDK and unshare -rn")


@pytest.fixture
def jdk() -> Toolchain:
    return run_snippets.build_toolchain(PINS, needs_kotlin=False)


# --- toolchain pins ------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("reported", "matches"),
    [("25.0.5", True), ("25.0.5.0.3", True), ("25.0.50", False), ("25.0.4", False), ("26.0.1", False)],
)
def test_java_must_match_the_pin_on_whole_dotted_components(reported: str, matches: bool) -> None:
    assert toolchain.java_matches(reported, "25.0.5") is matches


def test_the_pins_come_from_versions_yaml() -> None:
    assert PINS.java == "25.0.5" and PINS.kotlin == "2.4.21"


def test_any_kotlin_version_but_the_pinned_one_is_refused() -> None:
    with pytest.raises(toolchain.ToolchainError, match=r"refusing Kotlin 2\.5\.0"):
        toolchain.provision_kotlin(PINS, "2.5.0")


# --- running ---------------------------------------------------------------------------------------------


HELLO = (
    'public class Hello { public static void main(String[] a) { System.out.println("hi " + (1 + 2)); } }\n'
)


@needs_jdk
def test_a_snippet_is_run_and_its_output_recorded_with_hashes_and_versions(jdk: Toolchain) -> None:
    record = run_snippets.run_source("Hello.java", HELLO, jdk)
    assert (record.exit_code, record.stdout, record.stderr) == (0, "hi 3\n", "")
    assert record.stdout_sha256 == run_snippets.sha256_text("hi 3\n")
    assert record.snippet_sha256 == run_snippets.sha256_text(HELLO)
    assert record.java.startswith("25.0.5") and record.commands == [["java", "Hello.java"]]


@needs_jdk
def test_a_deliberately_broken_snippet_records_its_compiler_error(jdk: Toolchain) -> None:
    record = run_snippets.run_source("Broken.java", 'public class Broken { int x = "s"; }\n', jdk)
    assert record.exit_code != 0 and "incompatible types" in record.stderr


@needs_jdk
def test_a_snippet_that_runs_too_long_is_killed_and_marked(jdk: Toolchain) -> None:
    loop = "public class Spin { public static void main(String[] a) { while (true) { } } }\n"
    record = run_snippets.run_source("Spin.java", loop, jdk, timeout=3)
    assert record.timed_out and record.exit_code == 124


@needs_jdk
def test_a_snippet_cannot_reach_the_network(jdk: Toolchain) -> None:
    probe = (
        "public class Probe { public static void main(String[] a) { try (var s = new java.net.Socket()) {"
        ' s.connect(new java.net.InetSocketAddress("1.1.1.1", 80), 2000); System.out.println("connected");'
        ' } catch (Exception e) { System.out.println("blocked"); } } }\n'
    )
    assert run_snippets.run_source("Probe.java", probe, jdk).stdout == "blocked\n"


def test_nothing_runs_when_the_wrong_java_is_on_the_path(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(toolchain, "java_version", lambda: "21.0.1")
    with pytest.raises(toolchain.ToolchainError, match=r"pins 25\.0\.5"):
        toolchain.checked_java(PINS)


# --- --check ---------------------------------------------------------------------------------------------


def _snippet_course(root: Path, block_body: str) -> Path:
    course = root / "content" / "tc"
    folder = course / "snippets" / "m06-l02"
    folder.mkdir(parents=True)
    (folder / "Hello.java").write_text(HELLO, encoding="utf-8")
    (course / "en" / "lessons").mkdir(parents=True)
    (course / "en" / "lessons" / "m06-l02.md").write_text(
        f"## S\n\n```java snippet=m06-l02/Hello.java\n{block_body}```\n", encoding="utf-8"
    )
    (course / "exercises").mkdir()
    (course / "exercises" / "m06-l02-ex-1.yaml").write_text(
        "type: quiz\nvariants:\n- id: q1\n  snippet: m06-l02/Missing.java\n", encoding="utf-8"
    )
    (course / "sources").mkdir()
    (course / "sources" / "versions.yaml").write_text(
        "products:\n- product: Java 25 LTS\n  version: 25.0.5\n- product: Kotlin\n  version: 2.4.21\n",
        encoding="utf-8",
    )
    return folder


def test_check_demands_a_record_a_matching_block_and_an_existing_question_snippet(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(lessons, "REPO", tmp_path)
    folder = _snippet_course(tmp_path, "different\n")
    assert run_snippets.check_problems("tc") == [
        "m06-l02/Hello.java: no run record (Hello.run.json)",
        "lesson m06-l02 line 3: the block differs from m06-l02/Hello.java",
        "question m06-l02-ex-1/q1: snippet m06-l02/Missing.java does not exist",
    ]
    (folder / "Hello.run.json").write_text(json.dumps({"snippet_sha256": "stale"}), encoding="utf-8")
    assert run_snippets.check_problems("tc")[0].endswith(
        "the run record is of another version of the snippet"
    )


def test_check_passes_when_record_and_block_match_the_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(lessons, "REPO", tmp_path)
    folder = _snippet_course(tmp_path, HELLO)
    (tmp_path / "content/tc/exercises/m06-l02-ex-1.yaml").unlink()
    record = {"snippet_sha256": run_snippets.sha256_text(HELLO), "java": "25.0.5"}
    (folder / "Hello.run.json").write_text(json.dumps(record), encoding="utf-8")
    assert run_snippets.check_problems("tc") == []


def test_check_fails_a_record_made_on_a_toolchain_other_than_the_pinned_one(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(lessons, "REPO", tmp_path)
    folder = _snippet_course(tmp_path, HELLO)
    (tmp_path / "content/tc/exercises/m06-l02-ex-1.yaml").unlink()
    record = {"snippet_sha256": run_snippets.sha256_text(HELLO), "java": "21.0.1"}
    (folder / "Hello.run.json").write_text(json.dumps(record), encoding="utf-8")
    assert run_snippets.check_problems("tc") == [
        "m06-l02/Hello.java: recorded on Java 21.0.1, the course pins 25.0.5"
    ]


def test_a_fenced_block_with_snippet_meta_is_still_code_to_the_reading_time_counter() -> None:
    plain = prose_word_count("Some prose here.")
    with_block = prose_word_count(
        "Some prose here.\n\n```java snippet=m06-l02/Hello.java\nclass A { int many words in code; }\n```\n"
    )
    assert with_block == plain


# --- variants --------------------------------------------------------------------------------------------


def test_grid_points_and_mutants_are_pure_substitutions() -> None:
    assert build_variants.grid_points({"a": [1, 2], "b": ["x"]}) == [{"a": 1, "b": "x"}, {"a": 2, "b": "x"}]
    mistake = build_variants.Mistake("m", "i < @@n@@", "i <= @@n@@")
    assert build_variants.mutant("for (i < 3)", mistake, {"n": 3}) == "for (i <= 3)"
    assert build_variants.mutant("nothing", mistake, {"n": 3}) is None


@needs_jdk
def test_a_family_is_instantiated_run_and_written_as_a_quiz_with_script_computed_distractors(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, jdk: Toolchain
) -> None:
    monkeypatch.setattr(lessons, "REPO", tmp_path)
    (tmp_path / "content" / "tc").mkdir(parents=True)
    family = build_variants.load_family(FIXTURE_FAMILY)
    variants, skipped = build_variants.build_family(family, jdk)
    assert skipped == [] and len(variants) == 4
    exercise, runs = build_variants.write_outputs("tc", family, variants)

    loaded = yaml.safe_load(exercise.read_text(encoding="utf-8"))
    for raw in loaded["variants"]:
        QuizVariant.model_validate(raw)
    # limit=3 step=1 prints 3; the mistakes print 6 (bound included), 1 (bound - 1) and 4 (sum starts at one)
    first = loaded["variants"][0]
    texts = {o["id"]: o["text"]["en"] for o in first["options"]}
    assert sorted(texts.values()) == ["`1`", "`3`", "`4`", "`6`"]
    assert [texts[o["id"]] for o in first["options"] if o.get("correct")] == ["`3`"]
    keys = [next(i for i, o in enumerate(v["options"]) if o.get("correct")) for v in loaded["variants"]]
    assert keys == [0, 1, 2, 3]
    assert "```java" in first["prompt"]["en"] and "@@" not in first["explanation"]["en"]
    evidence = json.loads(runs.read_text(encoding="utf-8"))
    assert evidence[0]["stdout_sha256"] == run_snippets.sha256_text("3\n")


def _kotlin_ready() -> bool:
    try:
        toolchain.checked_kotlin(PINS)
    except toolchain.ToolchainError:
        return False
    return _runnable()


@pytest.mark.skipif(not _kotlin_ready(), reason="needs the provisioned Kotlin compiler")
def test_a_kotlin_snippet_is_compiled_and_run_on_the_pinned_compiler() -> None:
    tools = run_snippets.build_toolchain(PINS, needs_kotlin=True)
    record = run_snippets.run_source(
        "Main.kt", "fun main() { println(listOf(1, 2).sum()) }\n", tools, timeout=120
    )
    assert (record.exit_code, record.stdout, record.kotlin) == (0, "3\n", "2.4.21")
    assert record.commands[1] == ["java", "-jar", "Main.jar"]
