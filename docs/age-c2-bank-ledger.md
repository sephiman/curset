# Question bank ledger — age-auxiliar-c2 (round R3)

Started 2026-11-07. Nothing committed. Plan: `docs/age-c2-bank-plan.md`. Working files, specs and reports:
`docs/age-verification/c2/bank/` (`tools/`, `style-check-brief.md`, `writer-spec.md`, `verify-spec.md`,
`<bloque>/`). Agents under `CLAUDE.md` «Subagent models and concurrency» (writers Sonnet, verifiers Opus, the step-2
style check Sonnet as the round brief says; at most four at once).

## Conventions (standing)

- **Derived candidates** (`tools/derive_candidates.py <bloque>`, from `backend/` with `uv run`). Every kept C1
  question (built exercise YAML, `ofi-*` official sets excluded; cases included) is tried in the C2 lessons its C1
  lesson maps to (`MAPPING`, from the R2 bloque specs). It becomes a candidate when its citation resolves to an anchor
  there and every cited file has the same sha256 in both snapshots. Text is verbatim. The provenance is
  «verificado en C1: <report>», where the report is the newest C1 report (by file time) with a PASS row for the id.
  157 candidates point to an explanation-rewrite check (`bank/style-rewrites-*.check.md`), which is the newest PASS
  for those ids. Their other checks are in the earlier batch report. Output: `<bloque>/<lesson>.derived.json`
  (C2 ids `<lesson>-qNNN` in C1 order), `<bloque>/derivation.md`.
- **Style check, step 2.** `tools/mechanical_style.py` drops what a script decides (checklist 2, 3, 14, 21). Item 6
  is flagged only. Then Sonnet checkers (`style-check-brief.md`) rule on the rest of the C2 checklist. Every failure
  goes to `<bloque>/drops.tsv` (`id tema batch check reason`; batch `mechanical` or `style/<file>`) and is never
  rewritten.
- **Ruling (coordinator, 2026-11-07), checklist 16:** an ofimática stem passes when it names the application and
  version («Excel 365» or «Microsoft Excel 365»); the «Microsoft» prefix of the 2025 stems is not required. Without
  this ruling almost every C1 ofimática question would drop on the prefix alone. Juanjo may overrule it; the drop
  would then be mechanical.
- **Ruling (coordinator, 2026-11-07), checklist 16, locale:** «configurado en español» is required only when the
  key is a shortcut, key tip or format code whose characters differ by locale (Ctrl+B, Alt+H, `aa`). A translated UI
  label or menu path does not need it. Seven II.5 candidates a recheck failed on the wider reading were reinstated
  (`bloque-ii/style/overrides.tsv`, honoured by `tools/collect_style.py`).
- **Consistency recheck (2026-11-07).** The first checkers of II.1–II.7 read item 9 leniently (a few FAILs in 1,026).
  The II.8–II.12 checkers read it strictly: every distractor must be explained by content, never dismissed on the
  source's silence. A script cannot tell the two readings apart (an option-word heuristic flagged passes as often as
  fails). So the kept II.1–II.7 candidates were rechecked strictly on items 6, 9, 16 and 17
  (`style/recheck-a.*`, `recheck-b.*`). Group a (II.1–II.5): 59 of 326 FAIL, 52 of them on item 9 (7 item-16 FAILs reinstated by the locale ruling). Group b (II.6–II.7 and three never-checked ids): 21 of 339 FAIL (item 9: 14, item 16: 7 — «Copilot para Windows» with no version; Snipping Tool key tips Alt+N, Alt+D, Alt+M with no locale).
- **Ruling (coordinator, 2026-11-07), checklist 9, norm temas:** as C1's R3 close accepted, when the cited text
  gives a single value, a single holder of the function or a closed list, and the explanation states that rule, the
  explanation may dismiss the distractors as absent from the precept. Bloque I's first checkers failed 31–53 % of
  I.1–I.10 on a stricter reading (spot-check of I.7 q002–q006: all exclusive rules). Their item-9-only FAILs in I.1–I.10
  and II.1–II.4 are re-judged under the ruling (`rejudge-item9.md`). A re-judged PASS goes to
  `<bloque>/style/overrides.tsv`. Ofimática stays strict (a page's silence does not show a feature is absent).
- **Trim to quota** (`tools/plan_delta.py <bloque> [lesson …]`). Over quota, candidates are kept round-robin across
  anchors, each stem form only up to its 2025 share + 10, keys-not-longest first. The rest are **held**
  (`<bloque>/held.tsv`), not dropped. It writes `<lesson>.kept-derived.json` and the writers' `delta/<lesson>.md`.
- **Authored questions:** `<bloque>/<lesson>.authored.draft.json` (ids continue after the derived ones), verified
  blind by Opus (`verify-spec.md`), reports in `<bloque>/verify/`.
- **Calibration (session 1, done).** atencion-codificacion: 8-letter words to code, binary tables a–f in order,
  filing items at the index's nivel 2 (unchanged, now pinned). Failing tests first. Goldens regenerated. Blind
  re-read pass 5: 50/50 (`docs/age-verification/c2/psicotecnicos/review/README.md` «R3 calibration»).

## Derivation and style check (2026-11-07)

After the style check, the rechecks and the coordinator rulings. «Held» is not dropped (`held.tsv`). Authored and verified columns follow as temas close.

| Tema | Derived | Mechanical drop | Style drop | Kept after style | Held (pre-trim + over quota) | Kept derived | To author (to quota) | Quota |
|---|---|---|---|---|---|---|---|---|
| II.1 | 21 | 2 | 3 | 16 | 0 | 16 | 84 | 100 |
| II.2 | 46 | 2 | 8 | 36 | 0 | 36 | 87 | 123 |
| II.3 | 65 | 3 | 3 | 59 | 0 | 59 | 63 | 122 |
| II.4 | 63 | 6 | 13 | 44 | 0 | 44 | 134 | 178 |
| II.5 | 167 | 3 | 15 | 149 | 0 | 149 | 107 | 256 |
| II.6 | 159 | 0 | 6 | 153 | 0 | 153 | 3 | 156 |
| II.7 | 183 | 0 | 18 | 165 | 0 | 165 | 102 | 267 |
| II.8 | 174 | 0 | 11 | 163 | 0 | 163 | 71 | 234 |
| II.9 | 159 | 7 | 25 | 127 | 0 | 127 | 163 | 290 |
| II.10 | 239 | 0 | 26 | 213 | 0 | 213 | 10 | 223 |
| II.11 | 167 | 0 | 8 | 159 | 0 | 159 | 64 | 223 |
| II.12 | 160 | 0 | 6 | 154 | 0 | 154 | 124 | 278 |
| I.1 | 30 | 2 | 2 | 26 | 0 | 26 | 110 | 136 |
| I.2 | 72 | 21 | 4 | 47 | 0 | 47 | 127 | 174 |
| I.3 | 70 | 13 | 4 | 53 | 0 | 53 | 63 | 116 |
| I.4 | 56 | 5 | 4 | 47 | 0 | 47 | 88 | 135 |
| I.5 | 44 | 9 | 5 | 30 | 0 | 30 | 164 | 194 |
| I.6 | 49 | 9 | 0 | 40 | 0 | 40 | 57 | 97 |
| I.7 | 54 | 1 | 5 | 48 | 0 | 48 | 87 | 135 |
| I.8 | 62 | 3 | 7 | 52 | 0 | 52 | 161 | 213 |
| I.9 | 106 | 21 | 3 | 82 | 0 | 82 | 34 | 116 |
| I.10 | 54 | 9 | 4 | 41 | 0 | 41 | 114 | 155 |
| I.11 | 344 | 61 | 44 | 239 | 0 | 239 | 51 | 290 |
| I.12 | 49 | 6 | 6 | 37 | 0 | 37 | 21 | 58 |
| I.13 | 468 | 66 | 13 | 389 | 215 | 174 | 0 | 174 |
| I.14 | 429 | 68 | 8 | 353 | 159 | 194 | 0 | 194 |
| I.15 | 171 | 16 | 11 | 144 | 0 | 144 | 11 | 155 |
| I.16 | 57 | 1 | 4 | 52 | 0 | 52 | 122 | 174 |
| **Total** | **3718** | **334** | **266** | **3118** | **374** | **2744** | **2222** | **4,966** |

## Capacity notes

- **II.1, II.2 (writer, 2026-11-07):** the C2 lessons' cited text carries 71 and 72 new questions beyond the kept
  candidates. Past that, every new question repeats a fact from the same angle. That leaves II.1 13 short and II.2
  14 short of quota before verification. Per plan § 1, the bloque's total must hold. A shortfall in a thin norm tema
  is made up at the end of bloque II from the ofimática temas with the most uncovered page facts (II.9, II.12, II.7),
  recorded here when applied. It is never made up by repeating a fact.
- **Item 10 ruling, consistency (2026-11-07):** a norm named by the text it approves («texto refundido de la Ley del
  Estatuto Básico del Empleado Público», «Texto Refundido de la Ley General de derechos…») passes as the title. II.1
  q004–q006, failed earlier on the stricter reading, are reinstated (`overrides.tsv`). A bare short name («Estatuto
  Básico del Empleado Público», «la Ley General Presupuestaria») fails, as C1's lint now flags it.

## Authored and verified (bloque II, session 1)

| Tema | Kept derived | Authored | Verify drops | Kept | Quota | Reports |
|---|---|---|---|---|---|---|
| II.1 | 16 | 71 | 11 | 76 | 100 | `verify/m02-l01.v1–v2` |
| II.2 | 36 | 72 | 14 | 94 | 123 | `verify/m02-l02.v1–v2`, `.recheck5` |
| II.3 | 59 | 72 | 2 | 129 | 122 | `verify/m02-l03.v1–v2` |
| II.4 | 44 | 109 | 7 | 146 | 178 | `verify/m02-l04.v1–v2` |
| II.8 | 163 | 92 + r1 41 | 56 + 6 | 234 | 234 | `verify/m02-l08.v1–v2`, `.r1` |
| II.9 | 127 | 196 | 26 | 297 | 290 | `verify/m02-l09.v1–v4` |
| II.10 | 213 | 28 | 7 | 234 | 223 | `verify/m02-l10.v1` |
| II.11 | 159 | 87 | 10 | 236 | 223 | `verify/m02-l11.v1–v2` |
| II.12 | 154 | 157 | 10 | 301 | 278 | `verify/m02-l12.v1–v3` |
| II.5 | 149 | 138 + r1 27 | 53 + 10 | 251 | 256 | `verify/m02-l05.v1–v3`, `.r1` |
| II.6 | 153 | 46 | 6 | 193 | 156 | `verify/m02-l06.v1` |
| II.7 | 165 | 114 + r1 39 | 44 + 3 | 271 | 267 | `verify/m02-l07.v1–v2`, `.r1` |

- **Check 5, spelled out (coordinator, 2026-11-07; `verify-spec.md`):** a check-5 FAIL needs the same stem and options,
  or the same fact, angle and key **with an official distractor carried over**. The II.2 verifier failed nine without
  one. A second Opus verifier re-judged them: 8 PASS (reinstated through `style/overrides.tsv`; their checks 1–4 PASS
  are in `v1`/`v2`), q095 FAIL.
- **Windows 10 (coordinator, 2026-11-07; writer and verifier specs):** no question on a fact a page gives only for
  Windows 10, the web, Mac or mobile, even with the platform named. II.7 lost 12 to it.
- **II.8 (56 of 92 dropped):** the writer patched generic distractor reasons by appending source sentences by script.
  Item 9 still failed («no es lo que dice la página»). Also macOS-only facts, claims no page states, agreement
  errors («cuál de las siguientes botones»), Ctrl+U from a US-shortcut page. The writer spec now forbids scripted
  explanation edits. II.5, by the same writer and run, lost 53 of 138 (item 9: 26; claims no page states: 7; open-list distractors no
  page refutes: 6; Mac/mobile facts: 4).
- **II.7 writer faults:** 18 stems without «Windows 11» (item 16) and 7 explanations that skip distractors. The
  replacement brief must stress both.

## Open items

1. **II.7 «Lo que más cae» line 10 (Liberador de espacio en disco)** rests on `ms-win-liberar-espacio` text that
   only the page's Windows 10 tab gives. No question can test it under the Windows 11 rule. A lesson fix (C2 lesson
   round, with `provenance.py record`) or Juanjo's call.
1b. **II.9 lesson line 119 and «Lo que más cae» line 7 (gráfico de dispersión)** cite `ms-excel-graficos.html`,
   whose scatter-chart text sits only in the page's Excel para la web tab (verifier, `verify/m02-l09.v3.md` notes).
   Same class as item 1: a lesson fix (C2 lesson round, `provenance.py record`) or Juanjo's call. Kept questions
   that rest on that text should be listed and rechecked when it is decided.
2. **Capacity:** II.1, II.2 and II.4 lessons carry fewer questions than their quotas (writers stopped at 71, 72
   and 109 new; II.1 and II.2 after verification 24, 29 and 32 short). Per «Capacity notes», the gap is made up in ofimática at the end of
   bloque II.
3. Ofimática rulings for Juanjo to confirm or overrule: «Excel 365» without «Microsoft» passes item 16. The locale
   clause applies only to locale-dependent shortcuts, key tips and format codes. Norm-tema item 9 accepts an exclusive
   rule. A norm named by the text it approves passes item 10.
4. **Calibration items** (34) and the platform side of storing them: after bloque I (plan § 1).
5. **Register:** II.4 q130, q153, q155 say «consultada en la lección» in the stem (verifier note, passed). Reword
   is not allowed (drop-not-fix): decide at the bloque II build whether to drop them as out of exam register.
6. **II.12, passed but for Juanjo (verifier notes, `verify/m02-l12.v*`):** (a) q269–q275 test Azure App Service
   plan labels and scaling, well past the shared/dedicated hosting concept the lesson cites the page for, and plan
   names are commercial facts that change (checklist 15); (b) q197–q205 name «Búsqueda de Google» (passed: naming
   a service is not naming an application version); (c) q267–q268 test the Windows 11 Start menu, II.6 material,
   under II.12 (the lesson cites that page only for pinning a site from Edge). Drop-not-fix: decide at the bloque
   II build whether (a) and (c) go. II.12 stays over quota either way (301 − 9 = 292 ≥ 278).
7. **II.1–II.4 stem-form mix off target:** norma-completar 46 / 40 / 37 / 45 % against 58 ±10 (derived C1 questions
   name articles). R5.1 allows other stem forms of a tested fact: write norma-completar variants of facts the kept
   set asks in article form (also narrows the capacity gaps), verify, then recheck the mix. Holding art-form derived
   questions would fix the mix but deepen the gaps. Ofimática mixes are all within ±10.
8. **Stem-form mix (check before the build):** II.6 authored is 85 % directa. The tema's combined mix still has to be checked with
   `c2_stats.py` on kept derived + kept authored before the bloque II build. Trim or write `cual` forms to fit.

## Session 1 summary (2026-11-07)

1. Calibration done: three codificación tweaks, tests failing first, goldens regenerated, blind re-read 50/50.
2. Plan written (`docs/age-c2-bank-plan.md`): 2,516 + 2,450 + 34; per-tema quotas; mix and article targets.
3. Tools in `docs/age-verification/c2/bank/tools/`: `derive_candidates.py`, `mechanical_style.py`, `c2_stats.py`,
   `plan_delta.py`, `collect_style.py`, `check_draft.py`, `build_exercises.py` (C1 builder, course-parameterised,
   writes per-question provenance; not yet run).
4. Derived: 3,718 C1 candidates (bloque I 2,115, bloque II 1,603), each with «verificado en C1: <report>».
5. Mechanical drops 334 (mostly bloque I stems outside 20–40 words: C1's date computations ran to 50).
6. Style check (Sonnet) on every candidate, then consistency rechecks and rulings: 266 style drops in all.
7. Trim to quota: 374 held (I.13, I.14), 2,744 kept derived; about 2,220 to author to reach quotas.
8. Written: II.1, II.2, II.6, II.7 (303 questions), all verified blind (Opus): 75 dropped.
9. II.3 (72, to quota) and II.4 (109, 25 short: capacity) written. `c2_stats.py` fixed: its norm regex missed
   «Orden PCM/…» and «Orden HAP/…» (`\bOrden [A-Z]\b`), so those stems counted as enunciado/directa; earlier
   trims used the old classifier (harmless: no tema was over quota on those forms). II.5 (138) and II.8 (92) written,
   both above quota need; the writer appended source sentences to generic distractor reasons by script (verifiers
   to watch item 9). II.9 written (196; q160–q257 verified 87/98), II.12 written (157). `plan_delta.py` now counts kept authored
   questions too and starts ids after the highest existing one. In progress: no verifier (II.9 170/196, II.12 147/157 done); writers on II.11–II.10 and on replacements r1 for II.8 (35) and II.5 (22). Verified: II.3 70/72, II.4 102/109, II.5 85/138, II.8 36/92. Their drafts land as
   `bloque-ii/<lesson>.authored.draft.json` with notes. If a draft has no notes file, the run was cut: complete it.
10. Nothing built. Nothing committed. Suites not run since the calibration (psicotécnico suite passed then, apart
    from the goldens test the regeneration fixed).

## Where to resume

0. **Bloque II verified: 2,462 kept ≥ 2,450** (per tema in the table above). Remaining before the build: item 7
   of Open items (II.1–II.4 mix), Juanjo's calls on Open items 1, 1b, 5, 6, and the C1 bias guards per tema.
1. Every bloque II tema has had its first draft verified. Replacements r1 written: II.8 (41), II.5 (27), II.7
   (39). II.5 r1 verified (17/27), II.8 r1 (35/41). II.7 r1 (36/39). All done. In the coverage check before the build, confirm the official
   coverage of 2024-P2-23 and 2020-P2-15 (II.7 writer's request). Verify each new draft (Opus, `verify-spec.md`, batches ≤ 60 by cited unit), then `collect_style.py bloque-ii`.
2. (II.11 and II.10 are being written; if a draft has no notes file, the run was cut: complete it.)
3. Replacements: per tema, `plan_delta.py` again (kept derived is fixed; count kept authored against quota) and write
   the gap, II.1/II.2 shortfall into ofimática (Capacity notes). Re-verify replacements.
4. Mix and bias per tema (`c2_stats.py` on kept derived + kept authored; C1 slot and length-edge guards), then the
   bloque II build (`tools/build_exercises.py bloque-ii m02`), cross-reference, excerpts, goldens,
   `docs/age-verification/c2/tools/close_round.sh`.
5. Ten random bloque II questions for Juanjo, appended here.
6. Bloque I: all candidates style-checked and trimmed; delta sheets in `bloque-i/delta/`. Writing starts at I.1.

## Ten random bloque II questions (seed 20261107, from the kept set)

1. **m02-l12-q158** (II.12, derived from C1 m06-l08-q262) — En Microsoft Edge, en Windows 11, ¿qué pasos permiten quitar una extensión desde el botón Extensiones, a la derecha de la barra de direcciones?
   - a) Extensiones › Obtener extensiones para Microsoft Edge › Obtener
   - b) Extensiones › Notificar abuso › Rellenar el formulario
   - c) Extensiones › Más acciones › Quitar de Microsoft Edge › Quitar  ✓
   - d) Extensiones › Administrar extensiones › botón de alternancia
   Cita: fuente: `ms-edge-extensiones.html`; «Quitar una extensión de Microsoft Edge». Explicación: Desde el botón Extensiones se selecciona Más acciones junto a la extensión y después Quitar de Microsoft Edge › Quitar. Administrar extensiones y el botón de alternancia desactivan la extensión, sin quitarla. Obtener extensiones para Microsoft Edge sirve para agregar extensiones nuevas. Notificar abuso sirve para informar de una extensión que infringe las directivas, en el sitio web de complementos.

2. **m02-l09-q200** (II.9, authored) — En Excel 365, ¿cuál de las siguientes afirmaciones describe lo que caracteriza a los formatos de fecha que empiezan por un asterisco (*) en el cuadro de formato?
   - a) No cambian al modificar la configuración regional del Panel de control
   - b) Son formatos de fecha integrados que se pueden modificar directamente
   - c) Cambian cuando cambia la configuración regional de fecha y hora del Panel de control  ✓
   - d) Siempre muestran el año con cuatro cifras y el mes con su nombre completo en cada celda
   Cita: fuente: `ms-excel-formatos-numero.html`; «Formatos de número». Explicación: La página dice que los formatos con asterisco responden a la configuración regional del Panel de control y los demás no. «Siempre muestran el año con cuatro cifras y el mes con su nombre completo en cada celda»: la página define el asterisco por su respuesta al Panel de control, y no por las cifras del año. «No cambian al modificar la configuración regional del Panel de control»: esa es la propiedad que la página da a los formatos sin asterisco. «Son formatos de fecha integrados que se pueden modificar directamente»: la página dice que el formato de fecha integrado no se puede cambiar.

3. **m02-l10-q137** (II.10, derived from C1 m06-l06-q141) — Señale la afirmación correcta de la ayuda de Access 365 sobre las consultas de acción:
   - a) Se pueden deshacer con Ctrl+Z mientras la base de datos siga abierta
   - b) Solo se pueden deshacer si se ejecutan desde la vista Hoja de datos de la consulta
   - c) Se deshacen automáticamente si la ejecución devuelve un mensaje de error
   - d) No se pueden deshacer, por lo que conviene hacer una copia de seguridad de las tablas  ✓
   Cita: fuente: `ms-access-consultas.html`; «Crear una consulta de actualización». Explicación: La ayuda advierte: «Las consultas de acciones no se pueden deshacer. Conviene que haga una copia de seguridad de las tablas». Deshacerlas con Ctrl+Z contradice «no se pueden deshacer», y hacerlo solo desde la vista Hoja de datos de la consulta contradice lo mismo, que no distingue vistas. Y deshacerse solas ante un error tampoco: la única mención que hace la página de un error en una consulta es el mensaje que dice precisamente que la consulta no se puede deshacer.

4. **m02-l02-q082** (II.2, authored) — Un organismo autónomo del Estado presta servicios directos a los ciudadanos. ¿Le es aplicable el marco general para la mejora de la calidad en la Administración General del Estado?
   - a) No, porque solo se aplica a los departamentos ministeriales.
   - b) Sí, porque el marco se aplica también a los organismos autónomos del Estado.  ✓
   - c) No, porque solo se aplica a las Entidades Gestoras y Servicios Comunes de la Seguridad Social.
   - d) Sí, pero solo si el organismo cuenta con servicios periféricos.
   Cita: art. 4 RD 951/2005. Explicación: El artículo 4 incluye a los organismos autónomos. La aplicación no se limita a los departamentos ministeriales ni a las Entidades Gestoras de la Seguridad Social, y no depende de que el organismo tenga servicios periféricos.

5. **m02-l05-q170** (II.5, authored) — ¿Cuántos chips componían el conjunto que Intel diseñó para responder al encargo de la calculadora Busicom 141-PF, entre ellos la CPU 4004?
   - a) Doce chips personalizados
   - b) Dos chips con memoria
   - c) Cuatro chips en total  ✓
   - d) Ocho chips en total
   Cita: fuente: `intel-4004-aniversario.pdf`; «Intel celebra el 50º aniversario del Intel 4004». Explicación: Faggin y su equipo adaptaron los planes originales y diseñaron un conjunto de cuatro chips que incluía la CPU 4004. «Doce chips personalizados» son los chips personalizados de los planes originales, que el equipo de Intel redujo a cuatro. «Dos chips con memoria» no es el tamaño del conjunto que describe la nota de Intel. «Ocho chips en total» no es el tamaño del conjunto que describe la nota de Intel. Lo que dice la fuente: «diseñaron un conjunto de cuatro chips».

6. **m02-l08-q130** (II.8, derived from C1 m06-l04-q259) — En Word 365, ¿cuál es el orden de pasos correcto para restaurar una versión anterior de un archivo con Autoguardado?
   - a) Clic en el nombre del archivo › Abrir versión › Historial de versiones › Restaurar
   - b) Clic en el nombre del archivo › Historial de versiones › Restaurar › Abrir versión
   - c) Clic en el nombre del archivo › Historial de versiones › Abrir versión › Restaurar  ✓
   - d) Archivo › Guardar una copia › Historial de versiones › Restaurar
   Cita: fuente: `ms-office-autoguardado.html`; «No quería que los cambios se guardaran. ¿Cómo puedo restaurar la versión anterior?». Explicación: La página dice: «En la parte superior de la ventana, haz clic en el nombre del archivo y después, haz clic en Historial de versiones […]. A continuación, haz clic en Abrir versión […]. Para regresar a esta versión, haz clic en el botón Restaurar». La página pone Historial de versiones antes de Abrir versión. La página pide Abrir versión antes de Restaurar. La página parte del nombre del archivo, en la parte superior de la ventana.

7. **m02-l07-q123** (II.7, derived from C1 m06-l03-q151) — En Windows 11, para habilitar la búsqueda en la nube desde Inicio del Explorador de archivos, ¿en qué apartado de Configuración se inicia sesión en las cuentas en la nube?
   - a) Configuración › Cuentas  ✓
   - b) Configuración › Sistema › Acerca de
   - c) Configuración › Sistema › Multitarea
   - d) Configuración › Personalización › Temas
   Cita: fuente: `ms-win-explorador.html`; «Inicie sesión en sus cuentas en la nube desde Inicio>Configuración>Cuentas para habilitar la búsqueda en la nube.». Explicación: La nota de la página dice que se inicia sesión en las cuentas en la nube desde Inicio › Configuración › Cuentas para habilitar la búsqueda en la nube. «Acerca de» muestra los datos del dispositivo, «Multitarea» los ajustes de ventanas y escritorios y «Temas» la apariencia del escritorio.

8. **m02-l07-q004** (II.7, derived from C1 m06-l03-q004) — En el Explorador de archivos de Windows 11, ¿cuál de los siguientes comandos se selecciona para cambiar cómo aparecen los elementos, como iconos, listas o detalles?
   - a) Cambiar nombre
   - b) Compartir
   - c) Eliminar
   - d) Ver  ✓
   Cita: fuente: `ms-win-explorador.html`; «Explorador de archivos en Windows». Explicación: La ayuda del Explorador dice: «Para cambiar cómo aparecen los elementos en el Explorador de archivos, seleccione Ver» y elija entre iconos, listas y detalles. Compartir, Cambiar nombre y Eliminar son comandos del menú contextual que actúan sobre el archivo seleccionado; no cambian el diseño de la vista.

9. **m02-l03-q131** (II.3, authored) — Según el Real Decreto 1708/2011, de 18 de noviembre, por el que se establece el Sistema Español de Archivos, entre las funciones del Archivo General de la Administración está aplicar las resoluciones de la Comisión Superior Calificadora de Documentos Administrativos relativas a la conservación permanente y:
   - a) A la descripción de las fracciones de serie de los archivos de gestión.
   - b) A la transferencia a los Archivos Históricos Provinciales.
   - c) A la propuesta de plazos de los calendarios de conservación.
   - d) Al acceso, en su caso, de agrupaciones documentales.  ✓
   Cita: art. 11 RD 1708/2011. Explicación: Las resoluciones que aplica el Archivo General de la Administración se refieren a la conservación permanente y al acceso, en su caso, de agrupaciones documentales. La descripción, las transferencias provinciales y los plazos de los calendarios no son materia de esa función.

10. **m02-l12-q128** (II.12, derived from C1 m06-l08-q217) — En Microsoft Edge, en Windows 11, la combinación Ctrl+Mayús+D, que actúa sobre las pestañas abiertas de la ventana:
   - a) Abre Favoritos para consultar las páginas guardadas
   - b) Guarda solo la pestaña actual como favorita en la carpeta de favoritos
   - c) Muestra u oculta la barra de favoritos bajo la barra de direcciones
   - d) Guarda todas las pestañas abiertas como favoritos en una carpeta nueva  ✓
   Cita: fuente: `ms-edge-atajos.html`; «Métodos abreviados de teclado en Microsoft Edge». Explicación: Ctrl+Mayús+D guarda todas las pestañas abiertas como favoritos en una carpeta nueva. Guardar solo la pestaña actual como favorita es lo que hace Ctrl+D. Abrir Favoritos es la función de Ctrl+Mayús+O. Mostrar u ocultar la barra de favoritos es la función de Ctrl+Mayús+B.


# Decisions before the bloque II build (Juanjo, 2026-11-07)

1. **Windows 11 desktop only, no exception.** Removed from the lessons: m02-l07 «Liberador de espacio en disco»
   (list item and «Lo que más cae» line; `ms-win-liberar-espacio.html` gives it only on its Windows 10 tab) and
   m02-l09 «Gráfico de dispersión» (list item and «Lo que más cae» line; `ms-excel-graficos.html` gives it only in
   its Excel para la web section). «Lo que más cae» now has nine lines in both. `course.yaml` m02-l07 summary no
   longer names the Liberador. Blind check: `docs/age-verification/c2/bloque-ii/verify/r3-removals-2026-11-07.md`
   (all PASS once the summary was fixed; neighbouring items on the same pages rest on the Windows tab). Records
   redone with `provenance.py record m02-l07 m06-l03 m06-l02 m06-l01` (69 inherited, 20 verified) and
   `record m02-l09 m06-l05` (64 inherited, 53 verified); `test_provenance.py` 41 passed. No kept bank question
   tested either fact (the II.7 and II.9 ones had already failed verification).
2. **II.12:** q269–q275 (Azure App Service plans) dropped. q267 moved to II.6 as `m02-l06-q206`
   (`m02-l06.authored-moved.draft.json`; the II.6 lesson states it; re-anchored, 0 misses; provenance «verificado:
   PASS · verify/m02-l12.v2.md (como m02-l12-q267)»). q268 dropped (the II.6 lesson does not state it). Google
   search questions kept.
3. **II.4:** q130, q153, q155 dropped (a stem must stand on its own).
4. **The six style rulings confirmed** (Conventions above; Open items 3).
5. **II.1–II.4 stem mix:** norm-completion variants of facts the bank tests in article form, at most two per fact,
   from the mix sheets `bloque-ii/delta/m02-l0N.mix.md` (about 8 / 22 / 39 / 13 to write). Drafts
   `m02-l0N.authored-mix.draft.json`, verified as usual.

**Answer-bias guards per tema** (`tools/bias_per_tema.py`, the platform test's own statistics, C1's per-tema bar
±1.5; the course-level test allows ±3), before the mix questions:

| Tema | n | longest z | edge z | worst slot z |
|---|---|---|---|---|
| II.1 | 76 | −0.28 | +0.52 | 0.79 |
| II.2 | 94 | −0.93 | +1.09 | 1.31 |
| II.3 | 129 | −1.79 | −3.64 | 0.15 |
| II.4 | 143 | −1.16 | −3.61 | 1.01 |
| II.5 | 251 | −2.13 | −2.44 | 0.18 |
| II.6 | 194 | −0.52 | −0.07 | 0.41 |
| II.7 | 271 | −1.70 | +0.75 | 1.23 |
| II.8 | 234 | −1.67 | −1.46 | 0.38 |
| II.9 | 297 | −3.18 | +3.07 | 0.70 |
| II.10 | 234 | +0.37 | +0.58 | 1.74 |
| II.11 | 236 | −1.46 | +0.07 | 1.20 |
| II.12 | 292 | −1.31 | +1.31 | 0.54 |

Holding surplus questions alone (`tools/rebalance.py`, dry run) brings II.3 to 2.23, II.7 to 1.56, II.9 to 2.96 and
leaves II.4 and II.5 (no surplus) unchanged. Plan: the II.3–II.4 mix writer was told to lean keys longer; after the
mix questions verify, rerun the guards, write small bias-aware batches where a tema is still over ±1.5 (II.5, which
also needs 5 to reach quota; II.9; II.4 if still over), verify, then apply `rebalance.py --apply` and build.

**Kept-copy ruling for the mix variants (coordinator, 2026-11-07):** a norm-completion variant copies a kept question
(check 4 FAIL) only when it has the same fact, angle and key and carries over **two or more** of that question's
distractors, verbatim or reworded (R5.1 allows variants in other stem forms and distractor sets). The II.1–II.2
verifier applied it. The II.3–II.4 verifier failed on one carried distractor: its 24 copy fails are re-judged
(`verify/mix-recheck-l03-l04.md`). Re-judged PASSes go to `style/overrides.tsv`. The 5 single-distractor passes in
II.2 (q120, q128, q132, q138, q139) stand.

**Bias batches:** II.5 (14 written, keys strictly longest): 5 PASS, 9 FAIL, all item 4 (the key glossed in the
stem's own words, or distractors written as the key's opposite). Steering key length while writing degrades the
questions. Holding surplus (`rebalance.py`) is the lever from here; II.9's batch is being verified.

# Bloque II built (2026-11-07)

`tools/build_exercises.py bloque-ii m02`: **2,384 questions in 112 exercises** (`content/age-auxiliar-c2/exercises/m02-*`,
`course.yaml` entries), every question with exactly one record in `bloque-ii/provenance/<lesson>.md` («verificado en
C1: …» for derived, «verificado: PASS · <report>» for authored). The build skips `drops.tsv` and `held.tsv`, and reads
each report's «verdict» / «final verdict» column by header (reasons may hold «|»).

| Tema | Derived from C1 | Authored | Kept (built) | Quota | Held |
|---|---|---|---|---|---|
| II.1 | 16 | 66 | 82 | 100 | 0 |
| II.2 | 29 | 71 | 100 | 123 | 7 |
| II.3 | 30 | 92 | 122 | 122 | 36 |
| II.4 | 44 | 109 | 153 | 178 | 0 |
| II.5 | 149 | 107 | 256 | 256 | 0 |
| II.6 | 116 | 40 | 156 | 156 | 38 |
| II.7 | 161 | 106 | 267 | 267 | 4 |
| II.8 | 163 | 71 | 234 | 234 | 0 |
| II.9 | 120 | 170 | 290 | 290 | 14 |
| II.10 | 202 | 21 | 223 | 223 | 11 |
| II.11 | 146 | 77 | 223 | 223 | 13 |
| II.12 | 144 | 134 | 278 | 278 | 14 |
| **Total** | **1,320** | **1,064** | **2,384** | **2,450** | **137** |

Derived = copied verbatim from C1 with provenance; authored = written this round and verified blind (Opus).
Held = kept out of the build but not dropped (variant rounds may use them): trims, mix and bias holds.

**Mix:** every bloque II tema within ±10 points of 2025 on every stem form (II.1–II.4 after the norm-completion
variants and the II.2/II.3 mix holds). **Course-level bias guard** (`test_quiz_answer_bias.py`, C2 added to
`SINGLE_CHOICE_BANKS`): longest-is-correct first failed at z −3.95 (448 of 2,460 against 526.5): the writer brief's
«key longest in no more than about a fifth» sat below the 25 % chance of four options. **Juanjo's decision
(2026-11-07):** shift quota to bloque I. 7 held key-longest questions reinstated; 83 questions with a unique longest
distractor held from temas over quota (II.3, II.6, II.9–II.12). Course z −2.69; all bias tests pass. Bloque II
2,384 (47.7 % of 5,000, ≥ 45 %); **bloque I quota 2,516 → 2,582** (+66), to be filled first from its 374 held
C1-derived candidates. Writer spec fix for bloque I: the key is the longest option in about a quarter of a draft
(chance), not «no more than a fifth».

**Per-tema residuals** (C1's bar ±1.5; all within the course limit ±3): II.4 edge −2.57; II.9 longest −1.90, edge
+2.28; II.5 −1.52, II.7 −1.56, II.8 −1.67 (longest). Steering key length while writing failed (II.5 bias batch 5/14,
II.9 7/18: keys marked themselves), so they stay as residuals.

**Excerpts:** `scripts/extract_excerpts.py --course age-auxiliar-c2` built `excerpts.json`: 25 questions with no
excerpt, 113 on a flagged fallback (`docs/age-verification/c2/bank/bloque-ii/excerpts-build.log`). **Not yet
checked:** the blind excerpt check of authored questions (and of derived ones whose excerpt differs from C1's) is
the first item of the next session.

## Where to resume (after the bloque II build)

1. Blind excerpt check, bloque II (Opus, batches): authored questions, plus derived ones whose excerpt text differs
   from C1's; questions whose excerpt falls short go to `excerpt-exclusions.yaml` with the reason (C1's practice).
2. Bloque I: writer spec key-longest fix (above); fill I.13/I.14 and others from `bloque-i/held.tsv` before writing;
   quota 2,582; delta sheets in `bloque-i/delta/` (rerun `plan_delta.py bloque-i`).
3. Calibration items (34) after bloque I.
