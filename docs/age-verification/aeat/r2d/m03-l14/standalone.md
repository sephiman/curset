# m03-l14 standalone check (R2d)

| id | line | sentence (start) | problem | minimal fix |
|---|---|---|---|---|
| 1d7a9558d4 | 84 | Recibida esa documentación, se da audiencia por un plazo de 15 días... | «esa documentación» has no referent: the previous sentence (line 82, art. 4) names no documentation | Replace with «Recibido el expediente» or drop «esa documentación» for «Una vez tramitado el procedimiento» only if a verified sentence supports it; otherwise add the art. 5 sentence that names the documentation |
| 95a04b1d49 | 85 | Recibida la propuesta, se solicita el dictamen del Consejo de Estado... | «la propuesta» has no referent (no proposal is mentioned before it) | «Recibida la propuesta de resolución» |
| 3aceac12f8 | 95 | Recibida la copia del expediente y emitidos, en su caso, los informes... | «la copia del expediente» and «los informes» have no referent; the item before (art. 7, inicio) mentions neither | Drop «Recibida la copia del expediente y emitidos, en su caso, los informes,» and start at «Se da audiencia...» or add the art. 8.1-8.2 sentence |
| 35208f0217 | 112 | Recibida la copia y emitidos, en su caso, los informes... | «la copia» and «los informes» have no referent; lines 108-110 (art. 10) name neither | Same as line 95 |
| 9df239b93f | 810 | En estos casos, junto con la solicitud de suspensión de los órganos de la Administración... | «estos casos» points to a suspension request by Administration bodies, which appears only at lines 803-805; the previous sentence (809, art. 61.1) is about a legitimated party not appearing in first instance | «En el recurso de alzada ordinario interpuesto por órganos de la Administración, junto con la solicitud de suspensión...» |
| fea326b5d9 | 249 | Si el órgano competente estima pertinente examinar y resolver cuestiones no planteadas... | Repeats line 247 (art. 223.4 LGT) with a 10-day addition, two items later | Remove the repeated clause: «A los que estuvieren personados se les concede un plazo de 10 días...» or merge with line 247 |
| 87d41af554 | 388 | Salvo lo dispuesto en esos apartados, se aplican las normas reguladoras... | «esos apartados» has no referent in the sentence; the apartados (undécima.5, 6 y 7) appear only in the citation of the item before | «Salvo lo dispuesto en los apartados 5, 6 y 7 de esta disposición» |
| 39aee56463 | 242 | Ese examen se hace a partir del día siguiente al de la notificación... | «ese examen» has no antecedent noun; the previous sentence says only «para que se le ponga de manifiesto» | «Esa puesta de manifiesto se hace...» |
| 26ef0a30ad | 1005 | LGT (Ley 58/2003): arts. 7.2, 26.5, ... | Normativa mismatch (LGT). Missing: 26.4 (cited as «apartado 4 del artículo 26» at lines 276, 302, 586, 793, 914), 86 (line 788), 112 (line 656), disposición adicional undécima.5–7 (line 387). Listed but never cited: 221.1.a | Add 26.4, 86, 112 and «undécima.1–8»; remove 221.1.a |
| 25ba2eb3e2 | 1006 | RGRVA (RD 520/2005): arts. 2.1–2, ... | Normativa mismatch (RGRVA): lists 30.1–5 but the lesson cites only 30.1, 30.2, 30.3, 30.7, 30.9, 30.11–13; 30.4 and 30.5 are never cited | Replace «30.1–5» with «30.1–3» |

Flagged 10

## Fixes

| id | action | detail |
|---|---|---|
| 1d7a9558d4 | pool sentence added | art. 5.2 RGRVA sentence («El órgano competente para tramitar solicita al órgano que dictó el acto la remisión de una copia cotejada del expediente…») placed before «Recibida esa documentación» |
| 95a04b1d49 | pool sentence added | art. 5.4 RGRVA sentence («Concluido el trámite de audiencia, … formula la propuesta de resolución…») before «Recibida la propuesta» |
| 3aceac12f8 | pool sentence added | art. 8.2 RGRVA sentence («Acordado el inicio, … remite una copia cotejada del expediente…») before «Recibida la copia del expediente y emitidos…» |
| 35208f0217 | pool sentence added | art. 11.2 RGRVA first sentence of the pool paragraph, prepended in the same paragraph to «Recibida la copia y emitidos…» |
| 9df239b93f | reworded | «En estos casos, junto con la solicitud de suspensión» → «En el recurso de alzada ordinario, junto con la solicitud de suspensión» (art. 61.2 RGRVA checked: «el escrito de interposición del recurso de alzada ordinario podrá acompañarse de la solicitud de suspensión … En estos casos») |
| fea326b5d9 | removed | the art. 223.4 LGT copy of the «cuestiones no planteadas» rule; the fuller art. 26.2 RGRVA copy (10 days) is kept |
| 87d41af554 | reworded | «Salvo lo dispuesto en esos apartados» → «Salvo lo dispuesto en los apartados anteriores de esta disposición adicional» (disp. adic. undécima.8 LGT checked: «Salvo lo dispuesto en los apartados anteriores») |
| 39aee56463 | reworded | «Ese examen» → «Esa puesta de manifiesto» (art. 223.2 LGT checked: «para que se le ponga de manifiesto») |
| 26ef0a30ad | Normativa rebuilt | LGT: added 26.4, 86, 112, undécima.1–8 (was 1–4 y 8); removed 221.1.a |
| 25ba2eb3e2 | Normativa rebuilt | RGRVA: 30.1–5 → 30.1–3; also 5.3 → 5.2–4, 8.3–5 → 8.2–5, 11.3 → 11.2–3 for the added pool sentences |

Pool-check «not in pool»: 39aee56463, 87d41af554, 9df239b93f rewordings and the two Normativa lines (5 lines).
