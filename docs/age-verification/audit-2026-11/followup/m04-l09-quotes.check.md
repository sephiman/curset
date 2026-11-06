# m04-l09: quotations after RDL 31/2026, blind check (followup-2026-11)

Source: `content/age-administrativo-c1/sources/normativa/BOE-A-2015-11724_lgss_2026-10-21.pdf` (`pdftotext -layout`).
Wording rule R3.5: arts. 169.1.a) and 172 are cited in the wording printed first, in force from 01-12-2026, and not in the
«Redacción anterior». Art. 190 is integrated, in force since 23-10-2026. Diff against `HEAD` from
`docs/age-verification/bank/bloque-iv/m04-l09.draft.json`: only `explanation` and/or `source_quote` changed in q018,
q019, q022, q039, q040 and q042. In all six, `prompt`, `options` and `correct` are byte-identical to `HEAD`. No other
pre-existing id changed. Check 5 was unaffected because stems and options did not move.

| id | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|
| m04-l09-q018 | PASS | PASS | PASS | PASS | PASS | PASS | The quotation «una duración máxima de trescientos sesenta y cinco días, prorrogables por otros 180 días» is exact in the new wording (the old one has «ciento ochenta»). The source_quote is exact. The explanation refutes 365+365, «sin prórroga» and 180+180, which is the observation period of letra b). |
| m04-l09-q019 | PASS | PASS | PASS | PASS | PASS | PASS | The source_quote now has «otros 180 días cuando se presuma…», which is exact in the new wording. The quotation in the explanation is the same in both wordings. The «estudio y diagnóstico» distractor is correctly attributed to letra b). |
| m04-l09-q022 | PASS | PASS | PASS | PASS | PASS | PASS | «180 días dentro de los cinco años inmediatamente anteriores al hecho causante» is exact in art. 172.a) in force from 01-12-2026. The explanation correctly ties the seven years and the 360 days to art. 178.1.c). Option a) cannot be defended, because the 178.1 periods in art. 172.a) apply only to situación especial 2.ª, while the stem asks about «enfermedad común, con carácter general». |
| m04-l09-q039 | PASS | PASS | PASS | PASS | PASS | PASS | The new source_quote is an exact substring of art. 190.1. The old one, «se considera situación protegida la reducción…», skipped «a efectos de la prestación…» and was not exact, so the change fixes it. |
| m04-l09-q040 | PASS | PASS | PASS | PASS | PASS | PASS | «cuando ambas trabajen, o cuando solo haya una persona progenitora por tratarse de familias monoparentales» and the source_quote are exact in art. 190.1 in force. Style note: the stem and the key keep «progenitores… ambos… un progenitor… familia monoparental». This is a faithful reduction with the same condition, the key stays the only right option, and it does not mislead. |
| m04-l09-q042 | PASS | PASS | PASS | PASS | PASS | PASS | «hasta que la persona causante cumpla 26 años si antes de alcanzar los 23 años acreditara, además, un grado de discapacidad igual o superior al 65 por ciento» is exact in the third paragraph of art. 190.3, and so is the source_quote. |

## Unchanged items examined

- **m04-l09-q041** (PASS, not re-keyed). The quotation «se mantendrá la prestación económica hasta los 23 años» is exact
  except for the initial capital: the norm has «Se». The quotation is built into the sentence after «dice que», and
  Spanish typographic usage lets an integrated quotation begin in lower case, so this is acceptable. Style note on the
  stem: it says «hospitalización, tratamiento y cuidado», while the norm says «hospitalización o tratamiento y de
  cuidado durante los mismos». The stem describes a narrower case that the norm still covers, so the key («veintitrés
  años») stays the only right option. Option d) («veintiséis… en todo caso») stays wrong, even with the new
  «Excepcionalmente… más allá de los 26 años» paragraph. This does not mislead, and the stem could be aligned
  («hospitalización o tratamiento y cuidado») at the next touch.
- **m04-l09-q023** (PASS). The quotation «en caso de accidente, sea o no de trabajo, … no se exigirá ningún período
  previo de cotización» is exact apart from the lower-case «en», where the norm has «En». It is built into the sentence
  after «dice que», so it is acceptable. Letra b) of art. 172 reads the same in both wordings.

## Counts

Checked: 6 changed, plus 2 unchanged examined. PASS: 6 of 6, plus 2 of 2. FAIL: 0 (key 0, unique 0, citation 0, style 0,
official 0). No line was appended to `drops.tsv`.

Notes, which change no verdict:
- None of the six questions carries the `cambio-pendiente` tag. The fact each one tests (180 days, 180 days in five years)
  is the same in the old and new wording; only the figures moved from words to digits. No question is true today and
  false in 2027.
- Lesson: no sentence at odds with the norm was seen in the art. 169/172/190 lines checked (55–157).
