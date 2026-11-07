# tablas-lectura — blind review, pass 4 (2026-11-07)

Items read: 50. PASS: 50. FAIL: 0 (generator: 0, bank: 0, other: 0).

Every key recomputed in Python from the markdown rows (exact fractions for ratios, means and percentages): 50 of 50 match, and in every item the key is the only option that fits (single passing row in the «cuál de los siguientes» items; no ties at the top in the max/min items; percentages and means unambiguous at 2 decimals).

## Defects

None that fail an item.

Remarks (not FAILs):
- N1: count and filter-sum explanations («Pasan el filtro 3 filas; en ellas, la columna … suma 40», «Cumplen las condiciones (…) exactamente 2») do not name the passing rows, so a candidate who included a wrong row cannot see which one; naming them (e.g. «Lugo 14 + Toledo 5 + Jaca 21 = 40») would teach better.
- N2: the mean template prints an integer sum with decimals («La suma de la columna es 56,00»; item 13, 49); «56» reads more naturally.
- N3: stem template «el total de duración / de cuota mensual» is slightly stiff next to «la duración total»; acceptable.

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 274797139979144773 | PASS | | filtro y suma: recomputed 40, key a only fit |
| 2 | 3493489528897654557 | PASS | | filtro y suma: recomputed 21, key c only fit |
| 3 | 3888289725752918728 | PASS | | cociente por fila: recomputed Diego Rubio, key c only fit; 1,18 vs next option Rocío Mora 1,75 |
| 4 | 679292652377546788 | PASS | | recuento: recomputed 2, key c only fit |
| 5 | 2618344893097292910 | PASS | | recuento: recomputed 3, key c only fit |
| 6 | 995660733233502469 | PASS | | suma por grupo: recomputed Inglés, key d only fit |
| 7 | 1223983771725134866 | PASS | | cociente por fila: recomputed Pablo Vera, key a only fit |
| 8 | 4580581082989247247 | PASS | | cociente por fila: recomputed Marta Ríos, key c only fit |
| 9 | 3910380554785824084 | PASS | | filtro y máx/mín: recomputed León, key d only fit |
| 10 | 4441628925242482318 | PASS | | filtro, fila única: recomputed Ana Cortés, key c only fit |
| 11 | 2446871128147784257 | PASS | | recuento: recomputed 2, key c only fit |
| 12 | 3654112830433712182 | PASS | | filtro y máx/mín: recomputed Diego Rubio, key b only fit |
| 13 | 327284621952842892 | PASS | | media de columna: recomputed 5,09, key a only fit; 56/11; 5,60 is the /10 slip |
| 14 | 3262813409570128271 | PASS | | filtro, fila única: recomputed Omega, key d only fit |
| 15 | 1574408861979755188 | PASS | | filtro, fila única: recomputed Lugo, key c only fit |
| 16 | 2074564667347024303 | PASS | | filtro, fila única: recomputed Carla Nieto, key b only fit |
| 17 | 1580329207806355028 | PASS | | filtro, fila única: recomputed Sara Ortiz, key c only fit |
| 18 | 4157976482641714332 | PASS | | recuento: recomputed 2, key b only fit |
| 19 | 345352013983549247 | PASS | | filtro y suma: recomputed 495, key b only fit |
| 20 | 3725810980475735155 | PASS | | filtro, fila única: recomputed Diego Rubio, key a only fit |
| 21 | 3689692058427482923 | PASS | | recuento: recomputed 3, key b only fit |
| 22 | 549857973036573262 | PASS | | filtro, fila única: recomputed Aranmanoth, key d only fit; Valencia+Santillana already unique |
| 23 | 3911690445701389361 | PASS | | recuento: recomputed 2, key c only fit |
| 24 | 4092711762427273095 | PASS | | porcentaje de grupo: recomputed 26,92 %, key a only fit; 28/104 |
| 25 | 2736979108388417725 | PASS | | filtro y suma: recomputed 16, key b only fit |
| 26 | 4163390447536696390 | PASS | | filtro y máx/mín: recomputed Diego Rubio, key b only fit; tie 89 only for second place |
| 27 | 1586508015396871889 | PASS | | cociente por fila: recomputed Alfa, key a only fit |
| 28 | 3588842099432019975 | PASS | | suma por grupo: recomputed Sevilla, key a only fit |
| 29 | 4110580552696902388 | PASS | | recuento: recomputed 2, key d only fit |
| 30 | 3556477018594785593 | PASS | | recuento: recomputed 2, key c only fit |
| 31 | 2381850757681049524 | PASS | | filtro, fila única: recomputed León, key b only fit |
| 32 | 3706174181096166754 | PASS | | cociente por fila: recomputed Carla Nieto, key d only fit; 1/12; next option 0,44 |
| 33 | 3614112383633376201 | PASS | | filtro, fila única: recomputed Marta Ríos, key b only fit |
| 34 | 1166747531291222478 | PASS | | recuento: recomputed 4, key b only fit |
| 35 | 1690837818924781736 | PASS | | recuento: recomputed 2, key a only fit |
| 36 | 3525112190121478594 | PASS | | filtro, fila única: recomputed Delta, key c only fit |
| 37 | 778671632053513995 | PASS | | recuento: recomputed 2, key a only fit |
| 38 | 232616239795612045 | PASS | | filtro y máx/mín: recomputed Irene Pons, key d only fit |
| 39 | 1177092152084991428 | PASS | | filtro, fila única: recomputed Sigma, key a only fit |
| 40 | 2300311533501968391 | PASS | | recuento: recomputed 3, key b only fit |
| 41 | 4561429966377530467 | PASS | | porcentaje de grupo: recomputed 57,59 %, key b only fit; 937/1.627; 42,41 is the complement |
| 42 | 279218220529479154 | PASS | | filtro, fila única: recomputed Omega, key c only fit |
| 43 | 2042550028401227693 | PASS | | recuento: recomputed 2, key a only fit |
| 44 | 1065444377732371285 | PASS | | porcentaje de grupo: recomputed 15,97 %, key c only fit; 913/5.717 |
| 45 | 2719097753412396217 | PASS | | filtro y suma: recomputed 60, key a only fit |
| 46 | 3969796563389545576 | PASS | | filtro y suma: recomputed 20, key b only fit |
| 47 | 2439017718913394027 | PASS | | filtro y suma: recomputed 205, key c only fit |
| 48 | 2169652614732583283 | PASS | | recuento: recomputed 2, key c only fit |
| 49 | 4533545574814537803 | PASS | | media de columna: recomputed 37,73, key b only fit; 415/11; 41,50 is the /10 slip |
| 50 | 3814695743816065413 | PASS | | filtro y suma: recomputed 598, key d only fit |
