# Calendar audit 2b — round R4, 2026-10-30

Blind re-audit after the local-day edits (`local-festivos-facts.md`) under the user rule of 2026-10-30: no case
question may depend on an unpublished calendar. Kept questions from `case_check.kept()` (draft minus `drops.tsv`
plus `restored.tsv`). Calendar used: BOE-A-2026-21254 and Decreto 82/2026 (Madrid 2027: 1 and 6 Jan, 19, 25 and
26 Mar, 1 May, 16 Aug, 12 Oct, 1 Nov, 6, 8 and 25 Dec) plus the Madrid city days that each scenario states (Sat
15 May, Tue 9 Nov 2027). LPAC: hábiles exclude Sat/Sun/festivos, months date to date (art. 30.4), last day inhábil
→ next hábil (art. 30.5), August hábil; LJCA: August excluded (art. 128.2); LCSP: naturales unless hábiles (DA 12.ª).
Script: `/tmp/claude-1000/-home-juanjo-PycharmProjects-curset/cdf6381c-e69f-4bd9-ab76-b6a993e1c132/scratchpad/audit-2b/calc.py`
(127 computations, 1 mismatch); part 2 scan `scan2.py` in the same folder.

Criterion for «depends»: the key or a count the explanation states ends on a day whose hábil status comes from an
unpublished calendar (Madrid city or Valladolid or Zaragoza local days not stated in the scenario, or any year from
2028 on), and the end is a plazo to which art. 30.5 LPAC applies, with no scenario sentence settling it. Ages, start
dates and maximum durations of a measure or of liability (suspension, interim appointment, prescription of a
falta, the contractor's 15 years) are counted date to date with no roll and are listed as notes, not dependencies.

## Part 1 — sp-08, sp-10, sp-14, sp-16

### Scenario findings

| Case | Verdict | Finding |
|---|---|---|
| sp-08 | OK | Festivos sentence (25, 26 Mar, 1 Nov, 6, 8 Dec) and local-day sentence (15 May, 9 Nov) agree; «Ningún otro festivo afecta a los plazos» holds for every kept window (19 Mar, 16 Aug and 12 Oct fall in none; 25 Dec is a Saturday). The cut «Ambas quieren interponer recurso extraordinario de revisión» is carried by the q04 and q05 stems. Note: the q08 stem names «Atención Telefónica Meridiano, S.A.», a name the scenario never gives («la empresa con la mejor oferta»); «que el SEPE le ha requerido» ties it, so no answer changes. `depends_on` of q02, q08, q20 still quotes the pre-edit festivos sentence (metadata only). |
| sp-10 | OK, one completeness note | Festivos and local-day sentences agree; «Ningún otro festivo cae en los plazos por días» holds. **Note:** the q21 distractor (Tue 17 Aug, «el mes … acaba el lunes, 16 de agosto, festivo en Madrid») rests on 16 Aug, which the scenario does not name; it is published (Decreto 82/2026) and the key does not change. The cuts «Otra licitadora» / «En otro contrato» now let Seguridad Digital Meseta read as the auditoría adjudicataria; no kept question contradicts that (q09 uses only the delivery date). `depends_on` of q05, q09, q19, q25 quotes the pre-edit festivos sentence. |
| sp-14 | OK | Inhábiles sentence (16 Aug, 12 Oct, 1 Nov, 6 Dec) and local-day sentence (15 May, 9 Nov) agree; 8 Dec is not named and no window reaches it (last day window ends 29 Nov). |
| sp-16 | OK | Inhábiles sentence (19, 25, 26 Mar, 16 Aug) and local-day sentence agree; 12 Oct and 1 Nov lie in no day window. The cut «mal señalizado de uno de esos teatros» leaves the place of the fall implicit («espectador», the Instituto «con … varios teatros»); no kept question needs the place or the cause (q01, q03, q04, q05 use dates and the amount). |

Weekdays: `case_check.py --anchors` reports no wrong weekday in the four cases.

### Date questions

| Case/id | Key | Explanation counts | Unpublished day touched | Verdict | Note |
|---|---|---|---|---|---|
| sp-08/q02 | Tue 30 Nov ✓ | ✓ (23 Nov, 29 Nov, 9 Dec) | 9 Nov — stated | PASS | |
| sp-08/q03 | Mon 18 Jan 2027 ✓ | ✓ (360 days = 11 Jan) | — | PASS | |
| sp-08/q04 | Mon 27 Sep ✓ | ✓ (4×365 = 25 Sep) | — | PASS | |
| sp-08/q05 | Mon 13 Sep ✓ | ✓ (90 days = 9 Sep) | — | PASS | |
| sp-08/q21 | Thu 9 Dec ✓ | ✓ (3, 7, 16 Dec) | — | PASS | |
| sp-08/q08 | Wed 7 Apr ✓ | ✓ (5, 6, 1 Apr) | — | PASS | |
| sp-08/q09 | Wed 2 Jun ✓ | ✓ (27 May, 1 Jun, 14 Jun) | 15 May (Sat) — stated | PASS | |
| sp-08/q12 | Mon 12 Jul ✓ | ✓ (6, 9, 19 Jul) | — | PASS | |
| sp-08/q23 | Thu 30 Sep ✓ | no counts | — | PASS | |
| sp-08/q20 | Tue 7 Dec ✓ | 27 Dec ✓; **Mon 6 Mar 2028** | 2028 | **FAIL** | «La del lunes, 6 de marzo de 2028, es la de la ampliación excepcional a seis meses» — end of a plazo to justify, valid only if 6 Mar 2028 is hábil in Madrid; 2028 calendar unpublished |
| sp-10/q02 | Thu 30 Sep ✓ | 30 Aug, 29 Sep ✓; **30 Dec wrong** | — | **FAIL (1)** | «La del jueves, 30 de diciembre de 2027, aplica los seis meses del acto presunto»: with August excluded, as the explanation itself states (art. 128.2 LJCA), six months from 30 Jun end Sun 30 Jan 2028 → Mon 31 Jan 2028; 30 Dec counts August |
| sp-10/q26 | Mon 25 Oct ✓ | ✓ | — | PASS | |
| sp-10/q23 | Thu 14 Oct ✓ | ✓ (13 Oct, 28 Sep, 15 Nov) | — | PASS | |
| sp-10/q05 | Thu 18 Nov ✓ | ✓ (10, 16, 17 Nov) | 9 Nov — stated | PASS | |
| sp-10/q06 | Wed 29 Sep ✓ | ✓ | — | PASS | |
| sp-10/q24 | Tue 17 Aug ✓ | ✓ (2 Jul, 7 Sep, 19 Jul) | — | PASS | |
| sp-10/q08 | Mon 9 Aug ✓ | ✓ (3, 6 Aug, 8 Sep) | — | PASS | |
| sp-10/q09 | Tue 7 Dec ✓ | ✓ | — | PASS | |
| sp-10/q21 | Mon 2 Aug ✓ | ✓ (17 Aug via 16 Aug, published) | — | PASS | Scenario note above |
| sp-10/q13 | Thu 30 Sep ✓ | ✓ | — | PASS | |
| sp-10/q14 | Mon 30 Aug ✓ | ✓ | — | PASS | |
| sp-10/q16 | Tue 29 Feb 2028 ✓ | ✓ (28 Feb, 1 Mar, 180 days = Sat 26 Feb 2028) | 2028 (duration) | PASS | Note: maximum duration of a suspension, date to date, no roll; coordinator may treat as 2028-dependent |
| sp-10/q25 | Thu 4 Nov ✓ | ✓ (3, 12, 19 Nov; 12 Nov needs the stated 9 Nov) | 9 Nov — stated | PASS | |
| sp-10/q19 | Thu 9 Dec ✓ | ✓ | — | PASS | |
| sp-14/q01 | Thu 3 Jun ✓ | ✓ | — | PASS | |
| sp-14/q02 | Tue 8 Jun ✓ | ✓ | — | PASS | |
| sp-14/q04 | Mon 23 Aug ✓ | ✓ (18, 20, 24 Aug) | — | PASS | |
| sp-14/q21 | Thu 9 Sep ✓ | ✓ | — | PASS | |
| sp-14/q07 | Mon 27 Sep ✓ | ✓ | — | PASS | |
| sp-14/q09 | from Tue 30 Nov ✓ | ✓ (19, 20, 29 Nov) | 9 Nov — stated | PASS | |
| sp-14/q11 | Wed 1 Sep 2027 ✓ | ✓ | — | PASS | 2036 distractor is a start date, no calendar |
| sp-14/q15 | Fri 18 Oct 2030 ✓ | ✓ | 2029/2030/2033 (prescription) | PASS | Note: prescription of a falta, date to date, no roll |
| sp-14/q20 | **Wed 5 Apr 2028** | 5 Jan, 5 Jul, 5 Oct 2028 | 2028 | **FAIL** | Key is the last day of the extended plazo to justify (art. 10.1 RD 640/1987); it holds only if 5 Apr 2028 is hábil in Madrid; 2028 calendar unpublished, no scenario statement |
| sp-16/q01 | Tue 17 Aug ✓ | ✓ | — | PASS | |
| sp-16/q02 | Fri 16 Apr ✓ | ✓ (15, 14, 1 Apr) | — | PASS | |
| sp-16/q03 | Fri 24 Sep ✓ | ✓ (23, 20 Sep; 7 Sep from 17 Aug) | — | PASS | |
| sp-16/q05 | Mon 2 Aug ✓ | ✓ (30 Jul, 31 Aug) | — | PASS | |
| sp-16/q08 | Thu 18 Nov ✓ | ✓ (17 Nov, 2 Nov, 18 Dec) | — | PASS | |
| sp-16/q21 | Wed 10 Nov ✓ | ✓ (9 Nov, 8 Nov, 9 Dec) | 9 Nov — stated | PASS | |
| sp-16/q16 | Thu 5 Aug ✓ | ✓ (3 Aug, 31 Jul, 28 Jul) | — | PASS | |

Part 1: 40 date questions checked, 37 PASS, 3 FAIL (sp-08/q20 calendar, sp-10/q02 check 1, sp-14/q20 calendar).

## Part 2 — sp-02, sp-06, sp-09, sp-11, sp-12, sp-13, sp-17, sp-18, sp-19, sp-20

No kept question's key or explanation count ends on, or counts hábiles across, Madrid 15 May / 9 Nov, Valladolid
13 May / 8 Sep or Zaragoza 29 Jan / 5 Mar 2027 (sp-12 q04 is «instruido en Madrid»; sp-19 uses Zaragoza only as a
destination). Dependencies found, all on future-year calendars:

| Case/id | Day touched | Why it depends |
|---|---|---|
| sp-02/q05 | Fri 4 Feb 2028 (key), Valladolid | One-year plazo to claim (art. 67.1 LPAC) ends there; holds only if 4 Feb 2028 is hábil; 2028 calendar unpublished, no scenario sentence settles it |
| sp-09/q04 | Mon 13 Mar 2028 (key), Madrid | Four years end Sun 12 Mar 2028 and the key rolls to Mon 13 Mar 2028 (art. 30.5), assuming it hábil; 2028 calendar unpublished |
| sp-09/q12 | Mon 20 Dec 2038 (distractor count), Madrid | «La del lunes, 20 de diciembre de 2038, cuenta diez años y pasa del sábado al lunes» assumes 20 Dec 2038 hábil; key (Fri 18 Dec 2043) itself does not depend |

Touches of 2028 or later that do not depend (notes): sp-06 q05 and q14 (2028 month ends; the scenario states «los
plazos por meses terminan en día hábil»); sp-11 q20 and q23 distractors (same scenario statement; q23 is
prescription); sp-11 q12 (start date 2028); sp-17 q10 (nine-month interim appointment ends Wed 12 Jan 2028, a
maximum duration); sp-06 q24, sp-18 q22 (ages); sp-19 q22 (prórroga start dates 2029–2032); sp-09 q12 key (15 years
of liability, 2043).

## drops.tsv

Appended (batch `calendar-audit-2b`): sp-08/q20, sp-10/q02, sp-14/q20, sp-02/q05, sp-09/q04, sp-09/q12.
**sp-02/q05 is listed in `restored.tsv` (reread-1)**: `case_check.drops()` subtracts restored ids, so the new row
does not drop it until the coordinator resolves that row.
