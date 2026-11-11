# Blind check of the R2b/R2c edits — m03-l01, 2026-11-11

Verifier spec `docs/age-verification/aeat/r2b/verify/spec.md`. One esquema, «Naturaleza de los impuestos estatales según su
ley» (tabla), after the nine tax paragraphs it summarises.

| id | verdict | reason | replacement |
|---|---|---|---|
| `1eb4d2e2ce` | PASS | Header; columns fit every row (impuesto, naturaleza, cita). | |
| `e16134c563` | PASS | Art. 1 LIRPF: «es un tributo de carácter personal y directo que grava…». Verbatim; in the prose with art. 1 LIRPF. | |
| `2e1082349f` | PASS | Art. 1 LIS: «es un tributo de carácter directo y naturaleza personal que grava la renta de las sociedades…». Verbatim; in the prose. | |
| `85c597b17d` | PASS | Art. 1 LIVA: «es un tributo de naturaleza indirecta que recae sobre el consumo». Verbatim; in the prose. | |
| `9df8babbe5` | PASS | Art. 1 TRLIRNR: «es un tributo de carácter directo que grava la renta obtenida en territorio español…». Verbatim; in the prose. | |
| `a52a5b0530` | PASS | Art. 1 Ley 19/1991: «es un tributo de carácter directo y naturaleza personal». Verbatim; in the prose. | |
| `f761837eed` | PASS | Art. 1 Ley 29/1987: «El Impuesto sobre Sucesiones y Donaciones, de naturaleza directa y subjetiva, grava…». Verbatim; in the prose. | |
| `d140cdb10e` | PASS | Art. 1.1 TRLITPAJD: «es un tributo de naturaleza indirecta que… gravará». Verbatim; in the prose with art. 1.1. | |
| `d4106c511a` | PASS | Art. 1.1 Ley 38/1992: «Los impuestos especiales son tributos de naturaleza indirecta que recaen sobre consumos específicos». Verbatim; in the prose. | |
| `7934d68be8` | PASS | Art. 3.Uno Ley 38/2022: «es un tributo de carácter directo, naturaleza personal y complementario del Impuesto sobre el Patrimonio». Verbatim; in the prose with art. 3.Uno. | |
| title m03-l01 «Naturaleza de los impuestos estatales según su ley» | FAIL | The rows are nine state taxes; the State has others the lesson does not list (e.g. the Impuesto sobre las Primas de Seguros or the Impuesto sobre el Valor de la Producción de Energía Eléctrica of Ley 15/2012), and the lesson's own lead-in only says the naturaleza of each tax «está en su ley, en los preceptos que se citan a continuación», so the title reads a selective list as the complete set of «los impuestos estatales». | Naturaleza de algunos impuestos estatales según su ley |
