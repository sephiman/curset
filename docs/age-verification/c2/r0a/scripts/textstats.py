import json,re,statistics as st
M=json.load(open('work/master.json'))
EX=['2025','2024','2024X','2022','2020','2020X']
NEG=re.compile(r'\b(NO|FALSA|INCORRECTA|INCORRECTO|EXCEPTO|FALSO)\b|\bno es\b|\bno se\b|\bno corresponde|\bno forma|\bno podrá|\bno será|\bno está|\bno tiene',re.I)
NEGCAP=re.compile(r'\b(NO|FALSA|INCORRECTA|INCORRECTO|EXCEPTO|FALSO)\b')
w=lambda s: len(s.split())
def stats(qs):
    keyed=[q for q in qs if q['key'].lower() in 'abcd']
    d={'Questions':len(qs),
       'Negative stems (capitals: NO, FALSA, INCORRECTA, EXCEPTO)':sum(bool(NEGCAP.search(q['stem'])) for q in qs),
       'Stems naming an article':sum(bool(re.search(r'\bart[íi]culo\s+\d|\bart\.\s*\d',q['stem'],re.I)) for q in qs),
       'Stems naming a norm':sum(bool(re.search(r'\b(Ley|Real Decreto|Reglamento|Constitución|Orden|TREBEP|LGP|CE|Resolución|Tratado)\b',q['stem'])) for q in qs),
       'Options «Ninguna…» (keyed)':f"{sum(any(re.match(r'ninguna',o,re.I) for o in q['opts'].values()) for q in qs)} ({sum(re.match(r'ninguna',q['opts'].get(q['key'].lower(),''),re.I) is not None for q in keyed)})",
       'Options «Todas…» (keyed)':f"{sum(any(re.match(r'todas',o,re.I) for o in q['opts'].values()) for q in qs)} ({sum(re.match(r'todas',q['opts'].get(q['key'].lower(),''),re.I) is not None for q in keyed)})",
       'Stem words, mean / median':f"{round(st.mean(w(q['stem']) for q in qs))} / {round(st.median(w(q['stem']) for q in qs))}",
       'Option words, mean / median':f"{round(st.mean(w(o) for q in qs for o in q['opts'].values()))} / {round(st.median(w(o) for q in qs for o in q['opts'].values()))}",
       'Keyed option is the longest':f"{sum(w(q['opts'][q['key'].lower()])==max(w(o) for o in q['opts'].values()) and list(map(w,q['opts'].values())).count(max(w(o) for o in q['opts'].values()))==1 for q in keyed)} ({round(100*sum(w(q['opts'][q['key'].lower()])==max(w(o) for o in q['opts'].values()) and list(map(w,q['opts'].values())).count(max(w(o) for o in q['opts'].values()))==1 for q in keyed)/max(1,len(keyed)))}%)",
       'Key a / b / c / d / anulada':'/'.join(str(sum(q['key'].lower()==k for q in qs)) for k in 'abcd')+'/'+str(len(qs)-len(keyed)),
    }
    return d
out={}
for part,f in [('bloque I',lambda q:q['kind']=='conocimiento'),('psicotécnico',lambda q:q['kind']=='psicotecnico'),('bloque II',lambda q:q['kind']=='bloque II')]:
    out[part]={e:stats([q for q in M if q['exam']==e and f(q)]) for e in EX}
json.dump(out,open('work/textstats.json','w'),ensure_ascii=False,indent=1)
for part,v in out.items():
    print('##',part)
    keys=list(v['2025'])
    print('| Measure | '+' | '.join(EX)+' |')
    for k in keys: print('| '+k+' | '+' | '.join(str(v[e][k]) for e in EX)+' |')
