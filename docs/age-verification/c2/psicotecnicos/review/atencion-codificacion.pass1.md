# atencion-codificacion — blind review, pass 1 (2026-11-07)

Items read: 50. PASS: 28. FAIL: 22 (generator: 11, bank: 11, other: 0). Item 36 has both causes and is counted once, under generator.

Every key was recomputed in Python: binary blocks decoded against the printed equivalences (all six codes distinct in every item), digit words decoded, letter-class sums added letter by letter, and every «Clave de archivo» statement checked against its row. All 50 printed keys are correct and the only defensible option. The FAILs are realism and spelling defects.

## Defects
- G1 (generator): in the digit-word subtype («¿Qué palabra se obtiene al descodificar…?») the three distractors are scrambles that are not words (archiov, arhcivo, arcviho), so the key is the only real Spanish word and can be picked without decoding; some distractors are not even anagrams of the key (oifcfna, cfioina in 9). Items 3, 9, 11, 13, 16, 18, 23, 30, 36, 38, 46 (item 15 passes because «ofician» is also a word). The index gives no official example of this subtype, so this is judged on the brief's «distractor so absurd the item is trivial». Suggested fix: build distractors by decoding with one or two digit–letter pairs swapped and keep only those that differ from the key at a digit position, preferring results that are real words or near-words (oficina/ofician), or use a non-word code string as the official binary items do.
- B1 (bank): words are printed without their written accent, which is a spelling error in the stem or in the key: «tramites» for trámites (1, 5, 22, 26, 27, 31), «gestion» for gestión (14, 36, 39, 45, 47; in 36 it is the key option), «Martinez» for Martínez (43). Suggested fix: store the accented forms (trámites, gestión, Martínez) and classify á é í ó ú as vowels, or drop these entries from the bank.

Advisory, not counted as FAIL:
- A1: the «Clave de archivo» items use 4 positions; the official 2024X code has 6 positions × 4 values. The 4-position form is easier but a candidate would not see it as foreign. Each option also names the field («La posición 2 (custodia)»), so the candidate never has to find the row by number.
- A2: the «Clave de archivo» explanation only repeats the answer («la única falsa es: …»); saying what the digit decodes to («la cifra 2 es 0 = archivo, no oficina») would teach the check.

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 3167175567751435939 | FAIL | bank (B1) | key 30 (letter-class sum of «TRaMiTes»); word printed without its tilde |
| 2 | 4465995626877660290 | PASS | | key egef (four 4-digit blocks, codes unique) |
| 3 | 2414638611166857818 | FAIL | generator (G1) | key archivo (digits replaced); only the key is a real word |
| 4 | 4568015269300506277 | PASS | | key 42 (letter-class sum of «aRCHIVoS») |
| 5 | 2215247901385794297 | FAIL | bank (B1) | key 32 (letter-class sum of «TramITes»); word printed without its tilde |
| 6 | 4175173347260579743 | PASS | | clave 0113: only a) is CIERTA |
| 7 | 2391709619775052229 | PASS | | key gfee (four 4-digit blocks, codes unique) |
| 8 | 1863176285435730613 | PASS | | key gfad (four 4-digit blocks, codes unique) |
| 9 | 1602508387861334123 | FAIL | generator (G1) | key oficina (digits replaced); only the key is a real word |
| 10 | 1599557441512053633 | PASS | | key fdad (four 4-digit blocks, codes unique) |
| 11 | 3198995701451015775 | FAIL | generator (G1) | key registro (digits replaced); only the key is a real word |
| 12 | 3271328786901460905 | PASS | | key abcc (four 4-digit blocks, codes unique) |
| 13 | 1818467762689500913 | FAIL | generator (G1) | key oficina (digits replaced); only the key is a real word |
| 14 | 3507279643990949018 | FAIL | bank (B1) | key 40 (letter-class sum of «gestiON»); word printed without its tilde |
| 15 | 3232733006242683934 | PASS | | key oficina (digits replaced); «ofician» is a real word too, so decoding is needed |
| 16 | 3052284052258496994 | FAIL | generator (G1) | key archivo (digits replaced); only the key is a real word |
| 17 | 2120375140066735932 | PASS | | key ecde (four 4-digit blocks, codes unique) |
| 18 | 1463794077017128425 | FAIL | generator (G1) | key ventana (digits replaced); only the key is a real word |
| 19 | 331575075545083042 | PASS | | clave 0003: only b) is FALSA |
| 20 | 59091345861384708 | PASS | | clave 3303: only c) is FALSA |
| 21 | 3728727243465715397 | PASS | | key ccff (four 4-digit blocks, codes unique) |
| 22 | 3855469327430853671 | FAIL | bank (B1) | key 49 (letter-class sum of «TRaMiTES»); word printed without its tilde |
| 23 | 2307144971077380955 | FAIL | generator (G1) | key teclado (digits replaced); only the key is a real word |
| 24 | 4077319563193477691 | PASS | | key cbgb (four 4-digit blocks, codes unique) |
| 25 | 3186026344920370923 | PASS | | key 38 (letter-class sum of «OfIcINA») |
| 26 | 91365215922186741 | FAIL | bank (B1) | key 39 (letter-class sum of «trAmITeS»); word printed without its tilde |
| 27 | 1628141305348886531 | FAIL | bank (B1) | key 31 (letter-class sum of «trAMIteS»); word printed without its tilde |
| 28 | 2954680972709955460 | PASS | | clave 1132: only b) is CIERTA |
| 29 | 2015874354225302345 | PASS | | clave 3012: only d) is FALSA |
| 30 | 1529676557096434881 | FAIL | generator (G1) | key usuario (digits replaced); only the key is a real word |
| 31 | 2908773674053339039 | FAIL | bank (B1) | key 41 (letter-class sum of «tRamiteS»); word printed without its tilde |
| 32 | 45091008023642553 | PASS | | key 35 (letter-class sum of «OFiCINA») |
| 33 | 3956046606618673537 | PASS | | key 31 (letter-class sum of «SeLlado») |
| 34 | 2193356500958727543 | PASS | | key gfbf (four 4-digit blocks, codes unique) |
| 35 | 306428319324550081 | PASS | | key dede (four 4-digit blocks, codes unique) |
| 36 | 1952504928800109889 | FAIL | generator (G1), bank (B1) | key gestion (digits replaced); only the key is a real word; word printed without its tilde |
| 37 | 834599586222951670 | PASS | | key fedc (four 4-digit blocks, codes unique) |
| 38 | 2474667349443405148 | FAIL | generator (G1) | key ventana (digits replaced); only the key is a real word |
| 39 | 748262120684895621 | FAIL | bank (B1) | key 39 (letter-class sum of «GeStIoN»); word printed without its tilde |
| 40 | 1079058097590614563 | PASS | | clave 1022: only d) is FALSA |
| 41 | 3268200537010584946 | PASS | | key baeg (four 4-digit blocks, codes unique) |
| 42 | 3287665898356817018 | PASS | | key dage (four 4-digit blocks, codes unique) |
| 43 | 579285444686769818 | FAIL | bank (B1) | key 36 (letter-class sum of «MaRtInez»); word printed without its tilde |
| 44 | 2699695608080192048 | PASS | | key 35 (letter-class sum of «ReGiStro») |
| 45 | 3880715363111302178 | FAIL | bank (B1) | key 41 (letter-class sum of «GEStION»); word printed without its tilde |
| 46 | 1289249862356801085 | FAIL | generator (G1) | key carpeta (digits replaced); only the key is a real word |
| 47 | 1882981401235517409 | FAIL | bank (B1) | key 30 (letter-class sum of «geStIoN»); word printed without its tilde |
| 48 | 3938993709843485075 | PASS | | key eeda (four 4-digit blocks, codes unique) |
| 49 | 4034968673927375854 | PASS | | key faaf (four 4-digit blocks, codes unique) |
| 50 | 4552337786013420949 | PASS | | key bgad (four 4-digit blocks, codes unique) |
