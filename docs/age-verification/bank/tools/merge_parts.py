"""Merge an engine tema's part drafts into its draft. Usage: merge_parts.py bloque-iii m03-l03.

Concatenates `<lesson>.part-<k>.draft.json` in part order (each part keeps its id range and lesson-section order) into
`<lesson>.draft.json`; stops on a duplicate id.
"""
import json
import sys
from pathlib import Path

folder = Path(__file__).resolve().parents[1] / sys.argv[1]
lesson = sys.argv[2]
parts = sorted(folder.glob(f'{lesson}.part-*.draft.json'), key=lambda p: int(p.name.split('.')[1].split('-')[1]))
merged = [q for p in parts for q in json.loads(p.read_text(encoding='utf-8'))]
ids = [q['id'] for q in merged]
dupes = {i for i in ids if ids.count(i) > 1}
if dupes:
    sys.exit(f'duplicate ids: {sorted(dupes)}')
(folder / f'{lesson}.draft.json').write_text(json.dumps(merged, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(f'{lesson}: {len(parts)} parts, {len(merged)} questions')
