# m04-l09 quotations under RDL 31/2026 (writer)

Only `explanation` and `source_quote` of `bloque-iv/m04-l09.draft.json` changed. `prompt`, `options` and `correct` are identical to `HEAD` for every question present there (q078-q084 are uncommitted additions, untouched).

## Changed

| id | field | old → new |
|---|---|---|
| q018 | explanation | «…prorrogables por otros ciento ochenta días» → «…prorrogables por otros 180 días» (art. 169.1.a) prints «180» now); sentence now opens «En la redacción vigente desde el 1 de diciembre de 2026, el artículo 169.1.a) fija…» |
| q018 | source_quote | «otros ciento ochenta días» → «otros 180 días» |
| q019 | source_quote | «prorrogables por otros ciento ochenta días cuando…» → «prorrogables por otros 180 días cuando…». Explanation quote («cuando se presuma que durante ellos puede…») is unchanged text, left as is. |
| q022 | explanation | «ciento ochenta días dentro de los cinco años…» → «180 días dentro de los cinco años inmediatamente anteriores al hecho causante»; opens with «En la redacción vigente desde el 1 de diciembre de 2026, el artículo 172.a) exige…» |
| q022 | source_quote | «ciento ochenta días» → «180 días» |
| q039 | source_quote | «se considera situación protegida la reducción de la jornada…» → «la reducción de la jornada de trabajo de, al menos, un 50 por ciento» (art. 190.1 now says «Se considera situación protegida a efectos de la prestación de cuidado de menores de 18 años… la reducción…», so the old string was not a substring) |
| q040 | explanation | «cuando ambos trabajen, o cuando solo haya un progenitor por tratarse de familias monoparentales» → «cuando ambas trabajen, o cuando solo haya una persona progenitora por tratarse de familias monoparentales» |
| q040 | source_quote | «los progenitores, guardadores… acogedores… ambos trabajen… un progenitor» → «las personas progenitoras, guardadoras… acogedoras… ambas trabajen… una persona progenitora» |
| q042 | explanation, source_quote | «hasta que el causante cumpla 26 años» → «hasta que la persona causante cumpla 26 años si antes de alcanzar los 23 años acreditara, además, un grado de discapacidad igual o superior al 65 por ciento» |

No other sentence was changed: every other sentence stays true under the new wording.

## Not changed, with reason

- q041 (art. 190.3): the stem says «hospitalización, tratamiento y cuidado»; art. 190.3 now reads «hospitalización o tratamiento y de cuidado». Stem untouched. Key b (23 años) still right and no second option becomes right. The explanation quote «se mantendrá la prestación económica hasta los 23 años» is in the new text (only the initial capital differs, as in the source: «Se mantendrá…»); left lower-case, the course's mid-sentence convention. The new text adds an exceptional extension beyond 26 (65 % disability or grado III de dependencia with convivencia), which the explanation's «los veintiséis años solo se alcanzan si…» does not contradict for the 26 limit; the verifier may want to judge option d («veintiséis años en todo caso»), which stays wrong.
- q040 stem and options say «ambos trabajen… un progenitor» (old wording); untouched. Key a unchanged and still correct.
- q020, q021, q023, q024, q026, q027, q028, q043, q044, q077-q084: every «» quotation and `source_quote` is an exact substring of the new text. q024 (art. 171 donation) is the same sentence in the new text. q023's quote begins lower-case «en caso de accidente…» against «En caso» in the norm (case-only, pre-existing, left). q077-q084 already carry «En la redacción vigente desde el 1 de diciembre de 2026».
- Kept questions with LGSS arts. 169/171/172/173/190-192 where I found no keyed answer made wrong or second option made right under the new wording: none. No question flagged for the verifier on that ground.
- q006 (cites art. 42.1.a)): mentions «ciento ochenta días» in the explanation's own words, no quotation; untouched.

## Checks

- prompt/options/correct identical to HEAD for all 77 questions present there: OK.
- Every «» quotation in the 7 changed explanations and every `source_quote` of the 22 in-scope kept questions is in the whitespace-normalised new text (case-sensitive), except the q023 and q041 capital-letter cases above.
- `lint_drafts.py bloque-iv m04-l09`: 4 faults (q014, q068, q072, q074), none in the ids I touched and none caused by my edits.
