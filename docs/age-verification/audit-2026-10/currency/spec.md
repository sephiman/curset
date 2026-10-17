# Currency check (R2b, Part C) — checker spec

Date 2026-10-17. Do not edit lessons, glossary, `normativa.yaml` or `fuentes.yaml`; write your report and save
downloads only where this spec says. Commit nothing. Shell commands: quote URLs (the shell globs `?`).

## C1a. Norms (`content/age-administrativo-c1/sources/normativa.yaml`)

For every entry with a `boe_id`:

1. Read the latest consolidated version on boe.es: the «Última actualización publicada el …» line of
   `https://www.boe.es/buscar/act.php?id=<ID>`, and the list of modifying norms in
   `https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/<ID>/analisis` (send `Accept: application/json`).
   The metadatos field `fecha_actualizacion` is a metadata timestamp, not the consolidation date: do not use it alone.
2. Compare with the stored `consolidated_as_of`, and with the date in the stored `file` name and any
   `cambios_pendientes`. A norm is **newer** when boe.es shows an update published after the stored date that the
   stored file does not contain (a pending change already in the stored file and recorded in `cambios_pendientes` is
   not newer).
3. For each newer norm: list every modifying norm published after the stored date (BOE id, date, title) and the
   articles of this norm it changes (from the análisis «referencias anteriores» and the modifying norm's text), with
   each change's entry into force. Download the new consolidated PDF
   (`https://www.boe.es/buscar/pdf/<año>/<ID>-consolidado.pdf`) into `SP/currency/normativa/` named
   `<ID>_<short>_<YYYY-MM-DD>.pdf` (date = the new «Última modificación»), and each modifying norm's text
   (`https://www.boe.es/boe/dias/…/pdfs/<ID>.pdf`) the same way.
4. For EU norms (`celex`): compare with the latest consolidated version date on EUR-Lex; same report.
5. Entries marked `unverified` or without a consolidated text: check whether boe.es now has one.

Then, for each changed article, list every place that cites it: lessons (`content/age-administrativo-c1/es/lessons/`),
glossary (`content/age-administrativo-c1/glossary.yaml`), course.yaml summaries. Quote the sentence and say whether
the new wording changes the fact it states (yes / no / unclear), quoting old and new article text.

Also list every `cambios_pendientes` item in `normativa.yaml` with its `en_vigor`, and every «(desde …)» mark in the
lessons, glossary and course.yaml (`grep -rn "desde [0-9]"` and «(desde la …)»), each with whether its date has passed
on 2026-10-17.

Report: `docs/age-verification/audit-2026-10/currency/normativa.md`: a table `| Norm | ID | Stored date | Latest on
boe.es | Newer? | Modifying norms | Articles changed |` for every entry, then the per-article citation list, then the
cambio-pendiente and «(desde …)» lists.

## C1b. Saved pages (`content/age-administrativo-c1/sources/otros/fuentes.yaml`)

For every entry in your share (given in your prompt):

1. Fetch the live `url` (`curl -sL --compressed -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like
   Gecko) Chrome/130.0 Safari/537.36" -H "Accept-Language: es-ES,es;q=0.9"`) into `SP/currency/pages/` under the same
   file name. Record HTTP status and final URL (a redirect to another page, a 404, or a login wall is a finding).
2. Compare sha256 with the stored one. If different, compare the readable text: HTML with `SP/pagetext.py` (`python3
   -I SP/pagetext.py FILE`), PDF with `pdftotext -layout`; `diff` the two texts. Ignore pure boilerplate (cookie
   banners, dates of the page footer, navigation, feedback widgets, «Artículos relacionados», tracking ids).
3. Classify: **identical** (sha256 equal), **text-identical** (only boilerplate differs), **changed** (body text
   differs), **gone** (404 / redirect elsewhere / no longer the same page).
4. For every **changed** or **gone** page: find each lesson sentence or glossary entry that cites the file
   (`grep -rn "<file>"` in lessons and glossary), and for each, quote the sentence and the old and new page text it
   rests on, and say whether the cited fact still holds on the live page (holds / changed / removed). Labels, menu
   paths, shortcuts and «Se aplica a» lines count as facts.

Report: `docs/age-verification/audit-2026-10/currency/pages-<share>.md`: a table `| File | Status | HTTP / final URL
| Note |` for every entry in the share, then per changed or gone page the affected citations with old/new text and
the verdict. Keep the downloads in `SP/currency/pages/` (they are the candidates to save).
