# Verification — `m02-l05`, re-check 3

Verifier: blind verifier (opus), 2026-11-06. Did not write the lesson. Checked against the sources, not the proposer's
wording. The pending file lists 0 items; the coordinator named the new «Fuentes» line for `ms-win-configuracion-red.html`
(id from `backend/scripts/provenance.py` `sentence_id`, lesson line 159).

Files read: `content/age-auxiliar-c2/es/lessons/m02-l05.md`, `content/age-auxiliar-c2/sources/otros/fuentes.yaml`
(entry `ms-win-configuracion-red.html`), `<title>` of the saved page.

Result: 1 PASS, 0 FAIL.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `027f0a6e2e` | PASS | Fuentes; fuentes.yaml `ms-win-configuracion-red.html` | title «Comprender y explorar la configuración de Windows» (fuentes.yaml and page `<title>`), host support.microsoft.com, consultado 2026-11-06: match. The file is first cited at line 29 («Periféricos»), the 11th distinct file in the prose; the line is 11th in «Fuentes», right after `ms-win-dispositivos-entrada.html` (10th) | — |

Finding outside the pending id: the rest of «Fuentes» is not in order of first citation. Lines 12–28 (from
`hp-plotter-designjet.html` to `ms-win-update.html`) come before the six files first cited earlier in the prose
(`ms-excel-sistemas-numericos.html`, `python-tutorial-introduccion.html`, `ms-mixed-reality-cad.html`,
`ms-azure-ocr.html`, `moodle-codigo-abierto.html`, first cited lines 33–46; `ms-win-cuentas-usuario.html`, first cited
after `apple-macos.html`), which sit at the end. Every cited file is listed and no extra file is.
