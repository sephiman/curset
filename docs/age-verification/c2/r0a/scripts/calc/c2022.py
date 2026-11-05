import itertools
from fractions import Fraction as F
print(-18/52, 980*.2/1000*1600, (1-F(1,2)-F(1,3)-F(1,9))*100*1.0, 15990*.3, 18*3, 3*(6*4+2*6))
def ev(nums,ops):
  e=str(nums[0])
  for o,n in zip(ops,nums[1:]): e+=o+str(n)
  return e,eval(e)
for ops in ['-++','+-+','+++','++-']: print(ev([43,33,12,54],ops))
for ops in ['++*','-*+','*-+','*--']: print(ev([17,13,11,8],ops))
P=[l.split('|') for l in """M1|1|Comercial|Charla|Pdf|41|4
M1|2|Contabilidad|Mesa redonda|Word|52|17
M2|1|RRHH|Charla|Cd|48|6
M2|3|Administración|Laboratorio|Cd|41|2
M3|3|Comercial|Laboratorio|Pdf|42|11
T1|1|Administración|Charla|Pdf|56|13
T1|2|Contabilidad|Laboratorio|Cd|39|9
T2|1|Comercial|Laboratorio|Pdf|48|2
T2|3|RRHH|Laboratorio|Cd|51|5
T3|3|Administración|Charla|Pdf|43|5
T3|2|Contabilidad|Mesa redonda|Word|54|15
T3|1|Comercial|Charla|Pdf|37|3""".split('\n')]
for r in P: r[5]=int(r[5]); r[6]=int(r[6])
print('49',[r[5]/r[6] for r in P if r[0]=='T2' and r[2]=='Comercial'])
print('50',sum(r[6] for r in P if r[0][1]=='2' and r[2]=='RRHH' and r[4]=='Cd'))
print('51',sum(r[5]+r[6] for r in P if r[0][0]=='T' and r[1]=='1' and r[4]=='Pdf'))
print('52',min(r[5]+r[6] for r in P if r[0][0]=='T' and r[3]=='Charla'),min(r[5] for r in P if r[0][0]=='T' and r[3]=='Charla'))
print('53',sum(r[5]+r[6] for r in P if r[0][1]=='2' and r[3]=='Laboratorio' and r[2]!='RRHH'))
print('54',sum(r[5]+r[6] for r in P if r[0][0]=='T' and r[1]=='1'), sum(r[5] for r in P if r[0][0]=='T' and r[1]=='1'))
FL={}
for l in """Margarita|blanco amarillo|3|2|2|2|3|NO|SI|NO|SI|SI
Rosa|blanco amarillo rosa|6|4|5|4|2|NO|NO|SI|SI|SI
Clavel|amarillo rosa|3 6|3|1|6|5|SI|NO|NO|NO|NO
Salvia|rosa|3 6 12|1|6|3|2|SI|SI|SI|SI|NO
Crisantemo|blanco rosa|3 6 12|4|4|8|5|NO|NO|SI|SI|NO
Tulipán|amarillo|3 6 12|5|5|5|4|SI|SI|NO|NO|SI
Cardo|blanco|3|4|1|4|5|NO|NO|SI|SI|NO
Lirio|blanco amarillo|6|3|5|6|4|SI|NO|NO|NO|SI
Orquídea|blanco rosa|3 6 12|4|6|8|3|NO|SI|SI|SI|NO
Gerbera|amarillo rosa|3 6|5|1|7|5|SI|NO|SI|SI|NO""".split('\n'):
  f=l.split('|'); FL[f[0]]=dict(col=f[1].split(),ramos=f[2].split(),pet=int(f[3]),peso=int(f[4]),est=int(f[5]),pr=int(f[6]),frag=f[7]=='SI',dom=f[8]=='SI',peq=f[9]=='SI',promo=f[10]=='SI',dur=f[11]=='SI')
print('55',[k for k,v in FL.items() if 'rosa' in v['col'] and v['dom'] and '6' in v['ramos']])
print('56',[k for k,v in FL.items() if v['frag'] and '12' in v['ramos'] and v['peq']])
print('57',[k for k,v in FL.items() if v['pet']>2 and v['promo'] and not v['dur']])
print('58',sum(v['est'] for v in FL.values() if 'blanco' in v['col'] and not v['dom']),[k for k,v in FL.items() if 'blanco' in v['col'] and not v['dom']])
print('59',sorted((v['pr'],k) for k,v in FL.items() if v['peq'] and not v['frag']))
print('60',[k for k,v in FL.items() if v['peq'] and 'rosa' in v['col'] and not v['dur'] and v['pet']>3 and v['pr']<5])
print('R5',(2100-995)/85*2)
