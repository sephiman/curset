# tablas-lectura — blind review, pass 3 (2026-11-07)

Items read: 50. PASS: 47. FAIL: 3 (generator: 3, bank: 0, other: 0).

Every table was parsed from the markdown rows and every key recomputed in Python (exact fractions for ratios, means and shares). All 50 printed keys are the only option that matches; every count of rows, group sum, ratio and share quoted in the explanations is right; no ratio, group-sum or filtered max/min has a tie at the top; no condition is vacuous (each one removes at least one row); every name option is a row of its table.

## Defects
- G1 (generator): the share stem drops the article before the group value — «¿Qué porcentaje del total de horas semanales corresponde a turno Noche?», «… a titularidad Pública?», «… a ciudad Valencia?» — which reads as a template slot, not Spanish a tribunal would print (items 24, 41, 44; the explanation repeats it: «Turno Noche suma 28…»). Suggested fix: «… corresponde al turno de noche?» / «… a los laboratorios de titularidad pública?» / «… a los laboratorios de Valencia?», or keep the filter form «… a los de turno «Noche»?».

Minor, not counted: the mean explanations write an integer sum with decimals («La suma de la columna es 56,00», items 13, 49) and item 32 gives its ratio with three decimals («0,083») where the others give two; the thresholds are often one unit from a cell (14: «más de 717» with 718 in the table), stricter reading than the official round thresholds but not wrong.

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 274797139979144773 | PASS | | Jaca, Lugo, Toledo pass; 21+14+5 = 40 (a) |
| 2 | 3493489528897654557 | PASS | | Omega, Gamma; 6+15 = 21 (c) |
| 3 | 3888289725752918728 | PASS | | Diego Rubio 424/358 = 1,18, next 1,67 (c) |
| 4 | 679292652377546788 | PASS | | Iván Duarte, Ana Cortés: 2 (c) |
| 5 | 2618344893097292910 | PASS | | three Coche rows, all >5 viajes: 3 (c) |
| 6 | 995660733233502469 | PASS | | sums Alemán 17, Francés 13, Informática 22, Inglés 9; min Inglés (d) |
| 7 | 1223983771725134866 | PASS | | Pablo Vera 120/3 = 40, next 15,5 (a) |
| 8 | 4580581082989247247 | PASS | | Marta Ríos 767/742 = 1,03, next 1,18 (c) |
| 9 | 3910380554785824084 | PASS | | Autobús: León 29, Mérida 50, Jaca 95; min León (d) |
| 10 | 4441628925242482318 | PASS | | only Ana Cortés (2 viajes, Avión, 384) (c) |
| 11 | 2446871128147784257 | PASS | | Cuenca 85, Lugo 89: 2 (c) |
| 12 | 3654112830433712182 | PASS | | 4 rows with <7 faltas; max edad Diego Rubio 51 (b) |
| 13 | 327284621952842892 | PASS | | 56/11 = 5,0909 → 5,09 (a); «56,00» odd but right |
| 14 | 3262813409570128271 | PASS | | only Omega (798, 34, Privada) (d) |
| 15 | 1574408861979755188 | PASS | | only Lugo passes all three (c) |
| 16 | 2074564667347024303 | PASS | | only Carla Nieto passes all three (b) |
| 17 | 1580329207806355028 | PASS | | only Sara Ortiz (2 h, 15 faltas) (c) |
| 18 | 4157976482641714332 | PASS | | Kappa, Iota: 2 (b) |
| 19 | 345352013983549247 | PASS | | Hija de la fortuna, Contra vosotros; sum 495 (b) |
| 20 | 3725810980475735155 | PASS | | only Diego Rubio passes all three (a) |
| 21 | 3689692058427482923 | PASS | | Carla Nieto, Sara Ortiz, Jorge Luna: 3 (b) |
| 22 | 549857973036573262 | PASS | | only Aranmanoth passes all four (d) |
| 23 | 3911690445701389361 | PASS | | Pablo Vera, Irene Pons: 2 (c) |
| 24 | 4092711762427273095 | FAIL | generator (G1) | key right (28/104 = 26,92 %, a) but «corresponde a turno Noche» |
| 25 | 2736979108388417725 | PASS | | Nuria Salas, Raúl Mena; sum 16 (b) |
| 26 | 4163390447536696390 | PASS | | 4 rows under 35; max cuota Diego Rubio 116 (b) |
| 27 | 1586508015396871889 | PASS | | Alfa 236/3 = 78,67, next 32,08 (a) |
| 28 | 3588842099432019975 | PASS | | sums Barcelona 576, Madrid 421, Sevilla 326, Valencia 538; min Sevilla (a) |
| 29 | 4110580552696902388 | PASS | | Elena Soler, Diego Rubio: 2 (d) |
| 30 | 3556477018594785593 | PASS | | Iota, Zeta: 2 (c) |
| 31 | 2381850757681049524 | PASS | | only León passes all four (b) |
| 32 | 3706174181096166754 | PASS | | Carla Nieto 1/12 = 0,083, next 0,125 (d) |
| 33 | 3614112383633376201 | PASS | | only Marta Ríos passes all four (b) |
| 34 | 1166747531291222478 | PASS | | four Noche rows with >6 faltas (b) |
| 35 | 1690837818924781736 | PASS | | Hugo Beltrán, Diego Rubio: 2 (a) |
| 36 | 3525112190121478594 | PASS | | only Delta passes all three (c) |
| 37 | 778671632053513995 | PASS | | León, Úbeda: 2 (a) |
| 38 | 232616239795612045 | PASS | | 5 rows pass; max coste Irene Pons 95 (d) |
| 39 | 1177092152084991428 | PASS | | only Sigma passes all three (a) |
| 40 | 2300311533501968391 | PASS | | Kappa, Gamma, Alfa: 3 (b) |
| 41 | 4561429966377530467 | FAIL | generator (G1) | key right (937/1627 = 57,59 %, b) but «corresponde a titularidad Pública» |
| 42 | 279218220529479154 | PASS | | only Omega (Bilbao, <523) (c) |
| 43 | 2042550028401227693 | PASS | | Ávila, Úbeda: 2 (a) |
| 44 | 1065444377732371285 | FAIL | generator (G1) | key right (913/5717 = 15,97 %, c) but «corresponde a ciudad Valencia» |
| 45 | 2719097753412396217 | PASS | | Soria, Cuenca, Lugo; sum 60 (a) |
| 46 | 3969796563389545576 | PASS | | Mano de sombra, Adiós a las novias; sum 20 (b) |
| 47 | 2439017718913394027 | PASS | | Raúl Mena, Jorge Luna; sum 205 (c) |
| 48 | 2169652614732583283 | PASS | | Hija de la fortuna, El amante lesbiano: 2 (c) |
| 49 | 4533545574814537803 | PASS | | 415/11 = 37,727 → 37,73 (b); «415,00» odd but right |
| 50 | 3814695743816065413 | PASS | | Lugo, Ávila; sum 598 (d) |
