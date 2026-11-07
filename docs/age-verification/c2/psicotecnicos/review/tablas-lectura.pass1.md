# tablas-lectura — blind review, pass 1 (2026-11-07)

Items read: 50. PASS: 13. FAIL: 37 (generator: 37, bank: 0, other: 0).

Every key was recomputed in Python over the parsed markdown table (exact fractions): all 50 printed keys are correct and unique (each «¿Cuál de los siguientes…?» item has exactly one option passing every condition; no ties at the max/min of any ratio, group sum or filtered column). All FAILs are realism or explanation defects.

## Defects
- G1 (generator): the condition template «tienen <columna> superior/inferior a N» does not agree with plural column names («tienen técnicos superior a 10», «informes emitidos inferior a 111», «viajes al año inferior a 14», «ejemplares disponibles superior a 5»); it is wrong Spanish a candidate notices, and the official stem says «cuenta con más de 10 ejemplares disponibles». Items 1, 2, 7, 10, 11, 15, 17, 18, 19, 21, 22, 24, 25, 26, 27, 32, 34, 38, 46, 47, 48, 50. Suggested fix: phrase numeric conditions as «más de / menos de N <columna>» (or inflect «superiores/inferiores» by the column's number).
- G2 (generator): the sum explanation «Pasan el filtro n filas; sus <columna> suman X» breaks with singular columns («sus distancia suman», «sus presupuesto suman», «sus precio por persona suman»). Items 6, 18, 24, 34. Suggested fix: «la suma de su <columna> es X» or inflect the possessive and the column by number.
- G3 (generator): the operation draws column pairs with no meaning, which no official table asks: cociente «año de publicación / ejemplares prestados» (4) and «ejemplares disponibles / año de publicación» (49), «viajes al año / distancia» (20), «Sumando edad por curso» (28, where the winning «total» is one 27-year-old), «total de precio por persona» (34), and the filter «año de publicación inferior a 2253» (48), a year that cannot exist. Suggested fix: whitelist meaningful ratio and sum columns per table (préstamos/ejemplares, presupuesto/técnicos, coste/viajes…) and draw thresholds inside the column's range.
- G4 (generator): the ratio explanation rounds the winning quotient to 2 decimals, so item 49 prints «(0,00)», which teaches nothing and looks like an error. Suggested fix: print enough significant figures, or skip the number when it rounds to 0.
- G5 (generator): item 24 is labelled nivel 3 but is a two-condition filter with two rows passing and a sum of two three-digit numbers (364 + 503); the index reserves nivel 3 for close ratios. Suggested fix: level filter-and-sum items by rows passing and closeness of distractors, not above 2 for this shape.
- G6 (generator): the tables are built from independent random columns, which produces situations a candidate notices: every «Excursiones» table sends groups «en Barco» to inland towns (Teruel, Toledo, Jaca, Ávila, Úbeda, Soria, León, Mérida, Lugo, Ronda), and every «Desplazamientos» table has buses and cars at 250–500 km/h (e.g. 846 km en autobús en 198 min; 536 km en autobús en 103 min). Items 1, 5, 12, 16, 34, 35, 37, 38, 44 (Excursiones) and 3, 6, 9, 19, 20, 24, 27, 30, 41, 46 (Desplazamientos). Suggested fix: restrict «Barco» to coastal or island destinations (or replace it), and derive Tiempo from Distancia with a speed band per Medio.

Advisory, not counted as FAIL:
- A1: count and filter-and-sum explanations give only the number («Cumplen las condiciones … exactamente 3», «Pasan el filtro 2 filas») without naming the rows; a candidate who erred cannot see which row they mis-read. Naming the passing rows would teach more.
- A2: the mean explanations print the integer column sum with decimals («La suma de la columna es 182,00»); «182» is the natural form.

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 274797139979144773 | FAIL | generator (G1, G6) | key 3 recomputed; «<plural> superior/inferior a»; implausible table |
| 2 | 3493489528897654557 | FAIL | generator (G1) | key 18 (Beta 8 + Gamma 10); «<plural> superior/inferior a» |
| 3 | 3888289725752918728 | FAIL | generator (G6) | key Lucía Costa, only option passing; implausible table |
| 4 | 679292652377546788 | FAIL | generator (G3) | key Mano de sombra 2002/4=500,5; meaningless quantity |
| 5 | 2618344893097292910 | FAIL | generator (G6) | key 303 (Ronda 225 + León 78); implausible table |
| 6 | 995660733233502469 | FAIL | generator (G2, G6) | key 1043 (3 rows); «sus <singular> suman»; implausible table |
| 7 | 1223983771725134866 | FAIL | generator (G1) | key Óscar Lara, only option passing; «<plural> superior/inferior a» |
| 8 | 4580581082989247247 | PASS | | key Kappa 77/23=3,35; next Sigma 6,33 |
| 9 | 3910380554785824084 | FAIL | generator (G6) | key 2; implausible table |
| 10 | 4441628925242482318 | FAIL | generator (G1) | key Delta 358 among 5 filtered; «<plural> superior/inferior a» |
| 11 | 2446871128147784257 | FAIL | generator (G1) | key Zeta 148 among 5 filtered; «<plural> superior/inferior a» |
| 12 | 3654112830433712182 | FAIL | generator (G6) | key Ronda, only option passing; implausible table |
| 13 | 327284621952842892 | PASS | | key 182/11=16,545 → 16,55 |
| 14 | 3262813409570128271 | PASS | | key Sigma 0,954; next Delta 0,344 |
| 15 | 1574408861979755188 | FAIL | generator (G1) | key Alfa, only option passing; «<plural> superior/inferior a» |
| 16 | 2074564667347024303 | FAIL | generator (G6) | key Cuenca, only option passing; implausible table |
| 17 | 1580329207806355028 | FAIL | generator (G1) | key Épsilon, only option passing; «<plural> superior/inferior a» |
| 18 | 4157976482641714332 | FAIL | generator (G1, G2) | key 391 (Iota + Zeta); «<plural> superior/inferior a»; «sus <singular> suman» |
| 19 | 345352013983549247 | FAIL | generator (G1, G6) | key 3; «<plural> superior/inferior a»; implausible table |
| 20 | 3725810980475735155 | FAIL | generator (G3, G6) | key Óscar Lara 0,0375; meaningless quantity; implausible table |
| 21 | 3689692058427482923 | FAIL | generator (G1) | key Irene Pons, only option passing; «<plural> superior/inferior a» |
| 22 | 549857973036573262 | FAIL | generator (G1) | key 2; «<plural> superior/inferior a» |
| 23 | 3911690445701389361 | PASS | | key 2 |
| 24 | 4092711762427273095 | FAIL | generator (G1, G2, G5, G6) | key 867 (364+503); «<plural> superior/inferior a»; «sus <singular> suman»; nivel 3 for a 2-row sum; implausible table |
| 25 | 2736979108388417725 | FAIL | generator (G1) | key 3; «<plural> superior/inferior a» |
| 26 | 4163390447536696390 | FAIL | generator (G1) | key 2; «<plural> superior/inferior a» |
| 27 | 1586508015396871889 | FAIL | generator (G1, G6) | key Óscar Lara, only option passing; «<plural> superior/inferior a»; implausible table |
| 28 | 3588842099432019975 | FAIL | generator (G3) | key Alemán 27 (one student); meaningless quantity |
| 29 | 4110580552696902388 | PASS | | key Planeta 14; Santillana 13 |
| 30 | 3556477018594785593 | FAIL | generator (G6) | key Hugo Beltrán 11 among 4; implausible table |
| 31 | 2381850757681049524 | PASS | | key Nuria Salas 61; next Iván Duarte 42,5 |
| 32 | 3706174181096166754 | FAIL | generator (G1) | key Mano de sombra 4 among 3; «<plural> superior/inferior a» |
| 33 | 3614112383633376201 | PASS | | key Zeta 39; next Sigma 32 |
| 34 | 1166747531291222478 | FAIL | generator (G1, G2, G3, G6) | key 200 (4 rows); «<plural> superior/inferior a»; «sus <singular> suman»; meaningless quantity; implausible table |
| 35 | 1690837818924781736 | FAIL | generator (G6) | key 3; implausible table |
| 36 | 3525112190121478594 | PASS | | key Lambda 1,957; next Alfa 1,03 |
| 37 | 778671632053513995 | FAIL | generator (G6) | key Soria 40 among 4 Barco rows; implausible table |
| 38 | 232616239795612045 | FAIL | generator (G1, G6) | key Mérida, only option passing; «<plural> superior/inferior a»; implausible table |
| 39 | 1177092152084991428 | PASS | | key Gamma 0,80; next Zeta 2,80 |
| 40 | 2300311533501968391 | PASS | | key Theta 0,060; next Gamma 0,075 |
| 41 | 4561429966377530467 | FAIL | generator (G6) | key 4396/12=366,33; implausible table |
| 42 | 279218220529479154 | PASS | | key Kappa 7,19; next Sigma 4,54 |
| 43 | 2042550028401227693 | PASS | | key Delta 2,13; next Omega 1,63 |
| 44 | 1065444377732371285 | FAIL | generator (G6) | key 543/3272=16,595 → 16,60 %; implausible table |
| 45 | 2719097753412396217 | PASS | | key Barcelona 72 |
| 46 | 3969796563389545576 | FAIL | generator (G1, G6) | key Andrés Peña, only option passing; «<plural> superior/inferior a»; implausible table |
| 47 | 2439017718913394027 | FAIL | generator (G1) | key Iván Duarte, only option passing; «<plural> superior/inferior a» |
| 48 | 2169652614732583283 | FAIL | generator (G1, G3) | key Adiós a las novias, only option passing; «<plural> superior/inferior a»; meaningless quantity |
| 49 | 4533545574814537803 | FAIL | generator (G3, G4) | key La casa del lago 4/1996; next El jardín cerrado 5/2004; meaningless quantity; explanation «(0,00)» |
| 50 | 3814695743816065413 | FAIL | generator (G1) | key 2; «<plural> superior/inferior a» |
