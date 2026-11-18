# Writer notes — m03-l20 (III.20, Aduana)

Method: as m03-l18; CAU from the PDF (soft hyphens and page footers cleaned), the two reglamentos from the .html (tags stripped with `html.parser`).

1. Work list
- 1 art. 103 CAU whole, art. 124 whole (a)–k), 124.2–7), arts. 125–126, Reglamento Delegado art. 103: done, new section «Límites y extinción de la deuda aduanera».
- 2 Reglamento Delegado arts. 77–80 (plazo del art. 87.2): done, after the 87.2 paragraph.
- 3 art. 83.3, 86.3–86.6, 88 whole; Reglamento Delegado arts. 72–76 (first paragraph of each, one line each): done.
- 4 Reglamento Delegado arts. 135–143 whole and Reglamento de Ejecución arts. 217–219, 220 bis, 221 whole: done, after art. 158 and after art. 161.
- 5 arts. 4 and 9 CAU whole, Reglamento Delegado arts. 5–7: done, at the head of the lesson (headings «Territorio aduanero», «Registro de los operadores económicos»).
- 6 art. 39 a)–d): done after art. 18.3.
- 7 art. 71 whole (a)–e) with incisos, 71.2, 71.3): done; «entre otros elementos» gone.
- 8 l. 11: «El artículo 5 CAU define, entre otros, estos términos» → «Del artículo 5 CAU, estos términos:».
- 9 «No confundir» ×3: directa/indirecta (arts. 18.1 / 77.3), inclusión/incumplimiento (arts. 77.2 / 79.2.a), lugar de nacimiento (arts. 87.1 / 87.4).
- 10 esquema «Clases de representación aduanera» removed (it repeated l. 27); l. 31, 86, 111, 155, 157, 163, 179 split into lists, one sentence per item with its citation.
- 11 Normativa: CAU, Reglamento Delegado, Reglamento de Ejecución added; intro names both reglamentos and the extinción.
- Coordinator note: arts. 162–163 CAU restored at the end of «Inclusión de mercancías…» under «Declaraciones en aduana normales».

2. Words: 5369 → about 16,000.

3. Articles treated now: CAU 4, 9, 39 a)–d), 71 whole, 83.3, 86.3–6, 88, 103, 124–126, 162, 163; Reglamento Delegado 5–7, 72–80, 103, 135–143; Reglamento de Ejecución 217–219, 220 bis, 221.

4. Enumerations completed: art. 71.1 (a)–e) with incisos → whole), art. 4.1 (28 territorios), art. 9.3 a)–b), art. 124.1 a)–k), art. 39 a)–d) (the e) criterion is not incorporated by art. 18.3 and is left out).

5. «No confundir»: three, after art. 18 (representación), after the exportación esquema block (77.2 / 79.2.a), after art. 87.

6. Reworded without being named: none besides the removed esquema (item 10), the intro (item 11) and the sentences split into list items.

7. Facts added with no pack question: all of the above except arts. 18.1, 158.1, 5.5, 5.26, 71.1.e), 72.a), 144, 149, 233.4.a), 237, 240 (about 60 units).

8. Glossary proposals: none.

9. Course summary: «El territorio aduanero y el registro EORI, la representación aduanera, el nacimiento, el lugar y la extinción de la deuda aduanera (límite de tres años) y la declaración en aduana.»

10. Sources missing: none. Unresolved citations: none; the reglamentos resolve (the tool found a unit for them). The CAU PDF carries the consolidation of 12-12-2022; the citations of the CAU articles are in the future tense of that text («nacerá»).

## Fix pass (verifier FAILs)

- `extra-L60`: footnote mark «( 7 )» removed (art. 5.1.a).iii) RD 2015/2446). `extra-L510`: «( 13 )» removed (art. 141.5). `extra-L424`: j bis) of art. 136.1 is its own list item. All three fixed.

## Fix pass (verifier notes), R2d fixer 2

- art. 5.1.a) Reglamento Delegado: incisos i)–iv) each a nested sub-item under a), words kept. Normativa: final line for Convenio de tránsito común, Convenio de París 1963, TIR, ATA, Convenio de Estambul (no entry in normativa.yaml). cites.py: 0 unresolved.

## Fix pass (verifier notes, round 5)

- Copied EU text: «no 1186/2009», «n.o 2658/87», «n.o 1/2023» (and «n.o» elsewhere) written «n.º». Left untouched: «Treaty Series no 4 (1961)», a title.

Checks: cites.py 0 unresolved; index_sources.py run (see coordinator).
