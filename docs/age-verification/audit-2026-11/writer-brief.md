# Writer brief — currency audit 2026-11, bloque VI replacements and re-cites

Read and follow `docs/age-verification/bank/bloque-vi/spec.md` (and what it tells you to read) and
`docs/age-verification/bank/s5-writer-brief.md` § «Replacements» and its rules; this page says only what differs.
Commit nothing. Do not edit lessons, content, tests, goldens, other drafts or any `drops.tsv`.

**Why.** On 2026-11-05 the live check of the saved pages found pages that moved or changed. The dropped questions are
listed with their reasons in `docs/age-verification/bank/bloque-vi/drops.tsv` (batch `audit-2026-11`); do not read
`docs/age-verification/audit-2026-11/pages.md`.

**Sources you may use.** Only saved pages in `content/age-administrativo-c1/sources/otros/` whose entry in
`fuentes.yaml` has no `comprobacion` field, or a `comprobacion` saying the text or the cited facts are the same (`texto
visible igual`, `los hechos citados se mantienen`, `mismo texto`). Never a page marked `live check pending`, and never
`ms-office-formatos-archivo.html`, `ms-cuenta-mfa.html`, `ms-outlook-grupos-envio-recepcion.html` or the old
`ms-win-lupa.html` for anything but «amplía toda la pantalla o parte de ella». New pages saved on 2026-11-05:
`ms-win-lupa-cap1.html`, `ms-win-lupa-cap2.html`, `ms-win-lupa-atajos.html` (Apéndice A, every Lupa shortcut),
`ms-entra-mfa.html`, `transparencia-planes-accion_2026-11-05.html`. Every fact a replacement asks must be stated by
the lesson of its tema (search the lesson for it); a fact the lesson does not state is not a candidate.

**Replacements.** One new question per dropped id, same tema and lesson, ids as your prompt gives them. Do not ask an
angle any kept question of the lesson's draft already asks (read the draft; kept = not in `drops.tsv`). If a dropped
question `covers` an official question and you can cover the same official fact from an allowed page, keep the
`covers`; otherwise leave `covers` empty and say so in your notes. Citation form: ``fuente: `<file>`; «<label>»``,
where the label is the page's own sentence holding the key, copied exactly from one paragraph or list item (six words
or more, ending in «.», «:», «?» or «!»). Files: `bank/bloque-vi/<lesson>.audit-2026-11.draft.json` (JSON list, same
fields as the lesson's draft) and `<lesson>.audit-2026-11.writer-notes.md`.

**Re-cites.** For each id in your prompt, the question stays as it is; only its source moves. Find the sentence on
the new page that holds the key, and write `bank/<bloque>/<lesson>.audit-2026-11.recite.json`: a JSON object
`{"<id>": {"citation": "…", "source_quote": "…", "explanation": "…"}}`. Change `explanation` only where it quotes the
old page in words the new page does not print (re-quote from the new page; keep everything else). If the new page does
not hold the key, or holds a different label, say so in your notes and leave the id out.

**Checks before hand-back.** `source_quote` is an exact substring of your text extraction of the page (whitespace
normalised); `python3 docs/age-verification/bank/tools/lint_drafts.py bloque-vi <lesson>.audit-2026-11` clean of real
faults; anchors resolve (`check_anchors.py` way, from `backend/` with `uv run`); `correct` set by script. Keep your
scripts in your own scratchpad subfolder named in your prompt.

Final message: per id, the stem with its keyed option and citation (replacements) or the new citation (re-cites);
covers kept or lost; lint and anchor results. Keep it short.
