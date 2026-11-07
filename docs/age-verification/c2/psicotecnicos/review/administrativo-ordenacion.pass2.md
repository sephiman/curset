# administrativo-ordenacion — blind review, pass 2 (2026-11-07)

Items read: 50. PASS: 22. FAIL: 28 (generator: 27, bank: 1, other: 0).

All 50 keys are right under the Spanish order (ñ after n, accents ignored, letter by letter); exactly one option is in order in every item. The FAILs are all in the explanation, plus one bank word.

## Defects
- G1 (generator): the explanation names only one pair of words that share the «ordering» letter, when that letter is shared by three words or a second pair also shares one, so it presents the rest as decided by that letter when they are not (e.g. 3: «experiencia y experto … se separan en la 6.ª», but explicar also has «p» as 3.ª letter and is placed by the 4.ª; 9: extintor / extraer also tie at the 3.ª letter). A candidate following it cannot see how the remaining words are placed. Items 1, 3, 5, 6, 7, 9, 10, 12, 16, 17, 21, 22, 25, 28, 29, 30, 31, 34, 35, 37, 38, 39, 41, 42, 44, 46, 50. Suggested fix: list every tie group at the deciding letter (all its words, not a pair) with the letter where each group splits, or walk the order word by word.
- G2 (generator): the shared prefix is copied with the accent of the first word in order, so item 6 says «Todas empiezan por «cóm»», which is false for compás, compasión, competir and comunidad. Suggested fix: print the prefix unaccented («com») and say once that accents do not count.
- B1 (bank): «consiste» is a conjugated form of «consistir», not a dictionary entry, in a list of headwords (items 11, 28); the official lists are all headwords. Suggested fix: replace it with «consistir» or another noun/infinitive (e.g. «consistorio»).

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 4555066965740239113 | FAIL | generator (G1) | clave a correcta (consenso, conserva, consola, consuelo, consumo); también empatan en la letra que «ordena»: consuelo / consumo, y la explicación no dice cómo se separan |
| 2 | 3939578575203761854 | PASS | | orden sensato, separar, serio, servir: única opción; explicación completa |
| 3 | 4474415237713957130 | FAIL | generator (G1) | clave d correcta (experiencia, experto, explicar, extintor); también empatan en la letra que «ordena»: experiencia / experto / explicar, y la explicación no dice cómo se separan |
| 4 | 3986174537117149445 | PASS | | orden arena, argolla, argumento, arriba: única opción; explicación completa |
| 5 | 603372815389903367 | FAIL | generator (G1) | clave c correcta (balanza, baldosa, ballena, banco); también empatan en la letra que «ordena»: balanza / baldosa / ballena, y la explicación no dice cómo se separan |
| 6 | 199010173629350221 | FAIL | generator (G1, G2) | clave a correcta (cómodo, compás, compasión, competir, comunidad); también empatan en la letra que «ordena»: compás / compasión / competir, y la explicación no dice cómo se separan; «Todas empiezan por «cóm»» es falso: compás, compasión, competir, comunidad llevan «com» |
| 7 | 1312285957095784798 | FAIL | generator (G1) | clave a correcta (experto, expreso, expulsar, extraño); también empatan en la letra que «ordena»: experto / expreso / expulsar, y la explicación no dice cómo se separan |
| 8 | 586411447732664663 | PASS | | orden precepto, preferir, prejuicio, premio, prensa: única opción; explicación completa |
| 9 | 3183826603561652651 | FAIL | generator (G1) | clave a correcta (expreso, expulsar, extintor, extraer); también empatan en la letra que «ordena»: extintor / extraer, y la explicación no dice cómo se separan |
| 10 | 3136843167391176986 | FAIL | generator (G1) | clave d correcta (comisión, cómodo, competir, complejo, comprobar); también empatan en la letra que «ordena»: competir / complejo / comprobar, y la explicación no dice cómo se separan |
| 11 | 1649338912055364273 | FAIL | bank (B1) | clave b correcta (consejo, conserva, consiste, consola, consumo); «consiste» es forma conjugada, no entrada de diccionario |
| 12 | 4216341121965525466 | FAIL | generator (G1) | clave c correcta (mono, monólogo, morder, moreno); también empatan en la letra que «ordena»: morder / moreno, y la explicación no dice cómo se separan |
| 13 | 3086864748112296577 | PASS | | orden tracción, tradición, traje, trama, tratado: única opción; explicación completa |
| 14 | 2275873008059443780 | PASS | | orden consenso, conserje, consigna, consola, consumo: única opción; explicación completa |
| 15 | 392052284423797926 | PASS | | orden baldosa, bambú, banco, bandido: única opción; explicación completa |
| 16 | 2089792014296908851 | FAIL | generator (G1) | clave c correcta (sendero, sentido, serio, servir); también empatan en la letra que «ordena»: serio / servir, y la explicación no dice cómo se separan |
| 17 | 2999734156096908936 | FAIL | generator (G1) | clave a correcta (arco, arrancar, arreglo, arriba); también empatan en la letra que «ordena»: arrancar / arreglo / arriba, y la explicación no dice cómo se separan |
| 18 | 2828410269824099816 | PASS | | orden arder, argumento, arreglo, arriba: única opción; explicación completa |
| 19 | 3215319322211431241 | PASS | | orden archivo, arena, argolla, aritmética: única opción; explicación completa |
| 20 | 2382926752439013763 | PASS | | orden balanza, bandido, barato, barco: única opción; explicación completa |
| 21 | 2816441409034343760 | FAIL | generator (G1) | clave d correcta (experto, exponer, expreso, extender); también empatan en la letra que «ordena»: experto / exponer / expreso, y la explicación no dice cómo se separan |
| 22 | 4279925548664825545 | FAIL | generator (G1) | clave a correcta (monedero, monje, montaña, moral); también empatan en la letra que «ordena»: monedero / monje / montaña, y la explicación no dice cómo se separan |
| 23 | 139046438580241723 | PASS | | orden trabajo, traducir, tráfico, traje, trama: única opción; explicación completa |
| 24 | 2831518037082271576 | PASS | | orden balcón, baldosa, bambú, barrio: única opción; explicación completa |
| 25 | 4302659435834502830 | FAIL | generator (G1) | clave d correcta (sentar, señor, separar, septiembre); también empatan en la letra que «ordena»: separar / septiembre, y la explicación no dice cómo se separan |
| 26 | 2346884929957470804 | PASS | | orden preámbulo, precio, precipicio, pregón, prejuicio: única opción; explicación completa |
| 27 | 4044016964376047688 | PASS | | orden preámbulo, predecir, pregunta, prejuicio, preparar: única opción; explicación completa |
| 28 | 3333530576730021914 | FAIL | generator (G1) + bank (B1) | clave b correcta (consenso, consigna, consiste, constante, constar); también empatan en la letra que «ordena»: consigna / consiste, y la explicación no dice cómo se separan; «consiste» es forma conjugada, no entrada de diccionario |
| 29 | 46984684564216847 | FAIL | generator (G1) | clave c correcta (balcón, ballena, banda, bandera); también empatan en la letra que «ordena»: balcón / ballena, y la explicación no dice cómo se separan |
| 30 | 1057138789483389353 | FAIL | generator (G1) | clave b correcta (monitor, mono, monólogo, moreno); también empatan en la letra que «ordena»: monitor / mono / monólogo, y la explicación no dice cómo se separan |
| 31 | 2002794908792901705 | FAIL | generator (G1) | clave a correcta (sendero, señal, serio, servicio); también empatan en la letra que «ordena»: serio / servicio, y la explicación no dice cómo se separan |
| 32 | 2940892646510383635 | PASS | | orden arder, arena, aroma, arreglo: única opción; explicación completa |
| 33 | 3005229353134768215 | PASS | | orden monitor, monólogo, montar, montón, monumento: única opción; explicación completa |
| 34 | 108197621066999492 | FAIL | generator (G1) | clave c correcta (comisión, comparar, competir, complejo, comunidad); también empatan en la letra que «ordena»: comparar / competir / complejo, y la explicación no dice cómo se separan |
| 35 | 3475784328170287105 | FAIL | generator (G1) | clave c correcta (sendero, sentencia, señal, sequía); también empatan en la letra que «ordena»: sendero / sentencia / señal, y la explicación no dice cómo se separan |
| 36 | 1913034449785600604 | PASS | | orden preámbulo, precisar, predecir, prejuicio, prensa: única opción; explicación completa |
| 37 | 2967880095416840016 | FAIL | generator (G1) | clave c correcta (banco, bandera, banquete, barco); también empatan en la letra que «ordena»: banco / bandera / banquete, y la explicación no dice cómo se separan |
| 38 | 1141178854406610116 | FAIL | generator (G1) | clave d correcta (expediente, experto, expreso, extraño); también empatan en la letra que «ordena»: expediente / experto / expreso, y la explicación no dice cómo se separan |
| 39 | 2255278545539089254 | FAIL | generator (G1) | clave a correcta (experiencia, explicar, exponer, extintor); también empatan en la letra que «ordena»: experiencia / explicar / exponer, y la explicación no dice cómo se separan |
| 40 | 3136358450649417723 | PASS | | orden precio, preferir, pregón, premio, preparar: única opción; explicación completa |
| 41 | 1519003733716666633 | FAIL | generator (G1) | clave a correcta (experiencia, exponer, exprimir, exterior); también empatan en la letra que «ordena»: experiencia / exponer / exprimir, y la explicación no dice cómo se separan |
| 42 | 839524238012051250 | FAIL | generator (G1) | clave b correcta (senda, serie, serio, servir); también empatan en la letra que «ordena»: serie / serio / servir, y la explicación no dice cómo se separan |
| 43 | 1152431999465106164 | PASS | | orden sentencia, septiembre, serio, servicio: única opción; explicación completa |
| 44 | 485261606043199589 | FAIL | generator (G1) | clave c correcta (sentir, serie, servicio, servir); también empatan en la letra que «ordena»: serie / servicio / servir, y la explicación no dice cómo se separan |
| 45 | 1427355938641086137 | PASS | | orden compañía, compasión, completo, componer, comprobar: única opción; explicación completa |
| 46 | 385616007790545021 | FAIL | generator (G1) | clave d correcta (bambú, bandeja, bandido, bañera); también empatan en la letra que «ordena»: bandeja / bandido / bañera, y la explicación no dice cómo se separan |
| 47 | 201456550062969828 | PASS | | orden preferir, pregunta, prejuicio, premio, prenda: única opción; explicación completa |
| 48 | 3638634045802014296 | PASS | | orden argolla, argumento, arqueología, arrabal: única opción; explicación completa |
| 49 | 648126843482918671 | PASS | | orden arcilla, arena, aritmética, arrabal: única opción; explicación completa |
| 50 | 4290145025528091064 | FAIL | generator (G1) | clave b correcta (expediente, explicar, exterior, extintor); también empatan en la letra que «ordena»: exterior / extintor, y la explicación no dice cómo se separan |
