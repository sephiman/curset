# SPDX-License-Identifier: AGPL-3.0-only
"""Strip saved pages (`content/<course>/sources/otros/*.html`) in place; record each new sha256.

Run on every page before it is recorded, and once over a course:

    uv run python scripts/strip_saved_pages.py --course <slug> [--files a.html …] --originals <dir>

`--originals` (outside the repo) keeps the bytes as fetched, out of git. `tests/test_saved_pages.py` fails
on an unstripped page.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tradeschool.citations.saved_pages import strip_page
from tradeschool.citations.sources import sha256

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / "content"
HTML_SUFFIXES = (".html", ".htm")


def saved_pages(otros: Path, names: list[str] | None) -> list[Path]:
    if names:
        return [otros / name for name in names]
    return sorted(p for p in otros.rglob("*") if p.suffix.lower() in HTML_SUFFIXES)


def record_sha256(fuentes: Path, digests: dict[str, str]) -> list[str]:
    """Rewrite the `sha256:` line of each entry named in `digests`; the names with no entry come back."""
    lines = fuentes.read_text(encoding="utf-8").split("\n")
    current: str | None = None
    seen: set[str] = set()
    for i, line in enumerate(lines):
        entry = re.match(r"^- file: ['\"]?(.+?)['\"]?\s*$", line)
        if entry:
            current = entry[1]
            continue
        field = re.match(r"^(\s+sha256: )\S+\s*$", line)
        if field and current in digests:
            lines[i] = field[1] + digests[current]
            seen.add(current)
    fuentes.write_text("\n".join(lines), encoding="utf-8")
    return sorted(set(digests) - seen)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--course", required=True)
    parser.add_argument("--files", nargs="*", help="names under sources/otros/; default: every saved page")
    parser.add_argument("--originals", type=Path, required=True, help="where the unstripped bytes go")
    args = parser.parse_args()

    originals: Path = args.originals.resolve()
    if originals.is_relative_to(REPO):
        parser.error("--originals must be outside the repository: the unstripped bytes stay out of git")
    otros = CONTENT / args.course / "sources" / "otros"
    digests: dict[str, str] = {}
    for page in saved_pages(otros, args.files):
        raw = page.read_bytes()
        stripped = strip_page(raw)
        if stripped == raw:
            continue
        name = page.relative_to(otros).as_posix()
        backup = originals / args.course / name
        backup.parent.mkdir(parents=True, exist_ok=True)
        if not backup.exists():  # a second run must not overwrite the bytes as fetched
            backup.write_bytes(raw)
        page.write_bytes(stripped)
        digests[name] = sha256(page)
    missing = record_sha256(otros / "fuentes.yaml", digests)
    print(f"{args.course}: {len(digests)} pages stripped; originals in {originals / args.course}")
    for name in missing:
        print(f"  no fuentes.yaml entry with a sha256 line: {name}")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
