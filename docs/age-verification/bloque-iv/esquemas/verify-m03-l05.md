# Verification — m03-l05, art. 69.3 LPAC sentence and the «Efectos» column (2026-10-18)

The reviewer did not write this change or the lesson. Scope: `git diff C/es/lessons/m03-l05.md` (one hunk) against
the open item in `docs/age-theory-ledger.md` («m03-l05 prose, art. 69.3 párr. 2») and `../../bloque-iii/esquemas/fixes.md`
row 5. Rules: `spec.md` (this folder, which defers to bloque III) and `docs/prose-voice.md`. Source: the scratchpad
`txt/BOE-A-2015-10565_lpac_2024-11-06.clean` (LPAC consolidated 2024-11-06), art. 69 read with `art.py lpac_ 69`.
No source was taken from memory.

| # | item | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|
| 1 | Prose l. 42–43, new sentence «La comunicación podrá presentarse dentro de un plazo posterior al inicio de la actividad cuando la legislación correspondiente lo prevea expresamente (art. 69.3 LPAC).» | PASS | Art. 69.3 párr. 2: «No obstante lo dispuesto en el párrafo anterior, la comunicación podrá presentarse dentro de un plazo posterior al inicio de la actividad cuando la legislación correspondiente lo prevea expresamente.» Verbatim from «la comunicación» to the end; subject (only the comunicación), the condition («cuando la legislación correspondiente lo prevea expresamente») and «expresamente» kept. Dropping «No obstante lo dispuesto en el párrafo anterior» does not change the meaning: the sentence follows directly the párr. 1 sentence and its content («posterior al inicio de la actividad») marks the exception by itself; nothing wider is stated (it does not extend to the declaración responsable). Citation right (párr. 2 sits in apartado 3). Voice: Peninsular, one fact, no filler, no «no obstante» tic, no coined term; 25 words is the norm's own wording, which a verbatim fragment keeps. | — |
| 2 | Tabla row «Declaración responsable», «Qué es» | PASS | Unchanged from the previous round (diff shows only the added cell). Art. 69.1 párr. 1, faithful shortening («éste» and «de tiempo» dropped; no condition lost). Same text in prose l. 30–34. | — |
| 3 | Tabla row «Declaración responsable», «Efectos» | PASS | Art. 69.3 párr. 1: «permitirán, el reconocimiento o ejercicio de un derecho o bien el inicio de una actividad, desde el día de su presentación, sin perjuicio de las facultades de comprobación, control e inspección que tengan atribuidas las Administraciones Públicas». Faithful shortening, identical to the prose sentence l. 40–42 («…de la Administración»). Párr. 2 rightly absent: it concerns only the comunicación. Not wider. | — |
| 4 | Tabla row «Declaración responsable», citation «arts. 69.1 y 69.3 LPAC» | PASS | Definition from 69.1, effects from 69.3; both citations carried by the prose. | — |
| 5 | Tabla row «Comunicación», «Qué es» | PASS | Unchanged. Art. 69.2, faithful shortening («aquel» → «El», «Pública» dropped after «Administración»). Same text in prose l. 36–38. | — |
| 6 | Tabla row «Comunicación», «Efectos» | PASS | First sentence: art. 69.3 párr. 1, as in row 3. Second sentence «Podrá presentarse dentro de un plazo posterior al inicio de la actividad cuando la legislación correspondiente lo prevea expresamente»: art. 69.3 párr. 2 verbatim with the subject elided (the row is the comunicación). Condition kept, so the row no longer drops párr. 2 (the bloque III FAIL) and is not wider. Both facts now in prose (l. 40–43). | — |
| 7 | Tabla row «Comunicación», citation «arts. 69.2 y 69.3 LPAC» | PASS | Definition 69.2, both effect sentences 69.3; both in prose. | — |
| 8 | Placement | PASS | The esquema still follows the three paragraphs it summarises (l. 30–43). | — |
| 9 | Nothing else changed | PASS | `git diff --stat`: 1 file, 6 insertions, 5 deletions, one hunk (l. 39–50): the prose line «LPAC).» extended with the new sentence, and the four table lines rewritten for the new column (header, separator, two rows). «Qué es» cells and «Documento» labels byte-identical to before. No other line in the file touched. | — |

## Notes

- The bloque IV spec says «the lesson diff only adds lines». This change is the separate R2 prose fix the ledger's open
  item called for, so a modified prose line is expected here; the rewritten table lines are what a new column requires.
- The «Efectos» cell of the comunicación row repeats párr. 1 and adds párr. 2; the declaración row has párr. 1 only. That
  asymmetry is the article's own (párr. 2 names only «la comunicación»), not a gap.
- The course has no EN tree (`C/en` does not exist), so there is no mirror to keep in step.
- The ledger open item 1 (`docs/age-theory-ledger.md`, «Open items» after esquemas bloque III) can be closed by the writer
  once this change is accepted; the reviewer did not edit it.

## Counts

9 items: 9 PASS, 0 FAIL.
