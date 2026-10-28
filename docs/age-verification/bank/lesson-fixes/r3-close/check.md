# R3 close, blind check (verifier-2): m03-l03, art. 62 LPAC (addition)

Source: `sources/normativa/BOE-A-2015-10565_lpac_2024-11-06.pdf` (consolidated 2024-11-06), art. 62, opened with
`pdftotext -layout`. Citations resolved with `CourseCitations.build(...)._anchor('m03-l03', 'art. 62.N LPAC', 'es')`:
N=1..5 all give `boe-a-2015-10565-art-62`. Only the art. 62 paragraphs and the Normativa line were judged; the other
hunks in the diff were checked earlier.

| # | Item | Lesson, lines | Faithful | Cited | Placed and scoped | Voice | Verdict | Reason |
|---|------|---------------|----------|-------|-------------------|-------|---------|--------|
| 1 | Denuncia: definition, contents, patrimonio público, no interesado | m03-l03, 240-247 | PASS | PASS | PASS | PASS | PASS | Matches 62.1 verbatim; 62.2 keeps «cuando sea posible»; 62.3 keeps «deberá ser motivada» and the notice «de si se ha iniciado o no»; 62.5 keeps «por sí sola». Placed after art. 58 (iniciación de oficio por denuncia). |
| 2 | Denunciante who took part in the infracción (leniency) | m03-l03, 252-260 | FAIL | PASS | PASS | PASS | FAIL | Drops a condition: the norm says «una infracción **de esta naturaleza**», the lesson «una infracción». Changes the subject of one condition: the norm says «y **se repare** el perjuicio causado» (impersonal), the lesson «y repare» (the denunciante). In the reduction sentence the grammatical subject is the órgano («debe reducir … cuando facilite»), but in the norm it is «el denunciante facilite». |
| 3 | Normativa line: «58, 62, 63.1» | m03-l03, 515 | PASS | n/a | PASS | n/a | PASS | Art. 62 added in order. Cosmetic: the line is now 124 characters (the wrap elsewhere is 120); rewrap if wanted. |

Replacement wording for item 2 (the whole paragraph, lines 254-260):

> Si el denunciante participó en la comisión de una infracción de esta naturaleza y existen otros infractores, el órgano competente para resolver debe eximirlo de la multa que le correspondería, u otra sanción no pecuniaria, cuando sea el primero en aportar pruebas que permitan iniciar el procedimiento o comprobar la infracción, en ese momento no se disponga de elementos suficientes para ordenar la misma y se repare el perjuicio causado. Si no se cumple alguna de esas condiciones, debe reducir el importe de la multa, o la sanción no pecuniaria, cuando el denunciante facilite pruebas que aporten un valor añadido significativo respecto de las disponibles. En ambos casos el denunciante ha de cesar en la participación en la infracción y no haber destruido pruebas relacionadas con el objeto de la denuncia (art. 62.4 LPAC).

Not-done items in the record: none.

Notes, not failures: lines 244 and 257 are 121 characters. Item 1 renders «recogerán» as «recoge también» and
«se notificará» as «se notifica», which is the usual present tense for a rule.

**Counts:** 3 items; 2 PASS, 1 FAIL (item 2, art. 62.4).

## Re-check (coordinator edit)

Item 2 re-judged after the coordinator's edit (m03-l03, lines 254-260), against art. 62.4 LPAC opened again from
`sources/normativa/BOE-A-2015-10565_lpac_2024-11-06.pdf` (`pdftotext -layout`). `_anchor('m03-l03', 'art. 62.4 LPAC',
'es')` gives `boe-a-2015-10565-art-62`.

| # | Item | Lesson, lines | Faithful | Cited | Placed and scoped | Voice | Verdict | Reason |
|---|------|---------------|----------|-------|-------------------|-------|---------|--------|
| 2 | Denunciante who took part in the infracción (leniency) | m03-l03, 254-260 | PASS | PASS | PASS | PASS | PASS | The three findings are fixed: «una infracción de esta naturaleza», «y se repare el perjuicio causado» (impersonal, as the norm), and «cuando el denunciante facilite pruebas que aporten un valor añadido significativo». The other conditions are kept: «existan otros infractores», «sea el primero en aportar elementos de prueba que permitan iniciar el procedimiento o comprobar la infracción», «en el momento de aportarse aquellos no se disponga de elementos suficientes», «cuando no cumpliéndose alguna de las condiciones anteriores», and the shared «cese en la participación … y no haya destruido elementos de prueba». Only this paragraph changed; it matches the proposed wording. |

Note, not a failure: «ordenar la misma» keeps the norm's own unclear antecedent. Line lengths 112-120, within the wrap.

**Counts after re-check:** 3 items; 3 PASS, 0 FAIL.
