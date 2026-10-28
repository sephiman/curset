# Style rewrites I–V, pass 3: check (verifier 2, R3 close, 2026-10-28)

Input: `style-rewrites-i-v-3.json` (4 «rewrite»). The standard is the same as in `style-rewrites-i-v-2.check.md`. Each `new` text was read against its question in `<bloque>/mBB-lTT.draft.json`. Every claim was checked in the norm text, using `pdftotext -layout` on the LCSP, LGP, LGSS and IOC files listed in `sources/normativa.yaml`.

This is the last round. Each id gets one of three outcomes:
- PASS.
- FAIL (style): the wording fails, but a sentence of a norm rules out each distractor. No drop.
- FAIL (check 2): some distractor is ruled out by no sentence of a norm in force. The question is dropped.

| id | decision | verdict | reason |
|---|---|---|---|
| m03-l04-q106 | rewrite | FAIL (check 2, dropped) | Art. 135.1 LCSP stacks places: the perfil de contratante, «además» the BOE for the AGE, and «además» the DOUE for regulación armonizada. No sentence says the DOUE is the only extra place, or that the anuncio may not also go in an autonomous or provincial boletín. The rewrite says «es otro lugar y la regulación armonizada no lo pide», which is absence again. This corrects pass 2, where I said the question stands. The sentence I suggested there («the one place added») depended on «one», a word the article does not contain, just like the «solo» I had rejected. Minor point: the BOE quotation adds a comma («además, en el») that is not in the norm («además en el»). |
| m05-l03-q002 | rewrite | FAIL (style, no drop) | The question stands. Art. 73.1 LGP («a través de las siguientes fases», a–e) is given whole and is closed. It rules out the retención and the propuesta, and 73.2 («se autoriza») rules out the autorización. The wording fails because the rewrite says the retención is «un acto propio, anterior al expediente». IOC regla 14.1 puts it «al inicio de la tramitación de un expediente de gasto», and its certificate goes «al respectivo expediente», so it is part of the expediente, not before it. LGP DA 21 is limited to expropiaciones and calls the retención neither «acto propio» nor anything else. |
| m05-l01-q036 | rewrite | FAIL (style, no drop) | The question stands. Norma primera of art. 36.2 LGP gives the instrument for this act («cuya composición se determinará por orden del Ministro de Hacienda»), and that rule excludes the other instruments. The wording fails in two places. «El acuerdo del Consejo de Ministros aparece en el apartado 5» is wrong: 36.5 reads «elevar al acuerdo del Gobierno». «El apartado 5 coloca la Ley al final de ese procedimiento» is also wrong: 36.5 speaks of the anteproyecto, and art. 37 sends the proyecto to the Cortes. The procedure produces the anteproyecto, not the Ley. Neither sentence rejects its distractor with the rule that actually decides it, which is the quoted orden ministerial. The Subsecretaría sentence holds. |
| m04-l09-q060 | rewrite | FAIL (check 2, dropped) | Distractor d (the causante's período mínimo de cotización) is ruled out by no sentence. Arts. 216.3 and 224.1 give the conditions with «siempre que…», plus «en los términos establecidos reglamentariamente», so the list is not closed. The rewrite says 224.1, first paragraph, links the pensión to a cotización. It does not: the paragraph says «en alta o situación asimilada a la de alta, o fuera pensionista», and it names no cotización period. That such a requirement would clash with «no reúnan los requisitos necesarios para causar una pensión de orfandad» is an inference the norm does not state. Pass 2 kept the question on distractor b, which art. 224.3 («menor de veinticinco años») still rules out. Distractor d was not examined then, and it fails. |

Summary: 4 checked: PASS 0, FAIL 4.
- FAIL (style, no drop): m05-l03-q002 and m05-l01-q036. The keys and distractors hold on the norm; only the explanation is wrong.
- FAIL (check 2, dropped): m03-l04-q106 and m04-l09-q060.

Drop rows (batch `style-recheck-3`, check `unique`): m03-l04-q106 in `bloque-iii/drops.tsv` and m04-l09-q060 in `bloque-iv/drops.tsv`.
