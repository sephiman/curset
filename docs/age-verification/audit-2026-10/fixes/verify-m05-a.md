# R2b fixes — bloque V, m05-l02 and m05-l03: blind verification

Verifier, 2026-10-17, to the «Verifier (blind)» section of `spec.md` (this folder). Share: every change to m05-l02 and
m05-l03 in `fix-m05.md` (m05-l04 and m05-l06 are verified in another report). Checked: the lessons as they stand
(`git diff` against HEAD for the changed lines); the articles read by the verifier with `pdftotext -layout` from
`content/age-administrativo-c1/sources/normativa/` (LGP arts. 34.1, 73.1–6, 75.1–4, 107; IOC reglas 6, 14.1, 15, 77.1–2;
Resolución de 20-01-2014 anexo II and anexo IV art. 22; Orden PRE/1576/2002 apartado octavo; LCSP arts. 100.1, 116.3;
Orden de documentos contables, searched for the RC amount); the questionnaires and definitive keys in `SP/exams/`
(conv2025 extraordinario Supuesto I 12, key a; conv2022 Supuesto II 11, key a; conv2024 modelo A Supuesto II 18, key b;
conv2025 modelo A Supuesto II 8, key a; conv2024 extraordinario Supuesto II reserva 5, key a); `coverage/m05-l02.md`,
`coverage/m05-l03.md`, `scope/m05.md` (gap S5a) and `docs/prose-voice.md`.

| # | Lesson | Change | PASS/FAIL | Reason | Replacement (for FAIL) |
|---|---|---|---|---|---|
| l02-1 | m05-l02 | coverage + restore, reglas 6.1–2 IOC under «Transferencias de crédito» | PASS | Regla 6.1 and 6.2 IOC as written («se deberá retener» → «se retiene»; «este tipo de operación» → «la transferencia»), nothing dropped; the cross-reference to regla 15 is left out, which removes no fact. Row conv2025_X Supuesto I 12 (key a, retain the amount before processing) is now stated; option c (two MC) is the 6.2 fact placed after approval, as the norm says. conv2022 Supuesto II 11 exists and asks 6.1. Pointer «Los documentos RC y MC están en m05-l03» is valid (m05-l03 table, rows RC and MC; regla 6.1 also at line 46). Wrap ≤ 120. | — |
| l02-2 | m05-l02 | coverage, subconcepto 221.03 under «Clasificación económica» | PASS | Anexo IV, art. 22 Res. 2014: «Artículo 22. Material, suministros y otros», «Concepto 221. Suministros», «Subconcepto 03. Combustible», and the exception «salvo en el caso de que tratándose de alquileres de edificios estén comprendidos en el precio de los mismos» kept as «Se exceptúa el caso de alquileres de edificios en cuyo precio esté comprendido». Code 221.03 matches anexo II of the Resolución. Row conv2024_A Supuesto II 18 (key b, 221.03) is now stated. m05-l05 does state it (lines 43, 103, 173), so the pointer holds. | — |
| l02-3 | m05-l02 | introduction, titles of the Resolución de 20-01-2014 and the IOC | PASS | Titles and short names identical to m05-l04/m05-l05 (Resolución) and m05-l03/m05-l05 (IOC). Wrap ≤ 120. | — |
| l02-4 | m05-l02 | confirmation only, conv2024_X Supuesto I 4 | PASS | No text changed. The sentence «Una transferencia que incremente el concepto 202 también va al Ministro de Hacienda…» is still at line 298–300; the lesson states the norm, not the disputed key. | — |
| l02-5 | m05-l02 | «Lo que más cae», new line 7 | PASS | Regla 6.1 IOC, correct; asked by two questions (conv2025_X Supuesto I 12, conv2022 Supuesto II 11). Block now 7 lines (≤ 10). Single-line format as the other lines of the block. | — |
| l02-6 | m05-l02 | Normativa | PASS | Adds «Resolución de 20-01-2014 … anexo IV, artículo 22 (concepto 221)» and «IOC … regla 6.1–2»: both now cited in the body; no line lost an article. | — |
| l03-1 | m05-l03 | coverage, art. 34.1.b) LGP under «Reconocimiento de la obligación» | PASS | Art. 34.1 and 34.1.b) copied in full («El ejercicio presupuestario coincidirá con el año natural, y a él se imputarán: … b) …»). The worked example (December 2025 → presupuesto 2025) follows from the article. Row conv2025_A Supuesto II 8 (key a: 2025, OK) is now fully stated: the imputation here, OK in the existing phase table. Art. 34.2–3 are separate apartados, not exceptions dropped from 34.1.b). | — |
| l03-2 | m05-l03 | coverage, art. 100.1 LCSP under «Contratos y subvenciones» + introduction | FAIL | Text is correct: art. 100.1 LCSP verbatim, and regla 77.1 IOC indeed gives no amount (nor do reglas 14.1 and 15 IOC, art. 116.3 LCSP or the Orden de documentos contables; a search of every saved source for RC/retención with «licitación» finds nothing). Introduction title matches m05-l06. But check (2) fails: conv2024_X Supuesto II reserva 5 asks the RC amount (key a: 300.000 € + IVA, the presupuesto base de licitación, not the 298.000 € award price). The lesson sets two facts side by side and says explicitly that no text joins them; the asked fact is still not stated. Row stays **partial**. Nothing invented, which is right: no saved norm states the amount. | Keep the paragraph as is (no saved text allows more). Record conv2024_X Supuesto II reserva 5 as partial in the ledger «Open items»: it closes only with an official source that states the amount of the initial RC in a contract file. Optional, to tie the two facts with texts already cited, replace the first sentence with: «Por el importe solicitado mediante el documento RC, el crédito queda retenido para su posterior utilización en el gasto de que se trate (regla 14.1 IOC); la regla 77.1 IOC no fija ese importe para los contratos.» |
| l03-3 | m05-l03 | gap S5a, «concepto» of the ordenación del pago (two paragraphs) | PASS | Every sentence is in the texts: art. 73.1.d) LGP (fourth phase, between reconocimiento and pago material; LGP art. 73.2–4 defines the first three phases and none defines the ordenación, so «La LGP no define la ordenación del pago» is true); art. 75.3 LGP (acreedor of the propuesta; Orden del Ministro de Economía; Habilitaciones, Cajas pagadoras, Depositarías, entidades colaboradoras de la LGS, agentes mediadores, intermediarias) complete; art. 107 LGP verbatim, «entre otros» kept; apartado octavo.1.1–1.2 and octavo.2.2 Orden PRE/1576/2002 faithful (the «sin perjuicio» art. 106 paragraph of 2.2 is a separate rule, not an exception to the stated sentences). The gap is filled from the texts the scope report names, without a coined definition. «Ministro de Economía» repeats the norm's wording after the paragraph that carries the «(hoy: …)» note, per convention. No exam 2022–2025 asks it (scope report), so no note is due. | — |
| l03-4 | m05-l03 | «Lo que más cae» unchanged | PASS | Still 9 lines; no new fact is asked twice. | — |
| l03-5 | m05-l03 | Normativa | PASS | LGP line adds 34.1.b), 75.3, 107 and keeps every earlier article (73.1–4 … 164.1); Orden PRE adds octavo.1, octavo.2.2; new LCSP line art. 100.1. Each is cited in the body; nothing became uncited. Wrap ≤ 120. | — |

## Other checks

- Covered rows: the diff of both lessons is additive except the rewrapped introduction sentence and Normativa lines, which
  keep their text. Every row `coverage/m05-l02.md` and `coverage/m05-l03.md` mark covered is still covered (including
  conv2022 Supuesto II 11, quoted from m05-l03 line 46, unchanged).
- Removals: none in these two lessons, so no dangling reference.
- Notes: none added in these two lessons; none was due.
- Voice: no filler, triad, rhetorical question, «no solo… sino también» or summary closer in the new prose; no
  blacklisted split opener. «La regla 77.1 IOC no dice…» and «La LGP no define…» state a limit plainly.
- Wrap: no changed prose line exceeds 120 characters; the new «Lo que más cae» line follows the block's single-line form.
- Word counts match the fix file: m05-l02 4,226; m05-l03 4,400.

## Counts

- Changes verified: 11 (m05-l02: 6; m05-l03: 5).
- PASS: 10.
- FAIL: 1 (l03-2: correct text, but conv2024_X Supuesto II reserva 5 is still partial; no saved source states the RC
  amount, so it goes to open items rather than to a rewrite).
