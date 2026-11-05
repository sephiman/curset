import re, json, sys, pathlib
TXT = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2])
FOOT = re.compile(r'(Página \d+ de \d+|AUX-L|AUX–LI|^\s*\d{4} - AUX)', re.I)
QRE = re.compile(r'^\s{0,9}(\d{1,2})(?:\.\s*|\s{3,})(?!a \d)([¿¡\"“A-ZÁÉÍÓÚÑa-z(].*)$')
ORE = re.compile(r'^\s{0,16}([a-d])\)\s*(.*)$')
def parse(name):
    lines = (TXT/f'{name}.txt').read_text().splitlines()
    start = next(i for i,l in enumerate(lines) if 'PRIMERA PARTE' in l and l.strip()=='PRIMERA PARTE')
    sec = 'P1'; qs=[]; cur=None; ctx=[]; gap=False
    for l in lines[start+1:]:
        s = l.strip()
        if s == 'SEGUNDA PARTE': sec='P2'; cur=None; ctx=[]; continue
        if re.match(r'^Preguntas de reserva', s): sec = 'R1' if sec=='P1' else 'R2'; cur=None; ctx=[]; continue
        if not s: gap=True; continue
        if FOOT.search(l) and len(s)<80 and not QRE.match(l):
            gap=True; continue
        was_gap=gap; gap=False
        parts = [x for x in re.split(r'\s{3,}(?=[a-d]\)\s)', l) if x.strip()]
        if len(parts)>1 and ORE.match(parts[0]):
            for p_ in parts:
                o=ORE.match('  '+p_.strip())
                if cur is not None and o: cur['opts'][o.group(1)]=o.group(2).strip(); last=o.group(1); oind=99
            continue
        m = QRE.match(l); o = ORE.match(l)
        if m and (cur is None or cur['opts'].get('d') is not None or int(m.group(1))==cur['n']+1):
            cur = {'sec':sec,'n':int(m.group(1)),'stem':m.group(2).strip(),'opts':{},'ctx':'\n'.join(ctx)}; ctx=[]; qs.append(cur); last='stem'; continue
        if o and cur is not None and (o.group(1)=='a' and not cur['opts'] or cur['opts'] and chr(ord(max(cur['opts']))+1)==o.group(1)):
            cur['opts'][o.group(1)] = o.group(2).strip(); last=o.group(1); oind=len(l)-len(l.lstrip()); continue
        if cur is not None and len(cur['opts'])==4 and not was_gap and last=='d' and len(l)-len(l.lstrip())>=oind+2 and not QRE.match(l) and not re.search(r'\s{6,}\S', l.strip()):
            cur['opts']['d'] += ' '+s; continue
        if cur is not None and len(cur['opts'])<4:
            if last=='stem': cur['stem'] += ' '+s
            else: cur['opts'][last] += ' '+s
        else:
            ctx.append(l.rstrip())
    return qs
for name in sys.argv[3:]:
    qs = parse(name)
    from collections import Counter
    c = Counter(q['sec'] for q in qs)
    bad = [(q['sec'],q['n']) for q in qs if len(q['opts'])!=4]
    seqerr=[]
    for sec in ['P1','R1','P2','R2']:
        ns=[q['n'] for q in qs if q['sec']==sec]
        if ns!=list(range(1,len(ns)+1)): seqerr.append((sec,ns))
    print(name, dict(c), 'bad_opts', bad, 'seqerr', seqerr)
    (OUT/f'{name}.json').write_text(json.dumps(qs,ensure_ascii=False,indent=1))
