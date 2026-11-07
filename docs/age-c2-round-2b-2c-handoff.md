# Handoff — age-auxiliar-c2, R2b and R2c bloque I (2026-11-06)

Nothing committed. Reports: `docs/age-c2-scope-audit.md` (Run 1, verdict per bloque), `docs/age-c2-theory-ledger.md`
(R2b, R2c, open items), working files `docs/age-verification/c2/r2b/` and `c2/bloque-i/esquemas/`.

**R2b scope.** 618 sections audited (three blind auditors): 601 mapped, 1 instrumental, 11 kept by exam evidence (8
notes), 5 removed (I.1 «Las reformas»; I.13 personal eventual, personal directivo, causas de pérdida; I.15 principios
de gestión presupuestaria), 0 gaps. Notes and trimmed Normativa lines: 12/12 PASS blind.
**Coverage.** Bloque I 134/134, unchanged by the cuts; bloque II «sin fuente oficial» list carried over unchanged.
**Currency.** 78 BOE norms and the EU texts current; LSSI stored date corrected. RDL 31/2026 not convalidated
(plazo ~04-12-2026). No passed «desde» mark. Pages: 312/325 same, 10 changed (23 places PASS), V Plan and CE
análisis by hand, `consilium-presidencia.html` 403.
**R2c bloque I.** 45 esquemas, 239 rows: 214 inherited from C1 byte-identical, 25 verified here; 9 FAILs fixed and
re-checked by other verifiers; m01-l06 none (narrative). Bloque II none (list-shaped).

**Saved pages stripped (your mid-round request).** All 529 HTML pages of C1 and C2 without script/style/iframe/
noscript/tracking attributes; sha256 re-recorded; originals in `~/PycharmProjects/curset-saved-originals/` (still in
git history: not rewritten). New: `saved_pages.py`, `scripts/strip_saved_pages.py`, `tests/test_saved_pages.py`;
`check_pages.py --course` strips the live copy too. Excerpts unchanged; C1 provenance pairs keep equal hashes.

**Tools.** `provenance.py` now blames past C2 commits that only re-flowed an authorised C1 sentence (test added,
failing first). `docs/age-verification/c2/tools/close_round.sh`: the brief's «close-round script» did not exist; this
codifies the ledger's closing checks. `r2b/tools/check_norms.py`, `bloque-i/esquemas/row_stats.py`.

**Close.** Goldens read; crypto-futures unchanged; C1 only the stripped pages and excerpt digests; Android bundle
byte-identical; backend 2,194 passed / 23 skipped; frontend 715 / 81; `tsc -b`, ruff, mypy clean.

**Follow-up (same day).** Both prose gaps fixed and blind-checked: m01-l04 art. 630.1 LOPJ exception restored from C1
(sentences and esquema rows) and «la ley» → «la LOPJ»; m01-l16 «(hoy: …)» gloss. Re-close green (same counts).
Open: C1 m01-l04 still says «salvo que la ley disponga otra cosa» (needs a C1 round + C2 provenance rerun); the
«copilot» extractor bug is platform delta L7. Next round: R3 (question bank).
