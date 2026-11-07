# tablas-lectura — blind review, pass 2 (2026-11-07)

Items read: 50. PASS: 22. FAIL: 28 (generator: 28, bank: 0, other: 0).

## Defects

- G1 (generator): categorical conditions are rendered as «tiene(n) <columna> <Valor>» with the table value capitalised mid-sentence («tienen más de 5 viajes al año y medio Coche», «tienen curso Alemán», «tiene … ciudad Bilbao», «corresponde a turno Noche», «tipo Deportiva»); capitalising common nouns and language names is an orthography error and the construction is not natural Spanish, unlike the official «está publicado en una editorial de Barcelona»; every key is right. Items 2, 5, 9, 10, 11, 14, 15, 16, 18, 19, 20, 22, 23, 24, 25, 30, 31, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 47. Suggested fix: per column, a phrase template with the value in lower case where it is a common noun («viajan en coche», «son del curso de alemán», «están en Bilbao», «del turno de noche», «de tipo deportivo», «editados en Barcelona», «de titularidad mixta»).

Notes (not FAILs): every key recomputed from the parsed rows with exact fractions is right and unique; no ties among the options in max/min/ratio items. Count and filter-sum explanations give the count but not the rows that pass («Pasan el filtro 3 filas»), so a candidate who got a different count cannot see which row they misjudged; naming the rows would teach better. The mean explanations print the integer sum as «56,00» / «415,00». Some tables have more «ejemplares prestados» than «disponibles» (19, 22, 48) and a minibús with 58 participants (49); plausible enough not to fail.

## Items

| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 274797139979144773 | PASS |  | Jaca, Lugo, Toledo pass; 21+14+5 = 40 |
| 2 | 3493489528897654557 | FAIL | generator (G1) | key correct; Omega, Gamma pass, 6+15 = 21; «titularidad Mixta» capitalised |
| 3 | 3888289725752918728 | PASS |  | Diego Rubio 424/358 = 1,18; next lowest 1,75 |
| 4 | 679292652377546788 | PASS |  | Iván Duarte, Ana Cortés: 2 |
| 5 | 2618344893097292910 | FAIL | generator (G1) | key correct; Rocío Mora, Raúl Mena, Carla Nieto: 3; «tienen … medio Coche» |
| 6 | 995660733233502469 | PASS |  | Inglés 9 (Francés 13, Alemán 17, Informática 22) |
| 7 | 1223983771725134866 | PASS |  | Pablo Vera 120/3 = 40; next 15,5 |
| 8 | 4580581082989247247 | PASS |  | Marta Ríos 1,03; next 1,70 |
| 9 | 3910380554785824084 | FAIL | generator (G1) | key correct; Autobús: León 29, Mérida 50, Jaca 95; «tienen transporte Autobús» |
| 10 | 4441628925242482318 | FAIL | generator (G1) | key correct; only Ana Cortés passes; «medio Avión» |
| 11 | 2446871128147784257 | FAIL | generator (G1) | key correct; Cuenca, Lugo: 2; «tienen … tipo Deportiva» |
| 12 | 3654112830433712182 | PASS |  | filter < 7 faltas: Diego Rubio 51 highest |
| 13 | 327284621952842892 | PASS |  | 56/11 = 5,0909 → 5,09; mean over 11 rows fits level 3 |
| 14 | 3262813409570128271 | FAIL | generator (G1) | key correct; only Omega passes; «titularidad Privada» capitalised |
| 15 | 1574408861979755188 | FAIL | generator (G1) | key correct; only Lugo passes; «tipo Cultural» |
| 16 | 2074564667347024303 | FAIL | generator (G1) | key correct; only Carla Nieto passes; «tiene medio Coche» |
| 17 | 1580329207806355028 | PASS |  | only Sara Ortiz passes |
| 18 | 4157976482641714332 | FAIL | generator (G1) | key correct; Kappa, Iota: 2; «tienen … ciudad Sevilla» |
| 19 | 345352013983549247 | FAIL | generator (G1) | key correct; Hija de la fortuna + Contra vosotros = 495; «tienen … lugar de edición Barcelona» |
| 20 | 3725810980475735155 | FAIL | generator (G1) | key correct; only Diego Rubio passes; «curso Alemán» (language name capitalised) |
| 21 | 3689692058427482923 | PASS |  | Carla Nieto, Sara Ortiz, Jorge Luna: 3 |
| 22 | 549857973036573262 | FAIL | generator (G1) | key correct; only Aranmanoth passes; «lugar de edición Valencia» |
| 23 | 3911690445701389361 | FAIL | generator (G1) | key correct; Pablo Vera, Irene Pons: 2; «tienen curso Alemán» |
| 24 | 4092711762427273095 | FAIL | generator (G1) | key correct; 28/104 = 26,923 → 26,92 %; «corresponde a turno Noche» |
| 25 | 2736979108388417725 | FAIL | generator (G1) | key correct; Nuria Salas, Raúl Mena: 16; «tienen curso Alemán» |
| 26 | 4163390447536696390 | PASS |  | edad < 35: Diego Rubio 116 highest (next 89, 89) |
| 27 | 1586508015396871889 | PASS |  | Alfa 236/3 = 78,67; next 29 |
| 28 | 3588842099432019975 | PASS |  | Sevilla 326 (Madrid 421, Valencia 538, Barcelona 576) |
| 29 | 4110580552696902388 | PASS |  | Elena Soler, Diego Rubio: 2 |
| 30 | 3556477018594785593 | FAIL | generator (G1) | key correct; Iota, Zeta: 2; «tienen titularidad Mixta» |
| 31 | 2381850757681049524 | FAIL | generator (G1) | key correct; only León passes; «transporte Minibús» |
| 32 | 3706174181096166754 | PASS |  | Carla Nieto 1/12 = 0,083; next 0,44 |
| 33 | 3614112383633376201 | FAIL | generator (G1) | key correct; only Marta Ríos passes; «turno Tarde, curso Inglés» |
| 34 | 1166747531291222478 | FAIL | generator (G1) | key correct; Andrés Peña, Paula Giner, Carla Nieto, Jorge Luna: 4; «tienen turno Noche» |
| 35 | 1690837818924781736 | FAIL | generator (G1) | key correct; Hugo Beltrán, Diego Rubio: 2; «tienen medio Autobús» |
| 36 | 3525112190121478594 | FAIL | generator (G1) | key correct; only Delta passes; «tiene … ciudad Madrid» |
| 37 | 778671632053513995 | FAIL | generator (G1) | key correct; León, Úbeda: 2; «transporte Minibús y tipo Gastronómica» |
| 38 | 232616239795612045 | PASS |  | filter: Irene Pons 95 highest of 5 |
| 39 | 1177092152084991428 | PASS |  | only Sigma passes |
| 40 | 2300311533501968391 | PASS |  | Kappa, Gamma, Alfa: 3 |
| 41 | 4561429966377530467 | FAIL | generator (G1) | key correct; 937/1627 = 57,59 %; «corresponde a titularidad Pública» |
| 42 | 279218220529479154 | FAIL | generator (G1) | key correct; only Omega passes; «tiene … ciudad Bilbao» |
| 43 | 2042550028401227693 | FAIL | generator (G1) | key correct; Ávila, Úbeda: 2; «tienen tipo Deportiva» |
| 44 | 1065444377732371285 | FAIL | generator (G1) | key correct; 913/5717 = 15,97 %; «corresponde a ciudad Valencia» |
| 45 | 2719097753412396217 | FAIL | generator (G1) | key correct; Soria, Cuenca, Lugo: 60; «tienen transporte Minibús» |
| 46 | 3969796563389545576 | PASS |  | Mano de sombra + Adiós a las novias = 20; «tienen editorial Santillana» is stiff but a proper noun, acceptable |
| 47 | 2439017718913394027 | FAIL | generator (G1) | key correct; Raúl Mena + Jorge Luna = 205; «tienen turno Tarde» |
| 48 | 2169652614732583283 | PASS |  | Hija de la fortuna, El amante lesbiano: 2 |
| 49 | 4533545574814537803 | PASS |  | 415/11 = 37,727 → 37,73 |
| 50 | 3814695743816065413 | PASS |  | Lugo + Ávila = 598 |
