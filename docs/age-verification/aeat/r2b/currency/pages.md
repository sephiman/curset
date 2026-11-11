# Currency audit, AEAT R2b part C — saved pages (2026-11-11)

`docs/age-verification/tools/check_pages.py --course aeat-agentes-hacienda`, one call per file (a first all-pages run
died on a read timeout of one host; the per-file runs completed), live copies in the session scratchpad, reports in
`pages-live/<file>.d/`. `consilium-presidencia.html` also with `--browser` (Playwright Chromium).

| File | Result | Places resting on it |
|---|---|---|
| clave-que-es.html | same text | — |
| consilium-presidencia.html | not read: 403 (plain and browser) | m01-l04, one sentence («El Consejo presenta a esos tres Estados como un trío»), inherited from C2 (C2's R2b could not read it either); the presidency order in the sentence before rests on Decisión 2016/1316, same text live. Kept as C2 has it; listed for the next live check |
| curia-tribunal-de-justicia.html | same text | — |
| curia-tribunal-general.html | same text | — |
| eurlex-decision-2016-1316.pdf | same text | — |
| incibe-glosario-ciberseguridad.pdf | same text | — |
| oecd-recomendacion-gobierno-abierto-2017.pdf | same text | — |
| sede-pag-portada.html | same text | — |
| transparencia-gobierno-abierto-que-es.html | changed: two list items on public consultations replaced by «El Pleno», «La Comisión Permanente», «Los Grupos de Trabajo» | m01-l05 cites it only for the Spanish wording of the OECD definition, which is unchanged live (read in the live copy); no sentence rests on the changed lines |
| ue-comision-europea.html | same text | — |
| ue-parlamento-europeo.html | same text | — |

Not retried by other means: the site refuses automated clients (bot check), and that refusal is not worked around.
Added this round: `doue-rgpd-correccion-2018.pdf` and `-2021.pdf` (copies of C1, same sha256; DO texts). `fuentes.yaml`
carries each result in `comprobacion`.
