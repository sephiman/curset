# Recite check — bloque VI, followup 2026-11 (blind verifier, 2026-11-06)

Pages read from my own text extraction (HTML-to-text, whitespace normalised): `ms-edge-privacidad.html`,
`ms-edge-inprivate_2026-11-06.html`, `ms-outlook-grupo-enviar_2026-11-06.html`,
`ms-outlook-listas-contactos_2026-11-06.html`; every other `ms-outlook-*` / `ms-edge-*` page grepped for the
distractors and the explanations' side claims. Anchors resolved with `CourseCitations._anchor` on
`m06-l07.draft.json` / `m06-l08.draft.json` (the tool's per-id output is overwritten by the part drafts, so I ran it
on the merged drafts directly): all 14 resolve. The other misses in those two drafts (l07 q044, q226–q228, q349,
q351, q364, q366; l08 q229, q230, q232–q239, q265) are all already in `drops.tsv`.

## 1. Questions

«=HEAD»: `prompt` and `options` byte-identical to `git show HEAD:<draft>`. «exact»: citation label, `source_quote`
and every «» quotation in the explanation are text of the new copy.

| id | =HEAD | exact | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | note |
|---|---|---|---|---|---|---|---|---|---|
| m06-l08-q231 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | Distractors: favoritos/descargas wrong by inprivate_2026-11-06 «permitir guardar descargas y favoritos» (the «» is that page's text, not privacidad's; the explanation names it as «la página de InPrivate de Edge», fine); «Solo el historial» and «Nada, hasta…» wrong by the privacidad sentence. Style note: the citation label is the whole sentence, not the heading «Qué datos se recopilan o almacenan y por qué» (resolves; excerpt heading is right). |
| m06-l07-q037 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | |
| m06-l07-q038 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | |
| m06-l07-q039 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | Style note: stem keeps «Nuevo Email», the page now prints «Nuevo email». No option depends on the label; exactly one option is right. Not misleading. |
| m06-l07-q040 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | Stem also says «Nuevo Email» (same note as q039). |
| m06-l07-q041 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | |
| m06-l07-q042 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | «carpeta Archivo» claim on `ms-outlook-archivar.html`. |
| m06-l07-q043 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | |
| m06-l07-q045 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | Distractor labels on `ms-outlook-smime.html` and `ms-outlook-delegados.html`. |
| m06-l07-q347 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | |
| m06-l07-q348 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | «vista People es la libreta de direcciones» on `ms-outlook-atajos.html`. |
| m06-l07-q350 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | |
| m06-l07-q352 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | |
| m06-l07-q365 | yes | yes | PASS | PASS | PASS | PASS | PASS | PASS | Style note: key keeps «Guardar & Cerrar», page prints «Guardar & cerrar» (explanation and quote use the page form). «Guardar» is the new-Outlook list button, a different label; exactly one option is right. Not misleading. |

Check 5: the only official VI.7 group question (conv2025_A·P1·66) asks about the group address and who may send;
no stem or option set here repeats it. Nothing on InPrivate or contact lists in VI.7/VI.8 official.

## 2. Lesson and glossary

| place | change | verdict | note |
|---|---|---|---|
| m06-l08 «InPrivate», new sentence | «Al cerrar todas las ventanas de InPrivate, Edge elimina el historial de exploración, las cookies y los datos del sitio, las contraseñas, las direcciones y los datos de formulario (fuente: `ms-edge-privacidad.html`).» | PASS | Faithful to privacidad's sentence, nothing wider. One idea, plain, no filler, no triad tic (it lists the page's items), no synonym rotation. Fits the previous sentence (not saved on the device; downloads and favourites kept): it adds what is deleted at close, no contradiction. |
| m06-l08 «InPrivate», source lines | `ms-edge-inprivate_2026-11-06.html` for open + not-saved + downloads/favourites | PASS | All stated by the new copy («Configuración y más», «ventana Nuevo InPrivate», «permitir guardar descargas y favoritos»). |
| m06-l08 «Fuentes» | inprivate_2026-11-06 «Explorar InPrivate en Microsoft Edge», privacidad «Microsoft Edge, datos de exploración y privacidad», 06-11-2026 | PASS | Titles match the pages' H1. |
| m06-l07 l.21–24 groups | source → `ms-outlook-grupo-enviar_2026-11-06.html` | PASS | New copy states: anyone in the organisation can start a conversation; in classic all members receive it; public = anyone in the organisation reads and replies; private = only members. |
| m06-l07 l.105–107 grupo de contactos | source → `ms-outlook-listas-contactos_2026-11-06.html` | PASS | New copy: classic «People» › «Nuevo grupo de contactos» › «Agregar miembros»; new Outlook calls it lista de contactos; deleting the list keeps the contacts. |
| m06-l07 «Fuentes» (two lines) | new file names, 06-11-2026 | PASS | Titles match. |
| glossary `g-lista-de-contactos` | source → `ms-outlook-listas-contactos_2026-11-06.html` | PASS | Definition and the classic name both stated by the new copy. |

## 3. Excerpts

| n | key | verdict | note |
|---|---|---|---|
| 1 | m06-l08-q231 | yes | Heading is the page section, right unit. |
| 2 | m06-l07-q037 | yes | |
| 3 | m06-l07-q038 | yes | |
| 4 | m06-l07-q039 | yes | Starts at the alias sentence; the «Nuevo email» step is just before it. Fact present. |
| 5 | m06-l07-q040 | yes | |
| 6 | m06-l07-q041 | yes | |
| 7 | m06-l07-q042 | yes | |
| 8 | m06-l07-q043 | yes | Flag (minor): carries the link text «¿Cómo sé si soy el propietario del grupo?» after the fact. |
| 9 | m06-l07-q045 | yes | |
| 10 | m06-l07-q347 | yes | |
| 11 | m06-l07-q348 | yes | Flag: garbled navigation tail «Puede: Crear una lista \| de contactosAgregar más contactos a una lista \| … \| de contactosEliminar una lista de contactos» (tab links, words run together). |
| 12 | m06-l07-q350 | yes | |
| 13 | m06-l07-q352 | yes | |
| 14 | m06-l07-q365 | yes | |

## Counts

- Check 1: 14 checked, 14 PASS, 0 FAIL. Prompt/options = HEAD 14/14; label, quote and «» exact 14/14. Style notes
  only: q039/q040 «Nuevo Email», q365 «Guardar & Cerrar» (neither misleads), q231 label is a sentence, not a heading.
- Check 2: 7 places, 7 PASS, 0 FAIL.
- Check 3: 14 items, 14 yes, 0 full-only, 0 no. Flags: n 11 (garbled tab-link tail), n 8 (link text, minor).
- No line added to `drops.tsv`.
