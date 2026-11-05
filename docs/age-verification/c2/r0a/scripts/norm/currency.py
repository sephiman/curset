import yaml,json,re,subprocess,sys,time
sys.path.insert(0,'.')
from c2sel import SEL, NEW
C1='/home/juanjo/PycharmProjects/curset/content/age-administrativo-c1/sources/normativa.yaml'
d=yaml.safe_load(open(C1)); by={e['short']:e for e in d}
miss=[s for s in SEL if s not in by]; print('missing in C1:',miss)
ids=[by[s]['boe_id'] for s in SEL if by[s].get('boe_id')]+[n['boe_id'] for n in NEW]
out={}
for i in ids:
    h=subprocess.run(['curl','-s','-A','Mozilla/5.0 (X11; Linux x86_64) curset-sources-check',f'https://www.boe.es/buscar/act.php?id={i}'],capture_output=True,text=True).stdout
    m=re.search(r'Última actualización publicada el (\d\d)/(\d\d)/(\d{4})',h)
    pub=re.search(r'Publicado en:.*?(\d\d)/(\d\d)/(\d{4})',h,re.S)
    out[i]={'ultima':f'{m.group(3)}-{m.group(2)}-{m.group(1)}' if m else None,'http_len':len(h),'notfound':'no se ha encontrado' in h.lower() or len(h)<5000}
    time.sleep(0.3)
json.dump(out,open('currency.json','w'),indent=1)
for s in SEL:
    e=by[s]; i=e.get('boe_id')
    if not i: continue
    c=out[i]; flag='' if c['ultima']==e['consolidated_as_of'] else '  <<< CHANGED' if c['ultima'] else '  (no line)'
    if flag: print(i,s[:45],'C1:',e['consolidated_as_of'],'now:',c['ultima'],flag)
for n in NEW: print(n['boe_id'],out[n['boe_id']])
