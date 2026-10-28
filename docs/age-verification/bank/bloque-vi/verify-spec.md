# Verifier spec — question bank, bloque VI (R3, session 5, 2026-10-23)

`../bloque-ii/verify-spec.md` (its rulings included) with these changes for bloque VI. You did not write the questions
you check. Read first: `docs/age-exam-style.md` (whole; § 9 and § 12), `bloque-vi/spec.md` (the writer's rules: what
may be asked, labels, citations), the tema's lesson, `docs/age-verification/bank/official/VI.N.md`, and the theory
ledger's «Open items (after bloque VI)» (label table, decoded paths, «Sin fuente oficial», Impr Pant). Do not read the
writer's notes before your verdicts.

Open the cited page yourself in `content/age-administrativo-c1/sources/otros/`; do not trust `source_quote`.

1. **Key.** Is the keyed option correct by the cited page?
2. **Unique.** Is exactly one option correct in Windows 11 / Microsoft 365 desktop? A distractor fails the question
   if any saved page or the cited page makes it true. It also fails if it is a real alternative way to do the same
   thing: another path, another shortcut, the right-click menu. If you know such an alternative but no saved page
   states it, say so in a note; fail only if you can show it in a saved page or in the cited page. A stem that does
   not say which Outlook, when the page treats the two apart, fails.
3. **Citation.** Does the cited page contain the answer, and does the lesson cite that file? (`check_anchors.py`, or
   `_anchor` on the citation.)
4. **Style.** Checklist § 12 items 1–12, 16, 17 as in the bloque II spec, but item 2 here means the stem names the
   application and version; no stem names an article. Also fail: a label that is not the page's official one where
   the ledger's table gives both; a fact from the «Sin fuente oficial» list or a retired feature; any key or
   distractor about what Impr Pant alone does or where the quick access toolbar sits by default; a feature the page
   gives only for another platform (web, Mac, Windows 10) asked as if it were desktop.
5. **Not official.** As in the bloque II spec, with its rulings: same stem with the same options, or same fact and
   angle with the official key and an official distractor carried over, fails. Check 5 compares stem and options, not
   the fact.

Report `bloque-vi/m06-lNN.part-<k>.verify-<batch>.md` with the same table and summary; drops to
`bloque-vi/drops.tsv` (append with `>>`). Keep extracted text in your own scratchpad subfolder named after your batch.
Final message: counts and failing ids with their check.

Coordinator ruling (2026-10-24), after a blind sample re-check failed 2 of 32 questions a first pass had passed: on
check 2, name for every distractor the page sentence that makes it wrong; if none does, it fails. Grep the text of
every saved page in `sources/otros/`, not only the cited one, for a description, path or shortcut that makes a
distractor true. A claim in the explanation that no page states fails check 4.
