# Excerpt verification — follow-up sample (2026-11-06)

Spec: `docs/age-verification/excerpts/verifier-spec.md`. Input: `excerpts-sample-new.jsonl` (7 items).
Extra rule for LGSS arts. 169 and 172: the fact must be in the wording in force from 01-12-2026 (RDL 31/2026),
and neither `excerpt_text` nor `excerpt_full` may contain the text printed after «Redacción anterior:».

Sources opened: `sources/normativa/BOE-A-2015-11724_lgss_2026-10-21.pdf` (the file `normativa.yaml` names,
consolidated 2026-10-21), `sources/otros/boe-rd-4-2010-eni.pdf`, `sources/otros/ms-entra-mfa.html`.

| n | key | verdict | note |
|---|---|---|---|
| 1 | m04-l09-q078 | yes | 169.1.a).4.ª verbatim in the 01-12-2026 wording; full is art. 169 without the «Téngase en cuenta» note or the «Redacción anterior» block. Text jumps from the apartado 1 lead-in straight to 4.ª with no «[…]» between them. |
| 2 | m04-l09-q080 | yes | Closing paragraph of 169.1.a) («En dichos documentos… inicio de la investigación») verbatim, new wording; no superseded text. Same missing «[…]» after the lead-in. |
| 3 | m04-l09-q082 | yes | Art. 172.a) second paragraph («según la edad… tomando como referencia la fecha de la baja médica») verbatim, new wording (the old wording lacks the baja-médica reference); full null = whole unit; no superseded text. |
| 4 | m04-l09-q083 | yes | 169.1.a).5.ª verbatim, new wording; no superseded text. Same missing «[…]» after the lead-in. |
| 5 | m04-l09-q084 | yes | 169.1.a).1.ª («…en cuyo caso tendrá la consideración de situación de incapacidad temporal por contingencias profesionales») in the text, new numbered wording; cut at 3.ª with «[…]»; no superseded text. |
| 6 | m06-l01-q378 | yes | Glossary entry matches the PDF word for word. Heading «ANEXO» is right but bare; the anexo's title is «Glosario de términos». |
| 7 | m06-l01-q379 | yes | «Algo que eres - biometría como una huella digital o un escaneo facial» in the text, matching the page. Flag: the heading «En este artículo» is Learn's table-of-contents label (navigation), not a section heading. |

## Misses and flags by cause

- Misses: none (7 yes, 0 full-only, 0 no).
- Superseded wording: none. All five LGSS excerpts (text and full) carry the RDL 31/2026 wording in force
  from 01-12-2026, and none contains the «Téngase en cuenta» note or the «Redacción anterior» block. No
  page headers or footers («Página 91/92/95», «BOLETÍN OFICIAL DEL ESTADO») leak into them.
- Silent elision (items 1, 2, 4): `excerpt_text` prints the apartado 1 lead-in and then a non-adjacent
  paragraph with no «[…]» between them, which hides the omitted letter a) and the «situaciones especiales»
  sentence. Cosmetic. The fact is present.
- Navigation heading (item 7): «En este artículo» used as `excerpt_heading`.
- Bare heading (item 6): «ANEXO» without its title «Glosario de términos». Minor.
- Garbled text: none.
