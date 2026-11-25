# SPDX-License-Identifier: AGPL-3.0-only
"""Remove the diagram blocks named by item id: drop_diagrams.py LESSON ITEM_ID...  (ids from <lesson>.items.tsv)."""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
lesson, ids = sys.argv[1], sys.argv[2:]
rows = {r.split("\t")[0]: r.split("\t")[3] for r in (REPO / f"docs/_work/backend-in-depth/d2/{lesson}.items.tsv").read_text().splitlines() if r}
path = REPO / f"content/backend-in-depth/en/lessons/{lesson}.md"
text = path.read_text(encoding="utf-8")
for item in ids:
    block = rows[item].replace(" ⏎ ", "\n")
    assert text.count(block) == 1, f"{item}: block not found once"
    text = re.sub(re.escape(block) + r"\n\n?", "", text, count=1)
    print(f"dropped {item}")
path.write_text(text, encoding="utf-8")
