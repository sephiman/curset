# C2 round R2, bloque II — writer and verifier spec

2026-11-06. Course `age-auxiliar-c2`, bloque II (temas II.1–II.12, lessons `m02-l01` … `m02-l12`). Theory only.

Everything in `docs/age-verification/c2/bloque-i/spec.md` applies (read it first: depth, provenance, verbatim facts,
conventions, verifier table shape, coverage format) except where this file says otherwise. Paths below: `B2` =
`docs/age-verification/c2/bloque-ii/`.

## Mapping: C2 tema → C1 source lessons (`content/age-administrativo-c1/es/lessons/`)

| C2 | Programme (short) | C1 lessons | Kind |
|---|---|---|---|
| II.1 `m02-l01` | Atención al público: acogida e información; personas con discapacidad | m02-l01 (atención, acogida, discapacidad) | norm-based |
| II.2 `m02-l02` | Servicios de información administrativa; información general y particular; iniciativas, reclamaciones, quejas, peticiones | m02-l01 (servicios de información, quejas y sugerencias), plus derecho de petición where a pack question asks | norm-based |
| II.3 `m02-l03` | Documento, registro y archivo | m02-l02 | norm-based |
| II.4 `m02-l04` | Administración electrónica; páginas web públicas; oficinas integradas; ventanilla única; PAG | m02-l03 | norm-based |
| II.5 `m02-l05` | Informática básica: hardware, software, almacenamiento, sistemas operativos, seguridad | m06-l01 | list |
| II.6 `m02-l06` | Windows: entorno gráfico, escritorio, menú Inicio, Copilot | m06-l02 | list |
| II.7 `m02-l07` | Explorador, carpetas y archivos, búsqueda, Este equipo, Acceso rápido, accesorios, herramientas del sistema | m06-l03 | list |
| II.8 `m02-l08` | Word 365 | m06-l04 | list |
| II.9 `m02-l09` | Excel 365 | m06-l05 | list |
| II.10 `m02-l10` | Access 365 | m06-l06 | list |
| II.11 `m02-l11` | Outlook 365 | m06-l07 | list |
| II.12 `m02-l12` | Internet: protocolos, servicios, navegadores | m06-l08 | list |

Question packs: `B2/questions/<lesson>.md` (built by `B2/tools/question_packs.py`, same columns as bloque I).

## Norm-based temas (II.1–II.4)

The bloque I method, unchanged: C2 depth, kept C1 sentences byte-identical, new text from
`content/age-auxiliar-c2/sources/normativa/`, ten «Lo que más cae» lines, «Normativa» block. Cambio pendiente: RD 366/2007
art. 13 (RD 707/2026, en vigor el 02-01-2027) is in `normativa.yaml`; it falls before the exam date only if the exam is
after 02-01-2027 — write the precept in force today and add the «Cambio pendiente» line, as `normativa.yaml` describes.
Pages of `sources/otros/` (Portal de la Administración, PAE, Cl@ve…) are cited «(fuente: `file`)».

## Ofimática temas (II.5–II.12): list-shaped

The C1 bloque VI rules apply: read `docs/age-verification/bloque-vi/spec.md`, sections «Sources (hard rules)», «Scope» and
«The lesson» items 2–10, with these changes:

- **Derive item by item from the C1 lesson.** Keep a C1 item byte-identical (whole list item, citation included) when C2
  needs it: it then inherits C1's verification. Cut items C2's programme does not name and no Auxiliar exam asked (index
  below). Write new items only where the C2 programme names a feature or an Auxiliar question asks something the C1
  lesson lacks.
- **Coverage map:** `docs/age-c2-ofimatica-index.md` (C2's own index, not C1's): read section 2 for this lesson's
  application, sections 3 (recurring families), 4 (single-convocatoria), 5 (programme features asked and never asked)
  and 6 (retired features, changed labels, version-dependent questions) for this tema. Every recurring family with its
  asked facts; every programme feature at least once.
- **Sources:** only the saved official pages in `content/age-auxiliar-c2/sources/otros/` (C1's pages are copied there
  with the same sha256). A new page: fetch it (curl with a browser user agent; if refused, the Playwright Chromium of
  the e2e suite as in `docs/age-verification/tools/fetch_rendered.mjs`), save it under `sources/otros/` with C1's
  naming scheme, and record it in `B2/writer/<lesson>-fuentes.yaml` (fields of `fuentes.yaml`: file, url, title,
  consultado, sha256, origen «descarga nueva», lessons). Never edit `fuentes.yaml` yourself; the coordinator merges.
- **Citation form:** «(fuente: `file`)» as in C1, or «(fuente: `file`; <label or heading on the page>)» when the page has
  several sections. Spanish-locale labels. Retired features are not described (one line with the replacement, sourced,
  if the programme names one). A disputed point (index section 6, or two pages that disagree) is stated with both
  sources, never resolved by guess.
- **Versions:** Windows 11 and Microsoft 365 desktop (Anexo I 2.2). Outlook: say «Outlook clásico» / «nuevo Outlook»
  when they differ.
- **No word ceiling** (R4.1/R4.3): completeness over length; nothing an official Auxiliar question asked is cut.
- **«Lo que más cae»:** ten lines, facts the Auxiliar exams asked for this tema (coverage questions first).
- **«Fuentes»** replaces «Normativa» (last section), C1's form, one line per page cited. The stub's «Normativa» section
  («Este tema no se apoya en ninguna norma.») is replaced by it.

## Writer's notes (`B2/writer/<lesson>.md`)

As bloque I (sections kept/cut/new, pack questions → section, «Lo que más cae» → questions, new sentences/items →
source, summary proposal, glossary ids from C1's glossary, ambiguities), plus for ofimática: the index rows of this tema
→ item; programme phrases → item; labels not confirmed; retired features named.

## Verifier

As bloque I (blind, PASS/FAIL per pending id, same table shape; output `B2/verify/<lesson>.md`). For ofimática items:
open the cited saved page and check every field the item states (label, path, shortcut, behaviour, default) is
literally on the page (Windows desktop section for shortcuts); for a new page, check sha256 and URL against its
`-fuentes.yaml` fragment and that the page is the article in Spanish. The «Fuentes» line passes when it lists exactly the
files the lesson cites.

## Coverage check

As bloque I, output `B2/coverage/<lesson>.md`. For ofimática temas also: each recurring family of the index for this
tema → item, and each programme feature → item.
