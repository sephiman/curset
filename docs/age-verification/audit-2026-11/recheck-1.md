# Audit 2026-11 — recheck 1 (blind verifier)

Date 2026-11-05. Source: `content/age-administrativo-c1/sources/normativa/BOE-A-2015-11724_lgss_2026-10-21.pdf`
(`pdftotext -layout`), under the R3.5 rule (the wording in force in 2027, including the 01-12-2026 changes).
Writer notes and earlier audit reports were not opened.

## Part 1 — bank question

| place/id | verdict | reason |
|---|---|---|
| m04-l09-q077 — 1 key | PASS | Art. 173.1, párrafo tercero, new wording (effect 01-12-2026): «En las situaciones especiales de incapacidad temporal previstas en el artículo 169.1.a), el subsidio se abonará, a cargo de la entidad gestora o colaboradora que cubra la incapacidad temporal por contingencias comunes, desde el día siguiente al de la baja en el trabajo, estando a cargo del empresario el salario íntegro correspondiente al día de la baja.» Key c is a faithful reduction. |
| m04-l09-q077 — 2 unique | PASS | Under the 2027 wording only c holds. «Desde el mismo día de la baja… sin salario alguno a cargo del empresario» is the redacción anterior for menstruación and donación only, so it is false under the cited wording (legitimate «norma anterior» distractor, tagged `cambio-pendiente`). «Desde el cuarto día… del cuarto al decimoquinto lo paga el empresario» is the enfermedad común rule (párrafo segundo). «Hasta el decimoquinto día lo paga íntegramente el empresario» contradicts «a cargo de la entidad gestora o colaboradora». No other norm in force bears on it, since the stem names art. 173.1. |
| m04-l09-q077 — 3 citation | PASS | Art. 173.1 holds the whole answer. The lesson cites the same precept for this rule (row «Situaciones especiales del art. 169.1.a)», «art. 173.1 LGSS, desde 01-12-2026»). |
| m04-l09-q077 — 4 style | PASS | «Según el artículo X…:» completion form. Norm named by the name of the text it approves (ruling). Stem has 31 words. Options run 22/20/28/18 words, which is allowed because they are statement options drawn from a norm sentence of about 50 words. All four options start with «Desde…». No article number, no ninguna/todas, not negative. Distractors use «norma anterior» plus altered text or a neighbouring plazo, so at most two patterns. The explanation names options by content, covers all three distractors and is correct. The optional «redacción vigente desde el 1 de diciembre de 2026» is in the explanation, and the tag is present. Peninsular Spanish, no typos. |
| m04-l09-q077 — 5 not official | PASS | `official/IV.9.md` has no question on art. 173.1. In `m04-l09.draft.json`, q025 (AT/EP), q026 (enfermedad común), q027 and q028 (dates) ask other situations of the same apartado, with different stems and option sets. The s5b draft has no 173.1 question. |
| **m04-l09-q077** | **PASS** | All five checks pass. Nothing appended to `drops.tsv`. |

## Part 2 — lesson `es/lessons/m04-l09.md`

| place/id | verdict | reason |
|---|---|---|
| (a) S1 «La prestación cubre la reducción de jornada de, al menos, un 50 por ciento…» (art. 190.1) | PASS | Matches 190.1: «reducción de la jornada de trabajo de, al menos, un 50 por ciento… personas progenitoras, guardadoras con fines de adopción o acogedoras de carácter permanente, cuando ambas trabajen, o cuando solo haya una persona progenitora por tratarse de familias monoparentales… cuidado directo, continuo y permanente… ingreso hospitalario o situación asimilada en los términos que reglamentariamente se desarrollen». |
| (a) S2 «Se mantiene hasta los 23 años cuando, alcanzada la mayoría de edad, persiste…» (art. 190.3) | PASS | 190.3, párrafo primero, word for word in substance. |
| (a) S3 «Cumplidos los 18 años, también puede reconocerse hasta que el causante cumpla 23…» (art. 190.3) | PASS | 190.3, párrafo segundo: «siempre que en el momento de la solicitud se acrediten los requisitos… salvo la edad». |
| (a) S4 «Se mantiene hasta que el causante cumpla 26 años si antes de los 23…» (art. 190.3) | PASS | 190.3, párrafo tercero: «grado de discapacidad igual o superior al 65 por ciento». |
| (a) S5 «Excepcionalmente, se prorroga más allá de los 26 años…» (art. 190.3) | PASS | 190.3, párrafo cuarto: «discapacidad igual o superior al 65 por ciento, o bien tengan reconocido el grado III de dependencia, siempre que persista la convivencia…». The new párrafo quinto (convivencia is deemed kept during a stay «de respiro o de corta duración») is not stated, but its absence makes nothing in the sentence false. |
| (a) S6 «El subsidio es el 100 por ciento de la base reguladora de la incapacidad temporal por contingencias profesionales, en proporción a la reducción de jornada.» (art. 192.1) | PASS | 192.1, párrafo primero. |
| (a) S7 «Si los dos… lo disfrutan a la vez… cada uno cobra el 50 por ciento de su base reguladora, sea cual sea su reducción de jornada» (art. 192.1) | PASS | 192.1, párrafo segundo: «50 por ciento de su respectiva base reguladora… con independencia del porcentaje de reducción». Voice: one idea per sentence, no fillers. Effect 23-10-2026, already in force, so no «desde» mark is needed. |
| (b) Esquema row «Cuidado de menores afectados por cáncer u otra enfermedad grave» (art. 192.1) | PASS | Reproduces both paragraphs of 192.1 (100 % of the contingencias profesionales base in proportion to the reduction; 50 % each when both use it at the same time, regardless of reduction). |
| (c) Table row «Situaciones especiales del art. 169.1.a)» | PASS | Matches new 173.1, párrafo tercero (quoted in Part 1). It carries «desde 01-12-2026». Old text, for the record: menstruación and donación «desde el mismo día de baja»; interrupción del embarazo and gestación «desde el día siguiente… salario íntegro… día de la baja». |
| (c) Paragraph under the table (example: baja on lunes 1 de marzo de 2027) | PASS | 173.1, párrafo segundo, the same in old and new wording: «a partir del cuarto día de baja… desde el día cuarto al decimoquinto de baja, ambos inclusive, el subsidio estará a cargo del empresario». Checked with `datetime`: 1-3-2027 is a Monday, the 4th a Thursday, the 15th a Monday. The stated assumption (the day of baja counts as day one, natural days) is declared. |
| (d) Normativa LGSS line, including «Cambio pendiente: Real Decreto-ley 31/2026, de 20 de octubre, en vigor el 01-12-2026 (art. 173.1).» | PASS | Follows the spec template. 173.1 is the only precept from which the lesson states new-wording content, and it is the only one marked «desde». The precepts listed (190.1, 190.3, 190.5, 192.1 and the rest) exist in the new file. |

## Notes (do not change a verdict)

- Arts. 169.1.a), 171 and 172 also print a 01-12-2026 wording in the new file, and the lesson cites all three (l. 55,
  67, 70; esquema rows at l. 172, 212–213). What the lesson states from them reads the same under both wordings: the
  365 + 180 days, the 180 cotización days, «reglas propias» for the situaciones especiales, and donación at 100 %. So no
  sentence fails and no «desde» mark is needed. If the coordinator reads R3.5 as «every cited precept with a future
  wording», the sentence becomes «Cambio pendiente: Real Decreto-ley 31/2026, de 20 de octubre, en vigor el 01-12-2026
  (arts. 169.1.a), 171, 172 y 173.1).»
- The new 169.1.a) adds two situaciones especiales: 4.ª (trastorno menopáusico secundario) and 5.ª (lesions from
  violencia de género). The new 171 sets the subsidy for 1.ª, 2.ª, 4.ª and 5.ª at the contingencias comunes amount.
  The lesson lists no situaciones especiales, so nothing in it is false. Both are examinable gaps.
