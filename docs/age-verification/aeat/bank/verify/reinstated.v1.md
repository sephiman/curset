# Verification — reinstated questions on doubtful official keys (reinstated.v1)

Verifier: blind (opus), 2026-11-12, under `verify-spec.md` including the Amendment of 2026-11-12. Writer notes not read.
Sources: LGT `BOE-A-2003-23186_lgt_2024-12-21.pdf` (arts. 66 bis, 104), RGAT `BOE-A-2007-15984_rgat_2026-10-07.pdf`
(arts. 102, 104), LPAC `BOE-A-2015-10565_lpac_2024-11-06.pdf` (art. 30.4), all `pdftotext -layout`. None of these
precepts is on the RDL 29/2026 revert list. Official comparison: all 680 questions in `r0a/parsed/` (conv*_A + 2022_X),
searched for 66 bis, 104 LGT/RGAT, plazo de resolución, acuerdo de inicio, rango de ley, dilaciones; relevant items
2022-43, 2023-77, 2024-43, 2025-20, 2025-68, 2020-52, 2021-55. Every explanation ends with the Amendment sentence.

Cómputos recomputed (art. 30.4 LPAC, fecha a fecha; dilaciones in días naturales, art. 102.5 RGAT; weekdays checked
against the 2026 calendar, no vencimiento on a national holiday):

- q0193: 12-02-2026 (jue) + 6 meses = 12-08-2026 (mié). Key b.
- q0194: 12-11-2025 (mié) + 6 meses = 12-05-2026 (mar). Key b.
- q0233: 11-02-2026 + 6 meses = 11-08-2026 (mar); dilación art. 104.b RGAT 31-03 a 09-04-2026 = 10 días; 21-08-2026 (vie). Key a.
- q0234: 13-04-2026 + 6 meses = 13-10-2026 (mar); dilación 14 días → 27-10-2026 (mar). Key b.

| id | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|
| m03-l04-q0009 | PASS | PASS | PASS | PASS | PASS | PASS | Key c = art. 66 bis.2 párr. 1 (diez años desde el fin del plazo reglamentario de declaración del período en que se generó el derecho). a: four years is not the 66 bis.2 term; b: wrong dies a quo; d: six years not in the text. 2024-43 shares the fact but asks a combined señale (plazo + procedural scope) and its key reads «finalice el periodo impositivo»; here completion form, key by the text, official D's «4 años … plazo reglamentario» only echoed in a; not a copy. |
| m03-l04-q0114 | PASS | PASS | PASS | PASS | PASS | PASS | Key a = «salvo lo dispuesto en el apartado siguiente» (66 bis.1), apartado 2 being the ten-year rule. b, c, d point to arts. 66, 68, 70, not the salvedad. No official asks 66 bis.1. |
| m03-l04-q0115 | PASS | PASS | PASS | PASS | FAIL | FAIL | Same fact, angle and key as official 2024-43 (señale CORRECTA on art. 66 bis; key clause «solo podrá realizarse en el curso de procedimientos de comprobación relativos a obligaciones tributarias y periodos cuyo derecho a liquidar no se encuentre prescrito» = second half of official B/D), with the official distractor «pueden realizarse en el curso de cualquier procedimiento de comprobación» (2024-43 A/C) carried over as a. Also key 24 words vs 16 for every distractor. |
| m03-l05-q0191 | PASS | PASS | PASS | PASS | PASS | PASS | Key b = art. 104.1 «salvo que esté establecido por una norma con rango de ley o venga previsto en la normativa comunitaria europea». a, c, d: no other source of a longer plazo in the text. No official has this exception as key (2025-20 only mentions it in its stem). |
| m03-l05-q0192 | PASS | PASS | PASS | PASS | FAIL | FAIL | Same fact, angle and key as official 2025-20 (direct question on the general plazo máximo when the normativa fixes none; key six months), with its distractors «Tres meses» (2025-20 A/B) and «Doce meses» (2025-20 C) carried over; only the confusing clause of the official stem is removed. |
| m03-l05-q0193 | PASS | PASS | PASS | PASS | PASS | PASS | Cómputo above agrees (12-08-2026, miércoles). Distractors: +1 day, 3 months, 12 months, each wrong by art. 104.1 / art. 30.4 LPAC. Cómputo angle, no official equivalent. |
| m03-l05-q0194 | PASS | PASS | PASS | PASS | PASS | PASS | Cómputo above agrees (12-05-2026, martes); dies a quo art. 104.1.b. Shares the fact of 2025-68 (key B) but asks a cómputo with date options; no official distractor carried. |
| m03-l05-q0195 | PASS | PASS | PASS | PASS | FAIL | FAIL | Same fact and key as official 2023-77 B («El cómputo del plazo máximo de resolución en los procedimientos iniciados de oficio se iniciará en la fecha de notificación del acuerdo de inicio») and same angle as 2025-68 (momento de inicio del plazo de resolución) and 2025-20 (notificación del acuerdo de inicio), with the 2025-68 C distractor «desde la fecha de iniciación del expediente electrónico» carried over as d («Desde la fecha en que se abre el expediente en la sede electrónica»). |
| m03-l05-q0203 | PASS | PASS | PASS | PASS | PASS | PASS | Key a = the rango-de-ley exception of art. 104.1. b contradicts «salvo que…»; c, d add conditions absent from the text. Same point as q0191 and q0204 (bank-internal near-duplicates, not a spec check). |
| m03-l05-q0204 | PASS | PASS | PASS | PASS | PASS | PASS | Key b = art. 104.1 (a reglamento cannot exceed six months). a, c, d contradict the six-month cap. Key 22 words vs 10–14 (counts toward item 9 across the tema). |
| m03-l05-q0233 | PASS | PASS | PASS | PASS | PASS | PASS | Cómputo above agrees (21-08-2026, viernes): 6 meses (104.1.a LGT, 30.4 LPAC) + 10 días de dilación (104.b RGAT, días naturales 102.5 RGAT; exclusion 104.2 LGT, taught in the lesson with the same method). Distractors: no dilación, −1 day, +20 days. Every date in the stem carries its year; stem 100 words (≤ 110). |
| m03-l05-q0234 | PASS | PASS | PASS | PASS | PASS | PASS | Cómputo above agrees (27-10-2026, martes): 6 meses desde la entrada en registro (104.1.b) + 14 días de dilación (104.a RGAT). Distractors: no dilación, +28, −1. The explanation attributes the exclusion to art. 102.5 RGAT (it is 104.2 LGT / 102.2 RGAT; 102.5 gives the días naturales), a loose cite, not a wrong fact. Taxpayer unnamed but fictional and every fact stated. |
| m03-l05-q0267 | PASS | PASS | PASS | PASS | PASS | PASS | Key a = art. 104.1.a and b. b inverts, c replaces the acuerdo de inicio by the primera actuación, d unifies; all contradicted by 104.1. Same fact as 2023-77 B / 2025-68 B but new options (no official distractor carried); passes under check 5. |

## Summary

- Checked: 13. PASS: 10. FAIL: 3.
- FAIL by first failing check: check 5 — m03-l04-q0115, m03-l05-q0192, m03-l05-q0195.
- Check 3 (`check_draft.py` from `backend/`): m03-l04.authored-p1 130 questions, 0 anchor misses; m03-l05.authored-p2
  140 questions, 0 anchor misses. None of the 13 ids is flagged «OFFICIAL SIMILAR» (≥ 0.80); the three check-5 fails
  are by fact, angle, key and carried distractor, below that textual threshold.
