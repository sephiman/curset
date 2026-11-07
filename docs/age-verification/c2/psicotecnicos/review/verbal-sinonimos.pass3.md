# verbal-sinonimos — blind review, pass 3 (2026-11-07)

Items read: 50. PASS: 49. FAIL: 1 (generator: 0, bank: 1, other: 0).

Every stem, key and distractor was checked in both directions against `dle_relations.json` (each sense's «Sinónimos y afines» and «Antónimos y opuestos»), and the definitions were read where a relation is not listed. Every key is a DLE synonym of the stem in a current sense, or its definition coincides (29 disidente via hereje 1.b; 41 rehusar via repudiar 1.a). No distractor is listed as a synonym of the stem in either direction. Every antonym claim in the explanations is listed or follows in one step (e.g. 2 aprobar: vetar lists it as antónimo; 19 mezquino = tacaño, antónimo of pródigo 2). No item has three distractors sharing one meaning.

## Defects
- B1 (bank): for TENUE, the distractor «Sobrio» matches tenue 3 (style without ornament ≈ sobrio 1.b «Que carece de adornos superfluos»), so a candidate who knows the DLE can argue for it, and the explanation's «no guardan relación» is wrong for it (item 24). Suggested fix: replace «Sobrio» with a distractor that matches no sense of tenue (e.g. «Tozudo»).

Remarks (not FAILs):
- N1: two distractors are synonyms of each other (both antonyms of the stem) in items 15, 16, 17, 34, 36, 38; that halves the field by elimination but the key still has to be known, as in the official antonym-heavy sets.
- N2: stem repetition is high for 50 items: PROHIBIR ×4 (2, 5, 22, 40), HEREJE ×3, ALUDIR ×3, PERENNE ×3, ESCASEZ ×3; item 7 is almost the official 2025 HEREJE item.

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 1141078955796556589 | PASS | | key insuficiencia: insuficiencia in escasez 1.a syn; others unrelated |
| 2 | 3697999702024966389 | PASS | | key vedar: vedar in prohibir 1 syn; «aprobar» antonym: vetar lists aprobar as antónimo |
| 3 | 391761397451418903 | PASS | | key efímero y permanente: efímero (ant eterno, perdurable) vs permanente; prolijo 1 «dilatado con exceso», abolir/derogar, erial/yermo listed |
| 4 | 116004607164568651 | PASS | | key perpetuo: perpetuo in perenne 1 syn; caduco is perenne 2 ant |
| 5 | 3739109203017044618 | PASS | | key vetar: vetar in prohibir 1 syn; consentir lists prohibir as ant |
| 6 | 2477451434074734619 | PASS | | key verídico: verídico in veraz 1.a syn; embustero in veraz ant |
| 7 | 1831078680427925677 | PASS | | key heterodoxo: heterodoxo in hereje 1.a syn; ortodoxo in ant |
| 8 | 42307564503573162 | PASS | | key nombrar: nombrar 1.a lists aludir; callar 1.c ant «mencionar» (aludir 1) |
| 9 | 2274908852475373546 | PASS | | key perpetuo: perpetuo in perenne 1 syn; caduco perenne 2 ant |
| 10 | 2380185456894922700 | PASS | | key derogar: derogar in abolir 1 syn (and its definition); rest unrelated |
| 11 | 3102290330842709567 | PASS | | key sagaz: sagaz in perspicaz 1.b syn; tenaz, callado, sereno unrelated |
| 12 | 2710382267331503504 | PASS | | key vigoroso: vigoroso in recio 1.a syn; endeble in ant |
| 13 | 2748927680885716892 | PASS | | key erial y vergel: erial lists vergel as ant; the other three pairs listed as syn |
| 14 | 1264712300136670570 | PASS | | key entretenido: entretenido in ameno 1.a syn; árido 2 lists ameno as ant |
| 15 | 4035954585872136485 | PASS | | key fortuna: fortuna in ventura 2.a syn; desdicha in ant; infortunio ant fortuna/dicha |
| 16 | 3664461994577420833 | PASS | | key penuria: penuria in escasez 1.b syn; abundancia, riqueza in ant |
| 17 | 388436220176971422 | PASS | | key raro: raro in insólito 1 syn; corriente in ant, ordinario lists insólito as ant |
| 18 | 3706719249404740009 | PASS | | key lacónico: lacónico in conciso 1 syn; prolijo in ant |
| 19 | 15866943472962960 | PASS | | key derrochador: derrochador in pródigo 1.a syn; mezquino = tacaño, pródigo 2 ant |
| 20 | 1791231385106181993 | PASS | | key viejo: viejo in vetusto 1 syn; rest unrelated |
| 21 | 4431003880411911138 | PASS | | key heterodoxo: heterodoxo in hereje 1.a syn; rest unrelated |
| 22 | 4419152165289371346 | PASS | | key impedir: impedir in prohibir 1 syn (and its definition); rest unrelated |
| 23 | 2288356635551494230 | PASS | | key vetusto y reciente: vetusto ant nuevo/moderno, reciente 1.b ant viejo; other pairs listed |
| 24 | 2970954828420294781 | FAIL | bank (B1) | fino in tenue 1 syn, but distractor «Sobrio» (1.b «Que carece de adornos superfluos») coincides with tenue 3 «Dicho del estilo, que carece de exornación y artificio»; explanation says sobrio has no relation |
| 25 | 4554195905415751112 | PASS | | key ardiente: ardiente in vehemente 1.b syn; rest unrelated |
| 26 | 4160236706677059376 | PASS | | key sobrio: sobrio in austero 2 syn; lujoso in ant |
| 27 | 2139058207335012124 | PASS | | key tranquilo: tranquilo in apacible 1.a/1.b syn; agitado 2 ant tranquilo |
| 28 | 1275234519385389615 | PASS | | key ascético: ascético 2 «Sobrio o muy austero»; lujoso in austero 2 ant |
| 29 | 1381822285186186068 | PASS | | key disidente: hereje 1.b «Persona que disiente…»; heterodoxo 1.b lists disidente; rest unrelated |
| 30 | 1833171781126301493 | PASS | | key delgado: delgado in tenue 1 syn; grueso in ant; reducido («estrecho, pequeño») not listed |
| 31 | 848860223766278201 | PASS | | key aliviar: aliviar in atenuar 1.a syn; agravar in ant |
| 32 | 257937586048960439 | PASS | | key adyacente: adyacente in contiguo 1 syn; lejano in ant |
| 33 | 3459256773527453636 | PASS | | key escrupuloso y chapucero: escrupuloso 1.a ant chapucero; other pairs listed |
| 34 | 1264190601773923234 | PASS | | key parlanchín: parlanchín in locuaz 1 syn; callado, silencioso in ant |
| 35 | 739066753297327869 | PASS | | key raro: raro in insólito 1 syn; ordinario lists insólito as ant |
| 36 | 2263199814511107285 | PASS | | key agudo: agudo in perspicaz 1.b syn; obtuso in ant, lerdo ant despierto/espabilado |
| 37 | 137131758207054398 | PASS | | key patente: patente in ostensible 1.b syn; latente lists patente as ant |
| 38 | 3140463039684393883 | PASS | | key citar: citar in aludir 1 syn; omitir in ant, callar 1.c ant mencionar |
| 39 | 4487982277828631144 | PASS | | key penuria: penuria in escasez 1.b syn; rest unrelated |
| 40 | 4105882922667581671 | PASS | | key vedar: vedar in prohibir 1 syn; autorizar lists prohibir as ant |
| 41 | 1362184417036264438 | PASS | | key rehusar: rehusar lists repudiar, same definition; aceptar/admitir opposite |
| 42 | 2226125404984364231 | PASS | | key porfiado: porfiado in obstinado 1 syn; rest unrelated |
| 43 | 3710091150001851258 | PASS | | key perpetuo: perpetuo in perenne 1 syn; efímero ant eterno/perdurable |
| 44 | 778549974590815917 | PASS | | key grato: grato in ameno 1.b syn; sereno, fogoso, verídico not listed either way |
| 45 | 4556326286907707653 | PASS | | key mitigar: mitigar in atenuar 1.a syn; rest unrelated |
| 46 | 387128807088702255 | PASS | | key nombrar: nombrar 1.a lists aludir; rest unrelated |
| 47 | 460663160848223813 | PASS | | key impetuoso: impetuoso in vehemente 1.a syn; flemático 2.a syn tranquilo = impetuoso ant |
| 48 | 1513654114817553163 | PASS | | key franco: franco in veraz 1.a syn; rest unrelated |
| 49 | 1927553710114634689 | PASS | | key sensato: sensato in lúcido 1 syn; confuso 1.a ant claro |
| 50 | 4455604520932371783 | PASS | | key próximo: próximo in contiguo 1 syn; lejano in ant |
