# Calendar audit 2a — round R4, cases sp-01, sp-03, sp-04, sp-05, sp-07, sp-15

Date: 2026-10-30. Blind re-audit after the local-day edits (`local-festivos-facts.md`) under the user rule of
2026-10-30: no case question may depend on an unpublished calendar. Scope: kept questions (draft minus `drops.tsv`
plus `restored.tsv`, `replaces` followed), every `"computes": "date"` question (49), plus scenario completeness for
the edited cases and the five checks for sp-01 q44.

Calendars used: Madrid 2027 = BOE-A-2026-21254 + Decreto 82/2026 (1 Jan, 6 Jan, 19 Mar, 25–26 Mar, 1 May, 16 Aug,
12 Oct, 1 Nov, 6 Dec, 8 Dec, 25 Dec) + the scenario-stated local days Sat 15 May and Tue 9 Nov 2027. Toledo 2027 =
Decreto 34/2026 (DOCM) + BOP Toledo 22-10-2026 (19 and 29 Mar). Madrid 2028 and later: none published, so only
Saturdays and Sundays are certain. Rules: LPAC hábiles exclude Sat/Sun/festivos, months date to date, last day
inhábil → next hábil; LCSP naturales unless hábiles (DA 12.ª, with roll). Script:
`/tmp/claude-1000/-home-juanjo-PycharmProjects-curset/cdf6381c-e69f-4bd9-ab76-b6a993e1c132/scratchpad/audit-2a/run.py`
(194 assertions; the one mismatch was a reading of mine, not the explanation's: sp-03 q32 d counts the 20 hábiles
from the publication, as it says).

## 1. Scenario findings

**sp-03.** Complete. The cuts («solicitud de certificación» → «solicitud»; «no ampliable» deleted) break nothing:
q22 needs only a procedure started at the citizen's request, and q37 asks only the Directora's limit for the
suplemento the scenario says is needed. The festivos sentence (12 Oct, 1 Nov, 6 and 8 Dec) and the local-day
sentence (15 May, 9 Nov) do not contradict each other. Fault: the festivos sentence covers only «los plazos por
días» of 2027. It says nothing about the month or year windows that roll into 2028 and 2031 (q22, q25). See §2.

**sp-04.** No kept question needs «La norma reguladora califica la infracción como leve.» q01 (art. 96.6) starts from
the simplified procedure the scenario says the INE agreed to. Art. 96.5 requires the organ to consider the infraction
leve before agreeing it, and the scenario's statement that it agreed implies that. q02 needs only «solo pecuniaria»,
and q03 needs only the sanctioning procedure. The leve negligence in q22 (art. 36.2 LRJSP) is Don Gaspar's and is
still stated. No contradiction between the festivos and local-day sentences.

The rewording removed «solo», so the list (12 Oct, 6, 8 and 25 Dec, 1 Jan) is no longer closed. That has two effects:
- **SCENARIO, harmless.** 1 Nov 2027 is missing. No kept window counts hábiles across it.
- **SCENARIO, breaks q08.** The rewording reopens q08's dependence on Madrid's 2028 calendar. q08's `depends_on` still
  quotes «los únicos festivos en Madrid son …».

The local day (9 Nov) now touches no kept question, because q23 is not kept. The `festivos` field still describes
q21 and q23, and neither is kept.

**sp-05.** Complete and consistent. «Son festivos el 12 de octubre y el 1 de noviembre … 15 de mayo … 9 de noviembre
… Ningún otro festivo afecta a los plazos» holds against the published calendar: no kept window contains 19 Mar,
25–26 Mar, 16 Aug, 6 Dec or 8 Dec.

**sp-07.** Complete. The deleted Don Nicolás sentence was used only by q10, which is dropped and replaced by q22.
Two faults:
- **SCENARIO, wording (check 16).** «Son festivos el 1 de noviembre» uses a plural verb for one date. It should be
  «Es festivo el 1 de noviembre». It breaks no question.
- **Minor tension.** «Ningún otro festivo afecta a los plazos» against the q24 explanation, which excludes Fri
  19 Mar 2027 («festivo en Madrid»). That day lies only in the count of a wrong distractor, not in a plazo the
  question asks. The count is right on the published calendar (BOCM), and the key does not change. Not failed.

**sp-01 (not edited, checked for q44).** «solo son inhábiles sábados y domingos» in the counted hábil plazos is true
for every window a key uses. The q43 explanation excludes 19 Mar, festivo in Madrid, in a distractor count, which is
the same minor tension as sp-07 q24. Not failed.

**sp-15 (not edited).** «Entre el 11 de enero y el 18 de marzo de 2027 no cae en Toledo ningún festivo» is true:
CLM's 2027 days fall outside that span, and Toledo's 19 and 29 Mar fall after it. The Madrid seat of the Jefatura
Central adds nothing inside the span either.

## 2. Date questions

| Case/id | Key holds | Explanation counts hold | Unpublished-calendar dependency | Note |
|---|---|---|---|---|
| sp-01/q21 | yes | yes | no | |
| sp-01/q41 | yes | yes | no | |
| sp-01/q43 | yes | yes | no | Distractor 23 Mar excludes San José (published); see §1 |
| sp-01/q24 | yes | yes | no | |
| sp-01/q25 | yes | yes | no | 9 Aug stated hábil by the scenario and true on the BOCM |
| sp-01/q26 | yes | yes | no | |
| sp-01/q44 | yes | yes | no | 4 May 2027 Tue hábil; window holds only Sat 1 May |
| sp-01/q31 | yes | yes | no | |
| sp-01/q33 | yes | yes | no | Month-level (Feb 2030); no day calendar |
| sp-03/q22 | yes on weekends only | yes | **yes** | Sat 5 Feb 2028 → Mon 7 Feb 2028: hábil status of a 2028 day, unpublished, not stated. **FAIL 1** |
| sp-03/q23 | yes | yes | no | 9 Nov from the scenario's local-day sentence; d (8 Nov) = 10 naturales ending Sun 7 Nov rolled |
| sp-03/q24 | yes | yes | no | |
| sp-03/q25 | yes on weekends only | yes | **yes** | Sat 14 Jun 2031 → Mon 16 Jun 2031: Madrid 2031 unpublished, not stated. **FAIL 1** |
| sp-03/q27 | yes | yes | no | c (13 Oct) = 5 naturales ending on festivo 12 Oct, rolled |
| sp-03/q32 | yes | yes | no | |
| sp-03/q33 | yes | yes | no | |
| sp-04/q01 | yes | yes | no | |
| sp-04/q04 | yes | yes | no | |
| sp-04/q08 | yes on weekends only | d holds only with 6 Jan 2028 inhábil (19 Jan; 18 Jan if hábil) | **yes** | Key needs Mon 3 Jan 2028 hábil; d needs Thu 6 Jan 2028 inhábil; list no longer closed. **FAIL 1** |
| sp-04/q12 | yes | yes | no | Natural days |
| sp-04/q14 | yes | yes | no | |
| sp-04/q15 | yes | yes | no | |
| sp-04/q20 | yes | yes | no | d (Wed 2 Feb 2028) is a raw six-month date; no hábil claim |
| sp-05/q02 | yes | yes | no | |
| sp-05/q03 | yes | yes | no | |
| sp-05/q22 | yes | yes | no | |
| sp-05/q05 | yes | yes | no | Sat 15 May before the window |
| sp-05/q07 | yes | yes | no | |
| sp-05/q11 | yes | yes | no | 1 Nov stated |
| sp-05/q14 | yes | yes | no | |
| sp-07/q01 | yes | yes | no | |
| sp-07/q02 | yes | yes | no | |
| sp-07/q24 | yes | yes | no | b 23 Mar excludes 19 Mar (published); see §1 |
| sp-07/q04 | yes | yes | no | |
| sp-07/q23 | yes | yes | no | |
| sp-07/q08 | yes | yes | no | Backward date-to-date in 2029; no hábil claim |
| sp-07/q11 | yes | yes | no | 1 Nov stated |
| sp-07/q14 | yes | yes | no | |
| sp-07/q15 | yes | yes | no | |
| sp-07/q18 | yes | yes | no | |
| sp-07/q19 | yes | yes | no | 9 Nov from the scenario's local-day sentence |
| sp-15/q02 | yes | yes | no | |
| sp-15/q03 | yes | yes | no | |
| sp-15/q04 | yes | yes | no | |
| sp-15/q08 | yes | yes | no | |
| sp-15/q09 | yes | yes | no | |
| sp-15/q10 | yes | yes | no | |
| sp-15/q13 | yes | yes | no | |
| sp-15/q14 | yes | yes | no | |

49 date questions. Every key and every stated distractor count holds as arithmetic. Three questions rest on an
unpublished calendar and fail check 1. The fix for each is a one-clause case fact, as sp-01 does with «el lunes,
9 de agosto de 2027, es hábil». For sp-04 q08, the distractor d also needs replacing.

## 3. sp-01 q44 (replaces q30)

| id | tema | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict |
|---|---|---|---|---|---|---|---|
| q44 | III.4 | PASS | PASS | PASS | PASS | PASS | **PASS** |

1. Art. 159.3 LCSP (consolidated 2026-04-09) says «no podrá ser inferior a quince días a contar desde el siguiente a
   la publicación … En los contratos de obras el plazo será como mínimo de veinte días». DA 12.ª makes these natural
   days. The 20th natural day from Thu 15 Apr is Tue 4 May 2027, which is hábil. The distractors also check out:
   29 Apr = 15 days, 3 May = publication day counted, 12 May = 20 hábiles (also under the scenario's
   weekends-only sentence).
2. Only 4 May is the earliest end for an obras contract. The scenario makes the contract obras («entrega la obra»,
   «certificación de obra») and abierto simplificado.
3. Art. 159.3 holds the key, and lesson `m03-l04` cites it in prose (line 196) and in its table (line 224).
4. The stem is 49 words, art-pregunta form, with the full BOE title. The options are dates with weekday and year, and
   the key is not the longest option. The explanation covers every distractor by content. It uses case facts (obras,
   abierto simplificado) and does not contradict the scenario: the 14 Apr anuncio comes before the 21 Jul garantía
   requirement.
5. The closest official question, conv2024_A S-II 15, asks the minimum plazo for a services contract, with the
   options «No podrá ser inferior a quince/veinte/veintiséis/treinta días». q44 asks for a date in obras, with
   date options. Under the 2026-10-28 ruling this is not a copy. No other kept case question cites art. 159.3.

## 4. FAILs (appended to `drops.tsv`, batch `calendar-audit-2a`)

- sp-04/q08: check 1. The key, Mon 3 Jan 2028, and option d, Wed 19 Jan 2028 (which needs 6 Jan 2028 inhábil), both
  rest on the unpublished Madrid 2028 calendar. The festivos list no longer closes.
- sp-03/q22: check 1. The key's roll to Mon 7 Feb 2028 needs the unpublished 2028 calendar.
- sp-03/q25: check 1. The key's roll to Mon 16 Jun 2031 needs the unpublished 2031 calendar.
