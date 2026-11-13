# SPDX-License-Identifier: AGPL-3.0-only
"""Replace "Summary pending." in course.yaml with each staged `<lesson>.summary.txt` of a module folder.

    python apply_summaries.py MODULE_DIR
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

COURSE = Path(__file__).resolve().parents[4] / "content/backend-in-depth/course.yaml"


def quoted(text: str) -> str:
    return "'" + text.replace("'", "''") + "'"


def apply(course_text: str, lesson: str, summary: str) -> str:
    pattern = re.compile(rf"(- id: {re.escape(lesson)}\n(?:      .*\n)*?        en: )Summary pending\.\n")
    return pattern.sub(lambda m: m.group(1) + quoted(summary) + "\n", course_text, count=1)


def main(argv: list[str]) -> int:
    text = COURSE.read_text(encoding="utf-8")
    for staged in sorted(Path(argv[1]).glob("m*-l*.summary.txt")):
        lesson = staged.name.split(".")[0]
        updated = apply(text, lesson, " ".join(staged.read_text(encoding="utf-8").split()))
        print(f"{lesson}: {'applied' if updated != text else 'unchanged'}")
        text = updated
    COURSE.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
