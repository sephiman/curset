# calculo-porcentajes — blind review, pass 2 (2026-11-07)

Items read: 50. PASS: 50. FAIL: 0 (generator: 0, bank: 0, other: 0).

## Defects

None.

Notes (not FAILs): all 50 keys recomputed exactly, each the only option equal to the value rounded to 2 decimals; formats follow the official «41,40 €» / «25,83 %». Four-digit amounts are written without the thousands point («7200 €», «5184,00 €») and five-digit ones with it («36.000 €»), which is the RAE rule for four-digit numbers. Items 5 and 45 share the stem (250 €, +4 %). The explanation «No son mujeres 240 − 100 alumnos; …» is terse but states the complement route.

## Items

| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 142476236321150123 | PASS |  | 150×0,88 = 132,00 €; only option |
| 2 | 3153587093285155725 | PASS |  | 480×0,35 = 168; only option |
| 3 | 4329001598901702266 | PASS |  | 80×0,85 = 68,00 €; only option |
| 4 | 1955380656800656500 | PASS |  | 240×0,6 = 144; only option |
| 5 | 3725729493402152290 | PASS |  | 250×1,04 = 260,00 €; only option |
| 6 | 2117962402322770033 | PASS |  | 120×0,8 = 96,00 €; only option |
| 7 | 2487637828318621257 | PASS |  | 30/90 = 33,33 %; only option |
| 8 | 3959917021571138196 | PASS |  | 44/120 = 36,67 %; only option |
| 9 | 3380244725848317813 | PASS |  | 140/240 = 58,33 %; only option |
| 10 | 1742165302305072693 | PASS |  | 60×0,88 = 52,80 €; only option |
| 11 | 1436328498479605197 | PASS |  | 8/16 = 50,00 %; only option |
| 12 | 949102330877243704 | PASS |  | 640×0,25 = 160; only option |
| 13 | 3507599616719210045 | PASS |  | 7200×0,72 = 5184,00 €; only option |
| 14 | 2444709385026133203 | PASS |  | 640×0,15 = 96; only option |
| 15 | 1115103071644253775 | PASS |  | 640×0,45 = 288; only option |
| 16 | 4409944088174337134 | PASS |  | 840×0,4 = 336; only option |
| 17 | 3424707981635780303 | PASS |  | 240×0,4 = 96; only option |
| 18 | 474943732836401442 | PASS |  | 5/11 = 45,45 %; only option |
| 19 | 2083004938889697647 | PASS |  | 97/150 = 64,67 % (35,33 % is the women share, a fair distractor); only option |
| 20 | 2658154806036797156 | PASS |  | 9/15 = 60,00 %; only option |
| 21 | 3332189881007156579 | PASS |  | 120×0,88 = 105,60 €; only option |
| 22 | 253289811712211533 | PASS |  | 60×0,82 = 49,20 €; only option |
| 23 | 2279813371715836147 | PASS |  | 120×1,06 = 127,20 €; only option |
| 24 | 738087651520347043 | PASS |  | 640×0,6 = 384; only option |
| 25 | 3690242722077379150 | PASS |  | 1200×0,6 = 720; only option |
| 26 | 3228707284633840114 | PASS |  | 36.000×0,65 = 23.400,00 € (12.600 = the spent part, fair distractor); only option |
| 27 | 249066545599108635 | PASS |  | 127/180 = 70,556 → 70,56 %; only option |
| 28 | 1293261734414209284 | PASS |  | 12.000×0,65 = 7800,00 €; only option |
| 29 | 446028645736675108 | PASS |  | 60×0,95 = 57,00 €; only option |
| 30 | 1962857571478651500 | PASS |  | 36/64 = 56,25 %; only option |
| 31 | 745574515080052875 | PASS |  | 2/18 = 11,11 %; only option |
| 32 | 4038212545246269410 | PASS |  | 520×0,45 = 234; only option |
| 33 | 2054718432311410353 | PASS |  | 85/120 = 70,83 %; only option |
| 34 | 2446400661098218715 | PASS |  | 36×0,8 = 28,80 €; only option |
| 35 | 3290344809042648204 | PASS |  | 80×0,92 = 73,60 €; only option |
| 36 | 3917655122574107515 | PASS |  | 1200×0,15 = 180; only option |
| 37 | 4609789906695029675 | PASS |  | 150×0,95 = 142,50 €; only option |
| 38 | 75174881938818380 | PASS |  | 36.000×0,85 = 30.600,00 €; only option |
| 39 | 2766366196040747855 | PASS |  | 17/75 = 22,67 %; only option |
| 40 | 2107588891287733513 | PASS |  | 2/13 = 15,38 %; only option |
| 41 | 2646920204310311088 | PASS |  | 13/75 = 17,33 %; only option |
| 42 | 724692298527132179 | PASS |  | 177/240 = 73,75 %; only option |
| 43 | 779722059324555270 | PASS |  | 42/150 = 28,00 %; only option |
| 44 | 1001196424421381176 | PASS |  | 36×0,82 = 29,52 €; only option |
| 45 | 4415635058867538551 | PASS |  | 250×1,04 = 260,00 € (same stem as item 5); only option |
| 46 | 3696879942483886843 | PASS |  | 36×1,04 = 37,44 €; only option |
| 47 | 4358477514223734441 | PASS |  | 25.000×0,58 = 14.500,00 €; only option |
| 48 | 234027857163100231 | PASS |  | 3/10 = 30,00 %; only option |
| 49 | 1621960650965964255 | PASS |  | 120×1,12 = 134,40 €; only option |
| 50 | 3182904617473281507 | PASS |  | 90×0,82 = 73,80 €; only option |
