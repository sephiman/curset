# Calendar replacements, batch b — blind verification (R4, 2026-10-30)

Spec: `verify-spec.md` with the rulings of 2026-10-28, plus the user rule of 2026-10-30 (no question may need an
unpublished calendar; see `calendar-publication-2027.md`). Scenarios unchanged; only the replacement questions were
checked. Articles read from `sources/normativa/` with `pdftotext -layout`: LPAC arts. 30.4–5, 107, 122.1; LCSP art. 53;
LGP art. 79; TREBEP art. 97; RD 640/1987 art. 10.1. Madrid 2027 = State BOE-A-2026-21254 + BOCM 1-10-2026, plus the
local days only as each scenario states them.

1. Scenario: not re-checked (unchanged). The replacements contradict no scenario sentence.
2. Table:

| id | tema | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|---|
| sp-08/q24 | V.5 | PASS | PASS | PASS | PASS | PASS | PASS | Art. 10.1 «dentro del mes siguiente a la inversión… y en todo caso en el plazo de tres meses desde la percepción». Payment Wed 6 Oct 2027 + 1 month = Sat 6 Nov → Mon 8 Nov (art. 30.5); percepción Mon 6 Sep + 3 months = Mon 6 Dec (national festivo) → Tue 7 Dec, later. Fri 5 Nov, Sat 6 Nov, Tue 7 Dec verified. All dates 2027, published calendar. Officials conv2025_A P1 38 and conv2024 P1 40 ask the rule in words; sp-04/q20 keys the three-month limit (other angle). |
| sp-09/q25 | III.3 | PASS | PASS | PASS | PASS | PASS | PASS | Art. 107.3 «Transcurrido el plazo de seis meses desde la iniciación… se producirá la caducidad». Wed 2 Jun 2027 → Thu 2 Dec 2027, hábil. Wed 1 Dec (first day counted), Mon 29 Nov (180 days), Thu 2 Sep (three months) verified. The 107.2 four-year limit is named without a date, so no 2028 day is needed. conv2024_X P1 18 asks the rule in words (tres meses distractor); this stem and option set are new. Stem 50 words. |
| sp-09/q26 | III.4 | PASS | PASS | PASS | PASS | PASS | PASS | Art. 53 «quedará en suspenso la tramitación del procedimiento cuando el acto recurrido sea el de adjudicación, salvo… acuerdo marco… sistema dinámico»; the obras contract is neither. Formalising, garantía and Tribunal-decided suspension are each wrong by the text. Admissibility (art. 44.1.a, VE 3.360.000 > 3.000.000) is a premise of the stem, not part of the key. conv2022 S-I 14 is about recurso against pliegos and keys medidas cautelares; its suspension sentence appears here as key under another stem and option set, not a rewording. |
| sp-10/q28 | III.3 | PASS | PASS | PASS | PASS | PASS | PASS | Art. 122.1 «un mes, si el acto fuera expreso»; art. 30.4 «Si en el mes de vencimiento no hubiera día equivalente… expira el último día del mes» (default cómputo). Wed 31 Mar 2027 → Fri 30 Apr 2027, hábil. Sat 1 May, Thu 29 Apr, Mon 31 May (two months) verified. conv2024_X S-II 15 also asks an alzada end date, but with another stem, other dates and the rollover rule as key; under the 2026-10-28 ruling this is not a copy. |
| sp-11/q25 | V.5 | PASS | PASS | PASS | PASS | PASS | PASS | Art. 79.3 «el Consejo de Ministros podrá acordar que, con los fondos librados a justificar para gastos en el extranjero… sean atendidos gastos realizados en el ejercicio siguiente, si ello fuese considerado relevante para el interés general». Lisboa (scenario) decides. Other options (never; Dirección del Injuve; Intervención Delegada) wrong by the text. No official V.5 question on this sentence. |
| sp-11/q26 | IV.6 | PASS | PASS | PASS | PASS | PASS | PASS | Art. 97.1 «las leves a los seis meses»; 97.2 «desde que se hubieran cometido». Tue 22 Jun 2027 → Wed 22 Dec 2027. Thu 23 Dec, Sun 19 Dec (180 days), Wed 22 Sep (three months) verified; all 2027, no hábil check needed. Officials ask the plazo by name or the start rule (conv2022 S-I 19, conv2022_X S-II 3), not a date. |
| sp-14/q28 | V.5 | PASS | PASS | PASS | PASS | PASS | PASS | Art. 79.2 «La citada designación implicará la atribución de competencias para la realización de los gastos y pagos… y la formación, rendición y justificación de las correspondientes cuentas»; the scenario's campaign in a town with no dependencia puts it under 79.2. Distractors wrong by the text. No official twin. |

3. Summary: 7 checked, 7 PASS, 0 FAIL. Computations recomputed with Python: 4 date questions, 16 dates (keys and
   distractors), 0 disagreements; no key or count depends on a 2028-or-later working day. Lesson anchors resolve (m05-l05,
   m03-l03, m03-l04, m04-l06 cite each article in prose). `case_check.py sp-08 sp-09 sp-10 sp-11 sp-14`: no DUPLICATE;
   its holiday flags on these questions (6 Dec, 1 May) are named or outside any counted day.
