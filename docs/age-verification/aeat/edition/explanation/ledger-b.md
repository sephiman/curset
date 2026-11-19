# Part B ledger (resume from here)

Assignment (writers): W1 m03-l01,02,03,04 · W2 m03-l05,06,07,09p · W3 m03-l08,10,11,13p · W4 m03-l12,14,15,16 · W5 m03-l17,18,19,20 ·
W6 m02-l01,02,03p,04,05 · W7 m01-l01,02,03,04 · W8 m01-l05,06,07.   (p = pilot lesson: redo cut cases, add PARA)
Stages: 1 writers · 2 lint+apply overview/NC (explanation.py) + blind verify overview/NC and cases (opus) + reader (sonnet) ·
3 rewrite once (sonnet) · 4 recheck by a different opus · 5 apply layer + terms + records · 6 close_round, goldens read, handoff.
Stage 1 launched 8 writers (W1–W8). Resume: check which <lesson>/layer.md (+draft.md for non-pilot) exist and lint clean.
Stage 2 started: W1,W6 lessons prepped (prep.sh) and sent to opus verifiers V1 (m03-l01..04), V2 (m02-l01..05). Prep command: tools/prep.sh <lessons>; layer-verifier-N.md/layer-reader-N.md per lesson (pilots use 2).
m01-l06: NC dropped (lesson at 1.77x, over cap)
Stage 2 progress: verifiers V1,V2 done; V3(m01-l05..07), V4(m03-l05..07), V5(m03-l08,10,11,13), V6(m03-l17..20) running; W4 (m03-l12,14,15,16) and W7 (m01-l01..04) writing. Next: readers, tools/fails.py merges FAIL+REWRITE into fix-brief.md; fixer once; recheck by different opus; cut leftovers; apply; records.
Stage 3: fixers F1 (m03-l01..04), F2 (m02-*) launched after V1,V2,R1,R2. First-check stats are computed at the end from layer-verifier-1/-2.md and layer-reader-1/-2.md (never overwritten). Verifier rechecks: write layer-verifier-recheck-N.md.
State: all writers done; prep.sh applied to all lessons (layer, overviews, NC, terms are IN the lesson files now, unverified ones included). Verified: m02-*, m03-l01..07, m01-l05..07 (first check). Pending verifier: V5 (m03-l08,10,11,13), V6 (m03-l17..20), V7 (m03-l12,14..16), V8 (m01-l01..04); readers R4. Fixers F1 (m03-l01..04), F3 (m01-l05,07); recheck RC1 (m02). Then: fails.py → fixers → rechecks (RECHECK=1 layer_verify) → cut leftovers (layer.py drop / cut-keys.txt) → records → close.
m02 final: rechecked (RC1) – m02-l03 Silencio cut (2nd fail).
m03-l02 overview: faulty sentence replaced by structure statement after 2nd fail; needs final blind re-check (batch FINAL-OV)
Rechecks launched: RC1 m02 done; RC2 m03-l02..04 done (m03-l02 overview failed twice→replaced, pending FINAL-OV); RC3 m01-l05,07 running. Fixers F4 (m03-l05..08), F5 (m03-l10,11,13) running. Verifiers V6 (m03-l17..20), V7 (m03-l12,14..16), V8 (m01-l01..04) running; readers R5 (m03-l12,14..16), R6 (m03-l17..20) running; R7 (m01-l01..04) todo.
Fixers done: F1,F3,F5 (rechecked or rechecking: RC2 ok, RC3 running, RC4 running m03-l10,11,13). Running: F4 (m03-l05..08), F6 (m03-l17,18), F7 (m03-l19,20); verifiers V7 (m03-l12,14..16), V8 (m01-l01..04); reader R7 (m01-l01..04). Todo after: fails.py m03-l12,14,15,16 (needs V7) → F8; m01-l01..04 (needs V8,R7) → F9; rechecks for F4,F6,F7,F8,F9; FINAL-OV m03-l02 overview.
Running: V7, F6(m03-l17,18), F7(m03-l19,20), RC4(m03-l10,11,13), RC5(m03-l05..08), F9(m01-l01..04). RC3 done: m01-l05 (Tramitación, Acceso) and m01-l07 (Plazas vacantes, Instrucción) failed twice -> cut via tools/finalize_layer.py (cut-keys ∪ latest FAIL). Todo: F8 (m03-l12,14,15,16 after V7), rechecks for F6,F7,F8,F9, FINAL-OV m03-l02, finalize_layer for all, records, close.
FINAL-OV batch: m03-l02 (sentence replaced), m03-l06 (75.3 RIRPF dropped from clause)
FINAL-OV batch2: m03-l15 overview clause replaced after 2nd fail
DONE: Part B closed; handoff-step2.md written; close_round exit 0.
Second pass: 288 -> 285 PASS, 3 FAIL rewritten and passed. m03-l06 overview fixed. Citations classified by script.
