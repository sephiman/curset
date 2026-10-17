# Spec — R2 bloque VI (temas VI.1–VI.8, lessons m06-l01…m06-l08)

Course `content/age-administrativo-c1` (call it C below). Date of this round: 2026-10-17. Nothing is committed.
SP = /tmp/claude-1000/-home-juanjo-PycharmProjects-curset/3bfdbef1-0a20-46f7-a34d-245ff55c6923/scratchpad

## Read first (writer and verifier)

- `docs/age-administrativo-course-requirements.md` R4.3, R4.6 (bloque VI lessons: short, list-shaped, 600–1,500 words).
- `docs/age-ofimatica-index.md` (the whole file: the map of what the exams ask).
- `docs/age-exam-style.md` §9 (ofimática).
- `docs/prose-voice.md` (the "never does" list is a hard constraint) and `CLAUDE.md` (no invented vocabulary; Peninsular
  Spanish, «tú»).
- `C/es/lessons/m00-l01.md` as the register; `C/es/lessons/m02-l03.md` for list and wrap conventions (hard wrap ≈120).
- `C/sources/programa.md` bloque VI (tema text verbatim).
- `docs/age-official-exams-ledger.md`: which exam question belongs to which tema (column Tema = `VI.N`) and its
  official key. Questionnaires and keys: `C/sources/examenes-oficiales/*.pdf` (`pdftotext -layout`).

## Sources (hard rules)

- For every feature: the official Microsoft documentation in Spanish (support.microsoft.com/es-es,
  learn.microsoft.com/es-es) for Windows 11 and Microsoft 365 desktop. For VI.1 and the internet / correo /
  seguridad items: an official or standards-body page (INCIBE, AEPD, CCN, IETF RFC, W3C, IEC, Microsoft, BOE).
  The ENS (`C/sources/normativa/BOE-A-2022-7191_ens_2024-11-06.pdf`) is already saved and may be cited by file.
- Never a third-party academy, blog, forum, Wikipedia, or Microsoft Q&A / Community forum (answers.microsoft.com,
  learn.microsoft.com/answers are forums: excluded).
- Save every page before citing it, under `C/sources/otros/`, with a short distinctive name: `ms-<app>-<topic>.html`
  (e.g. `ms-word-atajos.html`, `ms-excel-funcion-sierror.html`, `ms-win-explorador.html`), `incibe-<topic>.html`,
  `rfc5321-smtp.txt`, etc. Download: `curl -sSL -A "Mozilla/5.0" -o FILE URL`; check the final URL and that the
  saved page is the article you wanted (not a sign-in or home redirect) and in Spanish (`lang="es-es"`).
  sha256: `sha256sum FILE`.
- Before downloading, check whether the page is already saved: `C/sources/otros/fuentes.yaml` and the fragments
  `SP/m06-l*/fuentes.yaml` of earlier temas. Reuse an existing file rather than saving a second copy.
- Record each page you save in `SP/m06-lNN/fuentes.yaml` (your tema's fragment; never edit `C/sources/otros/fuentes.yaml`
  yourself), same fields as the main file:
  ```yaml
  - file: ms-word-atajos.html
    url: "https://support.microsoft.com/es-es/…"   # the final URL after redirects
    title: "Microsoft, «Métodos abreviados de teclado en Word»"
    consultado: "2026-10-17"
    sha256: …
    lessons: [m06-l04]
  ```
  When you reuse a page an earlier tema saved, add a line `reused: [file, …]` at the end of your notes so the
  coordinator adds your lesson to its `lessons` list.
- Where Microsoft's Spanish page does not exist: save the English page; the primary label is the Spanish-locale UI
  label, with the English one in brackets once («Acceso por voz [Voice access]»). The Spanish label must come from an
  official source (another Spanish Microsoft page that names it, the Microsoft terminology collection on
  learn.microsoft.com). If a label cannot be confirmed from an official source, do not guess: write the English label,
  say «etiqueta en español no confirmada» in your notes, and the ledger lists it.
- Never cite a live page. Never cite an official exam as the source of a fact (official keys are not a source; R5.5).
- Text extraction: `python3 -I SP/tools/pagetext.py FILE [REGEX]` prints the readable text of a saved HTML page (with a
  REGEX: matching lines with one line of context). Microsoft shortcut pages have Windows, Mac and web sections: use the
  Windows desktop section only.

## Scope

- Windows 11 and Microsoft 365 desktop (Anexo III 2.1). Features that exist only in Word para la Web, only in Windows
  10, or only in one of the two Outlooks are labelled as such («solo en Outlook clásico», «en el nuevo Outlook») or left
  out. Outlook: Microsoft 365 desktop has two clients, «Outlook clásico» and «nuevo Outlook para Windows»; state which one
  an item describes when they differ.
- Retired features (WordPad, Cortana, Asistente de concentración, Reconocimiento de voz de Windows, Grabación de
  acciones de usuario, Correo y Calendario, the Explorer ribbon, «Información/Tell Me», Presentar en línea…) are not
  described. If the programme still names one, one line says it was retired and what replaced it, with a source.
- Use the index's «Windows 11 / Microsoft 365 note» column as a lead to check, never as a source.

## The lesson (`C/es/lessons/m06-lNN.md`)

Keep the `# …` title line exactly. Remove the «Tema sin redactar» note. Then:

1. One or two lines of intro at most: what the lesson covers (e.g. «Word de Microsoft 365, versión de escritorio, con las
   etiquetas de la interfaz en español de España.»). Say once, in the first lesson that uses it (each lesson that uses
   shortcuts), how keys are written: «Windows» is the key with the Windows logo; key names as Microsoft's Spanish pages
   write them (Ctrl, Mayús, Alt, Entrar, Supr, Inicio, Fin, Re Pág, Av Pág, Impr Pant, Tab, Esc, F1…), joined with «+».
2. One `##` section per application or concept the programme names, in programme order, with the programme's own
   words as headings (e.g. for VI.4: «## Creación y estructuración del documento»). `###` subsections allowed for long
   sections.
3. Every item is a `- ` list item, one line or two (wrapped lines indented two spaces): the feature in bold, where it
   lives (menu path with Spanish-locale labels: «Inicio › Párrafo › Numeración»; Settings paths: «Configuración ›
   Sistema › Pantalla»), its shortcut if it has one, and the one or two behaviours the exams ask (what it does, its limit,
   its default). Ends with the citation `(fuente: `file`)` — the file name in a code span. Two files when the item
   needs both. Example:
   `- **Cambiar mayúsculas y minúsculas**: «Inicio › Fuente › Cambiar mayúsculas y minúsculas»; Mayús+F3 alterna entre
     mayúsculas, minúsculas y tipo título (fuente: `ms-word-atajos.html`).`
4. Every claim in an item must be literally supported by the cited page: label, path, shortcut, behaviour, default. If
   the page gives only the label, the item gives only the label. Do not infer a path the page does not print.
5. Coverage: every recurring family of the index (two or more convocatorias) that the ledger files under this tema,
   with the fact the exams asked; every feature the programme names for this tema with at least one item; the
   single-convocatoria features of this tema as far as words allow. Also the features the index lists under
   «Programme features never asked» for this tema: at least one item each.
6. `## Lo que más cae`: exactly ten `- ` lines, each a fact the official exams asked for this tema (most repeated
   families first), stated as the fact, with its `(fuente: `file`)`. Never copy an official question or option text.
7. `## Fuentes` (replaces «Normativa»; last section): one line per saved page the lesson cites, in order of first
   citation: ``- `file`: Microsoft, «Page title» (support.microsoft.com, consultado el 17-10-2026).``
8. Length 600–1,500 words, `wc -w` on the whole file. If coverage does not fit, cut single-convocatoria detail first, and
   list what you cut.
9. Voice: `docs/prose-voice.md`. No fillers, no triads, no rhetorical questions, no closers. Items are terse. Peninsular
   Spanish, «tú». No invented vocabulary: only terms that exist outside the course with the same meaning (Microsoft's
   own feature names count).
10. Hygiene: no `-`, `*` or `1.` right after sentence punctuation and a space in the middle of a line (the list-shape guard
    reads it as a broken list marker); write «signo más» / «signo menos» for those keys if needed (e.g. «Windows+signo
    más (+)» is fine only if the `+` is not preceded by `. `). Spanish quotes «…». Lines ≤120 chars.

## Also produce (writer)

- `SP/m06-lNN/notes.md`:
  - **Tally**: the index rows the ledger files under this tema (exam, nº, family, status), and per row the lesson item
    that covers it.
  - **Programme coverage**: each phrase of the tema text → section/item.
  - **Lo que más cae sources**: per line, the exams and question numbers.
  - **Labels not confirmed** from an official Spanish source; **programme features not documented** (no official page
    found), with what you searched; **retired** features named and their replacement.
  - **Summary proposal** for course.yaml: three sentences at most, only terms the lesson uses.
  - **Cuts** made for length.
  - Word count.
- `SP/m06-lNN/glossary.yaml`: candidates, same schema as `C/glossary.yaml` (id `g-…`, `es`, `origin: m06-lNN`, optional
  `match: {es: [singular, plural…]}` with head-noun plurals for multi-word terms, `definition: {es: >- …}`). A term
  qualifies if it is a technical term used in a precise sense that appears in two or more lessons, or is defined on an
  official page you saved; the definition follows that page and ends «(fuente: file)» in plain text. Microsoft's own
  feature names count. Never a term the course invents. Check `C/glossary.yaml` for an existing entry first (e.g.
  «certificado electrónico» exists from bloque II): do not duplicate; note overlaps. Be selective (≈3–8 per tema): terms a
  reader would look up, not every feature name.

## Verifier (separate agent, has not written the lesson)

For each tema, a blind pass over: every list item of the lesson, every «Lo que más cae» line, the Fuentes block, the
summary proposal and the glossary candidates.

- Open the cited saved page (`pagetext.py`) and check each field the item states: label, path, shortcut, behaviour,
  default/limit. PASS only if the page supports it literally (Windows desktop section for shortcuts). FAIL with the
  reason and a replacement wording the page supports (or «drop»).
- Check the saved file matches the fragment entry: `sha256sum`, URL domain official, title matches page, Spanish page or
  documented English fallback. Re-download one page in five and compare the article text (not the bytes: Microsoft pages
  carry per-request tokens) to confirm the file is what the URL serves.
- Check coverage: every recurring index family filed under this tema and every programme phrase has an item; every LQMC
  line matches a fact the index/ledger shows was asked for this tema (open the questionnaire and key PDFs to confirm the
  asked fact) and is supported by its source; no official question copied.
- Check form: 600–1,500 words; voice «never does» list; list-shape hygiene; retired features not described.
- Write `SP/m06-lNN/verify-passK.md`: a table `| # | item (first words) | field(s) | PASS/FAIL | reason | replacement |`,
  then counts, then coverage findings. Do not edit the lesson.

## Coordinator decisions (after VI.1)

- incibe.es rejects a bare `-A "Mozilla/5.0"`: use a full Firefox user agent plus `-H "Accept: text/html,application/xhtml+xml"`
  `-H "Accept-Language: es-ES,es;q=0.9"`.
- Accepted as official: NIST (government standards body) for the IEC binary prefixes; a vendor's own support page for
  its own product (Apple for macOS). Not used: RAE dictionary, Microsoft Q&A, academies, Wikipedia.
- Labels printed with «&» on Microsoft's Spanish pages («Privacidad & seguridad», «Importar & vínculo»): write them as
  printed, never silently as «y»; the ledger lists the «y» form as not confirmed. A plural or singular the page does not
  print is not confirmed either (exam «Gráficos modernos» vs page «Gráfico moderno»).
- «Lo que más cae» lines state facts the exams asked, not neighbouring facts from the same page.
