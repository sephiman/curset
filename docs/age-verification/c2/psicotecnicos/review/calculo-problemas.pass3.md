# calculo-problemas — blind review, pass 3 (2026-11-07)

Items read: 50. PASS: 49. FAIL: 1 (generator: 1, bank: 0, other: 0).

Every key recomputed in Python with exact fractions. All 50 printed keys are the only matching option. For the eight operator items every one of the 27 operator triples was tried: the keyed triple is the only one that reaches the target left to right, and it also gives the target with the usual precedence, so the «de izquierda a derecha» convention never changes the key. Every explanation states the right route and the right intermediate values.

## Defects
- G1 (generator): in the «suma de dos números» family a distractor can be not smaller than the sum itself; in item 30 (suma 144) the options include «154.» and «144.», both impossible for the larger of two positive numbers that add up to 144, which leaves a two-way choice (120/130). Suggested fix: draw the larger-number distractors strictly between half the sum and the sum.

Minor, not counted: items 46 and 50 are the same stem (8 cuadernos, 32 €, 30 cuadernos) with different distractor sets; the papelería family usually has two far-off distractors next to one close one (13: «78,00 €», «64,00 €» against 24,80 €; 20: «14,85 €»), which an estimate removes, but one close distractor always remains; the smaller-number trap appears in several two-number items (36: «19.»), which is a fair distractor.

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 180558790999070772 | PASS | | 3 × 16 × 9 = 432 (c) |
| 2 | 1278440966805938998 | PASS | | 780 / 65 = 12 (c) |
| 3 | 51261528581274285 | PASS | | 8,55 + 22,75 = 31,30 € (b) |
| 4 | 2260400680357392001 | PASS | | 825 / 11 = 75 (a) |
| 5 | 1554470352242268824 | PASS | | 9 × 9 × 14 = 1134 (c) |
| 6 | 2711105301957622312 | PASS | | 6 × 16 × 9 = 864 (b) |
| 7 | 2040222635848061935 | PASS | | 1320 / 11 = 120 (a) |
| 8 | 1753115355312637349 | PASS | | 48 / 3 = 16, mayor 32 (c) |
| 9 | 3898307950440185802 | PASS | | 8 × 18 × 9 = 1296 (d) |
| 10 | 4514091041932310672 | PASS | | −, +, + → 23, only triple (c) |
| 11 | 3071096475260907629 | PASS | | 34,80 + 41,60 = 76,40 € (b) |
| 12 | 4333413335859233782 | PASS | | 21,85 + 48,75 = 70,60 € (a) |
| 13 | 2874833144572324357 | PASS | | 8,55 + 16,25 = 24,80 € (a) |
| 14 | 2273078969149923779 | PASS | | ×, +, − → 29, only triple (a) |
| 15 | 1360915602804834736 | PASS | | 3 € × 18 = 54 (b) |
| 16 | 1776246719887320771 | PASS | | +, +, − → 8, only triple (d) |
| 17 | 2690789185829586602 | PASS | | 1200 / 120 = 10 (c) |
| 18 | 1829329591002600448 | PASS | | 3 € × 20 = 60 (a) |
| 19 | 4382408721980717508 | PASS | | −, +, + → 10, only triple (c) |
| 20 | 4329261219534426627 | PASS | | 8,55 + 45,50 = 54,05 € (a) |
| 21 | 1646624936382171282 | PASS | | 400 / 10 = 40 (a) |
| 22 | 4318315992289269181 | PASS | | 75 / 5 = 15, mayor 60 (b) |
| 23 | 3642917169328219885 | PASS | | 27,55 + 25,20 = 52,75 € (c) |
| 24 | 522745020435711845 | PASS | | 112 / 4 = 28, mayor 84 (c) |
| 25 | 3293218079445215240 | PASS | | 4 × 18 × 11 = 792 (a) |
| 26 | 4285634384778682878 | PASS | | 6 × 9 × 10 = 540 (d) |
| 27 | 4431004823014985952 | PASS | | ×, ×, − → 132, only triple (c) |
| 28 | 318122278133970235 | PASS | | 300 / 4 = 75 (b) |
| 29 | 2650114669333005095 | PASS | | 2 € × 20 = 40 (b) |
| 30 | 1749822834543286852 | FAIL | generator (G1) | key right (144 / 6 = 24, mayor 120, b) but «154.» and «144.» are impossible |
| 31 | 51454947361655028 | PASS | | 6 € × 30 = 180 (d) |
| 32 | 327419858050430848 | PASS | | 280 / 7 = 40 (d) |
| 33 | 1890776037983379231 | PASS | | 2 € × 30 = 60 (c) |
| 34 | 2220669330088175677 | PASS | | 350 / 7 = 50 (b) |
| 35 | 1503781903715164646 | PASS | | 2 € × 30 = 60 (b) |
| 36 | 1021355043926013886 | PASS | | 57 / 3 = 19, mayor 38 (d) |
| 37 | 3854091528299779889 | PASS | | 1840 / 80 = 23 (c) |
| 38 | 1436288844838428028 | PASS | | 675 / 75 = 9 (c) |
| 39 | 262654184820367357 | PASS | | 240 / 6 = 40, mayor 200 (c) |
| 40 | 2164152113904204897 | PASS | | 15,20 + 13,50 = 28,70 € (a) |
| 41 | 1262514110843238570 | PASS | | 68 / 4 = 17, mayor 51 (b) |
| 42 | 148281797622724415 | PASS | | 720 / 40 = 18 (c) |
| 43 | 376179894431768562 | PASS | | 30 / 5 = 6, mayor 24 (d) |
| 44 | 111790317788156661 | PASS | | 960 / 120 = 8 (b) |
| 45 | 2846568303615978718 | PASS | | 5 × 17 × 11 = 935 (c) |
| 46 | 822631935574881619 | PASS | | 4 € × 30 = 120 (c) |
| 47 | 2201565206855591012 | PASS | | 19,50 + 21,00 = 40,50 € (c) |
| 48 | 3998441012288977609 | PASS | | 45 / 5 = 9, mayor 36 (d) |
| 49 | 545074174834871478 | PASS | | 320 / 40 = 8 (b) |
| 50 | 2541008619776365774 | PASS | | 4 € × 30 = 120 (b); same stem as 46 |
