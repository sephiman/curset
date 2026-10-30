# Verification — calendar replacements, batch c (R4, 2026-10-30)

Blind verifier. Spec: `verify-spec.md` with the rulings of 2026-10-28, plus the user rule of 2026-10-30 (only the State
2027 calendar, BOE-A-2026-21254, and the 2027 regional calendars are published; Madrid city's local days count only as
the scenario states them; nothing in 2028 or later may need a working-day check). Articles read with `pdftotext
-layout` from the files named in `sources/normativa.yaml` (LPAC 2024-11-06, LCSP 2026-04-09, RD 640/1987 2026-10-08;
art. 7 is untouched by the pending RD 813/2026 change, which is to art. 6). Dates recomputed with Python `datetime`
against the published 2027 calendars (State; Madrid, Decreto 82/2026; Andalucía and Sevilla local) and the scenarios'
stated days. Writer notes not read.

## 1. Scenario findings

- **Weekdays.** Every dated phrase in the scenarios of sp-03, sp-04 and sp-06 and in all their questions has the true
  weekday.
- **Duplicates.** `case_check.py sp-03 sp-04 sp-06` prints no DUPLICATE.
- **sp-04, festivos sentence without «solo».** The list is now open, so the real 2027 Madrid festivos also count
  (1 and 6 Jan, 19, 25 and 26 Mar, 1 May, 16 Aug). None falls in a kept day window: q01 8 Jun–19 Jul, q04 16 Jul–5
  Aug, q14 22 Sep–13 Oct (only 12 Oct, named). The month count of q15 ends Sat 13 Nov → Mon 15 Nov 2027, hábil. q12
  counts natural days. q28 counts the hábiles of November 2027: 22 weekdays minus 1 Nov (national, published) and
  9 Nov (stated) = 20. The clash with the «inhábiles … 9 de noviembre» sentence, reported in batch a, is gone. No kept
  answer changes.
- **sp-04, «por causa suya».** It supplies the imputability that art. 193.3 LCSP requires («por causas imputables al
  mismo»). q07 keeps its key: Fri 22 Oct → Thu 4 Nov 2027 = 13 days; 85 × 0,60 = 51 €/day; 663 €. Distractors
  recomputed: 612 (12 days), 802,23 (663 × 1,21), 6.630 (0,60 per 100 €). The gap batch a noted for q07 is closed.
- **sp-04, «resbala en la sede del INE».** Consistent; q22 (art. 36.2 LRJSP, leve negligence) unchanged.
- **sp-06, clause «y los plazos por meses terminan en día hábil» removed.** No kept question needs it. Month counts all
  end in 2027 on hábiles or roll by art. 30.5 LPAC: q01 option 14 Dec 2027 (Tue), q06 option 19 Nov 2027 (Fri), q23
  option Sat 13 Nov → Mon 15 Nov 2027. Day counts recomputed with only 12 Oct and 1 Nov in their windows (Sevilla local
  14 Apr and 27 May are outside): q01 Wed 27 Oct, q06 Wed 3 Nov, q23 Thu 4 Nov, q28 Thu 21 Oct 2027, each distractor
  agreeing. Later dates are birthdays or service years (q15 1 Dec 2027, q24 2 Jun 2032/2034/2037) or budget years
  (q18), not working-day checks. All kept answers stand.
- **Stale metadata, no answer affected.** sp-04 `festivos` names dropped q21, q23 and q26. sp-04 q14 `depends_on`
  still quotes «los únicos festivos en Madrid son…», and q11 quotes «quiere cubrir 20 puestos vacantes». Neither
  wording is in the scenario now.

## 2. Table

| id | tema | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|---|
| sp-03/q43 | III.3 | OK | OK | OK | OK | OK | PASS | Art. 125.1 LPAC: «ante el órgano administrativo que los dictó, que también será el competente para su resolución». The firme resolution is the Directora's, so she resolves. The other options are wrong by the same text: the Subsecretaría as superior is the alzada rule, and the Consejo de Ministros and the Consejo de Estado do not resolve it. The lesson m03-l03 cites 125.1 (lines 421–422, 442). Official III.3: no question asks the resolving organ. conv2024_A P1 reserva 5 quotes this sentence in its stem but asks the circumstances, and conv2024_A SI 1 a) is the alzada. No kept question elsewhere on 125.1 (sp-08 q04/q05 are 125.2 plazos). Stem 34 words. Minor: the explanation's «por tratarse de un acto firme» is a loose reason for the Consejo distractors. |
| sp-04/q27 | III.4 | OK | OK | OK | OK | **FAIL** | FAIL | Lightly reworded conv2020_X P1 q28 («en el supuesto de demora en el plazo total de ejecución del contrato:»). Same stem with the case's names. It carries the official key «podrá optar entre la resolución del contrato o la imposición de penalidades» and the official intimation distractor (official c «previa y necesaria intimación al contratista» → «solo después de intimar a la empresa a cumplir»). Its «solo resolver» echoes official a. Checks 1–4 hold: art. 193.3 LCSP, imputability now in the scenario, art. 193.2 «no precisará intimación previa», lesson m03-l04 l. 306–309. |
| sp-04/q28 | V.5 | OK | OK | OK | OK | OK | PASS | Art. 7.2 RD 640/1987: the cash «no podrán exceder de los pagos que se prevea realizar durante un mes». November 2027 has 22 weekdays; minus Mon 1 Nov (national, BOE-A-2026-21254, and named in the scenario) and Tue 9 Nov (stated by the scenario) that leaves 20 × 140 = 2.800 €. Distractors recomputed: 3.080 (22 days), 2.940 (21 days), 4.200 (30 days). No 2028 count. The lesson m05-l05 cites 7.2 (l. 343–346). No official question on art. 7.2 in any bank file. No kept question on the same citation elsewhere (sp-06 q26 is art. 6.2 RD 725/1989). Stem 48 words, with the full title. Note: every distractor is a calendar miscount, the «cifra cercana» pattern. |

## 3. Summary

- **Checked:** 3 replacements, plus the scenario recheck of sp-04 (20 kept) and sp-06 (20 kept).
- **PASS:** 2 (sp-03/q43, sp-04/q28). **FAIL:** 1. By first failing check: not official 1 (sp-04/q27).
- **Kept questions:** all keep their answers under the edited scenarios, including sp-04 q07 and every sp-06 month
  count.
- **Computations recomputed:** 31 (keys and distractors of q28 and q07; the day and month counts of sp-04 q01, q04,
  q12, q14 and q15 and of sp-06 q01, q06, q23 and q28; sp-06 q09, q15 and q24). None disagreed.
