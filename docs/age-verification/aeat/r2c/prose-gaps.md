# Prose gaps fixed (2026-11-11)

Each gap was in the prose and in the esquema row. The rule was added in the article's own words with its inline citation, then the row was made to carry it. Nothing committed. `tests/test_esquema.py` passes (10); `taxprov.py plan` lists only esquema rows plus table headers.

## m03-l03
- `56de3bb17e`, `837f0f90ed`: line 146 (new paragraph, then list a)–d) and the closing sentences, lines 146–155): art. 27.2 LGT regularisation of other periods with conditions a)–d), the consequence of failing any of them, and art. 27.4 LGT. Rows: label of both rows now carries the exception and the art. 27.4 requirement; Cita is «arts. 27.2 y 27.4 LGT». Normativa: 27.1–2, 27.4–5.

## m03-l04
- `2ee25e2671`: line 294, art. 17.2 párrafo 2 RGAT exception added after the three-month sentence (state competence; the personal-tax model if its plazo ends first; «salvo que se hubiese efectuado con anterioridad»). Row: the plazo cell now carries the exception. Normativa unchanged (17.1–3).

## m03-l06
- `e226ce5ea7`: line 157, art. 40.2 LIS párrafo 2 (last period shorter than a year). Row: base cell of the general modalidad carries it.
- `d9532db64c`: line 169, art. 40.3 LIS párrafo 2 (periods not matching the calendar year; base by days elapsed, and what the payment is on account of). Row: base cell of the option modalidad carries the base for those contribuyentes. Normativa unchanged (40.1–5).

## m03-l14
- `2ebd233b74`: line 222, art. 235.1 LGT párrafo 4 (factura). Row: plazo cell now has all dies a quo (notificación, constancia, silencio, deudas periódicas, factura).
- `7d110daaae`: line 246, art. 242.2 párrafo 2 LGT (órgano not notified; conocimiento del contenido esencial). Row: cell carries it. Title unchanged (rows stay one per recurso). Normativa unchanged.

## m03-l16
- `cd815e171f`: line 100, art. 58.1 párrafo 2 (tutela y acogimiento, dependencia) and art. 58.2 párrafo 2 (adopción o acogimiento, three períodos; no inscription case). Row: «Por descendientes» cell carries both.
- `892243002c`: art. 59.1 párrafo 2 (ascendientes internados), in the ascendientes paragraph after the 59 sentence. Row: «Por ascendientes» cell carries it. Normativa unchanged (57–61).

## m03-l17
- `bedb82a652`: line 187 (list of two items after the art. 26.1 paragraph): DA 15.ª.1 LIS, 50 % / 25 % for cifra de negocios at least 20 / 60 millones, periods starting on or after 1-1-2024. The 70 % sentence in the first paragraph now says «salvo lo dispuesto … en la disposición adicional decimoquinta.1 LIS». «Lo que más cae» item on the 70 % limit carries the 50 % / 25 % rule. Row «Límite de la compensación» kept as the art. 26.1 rule; new second row for DA 15.ª.1 (citations cannot be combined in one cell: the loader needs one resolvable citation per row). The 70 % mentions in the later exceptions (extinction, new entities) are the exceptions of art. 26.1 and 26.3 as written and were left. Normativa: added «disposición adicional decimoquinta.1». Four unresolved `cites.py` items remain, all pre-existing «disposición transitoria cuadragésima cuarta» citations (lines 234–239).

## Second pass

- m03-l06 `967785ce3e`: prose (line 169) now adds, after the five-sevenths sentence, DA 14.ª.1.b) LIS (nineteen twentieths, redondeado por exceso, at least 10 millones) and DA 14.ª.1.a) LIS (23 % minimum of the resultado positivo de la cuenta de pérdidas y ganancias, minorado en los pagos fraccionados anteriores; the 25 % case, exclusions and exceptions of párrafos 2–6 left out). Row: the Porcentaje cell points to DA 14.ª.1 for the 10 millones case; Cita stays art. 40.3 LIS. Normativa: added disposición adicional decimocuarta.1.
- m03-l19 `b169819130`, `7abe2c7c75`: art. 99.Tres último párrafo (ventas ocasionales, art. 5.Uno.e) and art. 99.Cinco párrafo tercero (concurso) added to the prose after the related rules and to both rows. The concurso rectification and requerimiento paragraphs of 99.Tres stay out. Normativa unchanged.
- m03-l17 line 141: DA 15.ª.1 LIS replaces the art. 11.12 limit too; sentence added after the art. 11 sentence. No row cites art. 11.12; Normativa already lists DA 15.ª.1.
