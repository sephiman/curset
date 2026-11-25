# SPDX-License-Identifier: AGPL-3.0-only
"""Run the lesson snippets on the pinned toolchain, offline, and record each run beside its file.

    uv run python -m scripts.tech_course.run_snippets [--course C] [--lesson ID] [--timeout SECONDS]
    uv run python -m scripts.tech_course.run_snippets --check

A snippet is `snippets/<lesson>/<File>.java|.kt`; its record is `<File>.run.json`. Every command runs under
`unshare -rn` (an empty network namespace); with no such isolation nothing is executed. `--check` runs
nothing: it verifies records, lesson blocks (`snippet=<lesson>/<File>`) and the `snippet:` of questions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path

from scripts.tech_course.lessons import add_course_argument, course_dir, read_lessons
from scripts.tech_course.questions import read_questions
from scripts.tech_course.toolchain import (
    Pins,
    ToolchainError,
    checked_java,
    checked_kotlin,
    checked_libs,
    java_matches,
    pinned,
)

DEFAULT_TIMEOUT = 30
ISOLATION = ["unshare", "-rn", "--"]
SUFFIXES = {".java", ".kt"}
LIBS_GLOB = "libs/*"
_LIBRARY_IMPORT = re.compile(r"^import\s+(?:static\s+)?(?:org\.springframework|org\.aspectj|kotlinx)\.", re.M)


class IsolationError(RuntimeError):
    pass


@dataclass(frozen=True)
class Toolchain:
    java: str
    kotlin: str | None
    kotlin_home: Path | None
    libs: tuple[Path, ...] = ()


@dataclass(frozen=True)
class RunRecord:
    snippet: str
    snippet_sha256: str
    commands: list[list[str]]
    exit_code: int
    timed_out: bool
    stdout: str
    stderr: str
    stdout_sha256: str
    java: str
    kotlin: str | None
    isolation: str
    libs: list[str] | None = None


def needs_libs(source: str) -> bool:
    return _LIBRARY_IMPORT.search(source) is not None


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def require_isolation() -> None:
    probe = subprocess.run([*ISOLATION, "true"], capture_output=True, check=False)
    if probe.returncode != 0:
        raise IsolationError("no network isolation here (unshare -rn failed); refusing to run snippets")


def build_toolchain(
    pins: Pins, needs_kotlin: bool, kotlin_home: Path | None = None, needs_libraries: bool = False
) -> Toolchain:
    java = checked_java(pins)
    libs = tuple(checked_libs()) if needs_libraries else ()
    if not needs_kotlin:
        return Toolchain(java, None, None, libs)
    home, version = checked_kotlin(pins, kotlin_home)
    return Toolchain(java, version, home, libs)


def commands_for(file_name: str, with_libs: bool = False) -> list[list[str]]:
    """The steps, as written in the record (relative names; `libs/*` stands for the resolved jars)."""
    stem = file_name.removesuffix(".java").removesuffix(".kt")
    if file_name.endswith(".java") and not with_libs:
        return [["java", file_name]]
    if file_name.endswith(".java"):
        return [
            ["javac", "-parameters", "-cp", LIBS_GLOB, "-d", "out", file_name],
            ["java", "-cp", f"out:{LIBS_GLOB}", stem],
        ]
    if with_libs:
        return [
            ["kotlinc", "-cp", LIBS_GLOB, file_name, "-d", f"{stem}.jar"],
            ["java", "-cp", f"{stem}.jar:{LIBS_GLOB}", f"{stem}Kt"],
        ]
    return [
        ["kotlinc", file_name, "-include-runtime", "-d", f"{stem}.jar"],
        ["java", "-jar", f"{stem}.jar"],
    ]


def _real(command: list[str], toolchain: Toolchain, folder: str) -> list[str]:
    classpath = ":".join(str(jar) for jar in toolchain.libs)
    args = [part.replace(LIBS_GLOB, classpath) for part in command[1:]]
    if command[0] != "kotlinc":
        return [*ISOLATION, command[0], *args]
    assert toolchain.kotlin_home is not None
    return [*ISOLATION, str(toolchain.kotlin_home / "bin" / "kotlinc"), *args]


def run_source(
    file_name: str, source: str, toolchain: Toolchain, timeout: int = DEFAULT_TIMEOUT
) -> RunRecord:
    """Compile and run one snippet in a fresh folder; the last step's output is the record's."""
    commands = commands_for(file_name, needs_libs(source))
    with tempfile.TemporaryDirectory(prefix="snippet-") as folder:
        (Path(folder) / file_name).write_text(source, encoding="utf-8")
        for command in commands:
            try:
                done = subprocess.run(
                    _real(command, toolchain, folder),
                    cwd=folder,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    check=False,
                )
            except subprocess.TimeoutExpired as exc:
                return _record(
                    file_name, source, commands, toolchain, 124, True, _text(exc.stdout), _text(exc.stderr)
                )
            if done.returncode != 0:
                return _record(
                    file_name, source, commands, toolchain, done.returncode, False, done.stdout, done.stderr
                )
    return _record(file_name, source, commands, toolchain, 0, False, done.stdout, done.stderr)


def _text(captured: str | bytes | None) -> str:
    return captured.decode(errors="replace") if isinstance(captured, bytes) else captured or ""


def _record(
    name: str,
    source: str,
    commands: list[list[str]],
    toolchain: Toolchain,
    code: int,
    timed_out: bool,
    out: str,
    err: str,
) -> RunRecord:
    return RunRecord(
        snippet=name,
        snippet_sha256=sha256_text(source),
        commands=commands,
        exit_code=code,
        timed_out=timed_out,
        stdout=out,
        stderr=err,
        stdout_sha256=sha256_text(out),
        java=toolchain.java,
        kotlin=toolchain.kotlin if name.endswith(".kt") else None,
        isolation=" ".join(ISOLATION[:-1]),
        libs=sorted(jar.name for jar in toolchain.libs) if needs_libs(source) else None,
    )


def snippet_files(course: str, lesson: str | None = None) -> list[Path]:
    root = course_dir(course) / "snippets"
    pattern = f"{lesson}/*" if lesson else "*/*"
    return sorted(path for path in root.glob(pattern) if path.suffix in SUFFIXES)


def record_path(snippet: Path) -> Path:
    return snippet.with_suffix(".run.json")


def write_record(snippet: Path, record: RunRecord) -> None:
    named = RunRecord(**{**asdict(record), "snippet": f"{snippet.parent.name}/{snippet.name}"})
    record_path(snippet).write_text(
        json.dumps(asdict(named), indent=1, ensure_ascii=False) + "\n", encoding="utf-8"
    )


# --- check ---------------------------------------------------------------------------------------------


def check_problems(course: str) -> list[str]:
    root = course_dir(course) / "snippets"
    problems: list[str] = []
    pins = pinned(course)
    for snippet in snippet_files(course):
        problems += _record_problems(snippet, pins)
    for lesson in read_lessons(course):
        for block in lesson.snippet_blocks():
            problems += _block_problems(root, lesson.id, block.line, block.path, block.body)
    for question in read_questions(course):
        if question.snippet and not (root / question.snippet).is_file():
            problems.append(f"question {question.label}: snippet {question.snippet} does not exist")
    return problems


def _record_problems(snippet: Path, pins: Pins) -> list[str]:
    name = f"{snippet.parent.name}/{snippet.name}"
    path = record_path(snippet)
    if not path.is_file():
        return [f"{name}: no run record ({path.name})"]
    recorded = json.loads(path.read_text(encoding="utf-8"))
    if recorded.get("snippet_sha256") != sha256_text(snippet.read_text(encoding="utf-8")):
        return [f"{name}: the run record is of another version of the snippet"]
    source = snippet.read_text(encoding="utf-8")
    if needs_libs(source) and not recorded.get("libs"):
        return [f"{name}: uses the pinned libraries but the record names none"]
    return _toolchain_problems(name, snippet.suffix, recorded, pins)


def _toolchain_problems(name: str, suffix: str, recorded: dict[str, str | None], pins: Pins) -> list[str]:
    problems = []
    if not java_matches(str(recorded.get("java")), pins.java):
        problems.append(f"{name}: recorded on Java {recorded.get('java')}, the course pins {pins.java}")
    if suffix == ".kt" and recorded.get("kotlin") != pins.kotlin:
        problems.append(f"{name}: recorded on Kotlin {recorded.get('kotlin')}, the course pins {pins.kotlin}")
    return problems


def _block_problems(root: Path, lesson_id: str, line: int, path: str, body: str) -> list[str]:
    where = f"lesson {lesson_id} line {line}"
    file = root / path
    if not file.is_file():
        return [f"{where}: snippet {path} does not exist"]
    if file.read_text(encoding="utf-8").strip("\n") != body.strip("\n"):
        return [f"{where}: the block differs from {path}"]
    return []


# --- run -----------------------------------------------------------------------------------------------


def run_all(course: str, lesson: str | None, timeout: int, kotlin_home: Path | None = None) -> int:
    files = snippet_files(course, lesson)
    if not files:
        print("run_snippets: no snippets")
        return 0
    try:
        require_isolation()
        sources = {f: f.read_text(encoding="utf-8") for f in files}
        toolchain = build_toolchain(
            pinned(course),
            any(f.suffix == ".kt" for f in files),
            kotlin_home,
            any(needs_libs(text) for text in sources.values()),
        )
    except (IsolationError, ToolchainError) as exc:
        print(f"run_snippets: {exc}", file=sys.stderr)
        return 2
    failures = 0
    for snippet in files:
        record = run_source(snippet.name, snippet.read_text(encoding="utf-8"), toolchain, timeout)
        write_record(snippet, record)
        failures += record.timed_out
        print(f"{snippet.parent.name}/{snippet.name}\texit {record.exit_code}\t{record.stdout_sha256[:12]}")
    print(f"run_snippets: {len(files)} snippets run, {failures} timed out")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_course_argument(parser)
    parser.add_argument("--lesson")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--check", action="store_true", help="verify records and lesson blocks; run nothing")
    args = parser.parse_args(argv)
    if not args.check:
        return run_all(args.course, args.lesson, args.timeout)
    problems = check_problems(args.course)
    for problem in problems:
        print(f"FAIL {problem}")
    print(f"run_snippets --check: {len(snippet_files(args.course))} snippets, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
