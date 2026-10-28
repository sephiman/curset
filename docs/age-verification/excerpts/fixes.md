# Excerpt verification — misses, flags and what the extractor does now

Sample: 100 excerpts at random (seed 20261028) from the 5,184 of the first full build; two blind opus verifiers,
`report-1.md` and `report-2.md`. Result: **94 yes, 1 full-only, 5 no**. All six are extractor bugs (F3). The item
outputs below were re-read against the rebuilt `content/age-administrativo-c1/excerpts.json` by the coordinator;
no second verifier pass was run.

| Item | Verdict | Cause | Fix | Now |
|---|---|---|---|---|
| 7 | no | The year is in an earlier paragraph of the page; the explanation's first sentence names the joining, not the founding | none | open |
| 19 | no | Doc page: the pick stopped one step short of the instruction | A pick that ends its paragraph short of two sentences takes the next paragraph's first sentence | fixed: «… en la pestaña Permisos, … seleccione Agregar.» shown |
| 27 | no | Table row split per cell; the shortcut cell was dropped | A table row is one block, cells joined by « — » | fixed: «Ctrl+Mayús+teclas de dirección — Cuando …» |
| 52 | full-only | «apartado octavo.2.2» read as octavo.2 | An ordinal apartado followed by a dotted path selects that sub-apartado | fixed: excerpt is 2.2 |
| 58 | no | Doc page: the pick ended on «…es la siguiente:», before the list | After «…:» the panel shows that sentence and the list item that best matches the explanation | partly: the list is reached, but the item chosen is «Encabezados: &f», not «&p»; `&p` scores nothing once punctuation is dropped. Open |
| 98 | no | Table row split per cell; the query cell was dropped | as 27 | fixed: «hasattachment:yes — Los elementos que tengan datos adjuntos …» |
| 16 | flag | BOE editorial note «Téngase en cuenta …» inside the article | Notes («Téngase en cuenta», «Redacción anterior», «Se modifica … Ref. BOE-…») are dropped from excerpts | fixed |
| 85 | flag | «CAPITULO II» without accent not taken as a boundary | `TITULO`/`CAPITULO` accepted unaccented | fixed |
| 97 | flag | A hard line break after «artículo» kept as a paragraph break | A line ending in a word that cannot end a sentence never closes a paragraph | fixed |
| 26 | flag | A long list item chosen alone, without the apartado's opening words | A focused item keeps the apartado's opening sentence when it ends in «:» | partly: «1. Serán objeto de anotación …:» + item 20; the letter «a)» line is still not shown |
| 21, 31 | flag | Letters cited, whole apartado shown | By design: letters narrow the excerpt only when the apartado exceeds 200 words | kept |
| 82, 84 | flag | Term glued to its definition | The page itself has no separator (inline bold); `<dd>` now gets « — » | kept |
| 23, 49, 8, 9 | flag | Spacing at inline formatting boundaries | The page's own markup; not changed | kept |
| 7 (heading) | flag | Heading is the raw `<title>` for a page cited without label | not changed | kept |

After the fixes: 5,179 excerpts, 21 questions with no excerpt (0.40 %), every one with its reason. Of the 3,672
excerpts whose explanation quotes its source in «», 3,636 (99.0 %) contain a quoted fragment (automatic proxy, not
a verification).

## Pass 2 (closing round, 2026-10-29)

Three blind opus passes on the rebuilt file: `report-3.md` (the 12 items fixed or flagged after pass 1, plus 14
questions that a key-token rule had newly given an excerpt), `report-4.md` (50 at random from bloque VI),
`report-5.md` (the 11 sampled excerpts whose text changed after a verifier last judged them).

| Check | Result | What was done |
|---|---|---|
| Items 7 and 58 | yes (101, 105) | 7: a pick lacking a number its explanation's first sentence states takes the page sentence that holds it (two sentences at most). 58: codes («&p») and numbers of two digits or more rank lines under the cited label |
| Pass-1 fixes 19, 27, 52, 98 and flags 16, 26, 82, 84, 85, 97 | all yes (102–112); 108 (=26) still has no «[…]» before the list item, 109/110 (=82/84) term run-ins as in the source | none further |
| 14 newly matched no-excerpt questions | 6 yes, 8 no (navigation labels, wrong table rows, XML records) | rule restricted: a number or code qualifies a line only inside the cited label's section and with a word of the explanation; the 14 are «sin extracto» again (21 in all) |
| Bloque VI sample | 46 yes, 4 no | 128: quotes in the explanation's first sentence weigh double (later quotes are often the wrong options'). 152: shared runs of four words with the first sentence break ties. 145: only a first-sentence quote leaves the cited section. 148: the other half of a two-part fact, further down the section, is shown after «[…]» when it adds the explanation's words and is no wrong option's quote |
| Re-check of changed texts | 10 yes, 1 no (187 = 152: row label lost) | an argument row's label («value_if_error Obligatorio.») is kept with its description; a see-also question («¿Busca información…?») is never appended (flag 178) |

Not changed: flags 160 (PDF pull-quote), 169 (Copilot banner text), 181 («Win32_Processorclase», the page's own
markup), 162 (dangling «Nota:»). After the last fix only three excerpts changed (q206, q207, q042), all checked by
reading; no further verifier pass. Final: 5,179 excerpts, 21 «sin extracto» (0.40 %), listed in
`docs/age-bank-ledger.md`.

## Samples 6 and 7 (2026-10-30): fresh bloque VI

Two further blind opus samples of 50 from bloque VI, none of them sampled before (`report-6.md`, `report-7.md`).
Both came back at **44 yes, 6 no (12 %)**, so the 2 % threshold was missed twice; the second sample was drawn after
the sample-6 fixes. Per the round's instruction, no third sample.

| Item | Cause | Extractor change | Now |
|---|---|---|---|
| 198, 216 | label matched in an «Obtener ayuda con Copilot» banner; a wrong option's quote pulled the pick elsewhere | blocks inside `copilot`/`banner` containers are dropped; outside the cited section only the first sentence's quotes and the explanation's words count | fixed |
| 201 | «…siga estos pasos:» rule dropped the paragraph's first sentence (the fact) | a «…:» pick keeps its best sentence plus the list's best item | fixed |
| 217 | the next step was a list lead-in («…acciones siguientes:») | a lead-in of four words or more gives way to the list item that matches | fixed |
| 220 | a label inside a paragraph made a one-paragraph section | an inline label opens the paragraphs after it, up to the next heading | fixed |
| 226 | missing-number donor took another section's «1983» | donor searched in the cited section first; ties go to the earlier sentence; words match by their first five letters | fixed |
| 255 (flag) | splitter broke at the initial «S.» and spliced two sentences | no split after a lone capital initial when a capitalised word follows | fixed |
| 265 | the second quoted half was in the next sub-section | the other half of a two-part fact may come from anywhere on the page when it holds a quote of the explanation's first sentence | fixed |
| 271 | a quote that is the cited label's own name outranked the paragraph with the fact | quotes the cited label already holds are ignored | fixed |
| 243 (flag) | excerpt was the label itself | (changed by the 220 rule) the section's body text is shown | improved |
| 240 | English page, the DNS paragraph shares no exact words with the Spanish explanation | a stem-based paragraph fallback was tried and reverted: it gave English filler to the NIST questions | open |
| 260, 263 | the cited unit holds no prose (a table under another heading; a list of link titles) | none: citation form | open |
| 280 | the fact needs four sentences of one paragraph | none: F2's two-sentence cap | open |

Tried and reverted in this pass (each moved other excerpts, including verified ones, or added «sin extracto»):
a paragraph-title section rule, the stem fallback, a weaker weight for short quotes. Final state checked against
every sampled item: apart from the fixed misses and 243, no verified excerpt changed; the 21 «sin extracto» are the
same questions. The fixes of sample 7 have not had a blind re-check.
