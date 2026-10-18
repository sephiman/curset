# SPDX-License-Identifier: AGPL-3.0-only
"""Build each course's `source-index.json`: the page (PDF) or element id (HTML) where every cited unit starts.

Run at generation time, after a course's `sources/normativa/` changes:

    uv run python scripts/index_sources.py                 # every course under content/ with normativa.yaml
    uv run python scripts/index_sources.py --course <slug>

Serving reads the index and never opens a PDF. `tests/test_citations.py` fails while an indexed file's
sha256 no longer matches the file on disk.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml
from pypdf import PdfReader

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tradeschool.citations.sources import INDEX_FILE, index_html, index_pdf_pages, sha256

CONTENT = Path(__file__).resolve().parents[2] / "content"


def index_file(path: Path) -> dict[str, object]:
    if path.suffix.lower() == ".pdf":
        pages = [page.extract_text() or "" for page in PdfReader(path).pages]
        units: dict[str, object] = dict(index_pdf_pages(pages))
    else:
        units = dict(index_html(path.read_text(encoding="utf-8", errors="replace")))
    return {"sha256": sha256(path), "units": dict(sorted(units.items()))}


def build(course_dir: Path) -> dict[str, object]:
    norms = yaml.safe_load((course_dir / "sources" / "normativa.yaml").read_text(encoding="utf-8")) or []
    files: dict[str, object] = {}
    for entry in norms:
        file = entry.get("file") if isinstance(entry, dict) else None
        if not file or not (course_dir / file).exists():
            continue
        files[file] = index_file(course_dir / file)
        units = files[file]["units"]  # type: ignore[index]
        print(f"  {file}: {len(units)} units")
    return {"files": dict(sorted(files.items()))}


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
        print(course_dir.name)
        index = build(course_dir)
        (course_dir / INDEX_FILE).write_text(
            json.dumps(index, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
