"""Replace one sentence of a lesson, matching across hard line wraps: replace_sentence.py <lesson.md> <old> <new>."""

import re
import sys
from pathlib import Path

path, old, new = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
text = path.read_text()
pattern = r"\s+".join(re.escape(token) for token in old.split())
matches = list(re.finditer(pattern, text))
if len(matches) != 1:
    sys.exit(f"{len(matches)} matches for: {old[:80]}")
path.write_text(text[: matches[0].start()] + new + text[matches[0].end() :])
print("replaced", old[:60])
