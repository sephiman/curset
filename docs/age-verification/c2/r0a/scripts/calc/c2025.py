from collections import defaultdict
from fractions import Fraction as F
print(45*0.92, 58*1.04, 50*0.36, 616-616*5//8)
print(60*5, 384/4/4/4)
print(F(15,24), F(118,64), F(26,13))
P=[l.split('|') for l in """Aranmanoth|Matute|Barcelona|2000|Destino|5|2|249
Contra Vosotros|Soriano|Madrid|1998|Alfaguara|5|4|114
Mano de sombra|Marías|Madrid|1997|Santillana|7|5|311
Adiós a las novias|Puértolas|Barcelona|1998|Anagrama|14|6|201
La temporada de caza|Camilleri|Barcelona|2000|Anagrama|15|5|154
El equipaje del viajero|Saramago|Madrid|1999|Alfaguara|11|3|248
El amante lesbiano|Sampedro|Barcelona|2000|Plaza & Janés|8|7|130
Entre visillos|Martín Gaite|Barcelona|1998|Destino|10|3|268
Un calor tan cercano|Torres|Madrid|1997|Santillana|15|5|290
Hija de la fortuna|Allende|Barcelona|1999|Plaza & Janés|13|7|206""".split('\n')]
for col,name in ((5,'disp'),(7,'realiz'),(6,'prest')):
  s=defaultdict(int)
  for r in P: s[r[4]]+=int(r[col])
  print(name,dict(s))
print([r[0] for r in P if r[2]=='Barcelona' and int(r[3])>1998 and int(r[5])>10])
print(sorted(((int(r[6])/int(r[5]),r[0]) for r in P),reverse=True))
print(sorted(((int(r[6])/int(r[7]),r[1]) for r in P),reverse=True))
D=[l.split() for l in """A-115 Administración Zaragoza 1 505 40.64
M-254 Marketing Zaragoza 0.5 721 16.60
C-491 Administración Valencia 2 678 10.84
A-115 Marketing Tarragona 1 1425 38.90
M-254 Técnico Bilbao 2 1250 30.40
C-510 Comercial Valencia 3 707 22.34
C-510 Marketing Bilbao 0.5 1388 11.78
M-254 Técnico Málaga 3 962 35.87
C-510 Comercial Tarragona 2 1104 5.97
A-115 Comercial Málaga 2 1541 22.72""".split('\n')]
def agg(k,v,mean=False):
  s=defaultdict(list)
  for r in D: s[r[k]].append(float(r[v]))
  return {a:(sum(b)/len(b) if mean else sum(b)) for a,b in s.items()}
print(agg(2,4)); print(agg(1,3,True)); print(agg(1,5,True))
km=agg(0,4); pe=agg(0,5); print({p:pe[p]/km[p] for p in km})
tot=sum(float(r[4]) for r in D); print(tot, agg(2,4)['Tarragona']/tot*100, km['A-115']/tot*100)
