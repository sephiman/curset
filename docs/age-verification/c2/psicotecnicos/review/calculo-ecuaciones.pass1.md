# calculo-ecuaciones — blind review, pass 1 (2026-11-07)

Items read: 50. PASS: 50. FAIL: 0 (generator: 0, bank: 0, other: 0).

Every equation was solved in Python with exact fractions and the result rounded half-up to 2 decimals. All 50 printed keys match the rounded value; in no item does the truncated value (the 2020 official habit, e.g. −0,6757 → «−0,67») coincide with a different option, so rounding versus truncation never makes two options defensible. Every explanation's «ax = b» reduces to the same solution. Form a(bx ± c) = dx + e or e − dx = a(x − c), coefficients and constants inside the official range, and the levels match the index (nivel 1 exactly for the three integer solutions: 4, 11, 17).

## Defects
None.

Advisory, not counted as FAIL:
- A1: the explanation jumps from the equation to «34x = 89»; showing the expanded line once («36x − 72 = 2x + 17») would make the route a candidate is taught explicit, especially when the sign flips (3: «−28x − 350 = 9x + 21» printed as «37x = −371»).
- A2: negatives are printed with a hyphen («-10,03»); a typographic minus («−10,03») is the form in the index's transcriptions.

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 2226927027398353954 | PASS | | key 2,62: 34x = 89, x = 2,6176; no truncation clash |
| 2 | 2183089472243988427 | PASS | | key 3,48: -25x = -87, x = 3,4800; no truncation clash |
| 3 | 404803762646097728 | PASS | | key -10,03: -37x = 371, x = -10,0270; no truncation clash |
| 4 | 1687612876087919413 | PASS | | key -8: 3x = -24, integer |
| 5 | 243518984827179051 | PASS | | key 3,88: -17x = -66, x = 3,8824; no truncation clash |
| 6 | 343766486458628376 | PASS | | key 3,45: 180x = 621, x = 3,4500; no truncation clash |
| 7 | 2205036454641259424 | PASS | | key 4,64: -22x = -102, x = 4,6364; no truncation clash |
| 8 | 654847202426281987 | PASS | | key 4,13: 194x = 801, x = 4,1289; no truncation clash |
| 9 | 166053260362945965 | PASS | | key -6,12: -113x = 692, x = -6,1239; no truncation clash |
| 10 | 706317801245479882 | PASS | | key -22,50: -28x = 630, x = -22,5000; no truncation clash |
| 11 | 4387615036570604073 | PASS | | key -6: -15x = 90, integer |
| 12 | 3471482187590819963 | PASS | | key 17,92: -13x = -233, x = 17,9231; no truncation clash |
| 13 | 4407462498518999457 | PASS | | key 5,70: -27x = -154, x = 5,7037; no truncation clash |
| 14 | 547410036944736976 | PASS | | key 3,79: 58x = 220, x = 3,7931; no truncation clash |
| 15 | 2485879207418477570 | PASS | | key 1,93: -27x = -52, x = 1,9259; no truncation clash |
| 16 | 3798411885256561511 | PASS | | key -2,30: -181x = 417, x = -2,3039; no truncation clash |
| 17 | 4353883021363900545 | PASS | | key -5: -24x = 120, integer |
| 18 | 4200701442120315785 | PASS | | key 10,22: -18x = -184, x = 10,2222; no truncation clash |
| 19 | 3357144374415288654 | PASS | | key 33,50: 2x = 67, x = 33,5000; no truncation clash |
| 20 | 939413482359747115 | PASS | | key 5,25: -8x = -42, x = 5,2500; no truncation clash |
| 21 | 2368019832978027031 | PASS | | key 8,40: -10x = -84, x = 8,4000; no truncation clash |
| 22 | 841962442338370970 | PASS | | key 3,73: -22x = -82, x = 3,7273; no truncation clash |
| 23 | 2010255594933495171 | PASS | | key 7,38: 16x = 118, x = 7,3750; no truncation clash |
| 24 | 2867638287619122265 | PASS | | key -2,11: -180x = 380, x = -2,1111; no truncation clash |
| 25 | 3919231382380045124 | PASS | | key 7,40: -10x = -74, x = 7,4000; no truncation clash |
| 26 | 3561951912193679764 | PASS | | key 0,50: 205x = 102, x = 0,4976; no truncation clash |
| 27 | 1414345035477793999 | PASS | | key 4,76: -17x = -81, x = 4,7647; no truncation clash |
| 28 | 1779904065475435431 | PASS | | key 7,13: -16x = -114, x = 7,1250; no truncation clash |
| 29 | 4314660286558051745 | PASS | | key 3,17: 18x = 57, x = 3,1667; no truncation clash |
| 30 | 2111470234278424055 | PASS | | key 5,94: -32x = -190, x = 5,9375; no truncation clash |
| 31 | 865239775855985511 | PASS | | key -3,11: -200x = 621, x = -3,1050; no truncation clash |
| 32 | 3012594628465807155 | PASS | | key 15,68: -38x = -596, x = 15,6842; no truncation clash |
| 33 | 1788692189745688926 | PASS | | key 6,65: -26x = -173, x = 6,6538; no truncation clash |
| 34 | 2339366065953537568 | PASS | | key 1,86: -7x = -13, x = 1,8571; no truncation clash |
| 35 | 4249084410206665994 | PASS | | key 2,70: -10x = -27, x = 2,7000; no truncation clash |
| 36 | 1113969408436792603 | PASS | | key 4,47: 36x = 161, x = 4,4722; no truncation clash |
| 37 | 2128670164493241985 | PASS | | key 4,41: -32x = -141, x = 4,4062; no truncation clash |
| 38 | 2021850630852417764 | PASS | | key 4,85: -26x = -126, x = 4,8462; no truncation clash |
| 39 | 2862515124131407866 | PASS | | key 2,97: -33x = -98, x = 2,9697; no truncation clash |
| 40 | 1738612174352676445 | PASS | | key 9,35: -17x = -159, x = 9,3529; no truncation clash |
| 41 | 3914599193106638638 | PASS | | key 0,15: -131x = -20, x = 0,1527; no truncation clash |
| 42 | 4487108973369358160 | PASS | | key 2,19: -32x = -70, x = 2,1875; no truncation clash |
| 43 | 1493994991637926998 | PASS | | key 5,20: -10x = -52, x = 5,2000; no truncation clash |
| 44 | 4428342542711124849 | PASS | | key 3,93: -28x = -110, x = 3,9286; no truncation clash |
| 45 | 2405804462862590377 | PASS | | key -2,25: 63x = -142, x = -2,2540; no truncation clash |
| 46 | 4109708408076377924 | PASS | | key 13,75: -8x = -110, x = 13,7500; no truncation clash |
| 47 | 3307706073234414067 | PASS | | key -1,01: -69x = 70, x = -1,0145; no truncation clash |
| 48 | 583955574211673912 | PASS | | key 3,02: -223x = -674, x = 3,0224; no truncation clash |
| 49 | 1880341808981504982 | PASS | | key 10,50: -24x = -252, x = 10,5000; no truncation clash |
| 50 | 4562669751112520438 | PASS | | key 5,11: -9x = -46, x = 5,1111; no truncation clash |
