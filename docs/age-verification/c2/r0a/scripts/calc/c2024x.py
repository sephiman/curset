print(-58/11, (47034632-1887689)/47034632*100, 832/89, 4*(7*2.4+4*16.3), 2840/8*2, 975/65)
T={'Enero':(6521,321,245,7,201),'Febrero':(5364,290,255,8,603),'Marzo':(5287,267,232,6,103),'Abril':(6002,241,241,9,497),'Mayo':(5781,222,187,15,417),'Junio':(3057,175,97,12,300),'Julio':(3825,152,88,11,300)}
print(sum(v[4] for v in T.values())/7)
print({m:round(v[1]/v[0]*100,3) for m,v in T.items()})
print(300*(1-.62))
print({m:round(v[4]/v[0]*100,3) for m,v in T.items()})
print({m:v[0]-v[1]-v[2]-v[3] for m,v in T.items()})
print({m:round(v[2]/v[0]*100,3) for m,v in T.items()})
