# calculo-porcentajes — blind review, pass 1 (2026-11-07)

Items read: 50. PASS: 38. FAIL: 12 (generator: 6, bank: 6, other: 0).

All 50 keys recomputed with exact fractions: every key is right and is the only option equal to the value rounded to 2 decimals. Explanations name the official route (pay the complement, 104 %, part / total × 100) with the concrete numbers; none fails.

## Defects
- G1 (generator): one-multiplication discount/increase items with friendly numbers are labelled nivel 2 while the same template with equal or harder numbers is nivel 1 (25 % of 60, 30 % of 60, 5 % of 75, 10 % of 120 at nivel 2 against 18 % of 60, 12 % of 120, 8 % of 80 at nivel 1); the index puts one multiplication at level 1. Items 11, 20, 40, 47. Suggested fix: derive the level from the operation count / base size of the subtype, not from a separate draw, so discount and increase items are nivel 1 unless the base is large.
- G2 (generator): in discount items some distractors are above the original price without being the sign-flip error (63,84 € and 72,96 € on 60 € −5 %; 37,79 € on 36 € −18 %); with the other natural distractor far off, only the key survives a glance. Items 29, 44. The same kind of wrong-side, non-natural distractor appears singly (no FAIL, the item still needs the computation) in 5 (249,60 € for a rise on 250 €), 28 (7833,60 € left of a 7200 € budget), 45 (239,20 € for a rise on 250 €), 47 (105,60 € for a rise on 120 €). Suggested fix: keep every distractor on the side of the base the stem implies, except the one deliberate sign-flip distractor (base × (1 ± p)).
- B1 (bank): the product noun «un material de oficina» («Si hay un 20 % de descuento en un material de oficina cuyo precio original…») is unnatural Spanish: «material de oficina» is a mass noun and does not take «un» for one priced item. Items 6, 10, 21, 22, 34, 44, 50. Suggested fix: replace the entry with a countable noun («una impresora», «una silla de oficina», «un lote de material de oficina»).

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 142476236321150123 | PASS | | 150 × 0,88 = 132,00 € only fit |
| 2 | 3153587093285155725 | PASS | | 480 × 0,35 = 168 |
| 3 | 4329001598901702266 | PASS | | 80 × 0,85 = 68,00 €; 92 € is the sign-flip distractor |
| 4 | 1955380656800656500 | PASS | | 240 × 0,6 = 144 |
| 5 | 3725729493402152290 | PASS | | 250 × 1,04 = 260,00 €; 254 € (+4 €) good trap; 249,60 € wrong-side (G2 note) |
| 6 | 2117962402322770033 | FAIL | bank (B1) | key 96,00 € right; «un material de oficina» |
| 7 | 2487637828318621257 | PASS | | 30/90 = 33,33 % |
| 8 | 3959917021571138196 | PASS | | 44/120 = 36,67 % |
| 9 | 3380244725848317813 | PASS | | 8/19 = 42,11 %; 47,06 % (8/17) good trap |
| 10 | 1742165302305072693 | FAIL | bank (B1) | key 52,80 € right; «un material de oficina» |
| 11 | 1436328498479605197 | FAIL | generator (G1) | 60 × 0,75 = 45,00 € right; nivel 2 for a level-1 computation |
| 12 | 949102330877243704 | PASS | | 640/4 = 160 |
| 13 | 3507599616719210045 | PASS | | 2/17 = 11,76 %; close options need the division, fits nivel 2 |
| 14 | 2444709385026133203 | PASS | | 640 × 0,15 = 96 |
| 15 | 1115103071644253775 | PASS | | 640 × 0,45 = 288 |
| 16 | 4409944088174337134 | PASS | | 840 × 0,4 = 336 |
| 17 | 3424707981635780303 | PASS | | 240 × 0,4 = 96 |
| 18 | 474943732836401442 | PASS | | 4500 × 0,65 = 2925,00 € |
| 19 | 2083004938889697647 | PASS | | 7/16 = 43,75 % |
| 20 | 2658154806036797156 | FAIL | generator (G1) | 60 × 0,7 = 42,00 € right; nivel 2 for a level-1 computation |
| 21 | 3332189881007156579 | FAIL | bank (B1) | key 105,60 € right; «un material de oficina» |
| 22 | 253289811712211533 | FAIL | bank (B1) | key 49,20 € right; «un material de oficina» |
| 23 | 2279813371715836147 | PASS | | 120 × 1,06 = 127,20 € |
| 24 | 738087651520347043 | PASS | | 640 × 0,6 = 384 |
| 25 | 3690242722077379150 | PASS | | 1200 × 0,6 = 720 |
| 26 | 3228707284633840114 | PASS | | 6/19 = 31,58 % |
| 27 | 249066545599108635 | PASS | | 127/180 = 70,56 % |
| 28 | 1293261734414209284 | PASS | | 7200 × 0,85 = 6120,00 €; 7833,60 € exceeds the budget (G2 note) |
| 29 | 446028645736675108 | FAIL | generator (G2) | 60 × 0,95 = 57,00 € right; 63,84 € and 72,96 € above the price, 47,88 € far off: trivial |
| 30 | 1962857571478651500 | PASS | | 6/20 = 30,00 % |
| 31 | 745574515080052875 | PASS | | 25.000 × 0,72 = 18.000,00 € |
| 32 | 4038212545246269410 | PASS | | 520 × 0,45 = 234 |
| 33 | 2054718432311410353 | PASS | | 85/120 = 70,83 % |
| 34 | 2446400661098218715 | FAIL | bank (B1) | key 28,80 € right; «un material de oficina» |
| 35 | 3290344809042648204 | PASS | | 80 × 0,92 = 73,60 € |
| 36 | 3917655122574107515 | PASS | | 1200 × 0,15 = 180 |
| 37 | 4609789906695029675 | PASS | | 150 × 0,95 = 142,50 € |
| 38 | 75174881938818380 | PASS | | 85/120 = 70,83 % |
| 39 | 2766366196040747855 | PASS | | 17/75 = 22,67 % |
| 40 | 2107588891287733513 | FAIL | generator (G1) | 75 × 0,95 = 71,25 € right; nivel 2 while 5 % of 150 (item 37) is nivel 1 |
| 41 | 2646920204310311088 | PASS | | 13/75 = 17,33 % |
| 42 | 724692298527132179 | PASS | | 3/21 = 14,29 %; 25,00 % (3/12) good trap |
| 43 | 779722059324555270 | PASS | | 42/150 = 28,00 % |
| 44 | 1001196424421381176 | FAIL | generator (G2); bank (B1) | 36 × 0,82 = 29,52 € right; 42,48 € and 37,79 € above the price, 18,00 € far off: trivial; «un material de oficina» |
| 45 | 4415635058867538551 | PASS | | 250 × 1,04 = 260,00 €; 239,20 € wrong-side (G2 note) |
| 46 | 3696879942483886843 | PASS | | 36 × 1,04 = 37,44 € |
| 47 | 4358477514223734441 | FAIL | generator (G1) | 120 × 1,1 = 132,00 € right; 10 % rise labelled nivel 2 while 12 % (item 49) is nivel 1 |
| 48 | 234027857163100231 | PASS | | 25.000 × 0,36 = 9000,00 € |
| 49 | 1621960650965964255 | PASS | | 120 × 1,12 = 134,40 € |
| 50 | 3182904617473281507 | FAIL | bank (B1) | key 73,80 € right; «un material de oficina» |
