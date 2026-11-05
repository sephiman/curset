import re, json, sys, pathlib
TXT = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2])
TOK = re.compile(r'(?<!\S)(\d{1,2})\.\s+((?:ANULADA|Anulada|[A-Da-d]\b)(?: {1,2}\S+)*)')
HDR = re.compile(r'(Primera parte|Segunda parte|Preguntas de reserva|Reserva)', re.I)
def parse(name):
    lines = (TXT/f'{name}.txt').read_text().splitlines()
    items=[]  # (col_x, line_no, kind, payload)
    for i,l in enumerate(lines):
        for m in HDR.finditer(l):
            if 'PLANTILLA' in l.upper(): continue
            items.append((m.start(), i, 'H', m.group(1).lower()))
        for m in TOK.finditer(l):
            items.append((m.start(), i, 'K', (int(m.group(1)), m.group(2).strip())))
    xs = sorted(set(x for x,*_ in items)); cols=[]
    for x in xs:
        if cols and x-cols[-1][-1] <= 12: cols[-1].append(x)
        else: cols.append([x])
    colof = {x:ci for ci,c in enumerate(cols) for x in c}
    state='P1'; keys={}; dup=[]
    for ci in range(len(cols)):
        for x,i,k,p in sorted([t for t in items if colof[t[0]]==ci], key=lambda t:t[1]):
            if k=='H':
                if p=='primera parte': state='P1'
                elif p=='segunda parte': state='P2'
                else: state = 'R1' if state in ('P1','R1') else 'R2'
            else:
                key=(state,p[0])
                if key in keys: dup.append(key)
                keys[key]=p[1]
    return keys, dup
for name in sys.argv[3:]:
    keys,dup = parse(name)
    from collections import Counter
    c=Counter(s for s,_ in keys)
    odd={f'{s}{n}':v for (s,n),v in keys.items() if v.lower() not in 'abcd'}
    miss=[(s,n) for s,N in [('P1',60),('R1',5),('P2',50),('R2',5)] for n in range(1,N+1) if (s,n) not in keys]
    print(name, dict(c), 'dup',dup, 'missing',miss, 'nonletter',odd)
    (OUT/f'{name}.json').write_text(json.dumps({f'{s}.{n}':v for (s,n),v in sorted(keys.items())},ensure_ascii=False,indent=0))
