# Calendar replacements, batch d — blind verification (R4, 2026-10-30)

Spec: `verify-spec.md` with the rulings of 2026-10-28, plus the user rule of 2026-10-30 (no question may need an
unpublished calendar; State 2027 and 2027 regional calendars are published, nothing in 2028+). Articles read from
`sources/normativa/` with `pdftotext -layout`: LCSP arts. 243.1–4 and 244.1 (BOE-A-2017-12902, 2026-04-09); TREBEP
art. 10.1 (BOE-A-2015-11719, 2026-10-03). Madrid 2027 = State BOE-A-2026-21254 + BOCM 1-10-2026 (Decreto 82/2026).

## 1. Scenarios

**sp-09 (edited): OK.** All 16 dated phrases carry the true weekday (Python `datetime`; 19 and 25 Mar 2027 checked by
hand: Fri, Thu). The festivos sentence now lists 19, 25, 26 Mar and 16 Aug 2027 only; every hábil window and month
rollover of a kept question was recomputed against the Madrid 2027 calendar and touches no other festivo (q02 19 May–8
Jun, q10 8–28 Jun, q21 9 Mar–8 Apr; month ends 8 Mar, 18 May, 6 Sep, 2 Dec 2027 all hábiles; Madrid city's 15 May and
9 Nov 2027 lie in no window). The 2028 dates left in the scenario (delivery Thu 14 Dec 2028, reception Mon 18 Dec 2028)
are facts only: no kept question counts days from or to them. No contradiction, fictional people and companies, OAPN
and Subdelegación del Gobierno en Segovia under current names.

Kept sp-09 (20: q01, q02, q06–q10, q13–q17, q20–q27; `case_check.py sp-09 sp-17` prints no DUPLICATE): every key
recomputed and unchanged (q01 Tue 18 May; q02 Tue 8 Jun; q06 Mon 8 Mar; q10 Mon 28 Jun; q21 Thu 8 Apr; q23 Sun 5 Sep →
Mon 6 Sep; q25 Thu 2 Dec 2027; q08 375.100; q09 2.400.000; q15 11; q20 18,02; q24 56,10), and every date distractor
reproduces its stated count. None needs a 2028-or-later working day (2028/2029 appear only as budget years in q08, q09,
q13).

Notes, no verdict: the `festivos` field still describes the dropped q11 (6 and 8 Dec 2028) and q04 (13 Mar 2028); the
`depends_on` of q14 and q21 still quotes the old festivos sentence with «el miércoles, 6, y el viernes, 8 de diciembre
de 2028». Metadata only; the scenario text is correct.

**sp-17: OK** for q25. The stem's added fact (five months as interina in the last eighteen) contradicts no scenario
sentence: the scenario says only that Doña Nuria «es nombrada funcionaria interina por exceso de tareas»; the dropped
q10's «sin nombramientos anteriores» is no longer in a kept question.

## 2. Table

| id | tema | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|---|
| sp-09/q27 | III.4 | PASS | PASS | PASS | PASS | PASS | PASS | Art. 243.3 «El plazo de garantía se establecerá en el pliego… atendiendo a la naturaleza y complejidad de la obra y no podrá ser inferior a un año salvo casos especiales». Distractors wrong by the text: two years and the director facultativo (not in 243.3; the director only reports before expiry), fifteen years = art. 244.1 vicios ocultos, three months = art. 243.1 certificación final. A visitors' centre is not an art. 243.4 exception. Lesson m03-l04 cites art. 243.3 in prose. Uses case facts (the obras, reception sin reservas); no calendar. Stem 38 words. No official III.4 question on the plazo de garantía (the official III.4 option «seis meses… certificación final» is another sentence); no other kept case on art. 243. |
| sp-17/q25 | IV.3 | FAIL | FAIL | PASS | PASS | PASS | FAIL | Art. 10.1.d) «por plazo máximo de nueve meses, dentro de un periodo de dieciocho meses» bounds the interinidad for the exceso o acumulación de tareas; the stem gives neither the cause of the earlier five months (a prior sustitución or vacante does not count, leaving nine) nor where they fall in the eighteen-month period, so «cuatro meses» rests on facts not stated and «nueve meses» becomes defensible. |

## 3. Summary

2 checked, 1 PASS, 1 FAIL (key: sp-17/q25). Computations recomputed with Python: 7 date questions (28 dates, keys and
distractors) and 5 amount questions in sp-09, plus the q25 subtractions (4, 13, 31); 0 arithmetic disagreements. No
kept sp-09 question depends on a 2028-or-later working day.
