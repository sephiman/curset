"""Covers codes (lmc lines, official questions) that some draft question claimed but no kept question still does.

Usage: lost_coverage.py bloque-iii m03-l06 [m03-l07 …]; part drafts of a lesson are read with it.
"""
import csv
import json
import sys
from pathlib import Path

D = Path(__file__).resolve().parents[1] / sys.argv[1]
drops = {r['id'] for r in csv.DictReader(open(D / 'drops.tsv'), delimiter='\t')}
for lesson in sys.argv[2:]:
    files = sorted(D.glob(f'{lesson}.part-*.draft.json')) or [D / f'{lesson}.draft.json']
    qs = [q for f in files for q in json.loads(f.read_text())]
    claimed = {c for q in qs for c in q.get('covers', [])}
    kept = {c for q in qs if q['id'] not in drops for c in q.get('covers', [])}
    lost = sorted(claimed - kept)
    print(f"{lesson}: lost {len(lost)}", *[f"{c} ← {[q['id'] for q in qs if c in q.get('covers', [])]}" for c in lost], sep='\n  ')
