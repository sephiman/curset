# SPDX-License-Identifier: AGPL-3.0-only
"""Build and close scripts never produce published content from round working files (docs/_work/)."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
WORK_DIR = re.compile(r"docs/_work|[\"']_work[\"']")
PYTHON_WRITE = re.compile(
    r"write_text|write_bytes|open\([^)]*[\"'][wa]b?[\"']|json\.dump\(|yaml\.(?:safe_)?dump\(|shutil\."
)
SHELL_WRITE = re.compile(r">\s*\"?\$|\b(?:rm|cp|mv|tee)\b")
INVOKED_PATH = re.compile(r"[\w./-]+\.(?:py|sh)\b")
INVOKED_MODULE = re.compile(r"\btech (\w+)|scripts\.tech_course\.(\w+)")


def tracked(pattern: str) -> list[Path]:
    listed = subprocess.run(
        ["git", "ls-files", pattern], cwd=REPO, capture_output=True, text=True, check=True
    )
    return [REPO / line for line in listed.stdout.splitlines() if (REPO / line).is_file()]


def invoked_by(script: Path) -> set[Path]:
    text = script.read_text(encoding="utf-8")
    found = {
        REPO / "backend" / "scripts" / "tech_course" / f"{a or b}.py" for a, b in INVOKED_MODULE.findall(text)
    }
    for raw in INVOKED_PATH.findall(text):
        name = raw.removeprefix("$repo/")
        found |= {base / name for base in (REPO, REPO / "backend") if (base / name).is_file()}
    return {path for path in found if path.is_file() and path != script}


def build_and_close_scripts() -> list[Path]:
    closers = tracked("*close_round.sh")
    builders = [*tracked("*build_*.py"), *tracked("*build_*.sh")]
    invoked = {path for closer in closers for path in invoked_by(closer)}
    return sorted({*closers, *builders, *invoked})


def writes_files(script: Path) -> bool:
    pattern = SHELL_WRITE if script.suffix == ".sh" else PYTHON_WRITE
    return bool(pattern.search(script.read_text(encoding="utf-8")))


def test_close_round_and_what_it_runs_are_in_scope() -> None:
    scripts = {path.relative_to(REPO).as_posix() for path in build_and_close_scripts()}
    assert "docs/backend-verification/tools/close_round.sh" in scripts
    assert "backend/scripts/export_bundle.py" in scripts
    assert "backend/scripts/tech_course/lint_questions.py" in scripts


@pytest.mark.parametrize("script", build_and_close_scripts(), ids=lambda p: p.relative_to(REPO).as_posix())
def test_build_or_close_script_that_writes_does_not_read_round_working_files(script: Path) -> None:
    if writes_files(script):
        assert not WORK_DIR.search(script.read_text(encoding="utf-8")), (
            "reads docs/_work/ while writing output"
        )
