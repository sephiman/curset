# Question bank ledger — aeat-agentes-hacienda (round R3, stage 2)

Started 2026-11-12. Nothing committed. Plan: `docs/aeat-bank-plan.md`. Working files: `docs/age-verification/aeat/bank/`.
Agents under `CLAUDE.md` «Subagent models and concurrency» (writers Sonnet, verifiers Opus, the derived style check
Sonnet; at most four at once).

## Conventions (standing)

- Derivation, pool, style check, trim, writing, verification and build as `docs/aeat-bank-plan.md` § 4–5.
- Drop, never fix: a FAIL goes to `bank/drops.tsv` (`id tema batch check reason`); replacements are new questions,
  re-verified. Surplus verified questions go to `bank/held.tsv` (reserve), never deleted.
- Doubtful official keys (2024-43, 2022X-69, 2025-20, 2025-24, 2023-80, 2022X-88): no question on their points.
- RDL 29/2026 held: `tools/rdl_held.py` + verifiers; the held list is in «Held questions» below.

## Decisions taken without asking

1. `docs/aeat-bank-plan.md` did not exist; written first (this round).
2. Quotas by the weights of OEP 2022–2025 (462 questions), floor 50, largest remainders: I 800, II 693, III 3,507.
3. Derived candidates come from both the C1 and the C2 banks (R2 derivation.yaml fed the lessons from both); a question in
   both is taken once, from C1. 2,087 candidates; 225 mechanical drops (182 on «options median under 5 words»).
4. Cost rule: only up to 1.3 × quota candidates per tema are style-checked (the pool); the rest are reserve.
5. `tools/rdl_held.py` holds whole articles for LIRPF 24, 67, 68, 95 ter, DA/DT listed, RIRPF 41 bis/69/75/76/93/94,
   TRLRHL 72, LIVA 91, RGAT 39 quater, and paragraph-aware LIRPF 23.2 and 85.1. LIRPF art. 7 (only 7.ñ) and LIVA art. 20
   (only 20.Uno.23.º) are left to writers and verifiers by paragraph.
6. Stem-form classifier: a writer's `stem_form` wins; derived questions are classified by text, `supuesto` only with a
   date or amount and ≥ 45 words.

## Derivation and style check (2026-11-12)

Pool 1,310 checked by Sonnet (two checkers); 75 style drops (mostly checklist 2: stem names no norm by title; item 7
copies). Rulings of the checkers kept: a direct «¿…?» stem naming the norm but not the article passes; a norm named by its
full formal name without number and date passes (PASS rows carrying that note, mainly I.6–I.7).

| Tema | Derived | Mechanical drop | Pooled | Style drop | Kept derived | Reserve (held) | To author |
|---|---|---|---|---|---|---|---|
| I.1 | 230 | 24 | 127 | 5 | 97 | 104 | 0 |
| I.2 | 258 | 35 | 127 | 9 | 97 | 117 | 0 |
| I.3 | 245 | 46 | 184 | 7 | 141 | 55 | 0 |
| I.4 | 229 | 36 | 184 | 13 | 141 | 39 | 0 |
| I.5 | 267 | 23 | 141 | 22 | 103 | 119 | 5 |
| I.6 | 96 | 10 | 86 | 14 | 72 | 0 | 25 |
| I.7 | 422 | 17 | 155 | 33 | 105 | 267 | 14 |
| II.1 | 58 | 22 | 36 | 1 | 35 | 0 | 62 |
| II.2 | 126 | 8 | 118 | 16 | 102 | 0 | 50 |
| II.3 | 66 | 3 | 63 | 27 | 36 | 0 | 116 |
| II.4 | 52 | 0 | 52 | 18 | 34 | 0 | 128 |
| II.5 | 38 | 1 | 37 | 14 | 23 | 0 | 107 |

Reserve = not pooled + over quota (unchecked ones are style-checked only if used). Common part to author: 507.

## Where to resume

1. Common temas: derived kept; delta sheets in `bank/delta/` for I.5–I.7 and II.1–II.5 (507 to author).
2. Writers running: III.4 (p1, p2) and III.12 (p1, p2). Then: III.15, III.8, III.5, III.13, III.19, III.14, rest; then
   the common delta. Verification (Opus) per draft with `tools/verify_batches.py`.

## Decisions (continued)

7. 2024-43 (art. 66 bis.2, ten years): the writer's III.4 q0009, q0114, q0115 rest on that article; dropped by the standing rule
   (the six doubtful keys stay out as facts). «Lo que más cae» line 5 of III.4 therefore stays untested; listed as open.
8. III.12: the writer relabelled difficulty by heuristic in its build script (23/57/20 % against 30/50/20); accepted, the
   label is not a fact. Verification queued behind III.4.

## III.4 (2026-11-12)

Authored 260 (p1 130, p2 130); verified blind (Opus): p1 111 PASS / 19 FAIL (11+7+1; 3 are the doubtful-key drops already
listed), p2 114 / 16. Kept 225 of 260 → quota 346 → **121 still to author** (replacement part, written with the
verifiers' lessons: name the article in every stem including supuestos; never carry an official distractor, check all
exams not only the pack; no option named by position). Near-misses the p1 verifier passed but flagged as same fact/key as
an official question with new distractors (q0055, q0028, q0027, q0003, q0103): kept (the rule fails only a carried-over
distractor). Reports: `bank/verify/m03-l04.p1.v1–v3`, `p2.v1–v3`.

## III.12 part 1 (2026-11-12)

p1 150 verified blind: 120 PASS / 30 FAIL (check 1: 1, 2: 5, 4: 5, 5: 19). Dominant fault: official copies (same fact, key and a
carried-over official distractor) — the writers' main failure class on III.4 and III.12; replacement briefs must say it
first. Reports `bank/verify/m03-l12.p1.v1–v3`. p2 verification running.

## III.12 (2026-11-12)

p2 verified: 133 PASS / 17 FAIL (check 5: 13). III.12 kept 253 of 300 against quota 260 → 7 to author. Official-copy detection:
`check_draft.py` (similarity ≥ 0.80) misses copies below the mark; verifiers compare with all 680 questions (ranked by word
overlap). Reports `bank/verify/m03-l12.p2.v1–v3`.

## III.15 (2026-11-12)

Written 272 (cap: the lesson's cited text, RDL 29/2026 precepts out, has no more distinct facts; quota 260). Held and not asked:
art. 7.ñ), 23.2, 24, 85.1, DA 55.ª and the 2026 imputación example. Supuesto 19 % across both parts (target 10, ±10).
Verification queued behind III.8. III.8: 290 written; verification running.

## III.8 (2026-11-12)

p1 145: 101 PASS / 44 FAIL; p2 145: 117 / 28. Kept 218 of 290 against quota 249 → 31 to author. Dominant faults: 29 supuestos
named neither the BOE title nor the article (checklist 2: «la Ley General Tributaria» with no number/date fails), 29
official copies, 2 wrong keys. Reports `bank/verify/m03-l08.p1.v1–v3`, `p2.v1–v3`.

**Standing lesson for every writer brief from here:** supuestos name the norm by its full BOE title (number and date) and the
article; check all 680 official questions for an angle before writing; no distractor defensible under a neighbouring paragraph.

## III.15 part 1 (2026-11-12)

p1 150: 134 PASS / 16 FAIL (check 4: 11, check 5: 5). Faults: explanations naming people absent from the stem, a false
explanation, a wrong annual figure (interés legal 2026 is 3,25 %, Ley 31/2022 DA 42.ª, not 3 %). Reports
`bank/verify/m03-l15.p1.v1–v3`. p2 verification running.

## III.15 (2026-11-12)

p2 122: 105 PASS / 17 FAIL. III.15 kept 239 of 272 against quota 260 → 21 to author. Verifier ruling on item 10: a question
fails only when the option **median** is under 5 words (as the mechanical drops); about 11 further questions with a single
short option pass. Item 8: a calculation fails only when at least two distractors are absurd. Reports `bank/verify/m03-l15.p2.v1–v3`.

III.13: 250 written (difficulty set by a script rule on key length and supuesto, not by hand: accepted, labels are not facts); verification running.

III.5: 280 written; verification queued behind III.13.

## III.13 part 2 (2026-11-12)

p2 125: 103 PASS / 22 FAIL (12 on «de el» in RGRST stems — a typo class now flagged by `mechanical_style.py` item 8; 5 official
copies). Reports `bank/verify/m03-l13.p2.v1–v3`. p1 verification running.

## III.13 (2026-11-12)

p1 125: 108 PASS / 17 FAIL. III.13 kept 211 of 250 against quota 217 → 6 to author. Faults: bare article-number options (checklist 4),
«de el» typos, two date/holiday keys the stem left undetermined (a stem with a deadline falling on a weekend must state the
domicile/holiday or avoid it). Reports `bank/verify/m03-l13.p1.v1–v3`.

## III.5 part 1 (2026-11-12)

p1 140: 127 PASS / 13 FAIL. Note: key-longest counted with ties is 33 % on III.5 p1 (17 % strict by `check_draft.py`); the
course-level bias guard decides at build. Reports `bank/verify/m03-l05.p1.v1–v3`. p2 verification running.

## Where to resume (usage limit reached, 2026-11-12)

Agents still running when the limit hit (they write files; check them first, do not relaunch blindly): III.5 p2 verifier
(`bank/verify/m03-l05.p2.v*.md`), writers III.19 (`m03-l19.authored-p1/p2.draft.json`) and III.14 (`m03-l14.…`).
1. Collect FAILs into `drops.tsv` (verifiers append themselves). Verify III.19 and III.14 drafts: `tools/verify_batches.py <draft> 1`, Opus, `verify-spec.md`.
2. Kept so far (verified): III.4 225/346, III.8 218/249, III.12 253/260, III.13 211/217, III.15 239/260, III.5 p1 127 (+p2 pending).
3. Not started: writers for III.1–III.3, III.6, III.7, III.9–III.11, III.16–III.18, III.20 (delta sheets ready in `bank/delta/`);
   replacement parts for the short temas (III.4 121, III.8 31, III.15 21, III.12 7, III.13 6); common delta ≈ 507 (I.5 5, I.6 25, I.7 14, II.1 62,
   II.2 50, II.3 116, II.4 128, II.5 107). Re-run `plan_delta.py kept` to refresh the sheets. Replacement briefs lead with the standing lessons
   (III.8 section above).
4. Then: bias guards (`tools/bias_per_tema.py`), build rehearsal with `build_exercises.py --course-dir <scratch copy>`, excerpts
   (`backend/scripts/extract_excerpts.py --course aeat-agentes-hacienda`, blind checks), live build, `docs/age-verification/aeat/tools/close_round.sh`,
   ten random questions per part, the 30-line handoff. Nothing under `content/` has been changed; nothing is committed.

## III.5 (2026-11-12, after the limit)

p2 140: 121 PASS / 19 FAIL; 10 of the fails are art. 104.1 LGT questions dropped as resting on the doubtful key 2025-20 (the verifier read
«that point» as the whole art. 104.1 six-month rule; the exception-only ones q0191, q0203, q0204 are the most open to a narrower
reading: revisit if Juanjo narrows the rule). III.5 kept 248 of 280 against quota 238 (surplus 10: reserve if bias guards need it).
Key-longest with ties 31–34 % on p2 and supuesto 22 % on p2: check at the bias step. Reports `bank/verify/m03-l05.p1.v1–v3`, `p2.v1–v3`.

III.14: 220 written (p1 110, p2 110); verification running.

III.14 p1 110: 95 PASS / 15 FAIL (check 5: 7, check 4: 7, check 2: 1). Reports `bank/verify/m03-l14.p1.v1–v2`. p2 verification running.

## Ruling by Juanjo (2026-11-12): doubtful official keys

Supersedes decision 7 and the standing rule: an official key is never a source of facts, but a point the norm states clearly can be
asked, keyed by the norm text alone; questions on the six flagged keys end their explanation with «En el examen <año> (pregunta N)
la plantilla oficial dio otra respuesta; esta pregunta sigue el texto del artículo.» Reinstated: III.4 q0009, q0114, q0115 and the ten
III.5 art. 104.1 questions (drop lines removed from `drops.tsv`; sentence appended to their explanations by script; ids in
`bank/verify/reinstated.ids`); verified blind (batch tag `reinstated`). Specs updated. The same reading applies to the remaining temas.

## III.14 (2026-11-12)

p2 110: 84 PASS / 26 FAIL. III.14 kept 179 of 220 against quota 195 → 16 to author. Nine p2 questions fail item 11 for printing
«Ministerio/Ministro de Economía y Hacienda» (the LGT/RGRVA text still does) — kept as drops under the m03-l05-q0073 precedent
(drop, never fix); replacements name the current organ with the norm's wording only when the stem dates it. Reports
`bank/verify/m03-l14.p2.v1–v2`.

III.19: 217 written (p1 120, p2 97; capacity). q0109 asks the 2023-80 point with the closing sentence. Verification running.

## Reinstated questions verified (2026-11-12)

13 checked blind: 10 PASS (III.4 q0009, q0114; III.5 q0191, q0193, q0194, q0203, q0204, q0233, q0234, q0267), 3 FAIL on check 5 as
copies of the official question itself, not for the doubtful key (III.4 q0115 ~ 2024-43; III.5 q0192 ~ 2025-20, q0195 ~ 2023-77/2025-68).
Net effect: III.4 kept 227, III.5 kept 258. Notes: III.5 q0191, q0203, q0204 test the same exception (near-duplicates; reserve
candidates if the bank needs to trim); q0234's explanation cites art. 102.5 RGAT where 104.2 LGT / 102.2 RGAT carry the exclusion
(verifier note; explanation not fixed in place — drop-not-fix applies only to FAIL, this is a passed question: decide at build).
Report `bank/verify/reinstated.v1.md`.

III.7: 200 written (p1, p2); a few facts rest on paragraphs the lesson cites without spelling out (art. 135.3, 108.4 LGT; 126.2–3 RGAT): the verifiers' check 3 decides. Verification queued behind III.19.

III.19 p1 120: 110 PASS / 10 FAIL (check 5: 4, check 4: 4, check 2: 2). Reports `bank/verify/m03-l19.p1.v1–v2`. p2 verification running.

III.19 p2 97: 82 PASS / 15 FAIL. III.19 kept 192 of 217 against quota 206 → 14 to author. Faults: distractors true under another paragraph (reventa art. 96.Dos.2.º; Canarias/Ceuta/Melilla; art. 104.Tres), bare article-range options, 4 official copies. Reports `bank/verify/m03-l19.p2.v1–v2`.

III.7 p1 100: 92 PASS / 8 FAIL. Open question for the build check (not a fail): q0030/q0088 count six months from 30 June to 31 December citing art. 30.4 LPAC (lesson's worked example and official 2025-43 do the same; a strict fecha-a-fecha reading gives 30 December, no option offers it). Re-read before the build; drop if the lesson's own example is wrong (theory fix is out of scope here: list it). Reports `bank/verify/m03-l07.p1.v1–v2`. p2 verification running.

III.7 p2 100: 83 PASS / 17 FAIL. III.7 kept 175 of 200 against quota 173 → quota met. Faults: article-number options by meaning (item 4), a bare key as the only option without a clause (item 8 cue), 4 official copies. Reports `bank/verify/m03-l07.p2.v1–v2`.

III.9: 182 written (p1 95, p2 87; capacity; 23 redundant pairs removed). q0115 asks the 2022X-69 point with the closing sentence. Verification running.

III.16: 199 written (p1 100, p2 99; capacity). q0044 touches 2022X-88 with the closing sentence; q0199 options rewritten after the last check_draft run (verifiers re-run it). Verification queued behind III.9.

III.9 p1 95: 84 PASS / 11 FAIL (check 5: 5, check 4: 4, check 2: 1, check 1: 1 — the art. 38.1.a second paragraph point on which official 2023-20 was annulled). Reports `bank/verify/m03-l09.p1.v1–v2`. p2 running; III.16 p1 verification launched; writers III.18, III.17 running.

III.9 p2 87: 68 PASS / 19 FAIL. III.9 kept 152 of 182 against quota 173 → 21 to author. Faults: 7 official copies, key-only-bare-option cue (item 8), a made-up 4 % interés legal with no year, a guarantee question whose stem gave no debt above the 50.000 € limit. Reports `bank/verify/m03-l09.p2.v1–v2`. Open: q0112 names «Dirección General del Tesoro y Política Financiera» (RGR text; current name unconfirmed) — passed; recheck at the build.

III.16 p1 100: 92 PASS / 8 FAIL. Note: this verifier wrote its drops.tsv batch column as a report path (verify/m03-l16.p1.v1.md) instead of the short form; the build reads only the id column. Reports `bank/verify/m03-l16.p1.v1–v2`. p2 running.

III.16 p2 99: 91 PASS / 8 FAIL. III.16 kept 183 of 199 against quota 173 → quota met. Reports `bank/verify/m03-l16.p2.v1–v2`.

III.18: 178 written (p1 95, p2 83; capacity). Verification running.

III.18 p2 83: 70 PASS / 13 FAIL (item 8 cue again in 4; true-under-another-letter distractors in 3; 2 official copies). Key-longest ties-included 35 % over the draft (47 % in p1 batch): decide at the bias step. Reports `bank/verify/m03-l18.p2.v1–v2`. p1 running; writers III.17 and III.20 running.

III.18 p1 95: 81 PASS / 14 FAIL. III.18 kept 151 of 178 against quota 162 → 11 to author. Reports `bank/verify/m03-l18.p1.v1–v2`.

III.17: 107 written (one part). Verification running.

III.17 107: 98 PASS / 9 FAIL. III.17 kept 98 against quota 87 → met. Two fails (q0062, q0081) are IS questions (arts. 26.5 and 31.7 LIS) the verifier tied to the 2024-43 point for lack of the closing sentence; the official question concerned art. 66 bis.2 LGT, so the sentence would not fit: left dropped, quota met; revisit if Juanjo wants them reinstated with a note. q0099 names a «Colegio Oficial de Delineantes de Tarragona» (not clearly fictional) — dropped. Reports `bank/verify/m03-l17.p1.v1–v2`.

III.10: 114 written (capacity). RGAT named in stems by a shortened title (number and date kept) to stay under 60 words. Verification running.

III.20: 135 written (one part). CAU citations resolve to celex-32013r0952-art-N despite the XHTML index. Verification running.

III.10 114: 94 PASS / 20 FAIL (check 5: 15 — including 5 thin supuestos that only restate an official rule with its key and a distractor; verifier's reading: same angle). III.10 kept 94 against quota 108 → 14 to author. Reports `bank/verify/m03-l10.p1.v1–v2`.

III.20 135: 122 PASS / 13 FAIL. III.20 kept 122 against quota 119 → met. All numeric supuestos recomputed correct. Reports `bank/verify/m03-l20.p1.v1–v3`.

III.11: 135 written (one part); q0065, q0066 ask the 2022X-69 point with the closing sentence. Verification running.

## Ruling by Juanjo (2026-11-12): III.7 six-month count and III.9 q0112

**III.9 q0112 (done).** The RGR's wording «Dirección General del Tesoro y Política Financiera» stays. The snapshot's Real Decreto 1009/2023
(`BOE-A-2023-24842`, consolidated 2026-07-29) still lists that organ (arts. on the Secretaría General del Tesoro y Financiación
Internacional, and «s) La Dirección General del Tesoro y Política Financiera»): the name is current, so no «(hoy: …)» is needed and the
question stands. For the post-election round: re-check the name against the structure real decreto in force after 29-11-2026.

**III.7 six-month count (in progress).** Rule: LPAC art. 30.4 (months counted from the day after the event; «El plazo concluirá el mismo
día en que se produjo la notificación, publicación o silencio administrativo en el mes … de vencimiento»), applicable supletoriamente; the
LGT has no counting rule of its own for this plazo (arts. 125.2 and 31.2 LGT only say it runs from the end of the presentation term and that
interest runs «desde la finalización de dicho plazo»). For a term ending 30 June 2025 the six months **conclude on 30 December 2025**, and the
interest runs from 31 December 2025. The lesson's example said «del 1 de julio al 31 de diciembre» (wrong by one day, though its result
«desde el 31 de diciembre» was right); official 2025-43 key B («desde el 31 de diciembre») agrees with the norm, so it is not a disputed key.
Lesson fixed (m03-l07 example lines 90 and 92; LPAC art. 30.4 added to its Normativa; III.7 added to LPAC's `temas`); blind check by an Opus
verifier recomputing the date: `r2-tax/m03-l07/verify-r3-date-1.md`; then `taxprov.py record m03-l07`, goldens, `test_provenance.py`.
Questions resting on the count: q0030 was already dropped (official copy); **q0031** (key «15 de enero de 2026» for a presentation on
15 July, explanation «terminan el 15 de enero … y el interés se devenga desde esa fecha») and **q0088** (explanation «vence el 31 de
diciembre») state the old count: both dropped with reason «lesson count corrected 2026-11-12» and replaced in the III.7 delta.

**III.7 six-month count (done, 2026-11-12).** Blind checks: `r2-tax/m03-l07/verify-r3-date-1.md` (one FAIL: «desde el 31 de diciembre» is not what
art. 31.2 LGT says) and `verify-r3-date-1-recheck-1.md` (both rewritten sentences PASS). The lesson now says the six months conclude on 30 December
2025 (art. 30.4 LPAC) and the interest runs «desde la finalización de ese plazo, al término del 30 de diciembre de 2025»; the «Resultado» line
matches. Provenance record rewritten (`taxprov.py record m03-l07`: 276 verified); `normativa.yaml` LPAC `temas` gained III.7; citations golden
regenerated (4 lines, read: the new art. 30.4 LPAC citation and the changed sentences). `test_provenance.py` and `test_citations.py`: 163 passed.
Official 2025-43 key B («desde el 31 de diciembre») is consistent with interest running from the end of 30 December: not a disputed key. Note
the lesson now cites LPAC; the Normativa of III.7 lists it. Questions: q0030, q0031, q0088 dropped (see above).

III.11 135: 117 PASS / 18 FAIL (check 5: 13 — heavily on the heaviest-asked art. 62 LGT plazos; q0066 is a copy of official 2022X-69 itself, so dropped even under the doubtful-key rule). III.11 kept 117 against quota 119 → 2 to author. Weekend roll-overs q0018, q0019 verified correct. Reports `bank/verify/m03-l11.p1.v1–v3`.

III.2: 102 written (capacity); III.3: 155 written. Both verification running.

## III.2 (2026-11-12)

102: 88 PASS / 14 FAIL (check 5: 11 official copies on the Administración / Delegación Especial and rank questions; check 3: stems naming a norm
without its title: 3). III.2 kept 88 against quota 97 → 9 to author. Reports `bank/verify/m03-l02.p1.v1–v2`.
**Open lesson defect (theory, not fixed here):** `m03-l02` line 74 and its Normativa list (line 250) cite «apartado 3 Resolución de 13-01-2021
(Departamento de Gestión Tributaria)» for the list of Subdirecciones Generales; the list is in apartado segundo.3 (apartado tercero is the
Oficina Nacional de Gestión Tributaria). q0054 (the only question resting on it) is dropped. A citation fix changes sentences (blind check +
provenance record + golden): list for the next theory round, with the citation grammar check for «segundo.3».

III.3 155: 129 PASS / 26 FAIL (item 8 cue: 16 — keys correct by the article but the only option without the restricting clause the three distractors carry; check 5: 9). III.3 kept 129 against quota 141 → 12 to author. Ley 31/2022 figures read in the BOE file: DA 42.ª Uno 3,25 %, Dos 4,0625 % (2026). Reports `bank/verify/m03-l03.p1.v1–v3`.

## Rulings applied (2026-11-12, second set)

1. **III.17 q0062 and q0081 reinstated** (keyed by the norm text; closing sentence appended). Verified blind: both PASS on all five checks
   (art. 26.5 and 31.7 LIS word for word; no other norm supports a distractor). III.17 kept 100 against quota 87.
   Report `bank/verify/reinstated2.v1.md`.
2. **III.2 lesson citation fixed** («apartado segundo.3» of the Resolución de 13-01-2021, lines 74 and 250, text unchanged): blind-checked PASS
   (`r2-tax/m03-l02/verify-r3-cite-1.md`: the list is in apartado segundo.3; form matches the neighbours; golden now `#page=4`, where
   apartado segundo begins — the list itself is on PDF page 5, same convention as every other golden line). Provenance record rewritten;
   `test_provenance.py` and `test_citations.py` rerun.

III.1: 112 written (one part). Verification running.

## III.6 (2026-11-12)

101 written. «Lo que más cae» lines 2 and 3 (art. 75.3.c) and d) RIRPF, pending convalidación) and official 2024-5, 2023-91 are **held** (RDL 29/2026): no question. Listed in «Held questions». Verification running.

III.1 112: 95 PASS / 17 FAIL (item 8 cue: 6; check 5: 7; defensible distractors under other provisions: 4). III.1 kept 95 against quota 97 → 2 to author. Verifier's item-8 ruling: a key fails only when it lacks wording the three distractors share; negation-only differences (q0039, q0045) pass. Reports `bank/verify/m03-l01.p1.v1–v2`. Replacement writers: III.4 (r1, 140) and batch A (III.8, 9, 10, 3, 2, 1) running.

## III.6 verified (2026-11-12)

101: 92 PASS / 9 FAIL (check 5: 5; check 1: 3 — two rounding errors in the art. 40.3 LIS / DA 14.ª LIS computations, one stem missing «derivada de la normativa del tributo»). III.6 kept 92 against quota 87 → met.
**Coordinator ruling (programme scope, checklist 14):** the retention-percentage questions under «pagos a cuenta» (art. 99.1 LIRPF) stay: the 2025 exam asked them
(2025-15, 2025-65, classified III.6 in the ledger); the style guide's exclusion of «retenciones» yields to a 2025 tema phrase covering the point. Older 2021-61 and
2022-89 are «fuera de temario» in the pack but are not sources here. Revisit if Juanjo prefers the strict reading. Reports `bank/verify/m03-l06.p1.v1–v2`.

## III.4 replacements r1 (2026-11-12)

100 written (ids q0261–q0360; asked 140): the lesson's cited text is exhausted (227 kept test nearly every cited paragraph). Supuestos 33 % of the draft
(the computations are the only new angle left): course-level supuesto share to be checked at the bias step. III.4 will end below its quota of 346 by the
drops of this batch plus ≈ 20: **capacity shortfall to be made up elsewhere** (reserve of derived common candidates, `held.tsv`, style-checked on use, or
the common delta), as the C2 plan does for thin temas; recorded in the final table. Verification running.

## Replacements batch A (2026-11-12)

Written: III.8 36, III.9 14, III.10 11, III.3 14, III.2 11, III.1 0 (asked 38/26/18/15/11/5; capacity: kept questions already test almost every cited paragraph; III.1 is
at 95 + nothing needed after the earlier count: **recount: III.1 kept 95 of 97, 2 short**, the writer's reading of «kept 112» included unverified drops — the final table
is recomputed by `plan_delta.py kept` after all verification). III.9 skipped 13.3 and 16.2 RGR (old ministry name). Verification running.

## III.4 r1 verified (2026-11-12)

100: 71 PASS / 29 FAIL (item 8: 10; duplicates of kept or official questions: 14; two stems missing the devengo date). III.4 kept 227 + 71 = 298 against quota 346 →
**48 short, capacity exhausted** (the lesson's cited text is fully tested; art. 4.2 RD 1619/2012 alone has 10+ passing questions). To be made up from the reserve (see the final table).
Reports `bank/verify/m03-l04.r1.v1–v2`.

## Replacements batch A verified (2026-11-12)

86: 39 PASS / 47 FAIL (check 5: 38 — repeats of a kept question's fact and angle, or an official question with a carried distractor; the
tax temas are capacity-saturated). Kept now: III.8 233 (+15), III.9 160 (+8), III.10 98 (+4), III.3 137 (+8), III.2 92 (+4).
Verifier rulings applied: a supuesto with computed dates/amounts is a new angle against a kept rule-only question; a direct question with the
official stem and key verbatim fails even with new distractors; item 8 read literally. Reports `bank/verify/m03-l0{8,9}.r1.v1`, `m03-l10.r1.v1`, `m03-l03.r1.v1`, `m03-l02.r1.v1`.

**Capacity conclusion for Juanjo:** the tax temas' cited text is close to exhausted at the quality bar of the checklist (each lesson yields 150–260 distinct passing
questions). The tax part will end below its quota of 3,507 in III.4 (-48), III.8 (-16), III.9 (-13), III.10 (-10), III.2 (-5), III.3 (-4) and the remaining ones by their
last batch. The 5,000 total is to be reached by using the common-temas reserve (about 1,000 derived, verified-in-origin candidates not yet style-checked: «not pooled» and
«over quota») and the common delta, so parts I–II end above their quotas and part III below its 70 % share; the bank's total, not the tax share, is the requirement (R6.1).

## Ruling by Juanjo (2026-11-12): gap rule (supersedes the «capacity conclusion» plan above)

As in C2: the bank is not filled past each part's share. **The common temas stop at their quota** (surplus verified questions stay in `held.tsv` as reserve; the
derived reserve of 697 stays reserve and is not style-checked further). If the bank ends below 5,000 because the tax lessons run out of facts at this depth, it is
built at what is verified; the gap per tema is recorded in the final table and **variant rounds close it, tax temas first**. **Part III must stay at or above its exam share**
(planned 70.1 % of the bank; 2025 exam 78 %): checked at the final table, trimming common temas below their quotas if needed to hold it. The common delta writers
already running write to the sheets' needs; their surplus beyond quota is trimmed by `plan_delta.py kept` into the reserve.

## Replacements batch B verified (2026-11-12)

72: 49 PASS / 23 FAIL (duplicates of kept questions 11; item 8 cue 7; official copy 1; one more on item 4, one defensible option; III.19 q0222 on the 2025-24 point fails on the
norm too: «un año» flat, the norm allows six months for small businesses; stays dropped). Kept now: III.15 250 (+11), III.14 194 (+15), III.19 203 (+11), III.18 155 (+4), III.12 253 (+0),
III.13 218 (+7), III.11 118 (+1). Reports `bank/verify/m03-l{15,14,19,18,12,13,11}.r1.v1`. The tax temas are now saturated: further tax questions come from variant rounds.

## Common delta A verified (2026-11-12)

II.3 127: 112 PASS / 15 FAIL; II.4 71: 62 PASS / 9 FAIL (check 5: 13 official/kept copies; check 2: 6). 21 cómputos recomputed correct (stems state the no-holiday assumption).
Kept now: II.3 36 + 112 = 148 of 152 (4 short); II.4 34 + 62 = 96 of 162 (66 short, capacity). Reports `bank/verify/m02-l03.v1–v3`, `m02-l04.v1–v2`.

## Common delta B verified (2026-11-12)

264: 176 PASS / 88 FAIL (check 5: ~45, check 3: 20; the common lessons are saturated). Kept: II.5 23 + 53 = 76 of 130; II.1 35 + 58 = 93 of 97; II.2 102 + 26 = 128 of 152; I.6 72 + 25 = 97 of 97;
I.7 105 + 11 = 116 of 119; I.5 103 + 3 = 106 of 108. Reports `bank/verify/m02-l05.v1–v2`, `m02-l01.v1–v2`, `m02-l02.v1`, `m01-l06.v1`, `m01-l07.v1`, `m01-l05.v1`.

## Bias check before the build (2026-11-12)

`tools/bias_per_tema.py` over the 4,760 verified: course-level **longest-is-correct z +1.88** (limit ±3: passes) but **length-edge z +19.35** (key length minus mean distractor length;
limit ±3: the platform test would fail the backend suite). The authored tax questions carry it (per-tema edge z +3 to +9); common derived ones are mostly within ±2.
Remedy as in C1/C2 (`rebalance.py`): hold, never delete, the largest positive-edge questions from the tax temas above quota first, until the course is within ±2.5 and each tax tema within ±2.5.
Cost: questions to reserve; the bank ends smaller than the verified count (recorded in the final table). Tool: `tools/rebalance.py`.

## Bias rebalance applied (2026-11-12)

`tools/rebalance.py --course-bar 2.0 --apply` (exact incremental length-edge statistic): **464 questions moved to reserve** (`held.tsv`, «bias rebalance»): 414 tax questions (the
largest key-over-distractor length edges, worst tema first) and 50 common questions nearest to zero edge, to keep Part III at ≥ 70.2 % of the bank (the exam-share floor).
Result: bank **4,296**; course length-edge z **+1.97** (limit ±3; before: +19.35); longest-is-correct z within ±3; every tax tema's edge z between +0.25 and +0.55.
Common temas keep per-tema edge z between −2.7 and +3.3 (I.6 +2.72, II.3 +3.25 above the C1 ±1.5 tema bar; the course-level test is the gate): noted for the variant rounds,
which should write keys no longer than their distractors. Gap to 5,000: 704 (tax temas first; see the final table).

## Where to resume (paused by Juanjo, PC shutdown, 2026-11-12)

State: all authoring and verification is finished (4,760 verified questions: 986 common derived + 3,430 tax + 344 common delta; every draft's FAILs are in `bank/drops.tsv`).
No agent is running; nothing built, nothing committed; `content/` untouched except the two theory fixes (m03-l07 date example, m03-l02 citation; records and goldens regenerated, tests green).
1. **Bias rebalance (not applied; `held.tsv` has no «bias rebalance» rows).** Course length-edge z is +19.35 (limit ±3), longest z +1.88. A first greedy on the edge alone overshot longest z to −7.8 and was undone.
   `bank/tools/rebalance.py` was just rewritten as a joint greedy (edge + longest, tax temas edge ≤ 2.5, Part III ≥ 70.2 %); its last run printed nothing within 100 s (it is slow, O(held × candidates)):
   run it in the background from `backend/` (`uv run python ../docs/age-verification/aeat/bank/tools/rebalance.py > out.txt`), read `out.txt`; if it errors, the failing spot is `worst_tema()`
   (tema with tema_v 0) — fix and rerun; expect ≈ 400–460 holds and a bank near 4,300. Then `--apply`, rerun `bias_per_tema.py`: course longest and edge |z| must both be ≤ 3 (aim ≤ 2).
2. Final per-tema table (kept, quota, gap, held reserve; Part III share ≥ 70.1 %); record the gap per tema and that variant rounds close it, tax temas first.
3. Rehearsal build on a scratch copy of the course (`build_exercises.py --course-dir <copy>`), then live build; excerpts (`backend/scripts/extract_excerpts.py --course aeat-agentes-hacienda`, blind checks on authored ones),
   cross-reference, `docs/age-verification/aeat/tools/close_round.sh <scratch>`; README note; ten random questions per programme part; the 30-line handoff.

## Final per-tema table (2026-11-13, after the bias rebalance)

Bias: `rebalance.py --course-bar 2.5 --tema-bar 99 --apply`: 672 questions to reserve (joint greedy on length edge and longest-is-correct; Part III share kept ≥ 70.2 %; floor of 50 per tema). Course edge z +2.49, longest z -2.49 (limit ±3). Per-tema tells remain in some temas (common and III.9, III.16, III.17 above the C1 per-tema bar): the platform gate is course-level; the variant rounds write keys no longer than their distractors.
Gap = quota - kept (tax temas first for the variant rounds). Reserve = every `held.tsv` row of the tema (not pooled, over quota, bias rebalance).

| Tema | Quota | Kept | Gap | Reserve (held) |
|---|---|---|---|---|
| I.1 | 97 | 50 | 47 | 151 |
| I.2 | 97 | 60 | 37 | 154 |
| I.3 | 141 | 110 | 31 | 82 |
| I.4 | 141 | 122 | 19 | 58 |
| I.5 | 108 | 81 | 27 | 142 |
| I.6 | 97 | 82 | 15 | 15 |
| I.7 | 119 | 103 | 16 | 279 |
| II.1 | 97 | 74 | 23 | 16 |
| II.2 | 152 | 108 | 44 | 20 |
| II.3 | 152 | 120 | 32 | 28 |
| II.4 | 162 | 85 | 77 | 11 |
| II.5 | 130 | 70 | 60 | 6 |
| III.1 | 97 | 85 | 12 | 10 |
| III.2 | 97 | 82 | 15 | 10 |
| III.3 | 141 | 113 | 28 | 24 |
| III.4 | 346 | 187 | 159 | 111 |
| III.5 | 238 | 202 | 36 | 54 |
| III.6 | 87 | 78 | 9 | 14 |
| III.7 | 173 | 133 | 40 | 40 |
| III.8 | 249 | 205 | 44 | 28 |
| III.9 | 173 | 159 | 14 | 1 |
| III.10 | 108 | 96 | 12 | 2 |
| III.11 | 119 | 114 | 5 | 4 |
| III.12 | 260 | 222 | 38 | 31 |
| III.13 | 217 | 214 | 3 | 4 |
| III.14 | 195 | 183 | 12 | 11 |
| III.15 | 260 | 233 | 27 | 17 |
| III.16 | 173 | 179 | 0 | 4 |
| III.17 | 87 | 86 | 1 | 14 |
| III.18 | 162 | 135 | 27 | 20 |
| III.19 | 206 | 197 | 9 | 6 |
| III.20 | 119 | 120 | 0 | 2 |

Total 4088 of 5,000; gap 912. Parts: I 608, II 457, III 3023 (73.9 % tax).

## Excerpts (2026-11-13)

`extract_excerpts.py --course aeat-agentes-hacienda`: 4,088 questions, 4,059 excerpts, 29 without (26 «heading not found» — the Orden de 2 de junio de 1994, the apartados as bare ordinals «Segundo.», «Quinto.»;
3 on the OECD recommendation). `tools/excerpt_prepare.py`: 777 derived questions inherit (excerpt byte-identical to the origin's), 3,311 to blind-check in 56 batches of 60
(`bank/excerpts/batches`, reports `bank/excerpts/reports`, spec `bank/excerpts/verifier-spec.md`). Batches 8–14 (420 items): yes 347, full-only 57, no 3, none-miss 13 (all the Orden de 1994 ordinal headings; the
fact is in the PDF text), the 3 «no» are Ley 31/1990 art. 103 sub-paragraphs cut by the 200-word limit; 57 full-only are the same limit (the fact sits in «Ver artículo completo»).
**Platform limits (list, never patch; this round does not touch the extractor):** (1) ordinal apartados of the Orden de 2 de junio de 1994 and the Resoluciones are not found as headings; (2) the 200-word excerpt
can end before the cited letter or paragraph (LGT 34.1, 95.1, RD 1619/2012 art. 4.2, 66 bis.2, 103.Tres); (3) a few PDF text-layer artefacts (item 698 «sopor tado»). Workaround for the Orden: none of these
questions gets an excerpt («sin extracto», excerpt-exclusions) or is re-cited to the «fuente: file; «label»» form if the extractor accepts it; decided when all batches are in.
Batches 1–7 (420 items): yes 362, full-only 24, no 21, none-miss 13. Causes: Ley 31/1990 art. 103 sub-apartados not isolated (13 «no», excerpt_full null: the fact cannot be seen);
the Orden de 1994 and a Resolución's «Primero.» headings (13 none-miss); questions resting on several articles whose citation carries one (7 «no»: citation-shape, not extractor); two structural
facts («sección 2.ª va del art. 30 al 38») in no article text; one Cl@ve page sentence; soft-hyphen artefacts in the TFUE/TUE excerpts (flag only). Verifiers use private scratch subfolders from batch 22 on.
Batches 15–21 (420 items): yes 393, full-only 24, no 5, none-miss 0 (the 5 «no»: the key rests on a second unit the single citation does not cover; full-only: lettered lists and long paragraphs cut at 200 words,
RGAT 103/104 letter selection inconsistent).
Batches 22–28 (420 items): yes 398, full-only 11, no 11, none-miss 0 (art. 150 LGT too long for `excerpt_full`: a cut apartado leaves nothing to see, 6 «no»; questions resting on a second unit the citation does not carry, 5 «no»).
Batches 29–35 (420 items): yes 400, full-only 14, no 6, none-miss 0 (the 6 «no»: the key needs other articles than the one cited; one extractor bug: a lettered heading «127.1.c» whose letra c) is cut away).
Batches 36–42 (420 items): yes 403, full-only 14, no 3, none-miss 0 (the 3 «no»: key rests on another article than the cited one; recurring extractor pattern: a question naming a sub-letter or regla still gets an excerpt starting at the first).
Batches 43–49 (420 items): yes 341, full-only 57, no 22, none-miss 0. Batch 49 (LIVA, 35 items) is the main extractor bug: a cited número (7.2.º–7.9.º, 8.Dos.5.º, 9.3.º, 11.Dos.15.º, 13.2.ª, 20.Uno.3.º–22.º) is never
reached; the excerpt starts at the first número of the apartado, and for 14 of them `excerpt_full` is null (20.Uno, 9.3.º): the fact cannot be seen. LIRPF 51 and LIS 29.1 are cut before the fact with no full text (3);
two double-article citations show one article (2); three keys rest on a provision the excerpt only cross-references.

## Ten random questions per part of the programme (seed 20261113, from the built bank)


### Part I (608 questions)

1. **m01-l03-q0127** — ¿Cuál de los siguientes es un departamento ministerial de los que estructura la Administración General del Estado, según el artículo 1 del Real Decreto 829/2023, de 20 de noviembre, por el que se reestructuran los departamentos ministeriales? → «Ministerio de Juventud e Infancia.»
2. **m01-l01-q0027** — Según la Constitución Española de 1978, que fija la mayoría de edad en el capítulo primero del título I, los españoles son mayores de edad: → «A los dieciocho años.»
3. **m01-l03-q0080** — Conforme al artículo 21.1 de la Ley 50/1997, de 27 de noviembre, del Gobierno, el Gobierno cesa, entre otros casos, en los de pérdida de la confianza parlamentaria previstos en: → «La Constitución.»
4. **m01-l05-q0065** — Conforme al artículo 12 de la Ley 19/2013, de 9 de diciembre, de transparencia, acceso a la información pública y buen gobierno, el derecho a acceder a la información pública corresponde a: → «Todas las personas.»
5. **m01-l01-q0059** — ¿Cuál de los siguientes derechos, recogido en la sección 2.ª del capítulo segundo del título I, es también susceptible de recurso de amparo según la Constitución Española de 1978? → «El derecho a la objeción de conciencia.»
6. **m01-l06-q0016** — Según el artículo 53 de la Ley Orgánica 3/2007, de 22 de marzo, para la igualdad efectiva de mujeres y hombres, los tribunales y órganos de selección de la Administración General del Estado responderán a la presencia equilibrada: → «Salvo por razones fundadas y objetivas, debidamente motivadas»
7. **m01-l02-q0089** — Señale la respuesta correcta sobre la independencia del Defensor del Pueblo respecto de mandatos e instrucciones, según el artículo 6.1 de la Ley Orgánica 3/1981, de 6 de abril, del Defensor del Pueblo: → «No recibirá instrucciones de ninguna Autoridad.»
8. **m01-l07-q0040** — Según la disposición final cuarta.1 del texto refundido de la Ley del Estatuto Básico del Empleado Público, ¿cuándo produce efectos en cada Administración la nueva redacción del artículo 16.1 de la Ley 53/1984? → «Con la entrada en vigor del capítulo III del título III, al aprobarse las leyes de Función Pública.»
9. **m01-l03-q0031** — De acuerdo con el artículo 24.2 de la Ley 50/1997, de 27 de noviembre, del Gobierno, los reglamentos se ordenarán según la siguiente jerarquía: → «Primero, las disposiciones aprobadas por Real Decreto del Presidente del Gobierno o acordado en el Consejo de Ministros; después, las aprobadas por Orden Ministerial.»
10. **m01-l02-q0207** — Conforme al artículo 560.1 de la Ley Orgánica 6/1985, de 1 de julio, del Poder Judicial, entre las atribuciones del Consejo General del Poder Judicial figura ejercer: → «La alta inspección de Tribunales.»

### Part II (457 questions)

1. **m02-l01-q0069** — ¿Cómo se agota la delegación legislativa en el Gobierno, una vez otorgada por las Cortes Generales, según el artículo 82.3 de la Constitución Española de 1978? → «Por el uso que de ella haga el Gobierno mediante la publicación de la norma correspondiente.»
2. **m02-l03-q0046** — De acuerdo con el artículo 9.2.c) de la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas, el órgano estatal competente por seguridad pública podrá acudir a la vía jurisdiccional previo informe vinculante de: → «La Secretaría de Estado de Seguridad, que deberá emitirlo en diez días.»
3. **m02-l01-q0071** — Conforme al artículo 83 de la Constitución Española de 1978, las leyes de bases, que otorgan la delegación legislativa al Gobierno, no podrán en ningún caso: → «Autorizar la modificación de la propia ley de bases.»
4. **m02-l03-q0153** — Según el artículo 30.7 de la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas, el calendario de días inhábiles a efectos del cómputo de plazos debe publicarse: → «antes del comienzo de cada año en el diario oficial que corresponda, así como en otros medios que garanticen su conocimiento generalizado.»
5. **m02-l01-q0017** — Según el artículo 82.1 de la Constitución Española de 1978, las Cortes Generales podrán delegar en el Gobierno la potestad de dictar normas con rango de ley: → «Sobre materias determinadas no incluidas en el artículo 81 de la Constitución.»
6. **m02-l04-q0051** — De acuerdo con el artículo 63.1 de la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas, los procedimientos de naturaleza sancionadora se inician: → «siempre de oficio, por acuerdo del órgano competente, y con la fase instructora y la sancionadora a cargo de órganos distintos.»
7. **m02-l02-q0068** — Según el artículo 41.5 de la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas, cuando el interesado o su representante rechace la notificación, se hará constar en el expediente: → «Especificando las circunstancias del intento de notificación y el medio empleado.»
8. **m02-l01-q0061** — Según el artículo 75.2 de la Constitución Española de 1978, el Pleno podrá recabar el debate y votación de cualquier proyecto o proposición de ley que haya sido objeto de delegación en una Comisión Legislativa Permanente: → «En cualquier momento, no obstante la delegación.»
9. **m02-l02-q0065** — ¿En cuál de los siguientes casos se hará la notificación por medio de un anuncio en el «Boletín Oficial del Estado», según la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas? → «Cuando, intentada la notificación, no se hubiese podido practicar.»
10. **m02-l05-q0090** — Hace dos meses, don Ricardo Salas reclamó a la Administración el pago de una prestación concreta que esta debe realizar en virtud de un convenio administrativo, y no ha recibido respuesta ni se ha llegado a ningún acuerdo. Según el artículo 29.1 de la Ley 29/1998, de 13 de julio, reguladora de la Jurisdicción Contencioso-administrativa, ¿puede ya deducir recurso contencioso-administrativo contra la inactividad? → «No todavía, porque han de transcurrir tres meses desde la fecha de la reclamación.»

### Part III (3023 questions)

1. **m03-l14-q0131** — Según el artículo 28.1 del Real Decreto 520/2005, de 13 de mayo, por el que se aprueba el Reglamento general de desarrollo de la Ley 58/2003, de 17 de diciembre, General Tributaria, en materia de revisión en vía administrativa, el Tribunal Económico-Administrativo Central tiene su sede en Madrid y extiende su competencia: → «A todo el territorio nacional.»
2. **m03-l01-q0071** — De acuerdo con el artículo 11 de la Ley Orgánica 8/1980, de 22 de septiembre, de Financiación de las Comunidades Autónomas, los Impuestos Especiales de Fabricación pueden cederse con carácter parcial con el límite máximo del 58 por ciento de cada uno de ellos, excepto: → «El Impuesto sobre la Electricidad y el Impuesto sobre Hidrocarburos.»
3. **m03-l18-q0098** — Promociones Ebro, S.A. terminó un edificio y arrendó un local, sin opción de compra, a una tienda desde el 1 de abril de 2023 hasta el 31 de enero de 2025. El 1 de marzo de 2025 vende el local a un tercero ajeno al arrendamiento. Conforme al artículo 20.Uno.22.º.A) de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido, ¿cómo se califica la entrega? → «Como primera entrega no exenta, porque el arrendamiento duró 22 meses, menos de los dos años exigidos.»
4. **m03-l19-q0065** — Según el artículo 84.Dos de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido, se consideran establecidos en el territorio de aplicación del impuesto los sujetos pasivos que tengan en el mismo la sede de su actividad económica, su domicilio fiscal o: → «un establecimiento permanente que intervenga en la realización de las entregas de bienes y prestaciones de servicios sujetas al impuesto.»
5. **m03-l19-q0094** — ¿Cuál de los siguientes vehículos se presume afecto a la actividad en la proporción del 100 por 100, según el artículo 95.Tres.2.ª de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido? → «Los vehículos mixtos utilizados en el transporte de mercancías.»
6. **m03-l09-q0201** — ¿Cuál de las siguientes deudas tributarias es inaplazable, según el artículo 65.2 de la Ley 58/2003, de 17 de diciembre, General Tributaria? → «La que se exige por medio de efectos timbrados.»
7. **m03-l14-q0160** — En una liquidación a nombre de Marta Ibáñez Sola se advierte un error aritmético en la suma de las bases. Marta reclama ante el tribunal económico-administrativo y pide la suspensión sin aportar garantía. Según el artículo 233.5 de la Ley 58/2003, de 17 de diciembre, General Tributaria, ¿puede suspenderse? → «Sí, se puede suspender la ejecución sin necesidad de aportar garantía.»
8. **m03-l19-q0142** — Vinos Ribeira, S.A. realiza en el año natural 2026 entregas de bienes que originan el derecho a la deducción por 650.000 euros y operaciones exentas que no lo originan por 150.000 euros. No tiene otras operaciones. Según el artículo 104.Dos de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido, ¿cuál es el porcentaje de prorrata general de ese año? → «Un porcentaje de prorrata general del 82 %.»
9. **m03-l13-q0045** — A Inversiones Calderón, S.L. se le impone por una infracción grave una multa de 40.000 euros y se ha aplicado el criterio de comisión repetida de infracciones. Según el artículo 186.1 de la Ley 58/2003, de 17 de diciembre, General Tributaria, ¿durante qué plazo se le puede privar de la posibilidad de obtener subvenciones y ayudas públicas? → «Un año, porque la infracción cometida es grave y la multa es de al menos 30.000 euros.»
10. **m03-l08-q0304** — Se formaliza el lunes 9 de marzo de 2026 un acta de conformidad a Talleres Rojas, S.L. Según el artículo 156.3 de la Ley 58/2003, de 17 de diciembre, General Tributaria, ¿hasta qué fecha puede el órgano competente para liquidar notificar un acuerdo que rectifique errores materiales, sin que se entienda producida la liquidación conforme a la propuesta del acta? → «El jueves 9 de abril de 2026, al cumplirse un mes desde la fecha del acta.»

## Close (2026-11-13)

`docs/age-verification/aeat/tools/close_round.sh` (second full run): goldens regenerated and read (`citations.es.txt`: 4 lines, the III.7 and III.2 theory fixes; `question-keys.tsv` regenerated with `UPDATE_QUESTION_KEYS=1`:
4,088 keys, an identity golden for a new bank, not a moved key); C1, C2, crypto-futures unchanged; Android bundle byte-identical; backend **3,192 passed, 21 skipped**; frontend **752 passed**; `tsc -b` clean.
Bias tests of the platform pass on the built course (edge z +2.49, longest z −2.53; limit ±3).

## Held questions (RDL 29/2026, pending convalidación)

No built question rests on a precept the RDL changed (writers skipped, verifiers failed, `rdl_held.py` held list is empty at build). Facts left untested for that reason: III.6 «Lo que más cae» lines 2 and 3 (art. 75.3.c) and d) RIRPF)
and official items 2024-5, 2023-91; III.15 art. 23.2, 24, 85.1 and DA 55.ª LIRPF and the 2026 imputación example; III.1 TRLRHL arts. 72 and 107.4; LIVA art. 20.Uno.23.º e´) and 91. If Congress convalidates (19-11-2026), they unlock for the variant rounds.

## Handoff (R3 → variant rounds / watch)

1. `aeat-agentes-hacienda`: 4,088 questions, 228 exercises (`quiz`), `lesson_practice: true`, presets and exams NOT built (R6.2 is a later round); course stays published.
2. Quotas 5,000 by OEP 2022–2025 weights; gap 912 (Part I 608/800, II 457/693, III 3,023/3,507); per tema in «Final per-tema table». Part III is 73.9 % of the bank.
3. Variant rounds close the gap, tax temas first (III.4 −159, III.8 −44, III.7 −41, III.12 −38, III.5 −35). The lessons are saturated at this depth: new questions need new angles, not new facts.
4. Rule for new questions (the verifiers' commonest fails, in order): official copies (read all 680, new angle and distractors); a key that is the only option without a clause the others share (item 8);
   distractors true under another paragraph; article numbers as options; stems without BOE title and article; and keys longer than their distractors (see 5).
5. Bias: the authored keys were systematically longer than the distractors (course edge z +19 before the rebalance). 672 questions are in reserve (`held.tsv`, «bias rebalance»). New questions must have keys no longer than the distractor mean.
6. Per-tema tells remain (common temas −3.8…+3.3; III.9, III.16, III.17 high): the platform gate is course-level; the guard to restore per tema is ±1.5.
7. Reserve (`held.tsv`): 697 derived common candidates (552 not style-checked) plus the 672 bias holds; usable in variant rounds after the AEAT style check (Sonnet) and a bias check.
8. Rulings in force: official keys are never a source of facts but a point the norm states clearly can be asked with the closing sentence (six flagged keys); III.7 six-month count is art. 30.4 LPAC (ends 30-12, interest from the end of that day);
   retention percentages under «pagos a cuenta» stay (2025 exam asked them); common temas stop at quota; Part III ≥ 70.1 %.
9. Excerpts: 3,944 of 4,088; 115 withheld by `excerpt-exclusions.yaml`; 26 + 3 without (Orden de 1994 ordinals, OECD page). Extractor limits to fix in a platform round: ordinal apartados; sub-números/letras (LIVA, CAU definitions, RGAT 103/104,
   LIRPF 31, 52, 84); units too long for `excerpt_full` (art. 150 LGT, 20.Uno LIVA); range headings «233.4.b)–e)»; soft-hyphen and header artefacts in EU texts.
10. Theory defects found: none open (the III.2 citation and III.7 example fixed). `m03-l02` and `m03-l07` records and goldens regenerated.
11. Open for the post-election round: III.9 q0112 organ name (RD 1009/2023 still lists the Dirección General del Tesoro y Política Financiera); the two dated copied sentences of m01-l03/l04 (elections of 29-11-2026); RDL 29/2026 on 18–19-11-2026; RDL 31/2026 about 04-12-2026.
12. Verification and provenance: `docs/age-verification/aeat/bank/verify/` (per-batch reports), `drops.tsv` (all FAILs), `held.tsv`, `provenance/<lesson>.md` (one line per built question), `excerpts/` (batches, reports), `derived/`, `style/`.
13. Tools: `derive_candidates.py`, `mechanical_style.py`, `plan_delta.py`, `check_draft.py`, `verify_batches.py`, `rebalance.py`, `final_table.py`, `build_exercises.py`, `excerpt_prepare.py`.
14. Specs: `writer-spec.md`, `verify-spec.md` (with the doubtful-key amendment), `style-check-brief.md`, `excerpts/verifier-spec.md`.
15. Nothing is committed. `.husky/pre-push` (modified) and `backend/raw.json` (untracked) are not from this round: check before committing.
16. Commit scope suggested: content/aeat-agentes-hacienda (exercises, course.yaml, excerpts.json, excerpt-exclusions.yaml, question-keys.tsv, citations golden, two lessons, normativa.yaml), docs/, README.md.

## R5 — first-exercise presets and official sets (2026-11-13)

Nothing committed. Handoff: `docs/aeat-round-5-handoff.md`.

**Rules quoted.** Base 6.2: «un cuestionario de 80 preguntas», cuatro respuestas, «cada contestación errónea se penalizará descontando un cuarto del valor de una respuesta correcta. Las respuestas en blanco no penalizan.»,
«una hora y media», «se calificará de 0 a 10 puntos, siendo necesario obtener un mínimo de 5 puntos para superarlo». Base 6: «La puntuación directa mínima que el Tribunal fije para superar el ejercicio equivaldrá a la calificación mínima necesaria
para superarlo. La puntuación directa máxima obtenible equivaldrá a la calificación máxima del ejercicio.» Criteria 2025: direct score A − E/4; pass only with «el 50 por ciento de la puntuación máxima» at least (criterion 2), which point 3 lets the Tribunal lower (2025: 40 %, 32,00, for the disability quota);
cut-off 41,00 of 80 in 2025 (nota de 9-04-2026); the formula t(d) is the course's `transformed_score`.

**«Primer ejercicio».** 80 questions = 8 (I) + 10 (II) + 62 (III), the part counts of the 2025 paper (ledger table). The 2025 paper prints the parts mixed (Q1 II.1, Q2 III.4, Q3 III.10 …), so no `order: by-source`.
90 min, `pause: never`, −1/4, blank 0, exact fractions, tema label hidden. **Mark:** the Tribunal fixes the raw score that equals 5 after each exam, so the preset pins the only figure the criteria state beforehand,
the 50 % of criterion 2 (the Tribunal may lower it): 40 raw = 5, 80 = 10. 41,00 (2025) appears in the description as information. «Bloque» 40 q / 45 min, «Tema» 10 q / 11 min (1,125 min per question), both described as course estimates.

**Official sets.** 13 presets `conv2025-a` … `conv2020-b`: 1,180 questions in (tipo A and 2022X 636, tipo B 544), raw score only, time as the convocatoria gave it (2025: 90, 2022–2024: 100, 2020–2021: 60 min), −1/4.
Excluded per set, counted in its description: anulada, norma modificada, and the 28 `fuera de temario` (tipo A total). Seven notes («Clave oficial discutida», plus the 2021 errata) show in the solution.
`summary.json` and `verify/` in `docs/age-verification/aeat/official/`.

**Findings.** (1) The OEP 2022 sheets (A and B) are filed as definitive but their header reads «PLANTILLA PROVISIONAL». Confirmed definitive in content (review, 2026-11-13): the Tribunal's
resolution of 9-05-2023 (`2023-04-22_conv2022_res-aprobados-1ej.pdf`, acuerdo primero) records that «vistas las alegaciones presentadas a las plantillas provisionales», in its session
of 4-05-2023, it annulled A-43 and A-80 (B-40 and B-81) and changed A-42 → C, A-46 → A, A-47 → C, B-49 → A, B-50 → C, and approved the cut-off «en base a las plantillas de respuestas
definitivas». Both files were created on 4-05-2023 and carry every one of those changes (A: 42-C, 43-ANULADA, 46-A, 47-C, 82-ANULADA; B: 40-ANULADA, 49-A, 50-C, 81-ANULADA); A-82 is
the question the resolution calls «80» (B-81 = A-82, ledger OEP 2022). The header is a leftover; the key is the definitive one.
(2) The papers have their own typos (kept as printed: «seguramiento» in 2022 A, «otro1.000» in 2020 B, «resoluciónes» in 2022X) and tipo A/B differ in a few commas and typos; each paper is stored as printed.
(3) The parsed text left a space after a compound's hyphen at line ends (24 cases): the blind check found it, the generator now closes it and a test rejects it.
(4) Platform: the sitting hid the tema by preset-id prefixes; it now follows `pause: never`.

**Blind check.** Two opus verifiers read every included question of the 13 sets against the questionnaire and sheet PDFs (stems, options, order, keys, notes, exclusions, counts). The first (2025–2023) found only the hyphen defect;
the second (2022–2020) re-ran on the corrected files: 0 FAIL, 0 UNREAD. Review re-check (2026-11-13): two fresh opus verifiers re-read the 2025–2023 sets on the
corrected files (534 variants, wording and key against the PDFs): 0 FAIL, 0 UNREAD; their reports replace the pre-fix ones in `verify/`.

**Close.** `close_round.sh`: goldens unchanged, C1, C2, crypto-futures untouched, Android bundle byte-identical; backend 3,377 passed, 34 skipped; frontend 753 passed; `tsc -b` clean; e2e 110 passed.
