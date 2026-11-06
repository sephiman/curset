# Currency audit 2026-11 — Part T (theory): m04-l07, m04-l09, glossary, course.yaml

Verifier: blind (opus), 2026-11-05. Spec: `spec.md`, Part T. Files read with `pdftotext -layout`:
`BOE-A-2015-11724_lgss_2026-10-21.pdf`, `BOE-A-2000-12140_trlssfce_2026-10-21.pdf`,
`BOE-A-1987-12636_trlcpe_2026-10-21.pdf`, `BOE-A-2026-21872_rdl-31-2026_2026-10-21.pdf`; previous texts
`…_lgss_2026-10-03.pdf` and `…_trlcpe_2025-01-29.pdf` for the old wording of precepts already in force.

Ruling used for the «desde» mark: a sentence that cites a precept with a pending new wording (19.1 RDL 4/2000;
169.1.a), 171, 172, 173.1 LGSS) but states only facts whose words are the same in the old and new wording does not
rest on the new wording, so it needs no mark. No sentence checked states a fact found only in the 01-12-2026 wording,
so no Normativa block needs a «Cambio pendiente» sentence. The FAILs below are all in force since 23-10-2026 (LGSS
190 and 192), so their replacements take no mark.

| place | sentence (short) | precept | verdict | old text → new text | replacement |
|---|---|---|---|---|---|
| m04-l07 l.123–126 | «Está en incapacidad temporal, entre otros, el funcionario que padece un proceso patológico…» | art. 19.1 RDL 4/2000 | PASS | First paragraph unchanged. Second paragraph moves from «169.1.a), párrafos segundo y tercero» to «169.1.a), 1.ª, 2.ª, 4.ª y 5.ª» (from 01-12-2026); «entre otros» covers it | — |
| m04-l07 l.128 | «La licencia y sus prórrogas las conceden los órganos con competencia en gestión de personal» | art. 19.3 RDL 4/2000 | PASS | unchanged | — |
| m04-l07 l.138–141 + esquema l.164 | subsidy from the 4th month, six months cotizados, donante without prior cotización | art. 95.1–2 RD 375/2003 | PASS | not a changed norm. New 19.1 includes 1.ª, 2.ª, 4.ª and 5.ª but not 3.ª (donación), as before | — |
| m04-l07 l.146–148 + esquema l.166 | donación: 100 % of the complementarias from the 3rd month | art. 21.1.c) RDL 4/2000 | PASS | unchanged | — |
| m04-l07 l.207–208 | base reguladora = pensión de jubilación o retiro | arts. 39.1, 42.1, 45.1 TRLCPE | PASS | unchanged | — |
| m04-l07 l.212 (Viudedad row) | cónyuge supérstite; one year of marriage unless hijos comunes or >2 years with prior convivencia; prestación temporal 2 years; 50 % | arts. 38.1, 39.3 TRLCPE | PASS | 38.1 and 39.3 unchanged. 38.4 (pareja de hecho; hijos en común now need 2 years of convivencia) is behind «Entre otros» and not stated | — |
| m04-l07 l.213 (Orfandad row) | hijos <21 or incapacitados before that age or the death; 25 % / 10 % + 15 % prorrateado | arts. 41, 42.2–3 TRLCPE | PASS | 41.1 first paragraph and 42.2–3 unchanged. 41.1 third paragraph (moved from old 42.10), 41.5 and 42.9 (minimum 2× SMI) are not stated; «otros si había pensión extraordinaria» stays true | — |
| m04-l07 l.214 (padres row) | padres; 15 % each | arts. 44.1, 45.2 TRLCPE | PASS | unchanged | — |
| m04-l07 Lo que más cae l.220–221 | 4th month: básicas + subsidio; 80 % / 75 % | art. 21.1.b) RDL 4/2000 | PASS | unchanged | — |
| m04-l07 Normativa (RDL 4/2000) | «…19.1, 19.3…» | — | PASS | no sentence rests on the 01-12-2026 wording | — |
| m04-l07 Normativa (RDL 670/1987) | «…38.1, 39.1, 39.3, 41, 42.1–3…» | — | PASS | cited precepts hold the facts stated | — |
| m04-l09 l.55–63 | 169.1 a) 365 days + 180; b) observación 180 + 180 | art. 169.1 LGSS | PASS | «prorrogables por otros ciento ochenta días» → «por otros 180 días» (same fact); new special-situation list 1.ª–5.ª not stated here | — |
| m04-l09 l.65–67 | enfermedad común: 180 days in 5 years; accidente/EP: none; special situations «tienen reglas propias» | art. 172 LGSS | PASS | same facts; special situations now 1.ª, 3.ª, 4.ª, 5.ª without minimum and 2.ª per art. 178.1 «tomando como referencia la fecha de la baja médica»; «reglas propias» still true | — |
| m04-l09 l.67–70 | subsidy a tanto por ciento; donación 100 % of the common-contingency base | art. 171 LGSS | PASS | donación kept (now cited as 169.1.a).3.ª); new third paragraph (1.ª, 2.ª, 4.ª, 5.ª: same amount as common contingencies, paid per 173.1) not stated | — |
| m04-l09 l.74 (table) | AT/EP: from the day after the baja; employer pays that day's full salary | art. 173.1 LGSS | PASS | first paragraph unchanged | — |
| m04-l09 l.75 (table) | EC/ANL: from the 4th day; employer pays days 4–15 | art. 173.1 LGSS | PASS | second paragraph unchanged | — |
| m04-l09 l.77 | «Las situaciones especiales tienen reglas propias» | art. 173.1 LGSS | PASS | old: menstruation and donation from the same day, others from the day after → new: all 169.1.a) special situations from the day after, employer pays the day of the baja; «reglas propias» true in both | — |
| m04-l09 l.77–80 (worked example) | baja on 1-3-2027; paid from Thursday 4; employer until Monday 15 | art. 173.1 LGSS | PASS | enfermedad común; second paragraph unchanged | — |
| m04-l09 l.108–112 | «…afectado por cáncer o por otra enfermedad grave que requiera ingreso hospitalario de larga duración, durante la hospitalización y el tratamiento continuado (art. 190.1 LGSS)» | art. 190.1 LGSS | **FAIL** | old: «que requiera ingreso hospitalario de larga duración, durante el tiempo de hospitalización y tratamiento continuado de la enfermedad» → new: «que requiera ingreso hospitalario o situación asimilada en los términos que reglamentariamente se desarrollen». Without the change, the sentence is false for a short stay or a situación asimilada | La prestación cubre la reducción de jornada de, al menos, un 50 por ciento que llevan a cabo los progenitores, guardadores con fines de adopción o acogedores de carácter permanente, cuando ambos trabajen o en familias monoparentales, para el cuidado directo, continuo y permanente del menor de 18 años a su cargo afectado por cáncer u otra enfermedad grave que requiera ingreso hospitalario o situación asimilada, en los términos que se desarrollen reglamentariamente (art. 190.1 LGSS). |
| m04-l09 l.112–113 | «Se mantiene hasta los 23 años cuando… subsiste la necesidad de hospitalización, tratamiento y cuidado.» | art. 190.3 LGSS, párr. 1 | **FAIL** | old: «subsistiera la necesidad de hospitalización, tratamiento y cuidado durante el mismo» → new: «subsistiera la necesidad de hospitalización o tratamiento y de cuidado durante los mismos». Treatment without hospitalisation now suffices | Se mantiene hasta los 23 años cuando, alcanzada la mayoría de edad, persiste el padecimiento diagnosticado antes y subsiste la necesidad de hospitalización o tratamiento y de cuidado durante ellos. |
| m04-l09 l.113–115 | after 18, it can be granted until 23 if diagnosed before the age of majority | art. 190.3 LGSS, párr. 2 | PASS | same wording («el causante» → «la persona causante») | — |
| m04-l09 l.115–117 | «Se mantiene hasta que el causante cumpla 26 años si antes de los 23 acredita… 65 por ciento (art. 190.3 LGSS).» | art. 190.3 LGSS, párr. 3–4; art. 192.2 | **FAIL** | old 192.2: extinction «en todo caso, cuando cumpla los 26 años» → deleted. New 190.3 párr. 4: «Excepcionalmente se prevé la prórroga del derecho a la prestación más allá de los 26 años… discapacidad igual o superior al 65 por ciento, o bien… grado III de dependencia, siempre que persista la convivencia…». «Hasta los 26» is now false for those cases | Se mantiene hasta que el causante cumpla 26 años si antes de los 23 acredita, además, un grado de discapacidad igual o superior al 65 por ciento. Excepcionalmente, se prorroga más allá de los 26 si acredita una discapacidad igual o superior al 65 por ciento o tiene reconocido el grado III de dependencia, siempre que siga la convivencia con el beneficiario y se sigan acreditando las necesidades de cuidado directo, continuo y permanente (art. 190.3 LGSS). |
| m04-l09 l.117–118 | «El subsidio es el 100 por ciento de la base reguladora de la IT por contingencias profesionales, en proporción a la reducción de jornada (art. 192.1 LGSS).» | art. 192.1 LGSS | **FAIL** | old: single paragraph (and old 191.2: «solo podrá ser reconocido a favor de uno de ellos») → new second paragraph: «En el supuesto de disfrute simultáneo por ambas personas progenitoras… para el cuidado de la misma persona causante… un subsidio equivalente al 50 por ciento de su respectiva base reguladora… con independencia del porcentaje de reducción». False for simultaneous enjoyment | El subsidio es el 100 por ciento de la base reguladora de la incapacidad temporal por contingencias profesionales, en proporción a la reducción de jornada. Si los dos progenitores, guardadores o acogedores lo disfrutan a la vez para cuidar a la misma persona, cada uno cobra el 50 por ciento de su base reguladora, sea cual sea su reducción de jornada (art. 192.1 LGSS). |
| m04-l09 l.120–121 | school attendance is not by itself a cause of denial, suspension or extinction | art. 190.5 LGSS | PASS | unchanged (already in the 2026-10-03 text) | — |
| m04-l09 esquema l.168 | IT enfermedad común, except 169.1.a) special situations: 180 days in 5 years | art. 172 LGSS | PASS | same as l.65–67 | — |
| m04-l09 esquema l.169 | IT accidente / EP: no prior period | art. 172 LGSS | PASS | unchanged | — |
| m04-l09 esquema l.208 | IT: a tanto por ciento over the base reguladora | art. 171 LGSS | PASS | 171.1 first paragraph unchanged | — |
| m04-l09 esquema l.209 | IT donación: 100 % of the common-contingency base | art. 171 LGSS | PASS | kept in the new 171.1 | — |
| m04-l09 esquema l.212 | cuidado de menores: 100 % of the base, in proportion to the reduction | art. 192.1 LGSS | **FAIL** | same as l.117–118 | Un subsidio equivalente al 100 por ciento de la base reguladora establecida para la prestación de incapacidad temporal derivada de contingencias profesionales, y en proporción a la reducción que experimente la jornada de trabajo; en caso de disfrute simultáneo por ambos progenitores, guardadores o acogedores para la misma persona causante, el 50 por ciento de su respectiva base reguladora para cada uno, con independencia de su reducción de jornada \| art. 192.1 LGSS |
| m04-l09 Lo que más cae l.231 | EC/ANL: from the 4th day, employer until the 15th | art. 173.1 LGSS | PASS | second paragraph unchanged | — |
| m04-l09 Normativa (LGSS) | «…169.1, 171–174, …190.1, 190.3, 190.5, 192.1…» | — | PASS | no sentence rests on the 01-12-2026 wording; the replacements above cite precepts already listed | — |
| m04-l09 l.183–186 (uncited-subject search: «orfandad») | prestación de orfandad for the children of a woman killed by violence against women | art. 216.3 LGSS | PASS | 216.3 unchanged and quoted with «con las excepciones establecidas en los artículos siguientes». The new 224.1 (in force) is not stated | — |
| glossary `g-incapacidad-temporal` | 169.1 a) 365 + 180; b) observación 180 + 180 | art. 169.1 LGSS | PASS | same facts in both wordings. Note: the definition has never named the special situations (old or new); this was not caused by RDL 31/2026 | — |
| course.yaml m04-l07 summary | IT: full pay for 3 months, then básicas + subsidio 80 % / 75 % | art. 21.1 RDL 4/2000 | PASS | not a changed precept | — |
| course.yaml m04-l09 summary | IT lasts at most 365 days, extendable by 180 | art. 169.1.a) LGSS | PASS | same fact in both wordings | — |

Other glossary entries: none cites arts. 169–173 or 190–192 LGSS, art. 19 RDL 4/2000, or arts. 27, 38, 41, 42 TRLCPE
(`g-regimen-de-clases-pasivas` cites arts. 1.1 and 18.2 TRLCPE; `g-mutualismo-administrativo` and `g-mutualista`
cite arts. 2.1.b), 4.1 and 7.1 RDL 4/2000, all unchanged).

Uncited-subject search («incapacidad temporal», «situaciones especiales», «viudedad», «orfandad», «nacimiento»,
«cuidado de menores», «guarda legal», «cáncer», «pareja de hecho») in m04-l05, m04-l07, m04-l08 and m04-l09 found no
other sentence that states a fact from a changed precept. Not counted, outside the changed norms: m04-l05 l.209
(permiso for a child with cancer, art. 49.e) TREBEP, which RDL 31/2026 does not amend; its «ingreso hospitalario de
larga duración» is TREBEP wording, not LGSS 190.1) and m04-l08 l.178 (art. 70 Convenio único).

## Counts

- Places checked: 35 (m04-l07: 11; m04-l09: 21; glossary: 1; course.yaml: 2).
- PASS: 30.
- FAIL: 5, all LGSS cuidado de menores (190.1, 190.3, 192.1), in force since 23-10-2026, no «desde» mark:
  m04-l09 l.108–112, l.112–113, l.115–117, l.117–118, esquema l.212.
- Pending-wording («desde 01-12-2026») marks or «Cambio pendiente» sentences needed: 0.
