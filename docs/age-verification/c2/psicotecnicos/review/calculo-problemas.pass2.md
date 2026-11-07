# calculo-problemas — blind review, pass 2 (2026-11-07)

Items read: 50. PASS: 45. FAIL: 5 (generator: 5, bank: 0, other: 0).

## Defects

- G1 (generator): in the «papelería» sum-of-products items every unit price is a multiple of 0,05 €, so the total must be too, but the distractors are random cents (55,01 €, 88,62 €, 17,86 €…); in items 11, 12, 13, 40 and 47 the key is the only option that can be a total, so the item is answered without multiplying, and in 3, 20 and 23 the impossible-looking cents still cut the field to 2–3. Suggested fix: build the distractors as plausible errors on the same 0,05 € grid (one product wrong, a unit price swapped, ±0,50 €).

Notes (not FAILs): all 50 keys recomputed exactly and unique; in the operator items no other option gives the target either left to right or with the usual precedence. Every «sillas» item (1, 5, 6, 9, 25, 26, 45) can also be answered from the last digit alone (e.g. 3×16×9 ends in 2, only 432 does); the official percentage example (41,40 €) has the same property, so this is not counted as a departure, but distractors sharing the key's last digit would make the product item real. Items 46 and 50 have the same stem (8 cuadernos, 32 €, 30 cuadernos) with different distractors.

## Items

| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 180558790999070772 | PASS |  | 3×16×9 = 432 |
| 2 | 1278440966805938998 | PASS |  | (1580−800)/65 = 12 exact |
| 3 | 51261528581274285 | PASS |  | 8,55 + 22,75 = 31,30 €; 30,05 € also a multiple of 0,05, so the cents shortcut does not decide it |
| 4 | 2260400680357392001 | PASS |  | 825/11 = 75 |
| 5 | 1554470352242268824 | PASS |  | 9×9×14 = 1134 |
| 6 | 2711105301957622312 | PASS |  | 6×16×9 = 864 |
| 7 | 2040222635848061935 | PASS |  | 1320/11 = 120 |
| 8 | 1753115355312637349 | PASS |  | 48/3 = 16, mayor 32 |
| 9 | 3898307950440185802 | PASS |  | 8×18×9 = 1296 |
| 10 | 4514091041932310672 | PASS |  | 9−9+11+12 = 23; only c, also under precedence |
| 11 | 3071096475260907629 | FAIL | generator (G1) | key 34,80 + 41,60 = 76,40 € right, but it is the only option that is a multiple of 0,05 € (55,01, 88,62, 70,29 cannot come from these prices) |
| 12 | 4333413335859233782 | FAIL | generator (G1) | key 21,85 + 48,75 = 70,60 € right; only multiple of 0,05 € among 50,83, 73,42, 90,37 |
| 13 | 2874833144572324357 | FAIL | generator (G1) | key 8,55 + 16,25 = 24,80 € right; only multiple of 0,05 € among 17,86, 22,82, 27,78 |
| 14 | 2273078969149923779 | PASS |  | 3×9+10−8 = 29; only a |
| 15 | 1360915602804834736 | PASS |  | 36/12 = 3, ×18 = 54 |
| 16 | 1776246719887320771 | PASS |  | 9+3+2−6 = 8; only d |
| 17 | 2690789185829586602 | PASS |  | 1200/120 = 10 |
| 18 | 1829329591002600448 | PASS |  | 18/6 = 3, ×20 = 60 |
| 19 | 4382408721980717508 | PASS |  | 6−12+8+8 = 10; only c |
| 20 | 4329261219534426627 | PASS |  | 8,55 + 45,50 = 54,05 €; 45,40 € also a multiple of 0,05, so not trivial (64,86 and 47,56 impossible-looking) |
| 21 | 1646624936382171282 | PASS |  | 400/10 = 40 |
| 22 | 4318315992289269181 | PASS |  | 75/5 = 15, mayor 60 |
| 23 | 3642917169328219885 | PASS |  | 27,55 + 25,20 = 52,75 €; 38,95 and 42,20 also multiples of 0,05 |
| 24 | 522745020435711845 | PASS |  | 112/4 = 28, mayor 84 |
| 25 | 3293218079445215240 | PASS |  | 4×18×11 = 792 |
| 26 | 4285634384778682878 | PASS |  | 6×9×10 = 540 |
| 27 | 4431004823014985952 | PASS |  | 2×10×7−8 = 132; only c |
| 28 | 318122278133970235 | PASS |  | 300/4 = 75 |
| 29 | 2650114669333005095 | PASS |  | 12/6 = 2, ×20 = 40 |
| 30 | 1749822834543286852 | PASS |  | 144/6 = 24, mayor 120 (distractor 144 is the sum itself, weak but one of three) |
| 31 | 51454947361655028 | PASS |  | 48/8 = 6, ×30 = 180 |
| 32 | 327419858050430848 | PASS |  | 280/7 = 40 |
| 33 | 1890776037983379231 | PASS |  | 16/8 = 2, ×30 = 60 |
| 34 | 2220669330088175677 | PASS |  | 350/7 = 50 |
| 35 | 1503781903715164646 | PASS |  | 30/15 = 2, ×30 = 60 |
| 36 | 1021355043926013886 | PASS |  | 57/3 = 19, mayor 38 |
| 37 | 3854091528299779889 | PASS |  | 1840/80 = 23 exact |
| 38 | 1436288844838428028 | PASS |  | 675/75 = 9 exact |
| 39 | 262654184820367357 | PASS |  | 240/6 = 40, mayor 200 |
| 40 | 2164152113904204897 | FAIL | generator (G1) | key 15,20 + 13,50 = 28,70 € right; only multiple of 0,05 € among 36,74, 22,96, 32,14 |
| 41 | 1262514110843238570 | PASS |  | 68/4 = 17, mayor 51 |
| 42 | 148281797622724415 | PASS |  | 720/40 = 18 exact |
| 43 | 376179894431768562 | PASS |  | 30/5 = 6, mayor 24 |
| 44 | 111790317788156661 | PASS |  | 960/120 = 8 exact |
| 45 | 2846568303615978718 | PASS |  | 5×17×11 = 935 |
| 46 | 822631935574881619 | PASS |  | 32/8 = 4, ×30 = 120 |
| 47 | 2201565206855591012 | FAIL | generator (G1) | key 19,50 + 21,00 = 40,50 € right; only multiple of 0,05 € among 45,36, 37,26, 43,74 |
| 48 | 3998441012288977609 | PASS |  | 45/5 = 9, mayor 36 |
| 49 | 545074174834871478 | PASS |  | 320/40 = 8 exact |
| 50 | 2541008619776365774 | PASS |  | 32/8 = 4, ×30 = 120 (same stem as item 46) |
