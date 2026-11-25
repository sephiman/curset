# SPDX-License-Identifier: AGPL-3.0-only
"""Prose words (the reading-time counter) of each lesson before (d2/prev) and after: word_counts.py LESSON..."""

import sys
from pathlib import Path

from tradeschool.content.reading import prose_word_count

REPO = Path(__file__).resolve().parents[4]
for lesson in sys.argv[1:]:
    before = prose_word_count((REPO / "docs/_work/backend-in-depth/d2/prev" / f"{lesson}.md").read_text(encoding="utf-8"))
    after = prose_word_count((REPO / "content/backend-in-depth/en/lessons" / f"{lesson}.md").read_text(encoding="utf-8"))
    print(f"{lesson}\t{before}\t{after}")
