print(-110/21, 300/43*12, 122*6+89*3+137*5, 60/46, 108/26)
D=[l.split('|') for l in """Diccionario biográfico americano|1876|Facsímil|Dic|Sí|Media|T|Terminada
Breve diccionario valenciano|1739|Libro|Dic|Sí|Baja|P|En proceso
Carácter convencional|2006|Documento|Ret|No|Alta|T|Aprobada
Diccionario Castellano-Valenciano|1839|Libro|Dic|No|Media|P|Aprobada
Diccionario histórico abreviado|1753|Manuscrito|Dic|Sí|Alta|T|En espera
Dictionarium|1581|Facsímil|Dic|No|Media|T|En proceso
El Lenguaje poético|2011|Documento|Ret|No|Alta|P|Aprobada
Manual de retórica|1848|Manuscrito|Ret|Sí|Baja|T|Terminada
Oratoria sacra|1772|Facsímil|Ret|Sí|Alta|T|Terminada
Rhetorica|1752|Facsímil|Ret|Sí|Baja|P|En espera""".split('\n')]
print(46,[r[0] for r in D if r[3]=='Dic' and r[6]=='T'])
print(47,[r[0] for r in D if 1701<=int(r[1])<=1800 and r[4]=='Sí' and r[2]=='Facsímil'])
print(48,[r[1] for r in D if r[2]=='Facsímil' and r[4]=='Sí' and r[6]=='T' and r[3]=='Ret'])
print(49,[r[1] for r in D if r[3]=='Dic' and r[2]!='Libro' and r[5]=='Media' and r[7]=='En proceso'])
print(50,[r[0] for r in D if r[2]=='Facsímil' and r[5]=='Media' and r[7]=='Terminada'])
print(51,[(r[1],r[2]) for r in D if 1801<=int(r[1])<=1900 and r[3]=='Dic' and r[4]=='No'])
E={}
for l in """Marzo 5785 482 231 317
Abril 5935 421 111 209
Mayo 5739 368 164 217
Junio 7465 409 227 129
Julio 7630 585 275 341
Agosto 6102 567 183 326
Septiembre 5817 346 184 125
Octubre 6028 305 132 138
Noviembre 5699 298 169 224
Diciembre 6420 256 158 253""".split('\n'):
  m,*v=l.split(); E[m]=list(map(int,v))
print(55,{m:round(v[0]/v[1],2) for m,v in E.items()})
print(56,{m:round(v[0]/sum(v[1:]),3) for m,v in E.items()})
print(57,{m:round(v[3]/sum(v[1:])*100,2) for m,v in E.items()})
print(58,{m:sum(v[1:]) for m,v in E.items()})
T=sum(v[0] for v in E.values()); print(59,{m:round(v[0]/T*100,2) for m,v in E.items()})
print(60,T/10)
