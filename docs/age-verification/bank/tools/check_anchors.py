"""Resolve every draft citation to its lesson anchor with the platform's resolver; print misses and write anchors."""
import json, sys
from pathlib import Path
from tradeschool.citations.course import CourseCitations
ROOT = Path('/home/juanjo/PycharmProjects/curset')
course = ROOT / 'content/age-administrativo-c1'
md = {'es': {p.stem: p.read_text() for p in (course / 'es/lessons').glob('*.md')}}
cc = CourseCitations.build(course, 'age-administrativo-c1', md)
D = ROOT / 'docs/age-verification/bank/bloque-i'
out = {}
for f in sorted(D.glob('m01-l*.draft.json')):
    lesson = f.name.split('.')[0]
    miss = []
    for q in json.loads(f.read_text()):
        a = cc._anchor(lesson, q['citation'], 'es')
        out[q['id']] = a
        if a is None: miss.append(f"{q['id']} «{q['citation']}»")
    print(lesson, 'misses', len(miss), *miss[:60], sep='\n  ' if miss else ' ')
json.dump(out, open(sys.argv[1], 'w'), indent=0)
