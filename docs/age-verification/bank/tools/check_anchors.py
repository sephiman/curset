"""Resolve every draft citation to its lesson anchor; print misses. Usage (from backend/): check_anchors.py bloque-ii m02 [out.json]."""
import json, sys
from pathlib import Path
from tradeschool.citations.course import CourseCitations
ROOT = Path('/home/juanjo/PycharmProjects/curset')
course = ROOT / 'content/age-administrativo-c1'
md = {'es': {p.stem: p.read_text() for p in (course / 'es/lessons').glob('*.md')}}
cc = CourseCitations.build(course, 'age-administrativo-c1', md)
D = ROOT / 'docs/age-verification/bank' / sys.argv[1]
out = {}
for f in sorted(D.glob(f'{sys.argv[2]}-l*.draft.json')):
    lesson = f.name.split('.')[0]
    miss = []
    for q in json.loads(f.read_text()):
        a = cc._anchor(lesson, q['citation'], 'es')
        out[q['id']] = a
        if a is None: miss.append(f"{q['id']} «{q['citation']}»")
    print(lesson, 'misses', len(miss), *miss[:60], sep='\n  ' if miss else ' ')
if len(sys.argv) > 3: json.dump(out, open(sys.argv[3], 'w'), indent=0)
