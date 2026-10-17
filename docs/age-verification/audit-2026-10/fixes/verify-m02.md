# R2b fixes — bloque II (m02-l01 … m02-l04): blind verification

Verifier, 2026-10-17, to the «Verifier (blind)» section of `spec.md` (this folder). Checked: the lessons as they stand
(`git diff` against HEAD for the changed lines), the source articles read by the verifier with `pdftotext -layout` from
`content/age-administrativo-c1/sources/normativa/` (RD 203/2021 art. 40.3; LPAC art. 53.1.a); LOPDGDD arts. 2.2,
3.1, 22.3, 34.1, 73.l)) and `sources/otros/incibe-glosario-ciberseguridad.pdf`, the questionnaires and keys in
`SP/exams/` (conv2025 modelo A P1 12; conv2025 extraordinario P1 17, 18, reserva 1; conv2024 extraordinario
Supuesto I 6, key b; conv2020 P1 14; conv2020 extraordinario P1 22), the coverage reports `coverage/m02*.md` and
`docs/prose-voice.md`. m02-l02 is unchanged against HEAD.

| # | Lesson | Change | PASS/FAIL | Reason | Replacement (for FAIL) |
|---|---|---|---|---|---|
| l01-1 | m02-l01 | note, «Las cartas de servicios» | PASS | conv2025 modelo A P1 12 exists and asks art. 10.4 RD 951/2005 (al menos cada tres años), stated in the section. Wording follows the spec form («la convocatoria 2025 (modelo A)»). Placed right after the heading; the parent «## Atención al público» carries no note. Wrap ≤ 120. | — |
| l03-1 | m02-l03 | coverage, art. 40.3.a) RD 203/2021 | PASS | Item a) is verbatim art. 40.3.a). «estas dos» → «estas tres» matches the list (a, f, g). Row conv2024_X Supuesto I 6 (key b «La digitalización de su solicitud») is now stated. Normativa already lists RD 203/2021 art. 40. List markers as the existing items; wrap ≤ 120. | — |
| l03-2 | m02-l03 | restore, art. 53.1.a) LPAC (PAG consultation) | FAIL | The second paragraph of art. 53.1.a) refers back to the first, and the new sentence copies that list. It drops the condition attached to the silencio: «en caso de que la Administración no dicte ni notifique resolución expresa en plazo». R2 rule: a shortening keeps every plazo and exception. Organs, the PAG and the rest are correct. Row conv2020_X P1 22, option d, is answered either way. | Quienes se relacionen con las Administraciones Públicas a través de medios electrónicos tienen derecho a consultar<br>en el Punto de Acceso General electrónico de la Administración el estado de la tramitación de los procedimientos en<br>los que sean interesados, el sentido del silencio administrativo que corresponda, en caso de que la Administración no<br>dicte ni notifique resolución expresa en plazo, el órgano competente para su instrucción, en su caso, y resolución, y<br>los actos de trámite dictados (art. 53.1.a) LPAC). |
| l03-3 | m02-l03 | no change, «CA» acronym | FAIL (reason only; optional) | The fix file says no saved source prints the acronym. `sources/otros/incibe-glosario-ciberseguridad.pdf`, 2.1.30, does: «La Autoridad de Certificación (AC o CA, por sus siglas en inglés, Certification Authority)». This is the source the coverage report cites. The row (conv2022_X P1 44) stays covered in m06-l01, so making no change is allowed. The stated reason is wrong. | Optional, after «…clave pública con su propietario (anexo RD 203/2021).»: «La Autoridad de Certificación se abrevia AC, o CA por sus siglas en inglés (Certification Authority) (INCIBE, «Glosario de términos de ciberseguridad», 2.1.30; sources/otros/incibe-glosario-ciberseguridad.pdf).» Wrap at 120. |
| l04-1 | m02-l04 | restore, arts. 2.2.b) and 3.1 LOPDGDD | PASS | Art. 2.2.b) is verbatim. Art. 3.1 is a faithful shortening: it keeps vinculados familiares o de hecho, herederos, responsable o encargado, acceso / rectificación / supresión, the two exceptions (prohibición expresa, ley) and the saving for patrimonial data. «aquel» refers to «el fallecido» and is correct. conv2020 P1 14 (key d) exists and is now stated. Normativa «arts. 1, 5–7» → «arts. 1–3, 5–7» is in step. Wrap ≤ 120. | — |
| l04-2 | m02-l04 | note, «Videovigilancia» | PASS | conv2025 extraordinario P1 17 exists and asks art. 22 (one month, salvo integridad de personas, bienes o instalaciones). The section states it. Note format and placement are correct. | — |
| l04-3 | m02-l04 | note, «Régimen sancionador» | PASS | conv2025 extraordinario P1 18 exists and asks art. 73 (option a = letter l). Note format and placement are correct. | — |
| l04-4 | m02-l04 | coverage precision, art. 73.l) | PASS | The new sentence is letter l) verbatim, both branches. Citation is correct. Rewrapped ≤ 120. | — |
| l04-5 | m02-l04 | «Lo que más cae», art. 34.1.g) and l) | PASS | g) and l), and the exception for individual health professionals, match art. 34.1 («en todo caso»). The exception now attaches to the centros sanitarios. conv2025 extraordinario reserva 1 (key b) exists. The block still has ten lines. The line is unwrapped like every line of this block in the course. | — |

## Covered rows re-checked

Every row that `coverage/m02-l01.md` … `m02-l04.md` marks covered was re-found in the lessons as they stand: 9 + 7 + 8 +
12 quotes, plus the m06-l01 «(CA)» line for conv2022_X P1 44. No edit removed or weakened one. m02-l02 is unchanged. The
one miss, conv2024_X Supuesto I 6, is now covered (l03-1).

## Other checks

- Removals: none. No dangling reference, Normativa line or «Lo que más cae» line to check. Glossary unaffected.
- Normativa: m02-l03's LPAC line already lists 53.1.a) and its RD 203/2021 line already lists art. 40. m02-l04's
  LOPDGDD line now lists art. 2 and art. 3. Nothing became uncited.
- Voice: the new prose has no filler, no triad, no rhetorical question and no summary closer. «Esa prohibición…» in l04-1
  opens a split sentence but is not one of the blacklisted openers.
- Wrap: no changed line exceeds 120 characters, outside the «Lo que más cae» convention. The pre-existing 142-character
  line in «Videovigilancia» (m02-l04 line 93) was not touched by this round.
- Word counts match the fix file: 3,510 / 3,045 / 3,583 / 4,076.

## Counts

- Changes verified: 9 (5 with new text in lessons, 3 notes, 1 no-change decision).
- PASS: 7.
- FAIL: 2. l03-2 must be fixed. l03-3 is a wrong reason only, and the replacement is optional.
