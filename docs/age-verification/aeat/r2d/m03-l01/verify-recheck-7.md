# Verify re-check 7 — `m03-l01`

2026-11-18. Blind verifier (Opus). Source: `content/aeat-agentes-hacienda/sources/normativa/BOE-A-2004-4214_trlrhl_2026-10-07.pdf` (pdftotext -layout). Ids recomputed from the lesson as it stands (sha1[:10] of the sentence text): both match `pending.md` (lines 686 and 766). Normativa line lists TRLRHL arts. 16.1–2 and 20.1–6.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `b19fe5773c` | FAIL | art. 16.2 TRLRHL, párrafos 3.º y 4.º | Rule, organ and cross-reference are faithful («apartado anterior» = art. 16.1, último párrafo). But the cut dropped «de ordenanzas fiscales» from the subject, so the sentence does not stand on its own: «los acuerdos de aprobación» names no object and «aquellas» has no antecedent in the sentence. Restore the subject as the article has it (and as the sibling 16.1 sentence does: «Los acuerdos de aprobación de estas ordenanzas fiscales…»). | Los acuerdos de aprobación de estas ordenanzas fiscales se adoptan simultáneamente a los de fijación de los elementos regulados en aquellas, y los acuerdos de modificación de dichas ordenanzas se ajustan a lo dispuesto en el último párrafo del apartado 1 del artículo 16 (art. 16.2 TRLRHL). |
| `271f93b2aa` | PASS | art. 20.4.n) TRLRHL | Verbatim to the letter n) of art. 20.4; every element and the «incluso cuando los gastos deban sufragarse por otras entidades de cualquier naturaleza» clause kept. «benéfico-asistenciales» is the BOE compound (the hyphen falls at a PDF line break but is part of the word), not an artefact. Letter and order (m) → n) → ñ)) match the article. | |

PASS 1 · FAIL 1
