# administrativo-clasificacion — blind review, pass 1 (2026-11-07)

Items read: 50. PASS: 25. FAIL: 25 (generator: 25, bank: 0, other: 0). B1 (bank) also applies to 6 of the generator FAILs.

Keys: all 50 recomputed (cabinet lookup; surname ranges with Spanish letter-by-letter order, accents ignored, ñ after n): every key is right and unique, the ranges are in order and every asked surname falls inside a range, not in a gap. The tela items copy the official 2020 item closely. Explanations name the range or the cabinet and drawer concretely; none fails.

## Defects
- G1 (generator): the cable and cuerda templates print «un bobina» («¿En qué ubicación guardarán un bobina de 25 metros de Sisal?»); «bobina» is feminine, so a candidate reads a grammar error in every such stem. Items 4, 9, 10, 11, 14, 15, 22, 24, 26, 27, 34, 37, 43, 44, 45, 48. Suggested fix: carry the article with the container noun («un rollo», «una bobina»).
- G2 (generator): the surname scheme can produce a drawer that holds a single surname («cajón 5: de Rojas a Rojas»; item 31 has three), which no real archive does and reads as a bug. Items 7, 19, 20, 21, 28, 30, 31, 32, 33. Suggested fix: draw range boundaries with at least one surname strictly between consecutive boundaries, or reject draws where a range's start equals its end.
- B1 (bank): the cable and cuerda banks include adjectives as type names (Plano, Flexible, Paralelo, Rígido, Apantallado, Trenzado/Trenzada), so stems read «un bobina de 10 metros de Plano», which is not how Spanish names a cable type. Items where the asked type is one: 9, 22, 24, 44, 45, 48. Suggested fix: keep only noun entries (cables: Coaxial, Fibra óptica, Cobre; cuerdas: Cáñamo, Sisal, Yute, Nailon, Algodón, Esparto).

Note (no FAIL): the surname items are all nivel 2 but most are decided at the first letter (Santos in Nieto–Zamora, Quintero in Lozano–Zamora); only a few need the 2nd–3rd letter (7 Molina/Moreno, 18 Díaz/Durán, 46 Rey/Rojas). Placing the asked surname next to a boundary more often would match the stated level and the index's «decided at the 3rd–5th letter».

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 2905171413568856296 | PASS | | Benítez → Cajón 1. only fit (Spanish order) |
| 2 | 2120614901432001151 | PASS | | Franela, 10 m → 2A |
| 3 | 3372990857722167844 | PASS | | Herrera → Cajón 2. only fit (Spanish order) |
| 4 | 4081202914252533723 | FAIL | generator (G1) | Sisal, 25 m → 5C, right; «un bobina» |
| 5 | 1328408313794206263 | PASS | | Santos → Cajón 6. only fit (Spanish order) |
| 6 | 4551224984430190870 | PASS | | Gabardina, 15 m → 1B |
| 7 | 4495506071432025915 | FAIL | generator (G2) | Molina → Cajón 2. only fit (Spanish order), right; one-surname drawer «de Rojas a Rojas» |
| 8 | 3893052480573515424 | PASS | | Gallego → Cajón 3. only fit (Spanish order) |
| 9 | 1113368139931146474 | FAIL | generator (G1); bank (B1) | Plano, 10 m → 1A, right; «un bobina»; type «Plano» is an adjective |
| 10 | 747090381621175415 | FAIL | generator (G1) | Nailon, 10 m → 4A, right; «un bobina» |
| 11 | 1042665603002150715 | FAIL | generator (G1) | Cáñamo, 10 m → 5A, right; «un bobina» |
| 12 | 369170782676929511 | PASS | | Moreno → Cajón 4. only fit (Spanish order) |
| 13 | 3463711355764829693 | PASS | | Castro → Cajón 1. only fit (Spanish order) |
| 14 | 2012502241861686181 | FAIL | generator (G1) | Coaxial, 15 m → 4B, right; «un bobina» |
| 15 | 4125722512877743755 | FAIL | generator (G1) | Sisal, 25 m → 4C, right; «un bobina» |
| 16 | 2868982601802913990 | PASS | | Crespo → Cajón 1. only fit (Spanish order) |
| 17 | 876322470897413790 | PASS | | Iglesias → Cajón 2. only fit (Spanish order) |
| 18 | 476091560135898611 | PASS | | Díaz → Cajón 3. only fit (Spanish order) |
| 19 | 2097352417082531498 | FAIL | generator (G2) | Cano → Cajón 1. only fit (Spanish order), right; one-surname drawer «de Ibáñez a Ibáñez» |
| 20 | 587241960816378758 | FAIL | generator (G2) | Quintero → Cajón 6. only fit (Spanish order), right; one-surname drawer «de Herrera a Herrera» |
| 21 | 3516795561458811259 | FAIL | generator (G2) | Bravo → Cajón 1. only fit (Spanish order), right; one-surname drawer «de Ruiz a Ruiz» |
| 22 | 2558837762794217705 | FAIL | generator (G1); bank (B1) | Flexible, 15 m → 7B, right; «un bobina»; type «Flexible» is an adjective |
| 23 | 684010108173381283 | PASS | | Pardo → Cajón 5. only fit (Spanish order) |
| 24 | 1628792368968939207 | FAIL | generator (G1); bank (B1) | Trenzado, 10 m → 6A, right; «un bobina»; type «Trenzado» is an adjective |
| 25 | 721045023008609602 | PASS | | Gabardina, 15 m → 4B |
| 26 | 1220475526916630724 | FAIL | generator (G1) | Sisal, 10 m → 5A, right; «un bobina» |
| 27 | 3176507720932832904 | FAIL | generator (G1) | Algodón, 15 m → 1B, right; «un bobina» |
| 28 | 4090706388276574091 | FAIL | generator (G2) | Ibáñez → Cajón 3. only fit (Spanish order), right; one-surname drawer «de Peña a Peña» |
| 29 | 1393354275355015028 | PASS | | Gabardina, 25 m → 4C |
| 30 | 2618592839315439520 | FAIL | generator (G2) | Castro → Cajón 1. only fit (Spanish order), right; one-surname drawer «de Iglesias a Iglesias», «de Ruiz a Ruiz» |
| 31 | 4515498070327445420 | FAIL | generator (G2) | Alonso → Cajón 1. only fit (Spanish order), right; one-surname drawer three one-surname drawers (Cano, Castro, Cortés) |
| 32 | 4387838571931312365 | FAIL | generator (G2) | Barrios → Cajón 1. only fit (Spanish order), right; one-surname drawer «de Castro a Castro» |
| 33 | 2273051828560295678 | FAIL | generator (G2) | Blanco → Cajón 1. only fit (Spanish order), right; one-surname drawer «de Navarro a Navarro» |
| 34 | 3145280539747514324 | FAIL | generator (G1) | Fibra, 15 m → 1B, right; «un bobina» |
| 35 | 3149934762592494150 | PASS | | Barrios → Cajón 1. only fit (Spanish order) |
| 36 | 1688487807612521401 | PASS | | Lino, 15 m → 1B |
| 37 | 2460083319849257704 | FAIL | generator (G1) | Yute, 10 m → 5A, right; «un bobina» |
| 38 | 2069325991953587449 | PASS | | Tweed, 25 m → 1C |
| 39 | 3524090669165052630 | PASS | | Gabardina, 25 m → 1C |
| 40 | 128479231797070650 | PASS | | Ortega → Cajón 4. only fit (Spanish order) |
| 41 | 4074712633999301858 | PASS | | Raso, 15 m → 5B |
| 42 | 923653918054675225 | PASS | | Raso, 25 m → 5C |
| 43 | 3910416812521792119 | FAIL | generator (G1) | Sisal, 15 m → 8B, right; «un bobina» |
| 44 | 41946785815617651 | FAIL | generator (G1); bank (B1) | Trenzada, 15 m → 6B, right; «un bobina»; type «Trenzada» is an adjective |
| 45 | 3498574836558340425 | FAIL | generator (G1); bank (B1) | Apantallado, 10 m → 2A, right; «un bobina»; type «Apantallado» is an adjective |
| 46 | 553914276719877251 | PASS | | Rey → Cajón 5. only fit (Spanish order) |
| 47 | 1501201975478940769 | PASS | | Batista, 10 m → 5A |
| 48 | 3607594572106293573 | FAIL | generator (G1); bank (B1) | Apantallado, 25 m → 1C, right; «un bobina»; type «Apantallado» is an adjective |
| 49 | 1109080077563619697 | PASS | | Aguirre → Cajón 1. only fit (Spanish order) |
| 50 | 2972229859820299606 | PASS | | Crepé, 25 m → 1C |
