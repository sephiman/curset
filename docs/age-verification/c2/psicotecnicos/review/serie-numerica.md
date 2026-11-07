# serie-numerica — blind review, pass 2 (2026-11-07)

Items read: 50. PASS: 50. FAIL: 0 (generator: 0, bank: 0, other: 0).

## Defects

None.

Notes (not FAILs): each series was tested against constant difference, constant ratio, a·k+c for k in −5…5, constant second difference, geometric differences, alternating differences, period-3 differences, interleaved arithmetic/geometric subseries, product of the two previous terms and Fibonacci-type sums; every rule that fits all printed terms continues to the key and to no other option, and every explanation states the evident rule with the right constants. 13 items are plain constant-difference series (3, 16, 19, 26, 30, 33, 35, 36, 39, 40, 44, 48, 49), a rule the official exams have not used and easier than any official series; with the 13 geometric ones, 26 of 50 items are level 1 against 4 of 9 officially. Several distractors repeat the last printed term (3, 4, 16, 19, 25, 26, 36, 40), which is weak but does not make the item trivial. Items 1/7 and 38/41 are the same series.

## Items

| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 3604771523163253630 | PASS |  | ×2+3 → 445; differences doubling (7,14,…,112 → 224) gives the same; explanation constants right |
| 2 | 1029929555374405386 | PASS |  | ×3 → 1458; explanation constants right |
| 3 | 1979611701012040691 | PASS |  | +9 → 60; explanation constants right |
| 4 | 1764417533972442181 | PASS |  | +2/+4 → 37; odd and even subseries +6 give the same; explanation constants right |
| 5 | 3419230411813774580 | PASS |  | ×4 → 5120; explanation constants right |
| 6 | 3747516313772188681 | PASS |  | ×3+2 → 971; differences ×3 give the same; explanation constants right |
| 7 | 8906045121054210 | PASS |  | ×2+3 → 445 (same series as item 1); explanation constants right |
| 8 | 1251753948063375174 | PASS |  | 4×3=12, 12×4=48, 48×5 → 240; odd ratios 3, 4, 5 give the same; explanation constants right |
| 9 | 2486857284230662319 | PASS |  | odd ×3 (5,15,45) → 135; odd differences ×3 give the same; explanation constants right |
| 10 | 1733044026214489607 | PASS |  | ×2+3 → 381; differences doubling agree; explanation constants right |
| 11 | 1856184255990522582 | PASS |  | 4×4=16, 16×5=80, 80×6 → 480; explanation constants right |
| 12 | 4549720373993387178 | PASS |  | +6/+4 → 42; subseries +10 agree; explanation constants right |
| 13 | 3709953615204655391 | PASS |  | ×2+2 → 382; differences doubling agree; explanation constants right |
| 14 | 3358700057252487754 | PASS |  | odd +3 (14,17,20) → 23; no rule gives 25, 34 or 37; explanation constants right |
| 15 | 2174533955744055934 | PASS |  | odd +3 (20,23,26) → 29; 53 = 26+27 does not fit earlier terms; explanation constants right |
| 16 | 4160932674941954849 | PASS |  | +11 → 77; explanation constants right |
| 17 | 3442653701613644319 | PASS |  | +6/+5 → 48; explanation constants right |
| 18 | 798041086905868480 | PASS |  | ×3+1 → 364; differences ×3 agree; explanation constants right |
| 19 | 1994244535332229067 | PASS |  | +3 → 26; explanation constants right |
| 20 | 4498383089559541478 | PASS |  | odd +5 → 35; explanation constants right |
| 21 | 675205827688034035 | PASS |  | 7×4=28, 28×5=140, 140×6 → 840; explanation constants right |
| 22 | 3143207125806766687 | PASS |  | odd +5 (12,17,22) → 27; even ×3 does not reach the next place; explanation constants right |
| 23 | 73987587473345171 | PASS |  | 6×2=12, 12×3=36, 36×4 → 144; explanation constants right |
| 24 | 2361716341232386713 | PASS |  | ×3 → 3645; explanation constants right |
| 25 | 1301673169460145953 | PASS |  | +7/+2 → 45; explanation constants right |
| 26 | 997335447331209310 | PASS |  | +11 → 85; explanation constants right |
| 27 | 3280724319347399465 | PASS |  | ×5 → 9375; explanation constants right |
| 28 | 2544757775986322010 | PASS |  | ×2 → 64; explanation constants right |
| 29 | 4133575398624473562 | PASS |  | +5/+3 → 29; explanation constants right |
| 30 | 936157746112372867 | PASS |  | +9 → 57; explanation constants right |
| 31 | 2572126029900605142 | PASS |  | ÷2 → 2; explanation constants right |
| 32 | 933380389744726313 | PASS |  | ×3 → 243; explanation constants right |
| 33 | 2365392985742928710 | PASS |  | +9 → 50; explanation constants right |
| 34 | 1247575142543004649 | PASS |  | 6×4=24, 24×5=120, 120×6 → 720; explanation constants right |
| 35 | 2526779308609822140 | PASS |  | +7 → 50; explanation constants right |
| 36 | 3735633739687929708 | PASS |  | +7 → 67; explanation constants right |
| 37 | 1377197843310556201 | PASS |  | ×2 → 32; explanation constants right |
| 38 | 3576891544876999370 | PASS |  | ×5 → 12.500; explanation constants right |
| 39 | 2987734765612558358 | PASS |  | +3 → 30 (32 only from a two-term ratio 18→24, not a rule); explanation constants right |
| 40 | 3660729587619517528 | PASS |  | +4 → 37; explanation constants right |
| 41 | 810594159226467023 | PASS |  | ×5 → 12.500 (same series as item 38); explanation constants right |
| 42 | 30091656953621213 | PASS |  | ×2 → 384; explanation constants right |
| 43 | 2109365895759077397 | PASS |  | odd ×3 (3,9,27) → 81; explanation constants right |
| 44 | 2903947277564821649 | PASS |  | +6 → 52; explanation constants right |
| 45 | 2602254555950291676 | PASS |  | odd +6 (7,13,19) → 25; explanation constants right |
| 46 | 3439458644624803675 | PASS |  | ×3 → 2916; explanation constants right |
| 47 | 4350611285897345984 | PASS |  | 3×4=12, 12×5=60, 60×6 → 360; explanation constants right |
| 48 | 1290123354545949506 | PASS |  | +3 → 37; explanation constants right |
| 49 | 1443631564220235768 | PASS |  | +7 → 52; explanation constants right |
| 50 | 1050428420244466415 | PASS |  | ×3 → 1458; explanation constants right |
