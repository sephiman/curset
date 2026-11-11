# Verification re-check 1 — `m03-l08` (blind)

Verifier: opus, 2026-11-11. Sources: snapshot PDFs of the LGT (2024-12-21: arts. 142.1, 150.1–4), RGAT (2026-10-07: art. 190.6); `normativa.yaml` entries of LGT, RGAT, Ley 39/2015 (LPAC), LIS, Concierto (Ley 12/2002) and Convenio con Navarra (Ley 28/1990). «Normativa» checked against every parenthetical citation of the lesson and every «artículo N» named in the prose (both extracted by script, l.1–352): every listed LGT and RGAT unit is cited or named (e.g. LGT 27 l.223, 93–94 l.11, 104.2 l.202, 134–135 l.12, 136–140 l.16, 188.1 l.252, 251 l.206; RGAT 97.1 l.82, 172.2 l.51, 190.2 and 190.4 l.296), and every norm the prose cites or names has a line (LIS named at l.198; Concierto and Convenio named at l.211; «Impuesto Complementario» at l.196 and l.345 is a tax named in art. 150.1.b) 3.º LGT, not a norm).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `4e74e60df3` | PASS | art. 142.1 LGT | second half of the article's sentence, complete; the verbless «También mediante…» is gone | — |
| `a9ec0268d3` | PASS | art. 150.1 LGT, last paragraphs of letter b) | «vinculadas de acuerdo con lo establecido en el artículo 18 de la Ley 27/2014…» kept; any one of them meeting a circumstance of letter b) extends the 27-month term to all | — |
| `87b244c952` | PASS | art. 190.6 RGAT | «salvo que concurra alguna de las circunstancias a que se refieren los apartados 2 y 3 de este artículo y, exclusivamente, en relación con los elementos… afectados» | — |
| `0d21281d53` | PASS | art. 150.1 and 150.2 LGT | 18 and 27 months; the three circumstances, with «que esté siendo objeto de comprobación inspectora» kept; the comunicación de inicio informs of the term (150.2, second paragraph). A «Lo que más cae» compression of 150.1.b) 2.º («grupo de consolidación fiscal o de entidades»); the full wording is at l.196 | — |
| `aae844f7a4` | PASS | art. 150.4 LGT | «uno o varios periodos en los que la inspección no podrá efectuar actuaciones…», «no podrán exceder en su conjunto de 60 días naturales para todo el procedimiento y supondrán una extensión del plazo máximo» | — |
| `a09c2cd5c1` | PASS | Ley 39/2015 (LPAC) «Normativa» line | starts with the `short`; art. 30.4 is the only LPAC unit in the prose (l.3 names the norm, the example cites 30.4); ends with article and paragraph | — |
| `3898a7c9a1` | PASS | LIS «Normativa» line | `short` «LIS (Ley 27/2014)»; art. 18 named inside art. 150.1 LGT (l.198), listed with «nombrado en…» | — |

PASS 7 · FAIL 0
