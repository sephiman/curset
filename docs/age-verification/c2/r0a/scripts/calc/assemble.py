import json,sys,runpy,collections
S=sys.argv[1]
R={}
for f in ('rows1','rows2','rows3','rows4'): R.update(runpy.run_path(f'{S}/calc/{f}.py')['ROWS'])
Q=json.load(open(f'{S}/work/p1_psico.json'))
ids=[q['id'] for q in Q]
print('missing',[i for i in ids if i not in R],'extra',[i for i in R if i not in ids])
out=[]
for q in Q:
  t,st,g,p,rule,c,dif,dn,status,nk,nota=R[q['id']]
  key=q['key'].lower()
  an=key=='anulada'
  if an: assert status=='anulada',q['id']
  m=None if an else c==key
  out.append(dict(id=q['id'],type=t,subtype=st,group=g,params=p,rule=rule,computed=c,matches_key=m,difficulty=dif,difficulty_note=dn,status=status,nota_clave=nk,nota=nota))
  if m is False: print('MISMATCH',q['id'],c,key,status)
json.dump(out,open(f'{S}/work/class_psico.json','w'),ensure_ascii=False,indent=1)
ex=['2025','2024','2024X','2022','2020','2020X']
C=collections.Counter((o['type'],o['id'].split('-P')[0].split('-R')[0]) for o in out)
types=sorted({o['type'] for o in out})
print('type|'+'|'.join(ex)+'|total')
for t in types: print(t+'|'+'|'.join(str(C[(t,e)]) for e in ex)+'|'+str(sum(C[(t,e)] for e in ex)))
print(collections.Counter(o['status'] for o in out))
print(collections.Counter(o['difficulty'] for o in out))
