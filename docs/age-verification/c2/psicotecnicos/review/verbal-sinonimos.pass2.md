# verbal-sinonimos — blind review, pass 2 (2026-11-07)

Items read: 50. PASS: 48. FAIL: 2 (generator: 2, bank: 0, other: 0).

Every stem word, key and distractor was checked against `dle_relations.json` (synonym/antonym lists and sense texts) and, where the lists were silent, against the sense definitions. No distractor is a DLE synonym of its stem, and no pair in the «pareja incorrecta» items other than the key is anything but a DLE synonym pair (or, for «Prolijo y dilatado», «Lúcido y claro», «Mediocre y mediano», a pair whose DLE definition uses the other word). Every «es su antónimo» claim in the explanations holds (DLE-listed in one direction or the other, or the plain opposite: «aprobar»/«autorizar»/«consentir» ↔ «prohibir», «ruin» ↔ «honesto» via «honrado», «latente» ↔ «ostensible» via «patente»).

## Defects
- G1 (generator): three distractors drawn from one synonym set («mofa», «irrisión», «befa» in 34; «consentir», «autorizar», «aprobar» in 40) give the key away by elimination: if one of them were the synonym the other two would be too, so none can be the key and the item is answered without knowing the stem word; items 34, 40. Suggested fix: allow at most two distractors that are DLE synonyms of each other (two antonyms is fine, as in the official items).
- Note (no FAIL): item 1's explanation says «fortuna» has no relation with «escasez», but DLE «fortuna» 2 is «Hacienda, capital, caudal», close to «riqueza», which the same explanation calls the antonym; the key is unaffected. Suggested fix: avoid «fortuna» as an «unrelated» distractor of «escasez» or call it «de sentido opuesto».

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 1141078955796556589 | PASS | | carencia (DLE syn escasez 1a); riqueza ant; fortuna 2 near «riqueza», see note |
| 2 | 3697999702024966389 | PASS | | impedir (DLE syn); aclarar, mitigar, aprobar not synonyms |
| 3 | 391761397451418903 | PASS | | efímero/permanente opposite; prolijo «dilatado con exceso», abolir/derogar, erial/yermo DLE syn |
| 4 | 116004607164568651 | PASS | | moderado (DLE syn frugal); excesivo opposite |
| 5 | 3739109203017044618 | PASS | | anular (DLE syn); implantar DLE ant, establecer ant via instituir/suprimir |
| 6 | 2477451434074734619 | PASS | | antiguo (DLE syn); moderno DLE ant |
| 7 | 1831078680427925677 | PASS | | sensato (DLE syn lúcido 1); confuso ↔ claro |
| 8 | 42307564503573162 | PASS | | honrado (DLE syn); ruin DLE ant honrado |
| 9 | 2274908852475373546 | PASS | | imperecedero (DLE syn); efímero opposite |
| 10 | 2380185456894922700 | PASS | | yermo (DLE syn); vergel DLE ant |
| 11 | 3102290330842709567 | PASS | | aliviar (DLE syn); agravar DLE ant |
| 12 | 2710382267331503504 | PASS | | suavizar (DLE suavizar lists atenuar); acentuar DLE ant; suprimir not a syn |
| 13 | 2748927680885716892 | PASS | | erial/vergel DLE ant; other three pairs DLE syn |
| 14 | 1264712300136670570 | PASS | | sensato (DLE syn); fogoso, delgado unrelated |
| 15 | 4035954585872136485 | PASS | | anular (DLE syn); instituir lists abolir as ant |
| 16 | 3664461994577420833 | PASS | | fino (DLE syn); grueso DLE ant |
| 17 | 388436220176971422 | PASS | | inusual (DLE syn); corriente DLE ant |
| 18 | 3706719249404740009 | PASS | | colindante (DLE syn); others unrelated |
| 19 | 15866943472962960 | PASS | | malgastador (DLE syn 1a); ahorrador DLE ant |
| 20 | 1791231385106181993 | PASS | | aliviar (DLE syn); agravar DLE ant |
| 21 | 4431003880411911138 | PASS | | disidente fits hereje 1b «persona que disiente…»; ortodoxo DLE ant |
| 22 | 4419152165289371346 | PASS | | impedir (DLE syn); nombrar, mitigar unrelated |
| 23 | 2288356635551494230 | PASS | | vetusto/reciente opposite; other three DLE syn |
| 24 | 2970954828420294781 | PASS | | charlatán (DLE syn); taciturno, reservado DLE antonyms (reverse) |
| 25 | 4554195905415751112 | PASS | | frugal/excesivo opposite; other three DLE syn |
| 26 | 4160236706677059376 | PASS | | fortuna (DLE syn ventura 2a); desgracia DLE ant |
| 27 | 2139058207335012124 | PASS | | momentáneo (DLE syn); eterno, duradero DLE ant |
| 28 | 1275234519385389615 | PASS | | desastroso (DLE syn 1b); propicio DLE ant |
| 29 | 1381822285186186068 | PASS | | disidente (hereje 1b); dicha, mofa, yermo unrelated |
| 30 | 1833171781126301493 | PASS | | porfiado (DLE syn); transigente DLE ant, dócil opposite |
| 31 | 848860223766278201 | PASS | | antiguo (DLE syn); moderno DLE ant |
| 32 | 257937586048960439 | PASS | | colindante (DLE syn); distante = lejano, DLE ant |
| 33 | 3459256773527453636 | PASS | | escrupuloso/chapucero DLE ant; other three DLE syn |
| 34 | 1264190601773923234 | FAIL | generator (G1) | key páramo right, but mofa/irrisión/befa are DLE synonyms of each other: solved by elimination |
| 35 | 739066753297327869 | PASS | | extraño (DLE syn); habitual, ordinario DLE ant (reverse) |
| 36 | 2263199814511107285 | PASS | | fuerte (DLE syn recio 1a); frágil opposite |
| 37 | 137131758207054398 | PASS | | patente (DLE syn 1b); latente DLE ant of patente |
| 38 | 3140463039684393883 | PASS | | hablador (DLE syn); silencioso, taciturno DLE ant |
| 39 | 4487982277828631144 | PASS | | impedir (DLE syn); rehusar = rechazar, not prohibir |
| 40 | 4105882922667581671 | FAIL | generator (G1) | key vedar right, but consentir/autorizar/aprobar are DLE synonyms of each other: solved by elimination |
| 41 | 1362184417036264438 | PASS | | fecundo (DLE syn); estéril DLE ant |
| 42 | 2226125404984364231 | PASS | | falta (DLE falta 1a lists escasez); profusión opposite |
| 43 | 3710091150001851258 | PASS | | pródigo/ahorrador DLE ant; other three DLE syn |
| 44 | 778549974590815917 | PASS | | vedar (DLE syn); autorizar DLE ant (reverse) |
| 45 | 4556326286907707653 | PASS | | suavizar (reverse DLE syn); intensificar DLE ant (reverse) |
| 46 | 387128807088702255 | PASS | | decente (DLE syn); tramposo, ruin opposite |
| 47 | 460663160848223813 | PASS | | sibilino 2 «misterioso u oscuro» vs claro; other three syn (lúcido «claro en el razonamiento») |
| 48 | 1513654114817553163 | PASS | | escueto (DLE syn); extenso, prolijo DLE ant |
| 49 | 1927553710114634689 | PASS | | impedir (DLE syn); nombrar, rehusar unrelated |
| 50 | 4455604520932371783 | PASS | | adyacente (DLE syn); lejano DLE ant |
