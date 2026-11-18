# m02-l01 — verify re-check 4 (blind, Opus)

Lesson text read 2026-11-18; every pending sentence matches the lesson verbatim (ids current).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `8484a4b985` | PASS | art. 150.2 CE | second sentence of 150.2, verbatim in the present tense | — |
| `ee409631d5` | PASS | art. 24.1.e) Ley 50/1997 | first clause of letter e), verbatim; the form clause is in the esquema row e) just above | — |
| `a04c5f531e` | PASS | art. 290.1, párrafo segundo, TFUE | faithful; only «por lo tanto» dropped | — |
| `8057e8524f` | FAIL | art. 4.3 TUE | text verbatim, but out of the norm's order: the paragraph at line 478 («Los Estados miembros adoptan todas las medidas apropiadas…», 4.3 párrafo segundo) comes before this one (4.3 párrafo primero). Structural fix: move the line-481 paragraph (this sentence and `956b9b36b5`) above line 478, or move line 478 between the two sentences of line 481 | Conforme al principio de cooperación leal, la Unión y los Estados miembros se respetan y asisten mutuamente en el cumplimiento de las misiones derivadas de los Tratados (art. 4.3 TUE). |
| `956b9b36b5` | PASS | art. 4.3, párrafo tercero, TUE | verbatim | — |

PASS 4 · FAIL 1
