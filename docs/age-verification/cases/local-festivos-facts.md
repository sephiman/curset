# Local festivos stated as case facts (2027), R4, 2026-10-30

User decision: no case question depends on an unpublished calendar. Madrid city (15 May Sat, 9 Nov Tue), Valladolid (13 May Thu, 8 Sep Wed) and Zaragoza (29 Jan Fri, 5 Mar Fri) are not in a bulletin, so the scenario states the days the councils fixed. Weekdays checked with Python `datetime`. Rule applied: an edit is made when a hábil-day window of a kept question, or a month-window rollover, touches the city's local day (key or explanation count); a natural-day window that merely spans a local day depends on no calendar and is not edited. Only the local day(s) a window touches are named, to stay within 550 words.

## Edited cases

| Case | Place | Windows touching a local day | Scenario sentence before | Scenario sentence after | Words before → after |
|---|---|---|---|---|---|
| sp-03 | Madrid | q23 (9 Nov, 10 hábiles from 28 Oct); q22/q24 end outside local days | "Los únicos festivos de Madrid en los plazos por días son el martes, 12 de octubre, el lunes, 1 de noviembre, el martes, 9 de noviembre, el lunes, 6 de diciembre y el miércoles, 8 de diciembre de 2027." | "Los únicos festivos en los plazos por días son el 12 de octubre, el 1 de noviembre, el 6 y el 8 de diciembre y, el que fija el Ayuntamiento de Madrid, el martes, 9 de noviembre de 2027." | 548 → 548 |
| sp-04 | Madrid | q23 (30 hábiles from 5 Nov, distractor 21 Dec crosses 9 Nov) | "En los plazos por días de este caso, los únicos festivos en Madrid son el 12 de octubre, el 9 de noviembre, el 6, el 8 y el 25 de diciembre y el 1 de enero." | "En los plazos por días solo son festivos el 12 de octubre, el 6, el 8 y el 25 de diciembre, el 1 de enero y, el que fija el Ayuntamiento de Madrid, el martes, 9 de noviembre de 2027." | 546 → 550 |
| sp-05 | Madrid | q05 (hábiles from 18 May; the explanation puts Sat 15 May outside the count) | "El martes, 12 de octubre, y el lunes, 1 de noviembre de 2027, son festivos en toda España; ningún otro festivo cae dentro de los plazos por días ni en el último día de los plazos por meses de las cuestiones." | "Son festivos el 12 de octubre y el 1 de noviembre y, los que fija el Ayuntamiento de Madrid, el sábado, 15 de mayo, y el martes, 9 de noviembre de 2027; ningún otro afecta a los plazos." | 549 → 546 |
| sp-07 | Madrid | q19 (15 hábiles from 27 Oct, 9 Nov excluded) | "…está en Madrid, donde son festivos el lunes, 1 de noviembre, y el martes, 9 de noviembre de 2027. Ningún otro festivo afecta a los plazos que cuentan las cuestiones." | "…está en Madrid. Son festivos el 1 de noviembre y, el que fija el Ayuntamiento de Madrid, el martes, 9 de noviembre de 2027; ningún otro afecta a los plazos." | 549 → 549 |
| sp-08 | Madrid | q02 (15 hábiles from 9 Nov); q09 (15 hábiles from 13 May, Sat 15 May inside) | "…donde son festivos el jueves, 25, y el viernes, 26 de marzo de 2027, el lunes, 1, y el martes, 9 de noviembre de 2027, y el lunes, 6, y el miércoles, 8 de diciembre de 2027. Ningún otro festivo cae en los plazos por días." | "…está en Madrid. Son festivos el 25 y el 26 de marzo, el 1 de noviembre y el 6 y el 8 de diciembre y, los que fija el Ayuntamiento de Madrid, el sábado, 15 de mayo, y el martes, 9 de noviembre de 2027; ningún otro afecta a los plazos." | 548 → 550 |
| sp-10 | Madrid | q05 (15 hábiles from 27 Oct, 9 Nov excluded) | "Son festivos en Madrid el lunes, 1, y el martes, 9 de noviembre, y el lunes, 6, y el miércoles, 8 de diciembre de 2027; ningún otro cae en los plazos por días." | "Son festivos el 1 de noviembre y el 6 y el 8 de diciembre y, el que fija el Ayuntamiento de Madrid, el martes, 9 de noviembre de 2027; ningún otro cae en los plazos por días." | 543 → 547 |
| sp-14 | Madrid | q09 (15 hábiles from 5 Nov, 9 Nov excluded) | "Son inhábiles, además de sábados y domingos, el lunes, 16 de agosto de 2027, el martes, 12 de octubre de 2027, el lunes, 1 de noviembre de 2027, el martes, 9 de noviembre de 2027 y el lunes, 6 de diciembre de 2027." | "Son inhábiles, además de sábados y domingos, el lunes, 16 de agosto de 2027, el martes, 12 de octubre de 2027, el lunes, 1 de noviembre de 2027 y el lunes, 6 de diciembre de 2027, y, el que fija el Ayuntamiento de Madrid, el martes, 9 de noviembre de 2027." | 496 → 504 |
| sp-16 | Madrid | q21 (two months end on Tue 9 Nov, rolls to the next hábil day) | "…, el viernes, 26 de marzo de 2027, el lunes, 16 de agosto de 2027 y el martes, 9 de noviembre de 2027." | "…, el viernes, 26 de marzo de 2027 y el lunes, 16 de agosto de 2027, y, el que fija el Ayuntamiento de Madrid, el martes, 9 de noviembre de 2027." | 542 → 550 |

## sp-01 (Madrid, replacement for 2028)

No window touches 15 May or 9 Nov 2027; the scenario sentence is unchanged (547 words). Kept q30 counted 30 natural days into March 2028 with a 30-hábiles distractor (20 Mar 2028), so it is dropped (row added to `drops.tsv`) and replaced by q44 (`replaces` q30, III.4, art. 159.3 LCSP): abierto simplificado de obras, anuncio on Wed 14 Apr 2027, plazo of 20 natural days (DA 12.ª LCSP) from Thu 15 Apr ends Tue 4 May 2027 (key); distractors Thu 29 Apr (15 days, not obras), Mon 3 May (publication day counted), Wed 12 May (20 hábiles). All asserted by script (`scratchpad/local-fest/sp01_q44.py`); the only festivo in the windows is Sat 1 May (national); 2 May is a Sunday (Decreto 82/2026). Not asked in another case (no `art. 159.3 LCSP` in `kept-index.tsv`). `festivos` field updated; computations 9 dates + 4 amounts = 13.

## Not edited

- sp-02 (Valladolid, 13 May and 8 Sep): no hábil window or rollover touches them (hábil windows 4-17 Feb, 9 Feb-1 Mar, 10-17 Jun, 6 Jul-17 Aug, 1-22 Mar; months end 9 Jul, 31 Aug, 6 Sep not used). q08 (60 natural days from 3 May) spans 13 May but counts natural days: no dependence. Flag for the coordinator if natural spans must also be stated.
- sp-12 (Madrid + Zaragoza): Zaragoza only enters q02 (23 Apr, Día de Aragón, published in the BOA decree); q04/q05 are Madrid procedures (29 Jan, 5 Mar not counted for Madrid). q06 spans 15 May only as a natural-day distractor.
- sp-19 (Madrid; Zaragoza only as a destination), sp-09, sp-11, sp-13, sp-18, sp-20: no hábil window or rollover touches 15 May or 9 Nov (month windows spanning them end on other days).
- sp-06 (Sevilla), sp-17 (Murcia): not in the three cities; their local days are in BOJA / BORM.
- sp-15 (Toledo): kept windows end on 17 Mar 2027 at the latest (q03 and q08 month windows end Mon 15 Mar; q08 distractor Wed 17 Mar; q16 and the others 8-10 Feb). None touches Fri 19 Mar or Mon 29 Mar 2027; no edit.

## Final check

`case_check.py sp-01 … sp-20 --anchors` from `backend/`: no DUPLICATE, no anchor miss; scenarios ≤ 550 words; remaining flags are the informational «named? fine» lines and pre-existing ones (sp-06 q15 norm title).


## Wording, 2026-10-30

Round R4. Words per scenario (before → after): sp-03 555 → 550; sp-04 557 → 549; sp-05 547 → 548; sp-07 556 → 539; sp-08 551 → 545; sp-10 554 → 550; sp-16 557 → 550; sp-14 unchanged (511).

Local-day sentence kept verbatim in every case. In sp-04 the `festivos` field now says «son festivos» instead of «solo son festivos»; the other `festivos` fields describe the calendar facts and needed no change. sp-14: its festivos sentence already reads correctly and was left alone.


### sp-03

- before: «Los únicos festivos en los plazos por días son el 12 de octubre, el 1 de noviembre, el 6 y el 8 de diciembre.»
  after: «En los plazos por días son festivos el 12 de octubre, el 1 de noviembre y el 6 y el 8 de diciembre.»
- before: «solicitud de certificación el»
  after: «solicitud el»
- before: «en ese capítulo, no ampliable.»
  after: «en ese capítulo.»

### sp-04

- before: «En los plazos por días solo son festivos el 12 de octubre, el 6, el 8 y el 25 de diciembre, el 1 de enero.»
  after: «En los plazos por días son festivos el 12 de octubre, el 6, el 8 y el 25 de diciembre y el 1 de enero.»
- before: « La norma reguladora califica la infracción como leve.»
  after: (deleted)

### sp-05

- before: «Son festivos el 12 de octubre y el 1 de noviembre; ningún otro afecta a los plazos. A efectos de este supuesto, en Madrid son inhábiles el sábado, 15 de mayo, y el martes, 9 de noviembre de 2027.»
  after: «Son festivos el 12 de octubre y el 1 de noviembre. A efectos de este supuesto, en Madrid son inhábiles el sábado, 15 de mayo, y el martes, 9 de noviembre de 2027. Ningún otro festivo afecta a los plazos.»

### sp-07

- before: «Son festivos el 1 de noviembre; ningún otro afecta a los plazos. A efectos de este supuesto, en Madrid son inhábiles el sábado, 15 de mayo, y el martes, 9 de noviembre de 2027.»
  after: «Son festivos el 1 de noviembre. A efectos de este supuesto, en Madrid son inhábiles el sábado, 15 de mayo, y el martes, 9 de noviembre de 2027. Ningún otro festivo afecta a los plazos.»
- before: « Don Nicolás Aznar Bielsa, funcionario de la Mutualidad, obtiene por concurso un puesto en el Gobierno de Aragón.»
  after: (deleted)

### sp-08

- before: «el 6 y el 8 de diciembre; ningún otro afecta a los plazos. A efectos de este supuesto, en Madrid son inhábiles el sábado, 15 de mayo, y el martes, 9 de noviembre de 2027.»
  after: «el 6 y el 8 de diciembre. A efectos de este supuesto, en Madrid son inhábiles el sábado, 15 de mayo, y el martes, 9 de noviembre de 2027. Ningún otro festivo afecta a los plazos.»
- before: « Ambas quieren interponer recurso extraordinario de revisión.»
  after: (deleted)

### sp-10

- before: «el 6 y el 8 de diciembre; ningún otro cae en los plazos por días. A efectos de este supuesto, en Madrid son inhábiles el sábado, 15 de mayo, y el martes, 9 de noviembre de 2027.»
  after: «el 6 y el 8 de diciembre. A efectos de este supuesto, en Madrid son inhábiles el sábado, 15 de mayo, y el martes, 9 de noviembre de 2027. Ningún otro festivo cae en los plazos por días.»
- before: «Otra licitadora, Controles»
  after: «Controles»
- before: «En otro contrato, Seguridad»
  after: «Seguridad»

### sp-16

- before: «al tropezar con un peldaño mal señalizado de uno de esos teatros.»
  after: «al tropezar con un peldaño.»
