# Excerpt verification — report, part 3 (items 101–126, pass 2)

Blind opus verifier, `sample-3.jsonl` (re-drawn on purpose: 101–112 are the items fixed after pass 1; 113–126 the 14
questions that gained an excerpt from the key-token rule). Saved by the coordinator from the verifier's returned text.

Counts: **18 yes, 0 full-only, 8 no** (113, 117, 119, 120, 121, 122, 123, 125). Flags: 118, 122, 123, 124 garbled;
108, 109, 110, 116, 126 leaks, run-ins or an unmarked cut. All 8 misses come from saved documentation pages.

| n | key | verdict | note |
|---|---|---|---|
| 101 | m01-l06-ex-1/m01-l06-q007 | yes | «España se unió a la OGP en el mismo año de su fundación» plus «fundada en septiembre de 2011». |
| 102 | m06-l07-ex-3/m06-l07-q053 | yes | Right-click on the folder › Propiedades › pestaña Permisos › Agregar. |
| 103 | m06-l02-ex-10/m06-l02-q358 | yes | The table row for Ctrl+Mayús+teclas de dirección. |
| 104 | m05-l03-ex-4/m05-l03-q115 | yes | Subapartado 2.2 in full: art. 107 «y teniendo en cuenta criterios de gestión eficiente de tesorería». |
| 105 | m06-l03-ex-8/m06-l03-q268 | yes | «&p — Imprimir el número de página.» |
| 106 | m06-l07-ex-5/m06-l07-q134 | yes | The hasattachment:yes row. |
| 107 | m04-l02-ex-1/m04-l02-q011 | yes | Para. 3 of 18.6: «será aprobada por el Gobierno a propuesta del Ministerio…». |
| 108 | m04-l01-ex-3/m04-l01-q060 | yes | «20. Sentencias firmes relacionadas con su condición de funcionario.» FLAG: lead-in of apartado 1 straight to item 20, without the «a) Para el personal funcionario de carrera…» line and items 1–19, and no «[…]» marking the cut. |
| 109 | m06-l06-ex-7/m06-l06-q248 | yes | The vista Diseño sentence. FLAG (minor): term label runs into the definition («vista Diseño La vista Diseño…»). |
| 110 | m06-l06-ex-1/m06-l06-q001 | yes | «(tablas, consultas, formularios, informes, macros y módulos)». FLAG (minor): «Rendimiento mejorado El rendimiento…». |
| 111 | m04-l05-ex-9/m04-l05-q253 | yes | «dos años en el Cuerpo o Escala a que pertenezcan». |
| 112 | m04-l07-ex-1/m04-l07-q015 | yes | 8.1.b) «pierdan tal condición, cualquiera que sea la causa». |
| 113 | m01-l01-ex-1/m01-l01-q010 | no | Garbled fragment crossing records of the XML; joins the 2024 reform's id to the 2004 Declaración's text. The four «SE MODIFICA» records are not shown. |
| 114 | m01-l06-ex-1/m01-l06-q003 | yes | «adopted by the OECD Council on 14 December 2017». |
| 115 | m01-l06-ex-2/m01-l06-q025 | yes | «Avances del I Plan de Gobierno Abierto 2012-2014». |
| 116 | m01-l06-ex-2/m01-l06-q026 | yes | «Avances del III Plan de Gobierno Abierto 2017-2019». FLAG: navigation text leaks in first. |
| 117 | m01-l06-ex-2/m01-l06-q027 | no | Navigation menu text only. The source has «Avances del IV Plan de Gobierno Abierto 2020-2024». |
| 118 | m01-l06-ex-3/m01-l06-q043 | yes | «Resolución aprobada por la Asamblea General el 25 de septiembre de 2015». FLAG garbled: split words, page footer inside. |
| 119 | m01-l06-ex-3/m01-l06-q054 | no | The site menu's label «Objetivo 15: Bosques…», not the body heading «Objetivo 15: Vida de ecosistemas terrestres». |
| 120 | m01-l06-ex-3/m01-l06-q055 | no | Wrong passage (official development assistance) instead of meta 15.6. FLAG garbled: split words. |
| 121 | m01-l06-ex-3/m01-l06-q057 | no | Menu label «Objetivo 16: Paz y justicia» instead of «Paz, justicia e instituciones sólidas»; could mislead. |
| 122 | m06-l01-ex-1/m06-l01-q031 | no | MB and GiB rows, not the 1 GB row. FLAG garbled: superscripts flattened («106 B»). |
| 123 | m06-l01-ex-1/m06-l01-q032 | no | Same excerpt as 122; 1 GB = 1.000 MB cannot be worked out. |
| 124 | m06-l01-ex-2/m06-l01-q037 | yes | «1 MiB = 220 B = 1 048 576 B». FLAG: superscripts flattened. |
| 125 | m06-l01-ex-2/m06-l01-q038 | no | The diskette sentence instead of the Kibit row. |
| 126 | m06-l01-ex-2/m06-l01-q040 | yes | IEC 1998 sentence. FLAG: caption repeated before it. |

## Misses and flags grouped by cause (verifier's grouping)

1. Wrong sentence or row picked from a documentation page: 117, 120, 122, 123, 125.
2. The site's navigation labels preferred over the body heading: 119, 121 (116, 117 for the leak).
3. Sentence splitting on «art.» in structured XML, records joined: 113.
4. Garbled PDF text (split words, footers): 118, 120.
5. Flattened superscripts in the NIST tables: 122, 123, 124.
6. Caption or term labels run into the text: 109, 110, 126 (cosmetic).
7. Unmarked cut inside a list: 108.
