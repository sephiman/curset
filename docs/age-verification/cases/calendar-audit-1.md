# Calendar audit 1 — round R4, cases sp-01 … sp-08, sp-10

Date: 2026-10-29. Scope: every kept question with `"computes": "date"` (draft minus `drops.tsv` plus `restored.tsv`; `replaces` questions included), 82 questions, plus each scenario's festivos sentence. Every key and every count an explanation gives for a distractor was recomputed in Python (LPAC hábiles exclude Sat/Sun/festivos, months date to date, last day inhábil → next hábil, August hábil; LCSP naturales unless hábiles, DA 12.ª roll; LJCA August inhábil). Script: `/tmp/claude-1000/-home-juanjo-PycharmProjects-curset/cdf6381c-e69f-4bd9-ab76-b6a993e1c132/scratchpad/calendar-audit/calc.py`, `calc2.py`.

## Calendar used

| Place, year | Inhábiles beyond Sat/Sun | Source |
|---|---|---|
| Madrid (Comunidad), 2027 | 1 Jan, 6 Jan, 19 Mar (San José), 25 Mar, 26 Mar, 1 May (Sat), 16 Aug (Asunción moved), 12 Oct, 1 Nov, 6 Dec, 8 Dec, 25 Dec (Sat); 2 May is Sunday and not moved | Decreto 82/2026, de 30 de septiembre (BOCM 1 Oct 2026), annex text read in full (copy on laboral-social.com) |
| Madrid (city), 2027 | 15 May San Isidro (Sat), 9 Nov Almudena (Tue) | Pleno of 29 Sep 2026, unanimous (press: moncloa.com 30 Sep 2026, eldiario.es; madrid.es page «Calendario oficial laboral … 2027»); city act itself not read |
| Madrid, 2028 | Not published. Used national fixed days + 2 May; only Jan–Mar 2028 matter (1 Jan Sat, 6 Jan Thu) | Provisional |
| Sevilla (Andalucía), 2027 | National list + 1 Mar (Día de Andalucía moved), 16 Aug (Asunción moved) | Decreto 84/2026, de 29 de abril (BOJA 84, 5 May 2026), via press summary and BOJA listing |
| Sevilla (city), 2027 | 14 Apr (miércoles de Feria), 27 May (Corpus) | Municipal proposal (andaluciainforma.es); Pleno vote not confirmed. Outside every sp-06 window either way |
| Valladolid (Castilla y León), 2027 | National list + 23 Apr, 16 Aug (Asunción moved); no 19 Mar | Decreto 7/2026, de 26 de marzo (BOCYL 30 Mar 2026), list via Diario de León |
| Valladolid (city), 2027 | Not found; assumed 13 May, 8 Sep (traditional). Outside every sp-02 window either way | — |
| Recurso especial | Counted at the TACRC's seat (Madrid) | — |

The plan's «Madrid 2027 inhábiles» list matches the decree and the city's festivos exactly.

## Questions checked

| Case/id | Key holds | Explanation counts hold | Note |
|---|---|---|---|
| sp-01/q21 | yes | yes |  |
| sp-01/q23 | yes | no | Distractor c (22 Mar) said to count 10 hábiles; with San José 19 Mar inhábil that count ends 23 Mar |
| sp-01/q24 | yes | yes |  |
| sp-01/q25 | yes | yes |  |
| sp-01/q26 | yes | yes |  |
| sp-01/q30 | yes | yes | Distractor d (20 Mar 2028, 30 hábiles) assumes 20 Mar 2028 hábil; Madrid 2028 decree not yet published (19 Mar 2028 is a Sunday) |
| sp-01/q31 | yes | yes |  |
| sp-01/q33 | yes | yes |  |
| sp-01/q41 | yes | yes |  |
| sp-02/q03 | yes | yes |  |
| sp-02/q04 | yes | yes |  |
| sp-02/q05 | yes | yes |  |
| sp-02/q06 | yes | yes |  |
| sp-02/q07 | yes | yes |  |
| sp-02/q12 | yes | yes |  |
| sp-02/q13 | yes | yes |  |
| sp-02/q14 | yes | yes |  |
| sp-02/q21 | yes | yes |  |
| sp-02/q22 | yes | yes |  |
| sp-02/q23 | yes | no | Distractor c (16 Aug) said to count 30 hábiles; 16 Aug is festivo in Castilla y León, the count ends 17 Aug |
| sp-02/q24 | yes | yes | Return day after 5 hábiles 10–16 Jun; no Valladolid festivo in window |
| sp-03/q22 | yes | yes |  |
| sp-03/q23 | yes | yes |  |
| sp-03/q24 | yes | yes |  |
| sp-03/q25 | yes | yes |  |
| sp-03/q27 | yes | yes |  |
| sp-03/q32 | yes | yes |  |
| sp-03/q33 | yes | yes | Distractor d «empieza a contar un día después» read as first day Tue 28 Sep → 30 Sep |
| sp-04/q01 | yes | yes |  |
| sp-04/q04 | yes | yes |  |
| sp-04/q08 | yes | yes |  |
| sp-04/q12 | yes | yes |  |
| sp-04/q14 | yes | yes |  |
| sp-04/q15 | yes | yes |  |
| sp-04/q20 | yes | yes |  |
| sp-04/q21 | yes | yes |  |
| sp-04/q23 | yes | yes |  |
| sp-05/q02 | yes | yes |  |
| sp-05/q03 | yes | yes |  |
| sp-05/q05 | yes | yes | 15 May (San Isidro) is Saturday, outside window anyway |
| sp-05/q07 | yes | yes |  |
| sp-05/q11 | yes | yes |  |
| sp-05/q14 | yes | yes |  |
| sp-05/q22 | yes | yes |  |
| sp-06/q01 | yes | yes |  |
| sp-06/q05 | yes | yes |  |
| sp-06/q06 | yes | yes |  |
| sp-06/q14 | yes | yes |  |
| sp-06/q15 | yes | yes |  |
| sp-06/q23 | yes | yes | Same result counted at TACRC seat (Madrid) and Sevilla: 14 Oct–4 Nov holds only 1 Nov |
| sp-06/q24 | yes | yes |  |
| sp-07/q01 | yes | yes |  |
| sp-07/q02 | yes | yes |  |
| sp-07/q03 | yes | no | Distractor b (22 Mar) said to add 10 hábiles; San José 19 Mar inhábil, the count ends 23 Mar |
| sp-07/q04 | yes | yes |  |
| sp-07/q08 | yes | yes |  |
| sp-07/q11 | yes | yes |  |
| sp-07/q14 | yes | yes |  |
| sp-07/q15 | yes | yes |  |
| sp-07/q18 | yes | yes |  |
| sp-07/q19 | yes | yes |  |
| sp-07/q23 | yes | yes |  |
| sp-08/q02 | yes | yes |  |
| sp-08/q03 | yes | yes |  |
| sp-08/q04 | yes | yes |  |
| sp-08/q05 | yes | yes |  |
| sp-08/q08 | yes | yes |  |
| sp-08/q09 | yes | yes |  |
| sp-08/q12 | yes | yes |  |
| sp-08/q20 | yes | yes |  |
| sp-08/q21 | yes | yes |  |
| sp-08/q23 | yes | yes |  |
| sp-10/q02 | yes | yes | August excluded (art. 128.2 LJCA): 1 Jul–30 Sep |
| sp-10/q05 | yes | yes |  |
| sp-10/q06 | yes | yes |  |
| sp-10/q08 | yes | yes |  |
| sp-10/q09 | yes | yes |  |
| sp-10/q12 | yes | no | Distractor d (16 Aug) said to apply the month; 16 Aug festivo in Madrid, the month passes to 17 Aug |
| sp-10/q13 | yes | yes |  |
| sp-10/q14 | yes | yes |  |
| sp-10/q16 | yes | yes |  |
| sp-10/q19 | yes | yes |  |

Every key holds. Four explanations state a wrong distractor count; each is appended to `drops.tsv` as a FAIL (batch `calendar-audit-1`, check 1). Each fix needs only a new distractor date or a reworded label (23 Mar / 17 Aug), since no option coincides with the key.

## Scenario festivos sentences

| Case | True | Note |
|---|---|---|
| sp-01 | true | Listed windows hold no festivo. The q23 distractor window (to 22/23 Mar, San José) is not covered, but the sentence does not claim it |
| sp-02 | true | Castilla y León's 16 Aug falls after every listed window. A fixed q23 should name it if the 30-hábiles distractor stays |
| sp-03 | true | 12 Oct, 1 & 9 Nov, 6 & 8 Dec, the 2028 and 2031 Saturday rolls all correct |
| sp-04 | true | — |
| sp-05 | true | — |
| sp-06 | true | Same with Andalucía's 2027 calendar and with the TACRC (Madrid) count for q23 |
| sp-07 | true | The q03 distractor window reaches 19 Mar but the sentence lists q03 only to 15 Mar. A fixed q03 should name San José if a 22/23 Mar distractor stays |
| sp-08 | true | — |
| sp-10 | true | It calls q12 a plazo por meses; it is 15 días naturales (label slip, no fault in a date). A fixed q12 should name 16 Aug if the one-month distractor stays |

No scenario sentence is false, so there is no scenario-only fix. The four FAIL questions need their festivos coverage extended when they are rewritten.
