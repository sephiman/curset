# calculo-problemas — blind review, pass 4 (2026-11-07)

Items read: 50. PASS: 50. FAIL: 0 (generator: 0, bank: 0, other: 0).

Every key recomputed in Python with exact fractions: 50 of 50 match and each key is the only option that fits. In the five operator items all 27 operator combinations were tried left to right: exactly one gives the target in each, and it is the key (the stem fixes the left-to-right reading, so precedence is not a second reading). Distractors in the purchase items include the price-swap and the single-price slips; no option is absurd enough to make an item trivial.

## Defects

None that fail an item.

Remarks (not FAILs):
- N1: the razón-y-suma explanation («El menor es 48 / 3 = 16; el mayor es 2 × 16 = 32») does not say why it divides by 3; adding «(1 + 2 = 3 partes)» would state the taught route (items 8, 22, 24, 30, 36, 39, 41, 43, 48).
- N2: parameter variety is thin: items 46 and 50 are the same problem (8 cuadernos, 32 €, 30 cuadernos) with different options; items 3, 13, 20 repeat «19 bolígrafos a 0,45 €» and «carpetas a 3,25 €»; items 1, 6 and 9 repeat 16/18 filas de 9. Harmless in an exam draw, visible in a practice run.
- N3: in the precio-unitario items the money answer is a bare number («54.») while the purchase items print «31,30 €»; «54 €» would match the official money format.
- N4: the gratificación explanation names a trap («no entre 30») that no distractor uses; harmless.
- N5: operator options and explanations use the hyphen «-» where the other explanations use «−».

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 180558790999070772 | PASS | | producto 3 factores: recomputed 432, key c only fit |
| 2 | 1278440966805938998 | PASS | | días hasta capacidad: recomputed 12 días, key c only fit |
| 3 | 51261528581274285 | PASS | | suma de productos: recomputed 31,30 €, key b only fit; 64,90 swaps prices, 84,50 = 26 × 3,25 |
| 4 | 2260400680357392001 | PASS | | reparto entre subgrupo: recomputed 75, key a only fit |
| 5 | 1554470352242268824 | PASS | | producto 3 factores: recomputed 1134, key c only fit |
| 6 | 2711105301957622312 | PASS | | producto 3 factores: recomputed 864, key b only fit |
| 7 | 2040222635848061935 | PASS | | reparto entre subgrupo: recomputed 120, key a only fit |
| 8 | 1753115355312637349 | PASS | | razón y suma: recomputed 32, key c only fit |
| 9 | 3898307950440185802 | PASS | | producto 3 factores: recomputed 1296, key d only fit |
| 10 | 4514091041932310672 | PASS | | operadores izq.→dcha.: recomputed -, +, +, key c only fit; only (−,+,+) of the 27 combinations gives 23 |
| 11 | 3071096475260907629 | PASS | | suma de productos: recomputed 76,40 €, key b only fit |
| 12 | 4333413335859233782 | PASS | | suma de productos: recomputed 70,60 €, key a only fit |
| 13 | 2874833144572324357 | PASS | | suma de productos: recomputed 24,80 €, key a only fit; 64,00 swaps prices |
| 14 | 2273078969149923779 | PASS | | operadores izq.→dcha.: recomputed ×, +, -, key a only fit; only (×,+,−) of 27 gives 29 |
| 15 | 1360915602804834736 | PASS | | precio unitario: recomputed 54, key b only fit |
| 16 | 1776246719887320771 | PASS | | operadores izq.→dcha.: recomputed +, +, -, key d only fit; only (+,+,−) of 27 gives 8 |
| 17 | 2690789185829586602 | PASS | | días hasta capacidad: recomputed 10 días, key c only fit |
| 18 | 1829329591002600448 | PASS | | precio unitario: recomputed 60, key a only fit; only multiple of 3 among options |
| 19 | 4382408721980717508 | PASS | | operadores izq.→dcha.: recomputed -, +, +, key c only fit; only (−,+,+) of 27 gives 10; negative intermediate −6 |
| 20 | 4329261219534426627 | PASS | | suma de productos: recomputed 54,05 €, key a only fit |
| 21 | 1646624936382171282 | PASS | | reparto entre subgrupo: recomputed 40, key a only fit |
| 22 | 4318315992289269181 | PASS | | razón y suma: recomputed 60, key b only fit |
| 23 | 3642917169328219885 | PASS | | suma de productos: recomputed 52,75 €, key c only fit |
| 24 | 522745020435711845 | PASS | | razón y suma: recomputed 84, key c only fit |
| 25 | 3293218079445215240 | PASS | | producto 3 factores: recomputed 792, key a only fit |
| 26 | 4285634384778682878 | PASS | | producto 3 factores: recomputed 540, key d only fit |
| 27 | 4431004823014985952 | PASS | | operadores izq.→dcha.: recomputed ×, ×, -, key c only fit; only (×,×,−) of 27 gives 132 |
| 28 | 318122278133970235 | PASS | | reparto entre subgrupo: recomputed 75, key b only fit |
| 29 | 2650114669333005095 | PASS | | precio unitario: recomputed 40, key b only fit; only even option (unit 2 €), still one step |
| 30 | 1749822834543286852 | PASS | | razón y suma: recomputed 120, key b only fit |
| 31 | 51454947361655028 | PASS | | precio unitario: recomputed 180, key d only fit |
| 32 | 327419858050430848 | PASS | | reparto entre subgrupo: recomputed 40, key d only fit |
| 33 | 1890776037983379231 | PASS | | precio unitario: recomputed 60, key c only fit |
| 34 | 2220669330088175677 | PASS | | reparto entre subgrupo: recomputed 50, key b only fit |
| 35 | 1503781903715164646 | PASS | | precio unitario: recomputed 60, key b only fit |
| 36 | 1021355043926013886 | PASS | | razón y suma: recomputed 38, key d only fit |
| 37 | 3854091528299779889 | PASS | | días hasta capacidad: recomputed 23 días, key c only fit |
| 38 | 1436288844838428028 | PASS | | días hasta capacidad: recomputed 9 días, key c only fit |
| 39 | 262654184820367357 | PASS | | razón y suma: recomputed 200, key c only fit |
| 40 | 2164152113904204897 | PASS | | suma de productos: recomputed 28,70 €, key a only fit |
| 41 | 1262514110843238570 | PASS | | razón y suma: recomputed 51, key b only fit |
| 42 | 148281797622724415 | PASS | | días hasta capacidad: recomputed 18 días, key c only fit |
| 43 | 376179894431768562 | PASS | | razón y suma: recomputed 24, key d only fit |
| 44 | 111790317788156661 | PASS | | días hasta capacidad: recomputed 8 días, key b only fit |
| 45 | 2846568303615978718 | PASS | | producto 3 factores: recomputed 935, key c only fit |
| 46 | 822631935574881619 | PASS | | precio unitario: recomputed 120, key c only fit; same numbers as item 50 |
| 47 | 2201565206855591012 | PASS | | suma de productos: recomputed 40,50 €, key c only fit |
| 48 | 3998441012288977609 | PASS | | razón y suma: recomputed 36, key d only fit |
| 49 | 545074174834871478 | PASS | | días hasta capacidad: recomputed 8 días, key b only fit |
| 50 | 2541008619776365774 | PASS | | precio unitario: recomputed 120, key b only fit; same numbers as item 46 |
