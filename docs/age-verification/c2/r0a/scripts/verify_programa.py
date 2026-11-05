import re,sys
norm=lambda s: re.sub(r'\s+',' ',s).strip()
src=''
for f in sys.argv[2:]:
    t=open(f).read()
    t=re.sub(r'.*(BOLETÍN OFICIAL DEL ESTADO|cve: BOE-A|Verificable en|Núm\. 306 |MINISTERIO|INSTITUTO NACIONAL|ADMINISTRACIÓN P[UÚ]|PARA LA TRANSFORMACIÓN|Y DE LA FUNCIÓN|^\s*SELECCI).*\n','',t,flags=re.M)
    src+=' '+t
src=norm(src).replace('- ','-')
md=open(sys.argv[1]).read()
body=md.split('\n---\n',1)[1]
paras=[norm(p) for p in re.split(r'\n\s*\n',body) if p.strip() and not p.startswith(('#','---','|','(','Fichero','No forman','Del cuerpo','No se incluye','Recuento','- ')) ]
bad=[p for p in paras if p not in src and p.replace('- ','-') not in src]
print(len(paras),'paragraphs;',len(bad),'not found verbatim')
for b in bad: print('  !!',b[:150])
