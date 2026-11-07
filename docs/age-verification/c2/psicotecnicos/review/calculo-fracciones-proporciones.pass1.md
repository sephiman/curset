# calculo-fracciones-proporciones — blind review, pass 1 (2026-11-07)

Items read: 50. PASS: 43. FAIL: 7 (generator: 7, bank: 0, other: 0).

Keys: all 50 recomputed with exact fractions; every key is right and the only option equal to the value. The «paquetes de bienvenida» items copy the official 2025 item (unreduced «dos octavos», totals that divide exactly) and the reparto items are plain direct proportion with integer shares; levels (fractions 1, repartos 2) match the index. Distractors include natural errors (the equal share, another person's share, half the total) and none makes an item trivial.

## Defects
- E1 (generator): when the asked person has one part the explanation prints «la persona pedida tiene 1 partes», a number-agreement error a candidate reads in the feedback. Items 4, 15, 16, 32, 34, 38, 40. Suggested fix: inflect «parte/partes» on the count.

Note (no FAIL): the fraction explanation abbreviates the fraction name with an ordinal («Cada 6.º son 40 paquetes»); it reads, but «Cada sexto son 40 paquetes» is how a teacher would write it. «La persona pedida» is also stiff; «la segunda persona tiene 3 partes» says the same concretely.

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 2551544288612410887 | PASS | | 1490/10 = 149 per part, segunda → 447 only fit |
| 2 | 4152599773549995708 | PASS | | 1210/10 = 121 per part, primera → 242 only fit |
| 3 | 1890353104721632364 | PASS | | 240 − dos sextos − dos sextos → 80 only fit |
| 4 | 1720648679487398676 | FAIL | generator (E1) | 1080/10 = 108 per part, primera → 108, right; explanation «tiene 1 partes» |
| 5 | 313067831180357227 | PASS | | 470/10 = 47 per part, tercera → 141 only fit |
| 6 | 2947390127756596946 | PASS | | 1230/10 = 123 per part, tercera → 615 only fit |
| 7 | 4355465126745721054 | PASS | | 711/9 = 79 per part, tercera → 316 only fit |
| 8 | 1561936501959130475 | PASS | | 702/6 = 117 per part, tercera → 351 only fit |
| 9 | 2095848956380978624 | PASS | | 1368/12 = 114 per part, segunda → 456 only fit |
| 10 | 2855625301944719702 | PASS | | 252 − un sexto − un sexto → 168 only fit |
| 11 | 2239371105347858788 | PASS | | 312/12 = 26 per part, tercera → 130 only fit |
| 12 | 1493682941609889529 | PASS | | 1090/10 = 109 per part, segunda → 218 only fit |
| 13 | 835049422986561227 | PASS | | 675/9 = 75 per part, tercera → 375 only fit |
| 14 | 3734662075540952113 | PASS | | 1350/9 = 150 per part, segunda → 450 only fit |
| 15 | 3978185492214708219 | FAIL | generator (E1) | 504/6 = 84 per part, primera → 84, right; explanation «tiene 1 partes» |
| 16 | 3839890581003824112 | FAIL | generator (E1) | 1314/9 = 146 per part, primera → 146, right; explanation «tiene 1 partes» |
| 17 | 1665312986840670110 | PASS | | 420/10 = 42 per part, tercera → 126 only fit |
| 18 | 3625788656448990859 | PASS | | 1197/9 = 133 per part, tercera → 665 only fit |
| 19 | 397310281939477453 | PASS | | 390 − un quinto − dos quintos → 156 only fit |
| 20 | 1037874473950172780 | PASS | | 472 − tres octavos − tres octavos → 118 only fit |
| 21 | 3481901059957930986 | PASS | | 414 − dos novenos − dos novenos → 230 only fit |
| 22 | 1676038646047680883 | PASS | | 472 − dos octavos − tres octavos → 177 only fit |
| 23 | 1636627034901351484 | PASS | | 420/12 = 35 per part, tercera → 175 only fit |
| 24 | 950924364424571085 | PASS | | 790/10 = 79 per part, cuarta → 316 only fit |
| 25 | 1438280491475450585 | PASS | | 792/6 = 132 per part, segunda → 264 only fit |
| 26 | 2744232229661367368 | PASS | | 330/10 = 33 per part, segunda → 99 only fit |
| 27 | 1141203405627733600 | PASS | | 1287/9 = 143 per part, tercera → 572 only fit |
| 28 | 2923787596620599583 | PASS | | 207/9 = 23 per part, primera → 46 only fit |
| 29 | 453269273968422293 | PASS | | 690/6 = 115 per part, tercera → 345 only fit |
| 30 | 1021853573416244139 | PASS | | 350 − un quinto − dos quintos → 140 only fit |
| 31 | 446926014502010107 | PASS | | 360/9 = 40 per part, segunda → 120 only fit |
| 32 | 2430048803253070032 | FAIL | generator (E1) | 570/6 = 95 per part, primera → 95, right; explanation «tiene 1 partes» |
| 33 | 8985097211321483 | PASS | | 756/6 = 126 per part, tercera → 378 only fit |
| 34 | 2089214042176097912 | FAIL | generator (E1) | 1450/10 = 145 per part, primera → 145, right; explanation «tiene 1 partes» |
| 35 | 985449481815013239 | PASS | | 560 − un octavo − tres octavos → 280 only fit |
| 36 | 2137225267572820965 | PASS | | 603/9 = 67 per part, primera → 134 only fit |
| 37 | 2836323319656596250 | PASS | | 804/12 = 67 per part, primera → 201 only fit |
| 38 | 4190711681218700483 | FAIL | generator (E1) | 1470/10 = 147 per part, primera → 147, right; explanation «tiene 1 partes» |
| 39 | 332700659082654377 | PASS | | 930/10 = 93 per part, tercera → 465 only fit |
| 40 | 726144999472278345 | FAIL | generator (E1) | 297/9 = 33 per part, primera → 33, right; explanation «tiene 1 partes» |
| 41 | 2251849675853898693 | PASS | | 534 − dos sextos − tres sextos → 89 only fit |
| 42 | 1831363309609917936 | PASS | | 450 − un quinto − un quinto → 270 only fit |
| 43 | 4508178208781399786 | PASS | | 576/12 = 48 per part, tercera → 240 only fit |
| 44 | 2954989507417089959 | PASS | | 996/12 = 83 per part, segunda → 332 only fit |
| 45 | 1785962025360910106 | PASS | | 320 − dos octavos − un octavo → 200 only fit |
| 46 | 1222899436258926372 | PASS | | 192 − dos sextos − dos sextos → 64 only fit |
| 47 | 1301884130371718730 | PASS | | 1080/10 = 108 per part, tercera → 540 only fit |
| 48 | 1028122198593078284 | PASS | | 1668/12 = 139 per part, primera → 417 only fit |
| 49 | 3799623025150812446 | PASS | | 240/10 = 24 per part, tercera → 120 only fit |
| 50 | 3487753745496345899 | PASS | | 441/9 = 49 per part, segunda → 147 only fit |
