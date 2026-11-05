# Brief shared by every classifier of round R0a, course age-auxiliar-c2

Repo: /home/juanjo/PycharmProjects/curset. Scratchpad: /tmp/claude-1000/-home-juanjo-PycharmProjects-curset/bc5c5336-dddc-4169-bc56-f2c03f6e6c40/scratchpad (call it $S).

You classify official exam questions of the Cuerpo General Auxiliar de la Administración del Estado (C2), ingreso libre.
You write ONE output file in $S/work/ (named in your task) and nothing else, anywhere. Never write in the repo.
Run any Python with `python3 -I`. Today is 2026-11-05.

## Inputs
- Your questions: a JSON list in $S/work/ (named in your task). Each item: id («2025-P1-12» = exam, section, number),
  exam, sec (P1 = part 1, R1 = part-1 reserve, P2 = part 2, R2 = part-2 reserve), n, modeloB (number in modelo B,
  2025 and 2024 only), stem, opts {a..d}, key (definitive official key, or «Anulada»/«ANULADA»), ctx (text that precedes
  the question in the PDF: table titles, «31 a 36. En la tabla siguiente…» headers).
- The parse can mangle tables and two-column options. When a question depends on a table or looks truncated, read the
  layout text: $S/txt/<file>.txt (pdftotext -layout of each questionnaire). Files: 2025 →
  2026-05-23_conv2025_modeloA_cuestionario.txt, 2024 → conv2024_modeloA_cuestionario.txt, 2024X →
  conv2024_extraordinario_cuestionario.txt, 2022 → conv2022_cuestionario.txt, 2020 → conv2020_cuestionario.txt,
  2020X → conv2020_extraordinario_cuestionario.txt. Originals: content/age-auxiliar-c2/sources/examenes-oficiales/.
  Exception: the 2024 «Cuadro Laboratorios» table (2024 part 1, 55–60) is an image; its transcription is
  $S/work/laboratorios.tsv (checked: it reproduces the six official keys).
- Programme (28 temas, verbatim): content/age-auxiliar-c2/sources/programa.md. Bloque I «Organización pública»
  (I.1–I.16), bloque II «Actividad administrativa y ofimática» (II.1–II.12). Exam versions: Windows 11 and Microsoft 365
  desktop (Anexo I 2.2).
- Norms: content/age-auxiliar-c2/sources/normativa.yaml (short names, temas, version in force on 2026-11-05,
  cambios_pendientes) and the texts in content/age-auxiliar-c2/sources/normativa/ (use `pdftotext -layout`).
- Conventions to copy (the C1 course did this round already): docs/age-official-exams-ledger.md (status rules, notes),
  docs/age-exam-style.md sections «Statistics» (category names), docs/age-ofimatica-index.md (applications, forms,
  family names). Saved Microsoft support pages: content/age-administrativo-c1/sources/otros/ms-*.html (read-only).

## Status rules (one per question)
- `anulada`: the definitive sheet says Anulada. Still classify tema/type.
- `vigente`: official key correct today, no note.
- `vigente-con-nota`: key stays, visible note of one kind: «Clave oficial discutida: <why>» (key not supported by the
  text in force, or not unique) in `nota_clave`; «Denominación actual: <current name>» (organ renamed since);
  «Etiqueta actual: <Windows 11 / M365 label>» (feature still exists, label changed; add «sin confirmar en la interfaz
  española» if you could not confirm it).
- `norma modificada: <norma> art. X`: the correct answer changed because the law changed (version in force
  2026-11-05, or a cambio-pendiente: then «(cambio-pendiente, desde DD-MM-YYYY)»).
- `función retirada`: the feature no longer exists in Windows 11 / M365 desktop.
- `fuera de temario`: the topic is in no tema of the 2025 programme.
- `dudosa`: you cannot settle it. Say why.
Errata that do not change the key go in `nota` as «Errata: …», status unchanged.
Official keys are never a source of facts. Check each key against the norm text in force (quote the decisive words, ≤ 25
words, in `evidence`) or, for ofimática, against the saved Microsoft pages or what you know of Windows 11 / M365 desktop
(then say «conocimiento general» in evidence). Never change an official key: record a disagreement in nota_clave.

## Category vocabularies (use exactly these strings)
stem_form: «según el artículo X … (completar)», «según el artículo X … ¿?», «según la norma (sin artículo) … (completar)»,
«según la norma (sin artículo) … ¿?», «¿cuál de las siguientes…?», «señale/marque la (respuesta|afirmación) correcta»,
«pregunta directa ¿…?», «enunciado a completar».
option_type: enunciado, órgano, plazo, cantidad, procedimiento, fecha, artículo, ruta-menú, función-fórmula, atajo, otro.
distractor: «texto alterado», «otra figura del mismo tipo», «invención», «otro plazo», «cifra cercana», «órgano de otro
nivel», «norma derogada o anterior», «otra aplicación/comando», «mixto».
negative: true when the stem asks for the false/incorrect/excluded option (NO, FALSA, INCORRECTA, EXCEPTO, «no es»).

Work exam by exam, and save your output file after each exam (rewrite the whole JSON list), so a cut loses little.
At the end reply with: counts per status, the ids you marked dudosa / norma modificada / función retirada / fuera de
temario / clave discutida with one line each, and anything in the inputs that looked wrong.
