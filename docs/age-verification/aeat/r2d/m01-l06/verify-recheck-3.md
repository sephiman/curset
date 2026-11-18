# Blind re-check 3 — `m01-l06`

2026-11-18. Verifier: Opus, blind (spec `r2d/spec-verify.md`). Input: `pending.md` (205 rows). Every id is present
unchanged in the current lesson (sha1 recomputed with `provenance.sentences`). Sources: `sources/normativa/`
BOE-A-2007-6115 (LO 3/2007), BOE-A-2004-21760 (LO 1/2004), BOE-A-1995-25444 (Código Penal), BOE-A-2022-11589
(Ley 15/2022), BOE-A-2023-5366 (Ley 4/2023), BOE-A-2013-12632 (RDL 1/2013), BOE-A-2006-21990 (Ley 39/2006).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `2f57f1a4d1` | PASS | art. 50.2 LO 3/2007 | — | — |
| `5125a02da2` | PASS | art. 50.3 LO 3/2007 | — | — |
| `a34bda3ec7` | PASS | art. 50.4 LO 3/2007 | «entre otros criterios» is the article's own words, quoted; not a cut legal list | — |
| `9eb9544713` | PASS | art. 50.5 LO 3/2007 | — | — |
| `5c74cde301` | PASS | art. 9 LO 1/2004 | «en este capítulo» rendered as «capítulo I del título I»; art. 9 is in that chapter | — |
| `8fe64dda5e` | PASS | art. 10 LO 1/2004 | — | — |
| `4d2f4b00a1` | PASS | art. 12 LO 1/2004 | — | — |
| `6f26850b31` | PASS | art. 19.4 LO 1/2004 | second sentence of 19.4, verbatim | — |
| `5d2ecba600` | PASS | art. 21.2 LO 1/2004 | «previstas en el apartado anterior» dropped; the item follows the 21.1 item | — |
| `821833db54` | PASS | arts. 148.4.º, 153.1, 171.4, 172.2, 468.2 Código Penal | lead-in to five CP precepts that follow the art. 89.5 LOPJ table; true as stated | — |
| `b7d3d664db` | PASS | art. 148.4.º Código Penal | — | — |
| `55a577f759` | PASS | art. 153.1 Código Penal | — | — |
| `876811b41b` | PASS | art. 171.4 Código Penal | verbatim; the «mitad superior» paragraph belongs to apartado 5 | — |
| `525aa8a7f4` | PASS | art. 171.4 Código Penal | — | — |
| `11cc35e235` | PASS | art. 172.2 Código Penal | first paragraph of 172.2 verbatim; the «mitad superior» and «pena inferior en grado» paragraphs are separate rules, not conditions of this one | — |
| `fa6ec1b5c6` | PASS | art. 172.2 Código Penal | — | — |
| `f9795338da` | PASS | art. 468.2 Código Penal | — | — |
| `b3e798f2b1` | PASS | art. 61.2 LO 1/2004 | «en este capítulo» rendered as «capítulo IV del título V»; art. 61 is in that chapter | — |
| `f6749338f5` | PASS | art. 5.3 Ley 15/2022 | — | — |
| `287ff1f86c` | PASS | art. 5.3 Ley 15/2022 | — | — |
| `eb8f63a23d` | PASS | art. 5.5 Ley 15/2022 | — | — |
| `d91825704d` | PASS | art. 5.5 Ley 15/2022 | — | — |
| `1a1f23c5be` | PASS | art. 5.5 Ley 15/2022 | — | — |
| `6541b3483b` | PASS | art. 41.2 Ley 15/2022 | 41.2 list of laws complete | — |
| `f677849c6b` | PASS | art. 46.1 Ley 15/2022 | — | — |
| `49f1f78909` | PASS | art. 50.2 Ley 15/2022 | faithful cut of 50.2; keeps consent, «no muy graves», resolución motivada and every alternative | — |
| `df131a9717` | PASS | art. 52.3 Ley 15/2022 | — | — |
| `c0bb9045d0` | PASS | art. 52.3 Ley 15/2022 | — | — |
| `c2ed6e0e6c` | PASS | art. 52.3 Ley 15/2022 | — | — |
| `19370c46d6` | PASS | art. 52.3 Ley 15/2022 | — | — |
| `570be3dd90` | PASS | art. 2 Ley 4/2023 | — | — |
| `5a24ad4b1c` | FAIL | Ley 4/2023, título I, capítulo I (rúbrica) | chapter-level line cuts the chapter heading «Criterios y líneas generales de actuación de los poderes públicos y órgano de participación ciudadana»; the list it introduces includes the Consejo de Participación (art. 9.2) | Los criterios y líneas generales de actuación de los poderes públicos y el órgano de participación ciudadana están en el capítulo I del título I (arts. 4–9 Ley 4/2023): |
| `95c046de76` | PASS | art. 4 Ley 4/2023 | — | — |
| `40c86d1072` | PASS | art. 6 Ley 4/2023 | — | — |
| `3b81c833bb` | PASS | art. 7.1 Ley 4/2023 | — | — |
| `fdc21f94c1` | PASS | art. 7.2 Ley 4/2023 | — | — |
| `dc67afae78` | PASS | art. 7.2 Ley 4/2023 | — | — |
| `583518081f` | PASS | art. 7.3 Ley 4/2023 | — | — |
| `533014e0b5` | PASS | art. 8.1 Ley 4/2023 | — | — |
| `5039c10cb8` | PASS | art. 8.2 Ley 4/2023 | — | — |
| `fab956005b` | PASS | art. 9.2 Ley 4/2023 | — | — |
| `a4fe638de9` | PASS | art. 10.1 Ley 4/2023 | — | — |
| `d9d3c22683` | PASS | art. 10.2 Ley 4/2023 | — | — |
| `b7e2fbee18` | PASS | art. 10.2 Ley 4/2023 | — | — |
| `5f3b417469` | PASS | art. 10.3 Ley 4/2023 | — | — |
| `4b1cd176b9` | PASS | art. 10.3 Ley 4/2023 | — | — |
| `cd51944770` | PASS | art. 10.3 Ley 4/2023 | — | — |
| `64e0f5e5c2` | PASS | art. 10.3 Ley 4/2023 | — | — |
| `d0430d2849` | PASS | art. 10.4 Ley 4/2023 | — | — |
| `c0fdc1938f` | PASS | art. 10.4 Ley 4/2023 | 10.4 list a)–c) complete | — |
| `af3d83b495` | PASS | art. 10.4 Ley 4/2023 | — | — |
| `bca4ccc212` | PASS | art. 10.4 Ley 4/2023 | — | — |
| `d4f1071790` | PASS | art. 10.5 Ley 4/2023 | — | — |
| `b4fe8053c4` | PASS | art. 10.6 Ley 4/2023 | — | — |
| `4f3e11d8f4` | PASS | art. 10.7 Ley 4/2023 | — | — |
| `f4d432e6d3` | PASS | arts. 11–42 Ley 4/2023 | chapter heading «Políticas públicas para promover la igualdad efectiva de las personas LGTBI»; sección 1.ª is art. 10, so «el resto» = arts. 11–42 is right | — |
| `a68172d933` | PASS | art. 11, art. 12, art. 13, arts. 11–13 Ley 4/2023 | heading and article titles match | — |
| `ce4e3e71e6` | PASS | art. 14, art. 15, arts. 14–15 Ley 4/2023 | heading and article titles match | — |
| `8d21b346a5` | PASS | art. 16, art. 17, art. 18, art. 19, arts. 16–19 Ley 4/2023 | heading and article titles match | — |
| `710b270c8a` | PASS | art. 17 Ley 4/2023 | right; structural only: this rule item sits as a sibling of the «Sección …» items, it would read better nested under the sección 4.ª item | — |
| `69a18b857e` | PASS | art. 19.2 Ley 4/2023 | verbatim, «salvo» kept; same structural remark as the art. 17 item | — |
| `7b73db3372` | PASS | art. 19.2 Ley 4/2023 | — | — |
| `f113991558` | PASS | art. 20, art. 21, art. 22, art. 23, art. 24, arts. 20–24 Ley 4/2023 | heading and article titles match | — |
| `d9d31a157d` | PASS | art. 25, art. 26, arts. 25–26 Ley 4/2023 | heading and article titles match | — |
| `173bff5473` | PASS | art. 27, art. 28, art. 29, arts. 27–29 Ley 4/2023 | heading and article titles match | — |
| `6ed595e066` | PASS | art. 30, art. 31, art. 32, art. 33, arts. 30–35 Ley 4/2023 | «O.A.» splits the item into two parser sentences; the item renders whole and right | — |
| `b8b0a3ccdf` | PASS | art. 34, art. 35 | parser fragment of the sección 8.ª item (split at «O.A.»); the item renders whole and right | — |
| `dcd352cf55` | PASS | art. 36, art. 37, art. 38, arts. 36–38 Ley 4/2023 | heading and article titles match | — |
| `72e5f6f600` | PASS | art. 39, art. 40, art. 41, arts. 39–41 Ley 4/2023 | heading and article titles match | — |
| `90e7aad277` | PASS | art. 42 Ley 4/2023 | heading and article title match | — |
| `9f62e92de0` | FAIL | Ley 4/2023, título II, capítulo I (rúbrica); arts. 44–51 | calls arts. 47–51 «el procedimiento»: arts. 48–51 regulate the change of name and the adecuación de documentos, not the procedure; the chapter heading is «Rectificación registral de la mención relativa al sexo de las personas y adecuación documental» | La rectificación registral de la mención relativa al sexo de las personas y la adecuación documental están en el capítulo I del título II (arts. 44–45 y 47–51 Ley 4/2023): |
| `b0eda0251d` | PASS | art. 44.1 Ley 4/2023 | — | — |
| `7858c8cee7` | PASS | art. 44.2 Ley 4/2023 | — | — |
| `04579a3c74` | PASS | art. 44.3 Ley 4/2023 | — | — |
| `5667030ded` | PASS | art. 44.4 Ley 4/2023 | — | — |
| `8509805d3e` | PASS | art. 44.4 Ley 4/2023 | — | — |
| `b7c237abac` | PASS | art. 44.4 Ley 4/2023 | — | — |
| `5c1170188d` | PASS | art. 44.4 Ley 4/2023 | — | — |
| `52fd01b1cf` | PASS | art. 44.5 Ley 4/2023 | — | — |
| `72678d160d` | PASS | art. 44.5 Ley 4/2023 | — | — |
| `ca6550e307` | PASS | art. 44.6 Ley 4/2023 | — | — |
| `3329aae784` | PASS | art. 44.6 Ley 4/2023 | — | — |
| `7b39fed3de` | PASS | art. 44.7 Ley 4/2023 | — | — |
| `e6e035f7df` | PASS | art. 44.8 Ley 4/2023 | — | — |
| `e19018719d` | PASS | art. 44.9 Ley 4/2023 | — | — |
| `5821b5c95f` | PASS | art. 44.10 Ley 4/2023 | — | — |
| `e0f95749a8` | PASS | art. 44.11 Ley 4/2023 | — | — |
| `86a99104ba` | PASS | art. 45 Ley 4/2023 | — | — |
| `895055cb80` | PASS | art. 47 Ley 4/2023 | — | — |
| `f8b3302f44` | PASS | art. 47 Ley 4/2023 | — | — |
| `381eacd297` | PASS | art. 48 Ley 4/2023 | — | — |
| `404bdb7731` | PASS | art. 49.1 Ley 4/2023 | — | — |
| `8d576c9b85` | PASS | art. 49.1 Ley 4/2023 | — | — |
| `b215c032e3` | PASS | art. 49.1 Ley 4/2023 | — | — |
| `271af68e4c` | PASS | art. 49.2 Ley 4/2023 | — | — |
| `9d1ea59475` | PASS | art. 49.3 Ley 4/2023 | cut of «a la mención registral relativa al sexo»; art. 49 is wholly about that adecuación, rule unchanged | — |
| `8a01b0e212` | PASS | art. 49.4 Ley 4/2023 | — | — |
| `8083eaa701` | PASS | art. 50.1 Ley 4/2023 | — | — |
| `e0e3c030b9` | PASS | art. 50.1 Ley 4/2023 | — | — |
| `031e264223` | PASS | art. 50.2 Ley 4/2023 | — | — |
| `4cab6f3150` | PASS | art. 51.1 Ley 4/2023 | — | — |
| `029afb1786` | PASS | art. 51.2 Ley 4/2023 | — | — |
| `a2fa7e71ca` | PASS | art. 51.3 Ley 4/2023 | — | — |
| `fc3bc170ba` | PASS | art. 52.1 Ley 4/2023 | — | — |
| `04fbd4ea35` | PASS | art. 52.1 Ley 4/2023 | — | — |
| `ed4cef42b5` | PASS | art. 52.1 Ley 4/2023 | — | — |
| `de28ab29c7` | PASS | art. 52.2 Ley 4/2023 | — | — |
| `450d849ada` | PASS | art. 52.3 Ley 4/2023 | — | — |
| `7f98f059bf` | PASS | art. 52.4 Ley 4/2023 | — | — |
| `eaa28c66a8` | FAIL | Ley 4/2023, título II, capítulo II (rúbrica) | «El resto» of arts. 52–61 although its first item is art. 52, already set out in the paragraph above; the chapter heading is «Políticas públicas para promover la igualdad real y efectiva de las personas trans» | Las políticas públicas para promover la igualdad real y efectiva de las personas trans del capítulo II del título II (arts. 52–61 Ley 4/2023), por secciones: |
| `b7a9f32c9b` | FAIL | Ley 4/2023, título II, capítulo II, sección 1.ª (rúbrica) | section heading cut: the norm reads «Líneas generales de actuación de los poderes públicos para promover la igualdad real y efectiva de las personas trans»; article titles right | Sección 1.ª, líneas generales de actuación de los poderes públicos para promover la igualdad real y efectiva de las personas trans (arts. 52–53 Ley 4/2023): Estrategia estatal para la inclusión social de las personas trans (art. 52) y participación de las personas trans (art. 53). |
| `e628b15e7c` | FAIL | Ley 4/2023, título II, capítulo II, sección 2.ª (rúbrica) | section heading cut: the norm reads «Medidas en el ámbito laboral para promover la igualdad real y efectiva de las personas trans»; article titles right | Sección 2.ª, medidas en el ámbito laboral para promover la igualdad real y efectiva de las personas trans (arts. 54–55 Ley 4/2023): fomento del empleo de las personas trans (art. 54) e integración sociolaboral de las personas trans (art. 55). |
| `80610abf8c` | FAIL | Ley 4/2023, título II, capítulo II, sección 3.ª (rúbrica) | section heading cut: the norm reads «Medidas en el ámbito de la salud para promover la igualdad real y efectiva de las personas trans»; article titles right | Sección 3.ª, medidas en el ámbito de la salud para promover la igualdad real y efectiva de las personas trans (arts. 56–59 Ley 4/2023): atención sanitaria integral a personas trans (art. 56), consentimiento informado (art. 57), formación del personal sanitario, investigación y seguimiento (art. 58) y protocolos de actuación en el ámbito de la salud y servicios especializados (art. 59). |
| `f42558286d` | FAIL | Ley 4/2023, título II, capítulo II, sección 4.ª (rúbrica) | section heading cut: the norm reads «Medidas en el ámbito educativo para promover la igualdad real y efectiva de las personas trans»; article titles right | Sección 4.ª, medidas en el ámbito educativo para promover la igualdad real y efectiva de las personas trans (arts. 60–61 Ley 4/2023): tratamiento del alumnado menor de edad conforme al nombre registral (art. 60) y protocolos de atención al alumnado trans y contra el acoso transfóbico (art. 61). |
| `986373e8c7` | PASS | arts. 62–75 Ley 4/2023 | title III heading faithful | — |
| `4bc5b1d2f2` | FAIL | Ley 4/2023, arts. 62–67 | «Las medidas generales … son:» presents the list as complete, but it leaves out art. 62.2 (prevención y detección por las Administraciones), art. 62.3 (personas empleadoras o prestadoras de bienes y servicios), art. 63.2 (organizaciones interesadas en el procedimiento administrativo), art. 66.2 (informe de los organismos de igualdad) and art. 67, párrafo segundo | El capítulo I del título III regula las medidas generales de protección y reparación (arts. 62–67 Ley 4/2023): |
| `b4dc857dbe` | PASS | art. 62.1 Ley 4/2023 | — | — |
| `158df67c72` | PASS | art. 62.4 Ley 4/2023 | — | — |
| `eceebed11d` | PASS | art. 63.1 Ley 4/2023 | — | — |
| `30e8a8d6b1` | PASS | art. 63.3 Ley 4/2023 | — | — |
| `cfdcf4271d` | PASS | art. 64 Ley 4/2023 | — | — |
| `ee44a1dcfb` | FAIL | art. 65 Ley 4/2023 | drops «en los términos establecidos por las leyes procesales», the condition on the legitimation | Sin perjuicio de la legitimación individual de las personas afectadas, los partidos políticos, las organizaciones sindicales, las organizaciones empresariales, las asociaciones profesionales de personas trabajadoras autónomas, las asociaciones de personas consumidoras y usuarias y las asociaciones y organizaciones legalmente constituidas que tengan entre sus fines la defensa y promoción de los derechos de las personas LGTBI o de sus familias estarán legitimadas, en los términos establecidos por las leyes procesales, para defender los derechos e intereses de las personas afiliadas o asociadas, en procesos judiciales civiles, contencioso-administrativos y sociales, siempre que cuenten con su autorización expresa, y para demandar en juicio la defensa de los intereses difusos cuando las personas afectadas sean una pluralidad indeterminada o de difícil determinación (art. 65 Ley 4/2023). |
| `31ff99eee1` | FAIL | art. 66.1 Ley 4/2023 | drops «De acuerdo con lo previsto en las leyes procesales y reguladoras de los procedimientos administrativos», the frame the burden-of-proof rule applies within | De acuerdo con lo previsto en las leyes procesales y reguladoras de los procedimientos administrativos, cuando la parte actora o la persona interesada alegue discriminación por razón de orientación e identidad sexual, expresión de género o características sexuales y aporte indicios fundados sobre su existencia, corresponderá a la parte demandada o a quien se impute la situación discriminatoria la aportación de una justificación objetiva y razonable, suficientemente probada, de las medidas adoptadas y de su proporcionalidad (art. 66.1 Ley 4/2023). |
| `31c53adf5d` | PASS | art. 67 Ley 4/2023 | — | — |
| `d1bba2395e` | PASS | art. 68 Ley 4/2023 | — | — |
| `6a072975e5` | PASS | art. 68 Ley 4/2023 | — | — |
| `0885074be0` | PASS | art. 68 Ley 4/2023 | art. 68 list a)–d) complete | — |
| `f0228ae86f` | PASS | art. 68 Ley 4/2023 | — | — |
| `95e0bc24b9` | PASS | art. 68 Ley 4/2023 | — | — |
| `affea35eb9` | PASS | art. 68 Ley 4/2023 | — | — |
| `8e48785355` | PASS | art. 69.1 Ley 4/2023 | — | — |
| `00d44b4bd8` | PASS | art. 69.2 Ley 4/2023 | — | — |
| `3ededd391f` | PASS | art. 69.3 Ley 4/2023 | — | — |
| `a305532a89` | PASS | art. 70, art. 71, art. 72, art. 73, art. 74, art. 75 | chapter III heading and article titles 70–75 match | — |
| `aa4f2f5664` | PASS | art. 74, art. 74.2 Ley 4/2023 | — | — |
| `7057b47267` | PASS | art. 74, art. 74.2 Ley 4/2023 | — | — |
| `1bd2f1e19e` | PASS | arts. 76–82 Ley 4/2023 | — | — |
| `7707c31fe9` | PASS | art. 76.1 Ley 4/2023 | — | — |
| `36e77abd2a` | PASS | art. 76.1 Ley 4/2023 | — | — |
| `3016479c63` | PASS | art. 76.1 Ley 4/2023 | — | — |
| `f8115cff36` | PASS | art. 76.1 Ley 4/2023 | — | — |
| `86fa48a378` | PASS | art. 76.1 Ley 4/2023 | — | — |
| `622bd939de` | PASS | art. 76.2 Ley 4/2023 | — | — |
| `d499a7befc` | PASS | art. 76.2 Ley 4/2023 | — | — |
| `5c5c1f51cf` | PASS | art. 76.2 Ley 4/2023 | — | — |
| `7609271cdd` | PASS | art. 76.3 Ley 4/2023 | — | — |
| `0b2ad107d2` | PASS | art. 77.1 Ley 4/2023 | — | — |
| `62aa994b83` | PASS | art. 77.1 Ley 4/2023 | — | — |
| `cc8f695e92` | PASS | art. 77.2 Ley 4/2023 | — | — |
| `ec30a06509` | PASS | art. 77.2 Ley 4/2023 | — | — |
| `eb8c37abe3` | PASS | art. 78 Ley 4/2023 | — | — |
| `d88310ad76` | PASS | art. 79.1 Ley 4/2023 | — | — |
| `b5a7efe4a1` | PASS | art. 79.2 Ley 4/2023 | — | — |
| `97007d3d86` | PASS | art. 79.2 Ley 4/2023 | — | — |
| `21a7a30334` | PASS | art. 79.2 Ley 4/2023 | — | — |
| `82b6f6f6ff` | PASS | art. 79.2 Ley 4/2023 | 79.2 list a)–c) complete | — |
| `a72173ab2d` | PASS | art. 79.3 Ley 4/2023 | — | — |
| `c09cb516f2` | PASS | art. 79.3 Ley 4/2023 | — | — |
| `0313f72e1a` | PASS | art. 79.3 Ley 4/2023 | — | — |
| `50854d62be` | PASS | art. 79.3 Ley 4/2023 | 79.3 list a)–c) complete | — |
| `b306d903f9` | PASS | art. 79.4 Ley 4/2023 | — | — |
| `e9de94d720` | PASS | art. 79.4 Ley 4/2023 | — | — |
| `505b15b20e` | PASS | art. 79.4 Ley 4/2023 | — | — |
| `a971ba6a12` | PASS | art. 79.4 Ley 4/2023 | — | — |
| `8efbd593bc` | PASS | art. 79.4 Ley 4/2023 | — | — |
| `88e0dd27c7` | PASS | art. 79.4 Ley 4/2023 | — | — |
| `93af353b90` | PASS | art. 79.4 Ley 4/2023 | — | — |
| `e1e842fe8d` | PASS | art. 79.4 Ley 4/2023 | 79.4 list a)–i) complete | — |
| `c15efa35ee` | PASS | art. 79.4 Ley 4/2023 | — | — |
| `217d4f3315` | PASS | art. 79.4 Ley 4/2023 | — | — |
| `3c45c666e2` | PASS | art. 80 Ley 4/2023 | — | — |
| `6b36e1cb16` | PASS | art. 80.1 Ley 4/2023 | — | — |
| `2ae756c0a1` | PASS | art. 80.2 Ley 4/2023 | — | — |
| `e0fd2cae93` | PASS | art. 80.2 Ley 4/2023 | 80.2 accessory list a)–c) complete, in order | — |
| `6928e8526f` | PASS | art. 80.3 Ley 4/2023 | — | — |
| `ab483f1278` | PASS | art. 80.3 Ley 4/2023 | 80.3 accessory list a)–e) complete, in order | — |
| `afb1b17b40` | PASS | art. 80.4 Ley 4/2023 | — | — |
| `e7be26746d` | PASS | art. 80.4 Ley 4/2023 | — | — |
| `19bdea2f70` | PASS | art. 80.4 Ley 4/2023 | — | — |
| `e75c4da1b3` | PASS | art. 80.4 Ley 4/2023 | — | — |
| `0a031e9884` | PASS | art. 80.4 Ley 4/2023 | — | — |
| `dfb761ba88` | PASS | art. 80.4 Ley 4/2023 | — | — |
| `ad7a1a8a01` | PASS | art. 80.4 Ley 4/2023 | — | — |
| `cbc8a67ecf` | PASS | art. 80.4 Ley 4/2023 | — | — |
| `b9abf7f4cb` | PASS | art. 80.4 Ley 4/2023 | — | — |
| `93fca6be11` | PASS | art. 80.4 Ley 4/2023 | 80.4 criteria a)–h) complete | — |
| `fdd9633fe9` | PASS | art. 80.5 Ley 4/2023 | — | — |
| `02955e85b5` | PASS | art. 80.6 Ley 4/2023 | — | — |
| `538e43bbb2` | PASS | art. 81.1 Ley 4/2023 | — | — |
| `a5bcdcebae` | PASS | art. 81.2 Ley 4/2023 | — | — |
| `8e8eff0282` | PASS | art. 82 Ley 4/2023 | «ni otorgarán» for the norm's «u otorgarán»; same rule | — |
| `25a280abac` | PASS | art. 2.m) RDL 1/2013 | split of 2.m) «supone una discriminación … y la violación del derecho a la no discriminación»; content right | — |
| `b9ad761cd1` | PASS | art. 2.m) RDL 1/2013 | — | — |
| `d97f13ccd6` | PASS | art. 33.2 Ley 39/2006 | — | — |
| `df038f21cc` | FAIL | Normativa; CP named in arts. 89.5.a) and g) LOPJ (esquema rows), 7.1 LO 3/2007 | cited articles right (148.4.º, 153.1, 171.4, 172.2, 468.2); missing art. 468, named in the art. 89.5.g) LOPJ row («artículo 468 del Código Penal») | Código Penal: arts. 148.4.º, 153.1, 171.4, 172.2 y 468.2; art. 468 y título VIII del libro II, nombrados en el art. 89.5 LOPJ; nombrado, sin precepto citado, en el art. 7.1 LO 3/2007. |
| `b06e5034df` | PASS | Ley 4/2023 (trans y LGTBI) | every art. 1–82 cited (ranges and per-article citations); nothing outside | — |
| `fd8da25272` | PASS | LGSS (RDL 8/2015) | named in 21.2 and 21.5 LO 1/2004 only | — |
| `f05a760f0b` | FAIL | Normativa; Ley 40/2015 named in arts. 41.1, 41.2, 46.1 Ley 15/2022 and 9.2, 76.1 Ley 4/2023 | missing art. 22.3, named in the art. 9.2 Ley 4/2023 sentence, and the naming without precept in art. 76.1 Ley 4/2023 («Ley 39/2015 y en la Ley 40/2015») | Ley 40/2015 (LRJSP): art. 109, nombrado en el art. 41.1 Ley 15/2022; art. 22.3, nombrado en el art. 9.2 Ley 4/2023; nombrada, sin precepto citado, en los arts. 41.2 y 46.1 Ley 15/2022 y en el art. 76.1 Ley 4/2023. |
| `2aba6224bb` | FAIL | Normativa; Ley 39/2015 named in arts. 2.4.e), 40.b), 41.2, 46.1 Ley 15/2022 and 76.1 Ley 4/2023 | missing the naming without precept in art. 76.1 Ley 4/2023 («Los procedimientos sancionadores se regirán por lo dispuesto en la Ley 39/2015 y en la Ley 40/2015») | Ley 39/2015 (LPAC): arts. 2.2 y 112, nombrados en los arts. 2.4.e) y 40.b) Ley 15/2022; nombrada, sin precepto citado, en los arts. 41.2 y 46.1 Ley 15/2022 y en el art. 76.1 Ley 4/2023. |
| `ece36f92a7` | PASS | LGP (Ley 47/2003) | named only in 41.2 Ley 15/2022 | — |
| `47da0a9537` | PASS | RGPD (Reglamento (UE) 2016/679) | 4.2.p), 4.2.q) Ley 39/2006 rows and 7.3 Ley 4/2023 sentence; complete | — |
| `f1ed1295cc` | PASS | LOPDGDD (LO 3/2018) | complete | — |
| `b1f268e47d` | PASS | TREBEP (RDL 5/2015) | complete | — |
| `d1031c63fd` | PASS | Ley 8/1989 (Tasas y Precios Públicos) | complete | — |
| `5e142cf21f` | PASS | sin fichero | each norm checked at its naming article (LECrim 89.5 LOPJ, 62 LO 1/2004, 69.1 Ley 4/2023; Ley 15/2015 89.6.g) LOPJ, 47 Ley 4/2023; Ley 19/2007 3.1.ñ) Ley 15/2022; Ley 12/2009 and RD 1325/2003 5.1 Ley 39/2006; Ley 14/1986 11.1.c) Ley 39/2006; Directiva 95/46/CE 4.2.p) Ley 39/2006; Convención 1.a) RDL 1/2013; etc.); none missing, none in normativa.yaml | — |

PASS 192 · FAIL 13
