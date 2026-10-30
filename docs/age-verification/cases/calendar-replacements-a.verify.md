# Verification — calendar replacements, batch a (R4, 2026-10-30)

Blind verifier. Spec: `verify-spec.md` with the rulings of 2026-10-28, plus the user rule of 2026-10-30 (only the State
2027 calendar, BOE-A-2026-21254, and the 2027 regional calendars are published; Madrid city's local days count only as
the scenario states them; nothing in 2028 or later may need a working-day check). Articles read with `pdftotext
-layout` from the files named in `sources/normativa.yaml` (LPAC 2024-11-06, LCSP 2026-04-09, RD 33/1986 1991-12-31).
Dates recomputed with Python `datetime` against the published 2027 calendars (State, Madrid, Andalucía + Sevilla local)
and the scenarios' stated days. Writer notes not read.

## 1. Scenario findings

- **Weekdays.** Every dated phrase in the scenarios of sp-02, sp-03, sp-04 and sp-06 and in the six replacements has
  the true weekday.
- **sp-04, festivos sentence** («En los plazos por días son festivos solo el 12 de octubre, el 1 de noviembre, el 6,
  el 8 y el 25 de diciembre»). Checked against every kept sp-04 question:
  - q01 (8 Jun–19 Jul), q04 (16 Jul–5 Aug) and q14 (22 Sep–13 Oct) are day counts. Only 12 Oct falls inside them, and
    it is named. No real 2027 Madrid festivo that the «solo» list leaves out (1 and 6 Jan, 19, 25 and 26 Mar, 1 May,
    16 Aug) falls in any kept window.
  - The month counts end on Mon 15 Nov 2027 (q15), Tue 2 Nov and Mon 22 Nov 2027 (q20). All three are hábiles under
    the published 2027 calendars.
  - No kept answer changes.
- **`SCENARIO` (wording, changes no answer).** The «solo» clashes with the next sentence: «A efectos de este supuesto,
  en Madrid son inhábiles el sábado, 15 de mayo, y el martes, 9 de noviembre de 2027». Read literally, «son festivos
  solo» excludes Tue 9 Nov from the festivos of day plazos, while the next sentence makes it inhábil. No kept day-count
  window includes 15 May or 9 Nov, so no answer depends on which sentence wins.
- **Note, sp-04 q20 (not in this batch).** The explanation gives a count that ends in 2028: «El miércoles 2 de febrero
  de 2028 es la ampliación excepcional a seis meses». That end date holds only if Wed 2 Feb 2028 is hábil, which an
  unpublished calendar decides, where art. 30.5 LPAC applies. It is only a distractor, but it falls under the
  2026-10-30 rule («any count an explanation gives»). For the coordinator.
- **sp-06, «los plazos por meses terminan en día hábil».** No kept sp-06 question rests on it for a 2028 date.
  - The kept month counts all end in 2027: q01 option «14 de diciembre de 2027», q06 option «19 de noviembre de 2027»,
    and q23 option «15 de noviembre de 2027» (Sat 13 Nov rolled to Mon 15 Nov). All are hábiles under the published
    Andalucía and Sevilla 2027 calendars.
  - The dates after 2027 are birthdays, not plazos: q15 and q24 (2 Jun 2032, 2034, 2037). q18's later years are
    budget years.
  - The sentence is now vestigial. The case's `festivos` field still names the dropped q05 and q14 (stale metadata).
- **Duplicates.** `case_check.py sp-02 sp-03 sp-04 sp-06` prints no DUPLICATE.

## 2. Table

| id | tema | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|---|
| sp-02/q27 | III.6 | OK | OK | OK | OK | OK | PASS | Art. 67.1 LPAC: «En caso de daños de carácter físico o psíquico… desde la curación». Alta Thu 4 Feb 2027 is the key; the weekdays are right; no 2028 count anywhere. The lesson cites 67.1. Official III.6 cases (2020 SI q4, 2020_X SI res. 3, 2022_X SI q11, annulled) ask for the prescription date or «¿en plazo?». This stem asks for the start date, and its options are new. Not a copy. |
| sp-03/q41 | III.3 | OK | OK | **FAIL** | OK | OK | FAIL | Art. 115.2 LPAC only says the miscalification is no obstacle «siempre que se deduzca su verdadero carácter». The key's «porque se deduce que es un recurso extraordinario de revisión» rests on art. 125.1.a) LPAC (acto firme, «error de hecho, que resulte de los propios documentos incorporados al expediente»), which the citation does not carry. |
| sp-03/q42 | III.3 | OK | OK | OK | OK | OK | PASS | Art. 126.3 LPAC: three months from the interposición. Mon 12 Jul + 3 months = Tue 12 Oct 2027 (Fiesta Nacional, BOE-A-2026-21254), rolled to Wed 13 Oct 2027 (art. 30.4–30.5 LPAC, the default cómputo). Distractors recomputed: 90 natural days end Sun 10 Oct → Mon 11 Oct; 2 months end Sun 12 Sep → Mon 13 Sep. The interposición falls within art. 125.2's four months (ends Thu 14 Oct). The norm is named by number and date only, allowed by the ruling because the full title would push the stem past 50 words. The lesson cites 126.3. No official 126.3 question. |
| sp-04/q26 | III.4 | **FAIL** | — | OK | — | OK | FAIL | The key «Sí» needs a fact the case does not give. The INE may opt for resolution only when the contractor is in demora «por causas imputables al mismo» (art. 193.3 LCSP). Otherwise art. 195.2 grants an extension. Neither the scenario nor the stem says the 13-day delay (Fri 22 Oct → Thu 4 Nov, recomputed) is imputable. The tablets are also already delivered in full. Official 2020_X P1 q28 makes imputability the deciding term. Note: kept q07 shares the imputability gap. |
| sp-06/q27 | III.3 | OK | OK | OK | OK | OK | PASS | Art. 108 LPAC: «podrá suspender la ejecución del acto, cuando ésta pudiera causar perjuicios de imposible o difícil reparación». The key matches. The distractors (always, after the dictamen, only at the titular's request) are each wrong by the text. The lesson cites 108. Official 2022_X P1 res. 3 has the same key, but its stem is a sentence to complete and none of its distractors is carried, so not a copy under the 2026-10-28 ruling. Minor: the explanation's «la suspensión llega con el inicio de la revisión» reads loosely. |
| sp-06/q28 | IV.6 | OK | OK | OK | OK | OK | PASS | Art. 36 RD 33/1986: «un plazo de diez días». Counted in días hábiles under art. 30.2–30.3 LPAC (default cómputo; lesson m04-l06 says so). From Wed 6 Oct 2027 the 10th hábil day is Thu 21 Oct 2027. Andalucía and Sevilla 2027 have only 12 Oct in the window. Recomputed: without the festivo, Wed 20 Oct; 10 natural days end Sat 16 Oct → Mon 18 Oct; 15 hábiles end Thu 28 Oct. The norm is named by number and date, allowed by the ruling (the full title would push the stem past 50 words). No official IV.6 question on the pliego de cargos. Minor: «el plazo de la audiencia del artículo 82.2» for fifteen days is the plazo's maximum, not the whole rule. |

## 3. Summary

- **Checked:** 6. **PASS:** 4 (sp-02/q27, sp-03/q42, sp-06/q27, sp-06/q28). **FAIL:** 2.
- **Fails by first failing check:** key 1 (sp-04/q26), citation 1 (sp-03/q41).
- **Computations recomputed:** 14 (keys and every distractor count in sp-03/q42 and sp-06/q28, the sp-04/q26 delay,
  the sp-02/q27 weekdays and the art. 125.2 window). None disagreed.
