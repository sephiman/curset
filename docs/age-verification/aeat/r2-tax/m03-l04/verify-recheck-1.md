# Verification re-check 1 — `m03-l04` (blind)

Verifier: opus, 2026-11-11. Sources: snapshot PDFs of the LGT (2024-12-21), RGAT (2026-10-07), RD 1619/2012 (2026-03-31); `normativa.yaml` entries of LGT, RGAT, RD 1619/2012 and LIVA. Worked example: every date and weekday recomputed with `python3` (`datetime`): 30-06-2022 jueves, 01-07-2022 viernes, 14-03-2025 viernes, 15-09-2026 martes; four years from 01-07-2022 end on 30-06-2026, before 15-09-2026; four years from 14-03-2025 end in March 2029. «Normativa» lines checked against every parenthetical citation of the lesson (parsed with the course citation loader) and every «artículo N» named in the prose.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `7b737351ef` | PASS | art. 19.2 RGAT | words of the article («por residir en el extranjero o por ser menores de 14 años, deberán obtener un número de identificación fiscal propio») | — |
| `b81a76c4d7` | PASS | art. 20.2 RGAT | nine characters, «una letra inicial, que será la M», seven alphanumeric, one alphabetic check character; «Si no lo tienen» stands for «no dispongan del número de identidad de extranjero» of the previous sentence's subject | — |
| `4a6b87dd24` | PASS | art. 4.2.a) RD 1619/2012 | words of the second paragraph of letter a) | — |
| `1d43c9bba4` | PASS | art. 4.2.a) RD 1619/2012 | «No se reputarán ventas al por menor…» rendered faithfully, all four criteria kept | — |
| `4408f124cb` | PASS | art. 35.6 LGT | words of the apartado | — |
| `6a26566434` | PASS | art. 68.7 LGT, last paragraph | words of the article («Lo dispuesto en este apartado no será aplicable… cuando no se hubiera acordado la suspensión en vía contencioso-administrativa») | — |
| `7181fd8ab7` | PASS | arts. 68.1.a) and 104.5 LGT (example premise) | 14-03-2025 is a viernes (checked); the notification falls inside the first four-year term (01-07-2022 to 30-06-2026); «termina sin caducidad» is the premise step 4 needs | — |
| `c04563a687` | PASS | arts. 68.1.a) and 104.5 LGT | art. 104.5: «las actuaciones realizadas en los procedimientos caducados no interrumpirán el plazo de prescripción»; the start notice of a comprobación limitada is an «acción de la Administración tributaria, realizada con conocimiento formal del obligado tributario, conducente a la… comprobación» (68.1.a)) | — |
| `79083e8ef8` | PASS | LGT «Normativa» line | every listed unit is cited or named in the prose (26 at l.130/137, 79 at l.225, 104.5 at l.345, 115 at l.295, 175 at l.218, 175.2 at l.209, 176 at l.233, 66 bis.3 at l.336, 35.4 named and cited); every LGT unit of the prose is listed; LGT has no cambios_pendientes, so no note; ends with «disposición adicional sexta.1–4.», not a bare «art. N.» | — |
| `53b1999968` | PASS | RD 1619/2012 «Normativa» line | 2.1 cited, 2.2 (l.86) and 2.3.b) b') (l.122) named, 3.1, 3.3, 4.1–4, 15.1–3 cited, 5 (l.121), 6 (l.117, 124), 7 (l.124) and 16.1 (l.93) named; no cambio-pendiente note is right: the RD 238/2026 changes (arts. 8.1, 8 bis, 9, 10) are not cited in the lesson | — |
| `dfed5c1192` | PASS | LIVA «Normativa» line | every listed article is named in the prose: 20 (l.88), 20.uno.23.º, 25.uno y dos, 26.tres (l.37), 25 (l.119), 68.Tres.a) (l.120), 80 (l.124), 121 (l.39, 65), 123.Uno.B).3.º (l.90), 129 apartado uno (l.93); no other LIVA article is named; the lesson names LIVA in the prose, so the line is required | — |
| `90f6b2cecc` | PASS | LIVA `cambios_pendientes` (RDL 29/2026, art. 7) | the lesson cites art. 20.uno.23.º, whose letter e´) the RDL 29/2026 changes with effects from 01-12-2026; norm name, «sin convalidar» and the date match `normativa.yaml`; art. 91, the other changed precept, is not cited, so it is rightly left out | — |

Not pending, observed while recomputing the example: step 6 (l.347) says «han pasado un año y seis meses» from 14-03-2025 to 15-09-2026; the exact span is one year, six months and one day (550 days). The conclusion does not change.

PASS 12 · FAIL 0
