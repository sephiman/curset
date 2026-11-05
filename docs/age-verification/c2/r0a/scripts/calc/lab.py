import csv,sys
from collections import defaultdict
R=list(csv.DictReader(open(sys.argv[1]),delimiter='\t'))
d=defaultdict(int)
for r in R: d[r['Día']]+=int(r['Inscritos'])
print(dict(d))
p=defaultdict(int)
for r in R: p[r['Planta']]+=int(r['Capacidad'])
print(dict(p))
print([(r['Aula'],r['Planta'],r['Inscritos']) for r in R if int(r['Planta'])>2])
print([r['Materia'] for r in R if int(r['Capacidad'])>45 and r['Día'] in('Miércoles','Jueves','Viernes') and r['Planta']=='3'])
print([(r['Profesor'],r['Hora']) for r in R if r['Planta']=='2'])
print([(r['Profesor'],r['Hora'],r['Capacidad']) for r in R if r['Aula']=='2'])
