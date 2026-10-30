# Cases ledger — age-administrativo-c1, round R4 (supuestos prácticos)

Started 2026-10-28. Nothing committed. Plan, slots and specs: `docs/age-verification/cases/` (`plan.md`,
`slots.tsv`, `spec.md`, `verify-spec.md`); drafts `sp-NN.draft.json`; verification reports `sp-NN.verify-<k>.md`;
drops `drops.tsv`. Writers sonnet, verifiers opus, at most four agents at once (`CLAUDE.md`).

## Progress (append-only)

- sp-01 written: La autorización de vertido, 20 questions, 14 computations
- sp-03 written: Formación en línea del INAP, 20 questions, 11 computations (revised after the sp-01 lessons)
- sp-01 verified (verify-1): 13 PASS, 7 FAIL (official 2, style 4, citation 1) → more than five drops: case rewritten; first version kept as sp-01.v1.draft.json, its ids q01–q20 retired; the rewrite uses q21–q40
- sp-04 written: Encuestas obligatorias del INE, 20 questions, 13 computations
- sp-02 written: La Subdelegación de Valladolid, 20 questions, 17 computations
- sp-04 verified (verify-1): 15 PASS, 5 FAIL (dependence 4, official 1); 3 scenario faults (festivos sentence, comma after year, date without weekday); replacements q21–q25 pending. Slots: V.3 2 → V.3 1 + V.5 1 (writer)
- sp-04 replacements q21–q25 written
- sp-03 verified (verify-1): 12 PASS, 8 FAIL (official 3, style/dependence 5); scenario festivos sentence untrue → more than five drops: case rewritten; first version kept as sp-03.v1.draft.json, ids q01–q20 retired, rewrite uses q21–q40. Spec gains «Self-test before hand-back»
- sp-02 verified (verify-1): 7 PASS, 13 FAIL (unique 1, citation 3, style/dependence 5, official 4); scenario fault (suegra's locality missing, changes q11) → case rewritten; first version sp-02.v1.draft.json, ids q01–q20 retired, rewrite uses q21–q40
- sp-05 written: La reproducción de un manuscrito, 20 questions, 13 computations
- sp-01 rewritten: La autorización de vertido, ids q21–q40, 20 questions, 13 computations, 0 check flags, festivos sentence checked by script
- sp-05 verified (verify-1): 8 PASS, 12 FAIL (key 1, style/dependence 7, official 4); 2 scenario faults (the Directora's act ends the vía administrativa under art. 9.4 RD 640/2016, so reposición, not alzada; festivos sentence misses 12 Oct) → case to be rewritten; first version sp-05.v1.draft.json. The verifier fetched RD 640/2016 from the BOE (not in sources/). New dependence reading: a question whose distractors are wrong whatever the scenario says fails
- sp-03 rewritten: Formación en línea del INAP, ids q21–q40, 20 questions, 12 computations, 0 real check flags (6 festivos named on purpose), festivos sentence checked by script, anchors zero misses
- **Rulings of 2026-10-28 (user).** Dependence as style guide § 11 (fail only a question using no case fact, or one contradicting the scenario); copies judged on stem and options, not on the kind of computation; a case with more than five drops gets replacements in batches, not a rewrite. Every dropped question of sp-01…sp-05 is re-read under these rules; one that passes is restored (`restored.tsv`; `drops.tsv` stays append-only). Base versions from here: sp-01 the rewrite (q21–q40; v1 ids stay retired), sp-02 and sp-05 back to their first version (rewrite cancelled), sp-03 the rewrite (q21–q40; v1 retired; first verification under the new rules), sp-04 as is (replacements q21–q25 apply only to drops that stay dropped).
- reread-1 sp-04/sp-05: sp-04 restored q03, q06, q11, q17 (their replacements q21, q23, q24, q25 fall away); q05 stays dropped (alta médica no longer in the scenario), q22 to verify. sp-05 restored q06, q09, q10, q11, q12, q19, q20; still dropped q01, q17 (copy), q04 (key: reposición), q13, q18 (style) → 5 replacements + scenario fixes pending
- reread-1 sp-01/sp-02: sp-01 restored q27, q29, q32, q33, q34, q37, q38, q39, q40; still dropped q22 (copy, conv2022·S2·16), q36 (unique) → 2 replacements + scenario fixes (Don Mateo's status; two sentences) pending. sp-02 restored q04, q05, q06, q10, q14, q15, q17, q19; still dropped q01 (explanation), q02, q09, q16 (citation), q11 (unique) → 5 replacements + scenario fix (suegra's locality) pending
- sp-06 written: Una extracción ilegal de agua, 20 questions, 13 computations
- sp-07 written: El mantenimiento del sistema informático de la MUFACE, 20 questions, 12 computations (11 dates, 1 amount); 0 real check flags (5 festivo flags are the intended 1 and 9 November), anchors zero misses, festivos sentence checked by script


## Paused (2026-10-28, user) — where to resume

- Running when paused (left to finish their current case): writers sp-06, sp-07; verifier sp-03 rewrite (`sp-03.verify-2.md`) + sp-04 q22 (`sp-04.verify-2.md`). Check their files and the Progress lines above.
- Next: one writer for the replacements — sp-01 q41–q42 (+ scenario: Don Mateo's status, two sentences), sp-02 q21–q25 (+ scenario: the suegra's locality), sp-05 q21–q25 (+ scenario: reposición, festivos sentence); then verify them. Then sp-06/sp-07 verification and sp-08…sp-20.
- Not started: build (`tools/build_cases.py`), excerpts, pairs, PDF, goldens, suites. `backend/tests/test_quiz_answer_bias.py` already has the case-pool guard; it fails until cases are built.
- sp-03 rewrite verified (verify-2): 20/20 PASS, 12 computations; scenario fault: «Doña Irene Vallejo Castro» shares name and surname with a known writer → rename in the scenario (no answer changes). sp-04 q22 PASS (verify-2): sp-04 complete, 20 kept, 12 computations
- sp-06 written (paused session): to verify next; writer asks the verifier to check Sevilla local festivos in the Oct–Nov 2027 windows, q03's conditional stem (sectoral prescription), q08 (DA 15.ª LCSP), q15 (art. 28.2 TRLCPE without letter)
- sp-07 written (paused session): to verify next. Writer's claims for the verifier to test: RDL 4/2000 art. 3.2.b read as excluding MUFACE's own staff from mutualismo (so the mutualistas are ministry staff); RD 577/1997 DA 1.ª and art. 6.3 on which acts end the vía administrativa (not cited by the lesson; no alzada/reposición asked). Lesson issue for the theory ledger: m05-l02's table and its «Lo que más cae» line disagree on who authorises a generación de crédito (ministro vs Director); no case question asks it.
- All agents finished; nothing running.

## Resumed (2026-10-29)

- sp-07 verified (verify-1): 19 PASS, 1 FAIL (q10, copy of conv2024_X·S2·18); scenario OK. Coordinator drop sp-07/q07: same dates and option set as sp-05/q07. 2 replacements pending (q21 for q07, q22 for q10). Checker gains a cross-case duplicate check
- sp-06 verified (verify-1): 14 PASS, 6 FAIL (key 2: q02 leve fine above the TRLA ceiling, q08 DA 15.ª start undetermined; unique 1: q19 subconcepto 226.03; copy 3: q07, q11, q20); 4 scenario faults (12.000 € fine for a leve infraction vs art. 117.1 TRLA's 10.000 €; adjudicación notification without publication fact; obligations above the credit; «la» without antecedent) → 6 replacements + scenario fixes pending
- sp-01 replacements written (2026-10-29): q41 (replaces q22; art. 121.2 LPAC, date) and q42 (replaces q36; art. 98.2 TREBEP); scenario: Don Mateo funcionario de carrera, the comma splice and the hanging clause fixed (the audiencia sentences, which only supported q22, removed); 13 computations kept, 0 check flags, anchors zero misses. To verify.
- sp-02 replacements written: q21–q25 (replacing q01, q02, q09, q11, q16: art. 16.2 RD 951/2005, art. 32.1 LPAC, art. 198.4 LCSP, art. 48.a TREBEP, art. 10.3 RD 462/2002); scenario: the suegra dies in Zamora and Doña Elena lives in Valladolid, Easter weekdays added, two trims; 17 computations, anchors zero misses; flags left only in kept explanations (q03, q05, q15) and the named Viernes Santo. To verify.
- sp-05 replacements written: q21–q25 (replacing q01, q04, q13, q17, q18: art. 123.2 and 124.2 LPAC, art. 16.4 Ley 53/1984, anexo IV art. 21 Resolución de 20-01-2014, art. 2.3 RD 725/1989); scenario: reposición against the Directora's act that ends the vía administrativa, 12 Oct named as festivo, Don Raimundo sentence and «Hoy no tiene respuesta» removed; 13 computations, anchors zero misses. To verify.
- sp-03: «Doña Irene Vallejo Castro» renamed «Doña Noelia Barrantes Cifuentes» (scenario, q25 stem, explanation, depends_on); no other change.
- sp-08 written: Las ayudas a la contratación del SEPE, 20 questions, 13 computations (9 dates, 3 euro amounts, 1 weeks count); 0 real check flags, no DUPLICATE, anchors zero misses; no alzada/reposición question (SEPE statute not checked)
- sp-06 replacements written (2026-10-29): q21–q26 (replacing q02, q07, q08, q11, q19, q20: art. 85.3 LPAC, art. 215.4 LCSP, art. 50.1 LCSP, art. 67.3 TREBEP, anexo IV art. 20 Resolución 20-01-2014, art. 6.2 RD 725/1989); scenario: fine 9.000 euros, adjudicación published and notified Wed 13 Oct, obligations «que debe reconocer», «recibe la petición», three unused sentences removed; 12 computations, anchors zero misses, no DUPLICATE. To verify.
- sp-07 replacements written: q21 (replaces q07; art. 158.2 LCSP, date) and q22 (replaces q10; art. 89.2 TREBEP); scenario unchanged; 12 computations, anchors zero misses, no DUPLICATE. To verify.
- Replacements verified (sp-01.verify-3, sp-02.verify-2, sp-05.verify-2): 11/12 PASS; scenarios OK, no kept question broken. sp-01 and sp-02 complete (20). sp-05/q24 FAIL (Resolución named by a short form) → 1 replacement pending. Coordinator, before verification: sp-06/q25 stem given the Resolución's full BOE title (same fault)
- sp-08 verified (verify-1): 17 PASS, 3 FAIL (q06 key: explanation miscounts over the unnamed 1 Nov; q07 unique: procedure type not stated; q19 copy of conv2024_X·P1·39, caja fija 7 %); scenario fault: festivos sentence misses 1 Nov → 3 replacements + scenario fix pending
- Replacements verified (sp-06.verify-2, sp-07.verify-2): sp-06 6/6 PASS, scenario OK, no kept question broken → sp-06 complete (20). sp-07 q22 PASS, q21 FAIL (explanation counts art. 158.1's fifteen days as hábiles; DA 12.ª makes them naturales) → 1 replacement pending
- sp-10 written: Las subvenciones del FEGA, 20 questions, 14 computations (13 dates, 1 amount); 0 real check flags (festivo flags are the named Madrid ones), no DUPLICATE, anchors zero misses, festivos checked by script; FEGA statute (alzada before the Ministro, not reposición) read in the BOE; no IOC question
- sp-09 written: El monte de Valsaín, 20 questions, 14 computations (8 dates, 6 amounts); 0 real check flags (3 festivo flags are the named Viernes Santo and 8 December 2028), no DUPLICATE, anchors zero misses; no alzada/reposición question (OAPN statute not checked), no IOC rule
- sp-05 replacement q26 written (replaces q24; same question, stem now carries the Resolución's full BOE title); sp-07 q23 written (replaces q21; art. 153.3 LCSP requerimiento to formalize, five días naturales, Tue 9 Mar 2027); sp-08 scenario fixed (1 Nov 2027 named; every kept day window rechecked by script, no key changes) and q21–q23 written (replacing q06, q07, q19: art. 81.2 LPAC date, art. 213.3 LCSP, art. 9.1 RD 725/1989 date); 0 DUPLICATE, anchors zero misses. To verify.
- sp-10 verified (verify-1): 16 PASS, 4 FAIL (q03 unique: Juzgado Central, Abogado alone; q04 key: no alzada against a reintegro, art. 42.5 LGS; q07 key: art. 158.1 days as hábiles in the explanation; q18 style: RD 2188/1995 by number) ; 2 scenario faults (alzada against reintegros; Audiencia Nacional instead of a Juzgado Central) → 4 replacements + scenario fixes pending. Spec gains «Repeat faults»
- sp-09 verified (verify-1): 16 PASS, 4 FAIL (q03, q18 key: Madrid 19 Mar and 16 Aug 2027 not counted, q18 also cites art. 56.1 for art. 53's plazo; q05, q19 copy); scenario fault: festivos sentence misses 19 Mar and 16 Aug → 4 replacements + scenario fix pending. plan.md gains the verified Madrid 2027 calendar; case_check flags those days
- Replacements verified (sp-05.verify-3, sp-07.verify-3, sp-08.verify-2): 5/5 PASS, sp-08 scenario OK after the edit, no kept question broken → sp-05, sp-07, sp-08 complete (20 each), subject to calendar-audit-1
- sp-11 written: El Encuentro Joven del Injuve, 20 questions, 13 computations (8 dates, 5 amounts); 0 check flags, no DUPLICATE, anchors zero misses; festivos (incl. 19 Mar, 16 Aug, 9 Nov) checked by script; no alzada/reposición/IOC question (Injuve statute not checked)
- calendar-audit-1 (82 kept date questions, sp-01…08, sp-10): every key holds; 4 explanations miscount a distractor over 19 Mar / 16 Aug 2027 → dropped sp-01/q23, sp-02/q23, sp-07/q03, sp-10/q12 (replacements pending). Scenario sentences all true. Open: sp-01/q30 distractor «20 de marzo de 2028» depends on Madrid's 2028 calendar (not yet published)
- sp-12 written: La campaña publicitaria de TURESPAÑA, 20 questions, 15 computations (10 dates, 5 amounts); 0 real check flags (the 2 flags are the named Mon 16 Aug 2027), no DUPLICATE, anchors zero misses, festivos checked by script over every window with the verified Madrid list; no alzada/reposición question (TURESPAÑA statute not checked)
- sp-11 verified (verify-1): 16 PASS, 4 FAIL (all key: q04, q05 ignore the declared urgency, art. 33.1 LPAC; q14, q15 explanation miscounts); 2 scenario faults (urgency halves the procedure's plazos; a joint request where one desists leaves the other in, art. 94.2) → 4 replacements + scenario fixes pending; the minor Álvaro needs surnames
- R4 calendar/verify replacements (2026-10-29): sp-01 q43 (for q23), sp-02 q26 (for q23), sp-07 q24 (for q03): same questions, distractor counts fixed over 19 Mar / 16 Aug 2027; computations kept 13, 17, 12. sp-09: scenario festivos sentence names 19 Mar and 16 Aug 2027 (convenio sentence trimmed), q21–q24 (for q03, q05, q18, q19), 14 computations. sp-10: scenario (alzada against a denied ayuda, reintegro thread now reposición, Audiencia Nacional removed), q21 (q12), q22–q25 (q03, q04, q07, q18), 14 computations. Checker: 0 DUPLICATE, anchors zero misses. To verify.
- Replacements written (repl-4): sp-01 q43, sp-02 q26, sp-07 q24, sp-09 q21–q24 (+ festivos sentence), sp-10 q21–q25 (+ scenario: alzada now against a denied ayuda, not a reintegro; no court named). Seven of them (sp-01 q43, sp-02 q26, sp-07 q24, sp-09 q21, sp-10 q21, q24, q25) are the dropped question with the wrong count or title corrected, under a new id; they go through the same blind check
- sp-12 verified (verify-1): 16 PASS, 4 FAIL (q12 key: explanation miscounts the 31 Aug distractor; q13 copy of conv2025_A·S2·16; q16 repeats sp-02/q18 with new figures — dropped under «No reuse across cases», the option-set check did not catch it; q17 citation: art. 10.3 RD 462/2002, not 12.3); scenario OK → 4 replacements pending
- sp-11 replacements written (2026-10-29): q21–q24 (replacing q04, q05, q14, q15: art. 88.1 and 94.4 LPAC dates, art. 97 TREBEP, art. 12.2 RD 462/2002 with 19 h 30 min); scenario: urgency moved to Doña Elena's request, Mirador sole applicant, Álvaro Prieto Zamora; 13 computations, 0 check flags, anchors zero misses. To verify.
- sp-13 written: Las encuestas del CIS, 20 questions, 11 computations (8 dates, 3 amounts); 0 real check flags (the named 12 October), no DUPLICATE, anchors zero misses; festivos (12 Oct, 16 Aug, 19 Mar) checked by script; organismo autónomo: no IOC rule, no alzada/reposición question
- sp-11 replacements verified (verify-2): 4/4 PASS, scenario OK, no kept question broken → sp-11 complete (20). Note: «la petición» declared urgent is ambiguous between Doña Elena's two requests (no question depends on it)
- sp-12 replacements written (2026-10-29): q21–q24 (replacing q12, q13, q16, q17: art. 19 RD 365/1995, art. 48.1 RD 364/1995 cese date, art. 10.2 and 10.3 RD 462/2002); scenario unchanged, festivos line adjusted; 14 computations, anchors zero misses, no DUPLICATE. To verify.
- repl-4 verified (sp-01.verify-4, sp-02.verify-3, sp-07.verify-4, sp-09.verify-2, sp-10.verify-2): 11/12 PASS; scenarios OK; FEGA premise confirmed (RD 202/2024 art. 12: Presidencia's acts open to alzada before the Ministro). sp-01, sp-02, sp-07, sp-09 complete (20). sp-10/q22 FAIL (copy of conv2022·S2·13) → 1 replacement (III.3) pending. Scenario wording to tighten (no verdict): sp-01 «solo son inhábiles sábados y domingos» and sp-07 «Ningún otro festivo…» should be limited to the plazos the questions count (a distractor's explanation skips 19 Mar)
- sp-12 replacements verified (verify-2): q21, q22 PASS; q23 FAIL (RD 462/2002 by number and date though the title fits), q24 FAIL (repeats sp-02/q25 with two shared distractors) → 2 replacements pending. Checker: same citation + ≥2 identical options now flags DUPLICATE
- sp-13 verified (verify-1): 19 PASS, 1 FAIL (q04 copy of conv2025_A·S2·13, convenio duration); scenario facts OK; 2 language faults (first sentence without verb; «ella la presenta» without antecedent) → 1 replacement + 2 sentence fixes pending. Verifier notes, no verdict: q14's explanation wording «suma los veinte días hábiles» is loose; q17's generación premise (ingresos no previstos) unstated
- sp-14 written: Los reactivos urgentes del ISCIII, 20 questions, 12 computations (9 dates, 3 amounts); 0 real check flags (the festivo flags are the named Madrid days), no DUPLICATE, anchors zero misses; slot V.3 → V.5 (q20); ISCIII stated as organismo autónomo (RD 375/2001); no IOC, alzada or contencioso question
- repl-7 (2026-10-29): sp-10 q26 (for q22: art. 124.2 LPAC, date Mon 25 Oct 2027; festivos line names q26), 14 date + 1 amount computations kept; sp-12 q25 (for q23: art. 23.Uno.D Ley 31/2022, 1.420,00 euros) and q26 (for q24: art. 34.a) Ley 33/1987, liquidación por días), 14 computations; sp-13 q21 (for q04: art. 51.2 LRJSP) + scenario (first sentence has a verb; «la» has its antecedent «documentación»; borrador sentence removed), 11 computations; sp-01 and sp-07 scenario festivo sentences limited to the plazos the questions count (547 and 549 words). Checker: no DUPLICATE, anchors zero misses. To verify.
- sp-15 written (2026-10-29): La Jefatura de Tráfico de Toledo, 20 questions, 13 computations (9 dates, 4 amounts); scenario 541 words; anchors zero misses, no DUPLICATE; one checker flag, the date inside the Resolución 20-01-2014 title (q18); Toledo calendar not sourced, every window kept between 11 Jan and 18 Mar 2027; OA status of the Jefatura Central de Tráfico stated from memory (statute unchecked), no alzada or sanction content. To verify.
- sp-14 verified (verify-1): 14 PASS, 6 FAIL (q05, q08 citation; q06, q17 copy of official; q18 repeats sp-05/q16, q19 repeats sp-03/q39) → 6 replacements pending; scenario OK. Coordinator drop sp-10/q10 (same figures as sp-06/q18) → 1 more sp-10 replacement. Checker: amount-based duplicate check (figures shared by all options ignored, ≥3 shared). Spec: art. 47.2 plurianual saturated
- repl-7 verified: sp-10/q26 PASS (sp-10 still owes 1 for the coordinator drop of q10); sp-13/q21 PASS, scenario OK → sp-13 complete (20); sp-01, sp-07 scenario wording OK, all kept hold; sp-12 q25 FAIL (key: December pay is proportional after a return in July), q26 FAIL (stem's toma de posesión contradicts kept q14) → 2 replacements still owed (V slots). Open (no verdict): sp-01/q30 distractor depends on the unpublished Madrid 2028 calendar
- sp-15 verified (verify-1): 19 PASS, 1 FAIL (q06 unique: art. 83.2's twenty-day floor vs urgency halving); scenario OK (Castilla-La Mancha Decreto 34/2026; Toledo 2027 local days not yet published — San Ildefonso falls on Saturday 23 Jan; re-check q02, q06, q14 if Toledo moves it) → 1 replacement owed. Notes: q19 is another art. 47.2 limit (written before the saturation note); q17's «236 km ida y vuelta» Toledo–Albacete is about half the real road distance (no answer change)
- sp-17 written (2026-10-29): La reforma de un archivo, 20 questions, 12 computations (10 dates, 2 amounts); scenario 520 words, Murcia calendar (BORM regional days; local days unsourced, windows kept 5–30 Apr 2027); slot V.3 2 → V.3 1 + V.5 1; anchors zero misses, no DUPLICATE, one checker flag (date in the IOC title, q17). To verify.
- sp-16 written: La caída en el teatro del INAEM, 20 questions, 13 computations (7 dates, 6 amounts); slot III.3 4 -> III.3 3 + III.6 2; 0 real check flags (festivo and norm-date flags only), no DUPLICATE, anchors zero misses; INAEM stated as organismo autónomo of Cultura (president is the Minister, so no alzada/reposición or competence question); no performance contract
- repl-8 sp-10 (2026-10-29): q27 (for q10: art. 60.3 LGP anticipo de tesorería, not art. 47.2); scenario: the 90.000 euros plurianual sentence replaced by the anticipo sentence; 14 computations, anchors zero misses, no DUPLICATE. To verify.
- repl-8 sp-12 (2026-10-29): q27 (for q25: art. 33.a) Ley 33/1987, December paga reduced by 149 days, 1.341,00 euros) and q28 (for q26: art. 34.a) Ley 33/1987, July liquidated por días, toma de posesión Mon 5 Jul 2027 = q14's last day); scenario unchanged; 14 computations, anchors zero misses, no DUPLICATE. To verify.
- sp-17 verified (verify-1): 16 PASS, 4 FAIL (q06 explanation: art. 159.3 gives obras twenty days; q07 repeats sp-03/q29; q12 unique: vacaciones are not «permisos o licencias» under art. 48.3 RD 364/1995; q18 repeats sp-07/q20); scenario fault: body's current name is «Delegación Especial de Economía y Hacienda en Murcia» → 4 replacements + name fix owed. Murcia 2027 calendar per BORM resolution of 27-07-2026 (city: 30 Mar, 14 Sep)
- Tool: tools/kept_index.py writes kept-index.tsv (case, id, tema, citation, key, stem) so writers check what is taken; spec «What is taken»
- sp-16 verified (verify-1): 17 PASS, 3 FAIL (q10, q19 official copies; q15 explanation miscount) → 3 replacements owed; scenario OK. Spec: two more official shapes listed as taken
- repl-8 sp-14 (2026-10-29): q21–q26 (for q05, q06, q08, q17, q18, q19: art. 40.2 LPAC date, art. 156.2–3 LCSP, art. 122.1 LCSP, art. 46, 47.1 and 47 bis LGP; none art. 47.2); scenario: the access/paper sentences and the 400.000 euros sentence removed; 11 computations, anchors zero misses, no DUPLICATE. sp-15 q21 (for q06: art. 33.2 LPAC, no recurso against the urgencia acuerdo) + scenario sentence; 12 computations. To verify.
- repl-8 verified (sp-10.verify-4, sp-12.verify-4, sp-14.verify-2, sp-15.verify-2): 9/10 PASS; scenarios OK, no kept question broken → sp-10, sp-12, sp-15 complete (20). sp-14/q24 FAIL (a 150.000 € credit contradicts the case's adjudication at 174.240 €) → 1 replacement owed (V.2, not art. 46 over the adjudicated contract)
- sp-18 written (2026-10-29): Coedición y archivo en el CEPC, 20 questions, 10 computations (7 dates, 3 amounts); scenario 550 words, Madrid 2027 calendar checked by script, no 2028 date; 0 check flags, anchors zero misses, no DUPLICATE; CEPC stated as organismo autónomo (statute unchecked), no alzada/reposición/IOC question; shared citations: art. 80.2 LPAC (sp-03 q23, other dates) and art. 51.2 LRJSP (sp-13 q21, letter a). To verify.
- repl-9 (2026-10-29): sp-16 q21–q23 (for q10, q15, q19: art. 79.6 LGP date Wed 10 Nov 2027 with Almudena, art. 54.1 RD 364/1995 unfavorable informe, art. 47.6 LGP tramitación anticipada); scenario: Don Eusebio's informe now desfavorable, 9 Nov 2027 named; 13 computations. sp-17 q21–q24 (for q06, q07, q12, q18: q06 corrected explanation, art. 159.6.c) LCSP, q12 as a permiso por asuntos particulares, art. 6.1 RD 725/1989); scenario: body name «Delegación Especial de Economía y Hacienda en Murcia», permiso sentence; 12 computations. Checker: no DUPLICATE, anchors zero misses. To verify.
- repl-9 verified (sp-16.verify-2, sp-17.verify-2): 7/7 PASS, scenarios OK, no kept question broken → sp-16, sp-17 complete (20). Coordinator ruling on the verifier's two check-3 notes: art. 30.5 LPAC as the default rollover (sp-16/q21) and an organ's current name from RD 829/2023 (sp-16/q22) are not rules the key rests on beyond the citation; both stand, as in sp-09/q04
- sp-18 verified (verify-1): 13 PASS, 7 FAIL (q01 unique/citation: «seis meses» without a cómputo rule; q10 citation: forced retirement is art. 67.4 TREBEP; q12, q20 official copies; q13 key: seniority unstated; q15 key: widow's age and income unstated; q18 unique: committed sum unclear); 3 scenario faults (Doña Aurora's entry into the Cuerpo; whether the formalised contract is inside the committed 26.500 €; a licitación opened with credit below the presupuesto base, art. 116.3 LCSP) → 7 replacements + scenario fixes owed (in batches per the 2026-10-28 ruling). Notes: IGC rise of 4,5 % implausible (q09 passes on the scenario's figure); Ley 16/1985 sets no access plazo (scenario fixes three months)
- repl-9 sp-14 (2026-10-29): q27 (for q24: art. 56.7 LGP, suplemento of an organismo autónomo for an obligation of a previous year with no credit annulled goes to the Cortes by proyecto de ley; no figure, nothing contradicts the 174.240-euro adjudication; not art. 47.2); 11 computations kept; anchors zero misses, no DUPLICATE. To verify.
- sp-20 written (2026-10-29): Las estaciones GNSS del IGN, 20 questions, 10 computations (7 dates, 3 amounts); scenario 550 words, Madrid 2027 calendar checked by script (only 12 Oct 2027 named); anchors zero misses, no DUPLICATE; Dirección General of a department: no alzada/reposición/contencioso question; annex III RD 462/2002 figures stated in the scenario. To verify.
- sp-19 written: La MUGEJU: ayudas y mantenimiento, 20 questions, 10 computations (8 dates, 2 amounts); 0 real check flags (6 flags: the named 16 August and the 1 May month-distractor), no DUPLICATE, anchors zero misses; festivos checked by script; no alzada/reposición (MUGEJU statute not checked), no IOC rule, no 47.2
- sp-18 replacements written (2026-10-29): q21–q27 (replacing q01, q10, q12, q13, q15, q18, q20: art. 53.1 RD 203/2021 date, art. 67.3 TREBEP date, art. 64.3 and 64.1 RD 364/1995, art. 42.2 TRLCPE, art. 46 LGP, art. 148 LGP); scenario: Aurora destinada en el Centro (promoción interna sentence removed), 14.520 € inside the 26.500 €, the 98.000 € shortfall made good before the licitación, Hipólito digitised Wed 3 Feb, Lorenza's two children; 10 computations kept, 0 check flags, anchors zero misses. To verify.
- sp-14/q27 PASS (verify-3) → sp-14 complete (20). sp-20 verified (verify-1): 12 PASS, 8 FAIL (q01, q02, q14 citation; q15 explanation; q16, q17 official copies; q18 same as sp-19/q19; q20 same as sp-17/q16); scenario fault: no plazo stated for the second company's request → 8 replacements + fix owed. RD 462/2002 anexo III figures confirmed against the 2022-12-24 consolidation
- sp-19 verified (verify-1): 17 PASS, 3 FAIL (q02 repeats sp-14/q01, sp-15/q03; q08 unique: «cinco años» to a 29 Feb; q17 citation: art. 53.2.c LGP); scenario OK; sp-19/q19 drop withdrawn by its verifier → restored.tsv. 3 replacements owed
- sp-19 replacements written (2026-10-29): q21–q23 (replacing q02, q08, q17: art. 87 LPAC, art. 29.4 LCSP, art. 53.2 LGP); «Berta Quintanilla Soria» renamed «Leocadia Marcos Soria»; scenario: Alcalá registry sentence dropped, actuaciones complementarias sentence added; 10 computations, anchors zero misses, no DUPLICATE. To verify.
- sp-18 replacements verified (verify-2): 5/7 PASS, scenario OK, no kept question broken; q21 FAIL (unique/citation: the stem's counting premise leads to the 4 Aug distractor), q26 FAIL (key: capítulo-level credit, other 226 subconceptos have saldo) → 2 replacements owed (II.2, V.2).

## Paused (2026-10-29, user: shutdown) — where to resume

- **Stopped mid-run:** the sp-20 replacement writer (repl-11) and the sp-19 replacement verifier (verify-2). `sp-20.draft.json` still ends at q20 (no replacements written), but the writer may have started editing its scenario: before relaunching, run `case_check.py sp-20` and compare the scenario with the sentences `sp-20.verify-1.md` quotes. `sp-19.verify-2.md` was not written and no sp-19 line was appended to `drops.tsv`.
- **Complete (20 verified questions each):** sp-01 to sp-17.
- **Owed:** sp-18: 2 replacements (for q21 II.2, q26 V.2). sp-19: verify q21–q23 and the edited scenario (rename to Leocadia Marcos Soria; actuaciones complementarias sentence). sp-20: scenario fix + 8 replacements (q01, q02, q14, q15, q16, q17, q18, q20; reasons in `sp-20.verify-1.md`), then verify.
- **Then:** final build (`tools/build_cases.py`), `kept_index.py`, pairs (`tools/pairs.py`, record the ten pairs here), `extract_excerpts.py` + `tools/excerpt_batches.py` and the blind excerpt check (misses → `excerpt-exclusions.yaml`), question-keys golden (`UPDATE_QUESTION_KEYS=1`), goldens read, PDF check, full suites, crypto-futures/Android unchanged, one full case written out in this ledger for Juanjo.
- **Open notes:** sp-01/q30 distractor depends on Madrid's unpublished 2028 calendar; sp-15 depends on Toledo's 2027 local days (San Ildefonso on a Saturday); m05-l02 table vs «Lo que más cae» on who authorises a generación (theory ledger item). The trial build of 2026-10-29 left `exercises/sp-01…05.yaml`, a `course.yaml` entry block under m00-l01 and 100 case entries in `excerpts.json`; the final build rewrites all three.
- sp-19 replacements verified (verify-2): q22, q23 PASS; q21 FAIL (art. 87's «siete días» needs art. 30.2's hábiles, uncited); scenario OK, no kept question broken → 1 replacement (q24) owed. Excerpts: build + extract_excerpts → 360 case keys, all with excerpt; blind check of sp-01…sp-17 (340) started in docs/age-verification/cases/excerpts/ (spec.md, batch-01…06)
- sp-18 replacements written (2026-10-30): q28 (replaces q21; II.4 art. 37.1 LOPDGDD, date) and q29 (replaces q26; V.2 art. 56.2 LGP, amount 23.500 euros); scenario unchanged; 10 computations kept, 0 flags, anchors zero misses. To verify.
- Excerpt check of sp-01…sp-17 (340, reports excerpts/report-01…06): 321 yes, 15 full-only, 4 no. sp-03/q29 re-cited to art. 159.6.f) LCSP (the excerpt then shows letter f; question text unchanged); sp-01/q26, sp-15/q09, sp-07/q06 → «sin extracto» (excerpt-exclusions.yaml). Full-only kept (the fact is behind «Ver artículo completo»). Extractor flags for a later platform round: BOE page header/footer inside Orden HFP/793/2023 art. 1 excerpts; a split «b)» in art. 62.1 LGP and art. 124.1 LPAC page breaks; art. 16.4/16.5 run together
- sp-20 replacements written (2026-10-30): q21–q28 (replacing q01, q02, q14, q15, q16, q17, q18, q20: art. 24.3–4 LRJSP, art. 23 LPAC, art. 48.1 and 42.2 RD 364/1995, art. 62.2 and 55.3 LGP, art. 16.1 RD 2188/1995, art. 12.1 RD 462/2002); scenario: no plazo stated for Mapas (nothing depends on it now), recusación resolution date, Natalia and Lisboa sentences removed, March festivos named; 10 computations kept, no real flags, anchors zero misses. To verify.
- sp-19 replacement written (2026-10-30): q24 (replaces q21; III.3 art. 87 LPAC seven days to allege, stem states «contando días hábiles»); scenario unchanged; 10 computations kept, no DUPLICATE, anchors zero misses. To verify.
- sp-18 replacements verified (verify-3): q28 (II.4, art. 37.1 LOPDGDD), q29 PASS → sp-18 complete (20); slot II.2 → II.4. sp-19/q24 FAIL (explanation: 21 Jul is the fourth día hábil, not the fifth) → q25 owed on a different III.3 angle
- sp-19 replacement q25 written (replaces q24): III.3, art. 56.2 LPAC, date, 10 computations kept
- sp-20 replacements verified (verify-2): 6/8 PASS; scenario OK, no kept question broken; q25 (copy of conv2022·S1·R1, discrepancia over a transferencia) and q28 (copy of conv2025_A·S1·R2, one-day dieta) FAIL → 2 replacements owed (V.2, V.4). Saturation note: the cese date (art. 48.1 RD 364/1995) is now asked in five cases
- sp-19/q25 PASS (verify-4, art. 56.2 LPAC) → sp-19 complete (20)
- sp-20 replacements written: q29 (replaces q25, V.2, art. 50.1 LGP, amount) and q30 (replaces q28, V.4, art. 12.3 RD 462/2002, amount); 11 computations kept
- sp-20 q29, q30 PASS (verify-3) → sp-20 complete (20). **All 20 cases: 400 questions verified.** q30's stem names no norm (coordinator edit before verification, to keep it within 50 words)
- Excerpt check batch 07 (sp-18…sp-20 + re-cited sp-03/q29): 60 yes, 1 full-only (sp-19/q07, art. 168 cut before its 2.º), 0 no; sp-03/q29 yes after re-citation. **Excerpts, all 400 case questions:** 381 yes, 16 full-only, 3 «sin extracto» (sp-01/q26, sp-07/q06, sp-15/q09; excerpt-exclusions.yaml)

# R4 close (2026-10-30): 20 cases, 400 questions

Nothing committed. Cases `sp-01`…`sp-20` are built as `case` exercises (`content/age-administrativo-c1/exercises/sp-NN.yaml`,
listed under `m00-l01` «Cómo es el examen» in `course.yaml`; `exercise_types: [quiz, case]`). Each question counts under its own tema.
Not offered in any exam preset yet (R5).

**Totals.** 400 kept questions, every one passed a blind opus verification (five checks + scenario consistency). Questions
authored: 536 (including the 40 of the two first-version rewrites of sp-01 and sp-03 before the 2026-10-28 rulings);
`drops.tsv` lines: 136, of which 29 restored on re-read under the rulings (`restored.tsv`). Every case: a one-page
scenario (496–550 words), 20 questions, ≥ 10 computations of a date or an amount (10–17 per case), all weekdays and counts
recomputed by verifiers with Python; a calendar audit (`calendar-audit-1.md`) re-checked 82 date questions against the
real 2027 calendars (Madrid Decreto 82/2026 + city days; Andalucía, Castilla y León, Castilla-La Mancha, Aragón, Murcia).
Bias guards on the 400: length-edge z +0.91, longest-is-correct z −0.52; key position 5/5/5/5 in most cases.

**Excerpts** (`docs/age-verification/cases/excerpts/`, blind opus, 7 batches): 381 yes, 16 full-only (the fact is behind «Ver
artículo completo»), 3 «sin extracto» (sp-01/q26, sp-15/q09: art. 159.4.f) cut before its 4.º; sp-07/q06: the figure is in art.
22.1.a)). sp-03/q29 re-cited to art. 159.6.f) LCSP (question text unchanged), then checked «yes».

**Build and checks.** `build_cases.py` → 20 cases; `extract_excerpts.py` → 400 case keys (397 with excerpt); question-keys
golden +400 rows (nothing else moved); citations / lesson-refs / glossary goldens unchanged (cases add no lesson text); print
export: every case prints scenario → 20 questions → 20 key entries with explanations (numbers `sp-NN.k`, as the AGE bank prints
raw ids). Backend: ruff, format, mypy clean; pytest 1,549 passed, 20 skipped (two test edits: the bias guards now include case
questions and a case-pool guard; the «sin extracto» test resolves case questions). Golden digest `f0ae701b…` unchanged (90
fingerprints); `export_bundle.py --verify-only` OK; crypto-futures, `dist/` and Android untouched. Frontend: `npm run build` (tsc + vite) clean; vitest 611 passed, 51 skipped, 2 timed out while the backend suite shared the CPU (`directives.test.ts`, `listShape.test.ts`, lesson-text tests); re-run alone: both pass (59 passed). Not done: the app was not run in a browser, and no PDF file was rendered (the print export was checked; the PDF renderer is tested on the fixture's cases).

## Per case

| Case | Title | Temas (kept) | Written | Dropped | Computations | Difficulty | Pair |
|---|---|---|---|---|---|---|---|
| sp-01 | La autorización de vertido | III.2 1 · III.3 4 · III.4 4 · IV.4 2 · IV.5 3 · IV.6 1 · V.2 3 · V.3 2 | 43 | 23 | 13 | 1.95 | sp-05 |
| sp-02 | La Subdelegación de Valladolid | II.1 1 · III.3 4 · III.4 3 · III.6 1 · IV.4 1 · IV.5 3 · IV.6 1 · V.2 2 · V.3 1 · V.4 3 | 26 | 6 | 17 | 1.90 | sp-11 |
| sp-03 | Formación en línea del INAP | II.4 1 · III.3 4 · III.4 4 · IV.3 1 · IV.4 1 · IV.5 3 · V.2 3 · V.3 2 · V.5 1 | 40 | 20 | 12 | 1.95 | sp-20 |
| sp-04 | Encuestas obligatorias del INE | III.3 4 · III.4 3 · III.6 1 · IV.5 2 · IV.8 2 · IV.9 2 · V.2 3 · V.3 1 · V.4 1 · V.5 1 | 25 | 5 | 12 | 1.85 | sp-16 |
| sp-05 | La reproducción de un manuscrito | III.3 4 · III.4 4 · III.6 1 · IV.4 2 · IV.5 1 · IV.6 2 · V.2 2 · V.3 2 · V.5 2 | 26 | 6 | 13 | 1.95 | sp-01 |
| sp-06 | Una extracción ilegal de agua | III.2 1 · III.3 4 · III.4 3 · III.6 1 · IV.4 2 · IV.5 2 · IV.6 1 · IV.7 1 · V.2 3 · V.5 2 | 26 | 6 | 12 | 2.00 | sp-14 |
| sp-07 | El mantenimiento del sistema informático de la MUFACE | II.3 1 · III.3 4 · III.4 3 · IV.4 2 · IV.5 2 · IV.6 1 · IV.7 2 · V.2 2 · V.3 2 · V.5 1 | 24 | 4 | 12 | 2.00 | sp-18 |
| sp-08 | Las ayudas a la contratación del SEPE | III.3 4 · III.4 4 · III.6 1 · IV.4 1 · IV.5 3 · IV.6 1 · V.2 2 · V.3 1 · V.5 2 · V.6 1 | 23 | 3 | 13 | 2.20 | sp-09 |
| sp-09 | El monte de Valsaín | III.3 4 · III.4 4 · III.6 1 · IV.4 1 · IV.5 2 · IV.8 2 · V.2 3 · V.3 1 · V.4 2 | 24 | 4 | 14 | 2.05 | sp-08 |
| sp-10 | Las subvenciones del FEGA | III.2 1 · III.3 4 · III.4 3 · IV.3 1 · IV.4 2 · IV.5 2 · IV.6 1 · V.2 2 · V.3 3 · V.6 1 | 27 | 7 | 14 | 2.00 | sp-12 |
| sp-11 | El Encuentro Joven del Injuve | II.1 1 · II.4 1 · III.3 3 · III.4 4 · IV.4 1 · IV.5 3 · IV.6 1 · V.2 2 · V.4 2 · V.5 2 | 24 | 4 | 13 | 1.90 | sp-02 |
| sp-12 | La campaña publicitaria de TURESPAÑA | III.3 4 · III.4 4 · III.6 1 · IV.3 1 · IV.4 2 · IV.5 2 · IV.6 1 · V.2 2 · V.3 1 · V.4 2 | 28 | 8 | 14 | 2.00 | sp-10 |
| sp-13 | Las encuestas del CIS | II.3 1 · III.3 4 · III.4 3 · III.6 1 · IV.4 1 · IV.5 2 · IV.7 1 · IV.8 2 · V.2 2 · V.3 3 | 21 | 1 | 11 | 1.85 | sp-19 |
| sp-14 | Los reactivos urgentes del ISCIII | III.2 1 · III.3 4 · III.4 4 · IV.4 2 · IV.5 2 · IV.6 2 · V.2 3 · V.3 1 · V.5 1 | 27 | 7 | 11 | 2.00 | sp-06 |
| sp-15 | La Jefatura de Tráfico de Toledo | II.1 1 · II.3 1 · III.3 4 · III.4 3 · III.6 1 · IV.4 1 · IV.5 3 · IV.6 1 · V.2 2 · V.4 2 · V.5 1 | 21 | 1 | 12 | 1.95 | sp-17 |
| sp-16 | La caída en el teatro del INAEM | III.3 3 · III.4 3 · III.6 2 · IV.5 2 · IV.6 1 · IV.8 2 · IV.9 1 · V.2 3 · V.3 1 · V.5 2 | 23 | 3 | 13 | 1.90 | sp-04 |
| sp-17 | La reforma de un archivo | II.3 1 · III.3 4 · III.4 4 · IV.3 1 · IV.5 3 · IV.6 2 · V.2 2 · V.3 1 · V.4 1 · V.5 1 | 24 | 4 | 12 | 1.95 | sp-15 |
| sp-18 | Coedición y archivo en el CEPC | II.4 1 · III.3 4 · III.4 3 · III.6 1 · IV.4 2 · IV.5 2 · IV.6 1 · IV.7 1 · V.2 3 · V.3 2 | 29 | 9 | 10 | 2.00 | sp-07 |
| sp-19 | La MUGEJU: ayudas y mantenimiento | II.4 1 · III.2 1 · III.3 4 · III.4 3 · IV.4 1 · IV.5 2 · IV.6 2 · IV.7 1 · V.2 2 · V.3 2 · V.6 1 | 25 | 5 | 10 | 1.85 | sp-13 |
| sp-20 | Las estaciones GNSS del IGN | II.4 1 · III.3 4 · III.4 4 · III.6 1 · IV.3 2 · IV.4 1 · IV.5 2 · V.2 2 · V.3 1 · V.4 2 | 30 | 10 | 11 | 1.95 | sp-03 |

Totals by tema (400): II.1 3, II.3 4, II.4 5, III.2 5, III.3 78, III.4 70, III.6 13, IV.3 6, IV.4 25, IV.5 46, IV.6 19, IV.7 6, IV.8 8, IV.9 3, V.2 48, V.3 27, V.4 15, V.5 16, V.6 3

## Pairs for «choose one of two» (R5)

Computed by `tools/pairs.py` (exact minimum-distance matching on mean difficulty ×4, share of computations, bloque and engine
mix): sp-01 + sp-05 · sp-02 + sp-11 · sp-03 + sp-20 · sp-04 + sp-16 · sp-06 + sp-14 · sp-07 + sp-18 · sp-08 + sp-09 ·
sp-10 + sp-12 · sp-13 + sp-19 · sp-15 + sp-17. Every pair within 0.15 of mean difficulty (only sp-08/sp-09 differ at all,
2.20/2.05) and within 10 points per bloque. The platform draws cases at random today; R5 decides how the preset uses the pairs.

## Open

- sp-01/q30: one distractor's explanation depends on Madrid's 2028 calendar (not yet published).
- sp-15: Toledo's 2027 local festivos not yet published (San Ildefonso falls on Saturday 23 Jan); re-check q02, q06 (dropped), q14 if Toledo moves a day.
- Theory ledger: m05-l02's table and its «Lo que más cae» line disagree on who authorises a generación de crédito por aportación del Estado.
- Extractor (platform round): BOE page header/footer inside Orden HFP/793/2023 art. 1 excerpts; split «b)» in art. 62.1 LGP; page breaks in art. 124.1 LPAC; art. 16.4/16.5 run together; the 200-word cut falls before ordinals of arts. 159.4.f), 168, 12.1 Ley 53/1984 (full-only or «sin extracto»).
- sp-03/q40's explanation dismisses two distractors with art. 78.3 LGP's 14 % (AECID) and 10 % (Interior, programa 222A); the citation is art. 2.2 RD 725/1989, which the lesson cites beside art. 78.3. Correct, but the excerpt shows only the 7 %.
- Saturation for R6 growth: art. 47.2 LGP (plurianual) asked in nine cases; the cese date (art. 48.1 RD 364/1995) in five.

## One full case for Juanjo

sp-03 as built after the 2026-10-30 changes (q22, q25 and q41 replaced by q42 and q43; Doña Irene renamed).

### sp-03 — Formación en línea del INAP

El Instituto Nacional de Administración Pública (INAP) es un organismo autónomo con sede en Madrid. En los plazos por días son festivos el 12 de octubre, el 1 de noviembre y el 6 y el 8 de diciembre. A efectos de este supuesto, en Madrid son inhábiles el sábado, 15 de mayo, y el martes, 9 de noviembre de 2027.

Don Mauricio Ferrer Lozano presentó una solicitud el miércoles, 8 de septiembre de 2027. El INAP le notificó el viernes, 5 de noviembre de 2027, que el procedimiento está paralizado porque no aporta un informe indispensable, y que caducará. Él ejerció su derecho de acceso el lunes, 22 de febrero de 2027, y vuelve a ejercerlo el lunes, 13 de septiembre de 2027, sin alegar causa. Doña Noelia Barrantes Cifuentes, notificada el lunes, 14 de junio de 2027, de una resolución firme de la Directora, advierte un error de hecho que resulta del expediente.

El jueves, 28 de octubre de 2027, el INAP pide a la Abogacía del Estado un informe facultativo, sin plazo especial. Acuerda también una información pública, anunciada en el «Boletín Oficial del Estado» el martes, 16 de noviembre de 2027, con el plazo mínimo legal.

El INAP adjudica por procedimiento abierto simplificado un contrato de servicios de formación en línea, de valor estimado 138.000 euros, y una licitadora excluida quiere recurrir. Compra, con la tramitación del artículo 159.6 de la Ley de Contratos del Sector Público, portátiles de uso corriente disponibles en el mercado, de valor estimado 54.000 euros, con anuncio el jueves, 7 de octubre de 2027. La adjudicataria, por 50.000 euros, IVA excluido, entrega con 20 días de retraso sobre el plazo total, por causa suya, y el INAP opta por penalidades. La Intervención Delegada formula reparo por insuficiencia de crédito a esa compra y la Directora no lo acepta. El INAP aprobó un contrato de videoconferencia sin la fiscalización previa preceptiva, y recibe su factura.

El viernes, 10 de septiembre de 2027, el «Boletín Oficial del Estado» publica el concurso por el que Don Esteban Calleja Roldán, del Ministerio de Hacienda, obtiene un puesto en el INAP, ambos en Madrid. Su cese, sin diferir, se produce el martes, 14 de septiembre de 2027, y un permiso le dura hasta el viernes, 24 de septiembre de 2027. Doña Natalia Bermejo Sanz, interina desde el martes, 4 de febrero de 2025, en una plaza vacante del INAP sin convocatoria, cobra retribuciones fijas de 80 euros por día. Don Ramiro Peña Ortiz, de grado personal 22, ve cambiadas por la relación de puestos de trabajo las funciones del puesto que obtuvo por concurso. Don Álvaro Casal Peña, funcionario del INAP con once años de servicios, solicita una excedencia voluntaria por interés particular.

El presupuesto inicial del INAP para 2027 asigna 3.400.000 euros al capítulo 2, gastos corrientes en bienes y servicios, sin modificaciones. El INAP necesita un suplemento de crédito en ese capítulo. El Estado se comprometió con firmeza a aportar 200.000 euros a un programa conjunto: ingresará 150.000 en diciembre de 2027 y 50.000 en febrero de 2028. El INAP alquila un local para aulas de 2027 a 2030, con renta anual de 55.000 euros y crédito inicial de 60.000 en 2027. Tiene anticipos de caja fija por 175.000 euros.

Se plantean las siguientes cuestiones:

**1.** Según la Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales, ¿puede el INAP considerar repetitiva la nueva solicitud de acceso de Don Mauricio Ferrer Lozano y negarse por ello a actuar?  
a) Sí, porque cualquier segundo ejercicio del derecho de acceso se considera repetitivo.  
b) Sí, porque el derecho de acceso solo puede ejercerse una vez al año.  
c) No, porque el ejercicio anterior fue hace más de seis meses y no hay otro motivo para considerarla excesiva. **(clave)**  
d) No, porque el responsable no puede negarse a actuar ante ninguna solicitud de acceso, por repetitiva que sea.  

*Explicación.* Se puede considerar repetitivo el ejercicio del derecho de acceso en más de una ocasión durante seis meses, salvo causa legítima. Don Mauricio lo ejerció el lunes, 22 de febrero de 2027 y lo vuelve a ejercer el lunes, 13 de septiembre de 2027, más de seis meses después. Sin otro motivo que la haga excesiva, el INAP debe atenderla. Considerar repetitivo cualquier segundo ejercicio ignora el plazo de seis meses. La norma no limita el derecho a una vez al año. Negarse a actuar sí cabe ante solicitudes manifiestamente excesivas (art. 12.5 RGPD), y el responsable debe demostrarlo.

*Cita:* art. 13.3 LOPDGDD · *tema* `m02-l04` · *id* `q21` · *dificultad* 2

**2.** Según el artículo 125.1 de la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas, ¿qué órgano resuelve el recurso extraordinario de revisión que plantea Doña Noelia Barrantes Cifuentes?  
a) La Subsecretaría del Ministerio al que está adscrito el INAP, como superior jerárquico.  
b) La propia Directora del INAP, que dictó la resolución firme que se impugna. **(clave)**  
c) El Consejo de Ministros, por tratarse de un recurso extraordinario contra un acto firme.  
d) El Consejo de Estado, que resuelve los recursos contra los actos firmes en vía administrativa.  

*Explicación.* El recurso extraordinario de revisión se interpone contra actos firmes en vía administrativa ante el órgano que los dictó, que también es el competente para resolverlo (art. 125.1 LPAC). La resolución firme es de la Directora del INAP, así que la resuelve ella misma. La Subsecretaría del Ministerio no interviene como superior jerárquico, que es la regla de la alzada. El Consejo de Ministros y el Consejo de Estado no resuelven este recurso por tratarse de un acto firme.

*Cita:* art. 125.1 LPAC · *tema* `m03-l03` · *id* `q43` · *dificultad* 1

**3.** Conforme a la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas, ¿hasta qué fecha debe la Abogacía del Estado emitir el informe facultativo que le solicita el INAP?  
a) Hasta el viernes, 12 de noviembre de 2027.  
b) Hasta el jueves, 11 de noviembre de 2027.  
c) Hasta el lunes, 8 de noviembre de 2027.  
d) Hasta el lunes, 15 de noviembre de 2027. **(clave)**  

*Explicación.* Los informes se emiten en diez días, salvo que una disposición o el resto de los plazos del procedimiento fijen otro, y aquí no hay plazo especial. Los días son hábiles: no cuentan sábados, domingos ni festivos (art. 30.2 LPAC). El informe se pide el jueves, 28 de octubre de 2027, y los diez días empiezan el viernes 29. No cuentan el lunes 1 y el martes 9 de noviembre, festivos. El décimo día hábil es el lunes, 15 de noviembre de 2027. El viernes, 12 de noviembre de 2027, cuenta el 9 de noviembre como hábil. El jueves, 11 de noviembre de 2027, ignora los dos festivos. El lunes, 8 de noviembre de 2027, cuenta diez días naturales.

*Cita:* art. 80.2 LPAC · *tema* `m03-l03` · *id* `q23` · *dificultad* 2

**4.** Conforme a la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas, ¿cuál es la fecha más temprana en que puede terminar el plazo de alegaciones de la información pública que acuerda el INAP?  
a) El jueves, 16 de diciembre de 2027. **(clave)**  
b) El miércoles, 15 de diciembre de 2027.  
c) El martes, 14 de diciembre de 2027.  
d) El martes, 7 de diciembre de 2027.  

*Explicación.* El anuncio de información pública fija un plazo de alegaciones que en ningún caso puede ser inferior a veinte días, y los días son hábiles (art. 30.2 LPAC). Anunciada el martes, 16 de noviembre de 2027, la cuenta empieza el miércoles 17. No cuentan el lunes 6 ni el miércoles 8 de diciembre, festivos. El vigésimo día hábil es el jueves, 16 de diciembre de 2027. El miércoles, 15 de diciembre de 2027, cuenta el 6 de diciembre como hábil. El martes, 14 de diciembre de 2027, ignora los dos festivos. El martes, 7 de diciembre de 2027, cuenta veinte días naturales, con el lunes 6 festivo.

*Cita:* art. 83.2 LPAC · *tema* `m03-l03` · *id* `q24` · *dificultad* 3

**5.** Según el artículo 126.3 de la Ley 39/2015, de 1 de octubre, si Doña Noelia Barrantes Cifuentes interpone el recurso extraordinario de revisión el lunes, 12 de julio de 2027, ¿hasta qué fecha puede el INAP dictar y notificar la resolución sin que el recurso se entienda desestimado?  
a) Hasta el lunes, 11 de octubre de 2027.  
b) Hasta el martes, 12 de octubre de 2027.  
c) Hasta el miércoles, 13 de octubre de 2027. **(clave)**  
d) Hasta el lunes, 13 de septiembre de 2027.  

*Explicación.* Transcurridos tres meses desde la interposición del recurso extraordinario de revisión sin haberse dictado y notificado la resolución, se entiende desestimado (art. 126.3 LPAC). Los meses se cuentan desde el día siguiente y acaban el mismo día del mes de vencimiento (art. 30.4 LPAC): desde el lunes, 12 de julio de 2027, el plazo acaba el martes, 12 de octubre de 2027, festivo. El último día inhábil pasa al primer día hábil siguiente, el miércoles, 13 de octubre de 2027 (art. 30.5 LPAC). El martes, 12 de octubre de 2027, no traslada el último día inhábil. El lunes, 11 de octubre de 2027, cuenta noventa días naturales, que acaban el domingo, 10 de octubre de 2027, y pasan al lunes. El lunes, 13 de septiembre de 2027, aplica dos meses, que acaban el domingo, 12 de septiembre de 2027, y pasan al lunes.

*Cita:* art. 126.3 LPAC · *tema* `m03-l03` · *id* `q42` · *dificultad* 3

**6.** Según la Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público, ¿cabe recurso especial en materia de contratación contra la adjudicación del contrato de servicios de formación en línea que quiere interponer la licitadora excluida?  
a) Sí, porque el valor estimado de un contrato de servicios supera los cien mil euros. **(clave)**  
b) No, porque el valor estimado no alcanza el umbral de 140.000 euros de la regulación armonizada.  
c) No, porque contra la adjudicación del procedimiento abierto simplificado solo cabe recurso de alzada.  
d) Sí, pero solo si el valor estimado supera los 216.000 euros de los demás entes del sector público.  

*Explicación.* El recurso especial cabe contra los actos de adjudicación de los contratos de servicios con un valor estimado superior a cien mil euros. El contrato de formación en línea tiene un valor estimado de 138.000 euros. El umbral de 140.000 euros es el de la regulación armonizada y no condiciona el recurso especial. Contra los actos que admiten recurso especial no proceden la alzada ni la reposición. Los 216.000 euros son el umbral de regulación armonizada de los demás entes del sector público, y no el del recurso especial.

*Cita:* art. 44.1 LCSP · *tema* `m03-l04` · *id* `q26` · *dificultad* 1

**7.** Según el artículo 159.6 de la Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público, ¿cuál es la fecha más temprana en que puede terminar el plazo de presentación de proposiciones para la compra de los portátiles?  
a) El jueves, 14 de octubre de 2027.  
b) El viernes, 22 de octubre de 2027.  
c) El miércoles, 13 de octubre de 2027.  
d) El viernes, 15 de octubre de 2027. **(clave)**  

*Explicación.* La tramitación del artículo 159.6 fija para las proposiciones diez días hábiles desde el siguiente a la publicación del anuncio, y cinco en las compras corrientes de bienes disponibles en el mercado. Los portátiles de uso corriente valen 54.000 euros, menos de 60.000. Anunciada la compra el jueves, 7 de octubre de 2027, los cinco días hábiles son el viernes 8, el lunes 11, el miércoles 13, el jueves 14 y el viernes 15 de octubre, porque el martes 12 es festivo. El jueves, 14 de octubre de 2027, cuenta el 12 de octubre como hábil. El viernes, 22 de octubre de 2027, aplica los diez días hábiles de la regla general. El miércoles, 13 de octubre de 2027, cuenta cinco días naturales.

*Cita:* art. 159.6 LCSP · *tema* `m03-l04` · *id* `q27` · *dificultad* 2

**8.** Según la Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público, el importe de las penalidades diarias que acumula la empresa adjudicataria de los portátiles por su demora en la entrega es de:  
a) Un total de 726 euros.  
b) Un total de 600 euros. **(clave)**  
c) Un total de 648 euros.  
d) Un total de 6.000 euros.  

*Explicación.* Por la demora en el plazo total, imputable al contratista, la Administración puede imponer penalidades diarias de 0,60 euros por cada 1.000 euros del precio del contrato, IVA excluido. El precio es de 50.000 euros, y 0,60 por 50 son 30 euros al día. En 20 días suman 600 euros. La cifra de 726 euros parte del precio con IVA, 60.500 euros. La de 648 euros toma el valor estimado de 54.000 euros y no el precio. La de 6.000 euros aplica 0,60 euros por cada 100 euros.

*Cita:* art. 193.3 LCSP · *tema* `m03-l04` · *id* `q28` · *dificultad* 1

**9.** Según la Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público, ¿debe la empresa adjudicataria de la compra de los portátiles constituir garantía definitiva para responder de la ejecución del contrato?  
a) Sí, por el 5 % del precio final ofertado, IVA excluido, en siete días hábiles desde la comunicación.  
b) Sí, por el 3 % del presupuesto base de licitación, IVA excluido, antes de formalizar el contrato.  
c) No, porque en esta tramitación del procedimiento abierto simplificado no se requiere garantía definitiva. **(clave)**  
d) Sí, pero solo si el pliego la exige de forma motivada.  

*Explicación.* En la tramitación del artículo 159.6, la letra f) dispone que no se requerirá la constitución de garantía definitiva. El INAP compra los portátiles con esa tramitación, por un valor estimado de 54.000 euros. El 5 % del precio final ofertado, en siete días hábiles desde la comunicación, es la regla del procedimiento abierto simplificado ordinario. El 3 % del presupuesto base de licitación es la penalidad por no formalizar el contrato por causa del adjudicatario, no una garantía. El pliego no tiene que exigirla ni eximirla, porque la tramitación especial la excluye.

*Cita:* art. 159.6.f) LCSP · *tema* `m03-l04` · *id* `q29` · *dificultad* 2

**10.** Según el artículo 155 de la Ley 47/2003, de 26 de noviembre, General Presupuestaria, ¿quién conoce de la discrepancia que plantea la Directora del INAP contra el reparo formulado al expediente de la compra de los portátiles?  
a) El Consejo de Ministros, que adopta la resolución definitiva del reparo.  
b) El Ministro de Hacienda, a propuesta de la Subsecretaría del Ministerio al que está adscrito el INAP.  
c) La Subsecretaría del Ministerio al que está adscrito el INAP, por conducto de la Directora.  
d) La Intervención General de la Administración del Estado, cuya resolución es obligatoria para la Intervención Delegada. **(clave)**  

*Explicación.* El órgano gestor que no acepta el reparo plantea una discrepancia motivada a la Intervención General de la Administración del Estado, en los organismos por conducto de su Director. Si el reparo lo formuló una intervención delegada, la Intervención General de la Administración del Estado la resuelve y su resolución obliga a aquella. Aquí el reparo es de la Intervención Delegada. El Consejo de Ministros decide solo cuando el reparo viene de la Intervención General de la Administración del Estado o esta confirmó el de otra. La Subsecretaría del Ministerio canaliza la discrepancia solo en los ministerios, y el INAP es un organismo autónomo. El Ministro de Hacienda no resuelve este trámite.

*Cita:* art. 155.a) LGP · *tema* `m05-l03` · *id* `q30` · *dificultad* 1

**11.** Según la Ley 47/2003, de 26 de noviembre, General Presupuestaria, ¿puede el INAP reconocer la obligación de pago derivada de la factura del contrato de videoconferencia que acaba de recibir?  
a) No, hasta que se subsane la omisión de la función interventora. **(clave)**  
b) Sí, porque la Directora aprueba y reconoce las obligaciones económicas del organismo.  
c) Sí, siempre que la prestación se haya ejecutado conforme al contrato.  
d) No, y el contrato queda anulado de pleno derecho por la omisión.  

*Explicación.* Si la función interventora era preceptiva y se omitió, no se puede reconocer la obligación, ni tramitar el pago, ni intervenir favorablemente, hasta que se subsane la omisión. El INAP aprobó el contrato de videoconferencia sin la fiscalización previa preceptiva. La Directora reconoce las obligaciones del organismo, pero no antes de esa subsanación. Que la prestación se ejecutara conforme al contrato no suple la fiscalización omitida. La norma no declara anulado el contrato: exige un informe de la Intervención General de la Administración del Estado.

*Cita:* art. 156.1 LGP · *tema* `m05-l03` · *id* `q31` · *dificultad* 1

**12.** Según el artículo 48.1 del Real Decreto 364/1995, de 10 de marzo, ¿hasta qué fecha debía cesar Don Esteban Calleja Roldán en su puesto del Ministerio de Hacienda, sin que se difiriera el cese?  
a) Hasta el lunes, 13 de septiembre de 2027.  
b) Hasta el miércoles, 15 de septiembre de 2027. **(clave)**  
c) Hasta el martes, 14 de septiembre de 2027.  
d) Hasta el viernes, 8 de octubre de 2027.  

*Explicación.* El cese se efectúa dentro de los tres días hábiles siguientes a la publicación de la resolución del concurso en el «Boletín Oficial del Estado». Publicada el viernes, 10 de septiembre de 2027, los tres días hábiles son el lunes 13, el martes 14 y el miércoles 15 de septiembre. El lunes, 13 de septiembre de 2027, cuenta tres días naturales. El martes, 14 de septiembre de 2027, cuenta el día de la publicación como primero. El viernes, 8 de octubre de 2027, aplica los veinte días hábiles del diferimiento, que no se concede.

*Cita:* art. 48.1 RD 364/1995 · *tema* `m04-l05` · *id* `q32` · *dificultad* 2

**13.** ¿Hasta qué fecha puede tomar posesión Don Esteban Calleja Roldán de su puesto en el INAP, según el Real Decreto 364/1995, de 10 de marzo?  
a) Hasta el viernes, 17 de septiembre de 2027.  
b) Hasta el lunes, 27 de septiembre de 2027.  
c) Hasta el miércoles, 29 de septiembre de 2027. **(clave)**  
d) Hasta el jueves, 30 de septiembre de 2027.  

*Explicación.* El plazo para tomar posesión es de tres días hábiles si el destino no implica cambio de residencia, y Don Esteban sigue en Madrid. El cómputo de los plazos posesorios se inicia cuando terminan los permisos concedidos. El permiso acaba el viernes, 24 de septiembre de 2027, y los tres días hábiles son el lunes 27, el martes 28 y el miércoles 29 de septiembre. El viernes, 17 de septiembre de 2027, cuenta desde el cese del martes 14 y olvida el permiso. El lunes, 27 de septiembre de 2027, cuenta tres días naturales desde el fin del permiso. El jueves, 30 de septiembre de 2027, empieza a contar un día después.

*Cita:* art. 48.3 RD 364/1995 · *tema* `m04-l05` · *id* `q33` · *dificultad* 3

**14.** ¿Cuál es el nivel más bajo que puede tener el puesto que se atribuya con carácter provisional a Don Ramiro Peña Ortiz, si es removido de su puesto, según el Real Decreto 364/1995, de 10 de marzo?  
a) Un puesto de nivel 22, el mismo de su grado personal.  
b) Un puesto de nivel 21, un nivel por debajo de su grado personal.  
c) Un puesto de nivel 19, tres niveles por debajo de su grado personal.  
d) Un puesto de nivel 20, dos niveles por debajo de su grado personal. **(clave)**  

*Explicación.* El funcionario removido desempeña provisionalmente un puesto de su Cuerpo o Escala, en el mismo municipio, no inferior en más de dos niveles al de su grado personal. Con grado personal 22, el nivel más bajo permitido es el 20. El nivel 22 exigiría igualar el grado, y la norma permite bajar. El nivel 21 baja un solo nivel y es válido, pero no es el más bajo. El nivel 19 baja tres niveles y excede el límite.

*Cita:* art. 50.5 RD 364/1995 · *tema* `m04-l05` · *id* `q34` · *dificultad* 2

**15.** Según el texto refundido de la Ley del Estatuto Básico del Empleado Público, la compensación económica que corresponde a Doña Natalia Bermejo Sanz si cesa de forma efectiva el viernes, 4 de agosto de 2028, es de:  
a) Un total de 5.600 euros. **(clave)**  
b) Un total de 4.800 euros.  
c) Un total de 6.400 euros.  
d) Un total de 8.400 euros.  

*Explicación.* A los tres años del nombramiento se produce el fin de la interinidad en una vacante sin convocatoria publicada, y seguir más allá incumple el plazo máximo de permanencia. La compensación es de veinte días de retribuciones fijas por año de servicio, con los períodos inferiores a un año prorrateados por meses. Doña Natalia sirve desde el martes, 4 de febrero de 2025, hasta el viernes, 4 de agosto de 2028: tres años y seis meses. El cálculo es 3 × 20 + 6/12 × 20 = 70 días, y a 80 euros por día suman 5.600 euros, por debajo del máximo de doce mensualidades. La cifra de 4.800 euros cuenta solo los tres años completos. La de 6.400 euros redondea a cuatro años. La de 8.400 euros aplica treinta días por año.

*Cita:* disposición adicional decimoséptima.4 TREBEP · *tema* `m04-l03` · *id* `q35` · *dificultad* 2

**16.** Según el Real Decreto 365/1995, de 10 de marzo, ¿de cuántos años puede ser como máximo el período de la excedencia voluntaria por interés particular que solicita Don Álvaro Casal Peña?  
a) De quince años, el máximo general de esta excedencia.  
b) De once años, los que acredita de servicios efectivos. **(clave)**  
c) De cinco años, el mínimo de servicios exigido para solicitarla.  
d) De tres años, como en la excedencia por cuidado de familiares.  

*Explicación.* Cada período de esta excedencia dura al menos dos años continuados y como máximo los años de servicios que el funcionario acredite en las Administraciones Públicas, con tope de quince. Don Álvaro acredita once, por debajo del tope, y once es su máximo. Quince años es el máximo general y solo lo alcanza quien acredita quince o más. Cinco años son los servicios previos que exige solicitar la excedencia, no su duración. Tres años es la duración de la excedencia por cuidado de familiares.

*Cita:* art. 16.3 RD 365/1995 · *tema* `m04-l04` · *id* `q36` · *dificultad* 1

**17.** Según la Ley 47/2003, de 26 de noviembre, General Presupuestaria, ¿hasta qué importe puede autorizar por sí sola la Directora del INAP el suplemento de crédito que necesita el capítulo 2?  
a) Un importe máximo de 500.000 euros.  
b) Un importe máximo de 680.000 euros.  
c) Un importe máximo de 340.000 euros. **(clave)**  
d) Un importe máximo de 1.000.000 euros.  

*Explicación.* Los Directores de los organismos autónomos autorizan suplementos de crédito hasta el 10 % del capítulo de su presupuesto inicial de gastos, siempre que no superen 500.000 euros. El capítulo 2 del INAP suma 3.400.000 euros, sin otras modificaciones, y el 10 % son 340.000 euros, menos de 500.000. La cifra de 500.000 euros es el tope en euros, que la Directora no alcanza porque el 10 % la limita antes. La de 680.000 euros es el 20 % del capítulo, que el Ministro de Hacienda no puede alcanzar. La de 1.000.000 euros es el otro límite del Ministro de Hacienda.

*Cita:* art. 56.3.a LGP · *tema* `m05-l02` · *id* `q37` · *dificultad* 2

**18.** Según la Ley 47/2003, de 26 de noviembre, General Presupuestaria, ¿por qué importe puede el INAP generar crédito en 2027 con la aportación que el Estado ha comprometido con firmeza?  
a) Por un importe de 200.000 euros.  
b) Por un importe de 50.000 euros.  
c) Por ningún importe, hasta que el Estado efectúe el ingreso.  
d) Por un importe de 150.000 euros. **(clave)**  

*Explicación.* En los organismos autónomos, la generación por aportaciones del Estado cabe cuando existe un compromiso firme de aportación, siempre que el ingreso se prevea realizar en el propio ejercicio. De los 200.000 euros comprometidos, 150.000 se ingresan en diciembre de 2027 y pueden generar crédito. Los 50.000 euros de febrero de 2028 se ingresan en otro ejercicio. La cifra de 200.000 euros cuenta todo el compromiso. La de 50.000 euros toma solo la parte del ejercicio siguiente. Esperar al ingreso efectivo es la regla general, y la norma exceptúa estas aportaciones.

*Cita:* art. 53.3 LGP · *tema* `m05-l02` · *id* `q38` · *dificultad* 2

**19.** Según el artículo 47.2 de la Ley 47/2003, de 26 de noviembre, General Presupuestaria, señale la respuesta correcta sobre el gasto plurianual de las aulas del INAP que se imputa a 2028:  
a) Puede comprometerse la renta íntegra, porque los límites porcentuales no se aplican a los arrendamientos de inmuebles. **(clave)**  
b) Solo puede comprometerse el 70 % del crédito inicial de 2027, porque 2028 es el ejercicio inmediato siguiente.  
c) Solo puede comprometerse el 60 % del crédito inicial de 2027, porque 2028 es el segundo ejercicio.  
d) Solo puede comprometerse el 50 % del crédito inicial de 2027, porque 2028 es el tercer ejercicio.  

*Explicación.* Los límites del 70 % para el ejercicio inmediato siguiente y del 60 % para el segundo no se aplican a los compromisos derivados de los arrendamientos de inmuebles. El local de las aulas es un inmueble alquilado, y el INAP puede comprometer en 2028 la renta íntegra de 55.000 euros. El 70 %, que daría 42.000 euros, sería el límite de 2028 si la norma se aplicara. El 60 % corresponde al segundo ejercicio, 2029, y tampoco se aplica. El 50 % corresponde a los ejercicios tercero y cuarto, 2030 y 2031, y tampoco se aplica.

*Cita:* art. 47.2 LGP · *tema* `m05-l02` · *id* `q39` · *dificultad* 2

**20.** Según el Real Decreto 725/1989, de 16 de junio, sobre anticipos de Caja fija, ¿cuánto puede aumentar como máximo el INAP la cuantía global de los anticipos que tiene establecidos?  
a) Un máximo de 238.000 euros adicionales.  
b) Un máximo de 63.000 euros adicionales. **(clave)**  
c) Un máximo de 165.000 euros adicionales.  
d) Un máximo de 301.000 euros adicionales.  

*Explicación.* La cuantía global de los anticipos de caja fija de un organismo autónomo no puede exceder del 7 % de los créditos del capítulo de gastos corrientes en bienes y servicios del presupuesto vigente. El 7 % de 3.400.000 euros son 238.000 euros. Con 175.000 euros ya establecidos, quedan 63.000 euros. La cifra de 238.000 euros olvida los anticipos existentes. La de 165.000 euros parte del 10 %, tope del artículo 23 del programa 222A del Ministerio del Interior. La de 301.000 euros parte del 14 %, tope de la Agencia Española de Cooperación Internacional.

*Cita:* art. 2.2 RD 725/1989 · *tema* `m05-l05` · *id* `q40` · *dificultad* 2


# Before commit (2026-10-30, user items 1–4)

## 3. Excerpt faults for the next platform round (extractor not patched)

**A. BOE page furniture inside the excerpt** (running head «BOLETÍN OFICIAL DEL ESTADO», «LEGISLACIÓN CONSOLIDADA», «cve: BOE…»,
«Verificable en…», page number). Mechanical scan of every excerpt in `excerpts.json` (bank and cases), 2026-10-30: 16 questions,
all from four PDFs (Orden HFP/793/2023, Orden HAC/557/2026, RDL 14/2025 — BOE originals, not consolidated texts — and none of the
consolidated-text PDFs). `part` says whether the furniture is in the shown text or only behind «Ver artículo completo».

| question | citation | part | furniture |
|---|---|---|---|
| `m05-l01-q055` | anexo I Orden HAC/557/2026 | text | «Núm. 137 Viernes 5 de» |
| `m05-l01-q056` | anexo I Orden HAC/557/2026 | text | «Núm. 137 Viernes 5 de» |
| `m05-l01-q078` | art. 4.2 Orden HAC/557/2026 | full | «Núm. 137 Viernes 5 de» |
| `m05-l01-q080` | art. 5 Orden HAC/557/2026 | full | «Núm. 137 Viernes 5 de» |
| `m05-l01-q081` | art. 4.2 Orden HAC/557/2026 | text | «Núm. 137 Viernes 5 de» |
| `m05-l01-q082` | art. 6, apartado 1.1, Orden HAC/557/2026 | full | «Núm. 137 Viernes 5 de» |
| `m05-l01-q083` | art. 6, apartado 1.1, Orden HAC/557/2026 | full | «Núm. 137 Viernes 5 de» |
| `m05-l01-q084` | art. 6, apartado 1.1, Orden HAC/557/2026 | full | «Núm. 137 Viernes 5 de» |
| `m05-l04-q004` | art. 2.1 RDL 14/2025 | full | «cve: BOE» |
| `m05-l04-q005` | art. 2.2 RDL 14/2025 | text | «cve: BOE» |
| `m05-l04-q032` | art. 1 Orden HFP/793/2023 | text | «Núm. 169 Lunes 17 de» |
| `m05-l04-q079` | art. 2.2 RDL 14/2025 | text | «cve: BOE» |
| `m05-l05-q006` | art. 6.1.3 Orden HAC/557/2026 | full | «Núm. 137 Viernes 5 de» |
| `sp-02/q17` | art. 1 Orden HFP/793/2023 | text | «Núm. 169 Lunes 17 de» |
| `sp-09/q20` | art. 1 Orden HFP/793/2023 | text | «Núm. 169 Lunes 17 de» |
| `sp-15/q17` | art. 1 Orden HFP/793/2023 | text | «Núm. 169 Lunes 17 de» |

**B. Text split or run together by the PDF layout** (case reports; text still readable, fact present): sp-04/q17 (art. 62.1 LGP,
«párrafo / b) del apartado 3» split so «b)» reads as a new letter); art. 124.1 LPAC «contencioso- / administrativo» split by a page
break (two case questions in batch 04/06, report items 184 and 325); one art. 16.4 excerpt runs apartado 5 into apartado 4 (report-05 item 272);
a stray «a) anterior.» closing letter b) (report-04 item 236).

**C. The 200-word cut falls before the sub-number that holds the fact** (case questions, blind reports in
`docs/age-verification/cases/excerpts/`; the bank's earlier audits in `docs/age-verification/excerpts/` list their own):

| question | citation | verdict | what is cut |
|---|---|---|---|
| `sp-01/q26` | art. 159.4.f) LCSP | «sin extracto» | the seven días hábiles are in letter f) 4.º; text stops at 3.º; no full text (unit too long) |
| `sp-15/q09` | art. 159.4.f) LCSP | «sin extracto» | same as sp-01/q26 |
| `sp-07/q06` | art. 159.1 LCSP | «sin extracto» | the figure is in art. 22.1.a), which 159.1.a) only refers to (another article, not a cut) |
| `sp-03/q29` | art. 159.6.f) LCSP | yes after re-citation | was cut at 159.6.d) under «art. 159.6» |
| `sp-19/q07` | art. 168 LCSP | full-only | cut in 168.a).1.º; the key is 168.a).2.º |
| `sp-04/q29` | art. 211.1 LCSP | full-only | cut in letter f); the key is letter i) |
| `sp-16/q17` | art. 12.1 Ley 53/1984 | full-only | cut at letter c); key in d) |
| `sp-15/q15` | art. 7.1 RD 33/1986 | full-only | cut at letter k); key in l) |
| `sp-12/q06` | art. 156.2–3 LCSP | full-only | cut at 3.a); key in 3.c) |
| `sp-07/q13`, `sp-09/q16` | art. 89.4 TREBEP | full-only | the reserve of the puesto is past the cut |
| `sp-04/q16`, `sp-07/q17`, `sp-09/q13` | art. 58 LGP | full-only | the organismos autónomos paragraph is past the cut |
| `sp-11/q23`, `sp-14/q15` | art. 97.2 TREBEP | full-only | the plazos are in 97.1 (citation names 97.2) |
| `sp-11/q24` | art. 12.2 RD 462/2002 | full-only | 12.2 refers on to 12.3.a) |
| `sp-01/q38`, `sp-05/q15` | art. 56.4 LGP | full-only | the limits are in 56.3 |
| `sp-03/q25`, `sp-08/q04` | art. 125.2 LPAC | full-only | «causa a)» is defined in 125.1.a) |
| `sp-05/q07`, `sp-06/q23`, `sp-08/q09`, `sp-09/q10` | art. 50.1 LCSP | yes (flagged) | the fifteen días hábiles are shown; letter d), which starts the count, is past the cut |

Groups C rows with «citation names 97.2 / 12.2 / 56.4 / 125.2» are partly citation choices rather than extractor cuts: a later
round may re-cite them to the apartado that holds the fact (question text unchanged), as sp-03/q29 was.

## 2. m05-l02: who authorises a generación de crédito

Law (read in arts. 53, 62, 63 LGP, consolidated 2022-12-24, no later amendment; art. 9 Ley 31/2022, the budget law in force
by extension): ministries authorise the generaciones of art. 53.2 a), d), f) (art. 63.1.b)); the Ministro de Hacienda those of
c), and b) and e) in the Estado (art. 62.1.b)), save Ley 31/2022 art. 9.Tres, Cuatro, Ocho; an organismo autónomo's head those of
b) and e) and the ministerial ones in its own budget, avocable by the minister (art. 63.2); and, during the extended budget, any
modification touching capítulos 4, 7 or 8 of the Estado or an organismo autónomo goes to the Ministro de Hacienda (art.
9.Dos.8 Ley 31/2022, save Cinco). The writer's «contradiction» was not one; the lesson's real gap was art. 9.Dos.8.
- Lesson changed (`docs/age-verification/bank/lesson-fixes/m05-l02-generaciones.md`, rounds 1–3): table rows 1 and 3 name the
  letters and add the capítulos 4/7/8 exception with art. 9.Dos.8; the summary row «Generación» names both criteria (ingreso,
  capítulo); the «Lo que más cae» line adds the exception on the competence and art. 63.1.b) to its citation.
- Blind checks (`m05-l02-generaciones.check.md`, `check-2.md` incl. «Check 3»): round 1 found the Dos.8 gap; round 2 passed
  four of five; the «Lo que más cae» line passed on check 3 after the coordinator applied check-2's order.
- Questions resting on that fact: 12 (bank m05-l02-q151, q152, q154, q176, q242, q291, q292, q293, q301, q308; cases sp-02/q19,
  sp-10/q17), re-verified against the law with the five checks: **12 PASS, 0 dropped** (q291 and q293 name their LGP article;
  the case questions concern capítulos 1 and 2). A wider search (any question on generaciones with organ options) found five
  more (q147, q159, q168, q256, sp-07/q16) whose keys do not rest on the organ.
- local festivos (2026-10-30): Madrid 9 Nov / 15 May stated as Ayuntamiento case facts in sp-03, 04, 05, 07, 08, 10, 14, 16; sp-01 q30 (2028) replaced by q44 (art. 159.3 LCSP, 2027); sp-02, 12, 15 and the rest unchanged; see `docs/age-verification/cases/local-festivos-facts.md`.

## 1. Calendars: no question depends on an unpublished calendar

Publication status of every calendar the cases use: `docs/age-verification/cases/calendar-publication-2027.md` (official
bulletins read 2026-10-30). Published: State 2027 (BOE-A-2026-21254, 13-10-2026); every regional 2027 calendar used (Madrid,
Andalucía, Castilla y León, Castilla-La Mancha, Murcia, Aragón); local 2027 days of Toledo (BOP Toledo 203, 22-10-2026: 19 and
29 Mar), Sevilla (BOJA 210, 29-10-2026), Murcia (BORM 171, 27-07-2026), Segovia/San Ildefonso (BOP Segovia 80, 6-07-2026). Not
published: Madrid city, Valladolid and Zaragoza local days 2027; every 2028+ calendar.

- **Local days stated as case facts** (user decision, option 3): «A efectos de este supuesto, en Madrid son inhábiles el
  sábado, 15 de mayo, y el martes, 9 de noviembre de 2027.» (the council-voted days) in **sp-03, sp-04, sp-05, sp-07, sp-08,
  sp-10, sp-14, sp-16** — the cases with a counted window or rollover touching a Madrid local day. Sentences before → after in
  `docs/age-verification/cases/local-festivos-facts.md`. No Valladolid or Zaragoza local day falls in any counted window.
- **Check when the lists appear** (BOCM «fiestas locales 2027», expected around December 2026; BOP Valladolid; BOA for
  Zaragoza): if Madrid city's published days differ from 15 May and 9 Nov 2027, edit only the stated-days sentence in the eight
  scenarios above to the published days and re-run the date count of the questions listed in `local-festivos-facts.md`; keys
  stay unchanged unless a count moves (then drop and replace as usual).
- sp-15 (Toledo): re-audited against the published BOP Toledo days: no window touches 19 or 29 Mar 2027; no change.
- sp-01: q30 (a distractor counted into March 2028) dropped and replaced by q44 (art. 159.3 LCSP, all counts in 2027); q44
  passed the five checks (`calendar-audit-2a.md`).
- **Re-audit of every kept date question** (`calendar-audit-2a.md`, `calendar-audit-2b.md`): every count touching a stated
  local day is right; 9 questions failed because a key or an explanation count ends in or rolls into 2028 or later (sp-02/q05,
  sp-03/q22, q25, sp-04/q08, sp-08/q20, sp-09/q04, q12, sp-10/q02 [also an explanation miscount], sp-14/q20), and the
  coordinator dropped 4 whose scenario asserted that 2028 month-ends are hábiles (sp-06/q05, q14, sp-11/q20, q23). All 13 are
  replaced (below). Bookkeeping: `restored.tsv` gained an «upto» column, so a restore cancels only the drops before it
  (sp-02/q05, restored on 2026-10-28, is dropped again).
- R4 calendar replacements (writer b, 2026-10-30): sp-08 q24, sp-09 q25 and q26, sp-10 q28, sp-11 q25 and q26, sp-14 q28 written for sp-08 q20, sp-09 q04 and q12, sp-10 q02, sp-11 q20 and q23, sp-14 q20; every count ends in 2027 or needs no date; 4 date and 3 non-date replacements.
- R4 calendar replacements (writer a, 2026-10-30): sp-02 q27, sp-03 q41 and q42, sp-04 q26, sp-06 q27 and q28 written for sp-02 q05, sp-03 q22 and q25, sp-04 q08, sp-06 q05 and q14; two date counts end on 2027 days (sp-03 q42 Wed 13 Oct, sp-06 q28 Thu 21 Oct), four need no date; sp-04's festivos sentence closed again.
- R4 calendar replacements (writer c, 2026-10-30): sp-03 q43 (for q41), sp-04 q27 and q28 (for q26 and q20), sp-06 scenario clause on month plazos removed; no count ends after 2027; sp-04 scenario states the delay is imputable and drops «solo» from the festivos sentence.
- R4 future-dates replacements (writer d, 2026-10-30): sp-09 q27 and sp-17 q25 written for sp-09 q11 and sp-17 q10; neither depends on a date count (art. 243.3 LCSP plazo de garantía; art. 10.1.d) TREBEP months remaining); kept computations 12 and 12.
- Coordinator: sp-09 scenario's festivos sentence drops «y el miércoles, 6, y el viernes, 8 de diciembre de 2028» (2028 calendar unpublished; no kept question counts them after q11's drop)
sp-04 q29 written (replaces q27): art. 211.1.i) LCSP, impago de salarios as cause of resolution, no computation; sp-04 keeps 11 computations
sp-17 q26 written (replaces q25): IV.3 art. 10.4 TREBEP, interino en vacante, no computation

### 1 (cont.). Replacements and their verification

The 13 calendar drops and the further faults their checks found were replaced and blind-verified
(`calendar-replacements-a/b/c/d/e.verify.md`): batch B 7/7 PASS; batch A 4/6 (sp-03/q41 citation, sp-04/q26 imputability
unstated → replaced again); a focused check of every kept question showing a 2028+ date (`future-dates-check.md`) dropped
sp-09/q11 (a distractor counted días hábiles in December 2028) and sp-17/q10 (two counting methods); the coordinator dropped
sp-04/q20 (an explanation count in 2028). Second-round replacements: sp-03/q43, sp-04/q28 PASS; sp-04/q27 (copy of conv2020_X
P1 28) → q29 (art. 211.1.i) LCSP) PASS; sp-09/q27 PASS; sp-17/q25 (two options defensible) → q26 (art. 10.4 TREBEP) PASS.
Scenario edits checked blind with every kept question: sp-04 (delay «por causa suya», «solo» removed from its festivos list),
sp-06 (the clause asserting that month-ends are hábiles removed), sp-09 (6 and 8 Dec 2028 removed from its festivos list).
**State now:** every case has 20 verified questions; no key or explanation count needs a calendar that is not published,
except through a local day the scenario states (the eight Madrid cases above). Kept computations per case 10–16.

**Excerpts after the replacements** (batch 08, 17 new questions: 16 yes, 1 full-only — sp-04/q29, art. 211.1 cut before
letter i)): over the 400 kept questions, **382 yes, 15 full-only, 3 «sin extracto»** (unchanged three). Add sp-04/q29 to
list C of item 3.

**Pairs, recomputed on the final questions** (`tools/pairs.py`; they replace the pairs in «R4 close»): sp-01 + sp-05 ·
sp-02 + sp-10 · sp-03 + sp-04 · sp-06 + sp-08 · sp-07 + sp-18 · sp-09 + sp-20 · sp-11 + sp-16 · sp-12 + sp-14 · sp-13 + sp-19 ·
sp-15 + sp-17. Every pair within 0.10 of mean difficulty (sp-06/sp-08 2.10/2.20, sp-03/sp-04 1.85/1.80, the rest equal) and
within 10 points per bloque. Length guards over the 400: edge z +1.15, longest z +0.03.

Per case, final (supersedes the table in «R4 close»; «Written» counts every authored id, including sp-01's and sp-03's
first versions):

| Case | Title | Temas (kept) | Written | Dropped | Computations | Difficulty | Pair |
|---|---|---|---|---|---|---|---|
| sp-01 | La autorización de vertido | III.2 1 · III.3 4 · III.4 4 · IV.4 2 · IV.5 3 · IV.6 1 · V.2 3 · V.3 2 | 44 | 24 | 13 | 1.95 | sp-05 |
| sp-02 | La Subdelegación de Valladolid | II.1 1 · III.3 4 · III.4 3 · III.6 1 · IV.4 1 · IV.5 3 · IV.6 1 · V.2 2 · V.3 1 · V.4 3 | 27 | 7 | 16 | 1.95 | sp-10 |
| sp-03 | Formación en línea del INAP | II.4 1 · III.3 4 · III.4 4 · IV.3 1 · IV.4 1 · IV.5 3 · V.2 3 · V.3 2 · V.5 1 | 43 | 23 | 11 | 1.85 | sp-04 |
| sp-04 | Encuestas obligatorias del INE | III.3 4 · III.4 3 · III.6 1 · IV.5 2 · IV.8 2 · IV.9 2 · V.2 3 · V.3 1 · V.4 1 · V.5 1 | 29 | 9 | 11 | 1.80 | sp-03 |
| sp-05 | La reproducción de un manuscrito | III.3 4 · III.4 4 · III.6 1 · IV.4 2 · IV.5 1 · IV.6 2 · V.2 2 · V.3 2 · V.5 2 | 26 | 6 | 13 | 1.95 | sp-01 |
| sp-06 | Una extracción ilegal de agua | III.2 1 · III.3 4 · III.4 3 · III.6 1 · IV.4 2 · IV.5 2 · IV.6 1 · IV.7 1 · V.2 3 · V.5 2 | 28 | 8 | 11 | 2.10 | sp-08 |
| sp-07 | El mantenimiento del sistema informático de la MUFACE | II.3 1 · III.3 4 · III.4 3 · IV.4 2 · IV.5 2 · IV.6 1 · IV.7 2 · V.2 2 · V.3 2 · V.5 1 | 24 | 4 | 12 | 2.00 | sp-18 |
| sp-08 | Las ayudas a la contratación del SEPE | III.3 4 · III.4 4 · III.6 1 · IV.4 1 · IV.5 3 · IV.6 1 · V.2 2 · V.3 1 · V.5 2 · V.6 1 | 24 | 4 | 13 | 2.20 | sp-06 |
| sp-09 | El monte de Valsaín | III.3 4 · III.4 4 · III.6 1 · IV.4 1 · IV.5 2 · IV.8 2 · V.2 3 · V.3 1 · V.4 2 | 27 | 7 | 12 | 1.95 | sp-20 |
| sp-10 | Las subvenciones del FEGA | III.2 1 · III.3 4 · III.4 3 · IV.3 1 · IV.4 2 · IV.5 2 · IV.6 1 · V.2 2 · V.3 3 · V.6 1 | 28 | 8 | 14 | 1.95 | sp-02 |
| sp-11 | El Encuentro Joven del Injuve | II.1 1 · II.4 1 · III.3 3 · III.4 4 · IV.4 1 · IV.5 3 · IV.6 1 · V.2 2 · V.4 2 · V.5 2 | 26 | 6 | 12 | 1.90 | sp-16 |
| sp-12 | La campaña publicitaria de TURESPAÑA | III.3 4 · III.4 4 · III.6 1 · IV.3 1 · IV.4 2 · IV.5 2 · IV.6 1 · V.2 2 · V.3 1 · V.4 2 | 28 | 8 | 14 | 2.00 | sp-14 |
| sp-13 | Las encuestas del CIS | II.3 1 · III.3 4 · III.4 3 · III.6 1 · IV.4 1 · IV.5 2 · IV.7 1 · IV.8 2 · V.2 2 · V.3 3 | 21 | 1 | 11 | 1.85 | sp-19 |
| sp-14 | Los reactivos urgentes del ISCIII | III.2 1 · III.3 4 · III.4 4 · IV.4 2 · IV.5 2 · IV.6 2 · V.2 3 · V.3 1 · V.5 1 | 28 | 8 | 10 | 2.00 | sp-12 |
| sp-15 | La Jefatura de Tráfico de Toledo | II.1 1 · II.3 1 · III.3 4 · III.4 3 · III.6 1 · IV.4 1 · IV.5 3 · IV.6 1 · V.2 2 · V.4 2 · V.5 1 | 21 | 1 | 12 | 1.95 | sp-17 |
| sp-16 | La caída en el teatro del INAEM | III.3 3 · III.4 3 · III.6 2 · IV.5 2 · IV.6 1 · IV.8 2 · IV.9 1 · V.2 3 · V.3 1 · V.5 2 | 23 | 3 | 13 | 1.90 | sp-11 |
| sp-17 | La reforma de un archivo | II.3 1 · III.3 4 · III.4 4 · IV.3 1 · IV.5 3 · IV.6 2 · V.2 2 · V.3 1 · V.4 1 · V.5 1 | 26 | 6 | 11 | 1.95 | sp-15 |
| sp-18 | Coedición y archivo en el CEPC | II.4 1 · III.3 4 · III.4 3 · III.6 1 · IV.4 2 · IV.5 2 · IV.6 1 · IV.7 1 · V.2 3 · V.3 2 | 29 | 9 | 10 | 2.00 | sp-07 |
| sp-19 | La MUGEJU: ayudas y mantenimiento | II.4 1 · III.2 1 · III.3 4 · III.4 3 · IV.4 1 · IV.5 2 · IV.6 2 · IV.7 1 · V.2 2 · V.3 2 · V.6 1 | 25 | 5 | 10 | 1.85 | sp-13 |
| sp-20 | Las estaciones GNSS del IGN | II.4 1 · III.3 4 · III.4 4 · III.6 1 · IV.3 2 · IV.4 1 · IV.5 2 · V.2 2 · V.3 1 · V.4 2 | 30 | 10 | 11 | 1.95 | sp-09 |

## 4. Suites (2026-10-30, final state)

Build (`build_cases.py`, 20 cases) and `extract_excerpts.py` (400 case keys, 397 with excerpt) rerun on the final drafts.
Goldens: `question-keys.tsv` +400 case rows (no bank key moved); `citations.es.txt` regenerated (`UPDATE_CITATIONS=1`) and
read: +4 rows, all the m05-l02 change (art. 9.Dos.8 Ley 31/2022 ×4; «arts. 53.2.a), 63.1.b) y 63.2 LGP»); lesson-refs and
glossary-links goldens unchanged. Backend: ruff, format, mypy (strict) clean; pytest 1,549 passed, 20 skipped.
`export_bundle.py --verify-only` OK; golden digest `f0ae701b…bcaea` (90 fingerprints) unchanged; crypto-futures, `dist/`
and Android untouched. Frontend: `npm run build` clean; vitest 613 passed, 51 skipped, 0 failed. Not done: the app was not
run in a browser and no PDF file was rendered (the print export was checked for all 20 cases).

Stale metadata, not shipped (draft fields only): several `depends_on` quotes and `festivos` fields in sp-04, sp-08, sp-09,
sp-10, sp-16 still quote festivos sentences as they were before 2026-10-30.
