# SPDX-License-Identifier: AGPL-3.0-only
"""Build each course's `excerpts.json`: the cited text of the norm for every question's solution panel.

Run at generation time, after a course's questions or `sources/` change (after `index_sources.py`):

    uv run python scripts/extract_excerpts.py                  # every course with sources/normativa.yaml
    uv run python scripts/extract_excerpts.py --course <slug>

Prints, per course, how many questions got an excerpt and every one that did not, with its reason. Serving
reads the file and never opens a PDF; loading a course fails while a cited question has no entry in it.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

from pypdf import PdfReader

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tradeschool.citations.excerpt_build import SourceTexts, build_excerpts
from tradeschool.citations.excerpt_store import EXCERPTS_FILE
from tradeschool.content.registry import load_registry

CONTENT = Path(__file__).resolve().parents[2] / "content"


def pdf_pages(path: Path) -> list[str]:
    return [page.extract_text() or "" for page in PdfReader(path).pages]


def report(slug: str, built: dict[str, object]) -> list[str]:
    """The build report: counts per course, then each question without an excerpt and why."""
    questions = built["questions"]
    assert isinstance(questions, dict)
    missing = {key: entry["none"] for key, entry in questions.items() if "none" in entry}
    total = len(questions)
    share = 100 * len(missing) / total if total else 0.0
    counts = f"{total - len(missing)} excerpts, {len(missing)} no excerpt ({share:.2f} %)"
    lines = [f"{slug}: {total} questions, {counts}"]
    lines += [f"  {count:5d}  {reason}" for reason, count in Counter(missing.values()).most_common()]
    lines += [
        f"  no excerpt: {key} «{questions[key]['citation']}»: {reason}" for key, reason in missing.items()
    ]
    flagged = {
        key: entry["excerpt"]["flag"]
        for key, entry in questions.items()
        if isinstance(entry.get("excerpt"), dict) and entry["excerpt"].get("flag")
    }
    lines += [f"  {count:5d}  flagged {flag}" for flag, count in Counter(flagged.values()).most_common()]
    lines += [f"  flagged {flag}: {key} «{questions[key]['citation']}»" for key, flag in flagged.items()]
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--content", type=Path, default=CONTENT)
    parser.add_argument("--course", help="one course slug; default: every course with sources/normativa.yaml")
    args = parser.parse_args()
    courses = (
        [args.content / args.course]
        if args.course
        else sorted(path.parents[1] for path in args.content.glob("*/sources/normativa.yaml"))
    )
    for course_dir in courses:
        registry = load_registry(course_dir, check_excerpts=False)
        built = build_excerpts(registry, SourceTexts(course_dir, pdf_pages))
        (course_dir / EXCERPTS_FILE).write_text(
            json.dumps(built, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8"
        )
        print("\n".join(report(registry.slug, built)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
