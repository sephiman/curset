# Writer spec — question bank, bloque VI (R3, session 5, 2026-10-23)

`../bloque-ii/spec.md` with the changes below; where they differ, this page rules. Read in full before writing:
`CLAUDE.md`, `docs/prose-voice.md`, `docs/age-exam-style.md` (whole; § 9 ofimática, § 12 the checklist),
`docs/age-bank-plan.md` § 3, `docs/age-ofimatica-index.md`, your tema's lesson
`content/age-administrativo-c1/es/lessons/m06-lNN.md`, the tema's official questions
`docs/age-verification/bank/official/VI.N.md`, and in `docs/age-theory-ledger.md` «# Bloque VI», the sections
«Decisions after bloque VI», «Coverage check 2022–2025» and «Open items (after bloque VI)». The last holds the label
table, the decoded paths, the «Sin fuente oficial» list and the Impr Pant note. Also read the `writer-brief.md`
practicalities (scratchpad subfolder, JSON written by script, `correct` set from the key text, lint, stats).

## Source of every question

R4.3: the bloque VI lessons are short and list-shaped, and the bank carries the bloque. So:
- The fact comes from a **saved official page** in `content/age-administrativo-c1/sources/otros/` that **your lesson
  cites** (`(fuente: \`file\`)` in the lines of your part). It may be any fact on that page within the feature your
  lesson's item treats, not only the sentence the lesson states. Read the page yourself (the HTML via a Python
  HTML-to-text pass; a PDF via `pdftotext -layout`). Never from an official key, never from memory, never from a page
  the lesson does not cite.
- The page must apply to **Windows 11** or **Microsoft 365 desktop for Windows** (look at the page's «Se aplica a» or
  its tabs). A fact the page gives only for Windows 10, Word para la web, Mac, mobile or one Outlook is not asked,
  unless the stem says which. For Outlook, the stem names classic Outlook («Outlook clásico») or the new Outlook
  («el nuevo Outlook para Windows») whenever the page treats them apart.
- Coordinator ruling (2026-10-23): a page on the theory ledger's «Files resting on non-UI sources» list (e.g.
  `ms-win-registro.html`, `ms-sql-bits.html`, the RFCs) may back **concept** questions only (what something is or
  does, as the page defines it). Never use such a page for a label, path, shortcut or setting.
  The same holds for a page on a retired product that a lesson cites for a general concept (`ms-mineria-datos.html`:
  the concept of data mining, not the SQL Server feature).
- **Not asked:** facts on the «Sin fuente oficial» list; retired features (the index's «Retired» table, and any page
  marking a feature as deprecated or removed); the two disputed points: what Impr Pant on its own does, and the quick
  access toolbar's default position (above or below the ribbon). Neither may appear in a key or in a distractor.
- **Labels:** the official Spanish label as the page prints it. Where the ledger's label table gives an exam label and
  an official one, the stem and options use the official one; the explanation may mention the exam's. Where a page
  prints a path garbled, use the decoded form the ledger gives; never decode a new one yourself (leave that fact out
  and note it).
- **Citation:** `fuente: \`file.html\`; «label»`, where the label is the page's heading, or the official label of the
  feature, under which the fact sits, as printed (`fuente: \`ms-word-atajos.html\`; «Tareas de documento frecuentes»`).
  Only files your lesson cites resolve. Check with `_anchor` as in `check_anchors.py`; zero misses.
- `source_quote`: the page's exact sentence(s) holding the answer, copied from your text extraction (checked by script
  against it, whitespace normalised).

## Your part, ids and quota

Each part writer covers a line range of the lesson. The range holds items, and each item cites pages; your facts come
from those items' pages. File: `bloque-vi/m06-lNN.part-<k>.draft.json` plus `.part-<k>.writer-notes.md`. Ids
`m06-lNN-q<k-1>01` upwards (part 1 q001…, part 2 q101…, part 3 q201…). Write the quota **plus about 15 %**: drops are
expected.

| Tema | Lesson | Part | Lines | Quota (kept) |
|---|---|---|---|---|
| VI.1 | m06-l01 | 1 / 2 / 3 / 4 | 5–27 / 28–47 / 48–73 / 74–93 | 61 / 60 / 60 / 60 (241) |
| VI.2 | m06-l02 | 1 / 2 / 3 / 4 | 6–34 / 35–56 / 57–76 / 77–105 | 51 / 51 / 50 / 50 (202) |
| VI.3 | m06-l03 | 1 / 2 / 3 / 4 | 6–30 / 31–53 / 54–80 / 81–105 | 56 / 55 / 55 / 55 (221) |
| VI.4 | m06-l04 | 1 / 2 / 3 / 4 | 6–28 / 29–51 / 52–77 / 78–102 | 55 / 54 / 54 / 54 (217) |
| VI.5 | m06-l05 | 1 / 2 / 3 / 4 | 6–30 / 31–55 / 56–78 / 79–107 | 51 / 51 / 50 / 50 (202) |
| VI.6 | m06-l06 | 1 / 2 / 3 / 4 / 5 | 5–29 / 30–56 / 57–77 / 78–95 / 96–118 | 51 / 51 / 51 / 50 / 50 (253) |
| VI.7 | m06-l07 | 1 / 2 / 3 / 4 | 7–36 / 37–57 / 58–85 / 86–111 | 62 / 62 / 61 / 61 (246) |
| VI.8 | m06-l08 | 1 / 2 / 3 | 6–43 / 44–68 / 69–96 | 56 / 56 / 56 (168) |

Quotas: the 1,750 total spread by the index's per-application shares (Windows 60, Word 30, Excel 28, Access 34,
Outlook 31, correo e Internet 24, otros 35 of 242). Each application's share is split over temas by where the exams
ledger files its non-retired questions.

## Coverage order, inside your line range

1. Each «Lo que más cae» line whose fact sits in your range: at least two questions, from different angles.
2. Each official question in `official/VI.N.md` whose fact sits in your range, retired ones excepted: at least one
   question, never with its stem and options. Change the angle; never carry its key with one of its distractors.
3. **Recurring families** of the index («Recurring feature families») whose feature sits in your range: together with
   the other parts, **at least five questions per family** in the tema. Write at least five yourself if the family's
   items are all in your range; otherwise at least two, and say so in your notes.
4. **Programme features** («Programme features never asked», and every feature the lesson's section headings name)
   in your range: at least two questions each.
5. Then the rest of your items' pages, item by item, until the quota plus 15 %. Spread the questions over the items in
   proportion to what their pages state. One fact may be asked from two angles (path and effect; shortcut and
   command), but never twice with the same angle.

If the pages of your range cannot carry the quota without repeating an angle, stop at what they carry and say so in
your notes, with the count and what is missing.

## Form

- Stems name the application and version as the exams do: «En Windows 11…», «En Word 365…», «En una hoja de Excel 365
  en idioma español…», «En Access 365…», «En Outlook 365…» (and «Outlook clásico» or «el nuevo Outlook» where the page
  separates them). Concept questions (hardware, Internet, security) name no application. **Every stem about how a
  Windows component works (Seguridad de Windows, Defender, Firewall, Windows Update, Copias de seguridad, Explorador…)
  names «Windows 11»**: VI.1 lost 29 questions for leaving it out. Not asked: the frequency of feature updates
  (`ms-win-update.html` says both «una vez al año» and «dos veces al año»).
- **No stem names an article.** Stem-form mix over your part (profile O, from the 2025 bloque VI stems), each ±10
  points: `cual` «¿Cuál de las siguientes…?» about 45 %; `directa` «¿…?» about 40 %; `enunciado` (a statement to
  complete, ending in «:») about 8 %; `senale` «Señale…» about 7 %. `names_article` is always false. Negative stems:
  at most 1 in 20 (in capitals).
- Question forms (style § 9): concept, behaviour («¿qué ocurre si…?»), menu path («pestaña Inicio › grupo Párrafo ›
  …»; write the path with «›» as the lesson does), shortcut, function, formula result. In the tema, aim for each
  form the lesson's items support. Formula results: give the formula and the cell values in the stem; compute the
  result with the function's page; error values exactly as the page prints them («#N/A», «#¡VALOR!»).
- Options: the four share form (four paths, four shortcuts, four statements). Keys and keyboard names as the lesson
  writes them (Ctrl, Mayús, Alt, Entrar, Supr, Tab, F7; joined with «+»). Option 5–20 words, statements to 40; a path,
  a shortcut, a function name or a label may be shorter (as a figure name is in bloques I–V).
- **Distractors** must be wrong according to the saved pages, not just because they seem odd:
  - `otra-figura`: a real sibling command, label, shortcut or function that a saved page shows doing something else;
  - `texto-alterado`: the page's own sentence with one element changed;
  - `otra-ruta`: the right command under the wrong tab or group;
  - `otro-atajo`: a real shortcut that another row of the same page assigns elsewhere;
  - `cifra-cercana`: a nearby limit or size;
  - `mixto`.
  An invented label or behaviour is allowed only when no saved page or real feature makes it true, and only as one
  option of a question. Avoid it where a real sibling exists.
- `tags`: one to three of `concepto`, `comportamiento`, `ofimática-menú`, `atajo`, `función`, `resultado-fórmula`,
  `configuración`, `requisito`, `cantidad`.
- `difficulty`: 1 for a «Lo que más cae» fact or the feature's headline; 2 for a detail on the page; 3 for a fine
  distinction between neighbouring commands, a formula result with a trap, or an exception the page states.
  Target 30/50/20 %.
- `section`: the lesson's `##` heading the item sits under. `covers`: `lmc-N`, `official:<code>·P1·<n>` (reserves
  `P1R`), and `family:<Family name as in the index>` for a recurring family, `prog:<VI.N feature as the index words
  it>` for a programme feature never asked.
- Explanations name options by content, never by letter or position, and every claim in them must hold on the pages.
  **Pattern:** for each distractor, name it by its content, then give the page sentence that makes it wrong
  («"Ctrl+B" abre el panel de navegación, no…»). Not accepted: «las otras opciones», a bare demonstrative after another
  option («Esa opción…», «Eso es…»), or «La página dice que…» without naming the distractor. VI.4 part 4 lost 38
  questions this way.
- Spanish: Peninsular, impersonal in stems; correct typography («», no English quotes).

## Hand-back

The draft and notes: coverage list (each lmc line, official question, family and programme feature → ids), the
`bank_stats.py` and `lint_drafts.py` output for `m06-lNN.part-<k>`, the anchor check (0 misses), the `source_quote`
check, every stem printed with its keyed option, and facts left out and why (page for another platform, garbled
label, sin fuente, retired, disputed). Final message: short.
