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

# Session 2 (2026-11-10): bloque II excerpts, bloque I

## Rulings and findings at the start

- **The +66 of bloque I (coordinator):** Juanjo's decision fills the raised quota first from the held C1 candidates,
  all of which are I.13 and I.14. So I.13 rises 174 → 205 and I.14 194 → 229 (`plan_delta.py` QUOTA; plan § 2); the
  other quotas stay as apportioned. `plan_delta.py bloque-i` re-trimmed: 31 + 35 more kept, 25 still held «over quota».
- **Held candidates not all style-checked:** of the 374 held, 283 carry «pre-trim before style check (over 1.3 ×
  quota)»: they passed the mechanical step only, never the Sonnet style check. The +66 was filled from the 91 that
  were checked. The 283 stay held; they are style-checked only if I.13/I.14 need them to fix mix or bias.
- **Style guide** (`docs/age-c2-exam-style.md`) unchanged since 2026-11-05, before the style check: not reapplied.
- **I.13 and I.14 after the fill** (all derived): stem mix off ±10 on cual (7 % / 10 % against 22) and señale (1 %
  against 12); key longest 15 % (longest z −2.52 / −2.08). To fix at their turn: cual/señale questions authored and
  surplus art-form questions held.

## Bloque II excerpts

- **Derived inheritance** (`tools/excerpt_inherit.py bloque-ii` → `excerpts/bloque-ii-inherit.tsv`): of 1,320 derived
  questions built, 1,297 have an excerpt byte-identical to C1's (heading, text, full text, file, flag) and inherit
  C1's check. The other 23 are questions C1 builds as «sin extracto» (a C1 verifier found the fact neither in the
  excerpt nor elsewhere on the page) for which C2, with no exclusion file, built an excerpt. They go through the check.
- **To check:** the build log's 24 «no excerpt» and 112 «flagged fallback» (the round brief's 25 and 113 were the
  ledger's figures; the log and `excerpts.json` hold 24 and 112), plus 22 of the 23 above (one is also flagged):
  158 items, `excerpts/bloque-ii/batch-01..03.jsonl` (`tools/excerpt_batches.py`), spec `excerpts/spec.md` (C1's
  full pass and re-citation in one step: verdict, and for a miss the exact label or «none: reason»). Two Opus
  verifiers.
- **Result (158 checked):** 47 yes as built (41 of them on a flagged fallback that does hold the fact); 81 misses
  re-cited to the verifier's label; 30 «none» (spread over paragraphs, rows or steps 22, heading only 2, garbled 1,
  no usable label 5). Of the 81 labels, 3 held «;», the citation grammar's separator: re-cited by the coordinator to
  a «;»-free sentence of the same paragraph (m02-l12-q185, q186, q305; tested against the extractor); 3 did not
  resolve and no single block holds the fact (m02-l05-q168, q171: the PDF text breaks the sentence over lines;
  m02-l12-q300: clause (ii) mid-paragraph): citation restored, «sin extracto». Blind Opus recheck of the 78 re-cited
  (`excerpts/bloque-ii/recheck/report-01..02.md`): 73 yes, 5 no (m02-l05-q029, q057, m02-l09-q295, m02-l12-q169,
  q299): «sin extracto», C1's «re-cited, but the blind re-check found the cited paragraph short of the fact».
- **Bloque II now:** 2,384 questions, **120 of the 158 with a checked excerpt, 38 «sin extracto»**
  (`content/age-auxiliar-c2/excerpt-exclusions.yaml`, new; each with its reason). 2,346 excerpts. Re-citations logged
  in `excerpts/bloque-ii-recited.tsv` (78 rows; question text and key unchanged; drafts edited and bloque II rebuilt:
  81 citation lines changed in 29 exercise files, nothing else). Recheck notes passed as yes: m02-l12-q310's excerpt
  heading names 4.12.1 though the text is 4.12.2's noscript element (extractor flag, not a content fault).
- **Open (plan § 7, not in this round's brief):** the 1,064 authored bloque II questions whose excerpt is neither
  flagged nor missing have not been blind-checked. A sampled or full pass is owed before R5.

## I.13 and I.14: derived only, chosen for mix and bias

- Held style check (Sonnet, `bloque-i/style/m01-l13.b5–b7`, `m01-l14.b6–b7`): 283 checked, 250 PASS, 33 FAIL
  (standalone 25: case-bound stems; item 7: 4; item 10: 2; item 4: 1; item 13: 1, m01-l14-q331's «Ministerio para las
  Administraciones Públicas»). Fails in `drops.tsv`; passes relabelled «over quota (style-checked 2026-11-10)».
- `tools/select_derived.py` (new): swaps kept for held derived questions while the mix (±9), article share, the
  longest/edge/slot z (±1.4), negatives and cited-unit coverage improve. **Do not rerun `plan_delta.py` on m01-l13 or
  m01-l14**: its trim would undo the choice.

| Tema | n | cual | señale | article | key longest | longest z | edge z | worst slot | Authored |
|---|---|---|---|---|---|---|---|---|---|
| I.13 | 205 | 13/22 | 3/12 | 66/69 | 19 % | −1.36 | +0.53 | 1.25 | 0 |
| I.14 | 229 | 13/22 | 2/12 | 69/69 | 17 % | −1.10 | −1.31 | 0.95 | 0 |

All stem forms within ±10 of 2025 (señale in I.14 at the edge). Held after the choice: I.13 and I.14 «over quota
(selected out for mix and bias)».

## Bloque I authored and verified (session 2)

Writers Sonnet (`writer-spec.md`, the updated brief), verifiers Opus blind (`verify-spec.md`, batches ≤ 60 by cited
unit, `tools/verify_batches.py`). Status per tema by `tools/tema_status.py` (kept derived + authored − drops − held).

| Tema | Derived kept | Authored | Dropped (key/unique/citation/style/official) | Kept | Quota | Short | Mix ±10 | longest z | edge z | slot | Reports |
|---|---|---|---|---|---|---|---|---|---|---|---|
| I.1 | 26 | 78 + r1 10 | 11 + 2 (0/1/1/7/4) | 101 | 136 | 35 | ok | +0.12 | **−2.59** | 0.86 | `verify/m01-l01.v1–v2`, `.r1.v1` |
| I.2 | 47 | 87 + r1 12 | 14 + 1 (0/3/2/6/4) | 131 | 174 | 43 | ok | +1.21 | −0.27 | 0.86 | `verify/m01-l02.v1–v2`, `.r1.v1` |
| I.3 | 53 | 93 | 15 (0/3/1/9/2) | 131 | 116 | −15 (over) | ok | +0.59 | +1.24 | 0.96 | `verify/m01-l03.v1–v2` |
| I.4 | 47 | 82 + r1 8 | 8 + 0 (0/2/0/2/4) | 129 | 135 | 6 | ok | −0.10 | **−1.82** | 0.56 | `verify/m01-l04.v1–v2`, `.r1.v1` |
| I.5 | 30 | 66 + r1 4 | 4 + 0 (0/0/1/2/1) | 96 | 194 | 98 | ok | −0.25 | −1.20 | 0.24 | `verify/m01-l05.v1–v2`, `.r1.v1` |
| I.9 | 82 | 49 | 8 (0/0/0/7/1) | 123 | 116 | −7 (over) | ok | +0.56 | −0.43 | 0.68 | `verify/m01-l09.v1` |
| I.6 | 40 | 67 | 2 (0/0/0/2/0); 3 held for bias | 102 | 97 | −5 (over) | **art-completar 15/41, señale 26/12** | +0.96 | +1.42 | 0.57 | `verify/m01-l06.v1–v2` |
| I.7 | 48 (3 held) | 97 + r1 20 | 21 + 2 (1/0/0/21/1); 4 held for bias | 135 | 135 | 0 | art-completar 52/41 (+1 over) | −0.51 | +1.26 | 0.84 | `verify/m01-l07.v1–v2`, `.r1.v1` |
| I.8 | 52 | 135 + r1 3 | 3 + 0 (0/1/0/1/1) | 187 | 213 | 26 | ok | +0.17 | +1.46 | 0.63 | `verify/m01-l08.v1–v3`, `.r1.v1` |
| I.10 | 41 | 80 + r1 4 | 4 + 2 (0/1/1/3/1) | 119 | 155 | 36 | ok | +0.28 | +0.09 | 0.26 | `verify/m01-l10.v1–v2`, `.r1.v1` |
| I.15 | 144 (6 held) | 18 + mix 6 | 1 + 1 (0/1/0/1/0) | 160 | 155 | −5 (over) | ok (cual 13/22) | +0.14 | +0.97 | 0.91 | `verify/m01-l15.v1`, `.mix.v1` |
| I.16 | 52 | 65 + r1 8 | 10 + 2 + q062 (0/2/2/3/6) | 112 | 174 | 62 | ok | +0.69 | **+1.86** | 0.65 | `verify/m01-l16.v1–v2`, `.r1.v1` |
| I.11 | 239 (2 held) | 58 + r1 9 | 9 + 0 (0/0/0/7/2); 5 authored held | 290 | 290 | 0 | directa 14/3 (+1 over) | +0.21 | +1.34 | 0.88 | `verify/m01-l11.v1`, `.r1.v1` |
| I.12 | 37 | 28 | 3 (0/1/0/2/0) | 62 | 58 | −4 (over) | ok | −0.45 | +0.83 | 0.73 | `verify/m01-l12.v1` |
| I.13 | 205 | 0 | – | 205 | 205 | 0 | ok | −1.36 | +0.53 | 1.25 | derived only |
| I.14 | 229 | 0 | – | 229 | 229 | 0 | ok | −1.10 | −1.31 | 0.95 | derived only |

- **Capacity (rule 2d):** I.1's lesson holds about 78 new fact-and-angle pairs beyond the 26 kept (writer stopped at
  78 of 110: 32 short before verification); I.2's about 87 (stopped at 87 of 127: 40 short). Replacements r1 cover
  the facts of the dropped questions from another angle (I.1 11, I.2 14). I.4: writer stopped 6 short of 88 (art.
  561.1's catch-all item left out); 8 verify drops, to replace. I.3: over quota by 15 with no bias to fix: kept
  (rule 2d holds surplus only where its removal fixes a bias); the surplus offsets the bloque's capacity shortfalls.
  I.3 q083's explanation miscounted the calendar (days 15/45 for 14/44): dropped (style), key was right.
- **Verifier calls to note:** I.1 q062, q076, q077, q085, q092 ask which chapter or section holds a right; passed on
  check 3 because the cited article sits under the heading that is the key (q085, citing art. 13.2 for the chapter's
  subject, the weakest). `drops.tsv` check column mixes numbers and words between verifiers (append-only; same meaning).

## Bloque I capacity: the quota is not reachable from the lessons alone (for Juanjo)

The C2 lessons are thinner than the quotas assumed. Writers stopped on capacity: I.1 78 of 110, I.2 87 of 127,
I.4 82 of 88, **I.5 66 of 164** (98 short; the lesson's sentences run out after the 30 kept candidates). Only I.3 had
more facts than its quota. If I.6–I.12, I.15 and I.16 run the same way, bloque I ends a few hundred below 2,582 and
may fall under its 50 % share (2,500 of 5,000). Levers, none applied yet (rule 2d: say so and move on):
(a) the 160 or so held, style-checked C1-derived I.13/I.14 candidates not chosen (mix and bias permitting; tilts the
tema weights); (b) a C2 lesson round adding facts (with `provenance.py record`); (c) a smaller bank total. To size
at the end of the bloque, before the build.

- **I.6 mix residual:** the lesson's facts are mostly the Plan de Gobierno Abierto, ODS and Agenda 2030 (saved
  pages, no article), so art-completar cannot reach 41 % (article share 23 % against 69). Before the bias holds the
  edge z was +2.75; `rebalance.py --apply` held q066, q077, q079 (worst |z| 1.42). Holding the 5 remaining surplus
  would not bring the mix within ±10. For Juanjo: accept, or have the bank lean on I.6's article questions elsewhere.
- **I.6 verifier notes:** `transparencia-v-plan.html`'s HTML title says 2024-2028, its body 2025-2029 (q069 offers
  neither as a trap); Resolución 70/1 named without date in four stems (q092, q097, q098, q115), passed on item 10.

- **I.7, item 10 (20 drops):** stems naming «Ley 19/2013, de 9 de diciembre» without its BOE title, where the
  title fits within 40 words. The guide's item 10 and the C1 ruling (number and date only when the title would pass
  40 words) agree; the step-2 style brief's looser line («number and date alone pass») was never needed for I.7's
  derived set (none of its kept derived stems does it). Drops upheld; r1 re-asks those facts with the title.
- **I.7 q086 and the lesson (open, for Juanjo / a C2 lesson round):** art. 16 Ley 19/2013 reads «deberá indicarse al
  solicitante que parte de la información ha sido omitida» (no accent). The verifier reads «que» as a conjunction
  (tell the applicant *that* part was omitted) and failed the key «Qué parte…»; the lesson (m01-l07.md line 127) says
  «se le indica qué parte se ha omitido». Common usage reads «qué»; the BOE text has no accent. Not changed here.

- **I.8:** writer stopped on capacity at 135 of 161. Verifier notes: the 14 RD 829/2023 ministry-name questions
  (q083–q089, q111–q117) share three stems word for word (no checklist item; first to hold if I.8 runs over);
  q179 names a second norm («la Ley 2/2014») by number inside a stem whose cited norm has its full title (passed).
- **I.4 edge z −1.82** after r1 (under quota: residual).

- **I.10, citation index gap (open):** the lesson's seat table cites «Protocolo n.º 6» with no article; no citation
  form resolves to an anchor, so the writer left out four seat questions (kept q013 covers the Consejo's seat). Fix:
  an index unit for the Protocol, or a lesson citation the index resolves (C2 lesson round).
- **Written, verifying:** I.5 r1 4 (q111–q114, none skipped); I.9 49 (q107–q155; sheet 34, coverage of untested
  facts took it over); I.10 80 (q055–q134; capacity: sheet 114).

- **I.9 q114 dropped by the coordinator** (verifier passed it with a note): «¿Cuál … pueden» does not agree, and the
  comma clause calls all four options art. 148.1 matters though three are art. 149.1. q146/q147 failed on option form
  (the q065 ruling extended: a key alone in another construction gives itself away).

- **I.10 q088 dropped by the coordinator** (verifier passed it with a note): the stem gives the Polonia–Dinamarca–
  Chipre trio (Jan 2025–Jun 2026) in the present tense; the saved page names the current trio (item 15). Passed on
  item 10 with a note: «Reglamento interno del Consejo, aprobado por la Decisión 2009/937/UE» (q065, q081, q085,
  q086), the short name official 2022 P1-2 uses.

- **I.15:** 161 kept, 6 over; its derived set was off the mix (cual 10/22, art-pregunta 17/6, norma-pregunta
  18/6) and edge z +1.67. A greedy hold of the 6 surplus with `select_derived.py`'s penalty (q004, q015, q016, q027,
  q040, q048: «mix and bias rebalance» in `held.tsv`) leaves only cual off (10/22); 6 cual-form questions written
  (`m01-l15.authored-mix`): 6 PASS; the coordinator dropped q195, whose key names «el artículo 29» (no article
  numbers in options). Verifier note: the lesson cites arts. 28.1 and 36.3 but does not state q192's and q195's facts.
- **I.16:** capacity (writer 65 of 122). q103 failed check 5 (same stem, three of 2025-R1-1's options, other key).
  The coordinator dropped q099 and q100 on the same ground (the verifier passed them, keys differ, three and two
  of 2025-R1-1's options carried). I.16 edge z +1.63, just over ±1.5, under quota: residual.

- **I.7 holds:** `rebalance.py --apply` held q081, q091, q122, q131 (bias), then a greedy mix-and-bias hold of the last 3
  surplus (q002, q007, q014). Edge z 2.61 → 1.26; art-completar 52 % (one point over ±10), residual.
- **I.11:** its derived set (239 of 288) is off on cual and directa and the edge z is +3.09; it sits 2 under quota, so
  nothing can be held. r1 (9 replacements) written in cual form with mid-length keys, to verify.
- **m01-l10 lesson line 119 (open, C2 lesson round):** «a fecha de 06-11-2026» names Polonia, Dinamarca y Chipre as
  the trío; the saved `consilium-presidencia.html` gives Irlanda, Lituania y Grecia (verifier, `verify/m01-l10.r1.v1`).
- **I.10 r1:** q135 (explanation says non-legislative deliberations are never public; art. 8 Reglamento interno
  makes some public) and q136 (official 2020X-P1-11 copy) dropped; q137, q138 kept.

- **I.11 final:** r1 9/9 PASS (all cual form, keys mid-length); the 7 surplus held by the mix-and-bias greedy
  (q068, q104, q358, q364, q383, q389, q396): edge z 2.80 → 1.34; directa 14 % (one point over), residual.
- **I.16 final:** r1 6/8 (q123: all four options of the official classification question; q125: key rests on art. 9.3
  Ley 4/2023, citation names only art. 20.2 RD 829/2023); q103 and q114 not replaced (no clean angle). Kept q062
  dropped by the coordinator on q123's ground (same four options as 2025-P1-30). Edge z +1.86, under quota: residual.

## Replacements (r1) (done)

- I.1 r1: 10 (q109–q118) for 11 drops; q087 skipped (its key needs art. 161.1.a, not cited by the I.1 lesson).
- I.2 r1: 12 (q160–q171) for 14 drops; q102 (needs art. 35.3 LOTC) and q109 (needs art. 87 CE) skipped, not cited.
- Verified: I.1 r1 8/10, I.2 r1 11/12. **I.1 edge z −2.59 stays a residual** (under quota, nothing to hold; the r1
  writer was told to leave short keys short and long ones long, and the z still moved the wrong way: bloque II's
  finding that key length cannot be steered in writing holds). Within the course limit ±3.
- `tools/verify_batches.py` now names replacement batches `<lesson>.r1.v<k>` (it had overwritten `m01-l01.v1.ids`
  and `m01-l02.v1.ids`; regenerated identically from the first drafts).

## Bloque I after verification (2026-11-10)

**2,312 kept of 2,582** (1,361 derived from C1 with provenance + 951 authored and verified blind; `tools/tema_status.py
bloque-i`). Over or at quota: I.3, I.6, I.7, I.9, I.11, I.12, I.13, I.14, I.15. Short on lesson capacity: I.1 −35,
I.2 −43, I.4 −6, I.5 −98, I.8 −26, I.10 −36, I.16 −62. Below the plan's 50 % share (2,500 of 5,000) by 188.
**Residuals:** edge z I.1 −2.59, I.4 −1.82, I.16 +1.86 (under quota, nothing to hold; within the course limit ±3);
mix I.6 (art-completar 15/41, señale 26/12: the lesson has few articles), I.7 art-completar 52/41, I.11 directa
14/3 (one point over each). «Lo que más cae»: every line covered per the writers' notes for the authored temas; I.13
and I.14 (derived only) not yet mapped — to check at the build.

**Decision for Juanjo before the build (bloque I is 270 short):** (a) fill from the 275 held, style-checked C1
candidates of I.13 (161) and I.14 (114), with `select_derived.py` for mix and bias, at the cost of tema weights
(I.13 up to ~366 against 205); (b) a C2 lesson round adding facts to I.5, I.16, I.2, I.10, I.1, I.8, then a writing
round; (c) a smaller bank (5,000 − 270), keeping bloque I at its current share (2,312 of 4,730 = 48.9 %, under 50 %).
## Ten random bloque I questions (seed 20261110, from the 2312 kept)

1. **m01-l03-q081** (I.3, authored) — ¿Cuál de los siguientes colectivos reúne a los electores y elegibles para el Congreso de los Diputados, según la Constitución Española de 1978?
   - a) Todos los españoles mayores de edad, sin más requisito.
   - b) Todos los españoles residentes en España en pleno uso de sus derechos civiles.
   - c) Todos los españoles que estén en pleno uso de sus derechos políticos.  ✓
   - d) Todos los ciudadanos de la Unión Europea residentes en España.
   Cita: art. 68.5 CE. Explicación: El artículo 68.5 exige ser español y estar en pleno uso de los derechos políticos. La mayoría de edad, la residencia y los derechos civiles son otros requisitos que el artículo no pone. Los ciudadanos de la Unión Europea no son titulares del sufragio para el Congreso: el artículo 13.2 solo admite el sufragio de los extranjeros en elecciones municipales, por tratado o ley.

2. **m01-l08-q093** (I.8, authored) — ¿Cuál de las siguientes funciones corresponde a los servicios comunes de los Ministerios, según el artículo 68.1 de la Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público?
   - a) Ejercer la potestad reglamentaria en las materias propias del Departamento.
   - b) Imponer la sanción de separación del servicio por faltas muy graves.
   - c) Prestar asesoramiento y apoyo técnico en materia de asistencia jurídica.  ✓
   - d) Declarar la lesividad de los actos administrativos.
   Cita: art. 68.1 LRJSP. Explicación: El artículo 68.1 incluye la asistencia jurídica entre las funciones de los servicios comunes, junto con la planificación, los recursos humanos o las publicaciones. La potestad reglamentaria, la separación del servicio y la declaración de lesividad son funciones de los Ministros según el artículo 61.

3. **m01-l12-q016** (I.12, derived from C1 m02-l04-q019) — De acuerdo con el artículo 13.3 de la Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales, se podrá considerar repetitivo el ejercicio del derecho de acceso:
   - a) En más de una ocasión durante el plazo de seis meses, salvo causa legítima para ello.  ✓
   - b) En más de una ocasión durante el plazo de un año, salvo causa legítima para ello.
   - c) En más de dos ocasiones durante el plazo de seis meses, salvo causa legítima para ello.
   - d) En más de una ocasión durante el plazo de tres meses, aunque exista causa legítima.
   Cita: art. 13.3 LOPDGDD. Explicación: El artículo 13.3 permite considerar repetitivo el acceso «en más de una ocasión durante el plazo de seis meses, a menos que exista causa legítima para ello». El periodo no es de un año ni de tres meses. Basta más de una ocasión, no más de dos. La causa legítima impide calificarlo de repetitivo.

4. **m01-l13-q002** (I.13, derived from C1 m04-l01-q002) — Según el artículo 8.2 del texto refundido de la Ley del Estatuto Básico del Empleado Público, los empleados públicos se clasifican en:
   - a) Funcionarios de carrera, funcionarios interinos, personal laboral y personal directivo.
   - b) Funcionarios de carrera, funcionarios en prácticas, personal laboral y personal eventual.
   - c) Funcionarios de carrera, personal laboral, personal eventual y personal directivo profesional.
   - d) Funcionarios de carrera, funcionarios interinos, personal laboral y personal eventual.  ✓
   Cita: art. 8.2 TREBEP. Explicación: El artículo 8.2 enumera cuatro clases: funcionarios de carrera, funcionarios interinos, personal laboral y personal eventual. El personal directivo no es una clase de esa lista; el Estatuto lo regula aparte, en su artículo 13. Los funcionarios en prácticas tampoco figuran en la lista del artículo 8.2. La lista que suprime a los interinos y añade el personal directivo profesional altera dos elementos.

5. **m01-l13-q381** (I.13, derived from C1 m04-l05-q039) — Según el artículo 58.2 del Real Decreto 364/1995, de 10 de marzo, el requisito de que el puesto atribuido al funcionario cesado en libre designación esté en el mismo municipio solo se exceptúa:
   - a) cuando el funcionario lo pida por razones de convivencia familiar.
   - b) cuando en el municipio no haya un puesto vacante de su Cuerpo o Escala.
   - c) cuando se trate del cese de funcionarios destinados en el exterior.  ✓
   - d) cuando el cese se deba a la supresión del puesto en la relación.
   Cita: art. 58.2 RD 364/1995. Explicación: El artículo 58.2 RD 364/1995 dice que «la necesidad de que el nuevo puesto que se atribuye al funcionario sea en el mismo municipio no será de aplicación cuando se trate del cese de funcionarios destinados en el exterior». Es la única excepción. El artículo no la extiende a la petición por convivencia familiar, a la falta de vacantes en el municipio ni a la supresión del puesto.

6. **m01-l15-q071** (I.15, derived from C1 m05-l02-q303) — Conforme al artículo 40.1.c) de la Ley 47/2003, de 26 de noviembre, General Presupuestaria, en los créditos para operaciones de capital se distinguirán:
   - a) las inversiones reales y los activos financieros.
   - b) las inversiones reales y las transferencias de capital.  ✓
   - c) los gastos financieros y las transferencias de capital.
   - d) las transferencias de capital y los pasivos financieros.
   Cita: art. 40.1.c) LGP. Explicación: Las operaciones de capital comprenden las inversiones reales y las transferencias de capital, los capítulos 6 y 7. Los activos y los pasivos financieros son las operaciones financieras, y los gastos financieros son operaciones corrientes.

7. **m01-l15-q168** (I.15, derived from C1 sp-15/q20) — ¿Puede la Jefatura dotar otro programa del mismo servicio con 50.000 euros del crédito del capítulo 2 suplementado en febrero, mediante una transferencia de crédito?
   - a) Sí, si el titular del Ministerio del Interior la autoriza previo informe favorable de la Intervención Delegada.
   - b) Sí, porque la restricción de las transferencias solo afecta a los créditos de distintas secciones presupuestarias.
   - c) Sí, si la persona titular de la Dirección del organismo la autoriza dentro de su presupuesto, sin otros requisitos.
   - d) No, porque las transferencias de crédito no pueden minorar créditos suplementados en el ejercicio.  ✓
   Cita: art. 52.1 LGP. Explicación: Las transferencias de crédito no pueden minorar créditos extraordinarios ni créditos que se hayan suplementado o ampliado en el ejercicio (art. 52.1.c) LGP). El capítulo 2 de la Jefatura recibió un suplemento de 200.000 euros en febrero, así que no puede dotar con él a otro programa. Que el titular del Ministerio, con informe de la Intervención Delegada, o la Dirección del organismo en su presupuesto autoricen ciertas transferencias, regula quién las autoriza y no levanta la restricción. La restricción tampoco se limita a las secciones distintas, que es otra regla de la misma lista.

8. **m01-l16-q036** (I.16, derived from C1 m03-l07-q039) — ¿Cuánto dura, según la Ley 15/2022, de 12 de julio, integral para la igualdad de trato y la no discriminación, el mandato de quien preside la Autoridad Independiente para la Igualdad de Trato y la No Discriminación?
   - a) Cinco años, renovable una sola vez por otros cinco
   - b) Cinco años, sin posibilidad de renovación  ✓
   - c) Seis años, sin posibilidad de renovación
   - d) Cuatro años, renovable por una sola vez
   Cita: art. 41.4 Ley 15/2022. Explicación: El artículo 41.4 dice: «Su mandato será de cinco años sin posibilidad de renovación». El mandato de cinco años no admite renovación. Seis y cuatro años no son la duración que fija la ley.

9. **m01-l16-q039** (I.16, derived from C1 m03-l07-q042) — ¿Cómo define la Ley 4/2023, de 28 de febrero, para la igualdad real y efectiva de las personas trans y para la garantía de los derechos de las personas LGTBI a la persona trans?
   - a) Persona que ha obtenido la rectificación registral de la mención relativa al sexo
   - b) Persona cuya identidad sexual no se corresponde con el sexo asignado al nacer  ✓
   - c) Persona cuya expresión de género no coincide con los roles sociales de su sexo
   - d) Persona nacida con características sexuales que no encajan en las nociones binarias
   Cita: art. 3.k) Ley 4/2023. Explicación: El artículo 3.k) define a la persona trans como aquella «cuya identidad sexual no se corresponde con el sexo asignado al nacer». La ley no exige haber rectificado la mención registral para ser persona trans. La expresión de género es la manifestación que cada persona hace de su identidad sexual (art. 3.j). Las características sexuales que no encajan en las nociones de cuerpo masculino o femenino describen la intersexualidad (art. 3.g).

10. **m01-l16-q097** (I.16, authored) — ¿Cuál de las siguientes conductas es infracción grave según el artículo 95.3 del Real Decreto Legislativo 1/2013, de 29 de noviembre?
   - a) Las vejaciones que padezcan las personas en sus derechos fundamentales por razón de su discapacidad.
   - b) Las acciones que deliberadamente generen un grave perjuicio económico o profesional.
   - c) La coacción, amenaza o represalia contra quien haya entablado o pretenda entablar una acción legal o reclamación para exigir la igualdad de oportunidades.  ✓
   - d) Conculcar deliberadamente la dignidad de las personas con discapacidad imponiendo condiciones o cargas humillantes para el acceso a los bienes, productos y servicios a disposición del público.
   Cita: art. 95.3 RDL 1/2013. Explicación: La coacción, amenaza o represalia contra quien reclama la igualdad de oportunidades es infracción grave según el artículo 95.3.h). Las vejaciones, el grave perjuicio económico o profesional deliberado y las situaciones de riesgo o grave daño deliberadas son muy graves en el artículo 95.4.

## Session 2 summary (2026-11-10)

1. Bloque II excerpts: 1,297 of 1,320 derived excerpts byte-identical to C1's (inherit its check); 23 differ (C1
   «sin extracto»). 158 checked blind (Opus): 47 right as built, 81 re-cited, 30 none.
2. Re-cited: 3 labels fixed by the coordinator (citation grammar «;»), 3 to «sin extracto»; blind recheck 73/78.
3. Bloque II: 120 of 158 with a checked excerpt, 38 «sin extracto» in the new `excerpt-exclusions.yaml`; rebuilt
   (81 citation lines changed, nothing else). Authored bloque II ordinary excerpts still unchecked (plan § 7).
4. +66 of bloque I to I.13 (205) and I.14 (229) from held C1 candidates; 283 held never style-checked found and
   checked (250 PASS, 33 FAIL).
5. I.13/I.14 chosen from the derived pool for mix and bias (`select_derived.py`): no authoring needed.
6. Bloque I written (Sonnet) tema by tema: 1,003 first drafts + 84 replacements and mix questions.
7. All verified blind (Opus, ≤ 60 per batch by cited unit): reports `bloque-i/verify/`, drops in `drops.tsv`.
8. Commonest drops: official copies with a distractor carried over, options off the stem's grammar, absurd
   distractors, keys resting on an uncited article, explanations misdescribing a distractor, item 10 (I.7).
9. Coordinator drops on verifier notes: I.9 q114, I.10 q088, I.15 q195, I.16 q062, q099, q100.
10. Capacity: most bloque I lessons hold fewer facts than their quotas; writers stopped rather than repeat.
11. Bias/mix: surplus held where it fixes a tema (I.6, I.7, I.11, I.15); residuals listed above.
12. Lesson issues found (not changed): m01-l07 line 127 «qué/que parte»; m01-l10 line 119 stale trío;
    m01-l10 «Protocolo n.º 6» has no index anchor.
13. New tools: `excerpt_inherit.py`, `excerpt_batches.py`, `apply_excerpt_reports.py`, `select_derived.py`,
    `verify_batches.py`, `tema_status.py`.
14. Nothing committed. Bloque I not built; suites not run (bloque II rebuild changed only citations and excerpts).

## Where to resume (after session 2)

1. Juanjo's decision on the bloque I gap (a/b/c above). For (a): run `select_derived.py` per lesson with the held
   pool and raised targets, then `tema_status.py`.
2. Bloque I build: `tools/build_exercises.py bloque-i m01` (from `backend/`), course.yaml entries, loader,
   cross-reference, `bias_per_tema.py bloque-i`, course-level bias test, i18n.
3. Excerpts: `scripts/extract_excerpts.py --course age-auxiliar-c2`; `excerpt_inherit.py bloque-i`; blind check
   (Opus, `excerpts/spec.md`) of every authored bloque I excerpt and every derived one not identical to C1's; apply
   with `apply_excerpt_reports.py bloque-i`, recheck re-cited (`excerpts/recheck-spec.md`).
4. «Lo que más cae» map for I.13 and I.14 (derived only). Goldens read; C1, crypto-futures, Android unchanged;
   `docs/age-verification/c2/tools/close_round.sh`.
5. Owed: blind check of authored bloque II ordinary excerpts; calibration items (34) after bloque I.
6. Do not rerun `plan_delta.py` on bloque I lessons: it would undo `select_derived.py` and the rebalance holds.

# Session 3 (2026-11-10): Juanjo's decisions, lesson fixes, excerpts, bloque I built

**Decisions (Juanjo):** build bloque I at 2,312 (gap per tema in plan § 6, variant rounds close it); fix the three
lesson problems first; blind-check the 1,064 authored bloque II excerpts now; leave the I.1/I.4/I.16 edge z and the
I.6 mix as recorded residuals.

## Lesson fixes (R2 rules)

- **m01-l07 line 126:** «Al solicitante se le indica que se ha omitido parte de la información (art. 16 Ley
  19/2013)», as art. 16 reads («que parte», a conjunction). No kept question rested on «qué parte» (q086 was dropped).
- **m01-l10 line 119:** the trío per the Decisión 2016/1316 table: Irlanda (julio-diciembre de 2026), Lituania
  (enero-junio de 2027), Grecia (julio-diciembre de 2027), as the saved consilium page presents them; holds on any
  exam date through 31-12-2027.
- **m01-l10 line 30, «Protocolo n.º 6»:** cited «(art. único Protocolo n.º 6)». Platform: the citation grammar and
  the source indexer learnt the «art. único» unit (`grammar.py`, `sources.py`; two tests in `test_citations.py`,
  failing first). New `normativa.yaml` entry «Protocolo n.º 6» on the consolidated TUE file, whose first «Artículo
  único» is the Protocol's (page 96). C2 `source-index.json` regenerated (C1's untouched); `citations.es.txt` golden
  +1 citation, +1 anchor. C1's lesson has the same sentence and gap, unchanged.
- Blind check (Opus): 11 sentences PASS (`docs/age-verification/c2/bloque-i/verify/m01-l07.r3-2026-11-10.md`,
  `m01-l10.r3-2026-11-10.md`). Records: `provenance.py record m01-l07 m01-l07` (144 inherited, 14 verified),
  `record m01-l10 m01-l11` (157 inherited, 32 verified). `test_provenance.py` 41 passed.

## Bloque II authored excerpts (953 not already in the 158)

`excerpts/bloque-ii/authored/batch-01..16`, Opus, `excerpts/spec.md`: **813 yes**, 110 labels, 30 none. 11 labels
were for norm citations (II.1–II.4: a sentence beyond the article's cut, a preámbulo paragraph, and three on RD
366/2007 art. 13.1 whose fact is the wording in force until 01-01-2027 while the excerpt shows the RD 707/2026 text):
«sin extracto». 99 re-cited, all resolving; blind recheck (`recheck2/`) 97 yes, 2 no (m02-l09-q230, m02-l11-q179):
«sin extracto». **Bloque II now: 2,384 questions; 2,303 with a checked or inherited excerpt; 81 «sin extracto»
with a reason; 0 unexplained.** Re-citations: `excerpts/bloque-ii-recited.tsv` (177 rows over both passes).
- **RD 366/2007 art. 13.1 (m02-l01-q075, q076, q100):** they tested the wording in force until 01-01-2027;
  resolved in session 4 (below).

## Bloque I built and its excerpts

- `build_exercises.py bloque-i m01`: **2,312 questions in 141 exercises**, one provenance record each. The builder
  empties the bloque's exercise files before writing: a failed run (a citation that resolves to no lesson anchor)
  leaves none until a clean rerun.
- Excerpts: 1,353 derived identical to C1's (inherit; 10 of them C1's own «sin extracto»). 959 checked blind
  (`excerpts/bloque-i/batch-01..16`, spec's new «Norm citations» section: a miss gets «cite:» or «none»): **888
  yes**, 10 fixes, 61 none. Six «none» the verifiers gave only because the spec then barred letter citations were
  re-cited by the coordinator to the letter (`coordinator-letters.md`: art. 2.2.k) and l) Ley 50/1997, 8.1.g) and h)
  Ley 19/2013, 19.1.f) LJCA, 95.3.h) RDL 1/2013). Two «disposición derogatoria CE» cites resolve to no lesson
  anchor and two OECD labels split over PDF lines: «sin extracto». Blind recheck of the 12 re-cited: 12 yes.
  **Bloque I: 2,243 with a checked or inherited excerpt, 69 «sin extracto»** (59 from this check, 10 inherited from C1; most: ODS short names only in box
  titles, chapter/section questions whose answer is a heading, letters past the cut where the citation has no
  letter).
- Extractor notes (not content faults): m01-l06-q069's excerpt runs into the page footer; m01-l06-q092 reads «pa
  ra»; bloque II recheck flags garbled menu paths copied from the pages.
- Course: **4,696 questions, 4,546 excerpts, 150 «sin extracto»** (140 in `excerpt-exclusions.yaml`, 10 inherited).
- Bias: `test_quiz_answer_bias.py` 27 passed (course level, C2 included). Per tema as in the bloque I table.

## close_round.sh (2026-11-10)

- Goldens: `citations.es.txt` +1 citation, +1 anchor (Protocolo n.º 6, art. único, page 96), read. C1 and
  crypto-futures: no path changed. Android bundle re-exported: byte-identical to `dist/bundle`.
- Backend: 2,952 passed, 23 skipped, 1 failed: `test_question_identity` for C2, the expected «regenerate and
  review» after adding bloque I. Regenerated (`UPDATE_QUESTION_KEYS=1`) and reviewed: 2,312 bloque I keys added, no
  bloque II key removed or changed. Test then 6 passed.
- Frontend: 723 passed, 81 skipped; `tsc -b` clean.
- README (C2 section: bank sizes, «sin extracto», `art. único`) and `content/README.md` (the `art. único` form) updated.

## Where to resume (after session 3)

R3 is done for bloques I and II. Nothing committed. Next:
1. Calibration items (34), plan § 1, after bloque I (platform side checked then).
2. R5 (variant rounds): close bloque I's gap per plan § 6 (I.5 −98, I.16 −62, I.2 −43, I.10 −36, I.1 −35, I.8 −26,
   I.4 −6); rebalance the edge z of I.1, I.4, I.16 and the I.6 mix.
3. C1 carries the same «Protocolo n.º 6» sentence without an anchor and the same «qué parte» sentence; a C1 round
   can now cite «art. único Protocolo n.º 6» (C1 provenance and C2 records follow the CLAUDE.md rule).
4. Do not rerun `plan_delta.py` on bloque I lessons (it would undo `select_derived.py` and the rebalance holds).

# Session 4 (2026-11-11): cambio-pendiente questions

**Juanjo:** the exam falls after 01-01-2027 (R3.5: the version in force on the exam date). m02-l01-q075, q076 and
q100 tested art. 13.1 RD 366/2007 as in force until then: dropped (`bloque-ii/drops.tsv`), replaced on the RD
707/2026 wording. The lesson already states the new wording («art. 13.1 RD 366/2007, desde 02-01-2027», art. 10.2.a)
of the Reglamento): no lesson change.

- **Replacements:** m02-l01-q101 (the decree that approves the Reglamento), q102 (the documents art. 13.1 covers),
  q103 (the art. 10.2.a) obligation lectura fácil serves). Written (Sonnet), verified blind 3/3 PASS
  (`bloque-ii/verify/m02-l01.r3.v1.md`), excerpts checked blind 3/3 yes (`excerpts/bloque-ii/r3/report-01.md`).
  II.1 stays at 82; mix and bias within bounds.
- **Bank-wide scan** of every built question's citation against `normativa.yaml`'s `cambios_pendientes` in force
  before the exam (RD 366/2007 art. 13, 02-01-2027; Reglamento del Congreso art. 23, XVI legislatura from
  23-12-2026; RDL 4/2000 art. 19.1 and LGSS arts. 144.4, 169.1.a), 171, 172, 173.1, 01-12-2026; LGSS art. 309.1,
  01-01-2027): **11 questions** cite an affected article (no question cites the LGSS ones). Each was checked blind
  against the wording in force from 02-01-2027 (`bank/pending-changes-check-2026-11-11.md`): **3 changed** (the three
  above) and **8 hold** (m02-l01-q077, q078, q079, q090; m01-l03-q050, q051, both already on the reformed art. 23.1;
  m01-l14-q295, q296, on parts of art. 19 RDL 31/2026 leaves as they are). So the count of questions treated is 3.
- Question keys regenerated: 3 removed, 3 added, nothing else moved.
- `close_round.sh` (2026-11-11), exit 0: goldens as in session 3 (the Protocolo n.º 6 anchor, read); C1 and
  crypto-futures untouched; Android bundle byte-identical; backend 2,953 passed, 23 skipped; frontend 723 passed,
  81 skipped; `tsc -b` clean. Nothing committed.
