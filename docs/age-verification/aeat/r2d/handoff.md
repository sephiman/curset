# R2d handoff — aeat-agentes-hacienda (2026-11-18)

**Done.** All 33 lessons through R2d (build from git HEAD, verified sentences only, reader pass, blind Opus checks, gap
fill); records written (`r2/<lesson>.md`); words 228,756 → 860k (`r2d/words-final.md`); coverage 452/452
(`r2d/coverage-final.md`); no article inside a range «not treated» (`docs/aeat-coverage-plan.md` «After»,
`docs/aeat-scope-audit.md` «Run 2»). Nothing committed.

**Close (`close_round.sh`, 2026-11-18): exit 1, recorded as it is — nothing fixed after it.**
- Goldens regenerated: only this course changed (`citations.es.txt` +15.6k lines, `glossary-links.es.txt`,
  `lesson-refs.es.txt`); no C1, C2 or crypto-futures path changed. Android bundle: byte-identical to `dist/bundle`.
- Backend: 3,706 passed, 35 skipped, 1 failed — `test_citations::…as_frozen[aeat-agentes-hacienda]` (16 min 42 s).
- Frontend: 865 passed, 210 skipped, 3 failed — `citations/annotate.test.ts` (aeat: «places every citation of the golden
  and changes no word of any lesson»), `refs/listShape.test.ts` (aeat: «carry no list marker in the middle of a
  sentence»), `pdf/lessonRefLabels.test.ts` (aeat m02-l02 → m02-l01 / m01-l05 labels). `tsc -b` clean.
- `test_provenance`: every aeat lesson passes (checked before the close run).
- Origin tags per sentence and esquema row: `r2d/tags/<lesson>.json` (`r2d/tools/tag_origins.py`): 23,517 units —
  HEAD 6,336, range coverage 11,757, reworded 3,139, review item 1,124, gap fill 789, «No confundir» 271, R2b restore
  101; every unit has its report except the 67 of m00-l01 (no record entries; unchanged introduction).

**What the external review got right.** 196 of its 339 items confirmed against the norm: missing enumerations and
articles (consultas, prueba, arts. 195–197 LGT, 162–163 CAU…), «entre otros» standing for legal lists, the glossary
senses of «silencio administrativo», «mutualista», «convenio», «diligencia».
**What it got wrong.** 143 items not confirmed by the article maps (reasons per item in `r2d/<lesson>-map.md`); its
academy material was never used as a source.

**Still open.**
- 7 sentences dropped after two failed re-checks (`r2d/dropped.md`), e.g. art. 3.1.d) Orden HAC/1425/2025, arts. 87.7
  and 96.2–3 LOPJ, arts. 60.3 RD 364/1995, 4.2/4.4 Ley 53/1984: the facts are not stated now.
- Gaps shared with C1/C2, listed not fixed (`r2d/c1-c2-list.md`): art. 122.1 LPAC gloss, art. 66.2 LRJSP «salvo», art.
  2.2.b) Ley 50/1997, art. 4.3 TUE, art. 24.1.e) Ley 50/1997.
- Platform: «apartado undécimo bis/ter/quater» not parsed as citations (prose workaround); `provenance.py` has no
  `m00` bloque (record tool fails on m00-l01; its HEAD record still passes).
- LOPJ text re-extraction owed for the condensed lists of arts. 87, 89, 401, 418–419 and art. 31.3 LO 3/1981.

**For Juanjo (decided without asking; details in `r2d/coordinator-notes.md`).**
- Completeness over size: lessons grew 3.77× (I.2 ×10, I.6 ×5); depth trims are yours to request.
- «Normativa» lines: verifier re-check loops closed by ruling after applying the verifier's list.
- Summaries m00-l01 and III.4: final text is the verifier's last replacement (a summary cannot be dropped).
- Glossary: silencio administrativo from art. 24.4 and 24.2 LPAC; recusación removed (arts. 23–24 LRJSP are in no range);
  diligencia linked to III.8 with 13 lessons excepted; mutualista and the complementos kept.
- Kept as selections: art. 5 CAU (III.20), arts. 9.1/10.1/11.1 LJCA (II.5); Ley 4/2023 chapter level (I.6).
- III.20 misprints in the official text corrected to the evident reading (art. 9.3 CAU, art. 219 Reglamento de Ejecución).
- Art. 68.6 RIRPF still refers to a letra d) of art. 32.2 RIRPF that no longer exists; LOPJ 86.5 vs 89.6 differ on «título
  I/II» of Ley 15/2015 — both kept as the law reads.
- Official keys doubted: 2024-43 (III.4), 2025-24 and 2023-80 (III.19).
