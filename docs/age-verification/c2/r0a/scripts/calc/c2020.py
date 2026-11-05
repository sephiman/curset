R=[l.split('|') for l in """Nueva York|reuniones|M|6|No|No|8|15|Est
Tokio|reuniones|T|17|Proyector|Sí|12|45|Est
Tijuana|reuniones|M|26|Proyector y Megafonía|Sí|12|50|Eje
Dubái|reuniones|M|28|Megafonía|No|13|52|Eje
Madrid|clases|MT|9|Proyector|No|3|25|Est
Las Vegas|reuniones|MT|10|No|No|14|28|Est
Múnich|clases|T|13|Proyector|No|7|30|Est
Seúl|clases|MT|22|Proyector|No|15|48|Eje
Londres|clases|MT|30|Proyector|Sí|30|53|Eje
Barcelona|reuniones|T|18|Proyector y Megafonía|Sí|7|47|Eje""".split('\n')]
for r in R: r[3]=int(r[3]); r[6]=int(r[6]); r[7]=int(r[7])
pj=lambda r:'Proyector' in r[4]
print(31,[r[0] for r in R if pj(r) and r[8]=='Est' and r[5]=='Sí'])
print(32,[r[0] for r in R if 'M' in r[2] and r[3]>15 and r[6]>=r[3]])
print(33,[(r[0],r[7]) for r in R if pj(r) and r[8]=='Eje' and 'T' in r[2]])
print(34,[(r[0],r[3]) for r in R if r[1]=='clases' and pj(r) and 'M' in r[2]])
x=[r[3] for r in R if pj(r) and r[5]=='Sí' and r[8]=='Eje']; print(35,x,sum(x)/len(x))
print(36,[r[0] for r in R if r[1]=='reuniones' and r[5]=='No' and 'M' in r[2] and r[8]=='Est'])
A={}
for l in """Enero 7150 407 531 843
Febrero 5860 367 498 802
Marzo 4865 320 462 732
Abril 6108 323 528 835
Mayo 5744 289 429 654
Junio 4500 220 405 539
Septiembre 6540 186 620 800
Octubre 8390 189 587 738
Noviembre 9120 194 553 720
Diciembre 9640 158 560 698""".split('\n'):
  m,*v=l.split(); A[m]=list(map(int,v))
print(44,{m:round(v[1]/(v[1]+v[2])*100,2) for m,v in A.items()})
print(45,{m:round(v[3]/(v[1]+v[2]),4) for m,v in A.items()})
print(46,{m:round(v[0]/(v[1]+v[2]),3) for m,v in A.items()})
print(47,{m:v[1]+v[2] for m,v in A.items()})
ad=sum(v[2] for v in A.values()); print(49,ad,ad*.62)
print(136/17*8, 85/25*41, -50/74, -192/63)
