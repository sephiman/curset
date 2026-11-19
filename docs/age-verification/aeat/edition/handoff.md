# Edition step 1 — handoff (2026-11-19)

**Done.** The 32 theory lessons of `aeat-agentes-hacienda` (m00 unchanged) are rebuilt in place from verified R2d sentences,
whole and byte-identical, within the budget table of `docs/aeat-edition-plan.md`. Nothing committed.
- Words (prose, esquema rows apart): pre-R2d 194,355 · pool 574,612 · now 220,833 (×1.14 of pre-R2d; budget at ×1.1 was
  212,728; overrun 14,489 over 21 temas: forced a/b/c sentences, bank-anchor restores, lead-in lists — reasons per tema in `edition/report.md`).
- Kept 7,056 of 15,599 sentences, 591 of 990 esquemas, 4,792 of 7,851 rows. The rest is in `reserve/<lesson>.md`; the full R2d lessons in `pool/`.
- Checks: identity 11,848 checked, 11,832 matched, 16 not matched (verifier replacements, below); coverage 452/452; bank anchors
  4,088/4,088 (the registry's own citation check clean); readers flagged 130 (127 solved by restoring the neighbour, 3 left: verbatim norm text).
- `close_round.sh` green (exit 0): backend 3,707 passed, frontend 868 passed, `tsc -b` clean; C1, C2, crypto-futures, Android bundle unchanged.
- Goldens regenerated and read: `citations` 5,440 prose citations, 0 naming a missing norm; `lesson-refs` 2 references (m02-l02), 0
  dangling; `glossary-links` 557 → 379 web marks.

**For Juanjo.**
- Size is 1.14, not 1.10: forced sentences (official questions, bank anchors, concept picks) cost 14.5k words over the table. Say if you want the bank-anchor restores (≈7k words) back in the reserve instead.
- 16 prose sentences are not byte-identical: blind-verifier replacements that restore a citation lost when a lead-in was cut (m01-l07, m01-l02, m01-l03, m03-l09). Each passed a recheck. Listed in `edition/patches.json`.
- Two pool sentences of m02-l02 are swapped for their pre-R2d id form («m02-l01», «m01-l05»): the platform test needs it.
- 14 table rows lost a stray list marker (decisions §10).
- «Normativa» is script-built and verifier-corrected, and about 30 cited norms have no line (listed in `decisions.md` and the verifier notes). The generator mis-credits units between similar norm names: rewrite it before any rerun.
- Five glossary entries went to `edition/glossary-waiting.md`.
- Not mine: `backend/tests/conftest.py` (registry cache) was changed during the session. The m01-l01 summary in `course.yaml` describes the exercises, not the Constitution (existing).
- I killed a stale `tag_origins` run from another terminal; and I once typed a `git checkout` on the lessons by mistake — the permission layer blocked it, nothing was lost.
