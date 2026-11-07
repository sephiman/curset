# serie-numerica — blind review, pass 1 (2026-11-07)

Items read: 50. PASS: 0. FAIL: 50 (generator: 50, bank: 0, other: 0).

Keys: all 50 recomputed and right. For each series I tried a second simple rule (arithmetic, geometric, interleaved, differences, a·r+b, alternating operations, products): where two readings fit (alternating differences vs. interleaved arithmetic in 4, 12, 17, 25, 29; interleaved reading of a plain geometric series in 2) they give the same next term, and no other option is reachable by a simple rule. Stems and options match the official form («¿Qué número continúa la secuencia …, _?», plain integers) and the levels fit the index (simple progressions 1, interleaved and a·r+b 2). Every FAIL is the explanation.

## Defects
- E1 (generator): the explanation never states the rule's numbers: «suma una cantidad constante», «multiplicado (o dividido) por una razón constante», «multiplicado por una constante más otra constante», «son dos series intercaladas, cada una con su propia regla» — the brief's own example of too vague to teach; the candidate learns nothing about +9, ×3, ×2+3 or which subseries does what. All items except the product items (8, 11, 21, 23, 34, 47). Suggested fix: fill the template with the constants and, for interleaved series, both subseries («posiciones impares: 14, 17, 20, +3 → 23; pares: 5, 11, 17, +6»).
- E2 (generator): the explanation names a rule other than the evident one: plain arithmetic or geometric progressions are explained as «dos series intercaladas» (2, 16, 19, 24, 26, 28, 36, 42, 46, 48, 49) and plain geometric progressions as «multiplicado por una constante más otra constante» (5, 27, 32, 37, 38, 41, 50). Suggested fix: pick the explanation from the simplest rule that generates the printed terms (the solver's canonical rule), not from the family that drew the item.
- E3 (generator): product items say «cada término en posición par es el producto de los dos anteriores», but counting from the first term as a candidate does, the products sit in the odd positions (3rd, 5th, 7th: 12 = 4 × 3, 48 = 12 × 4, 240 = 48 × 5); the statement is wrong as read. Items 8, 11, 21, 23, 34, 47. Suggested fix: «los términos en posición impar, desde el tercero, son el producto de los dos anteriores: 48 × 5 = 240».

Notes (no FAIL): some distractors repeat the last printed term (3, 4, 16, 19, 25, 26, 36, 40) or double it (4, 12, 15, 17, 39, 40, 44, 49); in 12 and 49 that leaves only two live options. Not trivial, but weaker than the official distractors (300/320/280/340).

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 3604771523163253630 | FAIL | generator (E1) | key 445 right and unique; ×2+3 → 445 (differences 7, 14, 28… ×2 agree); constants not stated |
| 2 | 1029929555374405386 | FAIL | generator (E1, E2) | key 1458 right and unique; ×3 → 1458; called «dos series intercaladas» |
| 3 | 1979611701012040691 | FAIL | generator (E1) | key 60 right and unique; +9 → 60; «cantidad constante» not stated |
| 4 | 1764417533972442181 | FAIL | generator (E1) | key 37 right and unique; odd terms +6 (or differences +2, +4) → 37, both readings agree; subseries rules not stated |
| 5 | 3419230411813774580 | FAIL | generator (E1, E2) | key 5120 right and unique; ×4 → 5120; called «multiplicado por una constante más otra constante» |
| 6 | 3747516313772188681 | FAIL | generator (E1) | key 971 right and unique; ×3+2 → 971; constants not stated |
| 7 | 8906045121054210 | FAIL | generator (E1) | key 445 right and unique; ×2+3 → 445; constants not stated |
| 8 | 1251753948063375174 | FAIL | generator (E3) | key 240 right and unique; odd terms are products 4×3, 12×4, 48×5 → 240; explanation says «posición par» |
| 9 | 2486857284230662319 | FAIL | generator (E1) | key 135 right and unique; odd terms ×3 → 135 (even +6); subseries rules not stated |
| 10 | 1733044026214489607 | FAIL | generator (E1) | key 381 right and unique; ×2+3 → 381; constants not stated |
| 11 | 1856184255990522582 | FAIL | generator (E3) | key 480 right and unique; odd terms are products 4×4, 16×5, 80×6 → 480; explanation says «posición par» |
| 12 | 4549720373993387178 | FAIL | generator (E1) | key 42 right and unique; odd terms +10 (or differences +6, +4) → 42; subseries rules not stated |
| 13 | 3709953615204655391 | FAIL | generator (E1) | key 382 right and unique; ×2+2 → 382; constants not stated |
| 14 | 3358700057252487754 | FAIL | generator (E1) | key 23 right and unique; odd terms +3 → 23 (even +6); subseries rules not stated |
| 15 | 2174533955744055934 | FAIL | generator (E1) | key 29 right and unique; odd terms +3 → 29 (even +6); subseries rules not stated |
| 16 | 4160932674941954849 | FAIL | generator (E1, E2) | key 77 right and unique; +11 → 77; called «dos series intercaladas» |
| 17 | 3442653701613644319 | FAIL | generator (E1) | key 48 right and unique; odd terms +11 (or differences +6, +5) → 48; subseries rules not stated |
| 18 | 798041086905868480 | FAIL | generator (E1) | key 364 right and unique; ×3+1 → 364; constants not stated |
| 19 | 1994244535332229067 | FAIL | generator (E1, E2) | key 26 right and unique; +3 → 26; called «dos series intercaladas» |
| 20 | 4498383089559541478 | FAIL | generator (E1) | key 35 right and unique; odd terms +5 → 35 (even +2); subseries rules not stated |
| 21 | 675205827688034035 | FAIL | generator (E3) | key 840 right and unique; 140×6 → 840; explanation says «posición par» |
| 22 | 3143207125806766687 | FAIL | generator (E1) | key 27 right and unique; odd terms +5 → 27 (even ×3); subseries rules not stated |
| 23 | 73987587473345171 | FAIL | generator (E3) | key 144 right and unique; 36×4 → 144; explanation says «posición par» |
| 24 | 2361716341232386713 | FAIL | generator (E1, E2) | key 3645 right and unique; ×3 → 3645; called «dos series intercaladas» |
| 25 | 1301673169460145953 | FAIL | generator (E1) | key 45 right and unique; odd terms +9 (or differences +7, +2) → 45; subseries rules not stated |
| 26 | 997335447331209310 | FAIL | generator (E1, E2) | key 85 right and unique; +11 → 85; called «dos series intercaladas» |
| 27 | 3280724319347399465 | FAIL | generator (E1, E2) | key 9375 right and unique; ×5 → 9375; called «multiplicado por una constante más otra constante» |
| 28 | 2544757775986322010 | FAIL | generator (E1, E2) | key 64 right and unique; ×2 → 64; called «dos series intercaladas» |
| 29 | 4133575398624473562 | FAIL | generator (E1) | key 29 right and unique; odd terms +8 (or differences +5, +3) → 29; subseries rules not stated |
| 30 | 936157746112372867 | FAIL | generator (E1) | key 57 right and unique; +9 → 57; constant not stated |
| 31 | 2572126029900605142 | FAIL | generator (E1) | key 2 right and unique; ÷2 → 2; «razón constante» not stated |
| 32 | 933380389744726313 | FAIL | generator (E1, E2) | key 243 right and unique; ×3 → 243; called «multiplicado por una constante más otra constante» |
| 33 | 2365392985742928710 | FAIL | generator (E1) | key 50 right and unique; +9 → 50; constant not stated |
| 34 | 1247575142543004649 | FAIL | generator (E3) | key 720 right and unique; 120×6 → 720; explanation says «posición par» |
| 35 | 2526779308609822140 | FAIL | generator (E1) | key 50 right and unique; +7 → 50; constant not stated |
| 36 | 3735633739687929708 | FAIL | generator (E1, E2) | key 67 right and unique; +7 → 67; called «dos series intercaladas» |
| 37 | 1377197843310556201 | FAIL | generator (E1, E2) | key 32 right and unique; ×2 → 32 (31, the circle-regions reading, is not an option); called «multiplicado por una constante más otra constante» |
| 38 | 3576891544876999370 | FAIL | generator (E1, E2) | key 12.500 right and unique; ×5 → 12.500; called «multiplicado por una constante más otra constante» |
| 39 | 2987734765612558358 | FAIL | generator (E1) | key 30 right and unique; +3 → 30; constant not stated |
| 40 | 3660729587619517528 | FAIL | generator (E1) | key 37 right and unique; +4 → 37; constant not stated |
| 41 | 810594159226467023 | FAIL | generator (E1, E2) | key 12.500 right and unique; ×5 → 12.500; called «multiplicado por una constante más otra constante» |
| 42 | 30091656953621213 | FAIL | generator (E1, E2) | key 384 right and unique; ×2 → 384; called «dos series intercaladas» |
| 43 | 2109365895759077397 | FAIL | generator (E1) | key 81 right and unique; odd terms ×3 → 81 (even ×2); subseries rules not stated |
| 44 | 2903947277564821649 | FAIL | generator (E1) | key 52 right and unique; +6 → 52; constant not stated |
| 45 | 2602254555950291676 | FAIL | generator (E1) | key 25 right and unique; odd terms +6 → 25 (even +5); subseries rules not stated |
| 46 | 3439458644624803675 | FAIL | generator (E1, E2) | key 2916 right and unique; ×3 → 2916; called «dos series intercaladas» |
| 47 | 4350611285897345984 | FAIL | generator (E3) | key 360 right and unique; 60×6 → 360; explanation says «posición par» |
| 48 | 1290123354545949506 | FAIL | generator (E1, E2) | key 37 right and unique; +3 → 37; called «dos series intercaladas» |
| 49 | 1443631564220235768 | FAIL | generator (E1, E2) | key 52 right and unique; +7 → 52; called «dos series intercaladas» |
| 50 | 1050428420244466415 | FAIL | generator (E1, E2) | key 1458 right and unique; ×3 → 1458; called «multiplicado por una constante más otra constante» |
