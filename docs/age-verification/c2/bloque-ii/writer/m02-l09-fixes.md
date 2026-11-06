# m02-l09 — coverage fixes (2026-11-06)

Pages saved: `ms-excel-error-almohadillas.html`, `ms-excel-numeros-redondeados.html`, `ms-excel-funcion-dias.html`,
`ms-excel-funcion-diasem.html`, `ms-excel-funcion-truncar.html`, `ms-excel-si-anidadas.html`,
`ms-excel-rellenar-datos.html`, `ms-excel-prioridad-operadores.html` (fragment `m02-l09-fix-fuentes.yaml`).
Pending after `plan m02-l09 m06-l05`: 18, all new.

| Row | Result | Item / what was searched |
|---|---|---|
| 2025-P2-34 («#####» with negative dates) | fixed | Item «##### con fechas negativas». The page states both causes (narrow column, already in the lesson; negative date or time value, now added). No disagreement left on the page. |
| 2025-P2-36 (decimals round the display) | fixed (partial) | Item «Decimales mostrados»: the page says the number looks rounded and the full number stays in the formula bar. It does not give the 0,758 → 76 % case. |
| 2024-R2-2 (DIAS argument order) | fixed | Item «DIAS»: fecha_final first, fecha final menos fecha inicial, example 364. The page has no negative example (-9). |
| 2024-R2-4 (three freeze options) | sin fuente | The es-es freeze-panes page (saved copy and a fresh fetch) lists only «Ver › Inmovilizar paneles › Inmovilizar paneles»; the top-row/first-column buttons appear only on the Excel for Mac page, not admissible. |
| 2024X-P2-18 (TRUNCAR) | fixed | Item «TRUNCAR»: optional núm_decimales, default 0. |
| 2024X-P2-20 (RENDTO, CUPON.DIAS financial) | fixed | Item «Funciones financieras», cited from the saved `ms-excel-funciones-categoria.html`. The page prints CUPON.DIAS as «COUPDACUPON.DIAS» (garbled); the item quotes it as printed next to CUPON.DIAS.L1 and CUPON.DIAS.L2. |
| 2022-P2-38 (DIASEM tipo 2) | fixed | Item «DIASEM». |
| Family: nested SI | fixed | Item «SI anidada» (the page writes its formula with commas; the item uses «;»). |
| Family: controlador de relleno | fixed | Item «Controlador de relleno». |
| Family: operator precedence | fixed | Item «Prioridad de operadores». |

Counts, MISS rows: fixed 6 (one partial), sin fuente 1. Family gaps: fixed 3.
