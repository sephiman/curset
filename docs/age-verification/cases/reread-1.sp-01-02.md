# Re-read 1 — sp-01 (q21–q40) and sp-02 (first version), dropped questions (R4, 2026-10-28)

Re-judged under «Rulings of 2026-10-28 (user)» in `verify-spec.md`: dependence fails only with no case fact at all
or a contradiction of the scenario; copies compare stem and options with the official question. Checks 1–3 and the
rest of 4 are taken from `sp-01.verify-2.md` and `sp-02.verify-1.md` where they show PASS. Check 5, left blank for
the sp-01 dependence drops, was evaluated here against `docs/age-verification/bank/official/<tema>.md`. Stem and key
weekdays re-checked with Python `datetime`; none contradicts the current scenario. The two sp-01 `SCENARIO` notes
(Don Mateo's relation not stated; comma splice) change no key, as the verify report says.

## sp-01 (`sp-01.verify-2.md`)

| id | original check | new verdict | reason |
|---|---|---|---|
| q22 | 4 dependence | still dropped (5) | Dependence passes, but it copies conv2022 · Supuesto II · 16: same question (can audiencia be skipped when only the interesado's facts figure), official key plus the official «en ningún caso podría prescindirse» and «sustituirse por el trámite de información pública» distractors. |
| q27 | 4 dependence | restored | Uses the case's PBL and IVA rate; no official asks the art. 100.1 amount (III.4, V.3 checked); 1–3 PASS. |
| q29 | 4 dependence | restored | Uses the formalización and delivery dates; conv2025_A · P1 · 20 asks art. 102 provisional prices, other stem and options; 1–3 PASS. |
| q32 | 4 dependence | restored | Uses the birth date and the stem's 28 Feb 2028 (Mon); conv2020 · SI · 17 shares only the «18 meses» idea in another stem; 1–3 PASS. |
| q33 | 4 dependence | restored | Uses the birth date; conv2022_X · SII · 7 states the three-year rule as text options, q33 asks a month from the case's dates; 1–3 PASS. |
| q34 | 4 dependence | restored | Uses Doña Irene's mother's situation; no official asks the cuidado-de-familiar duration (IV.4, IV.5 checked); 1–3 PASS. |
| q36 | 2 unique | still dropped (2) | Unique failed: art. 98.3 TREBEP makes the 1.160-euro option hold too. |
| q37 | 4 dependence | restored | Uses the capítulo's 6.200.000; conv2025_A · SI · 11 asks who authorises, not the amount; 1–3 PASS. |
| q38 | 4 dependence | restored | Uses the capítulo and the 300.000 already authorised; no official asks the remaining amount; 1–3 PASS. |
| q39 | 4 dependence | restored | Uses the State's firm, unpaid commitment; conv2025_A · SII · 11 asks which modification, another stem and options; 1–3 PASS. |
| q40 | 4 dependence | restored | Uses the Intervención Delegada's reparo; no official asks art. 155 (V.2, V.3, V.5 checked); 1–3 PASS. |

## sp-02 (`sp-02.verify-1.md`)

| id | original check | new verdict | reason |
|---|---|---|---|
| q01 | 4 explanation | still dropped (4) | Explanation describes a «lunes 15 de febrero» that is not among the options. |
| q02 | 3 citation, 5 | still dropped (3) | Art. 30.5 does not hold the three months of art. 21.3. |
| q04 | 4 dependence | restored | Uses the empresa's alzada, dated in the stem (Mon 31 May 2027 → Tue 31 Aug); 5 PASS in report; 1–3 PASS. |
| q05 | 5 copy | restored | conv2020 · SI · 4 and conv2020_X · SI reserva 3 compute the same kind of prescription, but stem and options differ and the dates are the case's own (Fri 4 Feb 2028); 1–4 PASS. |
| q06 | 5 copy | restored | conv2025_X · SII reserva 2 (date + sense options) and conv2024_X · SI · 11 differ in stem and options; the case's own dates (Tue 10 Aug 2027); 1–4 PASS. |
| q09 | 3 citation, 4 | still dropped (3) | Citation names only DA 12; the 30 days are art. 198.4. |
| q10 | 4 dependence, 5 | restored | Uses the case's cleaning contract; conv2025_A · SII · 8 asks exercise plus document («2025 - Documento OK»), another stem and option set; 1–3 PASS. |
| q11 | 2 unique | still dropped (2) | The scenario does not say where the death occurred, so the three-day option holds too. |
| q14 | 5 copy | restored | conv2022_X · SI · 14 has text options on the one-month rule; q14 asks a date from Don Hugo's cese (Fri 9 Jul 2027); art. 87.1.a TREBEP covers altos cargos autonómicos; 1–4 PASS. |
| q15 | 4 dependence, 5 | restored | Uses Don Ángel's falta date and the stem's incoación (Wed 20 Oct 2027); conv2020 · SI · 19 is a muy grave falta with another stem, key and option set; 1–3 PASS. |
| q16 | 3 citation | still dropped (3) | The 58,00 actually spent rests on art. 10.3 RD 462/2002, not the cited art. 12.3. |
| q17 | 4 dependence | restored | Uses Don Raúl's authorised own car; 5 PASS in report; 1–3 PASS. |
| q19 | 5 copy | restored | conv2020 · SII · 13 asks only the modification; q19 also asks the organ, has two «generación» options and is decided by «titular del ministerio previo informe favorable de la Intervención Delegada»; not the same stem or option set (closest call); 1–4 PASS. |

## Summary

- sp-01: re-read 11; restored 9 (q27, q29, q32, q33, q34, q37, q38, q39, q40); still dropped 2 (q22 check 5, q36 check 2).
- sp-02: re-read 13; restored 8 (q04, q05, q06, q10, q14, q15, q17, q19); still dropped 5 (q01 check 4, q02/q09/q16 check 3, q11 check 2).
