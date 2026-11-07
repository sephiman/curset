# administrativo-ordenacion — blind review, pass 1 (2026-11-07)

Items read: 50. PASS: 10. FAIL: 40 (generator: 40, bank: 0, other: 0).

Keys: all 50 recomputed with Spanish alphabetical order (letter by letter, accents ignored, ñ after n: sentar < señor < separar, bandido < bañera, compañía < compasión; cómodo < compás): in every item the four options are permutations of the same words, exactly one is in order and it is the key. Stem and option form copy the official 2024X item (lowercase words, final period); words are common rather than rare (the official uses giraldete, girándula), which is a fair level-1 choice.

## Defects
- E1 (generator): the explanation says «desde la primera en que dejan de coincidir (la N.ª en las más parecidas)» but N is the letter where the whole group first splits, not where the most similar pair splits; whenever two words share a longer prefix the stated letter is false (consenso/conserva differ at the 6.ª, the explanation says 5.ª; serio/servir at the 4.ª, it says 3.ª). Items: every FAIL row. Suggested fix: compute N as the deepest first-difference over adjacent pairs and name that pair («consenso y conserva se deciden en la 6.ª letra: n antes que r»), or drop the parenthesis.

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 4555066965740239113 | FAIL | generator (E1) | key a (consenso, conserva, consola, consuelo, consumo) right and unique; explanation says «la 5.ª en las más parecidas» but consuelo/consumo first differ at the 6.ª |
| 2 | 3939578575203761854 | FAIL | generator (E1) | key a (sensato, separar, serio, servir) right and unique; explanation says «la 3.ª en las más parecidas» but serio/servir first differ at the 4.ª |
| 3 | 4474415237713957130 | FAIL | generator (E1) | key d (experiencia, experto, explicar, extintor) right and unique; explanation says «la 3.ª en las más parecidas» but experiencia/experto first differ at the 6.ª |
| 4 | 3986174537117149445 | FAIL | generator (E1) | key d (arena, argolla, argumento, arriba) right and unique; explanation says «la 3.ª en las más parecidas» but argolla/argumento first differ at the 4.ª |
| 5 | 603372815389903367 | FAIL | generator (E1) | key c (balanza, baldosa, ballena, banco) right and unique; explanation says «la 3.ª en las más parecidas» but baldosa/ballena first differ at the 4.ª |
| 6 | 199010173629350221 | FAIL | generator (E1) | key a (cómodo, compás, compasión, competir, comunidad) right and unique; explanation says «la 4.ª en las más parecidas» but compás/compasión first differ at the 7.ª |
| 7 | 1312285957095784798 | FAIL | generator (E1) | key a (experto, expreso, expulsar, extraño) right and unique; explanation says «la 3.ª en las más parecidas» but expreso/expulsar first differ at the 4.ª |
| 8 | 586411447732664663 | PASS | | key b (precepto, preferir, prejuicio, premio, prensa) only correct series; «la 4.ª» right |
| 9 | 3183826603561652651 | FAIL | generator (E1) | key a (expreso, expulsar, extintor, extraer) right and unique; explanation says «la 3.ª en las más parecidas» but extintor/extraer first differ at the 4.ª |
| 10 | 3136843167391176986 | FAIL | generator (E1) | key d (comisión, cómodo, competir, complejo, comprobar) right and unique; explanation says «la 4.ª en las más parecidas» but complejo/comprobar first differ at the 5.ª |
| 11 | 1649338912055364273 | FAIL | generator (E1) | key b (consejo, conserva, consiste, consola, consumo) right and unique; explanation says «la 5.ª en las más parecidas» but consejo/conserva first differ at the 6.ª |
| 12 | 4216341121965525466 | FAIL | generator (E1) | key c (mono, monólogo, morder, moreno) right and unique; explanation says «la 3.ª en las más parecidas» but mono/monólogo first differ at the 5.ª |
| 13 | 3086864748112296577 | PASS | | key d (tracción, tradición, traje, trama, tratado) only correct series; «la 4.ª» right |
| 14 | 2275873008059443780 | FAIL | generator (E1) | key b (consenso, conserje, consigna, consola, consumo) right and unique; explanation says «la 5.ª en las más parecidas» but consenso/conserje first differ at the 6.ª |
| 15 | 392052284423797926 | FAIL | generator (E1) | key d (baldosa, bambú, banco, bandido) right and unique; explanation says «la 3.ª en las más parecidas» but banco/bandido first differ at the 4.ª |
| 16 | 2089792014296908851 | FAIL | generator (E1) | key c (sendero, sentido, serio, servir) right and unique; explanation says «la 3.ª en las más parecidas» but serio/servir first differ at the 4.ª |
| 17 | 2999734156096908936 | FAIL | generator (E1) | key a (arco, arrancar, arreglo, arriba) right and unique; explanation says «la 3.ª en las más parecidas» but arreglo/arriba first differ at the 4.ª |
| 18 | 2828410269824099816 | FAIL | generator (E1) | key c (arder, argumento, arreglo, arriba) right and unique; explanation says «la 3.ª en las más parecidas» but arreglo/arriba first differ at the 4.ª |
| 19 | 3215319322211431241 | PASS | | key b (archivo, arena, argolla, aritmética) only correct series; «la 3.ª» right |
| 20 | 2382926752439013763 | FAIL | generator (E1) | key d (balanza, bandido, barato, barco) right and unique; explanation says «la 3.ª en las más parecidas» but barato/barco first differ at the 4.ª |
| 21 | 2816441409034343760 | FAIL | generator (E1) | key d (experto, exponer, expreso, extender) right and unique; explanation says «la 3.ª en las más parecidas» but exponer/expreso first differ at the 4.ª |
| 22 | 4279925548664825545 | FAIL | generator (E1) | key a (monedero, monje, montaña, moral) right and unique; explanation says «la 3.ª en las más parecidas» but monje/montaña first differ at the 4.ª |
| 23 | 139046438580241723 | PASS | | key b (trabajo, traducir, tráfico, traje, trama) only correct series; «la 4.ª» right |
| 24 | 2831518037082271576 | FAIL | generator (E1) | key c (balcón, baldosa, bambú, barrio) right and unique; explanation says «la 3.ª en las más parecidas» but balcón/baldosa first differ at the 4.ª |
| 25 | 4302659435834502830 | FAIL | generator (E1) | key d (sentar, señor, separar, septiembre) right and unique; explanation says «la 3.ª en las más parecidas» but separar/septiembre first differ at the 4.ª |
| 26 | 2346884929957470804 | FAIL | generator (E1) | key c (preámbulo, precio, precipicio, pregón, prejuicio) right and unique; explanation says «la 4.ª en las más parecidas» but precio/precipicio first differ at the 6.ª |
| 27 | 4044016964376047688 | PASS | | key a (preámbulo, predecir, pregunta, prejuicio, preparar) only correct series; «la 4.ª» right |
| 28 | 3333530576730021914 | FAIL | generator (E1) | key b (consenso, consigna, consiste, constante, constar) right and unique; explanation says «la 5.ª en las más parecidas» but constante/constar first differ at the 7.ª |
| 29 | 46984684564216847 | FAIL | generator (E1) | key c (balcón, ballena, banda, bandera) right and unique; explanation says «la 3.ª en las más parecidas» but banda/bandera first differ at the 5.ª |
| 30 | 1057138789483389353 | FAIL | generator (E1) | key b (monitor, mono, monólogo, moreno) right and unique; explanation says «la 3.ª en las más parecidas» but mono/monólogo first differ at the 5.ª |
| 31 | 2002794908792901705 | FAIL | generator (E1) | key a (sendero, señal, serio, servicio) right and unique; explanation says «la 3.ª en las más parecidas» but serio/servicio first differ at the 4.ª |
| 32 | 2940892646510383635 | PASS | | key c (arder, arena, aroma, arreglo) only correct series; «la 3.ª» right |
| 33 | 3005229353134768215 | FAIL | generator (E1) | key a (monitor, monólogo, montar, montón, monumento) right and unique; explanation says «la 4.ª en las más parecidas» but montar/montón first differ at the 5.ª |
| 34 | 108197621066999492 | FAIL | generator (E1) | key c (comisión, comparar, competir, complejo, comunidad) right and unique; explanation says «la 4.ª en las más parecidas» but competir/complejo first differ at the 5.ª |
| 35 | 3475784328170287105 | FAIL | generator (E1) | key c (sendero, sentencia, señal, sequía) right and unique; explanation says «la 3.ª en las más parecidas» but sendero/sentencia first differ at the 4.ª |
| 36 | 1913034449785600604 | PASS | | key c (preámbulo, precisar, predecir, prejuicio, prensa) only correct series; «la 4.ª» right |
| 37 | 2967880095416840016 | FAIL | generator (E1) | key c (banco, bandera, banquete, barco) right and unique; explanation says «la 3.ª en las más parecidas» but bandera/banquete first differ at the 4.ª |
| 38 | 1141178854406610116 | FAIL | generator (E1) | key d (expediente, experto, expreso, extraño) right and unique; explanation says «la 3.ª en las más parecidas» but expediente/experto first differ at the 5.ª |
| 39 | 2255278545539089254 | FAIL | generator (E1) | key a (experiencia, explicar, exponer, extintor) right and unique; explanation says «la 3.ª en las más parecidas» but explicar/exponer first differ at the 4.ª |
| 40 | 3136358450649417723 | PASS | | key b (precio, preferir, pregón, premio, preparar) only correct series; «la 4.ª» right |
| 41 | 1519003733716666633 | FAIL | generator (E1) | key a (experiencia, exponer, exprimir, exterior) right and unique; explanation says «la 3.ª en las más parecidas» but exponer/exprimir first differ at the 4.ª |
| 42 | 839524238012051250 | FAIL | generator (E1) | key b (senda, serie, serio, servir) right and unique; explanation says «la 3.ª en las más parecidas» but serie/serio first differ at the 5.ª |
| 43 | 1152431999465106164 | FAIL | generator (E1) | key c (sentencia, septiembre, serio, servicio) right and unique; explanation says «la 3.ª en las más parecidas» but serio/servicio first differ at the 4.ª |
| 44 | 485261606043199589 | FAIL | generator (E1) | key c (sentir, serie, servicio, servir) right and unique; explanation says «la 3.ª en las más parecidas» but servicio/servir first differ at the 6.ª |
| 45 | 1427355938641086137 | FAIL | generator (E1) | key c (compañía, compasión, completo, componer, comprobar) right and unique; explanation says «la 5.ª en las más parecidas» but compañía/compasión first differ at the 6.ª |
| 46 | 385616007790545021 | FAIL | generator (E1) | key d (bambú, bandeja, bandido, bañera) right and unique; explanation says «la 3.ª en las más parecidas» but bandeja/bandido first differ at the 5.ª |
| 47 | 201456550062969828 | PASS | | key c (preferir, pregunta, prejuicio, premio, prenda) only correct series; «la 4.ª» right |
| 48 | 3638634045802014296 | FAIL | generator (E1) | key b (argolla, argumento, arqueología, arrabal) right and unique; explanation says «la 3.ª en las más parecidas» but argolla/argumento first differ at the 4.ª |
| 49 | 648126843482918671 | PASS | | key b (arcilla, arena, aritmética, arrabal) only correct series; «la 3.ª» right |
| 50 | 4290145025528091064 | FAIL | generator (E1) | key b (expediente, explicar, exterior, extintor) right and unique; explanation says «la 3.ª en las más parecidas» but exterior/extintor first differ at the 4.ª |
