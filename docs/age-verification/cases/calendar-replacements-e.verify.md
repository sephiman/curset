# Calendar replacements, batch e — blind verification (R4, 2026-10-30)

Spec: `verify-spec.md` with the rulings of 2026-10-28. Articles read from `sources/normativa/` with `pdftotext -layout`:
LCSP arts. 211.1 and 212.1 (BOE-A-2017-12902, 2026-04-09); TREBEP arts. 10.1–10.4 and DA 17.ª.4 (BOE-A-2015-11719,
2026-10-03). Official questions compared: `bank/official/III.4.md`, `bank/official/IV.3.md`. Kept index rebuilt
(`kept_index.py`); `case_check.py sp-04 sp-17` prints no DUPLICATE (its six sp-04 festivo flags and the sp-17 q17
flag concern other questions).

## 1. Scenarios

**sp-04: OK** for q29. The stem's hypothetical (the contractor stops paying wages during the supply) contradicts no
scenario sentence; the scenario says only that the tablets were delivered late, by the company's fault.

**sp-17: OK** for q26. Don Rubén Egea Paredes is a new person brought in by the stem, at the Delegación; no scenario
sentence names him or contradicts him.

## 2. Table

| id | tema | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|---|
| sp-04/q29 | III.4 | PASS | PASS | PASS | PASS | PASS | PASS | Art. 211.1.i) lists as a causa de resolución «El impago, durante la ejecución del contrato, de los salarios por parte del contratista a los trabajadores que estuvieran participando en la misma», with no pliegos condition; the pliegos requirement belongs to the «restantes obligaciones esenciales» of 211.1.f), concurso is the separate 211.1.b), and nothing confines the remedy to penalidades. Art. 212.1 (who may instar this resolución) changes no option. Key on art. 211.1 alone. Lesson m03-l04 § Resolución cites art. 211.1 LCSP in prose. Uses case facts (Tecnoterminales Alcor, the suministro, the INE). Stem 45 words, options 11–15. No official III.4 question on unpaid wages; no other kept case on art. 211. |
| sp-17/q26 | IV.3 | PASS | PASS | PASS | PASS | PASS | PASS | Art. 10.4 «podrá permanecer en la plaza… siempre que se haya publicado la correspondiente convocatoria dentro del plazo de los tres años… y sea resuelta conforme a los plazos establecidos en el artículo 70… sin que su cese dé lugar a compensación económica»: 20 months < 36, so the key holds. Cesar at three years is the general rule the exception displaces; the DA 17.ª.4 twenty days per year needs «incumplimiento del plazo máximo», not the case here; art. 10.2 bars becoming funcionario de carrera. Key on art. 10.4 alone. Lesson m04-l03 § Cese de los interinos cites art. 10.4 TREBEP and states the exception. Case facts: the Delegación and a named interino in its plaza. Stem 50 words (case limit), norm named by the text's title («Según la [norma]» form, as sp-12/q10). Not a copy of conv2020 Supuesto II q20 (key «formalizará de oficio… sin compensación» not carried; our key is the corrected form of its distractor d, new stem with months given). |

Notes, no verdict:

- sp-04/q29: the lesson cites art. 211.1 but does not state 211.1.i) (it names only mutuo acuerdo, demora del
  contratista, demora en el pago and obligación principal). Check 3 requires the lesson to cite the article in prose,
  which it does; the spec does not require it to state the fact, so this is not a FAIL.
- sp-04/q29 option «si el INE declara antes a la empresa en concurso»: the Administration does not declare concurso;
  read as a crossed condition from 211.1.b), wrong by the text, not absurd.

## 3. Summary

2 checked, 2 PASS, 0 FAIL. No date or amount computations in either question (0 recomputed, 0 disagreements); word
counts checked by split.
