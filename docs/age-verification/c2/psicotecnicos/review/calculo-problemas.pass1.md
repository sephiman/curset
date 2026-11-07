# calculo-problemas — blind review, pass 1 (2026-11-07)

Items read: 50. PASS: 50. FAIL: 0 (generator: 0, bank: 0, other: 0).

Every item was recomputed in Python with exact fractions: product counts, almacén days (all exact divisions, so no «día 13 o 14» reading), papelería totals, gratificación shares, two numbers from sum and ratio, unit price. For the «operadores que faltan» items all 27 operator combinations were tried: in each item exactly one combination reaches the target left to right, it is the key, and it also reaches the target with the usual precedence, so the 2022-39 dispute cannot arise. Stems follow the official forms (the almacén stem is the 2024X wording), magnitudes are doable by hand, levels fit the index (1 for one-step products and divisions, 2 for decimals, ratio-and-sum and operators).

## Defects
None.

Advisory, not counted as FAIL:
- A1: little variety in the unit-price subtype: items 46 and 50 have the same stem («Si 8 cuadernos cuestan 32 euros … 30 cuadernos») and key, and the seven cuaderno items use only unit prices 2, 3, 4 and 6 €. A mixed exam could show the same item twice.
- A2: in the gratificación items the explanation names the trap («El reparto es entre 11, no entre 30»), but no option carries it (825 / 30 = 27,50 is never offered); one distractor at the whole-department share would make the item test the trap it teaches.
- A3: «uno de ellos es 2 veces el otro» reads less naturally than «el doble» («el triple», «el cuádruple»), which is how a Spanish stem says it for small ratios.

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 180558790999070772 | PASS | | key 432: 3 × 16 × 9 = 432 sillas |
| 2 | 1278440966805938998 | PASS | | key 12 días: Faltan 1580 − 800 = 780 unidades; entre 65 al día son 12 días |
| 3 | 51261528581274285 | PASS | | key 31,30 €: 19 × 0,45 + 7 × 3,25 = 31,30 euros |
| 4 | 2260400680357392001 | PASS | | key 75: 825 / 11 = 75 |
| 5 | 1554470352242268824 | PASS | | key 1134: 9 × 9 × 14 = 1134 sillas |
| 6 | 2711105301957622312 | PASS | | key 864: 6 × 16 × 9 = 864 sillas |
| 7 | 2040222635848061935 | PASS | | key 120: 1320 / 11 = 120 |
| 8 | 1753115355312637349 | PASS | | key 32: El menor es 48 / 3 = 16; el mayor es 2 × 16 = 32 |
| 9 | 3898307950440185802 | PASS | | key 1296: 8 × 18 × 9 = 1296 sillas |
| 10 | 4514091041932310672 | PASS | | key -, +, +: only combination of 27 that gives the target left to right (same with precedence) |
| 11 | 3071096475260907629 | PASS | | key 76,40 €: 29 × 1,20 + 16 × 2,60 = 76,40 euros |
| 12 | 4333413335859233782 | PASS | | key 70,60 €: 23 × 0,95 + 15 × 3,25 = 70,60 euros |
| 13 | 2874833144572324357 | PASS | | key 24,80 €: 19 × 0,45 + 5 × 3,25 = 24,80 euros |
| 14 | 2273078969149923779 | PASS | | key ×, +, -: only combination of 27 that gives the target left to right (same with precedence) |
| 15 | 1360915602804834736 | PASS | | key 54: Cada cuaderno cuesta 36 / 12 = 3 euros; 18 × 3 = 54 |
| 16 | 1776246719887320771 | PASS | | key +, +, -: only combination of 27 that gives the target left to right (same with precedence) |
| 17 | 2690789185829586602 | PASS | | key 10 días: Faltan 1725 − 525 = 1200 unidades; entre 120 al día son 10 días |
| 18 | 1829329591002600448 | PASS | | key 60: Cada cuaderno cuesta 18 / 6 = 3 euros; 20 × 3 = 60 |
| 19 | 4382408721980717508 | PASS | | key -, +, +: only combination of 27 that gives the target left to right (same with precedence) |
| 20 | 4329261219534426627 | PASS | | key 54,05 €: 19 × 0,45 + 14 × 3,25 = 54,05 euros |
| 21 | 1646624936382171282 | PASS | | key 40: 400 / 10 = 40 |
| 22 | 4318315992289269181 | PASS | | key 60: El menor es 75 / 5 = 15; el mayor es 4 × 15 = 60 |
| 23 | 3642917169328219885 | PASS | | key 52,75 €: 29 × 0,95 + 12 × 2,10 = 52,75 euros |
| 24 | 522745020435711845 | PASS | | key 84: El menor es 112 / 4 = 28; el mayor es 3 × 28 = 84 |
| 25 | 3293218079445215240 | PASS | | key 792: 4 × 18 × 11 = 792 sillas |
| 26 | 4285634384778682878 | PASS | | key 540: 6 × 9 × 10 = 540 sillas |
| 27 | 4431004823014985952 | PASS | | key ×, ×, -: only combination of 27 that gives the target left to right (same with precedence) |
| 28 | 318122278133970235 | PASS | | key 75: 300 / 4 = 75 |
| 29 | 2650114669333005095 | PASS | | key 40: Cada cuaderno cuesta 12 / 6 = 2 euros; 20 × 2 = 40 |
| 30 | 1749822834543286852 | PASS | | key 120: El menor es 144 / 6 = 24; el mayor es 5 × 24 = 120 |
| 31 | 51454947361655028 | PASS | | key 180: Cada cuaderno cuesta 48 / 8 = 6 euros; 30 × 6 = 180 |
| 32 | 327419858050430848 | PASS | | key 40: 280 / 7 = 40 |
| 33 | 1890776037983379231 | PASS | | key 60: Cada cuaderno cuesta 16 / 8 = 2 euros; 30 × 2 = 60 |
| 34 | 2220669330088175677 | PASS | | key 50: 350 / 7 = 50 |
| 35 | 1503781903715164646 | PASS | | key 60: Cada cuaderno cuesta 30 / 15 = 2 euros; 30 × 2 = 60 |
| 36 | 1021355043926013886 | PASS | | key 38: El menor es 57 / 3 = 19; el mayor es 2 × 19 = 38 |
| 37 | 3854091528299779889 | PASS | | key 23 días: Faltan 2140 − 300 = 1840 unidades; entre 80 al día son 23 días |
| 38 | 1436288844838428028 | PASS | | key 9 días: Faltan 1875 − 1200 = 675 unidades; entre 75 al día son 9 días |
| 39 | 262654184820367357 | PASS | | key 200: El menor es 240 / 6 = 40; el mayor es 5 × 40 = 200 |
| 40 | 2164152113904204897 | PASS | | key 28,70 €: 19 × 0,80 + 9 × 1,50 = 28,70 euros |
| 41 | 1262514110843238570 | PASS | | key 51: El menor es 68 / 4 = 17; el mayor es 3 × 17 = 51 |
| 42 | 148281797622724415 | PASS | | key 18 días: Faltan 1020 − 300 = 720 unidades; entre 40 al día son 18 días |
| 43 | 376179894431768562 | PASS | | key 24: El menor es 30 / 5 = 6; el mayor es 4 × 6 = 24 |
| 44 | 111790317788156661 | PASS | | key 8 días: Faltan 1760 − 800 = 960 unidades; entre 120 al día son 8 días |
| 45 | 2846568303615978718 | PASS | | key 935: 5 × 17 × 11 = 935 sillas |
| 46 | 822631935574881619 | PASS | | key 120: Cada cuaderno cuesta 32 / 8 = 4 euros; 30 × 4 = 120 |
| 47 | 2201565206855591012 | PASS | | key 40,50 €: 13 × 1,50 + 10 × 2,10 = 40,50 euros |
| 48 | 3998441012288977609 | PASS | | key 36: El menor es 45 / 5 = 9; el mayor es 4 × 9 = 36 |
| 49 | 545074174834871478 | PASS | | key 8 días: Faltan 1520 − 1200 = 320 unidades; entre 40 al día son 8 días |
| 50 | 2541008619776365774 | PASS | | key 120: Cada cuaderno cuesta 32 / 8 = 4 euros; 30 × 4 = 120; same stem as 46 |
