# Verification — `m03-l05` (blind)

Verifier: opus, 2026-11-11. Sources: snapshot PDFs in `content/aeat-agentes-hacienda/sources/normativa/` (LGT 2024-12-21, RGAT 2026-10-07, LPAC 2024-11-06). No cited precept has a cambio pendiente or an unconvalidated-RDL change in normativa.yaml (the RDL 29/2026 change to the RGAT is art. 39 quater, not cited).

Worked examples recomputed with `python3` (`datetime`): 15-1-2026 Thursday; six months by art. 30.4 LPAC → 15-7-2026 Wednesday; alegaciones end 10-4-2026 Friday; dilación art. 104.b) RGAT from the day after (11-4) to the day of aportación (30-4), both included = 20 días naturales (art. 102.5 RGAT); 15-7 + 20 = 4-8-2026 Tuesday; 3-8 Monday, 5-8 Wednesday. Comparecencia: 3-3 Tuesday, 4-3 Wednesday, BOE 16-3 Monday (a publication day), day 1 = 17-3 Tuesday, day 15 = 31-3 Tuesday, notification 1-4-2026 Wednesday. All dates and weekdays match the lesson.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `4a937b1e4c` | PASS | structure (introduction) | — | — |
| `06e0bc23f8` | PASS | structure (introduction) | — | — |
| `ad821e0978` | PASS | structure (introduction) | — | — |
| `645e63adc0` | PASS | art. 85.1 LGT | — | — |
| `4e838ce180` | PASS | art. 85.2 LGT | — | — |
| `d5a018e55b` | PASS | art. 85.2 LGT | — | — |
| `02fe9feb2e` | PASS | art. 85.2 LGT | — | — |
| `0ad5f15eec` | PASS | art. 85.2 LGT | — | — |
| `681140e302` | PASS | art. 85.2 LGT | — | — |
| `0844cfb5e9` | PASS | art. 85.2 LGT | — | — |
| `34c638d5ed` | PASS | art. 62 RGAT | — | — |
| `a60e2d9cae` | PASS | art. 86.1 LGT | — | — |
| `b0c583befb` | PASS | art. 86.2 LGT | — | — |
| `7be1b77e95` | PASS | art. 86.4 LGT | — | — |
| `f325b3813e` | PASS | art. 87.1 LGT | — | — |
| `41a0711021` | PASS | art. 87.2 LGT | — | — |
| `a873ec2da6` | PASS | art. 63.1 y 63.2 RGAT | — | — |
| `1e92155b32` | PASS | art. 63.3 RGAT | — | — |
| `6b7e400d3e` | PASS | art. 63.3 RGAT | — | — |
| `c0a3c4dfb0` | PASS | art. 64.1 RGAT | — | — |
| `0c2ecdf1f7` | PASS | art. 88.1 LGT | — | — |
| `923a8f26f7` | PASS | art. 88.2 LGT | — | — |
| `521d4d88dd` | PASS | art. 88.3 LGT | — | — |
| `cfa8231291` | PASS | art. 88.4 LGT | — | — |
| `c2e6d64dc2` | PASS | art. 88.5 LGT | — | — |
| `ebbedf9324` | PASS | art. 65 RGAT | — | — |
| `ceb4d99aa6` | FAIL | art. 88.6 LGT | drops the narrowing clause: the six-month duty covers «las consultas que reúnan los requisitos establecidos en virtud del apartado 2 de este artículo»; the sentence also lacks its own citation | La Administración tributaria competente deberá contestar por escrito las consultas que reúnan los requisitos establecidos en virtud del artículo 88.2 LGT en el plazo de seis meses desde su presentación (art. 88.6 LGT). |
| `d7ee3ca0ec` | PASS | art. 88.6 LGT | — | — |
| `0ab73c005c` | PASS | art. 89.1 LGT | — | — |
| `8ace7e9083` | PASS | art. 89.1 LGT | — | — |
| `a547c8c46a` | PASS | art. 89.1 LGT | — | — |
| `2e0267c265` | PASS | art. 89.2 LGT | — | — |
| `ba16e328eb` | PASS | art. 89.3 LGT | — | — |
| `18be140a17` | PASS | art. 89.4 LGT | — | — |
| `16ed880e71` | PASS | art. 89.4 LGT | — | — |
| `595bfe26e3` | PASS | art. 90.1 LGT | — | — |
| `78d5ca07d5` | PASS | art. 90.2 LGT | — | — |
| `ed8c75035b` | PASS | art. 90.2 LGT | — | — |
| `96b25f29ae` | PASS | art. 90.3 LGT | — | — |
| `a2d57a029f` | PASS | art. 90.3 LGT | — | — |
| `fa71f27cec` | PASS | art. 90.3 LGT | — | — |
| `7682626ee5` | PASS | art. 69.1 RGAT | — | — |
| `2aaa81e7b9` | PASS | art. 69.1 RGAT | — | — |
| `c7a998bf9e` | PASS | art. 69.6 RGAT | — | — |
| `3071b8be08` | PASS | art. 91.1 LGT | — | — |
| `d176799643` | PASS | art. 91.2 LGT | — | — |
| `44f190ccea` | PASS | art. 91.3 LGT | — | — |
| `728a8ce103` | PASS | art. 91.4 LGT | — | — |
| `f0e73f2a6d` | PASS | art. 91.4 LGT | — | — |
| `c0f059fd81` | PASS | art. 91.5 LGT | — | — |
| `60ba0d5366` | PASS | art. 91.5 LGT | — | — |
| `ce68bc6c7d` | PASS | art. 91.6 LGT | — | — |
| `facc4aa8ea` | PASS | art. 91.6 LGT | — | — |
| `9414ba4a5c` | PASS | art. 70.1 RGAT | — | — |
| `ea17a92f31` | PASS | art. 70.2 RGAT | — | — |
| `5797db0e84` | PASS | art. 70.3 RGAT | — | — |
| `aa5a26a8a2` | PASS | art. 70.4 RGAT | — | — |
| `aa73f18117` | PASS | art. 70.5 RGAT | — | — |
| `1ce7748d3e` | PASS | art. 71.1 RGAT | — | — |
| `11921d3967` | FAIL | art. 72.1 RGAT | «al menos» list presented as complete omits letter c): «La inexistencia de la información que se solicita en las bases de datos de la Administración tributaria o la improcedencia de suministrar dicha información, cuando no se pueda certificar la información contenida en el párrafo b)» | Contienen, al menos, el nombre y apellidos o razón social o denominación completa, el número de identificación fiscal y el domicilio fiscal del obligado tributario; las circunstancias, obligaciones o requisitos que deban ser certificados o, cuando no se puedan certificar, la inexistencia de la información solicitada en las bases de datos de la Administración tributaria o la improcedencia de suministrarla; y el lugar, la fecha y la firma del órgano competente para su expedición y el código seguro de verificación (art. 72.1 RGAT). |
| `6688284382` | PASS | art. 72.1.b) RGAT | — | — |
| `db6deaf3ca` | PASS | art. 73.1 RGAT | — | — |
| `0816aedf9c` | PASS | art. 73.1 RGAT | — | — |
| `adfc837a6d` | PASS | art. 73.2 RGAT | — | — |
| `e99d4e82cc` | PASS | art. 73.4 RGAT | — | — |
| `d6ee226912` | PASS | art. 73.4 RGAT | — | — |
| `b03bc125f5` | PASS | art. 75.1 RGAT | — | — |
| `a2fec918dd` | PASS | art. 75.2 RGAT | — | — |
| `cd02d0aaf2` | PASS | art. 77.1 RGAT | — | — |
| `af697c186c` | PASS | art. 77.1 RGAT | — | — |
| `3081b5d4d7` | PASS | art. 77.4 RGAT | — | — |
| `263b39d9d2` | PASS | art. 78.1 RGAT | — | — |
| `b0f605c8f1` | PASS | art. 92.1 LGT | — | — |
| `0d976ff0f4` | PASS | art. 92.2 LGT | — | — |
| `dcec240f3c` | PASS | art. 92.3 LGT | — | — |
| `9a497090a6` | PASS | art. 92.3 LGT | — | — |
| `033c4b87ae` | PASS | art. 92.3 LGT | — | — |
| `3dd0c4b96d` | PASS | art. 92.3 LGT | — | — |
| `28811ec060` | PASS | art. 92.3 LGT | — | — |
| `3ea4d465e0` | PASS | art. 92.3 LGT | — | — |
| `95d3075365` | PASS | art. 92.3 LGT | — | — |
| `a6f4d969c5` | PASS | art. 92.3 LGT | — | — |
| `8349df7d16` | PASS | art. 92.3 LGT | — | — |
| `5d36a7adce` | PASS | art. 92.4 LGT | — | — |
| `0503f4fdeb` | PASS | art. 79.1 RGAT | — | — |
| `8d9c25ecfc` | PASS | art. 79.1 RGAT | — | — |
| `0847509fb8` | PASS | art. 79.1 RGAT | — | — |
| `88ad8c97bb` | PASS | art. 79.1 RGAT | — | — |
| `15a87c399d` | PASS | art. 79.1 RGAT | — | — |
| `39db33542e` | PASS | art. 79.1 RGAT | — | — |
| `fa36b76b61` | PASS | art. 79.1 RGAT | — | — |
| `160563c314` | PASS | art. 79.1 RGAT | — | — |
| `b5fe81820c` | PASS | art. 79.2 RGAT | — | — |
| `b45dae5656` | PASS | art. 79.2 RGAT | — | — |
| `a1d2a1fbcf` | PASS | art. 79.3 RGAT | — | — |
| `1b5efef3b9` | PASS | art. 79.4 RGAT | — | — |
| `68e227f520` | PASS | art. 95.1 LGT | — | — |
| `15437d0cc8` | PASS | art. 95.1 LGT | — | — |
| `15e4f08cd3` | PASS | art. 95.1 LGT | — | — |
| `9819466f23` | PASS | art. 95.1 LGT | — | — |
| `b129be09c5` | PASS | art. 95.1 LGT | — | — |
| `7141ffa3e3` | PASS | art. 95.1 LGT | — | — |
| `99c46eeea3` | PASS | art. 95.1 LGT | — | — |
| `df693b34bc` | PASS | art. 95.1 LGT | — | — |
| `a34c9c81c7` | PASS | art. 95.1 LGT | — | — |
| `0fae032cd8` | PASS | art. 95.1 LGT | — | — |
| `06afec77dd` | PASS | art. 95.1 LGT | — | — |
| `25b0312537` | PASS | art. 95.1 LGT | — | — |
| `d12fab40b2` | PASS | art. 95.1 LGT | — | — |
| `d15ae3b387` | PASS | art. 95.1 LGT | — | — |
| `1d3ac43493` | PASS | art. 95.1 LGT | — | — |
| `19c13fddc5` | PASS | art. 95.1 LGT | — | — |
| `3cb2d21450` | PASS | art. 95.2 LGT | — | — |
| `8bbfbd637c` | PASS | art. 95.2 LGT | — | — |
| `53462beaed` | PASS | art. 95.3 LGT | — | — |
| `77870ba1e1` | PASS | art. 95.3 LGT | — | — |
| `efc19d504d` | PASS | art. 95.3 LGT | — | — |
| `1cb3d2998c` | PASS | art. 95.4 LGT | — | — |
| `69cecdf673` | PASS | art. 95.5 LGT | — | — |
| `85afcd2c6a` | PASS | art. 95 bis.1 LGT | — | — |
| `c17353a8fc` | PASS | art. 95 bis.1 LGT | — | — |
| `e94282012f` | PASS | art. 95 bis.1 LGT | — | — |
| `3a3293d8f2` | PASS | art. 95 bis.1 LGT | — | — |
| `846ebcd38a` | PASS | art. 95 bis.2 LGT | — | — |
| `30142a0c44` | PASS | art. 95 bis.4 LGT | — | — |
| `42ff28b0d6` | PASS | art. 95 bis.4 LGT | — | — |
| `7089f9022b` | PASS | art. 95 bis.4 LGT | — | — |
| `ef34664dbc` | PASS | art. 95 bis.4 LGT | — | — |
| `3c9c07e7e7` | PASS | art. 95 bis.4 LGT | — | — |
| `b2936ea34e` | PASS | art. 95 bis.4 LGT | — | — |
| `5dcc69f208` | PASS | art. 95 bis.5 LGT | — | — |
| `967c5d9c14` | PASS | art. 95 bis.7 LGT | — | — |
| `4ffd088741` | PASS | art. 97 LGT | — | — |
| `f817b659e6` | PASS | art. 98.1 LGT | — | — |
| `c5e75f716f` | PASS | art. 98.2 LGT | — | — |
| `2504e85924` | PASS | art. 98.3 LGT | — | — |
| `a9d2c14ab9` | PASS | art. 98.4 LGT | — | — |
| `97f738711e` | PASS | art. 99.1 LGT | — | — |
| `25eed07cc5` | PASS | art. 99.2 LGT | — | — |
| `dc52f4904f` | PASS | art. 99.2 LGT | — | — |
| `e5f24c49a5` | PASS | art. 99.3 LGT | — | — |
| `18ea5cd4f0` | PASS | art. 99.4 LGT | — | — |
| `979392815b` | PASS | art. 99.4 LGT | — | — |
| `e16a8cf2de` | PASS | art. 99.6 LGT | — | — |
| `5fc30bb8a4` | PASS | art. 99.7 LGT | — | — |
| `ae19398d6b` | PASS | art. 99.7 LGT | — | — |
| `25af382a07` | PASS | art. 99.7 LGT | — | — |
| `b9a783e6ac` | PASS | art. 99.8 LGT | — | — |
| `a48dcb0709` | PASS | art. 99.8 LGT | — | — |
| `68324345e9` | PASS | art. 99.9 LGT | — | — |
| `31d8bd8f4f` | PASS | art. 99.9 LGT | — | — |
| `7b5b6438c6` | PASS | art. 91.1 RGAT | — | — |
| `8576ed8437` | PASS | art. 91.2 RGAT | — | — |
| `d744a3c1c8` | PASS | art. 91.3 RGAT | — | — |
| `c9c5713659` | PASS | art. 91.3 RGAT | — | — |
| `591655b500` | PASS | art. 91.3 RGAT | — | — |
| `e3110f6544` | PASS | art. 91.3 RGAT | — | — |
| `462d06e010` | PASS | art. 91.4 RGAT | — | — |
| `b5f44e8d4b` | FAIL | art. 91.5 RGAT | drops the second limb: «En el supuesto de que la circunstancia que impida la comparecencia se produzca transcurrido el citado plazo de tres días, se podrá solicitar el aplazamiento antes de la fecha señalada para la comparecencia» | Cuando el obligado tributario justifique circunstancias que le impidan comparecer en el lugar, día y hora fijados, podrá solicitar un aplazamiento dentro de los tres días siguientes al de la notificación del requerimiento o, si la circunstancia se produce transcurrido ese plazo, antes de la fecha señalada para la comparecencia (art. 91.5 RGAT). |
| `b290e3b3f4` | PASS | art. 91.6 RGAT | — | — |
| `46a6090b3a` | PASS | art. 100.1 LGT | — | — |
| `b0bb4afa6c` | PASS | art. 100.2 LGT | — | — |
| `384ad7947c` | PASS | art. 101.1 LGT | — | — |
| `cb35aa9487` | PASS | art. 101.1 LGT | — | — |
| `e92600b43f` | PASS | art. 101.2 LGT | — | — |
| `dfa2fbb546` | PASS | art. 101.3 LGT | — | — |
| `75ce5be4d4` | PASS | art. 101.3 LGT | — | — |
| `b88ab68dc2` | PASS | art. 101.3 LGT | — | — |
| `3a2803ab21` | PASS | art. 101.4 LGT | — | — |
| `8ec1de7352` | PASS | art. 101.4 LGT | — | — |
| `5bf862c9cc` | PASS | art. 101.4 LGT | — | — |
| `61ef6eba9e` | PASS | art. 101.4 LGT | — | — |
| `c750e5d65c` | PASS | art. 101.4 LGT | — | — |
| `223f380c2c` | PASS | art. 101.4 LGT | — | — |
| `73d759196a` | PASS | art. 102.1 LGT | — | — |
| `527d97d133` | PASS | art. 102.2 LGT | — | — |
| `c5d298f362` | PASS | art. 102.2 LGT | — | — |
| `d44ce5a6c2` | PASS | art. 102.2 LGT | — | — |
| `2a6c151507` | PASS | art. 102.2 LGT | — | — |
| `e09150f14e` | PASS | art. 102.2 LGT | — | — |
| `d45a9a0f5f` | PASS | art. 102.2 LGT | — | — |
| `be18530507` | PASS | art. 102.2 LGT | — | — |
| `d0771eb177` | PASS | art. 102.3 LGT | — | — |
| `82fe20eb1f` | PASS | art. 102.4 LGT | — | — |
| `d4911141f5` | PASS | art. 103.1 LGT | — | — |
| `e08ba743f1` | PASS | art. 103.2 LGT | — | — |
| `f20ab99261` | PASS | art. 103.2 LGT | — | — |
| `257e94200c` | PASS | art. 103.3 LGT | — | — |
| `e64937ba6b` | PASS | art. 104.1 LGT | — | — |
| `53c605fb7b` | PASS | art. 104.1 LGT | — | — |
| `8432a47299` | PASS | art. 104.1 LGT | — | — |
| `45277947ed` | PASS | art. 104.1 LGT | — | — |
| `08027d2d07` | PASS | art. 104.1 LGT | — | — |
| `2c60f293b7` | PASS | art. 104.1 LGT | — | — |
| `ac2aed52a1` | PASS | art. 102.1 RGAT | — | — |
| `b8f22aefd5` | PASS | art. 104.2 LGT | — | — |
| `f82e667822` | PASS | art. 104.2 LGT | — | — |
| `3384260494` | PASS | art. 104.2 LGT | — | — |
| `aa1b668bb6` | FAIL | art. 102.5 RGAT | after a sentence listing interrupciones, dilaciones and períodos de suspensión, «Se cuentan» reads as covering all three; art. 102.5 covers only «los períodos de interrupción justificada y las dilaciones por causa no imputable a la Administración» and sends the procedimiento inspector to art. 150 LGT and art. 184 RGAT | Los períodos de interrupción justificada y las dilaciones por causa no imputable a la Administración se cuentan por días naturales, salvo en el procedimiento inspector, que tiene sus propias reglas (art. 102.5 RGAT). |
| `f2268339f0` | PASS | art. 103 RGAT | — | — |
| `6bb9db4d92` | PASS | art. 103 RGAT | — | — |
| `5822df5ec9` | PASS | art. 103 RGAT | — | — |
| `8f69c04638` | PASS | art. 103 RGAT | — | — |
| `d85a0fa3c6` | PASS | art. 103 RGAT | — | — |
| `c640125728` | PASS | art. 103 RGAT | — | — |
| `78ab63d7c0` | PASS | art. 103 RGAT | — | — |
| `896965d11d` | PASS | art. 103 RGAT | — | — |
| `663598ed4d` | FAIL | art. 103.f) RGAT | «entre otras» is wrong: the letter names exactly three Juntas Arbitrales (art. 24 LOFCA, art. 66 Ley 12/2002 and art. 51 Ley 25/2003, Convenio con Navarra); if applied, the «Normativa» needs a line for the Navarra norm | f) Cuando se plantee el conflicto de competencias ante las Juntas Arbitrales previstas en el artículo 24 LOFCA, en el artículo 66 de la Ley 12/2002 y en el artículo 51 de la Ley 25/2003, de 15 de julio, por la que se aprueba la modificación del Convenio Económico entre el Estado y la Comunidad Foral de Navarra, por el tiempo que transcurra desde el planteamiento del conflicto hasta la resolución dictada por la respectiva Junta Arbitral. |
| `92002fff5c` | FAIL | art. 104 RGAT | the article lists nine letters a)–i); the lesson's lettered list a)–g) looks complete but omits h) (retraso por la disposición adicional tercera del RD 1363/2010) and i) (libros registro del IVA por la Sede electrónica); the intro must say the list is a selection | Entre las dilaciones por causa no imputable a la Administración tributaria que enumera el reglamento, que no es una lista cerrada, figuran estas (art. 104 RGAT): |
| `d89aaabc0a` | PASS | art. 104 RGAT | — | — |
| `d4b7c238de` | PASS | art. 104 RGAT | — | — |
| `915f8a3472` | PASS | art. 104 RGAT | — | — |
| `1daaa43796` | FAIL | art. 104.b) RGAT | drops the narrowing clause: «Cuando los documentos hubiesen sido requeridos durante la tramitación del procedimiento se aplicará lo dispuesto en el párrafo a) anterior» | La dilación se computa desde el día siguiente al de finalización del plazo de dicho trámite hasta la fecha en que se aporten; cuando los documentos hubiesen sido requeridos durante la tramitación del procedimiento, se aplica la letra a) (art. 104.b) RGAT). |
| `e1d815a149` | PASS | art. 104 RGAT | — | — |
| `17e5467538` | PASS | art. 104 RGAT | — | — |
| `66d3056bda` | PASS | art. 104 RGAT | — | — |
| `4ae9e0fb95` | PASS | art. 104 RGAT | — | — |
| `3984913852` | PASS | art. 104 RGAT | — | — |
| `66fc5f2c76` | PASS | art. 104 RGAT | — | — |
| `4a07ae17c3` | PASS | art. 104.3 LGT | — | — |
| `6a7baa28b2` | PASS | art. 104.3 LGT | — | — |
| `404903e25b` | PASS | art. 104.3 LGT | — | — |
| `6a8a7418f0` | PASS | art. 104.4 LGT | — | — |
| `a8a1d830c4` | PASS | art. 104.4 LGT | — | — |
| `f5e1a03e4b` | PASS | art. 104.4 LGT | — | — |
| `d92d8212e0` | PASS | art. 104.4 LGT | — | — |
| `33381be3bc` | PASS | art. 104.5 LGT | — | — |
| `efb2daf246` | PASS | art. 104.5 LGT | — | — |
| `baee4aed0d` | PASS | art. 104.5 LGT | — | — |
| `daa658b9ed` | PASS | structure (introduction) | — | — |
| `e4537bc29a` | PASS | structure (introduction) | — | — |
| `841bc821dc` | PASS | art. 104.1 LGT | — | — |
| `cf74eac847` | PASS | art. 104.1.a) LGT | — | — |
| `650fac2ef7` | PASS | art. 30.4 LPAC | — | — |
| `bfc4b30e74` | PASS | art. 30.4 LPAC | — | — |
| `1c917ccc26` | PASS | art. 104.b) RGAT | — | — |
| `d42c050475` | FAIL | art. 104.b) RGAT | voice: blacklisted split opener «Es…»; the fact is right | La aportación de nuevos documentos después del trámite de alegaciones es una dilación por causa no imputable a la Administración, que se computa desde el día siguiente al de finalización del plazo del trámite hasta la fecha en que se aportan (art. 104.b) RGAT). |
| `c47e1c8619` | PASS | art. 102.5 RGAT | — | — |
| `d6ce26247e` | PASS | art. 104.2 LGT | — | — |
| `e7a359299d` | PASS | structure (introduction) | — | — |
| `5e38153df7` | FAIL | art. 104.2 LGT; art. 14.2.a) LPAC | dates right (3-8-2026 is Monday, before the 4-8 deadline), but the step notifies a sociedad limitada on paper at the domicilio fiscal: a persona jurídica is obliged to relate electronically (art. 14.2.a) LPAC), and for such subjects art. 104.2 LGT, second paragraph, makes the puesta a disposición the act that meets the deadline; if applied, the LPAC «Normativa» line adds 14.2 | La Administración dicta la resolución el lunes 3 de agosto de 2026 y ese día la pone a disposición de Talleres Ribera, S.L., en la dirección electrónica habilitada, porque las personas jurídicas están obligadas a relacionarse con las Administraciones Públicas a través de medios electrónicos (art. 14.2.a) LPAC). |
| `e5b6704f23` | FAIL | art. 104.2 LGT | belongs to the paper attempt of the step, replaced in `5e38153df7` | drop |
| `64fe15c039` | FAIL | art. 104.2 LGT | follows the paper attempt; with the electronic notification the rule applied is the second paragraph of art. 104.2 LGT | La puesta a disposición, realizada antes del vencimiento, basta para entender cumplida la obligación de notificar dentro del plazo máximo, aunque Talleres Ribera, S.L., no acceda a su contenido hasta el miércoles 5 de agosto de 2026 (art. 104.2 LGT). |
| `fa1a2a4bf3` | FAIL | art. 104.2 LGT | result must follow step 7 as corrected; 4-8-2026 (Tuesday) is right: 15-7-2026 + 20 días naturales of dilación (11–30 April, both included, art. 104.b) RGAT) | Resultado: el plazo máximo vence el 4 de agosto de 2026 y la puesta a disposición del 3 de agosto lo cumple. |
| `cd34c875d7` | PASS | art. 105.1 LGT | — | — |
| `ae1dd961f7` | PASS | art. 105.2 LGT | — | — |
| `459b2e7972` | PASS | art. 106.1 LGT | — | — |
| `aadc7d0b4e` | PASS | art. 106.2 LGT | — | — |
| `39a8724319` | PASS | art. 106.3 LGT | — | — |
| `8f63c72ff5` | PASS | art. 106.4 LGT | — | — |
| `12767e4059` | PASS | art. 106.4 LGT | — | — |
| `9e93398ddc` | PASS | art. 107.1 LGT | — | — |
| `80fb5a801f` | PASS | art. 107.2 LGT | — | — |
| `75d2f591b3` | PASS | art. 108.1 LGT | — | — |
| `9969c7e049` | PASS | art. 108.2 LGT | — | — |
| `9041570217` | PASS | art. 108.3 LGT | — | — |
| `9151edb948` | PASS | art. 108.4 LGT | — | — |
| `720cd35af9` | PASS | art. 109 LGT | — | — |
| `7cf5ddef58` | PASS | art. 43.2 LPAC | — | — |
| `ace2a1008d` | PASS | art. 43.2 LPAC | — | — |
| `20f170230f` | PASS | art. 110.1 LGT | — | — |
| `2b3f49430e` | PASS | art. 110.2 LGT | — | — |
| `40334afa1a` | PASS | art. 111.1 LGT | — | — |
| `e7a2c20b34` | PASS | art. 111.2 LGT | — | — |
| `2b82c96172` | PASS | art. 112.1 LGT | — | — |
| `a4b83d01f1` | FAIL | art. 112.1 LGT | voice: blacklisted opener «Es…»; the fact is right | Un solo intento basta cuando el destinatario conste como desconocido en dicho domicilio o lugar (art. 112.1 LGT). |
| `071090a18a` | PASS | art. 112.1 LGT | — | — |
| `8ae666dc02` | PASS | art. 112.1 LGT | — | — |
| `72d911b733` | PASS | art. 112.2 LGT | — | — |
| `b7a040de8b` | PASS | art. 112.2 LGT | — | — |
| `5189222b3e` | PASS | art. 112.2 LGT | — | — |
| `8e996889a7` | PASS | art. 112.3 LGT | — | — |
| `b9e480681e` | PASS | art. 112.3 LGT | — | — |
| `997ee9d9ca` | PASS | structure (introduction) | — | — |
| `aaf38c4ec4` | PASS | structure (introduction) | — | — |
| `5eb4193107` | PASS | art. 110.2 LGT | — | — |
| `a18a9c795f` | PASS | art. 112.1 LGT | — | — |
| `7befd54fa1` | PASS | art. 112.1 LGT | — | — |
| `9ff42e23bf` | PASS | art. 112.1 LGT | — | — |
| `0dc86d711f` | PASS | art. 112.1 LGT | — | — |
| `650d11a6d1` | PASS | art. 112.2 LGT | — | — |
| `4c0878be07` | PASS | art. 112.2 LGT | — | — |
| `352d3ceecc` | PASS | art. 112.2 LGT | — | — |
| `caf3015825` | PASS | art. 112.2 LGT | — | — |
| `be80d5588c` | PASS | art. 112.1 LGT | — | — |
| `8c1745acbb` | PASS | art. 112.1 LGT | — | — |
| `d443221a34` | PASS | art. 104.1 LGT | — | — |
| `8698ae14f7` | PASS | art. 104.2 LGT | — | — |
| `fa1ce75cc8` | PASS | art. 110.1 LGT | — | — |
| `04cfa28022` | PASS | art. 73.1 RGAT | — | — |
| `b20aa2cabd` | PASS | art. 90.2 LGT | — | — |
| `86c8e3fa04` | PASS | arts. 91.4 y 91.5 LGT | — | — |
| `cd1811b304` | PASS | art. 75.2 RGAT | — | — |
| `adca57b3fe` | PASS | art. 95 bis.1 LGT | — | — |
| `598139bd0d` | FAIL | art. 86.1 LGT | «dicho año» in the article refers to «el año precedente»; here, after «durante el primer trimestre del año», it reads as the current year | El Ministerio de Hacienda difunde durante el primer trimestre del año una relación de todas las disposiciones tributarias aprobadas en el año precedente (art. 86.1 LGT). |
| `1801b057a2` | PASS | art. 101.4.b) LGT | — | — |
| `bd5c8664f3` | PASS | LGT (Ley 58/2003) | — | — |
| `2bcf5c9647` | PASS | RGAT (RD 1065/2007) | — | — |
| `0e5b93aee5` | PASS | LPAC (Ley 39/2015) | — | — |
| `2f7b50ef4d` | PASS | LOFCA (LO 8/1980) | — | — |
| `a3e32990ed` | PASS | Concierto Económico con el País Vasco (Ley 12/2002) | — | — |
| `042d0a92a9` | PASS | CE | — | — |
| `1501dde4f1` | FAIL | Normativa | two norms on one line; the spec asks one line per norm, starting with its `short` name; add a second line «LEC (Ley 1/2000): sin artículos concretos, citada en el art. 106.1 LGT.» | Código Civil: sin artículos concretos, citado en el art. 106.1 LGT. |

PASS 288 · FAIL 15
