# m02-l05 — blind re-check 2 (R2d)

2026-11-18. Verifier: Opus, blind. Input: `pending.md` (17 rows); every id matches the lesson as it stands (recomputed
with `provenance.sentences`). Sources: `BOE-A-2015-10565_lpac_2024-11-06.pdf`, `BOE-A-1998-16718_ljca_2025-01-03.pdf`,
`BOE-A-2025-76_lo-1-2025-eficiencia-justicia_2025-06-04.pdf`.

Arts. 8–11 LJCA lead-ins: the 8.1/8.2/8.6 bullets have no lead-in; 9.1.d), 10.1.d)–e), 11.1.a)/d) are introduced
with «en lo que interesa a la Agencia Tributaria»; 12.1.a) and 12.1.b)–c) are separate sentences with «también». No
lead-in presents a partial list as the article's whole list.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `813721d9c2` | PASS | art. 121.2 LPAC | — | — |
| `caa74a246f` | PASS | art. 122.1 LPAC | governed by the citation of the next sentence in the paragraph; that next sentence («desde el día siguiente al silencio») is not pending and glosses «a partir del día siguiente a aquel en que, de acuerdo con su normativa específica, se produzcan los efectos del silencio administrativo» | — |
| `3c5320ad14` | PASS | art. 124.1–2 LPAC | — | — |
| `06567b05fb` | PASS | art. 124.1 LPAC | verbatim | — |
| `faa80add4a` | FAIL | art. 125.2 LPAC | does not say which plazo («el plazo» of interposición of the recurso extraordinario de revisión is left to the context); «desde la notificación» drops «de la resolución impugnada»; «la firmeza de la sentencia» glosses «desde que la sentencia judicial quedó firme» | El recurso extraordinario de revisión se interpone, cuando se trate de la causa a) del artículo 125.1 LPAC, dentro del plazo de cuatro años siguientes a la fecha de la notificación de la resolución impugnada; en los demás casos, el plazo es de tres meses a contar desde el conocimiento de los documentos o desde que la sentencia judicial quedó firme (art. 125.2 LPAC). |
| `a89f13576f` | FAIL | art. 126.3 LPAC | «Sin resolución» drops «sin haberse dictado y notificado la resolución»: a resolution dictated but not notified within three months still lets the recurso be taken as desestimado | Transcurrido el plazo de tres meses desde la interposición del recurso extraordinario de revisión sin haberse dictado y notificado la resolución, se entiende desestimado (art. 126.3 LPAC). |
| `9729e24ada` | PASS | arts. 125.2 y 126.3 LPAC | «causa de error de hecho del artículo 125.1» is causa a) | — |
| `9118b3f130` | FAIL | art. 8.2 LJCA | drops «en única o primera instancia» and «de los recursos que se deduzcan frente a»; «salvo nacimiento o extinción… de funcionarios de carrera» glosses «salvo que se refieran al nacimiento o extinción de la relación de servicio de funcionarios públicos de carrera», and the comma run after that «salvo» lets «sanciones…» and «reclamaciones…» read as part of the exception; «sanciones» drops «administrativas» | Los Juzgados de lo Contencioso-administrativo conocen, asimismo, en única o primera instancia de los recursos que se deduzcan frente a los actos administrativos de la Administración de las comunidades autónomas, salvo cuando procedan del respectivo Consejo de Gobierno, cuando tengan por objeto cuestiones de personal, salvo que se refieran al nacimiento o extinción de la relación de servicio de funcionarios públicos de carrera; las sanciones administrativas que consistan en multas no superiores a 60.000 euros y en ceses de actividades o privación de ejercicio de derechos que no excedan de seis meses; o las reclamaciones por responsabilidad patrimonial cuya cuantía no exceda de 30.050 euros (art. 8.2 LJCA). |
| `0c4b195406` | FAIL | art. 8.6 LJCA, último párrafo | drops the condition «requiriendo dicho acceso el consentimiento de su titular» and «a ello»/«tal» in the opposition clause | Los Juzgados de lo Contencioso-administrativo conocen también de las autorizaciones para la entrada en domicilios y otros lugares constitucionalmente protegidos que haya sido acordada por la Administración Tributaria en el marco de una actuación o procedimiento de aplicación de los tributos, aun con carácter previo a su inicio formal, cuando, requiriendo dicho acceso el consentimiento de su titular, este se oponga a ello o exista riesgo de tal oposición (art. 8.6 LJCA). |
| `727da1f64e` | PASS | art. 13 LJCA | a)–c) complete; faithful cut of b) | — |
| `6a71318b5e` | PASS | art. 1.3 LJCA | lead-in to a)–c), list complete | — |
| `c516f22786` | PASS | art. 46.1 LJCA | governed by the citation of the next sentence (seis meses for the acto presunto) | — |
| `c7a79575ee` | PASS | art. 46.4 LJCA | verbatim | — |
| `47242175ea` | FAIL | art. 25.1 LJCA | «perjuicio irreparable» drops «a derechos o intereses legítimos»; also drops «de la Administración pública» | El recurso contencioso-administrativo es admisible en relación con las disposiciones de carácter general y con los actos expresos y presuntos de la Administración pública que pongan fin a la vía administrativa, ya sean definitivos o de trámite, si estos últimos deciden directa o indirectamente el fondo del asunto, determinan la imposibilidad de continuar el procedimiento, producen indefensión o perjuicio irreparable a derechos o intereses legítimos (art. 25.1 LJCA). |
| `958aaf1271` | PASS | art. 42.2 LJCA, párrafo segundo | verbatim; the article does not number its items, the «1.–4.» are the table's | — |
| `25071419b2` | PASS | LPAC citations of the lesson | both ways: every LPAC article cited in parentheticals and «Cita» cells is listed and every listed article is cited; arts. 24.1, 47, 48, 106 and 109.2 appear only inside copied law text | — |
| `67f93dbc94` | PASS | LJCA citations of the lesson | both ways: every LJCA citation (incl. 3.b)–c), 10.1.d)–e), 44.2–3, 115.1, 128.2) is covered and every listed article is cited; LO 1/2025, LOPJ, LOREG and LOTC named in the prose have their own lines | — |

PASS 12 · FAIL 5
