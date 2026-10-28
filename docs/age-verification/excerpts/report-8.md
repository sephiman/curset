# Excerpt verification — report, part 8 (items 301–400, norms of bloques I–V, step 5)

Blind opus verifier, `sample-8.jsonl`: 100 at random (seed 20261101) from the BOE/DOUE excerpts of bloques I–V, none in
samples 1–7. Saved by the coordinator from the verifier's returned text.

Counts: **96 yes, 1 full-only, 3 no**: 4 % without the fact in the excerpt text, above the 2 % threshold.

| n | key | verdict | note |
|---|---|---|---|
| 309 | m05-l02-ex-1/m05-l02-q039 | no | «arts. 43.2 y 44.2 LGP»: excerpt and full hold only art. 43; art. 44.2 (organismos autónomos list leaves out gastos reservados) is in neither. |
| 329 | m05-l02-ex-9/m05-l02-q282 | no | Anexo II Orden HAC/557/2026: the single line «227 Trabajos realizados por otras empresas y profesionales.»; the key is subconcepto «06 Estudios y trabajos técnicos», six lines below. |
| 375 | m05-l02-ex-11/m05-l02-q310 | no | Anexo II Orden HAC/557/2026: the opening of the whole annex, cut with «[…]»; the cited capítulos 3 and 4 come much later. BOE page header inside. |
| 377 | m05-l02-ex-9/m05-l02-q293 | full-only | art. 63.2 LGP refers to 63.1.b, which is only in `excerpt_full`. |

Flags: page headers or footers inside (301 BOE disclaimer, 365 DOUE running footer, 375 BOE page header); 318 garbled
(«funci ones», soft hyphen, paragraph break inside a word); multi-article citation shows only the first article (309);
annex units not narrowed to the cited entry (329, 375). Not an extractor bug: 348 «Adrninitraciones» is in the BOE.

Affected source types, per the round's step 5: multi-article norm citations, and annex code lists (`anexo …` units).
A full pass over those two kinds follows (`full-boe/`).
