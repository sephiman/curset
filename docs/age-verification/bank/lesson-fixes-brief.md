# Lesson fixes brief — session 5 (2026-10-23)

You change lessons of `content/age-administrativo-c1/es/lessons/` under the R2 rules, for the module named in your
prompt only. Do not commit; do not edit other modules, questions, tests or goldens. Read first: `CLAUDE.md`,
`docs/prose-voice.md` (its «never does» list is a hard constraint), `docs/age-theory-ledger.md` «Decisions applied
after bloque I» (standing conventions, e.g. «(hoy: …)» for renamed organs) and, as the model of method and record,
`docs/age-verification/bank/bloque-ii/prose-gaps/writer.md`. Norms: `sources/normativa.yaml` names each file in
`sources/normativa/`; read the article with `pdftotext -layout` (or the HTML); the version in force (later one where
`cambios_pendientes` applies).

Rules for every change:
- **Additions** (a fact an official exam asks that the lesson does not state): one sentence, or a clause joined to an
  existing sentence, stating the norm faithfully in its own words where shortening would drop a condition, with a
  parenthesised citation in the lesson's form, placed where the fact belongs. Nothing wider than the norm.
- **Corrections** (a lesson error a verifier found): change only what is wrong; keep the rest of the sentence.
- **Citation forms the resolver cannot read**: rewrite to a form it reads (parenthesised, one article per unit, no
  sub-range like «Y.1–2», no letter right before «)» in list rows, the norm named), without changing the fact.
- If a source the fix needs is not in `sources/` (e.g. RGLCAP, Orden HAC/965/2024), make no change and list it.
- If a change would contradict a norm in force, or you find the item is not a gap after all, make no change and say
  why.
- After editing, from `backend/`: `uv run pytest tests/test_esquema.py -q` (must pass) and
  `uv run pytest tests/test_citations.py -q -k "not frozen"` (must pass). Check with the resolver
  (`CourseCitations.build(...)._anchor(lesson, citation, 'es')`, as `docs/age-verification/bank/tools/check_anchors.py`
  does) that each new citation resolves. Do not regenerate goldens.

Record in `docs/age-verification/bank/lesson-fixes/<module>/writer.md`: per item, the lesson, the line numbers after
your change, the sentence added or the whole sentence changed (added words named), the norm's text quoted verbatim,
and the kind (addition / correction / citation form); then items not done and why. Final message: short — items done
per kind, items not done.

## Item lists

**m02** (bloque II)
- m02-l01: art. 17.2 RD 951/2005 and art. 9.1 LO 4/2001 old names without «(hoy: …)»; art. 3.2 RD 208/1996 names repealed
  LO 5/1992 and art. 37 Ley 30/1992 — add the «(hoy: …)» the conventions require (the laws now in force), quoting the
  RD's words as they are.
- m02-l03: RD 1112/2018 arts. 12–13 are not basic after STC 100/2019 (only if a source in `sources/` states it; otherwise
  list); art. 18.1 RD 1112/2018 old ministry name without «(hoy: …)»; the DUE also carries the cese trámites (disp.
  adic. 3.ª.1.d) TRLSC, only if the TRLSC is in sources).

**m03** (bloque III)
- m03-l03 additions: art. 128.2 LJCA (August inhábil in the contencioso, except where it says otherwise); the
  date-to-date month rule for the contencioso (art. 5 Código Civil or art. 185 LOPJ, whichever is in sources and the
  lesson's norms); art. 13 LRJSP (suplencia); art. 30.2 LRJSP (start of the prescription of infracciones and
  sanciones); art. 95.3 párr. 2 LPAC; art. 96.5 LPAC; art. 106.3 LPAC (inadmisión of revisión requests).
- m03-l03 citation form: `art. 6 LJCA` resolves to no anchor — make it resolve; art. 93.2 LRJSP «Ministerio de Hacienda y
  Administraciones Públicas» without «(hoy: …)».
- m03-l04: art. 29.7 LCSP (services complementing a contrato menor de obras); art. 98 RGLCAP only if the RGLCAP is in
  sources (else list).
- m03-l05: arts. 47.1, 48, 49, 51 and 123 LRJSP (convenios, consorcios), arts. 25.1.b) and 89.1 LPAC — one sentence each
  where the lesson's subject reaches them (they were filed «III.3 (o III.5)»); if they belong to m03-l03, add them there.
- m03-l06: art. 68 LPAC (subsanación) where the lesson's procedure needs it.
- m03-l07: the lesson cites art. 20 RD 829/2023 for the Observatorio's adscripción, which that article does not state —
  correct the citation to the norm that states it, or the sentence.

**m04** (bloque IV)
- m04-l07: Ley 29/1975 arts. tercero.uno and diez.uno in a form the resolver anchors; art. 28.3 TRLCPE (organ that
  decides jubilación voluntaria) if the lesson's subject reaches it; art. 4.1 RDL 4/2000 «Ministerio de Administraciones
  Públicas» and art. 5.1 RD 577/1997 «Ministro de Hacienda y Función Pública» stated as plain fact — quote them as the
  norm's words with «(hoy: …)»; MUFACE's nature as organismo autónomo after RD 466/2026 (art. 1.1 RD 577/1997) if in
  sources.
- m04-l09: jubilación anticipada (arts. 207–208 LGSS, the core conditions only) and DT 26.ª LGSS (grade names kept in
  force).
- m04-l06: art. 6 RD 33/1986 (faltas muy graves of the RD) where the lesson lists the RD's faltas; art. 61.s) LRJSP in the
  Resolución section beside art. 47.1 RD 33/1986 (state both; do not resolve the conflict); art. 30.4 LPAC (months date
  to date) where the procedure's month counts rely on it.
- m04-l04: art. 29.3 Ley 30/1984 trienios rule for excedencia por prestación de servicios en el sector público (it stays
  in force by the BOE note and DF 4.ª.2 TREBEP); art. 98.3 TREBEP judicial clause on suspensión provisional.
- m04-l02 and m04-l05: tables now anchor (the parser reads bare cells); check the «Convocatoria y plazos» and «Otras
  formas de provisión» rows resolve; nothing else unless a cell is in a form the resolver misreads.

**m05** (bloque V)
- m05-l01 (decision 2d): l. 136 calls the programas presupuestarios «de carácter plurianual» — keep it only if the LGP
  says it (art. 35.2 LGP); otherwise correct it to the norm's words. Also check the lesson states the art. 6 apartado 1.1
  Orden HAC/557/2026 definition of programas finalistas plainly.
- m05-l02: the criterion between nueva inversión (art. 62) and reposición (art. 63) from the norm that states it (anexo
  IV Resolución de 20-01-2014 or anexo II Orden HAC/557/2026); the retención adicional del 10 % in obras and art. 47.4–6
  LGP only if the lesson's subject reaches them; corrections: the esquema «Estructura de los estados de gastos» tags
  orgánica 40.1.b) and programas 40.1.c) — the LGP says 40.1.a) and 40.1.b); l. ~180 and ~345 «Ministro de Economía»
  unmarked — quote it as the norm's words with «(hoy: …)»; l. ~304 calls the art. 9.Dos.2–5 Ley 31/2022 transfers «del
  Ministro de Hacienda» though 9.Dos.5 belongs to department heads — correct.
- m05-l03: art. 13.2 RD 2188/1995 (fiscalización in ten days, five if urgent); the `art. 15.A).1.º RD 1009/2023` citation
  split across lines and its unbalanced «(hoy: …)» parenthesis — fix the form.
- m05-l04: «Formas de pago» cites apartado noveno.1 Orden PRE/1576/2002 outside parentheses — make it a citation;
  anexo II RD 462/2002 resolves to no anchor — make it resolve.
- m05-l05 l. ~440 merges art. 63's «inútiles por uso normal» with concepto 630 (only substitution by similar goods) —
  correct.
- m05-l06 l. ~70–71 says no due date falls on a weekend under DA 12.ª LCSP; DA 12.ª only moves an inhábil last day to the
  next hábil — correct.

Keep any extracted text or script in your own scratchpad subfolder named after your module (e.g. `<scratchpad>/lesson-fixes-m03/`); other agents share the scratchpad.

**Relaunch (2026-10-23).** An earlier run was stopped mid-way and left no record. Its unchecked edits are in
`git diff HEAD -- <lesson>` for m04-l07, m05-l02 and m05-l03. The m02 lessons' diffs also hold the earlier bloque II
prose gaps, recorded in `bloque-ii/prose-gaps/writer.md`; leave those alone. For every hunk in your module from the
stopped run, check it against the norm under the rules above. Keep it, correct it or revert it, and record it as an
item, saying it came from the stopped run. Then do the remaining items.
