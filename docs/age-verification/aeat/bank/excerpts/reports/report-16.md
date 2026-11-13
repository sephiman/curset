# Excerpt check — batch 16

| n | key | verdict | note |
|---|---|---|---|
| 901 | m03-l05-q0198 | yes |  |
| 902 | m03-l05-q0200 | yes |  |
| 903 | m03-l05-q0202 | yes |  |
| 904 | m03-l05-q0205 | yes |  |
| 905 | m03-l05-q0206 | yes |  |
| 906 | m03-l05-q0207 | full-only | cite «art. 103» (prompt names 103.b): excerpt shows the opening and letra a) only; letra b) («Este plazo de interrupción es independiente del regulado en el párrafo a)») in full |
| 907 | m03-l05-q0208 | yes |  |
| 908 | m03-l05-q0209 | full-only | cite «art. 103» (prompt names 103.d): excerpt shows letra a); letra d) (actuaciones judiciales en el ámbito penal) in full |
| 909 | m03-l05-q0210 | yes |  |
| 910 | m03-l05-q0211 | full-only | cite «art. 103» (prompt names 103.f): excerpt shows letra a); letra f) (Juntas Arbitrales, «hasta la resolución dictada por la respectiva Junta Arbitral») in full |
| 911 | m03-l05-q0212 | full-only | cite «art. 103», no letter in the prompt: excerpt shows letra a); the fuerza mayor of letra e) in full |
| 912 | m03-l05-q0215 | yes |  |
| 913 | m03-l05-q0216 | yes |  |
| 914 | m03-l05-q0217 | yes |  |
| 915 | m03-l05-q0219 | yes |  |
| 916 | m03-l05-q0220 | full-only | cite «art. 104» (prompt names 104.f): excerpt shows letras a)–b); letra f) (complementarias o sustitutivas) in full |
| 917 | m03-l05-q0221 | full-only | cite «art. 104» (prompt names 104.g): excerpt shows letras a)–b); letra g) («desde el inicio de un procedimiento en el que pueda surtir efectos, hasta la fecha de su presentación») in full |
| 918 | m03-l05-q0222 | yes |  |
| 919 | m03-l05-q0224 | yes |  |
| 920 | m03-l05-q0225 | yes |  |
| 921 | m03-l05-q0226 | yes |  |
| 922 | m03-l05-q0227 | yes |  |
| 923 | m03-l05-q0228 | yes |  |
| 924 | m03-l05-q0230 | yes |  |
| 925 | m03-l05-q0233 | no | excerpt (104.1 LGT) holds the six months from notification of the acuerdo de inicio; the 10-day dilación rests on art. 104.b RGAT, which the prompt names but neither text nor full holds (cite: art. 104 RGAT as well) |
| 926 | m03-l05-q0234 | no | excerpt (104.1 LGT) holds the six months from entry in the registro; the 14-day dilación rests on art. 104.a RGAT, which the prompt names but neither text nor full holds (cite: art. 104 RGAT as well) |
| 927 | m03-l05-q0235 | yes |  |
| 928 | m03-l05-q0237 | yes |  |
| 929 | m03-l05-q0239 | yes |  |
| 930 | m03-l05-q0241 | yes |  |
| 931 | m03-l05-q0242 | yes |  |
| 932 | m03-l05-q0243 | yes |  |
| 933 | m03-l05-q0244 | yes |  |
| 934 | m03-l05-q0245 | yes |  |
| 935 | m03-l05-q0246 | yes |  |
| 936 | m03-l05-q0247 | yes |  |
| 937 | m03-l05-q0248 | yes |  |
| 938 | m03-l05-q0249 | yes |  |
| 939 | m03-l05-q0251 | yes |  |
| 940 | m03-l05-q0252 | yes |  |
| 941 | m03-l05-q0253 | yes |  |
| 942 | m03-l05-q0254 | yes |  |
| 943 | m03-l05-q0255 | yes |  |
| 944 | m03-l05-q0256 | yes |  |
| 945 | m03-l05-q0257 | yes |  |
| 946 | m03-l05-q0258 | yes |  |
| 947 | m03-l05-q0259 | yes |  |
| 948 | m03-l05-q0260 | yes |  |
| 949 | m03-l05-q0261 | yes |  |
| 950 | m03-l05-q0263 | yes |  |
| 951 | m03-l05-q0266 | yes |  |
| 952 | m03-l05-q0267 | yes |  |
| 953 | m03-l05-q0268 | yes |  |
| 954 | m03-l05-q0271 | yes |  |
| 955 | m03-l05-q0272 | yes |  |
| 956 | m03-l05-q0275 | yes |  |
| 957 | m03-l05-q0280 | full-only | key pairs 99.2 (rehusar documentos no exigibles) and 99.3 (certificación); excerpt shows only 99.3, the 99.2 half is in full (prompt cites «artículo 99») |
| 958 | m03-l06-q0003 | yes |  |
| 959 | m03-l06-q0006 | yes |  |
| 960 | m03-l06-q0008 | no | key pairs 120.1 (autoliquidaciones son declaraciones) and art. 121 (comunicación de datos es declaración); excerpt shows 120.1 only, art. 121 is in neither text nor full (prompt names both; cite: art. 121 LGT as well) |

Counts: yes 50 · full-only 7 · no 3 · none-ok 0 · none-miss 0

## Misses and flags by cause

- **Lettered list: prompt names a letter but the excerpt falls back to letra a) (6 full-only)**: 906, 908, 910 (RGAT 103.b, d, f), 911 (103.e, letter not named), 916, 917 (RGAT 104.f, g). The citation is the bare article («art. 103 RGAT» / «art. 104 RGAT»); the extractor picks the named letter for 103.c, 103.e, 104.b, 104.c and 104.e (907, 909, 913–915) but not for these.
- **Key rests on several articles, but the citation and the excerpt cover only one (3 no)**: 925, 926 (104.1 LGT shown; the dilación rule of RGAT 104.a/b missing), 960 (120.1 LGT shown; art. 121 missing). Citation-shape problem, not an extractor cut.
- **Key pairs two apartados of the cited article, excerpt shows one (1 full-only)**: 957 (99.3 shown, 99.2 in full).
- 898/899-style date arithmetic (fecha a fecha, art. 30.4 LPAC) treated as computation, not a missing fact: 941, 947 counted yes.
- 915: RGAT 104 letra e) ends without a closing period; the source PDF has it that way too, so not an extractor flag.
- No garbled text or wrong-unit excerpts in this batch.
