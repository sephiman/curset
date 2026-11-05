import json,re,sys,difflib
def load(q,k):
    qs=json.load(open(f'parsed/{q}.json')); ks=json.load(open(f'keys/{k}.json'))
    for x in qs: x['key']=ks[f"{x['sec']}.{x['n']}"]
    return qs
norm=lambda s: re.sub(r'\W+',' ',s.lower()).strip()
for y,qa,ka,qb,kb in [('2025','2026-05-23_conv2025_modeloA_cuestionario','2026-05-23_conv2025_modeloA_plantilla-definitiva','2026-05-23_conv2025_modeloB_cuestionario','2026-05-23_conv2025_modeloB_plantilla-definitiva'),('2024','conv2024_modeloA_cuestionario','conv2024_modeloA_plantilla-definitiva','conv2024_modeloB_cuestionario','conv2024_modeloB_plantilla-definitiva')]:
    A=load(qa,ka); B=load(qb,kb); mp={}; probs=[]
    for a in A:
        cands=[b for b in B if b['sec']==a['sec']]
        best=max(cands,key=lambda b: difflib.SequenceMatcher(None,norm(a['stem']+' '.join(a['opts'].values())),norm(b['stem']+' '.join(b['opts'].values()))).ratio())
        r=difflib.SequenceMatcher(None,norm(a['stem']+' '.join(a['opts'].values())),norm(best['stem']+' '.join(best['opts'].values()))).ratio()
        ka_=a['key']; kb_=best['key']
        ta=a['opts'].get(ka_.lower(),ka_); tb=best['opts'].get(kb_.lower(),kb_)
        same = norm(ta)==norm(tb)
        mp[f"{a['sec']}.{a['n']}"]=f"{best['sec']}.{best['n']}"
        if r<0.9 or not same: probs.append((a['sec'],a['n'],best['n'],round(r,2),ka_,kb_,ta[:50],tb[:50]))
    vals=list(mp.values()); print(y,'mapped',len(mp),'unique',len(set(vals)),'probs',len(probs))
    for p in probs: print('  ',p)
    json.dump(mp,open(f'work/ab_{y}.json','w'))
