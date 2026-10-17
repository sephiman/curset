# R2b fixes — bloque I (m01-l01 … m01-l11)

Writer, 2026-10-17, to `spec.md` (this folder). Inputs: `coverage/m01.md`, `coverage/m01-l01.md` … `m01-l11.md`,
`scope/m01.md`, the bloque I section of `docs/age-theory-ledger.md` (lines 1–900), the questionnaires and keys in
`SP/exams/`, `docs/age-official-exams-ledger.md` for tema and estado. Sources read with `pdftotext -layout` from
`content/age-administrativo-c1/sources/normativa/`. Nothing committed. Lessons m01-l04, m01-l05, m01-l08, m01-l09 and
m01-l10: no change.

## m01-l01

1. **coverage** — section «Estructura» (after the table of títulos). Exam row: conv2025_X P1 19 (I.1 o I.5), «Conforme
   al artículo 94.1 de la Constitución … requieren la autorización previa de Cortes Generales los tratados
   internacionales:», key d «Los tratados o convenios que exijan medidas legislativas para su ejecución»; checked in
   `2026-07-24_conv2025_extraordinario_cuestionario.txt`. The miss in `coverage/m01.md`.
   Old: (table followed directly by «### El título preliminar»). New, after the table:
   ```
   El capítulo tercero del título III trata de los tratados internacionales. La prestación del
   consentimiento del Estado para obligarse por tratados o convenios que supongan modificación o
   derogación de alguna ley o exijan medidas legislativas para su ejecución requiere la previa
   autorización de las Cortes Generales (art. 94.1.e CE). La lista completa del artículo 94.1 está en
   m01-l03, el tema de las Cortes Generales.
   ```
   Source (`BOE-A-1978-31229_ce_2026-05-20.pdf`): título III, «CAPÍTULO TERCERO De los Tratados Internacionales»;
   art. 94.1: «La prestación del consentimiento del Estado para obligarse por medio de tratados o convenios requerirá la
   previa autorización de las Cortes Generales, en los siguientes casos: […] e) Tratados o convenios que supongan
   modificación o derogación de alguna ley o exijan medidas legislativas para su ejecución.»
   Normativa: CE line «81, 87, 116» → «81, 87, 94.1, 116». «Lo que más cae»: unchanged (one question).

2. **note** — section «Las reformas» (kept by scope). Exam rows: conv2022 P1 26 «¿Cuántas veces se ha reformado la CE
   desde su aprobación en 1978?» (`conv2022_cuestionario.txt`); conv2020 P1 1 «¿La Constitución Española de 1978 (en
   adelante CE) ha sido reformada?» (`conv2020_cuestionario.txt`). Both `norma modificada: CE art. 49` in the ledger;
   they still ask the content of the section.
   Old: (heading followed directly by «La Constitución se ha reformado cuatro veces…»). New, right after the heading:
   ```
   :::note{type=info}
   Fuera del enunciado literal del programa; preguntado en la convocatoria 2022, primera parte, pregunta 26; la
   convocatoria de la OEP 2020 (examen de 2022), primera parte, pregunta 1.
   :::
   ```
   Normativa / «Lo que más cae»: unchanged.

## m01-l02

1. **pointer** — section «La reforma del título II» → m01-l01 (procedimiento agravado). Scope «Missing
   cross-references».
   Old: `La reforma se somete después a referéndum para su ratificación (art. 168 CE).`
   New: `La reforma se somete después a referéndum para su ratificación (art. 168 CE). El procedimiento agravado
   está en m01-l01, el tema de la Constitución.`
   Normativa / «Lo que más cae»: unchanged.

## m01-l03

1. **coverage** — section «Otras atribuciones». Exam row: conv2022 P1 15 (I.3 o V.2), «De acuerdo con la CE, las Leyes
   de Presupuestos Generales del Estado ¿pueden crear o modificar tributos?», key c «No podrán crearlos, pero podrán
   modificarlos si está así previsto en una ley tributaria sustantiva»; checked in `conv2022_cuestionario.txt`. The
   miss in `coverage/m01.md`.
2. **pointer** — same paragraph → m05-l01 for the budget. Scope «Missing cross-references».
   Old (changes 1 and 2 together):
   ```
   Las Cortes aprueban los Presupuestos del Estado y controlan la acción del Gobierno (art. 66.2 CE). La
   investidura, la moción de censura y la cuestión de confianza están en m01-l05, el tema del Gobierno.
   ```
   New:
   ```
   Las Cortes aprueban los Presupuestos del Estado y controlan la acción del Gobierno (art. 66.2 CE). La
   Ley de Presupuestos no puede crear tributos. Puede modificarlos cuando una ley tributaria sustantiva así
   lo prevea (art. 134.7 CE). La elaboración, el examen y la aprobación de los Presupuestos están en
   m05-l01, el tema del presupuesto. La investidura, la moción de censura y la cuestión de confianza están
   en m01-l05, el tema del Gobierno.
   ```
   Source (`BOE-A-1978-31229_ce_2026-05-20.pdf`), art. 134.7: «La Ley de Presupuestos no puede crear tributos. Podrá
   modificarlos cuando una ley tributaria sustantiva así lo prevea.»
   Normativa: CE line «(título III), 145.2» → «(título III), 134.7, 145.2». «Lo que más cae»: unchanged (one question).

## m01-l06

1. **note** — section «La Alianza para el Gobierno Abierto» (kept by scope). Exam row: conv2022_X P1 22 «¿Desde qué año
   España forma parte del Comité Directivo de la Alianza para el Gobierno Abierto (Open Government Partnership,
   OGP)?» (`conv2022_extraordinario_cuestionario.txt`; ledger `dudosa`).
   New, right after the heading:
   ```
   :::note{type=info}
   Fuera del enunciado literal del programa; preguntado en la convocatoria 2022 (llamamiento extraordinario), primera
   parte, pregunta 22.
   :::
   ```
2. **removal** — section «El Gobierno Abierto en España» (heading and body: the competence paragraph, the AGE organs
   Dirección General de Gobernanza Pública and Grupo interministerial, the Comisión Sectorial and the Foro de Gobierno
   Abierto). Deleted whole.
   - Its child «### Los planes de Gobierno Abierto» is kept by scope; with its parent gone it is promoted to «## Los
     planes de Gobierno Abierto», so it does not fall under «Principios informadores». Text unchanged.
   - The Foro de Gobierno Abierto is still named in «Los planes» (IV Plan «aprobó … en la sesión del pleno del Foro de
     Gobierno Abierto»; V Plan «El pleno del Foro de Gobierno Abierto lo aprobó») and in «Lo que más cae» (V Plan line).
     Both read correctly without the removed description: they name the organ that approved each plan. Not changed.
   - Normativa: the section cited only `transparencia-gobierno-abierto-que-es.html`, still cited by «El Gobierno
     Abierto: concepto», «La Alianza» and «El Objetivo 16». No change. «Lo que más cae»: no line rested on it.
   - Cross-references: `grep -rn` of the course finds no reference to the section (m03-l01 points to m01-l06 for the
     art. 133 LPAC trámites, which stay).
3. **note** — section «Los planes de Gobierno Abierto» (kept by scope). Exam rows: conv2024_A P1 8 (= B 6) «¿En cuántos
   ejes se articula el IV Plan de Gobierno Abierto en España?» (`conv2024_modeloA_cuestionario.txt`); conv2024_X P1
   reserva 1 «¿En qué fecha se aprobó del IV Plan de Gobierno Abierto en España?»
   (`conv2024_extraordinario_cuestionario.txt`, first «Preguntas de reserva» block); conv2022 P1 29 «En España, ¿qué
   plan de Gobierno Abierto está actualmente vigente y cuál es su plazo de vigencia?» (`conv2022_cuestionario.txt`).
   New, right after the (promoted) heading:
   ```
   :::note{type=info}
   Fuera del enunciado literal del programa; preguntado en la convocatoria 2024 (modelo A), primera parte, pregunta 8;
   la convocatoria 2024 (llamamiento extraordinario), primera parte, pregunta de reserva 1; la convocatoria 2022,
   primera parte, pregunta 29.
   :::
   ```

## m01-l07

1. **restore** — section «Control y Portal de la Transparencia», art. 11 Ley 19/2013 (I.7 cut list). Exam row:
   conv2020_X P1 5 (I.7, vigente, key a «Accesibilidad, Interoperabilidad y Reutilización»), «De acuerdo con el
   artículo 11 de la Ley 19/2013 … el Portal de la Transparencia contendrá información publicada de acuerdo con las
   prescripciones técnicas … que deberán adecuarse a los principios de:» (`conv2020_extraordinario_cuestionario.txt`).
   Old: `… Presidencia (art. 10.1 Ley 19/2013).`
   New:
   ```
   Presidencia (art. 10.1 Ley 19/2013). El Portal publica la información conforme a las prescripciones
   técnicas que se establezcan reglamentariamente. Esas prescripciones deben adecuarse a los principios de
   accesibilidad, interoperabilidad y reutilización (art. 11 Ley 19/2013).
   ```
   Source (`BOE-A-2013-12887_ley-transparencia_2022-07-09.pdf`), art. 11: «El Portal de la Transparencia contendrá
   información publicada de acuerdo con las prescripciones técnicas que se establezcan reglamentariamente que deberán
   adecuarse a los siguientes principios: a) Accesibilidad […] b) Interoperabilidad […] c) Reutilización […]»
2. **restore** — section «Tramitación», art. 19.1 Ley 19/2013 (I.7 cut list). Exam row: conv2020_X P1 7 (I.7, vigente,
   key d «La remitirá al competente, si lo conociera, e informará de esta circunstancia al solicitante»), «Según la Ley
   19/2013, cuando una solicitud de acceso a la información pública se refiere a información que no obre en poder del
   sujeto al que se dirige, este:» (`conv2020_extraordinario_cuestionario.txt`).
   New, first paragraph of the section:
   ```
   Si la solicitud se refiere a información que no obra en poder del sujeto al que se dirige, este la
   remite al competente, si lo conoce, e informa de ello al solicitante (art. 19.1 Ley 19/2013).
   ```
   Source, art. 19.1: «Si la solicitud se refiere a información que no obre en poder del sujeto al que se dirige, éste
   la remitirá al competente, si lo conociera, e informará de esta circunstancia al solicitante.»

   Normativa (both restores): Ley 19/2013 «arts. 1–3, 5–10, 12–20 y 22–40» → «arts. 1–3, 5–20 y 22–40».
   «Lo que más cae»: unchanged (each asked once, programa anterior).

## m01-l11

1. **note** — section «Las competencias de la Unión» (kept by scope; one note covers «Competencia exclusiva»,
   «Competencia compartida» and «Acciones de apoyo, coordinación o complemento»). Exam rows: conv2025_A P1 reserva 3
   (= B reserva 3) «Según el artículo 3 del Tratado de Funcionamiento de la Unión Europea, ¿en qué ámbitos la Unión
   Europea dispondrá de competencia exclusiva?» (`2026-05-23_conv2025_modeloA_cuestionario.txt`, first «Preguntas de
   reserva» block); conv2022 P1 reserva 1 «De conformidad con el artículo 4 del Tratado de Funcionamiento de la Unión
   Europea, ¿cuál de las siguientes es una competencia compartida…?» (`conv2022_cuestionario.txt`, first block; option
   a «La industria» needs art. 6 TFUE).
   New, right after the heading:
   ```
   :::note{type=info}
   Fuera del enunciado literal del programa; preguntado en la convocatoria 2025 (modelo A), primera parte, pregunta
   de reserva 3; la convocatoria 2022, primera parte, pregunta de reserva 1.
   :::
   ```
2. **note** — section «Ingreso y retirada» (kept by scope). Exam row: conv2025_X P1 12 «De acuerdo con el artículo 49
   del Tratatado de la Unión Europea, ¿quién se pronunciará sobre la solicitud de ingreso como miembro en la Unión
   Europea?» (`2026-07-24_conv2025_extraordinario_cuestionario.txt`).
   New, right after the heading:
   ```
   :::note{type=info}
   Fuera del enunciado literal del programa; preguntado en la convocatoria 2025 (llamamiento extraordinario), primera
   parte, pregunta 12.
   :::
   ```
   TJUE sentences and EU currency: not touched (re-verified separately).

## Cut items checked

Every exam in `SP/exams/` (conv2020, conv2020_X, conv2022, conv2022_X, conv2024_A/B/X, conv2025_A/B/X; reserve and
annulled questions included) was searched for each item (article number, key phrase and topic words), and the bloque
I rows of conv2020 and conv2020_X were read whole. For 2022–2025 the coverage report also lists every bloque I row as
covered except the two misses fixed above, neither of which is a cut item.

| Tema | Cut item (ledger) | Verdict | Questions found |
|---|---|---|---|
| I.2 | Art. 57.5 CE (abdicaciones y renuncias por ley orgánica), left out | not asked | none («abdica», «renuncia» hits are TREBEP/LRJSP) |
| I.3 | Art. 93 CE, dropped for length | not asked | none (the conv2025_X second-part «artículo 93» question is LRJSP art. 93) |
| I.4 | Arts. 125–126 CE (jurado, acción popular; policía judicial), dropped in the trim | not asked | none |
| I.5 | Art. 105 CE | not asked | none |
| I.5 | Art. 24.1 Ley 50/1997 (forma de las disposiciones) | not asked | none (conv2022_X P1 28 option «Real Decreto del Presidente del Gobierno» asks art. 63 LRJSP) |
| I.5 | Plan Anual Normativo (art. 25 Ley 50/1997) | not asked | none |
| I.5 | Gabinetes appointments (art. 16 Ley 50/1997) | not asked | none (Gabinete hits are TREBEP situaciones: personal eventual) |
| I.5 | Disposición adicional tercera Ley 50/1997 (sesiones a distancia) | not asked | none (the conv2025_X second-part «a distancia» option is LRJSP art. 17) |
| I.5 | Part of the delegation rules (art. 20 Ley 50/1997) | not asked | conv2024_A P1 5 asks art. 8.4, already in m01-l05 |
| I.6 | Estrategia de Desarrollo Sostenible 2030 (omitted, source not downloadable) | not asked | conv2025_X P1 6 names it in the stem; it asks whose 17 ODS (Naciones Unidas), covered |
| I.7 | Art. 4 Ley 19/2013 | not asked | none |
| I.7 | Art. 5.5 | not asked | none |
| I.7 | Art. 6 bis | not asked | none |
| I.7 | Art. 8.3 | not asked | none |
| I.7 | Art. 11 | **restored** | conv2020_X P1 5 |
| I.7 | Art. 15.3 (ponderación criteria) | not asked | none |
| I.7 | Art. 19.1 | **restored** | conv2020_X P1 7 |
| I.7 | Art. 19.4 | not asked | none |
| I.7 | Art. 21 | not asked | none |
| I.7 | Art. 22.2–22.3 | not asked | none |
| I.7 | Art. 30.6–30.8 | not asked | none |
| I.7 | Art. 31.5 | not asked | none |
| I.7 | Art. 36.4 | not asked | none (conv2020_X P1 6 and conv2022 P1 reserva 2 ask art. 36.2, covered) |
| I.7 | Disposición adicional primera | not asked | none |
| I.7 | Estatuto CTBG art. 18.1 (vocal mandate) | not asked | none |
| I.8 | Adscription of the Delegaciones del Gobierno (no source) | not asked | none (conv2020 P1 8 names them in an option on RD 208/1996) |
| I.9 | CE DT 1.ª, 3.ª, 4.ª, 6.ª, 7.ª and DA 1.ª | not asked | none |

Seen while reading conv2020 bloque I, outside the cut lists and the coverage population (programa anterior), not
edited: conv2020 P1 3 asks art. 120.2 CE («predominantemente oral, sobre todo en materia criminal»; scope report says
120.1), not in m01-l04; conv2020 P1 5 asks art. 29.2.d) Ley 19/2013 (sigilo, grave), m01-l07 gives art. 29.2 only
«entre otras». conv2022 P1 26 and conv2020 P1 1 also ask by which procedure (art. 167 or 168) each reform passed;
m01-l01 does not say (no source in `sources/normativa/`, per the I.1 writer's notes).

## New sources

None. Every article cited is in `BOE-A-1978-31229_ce_2026-05-20.pdf` and `BOE-A-2013-12887_ley-transparencia_2022-07-09.pdf`.

## Glossary entries affected by the removal

No entry moves to the waiting list: no entry had «El Gobierno Abierto en España» as its only second lesson. Two
stale marks for the coordinator:
- `g-competencia-exclusiva`: its `link_except: [m01-l06]` existed for the removed sentence «Cada Administración pública
  tiene competencia exclusiva en Gobierno Abierto…»; the phrase no longer occurs in m01-l06, so the exception can go.
- `g-entidad-local` (origin m01-l10): its web mark in m01-l06 («las Entidades Locales tienen sus propias políticas»)
  disappears; the entry is used in other lessons, so nothing else changes.
`glossary-links.es.txt` and `lesson-refs.es.txt` need regenerating: three new lesson references (m01-l01 → m01-l03,
m01-l02 → m01-l01, m01-l03 → m05-l01).

## Word counts (`wc -w`)

| Lesson | Before | After |
|---|---|---|
| m01-l01 | 3,991 | 4,086 |
| m01-l02 | 2,489 | 2,500 |
| m01-l03 | 3,609 | 3,648 |
| m01-l06 | 2,177 | 2,041 |
| m01-l07 | 3,651 | 3,716 |
| m01-l11 | 3,902 | 3,951 |
| m01-l04, l05, l08, l09, l10 | unchanged | unchanged |

Checks: every new line ≤ 120 characters; `uv run pytest -m 'not integration' -k "glossary or registry or content or
pipeline"` in `backend/`: 68 passed.
