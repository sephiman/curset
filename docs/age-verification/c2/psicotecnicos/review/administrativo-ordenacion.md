# administrativo-ordenacion — blind review, pass 3 (2026-11-07)

Items read: 50. PASS: 50. FAIL: 0 (generator: 0, bank: 0, other: 0).

Every item recomputed in Python with the Spanish order (ñ a separate letter after n, accents ignored, letter by letter, a word that is a prefix of another goes first). In all 50 the four options are permutations of the same words, no two options repeat, and the keyed option is the only one in order. Every claim of every explanation was checked: the stated common prefix is the longest one shared by all the words, each adjacent pair is the pair of the sorted list, and each stated position and pair of letters is the first difference (or, for «mono»/«monólogo» and «compás»/«compasión», the shorter word ending there). The ñ items (25, 31, 35, 46) and the accent items (6, 10, 12, 23, 30) are decided and explained correctly. Words are common, real Spanish words; four words with a 2-letter prefix at nivel 1 and five with a 3–4-letter prefix at nivel 2 match the official items.

## Defects
None.

Minor, not counted: item 6 writes the accentless form in its reason, «(compas termina antes)», which a reader may take for a typo of «compás»; «(compás termina en la 6.ª)» would say the same without that risk.

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 4555066965740239113 | PASS | | consenso < conserva < consola < consuelo < consumo (a); explanation positions/letters right |
| 2 | 3939578575203761854 | PASS | | sensato < separar < serio < servir (a); explanation positions/letters right |
| 3 | 4474415237713957130 | PASS | | experiencia < experto < explicar < extintor (d); explanation positions/letters right |
| 4 | 3986174537117149445 | PASS | | arena < argolla < argumento < arriba (d); explanation positions/letters right |
| 5 | 603372815389903367 | PASS | | balanza < baldosa < ballena < banco (c); explanation positions/letters right |
| 6 | 199010173629350221 | PASS | | cómodo < compás < compasión < competir < comunidad (a); explanation positions/letters right; «compas termina antes» (accentless form) right |
| 7 | 1312285957095784798 | PASS | | experto < expreso < expulsar < extraño (a); explanation positions/letters right |
| 8 | 586411447732664663 | PASS | | precepto < preferir < prejuicio < premio < prensa (b); explanation positions/letters right |
| 9 | 3183826603561652651 | PASS | | expreso < expulsar < extintor < extraer (a); explanation positions/letters right |
| 10 | 3136843167391176986 | PASS | | comisión < cómodo < competir < complejo < comprobar (d); explanation positions/letters right; accent ignored (comisión < cómodo) |
| 11 | 1649338912055364273 | PASS | | consejo < conserva < consistorio < consola < consumo (b); explanation positions/letters right |
| 12 | 4216341121965525466 | PASS | | mono < monólogo < morder < moreno (c); explanation positions/letters right; «mono termina antes» right |
| 13 | 3086864748112296577 | PASS | | tracción < tradición < traje < trama < tratado (d); explanation positions/letters right |
| 14 | 2275873008059443780 | PASS | | consenso < conserje < consigna < consola < consumo (b); explanation positions/letters right |
| 15 | 392052284423797926 | PASS | | baldosa < bambú < banco < bandido (d); explanation positions/letters right |
| 16 | 2089792014296908851 | PASS | | sendero < sentido < serio < servir (c); explanation positions/letters right |
| 17 | 2999734156096908936 | PASS | | arco < arrancar < arreglo < arriba (a); explanation positions/letters right |
| 18 | 2828410269824099816 | PASS | | arder < argumento < arreglo < arriba (c); explanation positions/letters right |
| 19 | 3215319322211431241 | PASS | | archivo < arena < argolla < aritmética (b); explanation positions/letters right |
| 20 | 2382926752439013763 | PASS | | balanza < bandido < barato < barco (d); explanation positions/letters right |
| 21 | 2816441409034343760 | PASS | | experto < exponer < expreso < extender (d); explanation positions/letters right |
| 22 | 4279925548664825545 | PASS | | monedero < monje < montaña < moral (a); explanation positions/letters right |
| 23 | 139046438580241723 | PASS | | trabajo < traducir < tráfico < traje < trama (b); explanation positions/letters right; accent ignored (traducir < tráfico) |
| 24 | 2831518037082271576 | PASS | | balcón < baldosa < bambú < barrio (c); explanation positions/letters right |
| 25 | 4302659435834502830 | PASS | | sentar < señor < separar < septiembre (d); explanation positions/letters right; n before ñ before p |
| 26 | 2346884929957470804 | PASS | | preámbulo < precio < precipicio < pregón < prejuicio (c); explanation positions/letters right |
| 27 | 4044016964376047688 | PASS | | preámbulo < predecir < pregunta < prejuicio < preparar (a); explanation positions/letters right |
| 28 | 3333530576730021914 | PASS | | consenso < consigna < consistorio < constante < constar (b); explanation positions/letters right |
| 29 | 46984684564216847 | PASS | | balcón < ballena < banda < bandera (c); explanation positions/letters right |
| 30 | 1057138789483389353 | PASS | | monitor < mono < monólogo < moreno (b); explanation positions/letters right; «mono termina antes» right |
| 31 | 2002794908792901705 | PASS | | sendero < señal < serio < servicio (a); explanation positions/letters right; n before ñ |
| 32 | 2940892646510383635 | PASS | | arder < arena < aroma < arreglo (c); explanation positions/letters right |
| 33 | 3005229353134768215 | PASS | | monitor < monólogo < montar < montón < monumento (a); explanation positions/letters right |
| 34 | 108197621066999492 | PASS | | comisión < comparar < competir < complejo < comunidad (c); explanation positions/letters right |
| 35 | 3475784328170287105 | PASS | | sendero < sentencia < señal < sequía (c); explanation positions/letters right; n before ñ before q |
| 36 | 1913034449785600604 | PASS | | preámbulo < precisar < predecir < prejuicio < prensa (c); explanation positions/letters right |
| 37 | 2967880095416840016 | PASS | | banco < bandera < banquete < barco (c); explanation positions/letters right |
| 38 | 1141178854406610116 | PASS | | expediente < experto < expreso < extraño (d); explanation positions/letters right |
| 39 | 2255278545539089254 | PASS | | experiencia < explicar < exponer < extintor (a); explanation positions/letters right |
| 40 | 3136358450649417723 | PASS | | precio < preferir < pregón < premio < preparar (b); explanation positions/letters right |
| 41 | 1519003733716666633 | PASS | | experiencia < exponer < exprimir < exterior (a); explanation positions/letters right |
| 42 | 839524238012051250 | PASS | | senda < serie < serio < servir (b); explanation positions/letters right |
| 43 | 1152431999465106164 | PASS | | sentencia < septiembre < serio < servicio (c); explanation positions/letters right |
| 44 | 485261606043199589 | PASS | | sentir < serie < servicio < servir (c); explanation positions/letters right |
| 45 | 1427355938641086137 | PASS | | compañía < compasión < completo < componer < comprobar (c); explanation positions/letters right |
| 46 | 385616007790545021 | PASS | | bambú < bandeja < bandido < bañera (d); explanation positions/letters right; n before ñ |
| 47 | 201456550062969828 | PASS | | preferir < pregunta < prejuicio < premio < prenda (c); explanation positions/letters right |
| 48 | 3638634045802014296 | PASS | | argolla < argumento < arqueología < arrabal (b); explanation positions/letters right |
| 49 | 648126843482918671 | PASS | | arcilla < arena < aritmética < arrabal (b); explanation positions/letters right |
| 50 | 4290145025528091064 | PASS | | expediente < explicar < exterior < extintor (b); explanation positions/letters right |
