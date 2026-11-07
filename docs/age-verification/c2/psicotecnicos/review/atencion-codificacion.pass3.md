# atencion-codificacion — blind review, pass 3 (2026-11-07)

Items read: 50. PASS: 46. FAIL: 4 (generator: 4, bank: 0, other: 0).

Every key was recomputed by script and by hand: 18 binary-block items, 14 digit-substitution items, 14 letter-class sums, 4 «Clave de archivo» items. All 50 keys are correct and are the only matching option; per-letter values in the letter-class explanations all match the stated classes (accented vowels counted as vowels; «Ll» in «SeLlado» and «CH» in «aRCHIVoS» counted as two letters, which the mixed case makes evident). The filing-code items match the official 2024X-P1-55 form: six positions × four values (0–3), CIERTA/FALSA over four position statements; in each, exactly one statement is true (CIERTA) or false (FALSA).

## Defects
- G1 (generator): the «Clave de archivo» explanation only repeats the right option («la única cierta/falsa es: …») without decoding the digits, so a candidate who erred is not shown why the distractors fail (e.g. in 40 that position 5 is 0 = Compras); items 20, 22, 28, 40. Suggested fix: spell out the six readings, e.g. «2=Este, 2=almacén, 0=baja, 3=2024, 0=Compras, 0=papel», then name the true/false statement.

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 3167175567751435939 | PASS | | «TRáMiTes» sums to 30; only option |
| 2 | 4465995626877660290 | PASS | | 4×4 blocks decode to egef; only option |
| 3 | 2414638611166857818 | PASS | | substitution gives ar16i27; only option |
| 4 | 4568015269300506277 | PASS | | «aRCHIVoS» sums to 42; only option |
| 5 | 2215247901385794297 | PASS | | «TrámITes» sums to 32; only option |
| 6 | 4175173347260579743 | PASS | | «Oficina» sums to 35; only option |
| 7 | 2391709619775052229 | PASS | | 4×4 blocks decode to gfee; only option |
| 8 | 1863176285435730613 | PASS | | 4×4 blocks decode to gfad; only option |
| 9 | 1602508387861334123 | PASS | | substitution gives 46818na; only option |
| 10 | 1599557441512053633 | PASS | | 4×4 blocks decode to fdad; only option |
| 11 | 3198995701451015775 | PASS | | substitution gives 5e1i4t59; only option |
| 12 | 3271328786901460905 | PASS | | 4×4 blocks decode to abcc; only option |
| 13 | 1818467762689500913 | PASS | | substitution gives 85ici71; only option |
| 14 | 3507279643990949018 | PASS | | «gestiÓN» sums to 40; only option |
| 15 | 3232733006242683934 | PASS | | substitution gives o68c839; only option |
| 16 | 3052284052258496994 | PASS | | substitution gives 7r5hi42; only option |
| 17 | 2120375140066735932 | PASS | | 4×4 blocks decode to ecde; only option |
| 18 | 1463794077017128425 | PASS | | substitution gives 461t212; only option |
| 19 | 331575075545083042 | PASS | | «GeStiÓN» sums to 16; only option |
| 20 | 59091345861384708 | FAIL | generator (G1) | key b correct and unique (100110 → custodia 1=oficina; año 1=2022, soporte 0=papel, sede 0=Norte); explanation does not show the digit readings |
| 21 | 3728727243465715397 | PASS | | 4×4 blocks decode to ccff; only option |
| 22 | 3855469327430853671 | FAIL | generator (G1) | key a correct and unique (210113 → soporte 1=disco; depto 1=Ventas, año 0=2021, urgencia 3=máxima); explanation does not show the digit readings |
| 23 | 2307144971077380955 | PASS | | substitution gives te7l842; only option |
| 24 | 4077319563193477691 | PASS | | 4×4 blocks decode to cbgb; only option |
| 25 | 3186026344920370923 | PASS | | «OfIcINA» sums to 38; only option |
| 26 | 91365215922186741 | PASS | | «trÁmITeS» sums to 39; only option |
| 27 | 1628141305348886531 | PASS | | «trÁMIteS» sums to 31; only option |
| 28 | 2954680972709955460 | FAIL | generator (G1) | key a correct and unique (323223 → soporte 2=cinta; depto 3=Informática, urgencia 2=alta, sede 3=Oeste); explanation does not show the digit readings |
| 29 | 2015874354225302345 | PASS | | «GEstIóN» sums to 43; only option |
| 30 | 1529676557096434881 | PASS | | substitution gives usu7918; only option |
| 31 | 2908773674053339039 | PASS | | «tRámiteS» sums to 41; only option |
| 32 | 45091008023642553 | PASS | | «OFiCINA» sums to 35; only option |
| 33 | 3956046606618673537 | PASS | | «SeLlado» sums to 31; only option |
| 34 | 2193356500958727543 | PASS | | 4×4 blocks decode to gfbf; only option |
| 35 | 306428319324550081 | PASS | | 4×4 blocks decode to dede; only option |
| 36 | 1952504928800109889 | PASS | | substitution gives 95m8r6o; only option |
| 37 | 834599586222951670 | PASS | | 4×4 blocks decode to fedc; only option |
| 38 | 2474667349443405148 | PASS | | substitution gives 9376a7a; only option |
| 39 | 748262120684895621 | PASS | | «GeStIóN» sums to 39; only option |
| 40 | 1079058097590614563 | FAIL | generator (G1) | key c correct and unique (220300 → depto 0=Compras, so «Ventas» is the only false one; a, b, d true); explanation does not show the digit readings |
| 41 | 3268200537010584946 | PASS | | 4×4 blocks decode to baeg; only option |
| 42 | 3287665898356817018 | PASS | | 4×4 blocks decode to dage; only option |
| 43 | 579285444686769818 | PASS | | «MaRtÍnez» sums to 36; only option |
| 44 | 2699695608080192048 | PASS | | «ReGiStro» sums to 35; only option |
| 45 | 3880715363111302178 | PASS | | «GEStIÓN» sums to 41; only option |
| 46 | 1289249862356801085 | PASS | | substitution gives 4ar385a; only option |
| 47 | 1882981401235517409 | PASS | | «geStIóN» sums to 30; only option |
| 48 | 3938993709843485075 | PASS | | 4×4 blocks decode to eeda; only option |
| 49 | 4034968673927375854 | PASS | | 4×4 blocks decode to faaf; only option |
| 50 | 4552337786013420949 | PASS | | 4×4 blocks decode to bgad; only option |
