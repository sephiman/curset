# Verify — `m03-l15` (R2d, blind)

2026-11-14. Verifier: Opus, blind (no writer.md, no earlier verify*.md opened). Sources: `content/aeat-agentes-hacienda/sources/normativa/` (text extracted with pdftotext), `normativa.yaml`, `docs/age-verification/aeat/r1/rdl-29-2026-revert-list.md`.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `70ca871baa` | PASS | art. 40.1–2 LIRPF | — | — |
| `0423ac636b` | PASS | art. 41 LIRPF | — | — |
| `86980bc332` | PASS | art. 7 LIRPF | list a)–z) complete, 27 letters with ñ, in order | — |
| `48de3ced42` | PASS | art. 7.b) LIRPF | — | — |
| `588f1c2e31` | PASS | art. 7.c) LIRPF | — | — |
| `ae2e939ed9` | FAIL | art. 7.d), párrafos 2.º y 3.º LIRPF | the accident-insurance exemption also has the limit «hasta la cuantía que resulte de aplicar … el sistema para la valoración de los daños … en accidentes de circulación» and covers only «indemnizaciones por daños personales»; the sentence places the limit before it, so the insurance part reads unlimited; drops «legalmente establecido» and «no previstas en el párrafo anterior» | Asimismo, las indemnizaciones por daños físicos o psíquicos satisfechas por la entidad aseguradora del causante del daño, no previstas en el párrafo anterior, cuando deriven de un acuerdo de mediación o de cualquier otro medio adecuado de solución de controversias legalmente establecido, siempre que haya intervenido un tercero neutral y el acuerdo se haya elevado a escritura pública, hasta la cuantía que resulte de aplicar el sistema para la valoración de los daños y perjuicios causados a las personas en accidentes de circulación; e igualmente las indemnizaciones por daños personales derivadas de contratos de seguro de accidentes, salvo aquellos cuyas primas hubieran podido reducir la base imponible o ser consideradas gasto deducible, hasta esa misma cuantía. |
| `5960a74659` | PASS | art. 7.e), párrafo 1.º LIRPF | — | — |
| `69ec1c73c0` | PASS | art. 7.e), párrafo 2.º LIRPF | — | — |
| `62c2e290b6` | PASS | art. 7.e), último párrafo LIRPF | — | — |
| `47c58e5dbe` | FAIL | art. 7.f) LIRPF | the limit «prestación máxima que reconozca la Seguridad Social» applies only to the mutualidades' prestaciones; as written it also caps the Seguridad Social's incapacidad permanente absoluta and gran invalidez prestaciones, which the article exempts without limit; the article also says the mutualidad covers «profesionales no integrados» in the RETA | f) Las prestaciones reconocidas al contribuyente por la Seguridad Social o por las entidades que la sustituyan como consecuencia de incapacidad permanente absoluta o gran invalidez; y las reconocidas a los profesionales no integrados en el régimen especial de trabajadores autónomos por las mutualidades de previsión social alternativas a ese régimen en situaciones idénticas, estas con el límite de la prestación máxima que reconozca la Seguridad Social por el concepto que corresponda. |
| `7b2941d3ae` | FAIL | art. 7.h) LIRPF | drops the narrowing «percibidos de los regímenes públicos de la Seguridad Social y clases pasivas» for the orfandad pensions, and the second and third paragraphs (mutualidades alternativas; empleados públicos sin derecho a la prestación, with the limit of the prestación máxima) | h) Las prestaciones por maternidad o paternidad y las familiares no contributivas reguladas en la Ley General de la Seguridad Social, y las pensiones y los haberes pasivos de orfandad y a favor de nietos y hermanos, menores de veintidós años o incapacitados para todo trabajo, percibidos de los regímenes públicos de la Seguridad Social y clases pasivas; las prestaciones de las mutualidades de previsión social alternativas al régimen especial de trabajadores autónomos en situaciones idénticas y la retribución de los empleados públicos sin derecho a esa prestación durante los permisos por parto, adopción o guarda y paternidad, en ambos casos con el límite de la prestación máxima que reconozca la Seguridad Social; y las demás prestaciones públicas por nacimiento, parto o adopción múltiple, adopción, maternidad o paternidad, hijos a cargo y orfandad. |
| `0ac666c600` | PASS | art. 7.i) LIRPF | — | — |
| `e73e62ee55` | FAIL | art. 7.j), párrafo 2.º LIRPF | «las becas para investigación» is broader than the article: only research becas «en el ámbito descrito por el Real Decreto 63/2006» and those granted for research to public employees and university teaching and research staff | j) Las becas públicas, las concedidas por las entidades sin fines lucrativos a las que sea de aplicación su régimen especial y las concedidas por las fundaciones bancarias en el desarrollo de su actividad de obra social, percibidas para cursar estudios reglados, tanto en España como en el extranjero, en todos los niveles y grados del sistema educativo, y, en los términos que reglamentariamente se establezcan, las becas de esas mismas entidades para investigación en el ámbito del Real Decreto 63/2006 y las otorgadas con fines de investigación a los funcionarios y demás personal al servicio de las Administraciones públicas y al personal docente e investigador de las universidades. |
| `50a2a327ba` | PASS | art. 7.k) LIRPF | — | — |
| `9b6512c323` | PASS | art. 7.l) LIRPF | — | — |
| `441948a925` | PASS | art. 7.m) LIRPF | — | — |
| `d66fa81e5d` | PASS | art. 7.o) LIRPF | — | — |
| `46f721caf6` | PASS | art. 7.p) 1.º–2.º LIRPF | — | — |
| `a64ccde8a6` | PASS | art. 7.p), párrafos 3.º–4.º LIRPF | — | — |
| `34fe7f585a` | PASS | art. 7.q) LIRPF | — | — |
| `b00b5603e8` | PASS | art. 7.s) LIRPF | — | — |
| `9bd69d0e81` | PASS | art. 7.t) LIRPF | — | — |
| `94b1b2f7fd` | PASS | art. 7.u) LIRPF | — | — |
| `2ed8abf37d` | PASS | art. 7.w) LIRPF | — | — |
| `9ec95a0467` | FAIL | art. 7.y) LIRPF | drops the narrowing «cuando ellos y las personas a su cargo carezcan de medios económicos suficientes» and the purpose of the renta mínima («para garantizar recursos económicos de subsistencia a las personas que carezcan de ellos»); the victims' part is the Ley 35/1995 and LO 1/2004 aids «y demás ayudas públicas satisfechas a víctimas de violencia de género por tal condición» | y) La prestación de la Seguridad Social del Ingreso Mínimo Vital, las prestaciones económicas establecidas por las Comunidades Autónomas en concepto de renta mínima de inserción para garantizar recursos económicos de subsistencia a las personas que carezcan de ellos, y las demás ayudas establecidas por estas o por entidades locales para atender a colectivos en riesgo de exclusión social, situaciones de emergencia social, necesidades habitacionales de personas sin recursos o necesidades de alimentación, escolarización y demás necesidades básicas de menores o personas con discapacidad cuando ellos y las personas a su cargo carezcan de medios económicos suficientes, hasta un importe máximo anual conjunto de 1,5 veces el indicador público de rentas de efectos múltiples; y las ayudas a las víctimas de delitos violentos y contra la libertad sexual, las previstas en la ley de medidas de protección integral contra la violencia de género y las demás ayudas públicas satisfechas a víctimas de violencia de género por tal condición. |
| `3f8e5ec581` | PASS | art. 1 RIRPF | — | — |
| `86b7054303` | FAIL | art. 2.2.1.º RIRPF | drops the narrowing of the insurance («del que sea beneficiario el becario y, en su caso, el cónyuge e hijo del becario siempre que no posean cobertura de la Seguridad Social») and the proportional cap for becas shorter than a year | La exención de las becas para estudios reglados alcanza los costes de matrícula, o cantidades satisfechas por un concepto equivalente, y de seguro de accidentes corporales y asistencia sanitaria del becario y, en su caso, de su cónyuge e hijo siempre que no posean cobertura de la Seguridad Social, así como una dotación económica máxima, con carácter general, de 6.000 euros anuales, que se eleva hasta 18.000 euros anuales cuando compense gastos de transporte y alojamiento para estudios reglados hasta el nivel de máster incluido o equivalente, y a 21.000 euros anuales en estudios en el extranjero; en los estudios de doctorado el máximo es de 21.000 euros anuales o 24.600 euros anuales cuando sean en el extranjero, y si la beca dura menos del año natural la cuantía máxima exenta es la parte proporcional (art. 2.2 RIRPF). |
| `14279015f3` | PASS | arts. 4 y 6.2 RIRPF | — | — |
| `7e042ddd83` | PASS | art. 9.1.a) LIRPF | — | — |
| `b1361b524e` | PASS | art. 9.1.a), párrafo 2.º LIRPF | — | — |
| `34c1250dbf` | PASS | art. 9.2 LIRPF | — | — |
| `f4773375bb` | PASS | art. 14.1.b), párrafo 2.º LIRPF | — | — |
| `ee591674ed` | PASS | art. 14.2 LIRPF | list a)–m) complete and in order | — |
| `11af4c56f2` | PASS | art. 14.2.a) LIRPF | — | — |
| `f975c5de94` | PASS | art. 14.2.b) LIRPF | — | — |
| `3927920c4b` | PASS | art. 14.2.b), párrafo 2.º LIRPF | — | — |
| `8830719d1f` | PASS | art. 14.2.c) LIRPF | — | — |
| `ad24697f75` | PASS | art. 14.2.d) LIRPF | — | — |
| `30b87e6d14` | PASS | art. 14.2.d), párrafo 2.º LIRPF | — | — |
| `895295e556` | PASS | art. 14.2.d), párrafo 3.º LIRPF | — | — |
| `46bfd4c96d` | PASS | art. 14.2.e) LIRPF | — | — |
| `2cd23eee2b` | PASS | art. 14.2.f) LIRPF | — | — |
| `ab3aee918a` | PASS | art. 14.2.g) LIRPF | — | — |
| `d396f7fb19` | PASS | art. 14.2.h) LIRPF | — | — |
| `f79243d731` | PASS | art. 14.2.h) A)–B) LIRPF | — | — |
| `9661ce7c5f` | PASS | art. 14.2.h), último párrafo LIRPF | — | — |
| `6094efade4` | PASS | art. 14.2.i) LIRPF | — | — |
| `6d38911422` | PASS | art. 14.2.j) LIRPF | — | — |
| `7bb65f277b` | PASS | art. 14.2.k) LIRPF | — | — |
| `d41c862736` | PASS | art. 14.2.k), último párrafo LIRPF | — | — |
| `3b83e271e3` | PASS | art. 14.2.l) LIRPF | — | — |
| `e451e51247` | PASS | art. 14.2.m) LIRPF | — | — |
| `3165f483ad` | PASS | art. 14.2.m), último párrafo LIRPF | — | — |
| `bf5edcfc0a` | PASS | art. 14.3 LIRPF | — | — |
| `eee4197858` | PASS | art. 14.3, párrafo 2.º LIRPF | — | — |
| `88ba41c099` | PASS | art. 17.1 LIRPF | list a)–f) complete | — |
| `da7a3723b7` | PASS | art. 17.1.e) LIRPF | — | — |
| `08a45bb8b4` | PASS | art. 17.1.f) LIRPF | — | — |
| `f8c02ef9bd` | PASS | art. 17.1.f) LIRPF | — | — |
| `812cde9aa0` | PASS | art. 17.1.f), párrafo 2.º LIRPF | — | — |
| `8032dc9396` | PASS | art. 9.A.1 RIRPF | — | — |
| `5f8d66cfac` | PASS | art. 9.A.6 RIRPF | — | — |
| `432e33ee5b` | PASS | art. 9.A RIRPF | structure | — |
| `86ffd56837` | PASS | art. 9.A RIRPF | table header | — |
| `a881807396` | PASS | art. 9.A.2.a) RIRPF | — | — |
| `ba4a51deb3` | PASS | art. 9.A.2.b) RIRPF; art. único.1 Orden HFP/792/2023 | 0,26 €/km checked in the Orden and in the boe.es note under art. 9.A.2 | — |
| `4387ff3e8d` | PASS | art. 9.A.3.a) 1.º RIRPF | — | — |
| `9317df3f17` | PASS | art. 9.A.3.a) 1.º RIRPF | — | — |
| `3cb07ca363` | PASS | art. 9.A.3.a) 2.º RIRPF | — | — |
| `b83d8dc51a` | PASS | art. 9.A.3.a) RIRPF, personal de vuelo | — | — |
| `f918568a4e` | PASS | art. 9.A.3, párrafos 1.º–2.º RIRPF | — | — |
| `3bfe5606a8` | PASS | art. 9.A.3.a), último párrafo RIRPF | — | — |
| `046858e369` | PASS | art. 9.A.3.b) 1.º–4.º RIRPF | the four groups are all covered | — |
| `43c14e13b3` | FAIL | art. 9.A.4 RIRPF | drops the condition «siempre que aquellas asignaciones correspondan a desplazamientos a municipio distinto del que constituya la residencia habitual del trabajador» and «contratados específicamente» | El régimen es aplicable también a las asignaciones para gastos de locomoción, manutención y estancia que perciban los trabajadores contratados específicamente para prestar sus servicios en empresas con centros de trabajo móviles o itinerantes, siempre que correspondan a desplazamientos a municipio distinto del que constituya su residencia habitual (art. 9.A.4 RIRPF). |
| `bd3098aa5a` | PASS | art. 9.A.5 RIRPF | — | — |
| `875c013614` | FAIL | art. 9.B.1 RIRPF; art. único.2 Orden HFP/792/2023 | the kilometre figure for these contribuyentes was revised to 0,26 euros by art. único.2 of the Orden HFP/792/2023 (boe.es note under art. 9.B.1.a); the sentence gives only 0,19; also drops «siempre que justifiquen la realidad de sus desplazamientos» and that estancia must always be resarcida by the empresa | Cuando los gastos de locomoción y manutención no les sean resarcidos específicamente por las empresas, los contribuyentes con rendimientos del trabajo derivados de relaciones laborales especiales de carácter dependiente pueden minorar sus ingresos, siempre que justifiquen la realidad de sus desplazamientos, en el gasto de transporte público justificado o, en otro caso, en 0,19 euros por kilómetro, cantidad que la Orden HFP/792/2023 fija en 0,26 euros por kilómetro, más peaje y aparcamiento, y en 26,67 euros o 48,08 euros diarios por manutención, según el desplazamiento sea dentro del territorio español o al extranjero (art. 9.B.1 RIRPF; art. único.2 Orden HFP/792/2023). |
| `95b5ba4eea` | PASS | art. 9.B.2 RIRPF | — | — |
| `b7f8aa626f` | PASS | art. 9.B.3 RIRPF | — | — |
| `9315ade413` | PASS | art. 17.2 LIRPF | list a)–k) complete, a) with 1.ª–7.ª | — |
| `254704e450` | PASS | art. 17.2.a) 1.ª–7.ª LIRPF | — | — |
| `a8e72769dc` | PASS | art. 17.2.b) LIRPF | — | — |
| `a93c7eb089` | PASS | art. 17.2.g) LIRPF | — | — |
| `c3846b209d` | PASS | art. 17.2.i) LIRPF | — | — |
| `0d8c612140` | PASS | art. 17.2.j) LIRPF | — | — |
| `9cd660cc41` | PASS | art. 17.2.k) LIRPF | — | — |
| `9efb99a9be` | PASS | art. 42.1, párrafo 2.º LIRPF | — | — |
| `6b1ba5fc9c` | PASS | art. 42.3 LIRPF | list a)–f) complete | — |
| `7859510279` | PASS | art. 42.3.c) LIRPF | — | — |
| `9ee8997bea` | PASS | art. 42.3.e) LIRPF | — | — |
| `97af7744bd` | PASS | art. 42.3.f) LIRPF | — | — |
| `3878c136cb` | PASS | art. 42.3.f), párrafo 2.º LIRPF | — | — |
| `971e665a29` | PASS | art. 43.1.1.º d) LIRPF | — | — |
| `e064765819` | PASS | art. 43.1.1.º e) LIRPF | — | — |
| `707e12212f` | PASS | art. 43.1.1.º f) LIRPF | — | — |
| `01d38231e9` | PASS | art. 43.1.1.º g) LIRPF | — | — |
| `f64bcafff1` | PASS | art. 43.1.1.º b) LIRPF | — | — |
| `558d938f07` | PASS | art. 43.1.2.º LIRPF | — | — |
| `ac25699731` | PASS | art. 43.2 LIRPF | — | — |
| `228b6fc65d` | PASS | arts. 43–48 bis RIRPF | structure | — |
| `9dd6c1f985` | PASS | art. 43.1 RIRPF | — | — |
| `c316edf918` | PASS | art. 43.2 RIRPF | — | — |
| `59bc0bad58` | PASS | art. 44 RIRPF | — | — |
| `519ac31a59` | PASS | art. 45.1 RIRPF | — | — |
| `fe2da1e155` | PASS | art. 45.2.1.º RIRPF | — | — |
| `f7cd99d0dd` | PASS | art. 46 RIRPF | — | — |
| `ce138cbeae` | PASS | art. 46 bis RIRPF | — | — |
| `f205ab6b96` | PASS | art. 47 RIRPF | — | — |
| `24f66a6559` | PASS | art. 48 RIRPF | — | — |
| `9e877ddb12` | PASS | art. 48 bis RIRPF | — | — |
| `6402ec13ad` | PASS | art. 10 RIRPF | — | — |
| `b3b639f3a4` | PASS | art. 11.2 RIRPF | — | — |
| `a63773f9f4` | PASS | art. 11.1 RIRPF | — | — |
| `72b32695ce` | PASS | art. 18.1 LIRPF | — | — |
| `c250ff5048` | PASS | art. 18.2 LIRPF | structure | — |
| `d885345289` | PASS | art. 18.2, párrafo 1.º LIRPF | — | — |
| `5028fbbb41` | PASS | art. 18.2, párrafo 2.º LIRPF | — | — |
| `fa4526ef60` | PASS | art. 18.2, párrafo 3.º LIRPF | — | — |
| `016b64653c` | PASS | art. 18.2, párrafo 4.º LIRPF | — | — |
| `d1836b0f83` | PASS | art. 18.2, párrafo 5.º LIRPF | — | — |
| `e41311d87b` | PASS | art. 18.2, párrafo 6.º LIRPF | — | — |
| `8aadb11361` | PASS | art. 18.2, último párrafo LIRPF | — | — |
| `dca007ac71` | PASS | art. 18.3 LIRPF | — | — |
| `74d2ddacf2` | PASS | art. 18.4 LIRPF | — | — |
| `3832114371` | PASS | art. 12.1 RIRPF | list a)–g) complete | — |
| `304dd09ecb` | PASS | art. 12.1.a) RIRPF | — | — |
| `0facd40163` | PASS | art. 12.1.b) RIRPF | — | — |
| `f7c986a2a0` | PASS | art. 12.1.c) RIRPF | — | — |
| `5f72813ba8` | PASS | art. 12.1.d) RIRPF | — | — |
| `304b8683f9` | PASS | art. 12.1.e) RIRPF | — | — |
| `5b1fcde7e8` | PASS | art. 12.1.f) RIRPF | — | — |
| `5b2bb7bd8d` | PASS | art. 12.1.g) RIRPF | — | — |
| `fbfedd74a0` | PASS | art. 12.1, último párrafo RIRPF | — | — |
| `3b63b70de5` | PASS | art. 12.2 RIRPF | — | — |
| `02821f3807` | PASS | art. 12.3 RIRPF | — | — |
| `c521aa96e9` | PASS | art. 23.1.a) LIRPF | «entre otros» is the article's own wording, quoted as such; the four numbered items 1.º–4.º are all given | — |
| `b50ca9e8f6` | PASS | art. 13 RIRPF | list a)–h) complete | — |
| `ec39bb136e` | PASS | art. 13.a) RIRPF | — | — |
| `c44885a7ae` | PASS | art. 13.a), párrafos finales RIRPF | — | — |
| `7b3c100d0f` | PASS | art. 13.b) RIRPF | — | — |
| `a7f5085722` | PASS | art. 13.c) RIRPF | — | — |
| `e36c781241` | PASS | art. 13.d) RIRPF | — | — |
| `ae0839b188` | PASS | art. 13.e) RIRPF | — | — |
| `3d8ba5ee39` | PASS | art. 13.f) RIRPF | — | — |
| `2bd9727f5e` | PASS | art. 13.g) RIRPF | — | — |
| `855bea27c8` | PASS | art. 13.h) RIRPF | — | — |
| `ea2efb85b6` | PASS | art. 14.1 RIRPF | — | — |
| `4fa91dfe75` | PASS | art. 14.2.a), párrafo 2.º RIRPF | — | — |
| `4268b28bae` | PASS | art. 14.2.b) RIRPF | — | — |
| `97347559c9` | PASS | art. 14.3 RIRPF | — | — |
| `36cad8c392` | PASS | art. 15 RIRPF | list a)–c) complete | — |
| `a80c69f74e` | PASS | disp. trans. 3.ª LIRPF | — | — |
| `62a79ce2ce` | PASS | art. 23.2 LIRPF (RDL 29/2026) | mark right (revert list: LIRPF 23.2, 08-10-2026) | — |
| `c634a91896` | FAIL | disp. trans. 38.ª LIRPF | the DT 38.ª in the file is the wording of the RDL 29/2026 (art. 6, segundo; revert list row «LIRPF … DT 38.ª», 08-10-2026; it names 01-12-2026); the citation lacks the «convalidación pendiente» mark | La redacción del artículo 23.2 que se aplica depende de la fecha del contrato (disposición transitoria trigésima octava LIRPF, redacción del Real Decreto-ley 29/2026, convalidación pendiente): |
| `20c1a14c18` | FAIL | disp. trans. 38.ª.1 LIRPF | facts right; RDL 29/2026 mark missing (as above) | A los contratos celebrados con anterioridad a la entrada en vigor de la Ley 12/2023, de 24 de mayo, por el derecho a la vivienda, se aplica la reducción del artículo 23.2 en su redacción vigente a 31 de diciembre de 2021 (disposición transitoria trigésima octava LIRPF, redacción del Real Decreto-ley 29/2026, convalidación pendiente). |
| `804e5ec99e` | FAIL | disp. trans. 38.ª.2 LIRPF | facts right; RDL 29/2026 mark missing (as above) | A los celebrados entre la entrada en vigor de la Ley 12/2023 y el 1 de diciembre de 2026, se aplica la reducción en su redacción vigente a 31 de diciembre de 2025 (disposición transitoria trigésima octava LIRPF, redacción del Real Decreto-ley 29/2026, convalidación pendiente). |
| `27a936704b` | PASS | art. 23.2 LIRPF (RDL 29/2026) | — | — |
| `153ca0392b` | FAIL | disp. trans. 38.ª, último párrafo LIRPF | facts right; RDL 29/2026 mark missing (as above) | Con independencia de la fecha del contrato, la reducción del 80 por ciento para los supuestos de prórroga tácita se aplica a los rendimientos derivados de la prórroga, siempre que el plazo mínimo de cinco años del artículo 9 de la Ley de Arrendamientos Urbanos se produzca con posterioridad al 1 de diciembre de 2026 (disposición transitoria trigésima octava LIRPF, redacción del Real Decreto-ley 29/2026, convalidación pendiente). |
| `481391f989` | PASS | art. 23.2 LIRPF, versión BOE-A-2021-11473 (vigente 11-07-2021) in the versions XML | — | — |
| `d80a0078e4` | PASS | art. 23.2 LIRPF, versión BOE-A-2023-12203 (vigente 01-01-2024) | — | — |
| `e323abc56b` | PASS | art. 23.2.a), versión 2024 | — | — |
| `5ef4e92719` | PASS | art. 23.2.b) 1.º–2.º, versión 2024 | — | — |
| `42e31d3619` | PASS | art. 23.2.c), versión 2024 | — | — |
| `1017bf26b9` | PASS | art. 23.2.d), versión 2024 | — | — |
| `8d22c02c2f` | FAIL | art. 23.2 LIRPF (RDL 29/2026) | the «no gran tenedor» condition belongs only to letters a) and b); letters c) (70 %) and d) (60 %), listed under this lead-in, carry no such condition | Redacción vigente (art. 23.2 LIRPF, redacción del Real Decreto-ley 29/2026, convalidación pendiente); las reducciones de las letras a) y b) exigen que el arrendador no tenga, en el momento de la celebración del contrato, la consideración de gran tenedor a que se refiere la letra k) del artículo 3 de la Ley 12/2023: |
| `0a7e0a8938` | FAIL | art. 23.2.a).1.º LIRPF (RDL 29/2026) | percentages right; the item's own citation lacks the RDL 29/2026 mark that every citation of art. 23.2 carries (revert list) | Nuevo contrato formalizado por el mismo arrendador con renta inicial rebajada en más de un 5 por ciento respecto de la última renta (art. 23.2.a).1.º LIRPF, redacción del Real Decreto-ley 29/2026, convalidación pendiente): 100 por ciento si, finalizado el plazo mínimo de cinco años o la última de las prórrogas, se formaliza un nuevo contrato con el mismo arrendatario, o con otro arrendatario si la renta inicial es inferior al límite máximo del precio conforme al sistema de índices de precios de referencia; 95 por ciento si la vivienda está situada en una zona de mercado residencial tensionado y el arrendatario tiene entre 18 y 35 años; 90 por ciento si está situada en una zona de mercado residencial tensionado; 85 por ciento si el arrendatario tiene entre 18 y 35 años; 70 por ciento en los restantes casos. |
| `53df485b66` | FAIL | art. 23.2.a).2.º LIRPF (RDL 29/2026) | figure right; mark missing (as above) | Nuevo contrato con renta inicial no superior a la última renta: 50 por ciento (art. 23.2.a).2.º LIRPF, redacción del Real Decreto-ley 29/2026, convalidación pendiente). |
| `5514c197f3` | FAIL | art. 23.2.a).3.º LIRPF (RDL 29/2026) | figures right; mark missing (as above) | Nuevo contrato con renta inicial incrementada (art. 23.2.a).3.º LIRPF, redacción del Real Decreto-ley 29/2026, convalidación pendiente): 40 por ciento si el incremento es igual o inferior al 5 por ciento; 30 por ciento si es superior al 5 por ciento pero igual o inferior al 10 por ciento; 25 por ciento si es superior al 10 por ciento pero igual o inferior al 15 por ciento; 20 por ciento si es superior al 15 por ciento pero igual o inferior al 20 por ciento; 15 por ciento si es superior al 20 por ciento. |
| `30f7482dd4` | FAIL | art. 23.2.b) LIRPF (RDL 29/2026) | figures right; mark missing (as above) | Vivienda alquilada por primera vez (art. 23.2.b) LIRPF, redacción del Real Decreto-ley 29/2026, convalidación pendiente): 100 por ciento si la renta es inferior al límite máximo del precio conforme al sistema de índices de precios de referencia; 95 por ciento si, no dándose ese requisito, la vivienda está en una zona de mercado residencial tensionado y el arrendatario tiene entre 18 y 35 años; 90 por ciento si está en una zona de mercado residencial tensionado; 85 por ciento si el arrendatario tiene entre 18 y 35 años; 50 por ciento si la renta es superior o igual a ese límite máximo. |
| `3cbf1bdfb9` | FAIL | art. 23.2.c) LIRPF (RDL 29/2026); versión 2024, letra b) 2.º | wording identical to the 2024 version's b) 2.º, checked; mark missing (as above) | 70 por ciento cuando el arrendatario sea una Administración Pública o entidad sin fines lucrativos en las condiciones de la redacción de 31 de diciembre de 2025 (art. 23.2.c) LIRPF, redacción del Real Decreto-ley 29/2026, convalidación pendiente). |
| `8460fa9a5e` | FAIL | art. 23.2.d) LIRPF (RDL 29/2026) | fact right; mark missing (as above) | 60 por ciento cuando la vivienda hubiera sido objeto de una actuación de rehabilitación finalizada en los dos años anteriores a la fecha de celebración del contrato (art. 23.2.d) LIRPF, redacción del Real Decreto-ley 29/2026, convalidación pendiente). |
| `28d4db6f54` | PASS | art. 23.2.a).1.º y b), párrafos sobre varios arrendatarios (RDL 29/2026) | — | — |
| `f2aa0c898e` | PASS | art. 23.2, párrafo «Los requisitos…» (RDL 29/2026) | — | — |
| `0adbc5174d` | PASS | art. 23.2, párrafos finales (RDL 29/2026) | — | — |
| `ed076bdbfe` | PASS | art. 24 LIRPF, «Redacción anterior» | mark right (art. 24 changes from 01-01-2027) | — |
| `5dc296d747` | PASS | art. 24, párrafo 1.º LIRPF (RDL 29/2026, efectos 01-01-2027) | — | — |
| `0a785b396a` | PASS | art. 24, párrafo 2.º LIRPF (RDL 29/2026, efectos 01-01-2027) | — | — |
| `10e7151d55` | PASS | art. 25.1 LIRPF | — | — |
| `a71fc33f9a` | FAIL | art. 25.1.a)–e) LIRPF | letters a)–e) all present, but e) states only the general rule and drops the exception of its second paragraph for securities not admitted to trading (rendimiento up to the positive difference between fondos propios and valor de adquisición) | Quedan incluidos dentro de esta categoría los siguientes rendimientos, dinerarios o en especie (art. 25.1 LIRPF): - a) Los dividendos, primas de asistencia a juntas y participaciones en los beneficios de cualquier tipo de entidad. - b) Los rendimientos procedentes de cualquier clase de activos, excepto la entrega de acciones liberadas que, estatutariamente o por decisión de los órganos sociales, faculten para participar en los beneficios, ventas, operaciones, ingresos o conceptos análogos de una entidad por causa distinta de la remuneración del trabajo personal. - c) Los rendimientos que se deriven de la constitución o cesión de derechos o facultades de uso o disfrute, cualquiera que sea su denominación o naturaleza, sobre los valores o participaciones que representen la participación en los fondos propios de la entidad. - d) Cualquier otra utilidad, distinta de las anteriores, procedente de una entidad por la condición de socio, accionista, asociado o partícipe. - e) La distribución de la prima de emisión de acciones o participaciones: el importe obtenido minora, hasta su anulación, el valor de adquisición de las acciones o participaciones afectadas y el exceso tributa como rendimiento del capital mobiliario; si los valores no están admitidos a negociación en un mercado regulado y la diferencia entre el valor de los fondos propios del último ejercicio cerrado antes de la distribución y su valor de adquisición es positiva, el importe obtenido es rendimiento del capital mobiliario con el límite de esa diferencia, y el exceso minora el valor de adquisición. |
| `bd2e9dc58f` | PASS | art. 25.2 LIRPF | — | — |
| `bdd46d1586` | PASS | art. 25.3 LIRPF | — | — |
| `3a9c0ea869` | PASS | art. 25.3.a) 2.º LIRPF | — | — |
| `ec23516cc8` | PASS | art. 25.3.a) 2.º–6.º y b) LIRPF | — | — |
| `c98fee1dbc` | PASS | art. 25.4 LIRPF | «entre otros» quoted as the article's own words; letters a)–d) all given | — |
| `ed503999eb` | PASS | art. 26.2 LIRPF | — | — |
| `699616a817` | PASS | art. 17 RIRPF | — | — |
| `21b3e92e07` | PASS | art. 18 RIRPF | — | — |
| `2b3e237cdc` | PASS | art. 19 RIRPF | — | — |
| `c01d68a1c5` | PASS | art. 20 RIRPF | — | — |
| `fd0da3055d` | PASS | art. 21 RIRPF | list a)–c) complete | — |
| `ea3a93a455` | PASS | art. 27 RIRPF | — | — |
| `7d41ea502c` | PASS | art. 29.1 LIRPF | list a)–c) complete | — |
| `218d4fbbdb` | PASS | art. 29.1.a) LIRPF | — | — |
| `61ae43d6bb` | PASS | art. 29.1.b) LIRPF | — | — |
| `0c4a17328a` | PASS | art. 29.1.b) LIRPF | — | — |
| `202913c2b5` | PASS | art. 29.1.c) LIRPF | — | — |
| `1aca1ba9af` | PASS | art. 29.1.c) LIRPF | — | — |
| `70a97bde46` | PASS | art. 29.2 LIRPF | — | — |
| `60e7857ca6` | PASS | art. 29.3 LIRPF | — | — |
| `2b033f0ae1` | PASS | arts. 22–23 RIRPF | structure | — |
| `15efe610c8` | PASS | art. 22.1 RIRPF | — | — |
| `5b45eb372b` | PASS | art. 22.2 RIRPF | — | — |
| `b0bf978ab7` | PASS | art. 22.2 RIRPF | — | — |
| `3ed8d60384` | PASS | art. 22.3 RIRPF | — | — |
| `4698ebb097` | PASS | art. 22.4 RIRPF | — | — |
| `0b37884d1f` | PASS | art. 22.4 RIRPF | list a)–e) complete | — |
| `95dcba8933` | PASS | art. 23.1 RIRPF | — | — |
| `1833e39df4` | PASS | art. 23.2 RIRPF | — | — |
| `d1d45fc897` | PASS | art. 30.2 LIRPF | rules 1.ª–5.ª complete | — |
| `e53f71d20c` | PASS | art. 30.2.1.ª LIRPF | — | — |
| `080fc3af66` | PASS | art. 30.2.1.ª, párrafo 2.º LIRPF | — | — |
| `6ecc691ff8` | PASS | art. 30.2.2.ª LIRPF | — | — |
| `582c070316` | PASS | art. 30.2.3.ª LIRPF | — | — |
| `e80dd506a6` | PASS | art. 30.2.3.ª, párrafo 2.º LIRPF | — | — |
| `a454ae94b4` | PASS | art. 30.2.4.ª LIRPF | — | — |
| `cc8a6e9a48` | PASS | art. 30.2.ª RIRPF | — | — |
| `77587a8a9d` | PASS | art. 30.2.5.ª a)–c) LIRPF | — | — |
| `ff8dbca7ab` | PASS | art. 30.1.ª RIRPF | — | — |
| `2cb633d505` | PASS | art. 28.1 RIRPF | — | — |
| `768b20238e` | PASS | art. 28.2 RIRPF | — | — |
| `e6484adf0f` | PASS | art. 28.3 RIRPF | — | — |
| `a44ae0954b` | PASS | art. 29.1 RIRPF | — | — |
| `8d73e08b1d` | PASS | art. 29.2 RIRPF | — | — |
| `b59fd3e553` | PASS | art. 29.3 RIRPF | — | — |
| `9eabfcf3c2` | PASS | art. 31.1–4 RIRPF | — | — |
| `ff545e771a` | PASS | art. 24 RIRPF | — | — |
| `83fd34a820` | PASS | art. 31.1.3.ª LIRPF | list a)–d) complete | — |
| `8b1361e0b4` | PASS | art. 31.1.3.ª a) LIRPF | — | — |
| `46a11f440a` | PASS | art. 31.1.3.ª b) LIRPF | — | — |
| `c4bc8bbd07` | PASS | art. 31.1.3.ª c) LIRPF | — | — |
| `2f016e37e1` | PASS | art. 31.1.3.ª d) LIRPF | — | — |
| `d4e84cab4b` | PASS | disp. adic. 4.ª, 1.ª Orden HAC/1161/2026 | checked against the saved Orden (BOE-A-2026-23174) | — |
| `58b88f5d81` | PASS | disp. trans. 32.ª LIRPF | the consolidated LIRPF of 11-11-2026 prints «ejercicios 2016 … 2024», 250.000/125.000 for b) a´) and 250.000 for c) | — |
| `d484bf3c04` | FAIL | art. 6, primero, Cuatro RDL 9/2024; art. 14, Cuatro RDL 16/2025; art. 10, Cuatro RDL 2/2026; Resoluciones BOE-A-2025-1136, BOE-A-2026-2024, BOE-A-2026-4667 | facts right (RDL 9/2024 rewrote the DT 32.ª for 2016–2025; RDL 16/2025 and RDL 2/2026 for 2016–2026; the three resolutions record the Congreso's derogation agreements); but the extension claim cites no provision: only the resolutions are cited, and they prove only the derogation | El Real Decreto-ley 9/2024, para el período impositivo 2025 (art. 6, primero, Cuatro Real Decreto-ley 9/2024), y los Reales Decretos-leyes 16/2025 y 2/2026, para 2026 (art. 14, Cuatro Real Decreto-ley 16/2025; art. 10, Cuatro Real Decreto-ley 2/2026), prorrogaron o extendieron esos límites, y el Congreso de los Diputados acordó derogar cada uno de ellos (Resoluciones de 22 de enero de 2025, BOE-A-2025-1136, de 27 de enero de 2026, BOE-A-2026-2024, y de 26 de febrero de 2026, BOE-A-2026-4667). |
| `50ecb0b437` | PASS | art. 31.1.3.ª b)–c) LIRPF; disp. trans. 32.ª LIRPF | 2026 figure and its norm right: art. 31.1.3.ª LIRPF, the DT 32.ª ends at 2024 and the three extensions were derogated | — |
| `6118efc994` | PASS | — | structure | — |
| `e212de4305` | PASS | art. 32.2.c) RIRPF | — | — |
| `e477840c3f` | PASS | art. 3.1.a) Orden HAC/1425/2025 | quote verbatim | — |
| `5ad83bd80d` | PASS | art. 32.2 RIRPF | — | — |
| `fe10abb714` | PASS | art. 31.1.2.ª LIRPF | — | — |
| `48d4879399` | PASS | art. 31.1.4.ª LIRPF | — | — |
| `c8386cee89` | PASS | art. 31.2.2.ª LIRPF | — | — |
| `16b76aedf2` | PASS | art. 3.1.c) Orden HAC/1425/2025 | — | — |
| `03733e722d` | PASS | art. 3.1.c), párrafos 2.º–4.º Orden HAC/1425/2025 | — | — |
| `a7d214b5b8` | PASS | art. 3.1.d) Orden HAC/1425/2025 | the grouped list below covers every row of the Orden's table (69 activities), each at its figure | — |
| `b78b6de04e` | PASS | art. 3.1.d) Orden HAC/1425/2025 | 10 activities at 6, all | — |
| `b48740e67e` | PASS | art. 3.1.d) Orden HAC/1425/2025 | 3 at 10, all | — |
| `32b8d636e8` | PASS | art. 3.1.d) Orden HAC/1425/2025 | 5 at 8, all | — |
| `e1eec37713` | PASS | art. 3.1.d) Orden HAC/1425/2025 | 10 at 5, all | — |
| `5b00425e43` | PASS | art. 3.1.d) Orden HAC/1425/2025 | 14 at 4, all | — |
| `fd807c71a4` | PASS | art. 3.1.d) Orden HAC/1425/2025 | 13 at 3, all | — |
| `da529a03ea` | PASS | art. 3.1.d) Orden HAC/1425/2025 | the row ends at «n.c.o.p.» only because the sentence splitter cut at the abbreviation; the lesson sentence is whole | — |
| `f921df03e7` | PASS | art. 3.1.d) Orden HAC/1425/2025 | continuation of the previous row (splitter cut at «n.c.o.p.»); 2-person list complete | — |
| `1d22eb88dc` | PASS | art. 3.1.d) Orden HAC/1425/2025 | vehicle rows, all five | — |
| `f4fc7e9b2a` | PASS | art. 3.1.d), párrafos finales Orden HAC/1425/2025 | — | — |
| `449a705ddb` | PASS | art. 3.1, penúltimo párrafo Orden HAC/1425/2025 | — | — |
| `2cc6d2e30c` | PASS | art. 33.1 RIRPF | — | — |
| `5c5e03864e` | PASS | art. 33.2–3 RIRPF | — | — |
| `c259a49c34` | PASS | art. 34.1 y 34.3 RIRPF | — | — |
| `e34f5f73ea` | PASS | art. 34.2 RIRPF | — | — |
| `9fbccecc6a` | PASS | art. 35 RIRPF | — | — |
| `a2c94f869e` | PASS | art. 36 RIRPF | — | — |
| `64c1b6796e` | PASS | art. 37.1–2 RIRPF | — | — |
| `6d6117f0a1` | PASS | art. 37.3 RIRPF | — | — |
| `4a066f05ad` | FAIL | art. 37.4 RIRPF | presents art. 37.4 as three cases but drops the second paragraph of 37.4.2.º: the reducción is also authorised «cuando el titular de la actividad se encuentre en situación de incapacidad temporal y no tenga otro personal empleado», by the same procedure | Cuando la actividad se vea afectada por incendios, inundaciones u otras circunstancias excepcionales que afecten a un sector o zona determinada, el Ministro puede autorizar con carácter excepcional la reducción de los módulos; si hay anomalías graves por incendios, inundaciones, hundimientos o grandes averías en el equipo industrial, o cuando el titular de la actividad se encuentre en situación de incapacidad temporal y no tenga otro personal empleado, los interesados pueden solicitar la reducción en la Administración o Delegación de la Agencia Estatal de Administración Tributaria correspondiente a su domicilio fiscal, en el plazo de treinta días a contar desde la fecha en que se produzcan; y cuando haya gastos extraordinarios ajenos al proceso normal del ejercicio, los interesados pueden minorar el rendimiento neto en el importe de esos gastos, comunicándolo en el plazo de treinta días (art. 37.4 RIRPF). |
| `764cb4efad` | PASS | art. 37.5 RIRPF | — | — |
| `dd257266c2` | PASS | art. 38.1 RIRPF | — | — |
| `7635137eed` | PASS | art. 39 RIRPF | — | — |
| `77a53e81b0` | PASS | — | structure | — |
| `73790dc411` | FAIL | art. 30.1 LIRPF | «No confundir» line: the cut drops the condition «salvo que renuncie a su aplicación» (art. 30.1, párrafo 2.º) | La modalidad simplificada de la estimación directa se aplica para determinadas actividades cuyo importe neto de cifra de negocios, para el conjunto de actividades, no supere los 600.000 euros en el año inmediato anterior, salvo que el contribuyente renuncie a su aplicación; en los supuestos de renuncia o exclusión de la modalidad simplificada, el contribuyente determina el rendimiento neto de todas sus actividades por la modalidad normal durante los tres años siguientes (art. 30.1 LIRPF). |
| `23ac7cc1a6` | PASS | arts. 31.1.3.ª b) y 31.1.5.ª LIRPF | faithful cut of letter b) with every figure and the five-year rule of 5.ª | — |
| `3fd28c4f44` | PASS | art. 32.2.1.º LIRPF | — | — |
| `167d5a40ee` | PASS | art. 32.2.1.º, párrafo 2.º LIRPF | — | — |
| `fa47cf3d7d` | PASS | art. 32.2.1.º a) LIRPF | — | — |
| `95192d3287` | PASS | art. 32.2.1.º b) LIRPF | — | — |
| `30547b445a` | PASS | art. 32.2.2.º LIRPF | list a)–g) complete | — |
| `f42aef4d6d` | PASS | art. 32.2.2.º a) LIRPF | — | — |
| `67e09ea6c0` | PASS | art. 32.2.2.º b) LIRPF | — | — |
| `6d4e4b8d4a` | PASS | art. 32.2.2.º c) LIRPF | — | — |
| `dcddb9b74d` | PASS | art. 32.2.2.º d) LIRPF | — | — |
| `96dc83f066` | PASS | art. 32.2.2.º e) LIRPF | — | — |
| `16559792f7` | PASS | art. 32.2.2.º f) LIRPF | — | — |
| `d11d14e7d4` | PASS | art. 32.2.2.º g) LIRPF | — | — |
| `40e6fe968d` | PASS | art. 32.2.3.º LIRPF | — | — |
| `84ccd26555` | PASS | art. 32.2.3.º, último párrafo LIRPF | — | — |
| `619d360dcd` | PASS | art. 32.2.4.º LIRPF | — | — |
| `c0eff63650` | PASS | art. 25 RIRPF | list a)–d) complete | — |
| `a8503050b1` | PASS | art. 25.a) RIRPF | — | — |
| `6ef2125d65` | PASS | art. 25.b) RIRPF | — | — |
| `42b0b04331` | PASS | art. 25.c) RIRPF | — | — |
| `cfc1d95f47` | PASS | art. 25.d) RIRPF | — | — |
| `3ccc28acb0` | PASS | art. 26.1 RIRPF | — | — |
| `1cc6ba061f` | PASS | art. 26.2 RIRPF | — | — |
| `6f8a5aff15` | PASS | art. 18.2 LIRPF | «No confundir» line, faithful cut | — |
| `af51619da6` | PASS | art. 32.1 LIRPF | «No confundir» line, faithful cut with the habitual-activity exclusion | — |
| `5c90a1537a` | PASS | art. 85.1 LIRPF (RDL 29/2026, efectos 01-01-2027) | mark right | — |
| `be6240156d` | PASS | art. 85.1 LIRPF (2027) | table header | — |
| `649d188340` | PASS | art. 85.1 LIRPF (2027) | 0–100.000 at 1,1 % | — |
| `2ca3b1756e` | PASS | art. 85.1 LIRPF (2027) | 100.000 × 1,1 % = 1.100 | — |
| `d9bacd5dc1` | PASS | art. 85.1 LIRPF (2027) | 1.100 + 400.000 × 1,5 % = 7.100 | — |
| `fd1ff6f80e` | PASS | art. 85.1 LIRPF (2027) | 7.100 + 500.000 × 2 % = 17.100 | — |
| `6a6ff42412` | PASS | art. 85.1, párrafos 2.º–3.º LIRPF (RDL 29/2026, efectos 01-01-2027) | — | — |
| `0f32cba453` | PASS | art. 33.2 LIRPF | list a)–c) complete | — |
| `1892610404` | PASS | art. 33.2.a) LIRPF | — | — |
| `47c0f7e0f2` | PASS | art. 33.2.b) LIRPF | — | — |
| `70a1ba3d5a` | PASS | art. 33.2.c) LIRPF | — | — |
| `4a9619ed10` | PASS | art. 33.2, último párrafo LIRPF | — | — |
| `2c6d526ab6` | PASS | art. 33.3 LIRPF | list a)–e) complete | — |
| `879653d649` | PASS | art. 33.3.c) LIRPF | — | — |
| `d62299d266` | PASS | art. 33.3.d) LIRPF | — | — |
| `96e698a7f2` | PASS | art. 33.4 LIRPF | list a)–d) complete | — |
| `ab1cbb9b0e` | PASS | art. 33.4.a) LIRPF | — | — |
| `ba85a53a06` | PASS | art. 33.4.c) LIRPF | — | — |
| `e0e547f867` | PASS | art. 33.5 LIRPF | list a)–g) complete | — |
| `72b6bffac8` | PASS | art. 33.5.f) LIRPF | — | — |
| `0556f73808` | PASS | art. 33.5.g) LIRPF | — | — |
| `e517b6e376` | PASS | art. 33.5, último párrafo LIRPF | — | — |
| `6f6cff34b5` | PASS | art. 33.5.e) LIRPF | «No confundir» line, verbatim | — |
| `d77536d4a5` | PASS | art. 33.5.f)–g) LIRPF | «No confundir» line, faithful cut keeping both conditions | — |
| `0b13130463` | PASS | art. 34.2 LIRPF | — | — |
| `62d1f2aa9f` | PASS | art. 35.1 LIRPF | — | — |
| `658660c266` | PASS | art. 35.2 LIRPF | — | — |
| `d99609c0d3` | PASS | art. 40.1–2 RIRPF | — | — |
| `e93b8bc2c1` | PASS | art. 36, párrafo 1.º LIRPF | — | — |
| `6ab742f3a4` | PASS | art. 36, párrafos 2.º–3.º LIRPF | — | — |
| `9633ba37e0` | PASS | art. 37.1 LIRPF | list a)–n) complete | — |
| `cbf341adec` | PASS | art. 37.1.a) LIRPF | — | — |
| `ef75fbe786` | PASS | art. 37.1.b) LIRPF | — | — |
| `aec35b9e6d` | PASS | art. 37.1.c), párrafo 1.º LIRPF | — | — |
| `cd77c924e9` | PASS | art. 37.1.c), párrafos 2.º–4.º LIRPF | — | — |
| `f7387b9f76` | PASS | art. 37.1.d) LIRPF | — | — |
| `8bf02786ad` | PASS | art. 37.1.e) LIRPF | — | — |
| `4c1231824a` | PASS | art. 37.1.f) LIRPF | — | — |
| `64f1120aa2` | PASS | art. 37.1.g) LIRPF | — | — |
| `168bd8e5f0` | PASS | art. 37.1.h) LIRPF | — | — |
| `46d7823d71` | PASS | art. 37.1.i) LIRPF | — | — |
| `b359c605b6` | PASS | art. 37.1.j) LIRPF | — | — |
| `d41b9df5fd` | PASS | art. 37.1.k) LIRPF | — | — |
| `e6012fd034` | PASS | art. 37.1.l) LIRPF | — | — |
| `d9696d25d2` | PASS | art. 37.1.m) LIRPF | — | — |
| `aede08fbeb` | PASS | art. 37.1.n) LIRPF | — | — |
| `c1162d17d2` | PASS | art. 37.2 LIRPF | — | — |
| `b8db34ad66` | PASS | art. 37.3 LIRPF | — | — |
| `079755aa7f` | PASS | art. 38.1 LIRPF | — | — |
| `4c5d030f33` | PASS | art. 41 bis.1–2 RIRPF | the RDL 29/2026 (DF 3.ª, Uno) changed only art. 41 bis.3, not cited here, so no mark is due | — |
| `7eb18b6984` | PASS | art. 41.1 RIRPF | — | — |
| `cf963d08cc` | FAIL | art. 38.2 LIRPF | the entity exception is «a una entidad respecto de la que se produzca, con el contribuyente o con cualquiera de las personas anteriormente citadas, alguna de las circunstancias establecidas en el artículo 42 del Código de Comercio … distinta de la propia entidad cuyas participaciones se transmiten»; «entidad vinculada» drops both the link to those persons and the carve-out for the issuing entity; the homogeneous-securities exception covers only the securities that remain in the patrimonio; parentesco is «en línea recta o colateral, por consanguinidad o afinidad» | Pueden excluirse de gravamen las ganancias por la transmisión de acciones o participaciones por las que se hubiera practicado la deducción del artículo 68.1, siempre que el importe total obtenido se reinvierta en acciones o participaciones de las citadas entidades; no se aplica cuando el contribuyente hubiera adquirido valores homogéneos en el año anterior o posterior a la transmisión, respecto de los valores que por esa adquisición permanezcan en su patrimonio, ni cuando las acciones o participaciones se transmitan a su cónyuge, a una persona unida a él por parentesco, en línea recta o colateral, por consanguinidad o afinidad, hasta el segundo grado incluido, o a una entidad distinta de la propia entidad cuyas participaciones se transmiten respecto de la que se dé, con el contribuyente o con esas personas, alguna de las circunstancias del artículo 42 del Código de Comercio (art. 38.2 LIRPF). |
| `699a4d4d09` | PASS | art. 38.3, párrafo 1.º LIRPF | — | — |
| `bace8dee3e` | PASS | art. 38.3, último párrafo LIRPF | — | — |
| `91e48c06d9` | PASS | art. 42.2 RIRPF | — | — |
| `acd1d51a4b` | PASS | disp. adic. 65.ª.1 LIRPF (RDL 29/2026) | mark right | — |
| `785fcbe59d` | PASS | disp. adic. 65.ª.2 LIRPF (RDL 29/2026) | mark right | — |
| `5f44273523` | FAIL | Normativa; normativa.yaml, LIRPF (`cambio-pendiente`) | the article list matches the prose citations, but the line carries no cambio-pendiente note although normativa.yaml lists cambios_pendientes for arts. 24 and 85.1 (RDL 29/2026, from 01-01-2027), both cited in the prose; and the Real Decreto-ley 29/2026, whose wording the prose cites (arts. 7.ñ), 23.2, 24, 85.1, DA 55.ª, DA 65.ª, DT 38.ª), has no Normativa line: add one («Real Decreto-ley 29/2026: art. 6 y disposición final tercera, convalidación pendiente; nombrado en la redacción de los arts. 7.ñ), 23.2, 24 y 85.1 y de las disposiciones adicionales 55.ª y 65.ª y transitoria 38.ª LIRPF») | LIRPF (Ley 35/2006): arts. 1, 2, 3.1–3, 4.1–3, 5, 6.1–5, 7, 8.1–3, 9.1–2, 10.1–2, 11.1–5, 12.1–2, 13.1–2, 14.1–4, 16.2–3, 17.1–3, 18.1–4, 19.1–2, 20, 21.1, 22.1–2, 23.1–3, 24, 25.1–5, 26.1–2, 27.1–2, 28.1–2, 29.1–3, 30.1–2, 31.1.1.ª–5.ª, 31.2, 32.1–3, 33.1–5, 34.1–2, 35.1–2, 36, 37.1–3, 38.1–3, 39, 40, 41, 42.1–3, 43.1–2, 68.1, 68.3, 85.1–3, 97.3, disposiciones adicionales 55.ª y 65.ª y disposiciones transitorias 3.ª, 32.ª y 38.ª; arts. 7.ñ) y 23.2 y disposiciones adicionales 55.ª y 65.ª y transitoria 38.ª en la redacción del Real Decreto-ley 29/2026, convalidación pendiente; cambio pendiente: arts. 24 y 85.1 en la redacción del Real Decreto-ley 29/2026 desde el 01-01-2027. |
| `7c0b1cde5c` | PASS | Normativa | every RIRPF article cited is listed and every listed one is cited; the RDL 29/2026 changed only art. 41 bis.3, not cited | — |
| `2dbeff0149` | PASS | Normativa | matches the prose as it stands (if the fix to `875c013614` is applied, add art. único.2) | — |
| `e3b393c638` | PASS | Normativa | — | — |
| `40b9795dc7` | PASS | Normativa | matches the prose as it stands (if the fix to `d484bf3c04` is applied, list art. 6, primero, Cuatro RDL 9/2024, art. 14, Cuatro RDL 16/2025 and art. 10, Cuatro RDL 2/2026, and drop «sin precepto citado») | — |
| `e51d6d3ffb` | PASS | Normativa | — | — |
| `9a322edaf1` | PASS | Normativa | — | — |
| `976c9a6301` | PASS | Normativa | Ley 16/1985 absent from normativa.yaml, checked | — |
| `d86bab822e` | FAIL | Normativa | the prose names many more norms inside the cited articles than the four listed: Ley 46/1977 de Amnistía, Ley 20/2022 de Memoria Democrática, Ley 39/2006, LGSS, Estatuto de los Trabajadores, Código Civil, Código de Comercio, Ley 27/2014 and TRLIS, TRLPFP, Directivas 2003/41/CE, 2004/39/CE, 2009/65/CE and (UE) 2016/2341, Ley 49/2002, Ley 35/2003, Ley 22/2003, Ley 28/2022, Ley 20/2007, RD 1814/1991, TRLGDCU, the Reglamento de responsabilidad patrimonial, the Reglamento de facturación and Ley 37/1992 | Nombradas en el texto de los preceptos citados o por su materia: Ley 12/2023 (derecho a la vivienda), Ley de Arrendamientos Urbanos (arts. 2.1, 9, 10 y 17.6), Ley 14/2002 (art. 2), Real Decreto-ley 9/1993, Ley de Amnistía, Ley de Memoria Democrática (disposición adicional vigésima), Ley 39/2006 (dependencia), texto refundido de la Ley General de la Seguridad Social, Estatuto de los Trabajadores (arts. 51 y 52.c)), Código Civil (art. 90), Código de Comercio (art. 42), Ley 27/2014 del Impuesto sobre Sociedades (art. 18), texto refundido de la Ley del Impuesto sobre Sociedades (arts. 16 y 108 y capítulo VIII del título VII), texto refundido de la Ley de Regulación de los Planes y Fondos de Pensiones (arts. 8.6 y 8.8 y disposición adicional primera), Directivas 2003/41/CE, 2004/39/CE, 2009/65/CE y (UE) 2016/2341, Ley 49/2002 (título II), Ley 35/2003, Ley 22/2003 Concursal (arts. 71 bis, 133 y 176, disposición adicional cuarta y título X), Ley 28/2022, Ley 20/2007 (capítulo III del título II), Real Decreto 1814/1991, texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios (art. 60), Reglamento de los procedimientos de las Administraciones públicas en materia de responsabilidad patrimonial, Reglamento por el que se regulan las obligaciones de facturación (art. 6.1) y Ley 37/1992 (art. 122.dos.3.º). |

PASS 334 · FAIL 26
