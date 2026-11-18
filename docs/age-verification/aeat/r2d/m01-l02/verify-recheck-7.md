# Verify recheck 7 — `m01-l02`, part 2 of 4

Blind re-check (Opus) of `pending-part2.md` against the saved Reglamento del Congreso (2026-07-28) and Reglamento del Senado (2025-11-14). All 331 ids still match the current lesson text.

Normativa (no Normativa line is among the part-2 rows; checked against the rows' citations and named norms): the lesson's Normativa section covers Reglamento del Congreso arts. 1–207 and Reglamento del Senado arts. 1–196, but misses CE arts. 150 and 155 (named in art. 56.l) and 56.m) Reglamento del Senado, rows `349c15c473`, `be918d68c7`; the CE «nombrados en» line lists only arts. 18, 131 y 168), the Estatuto del Personal de las Cortes Generales (named in art. 27.6, row `2d80c60b79`) and the Reglamento de la Conferencia de Presidentes (named in art. 56 ter.3, row `f912be6796`). Those go on the «nombrado en …» lines or the final «no figuran en `normativa.yaml`» line.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `bdd7cfe217` | PASS | art. 204.4 Reglamento del Congreso | — | — |
| `2c84ca2a9a` | FAIL | art. 204.5 Reglamento del Congreso | turns two faculties into duties («se podrá reducir», «se podrá incluir» become «reduciendo», «con papeletas de») and drops the condition «si las circunstancias lo aconsejan» of the Presidencia's interruption | Si en la primera votación no se cubren los cuatro puestos con esos requisitos, se realizan sucesivas votaciones, en las que se puede reducir progresivamente el número de candidaturas a partir de un número no superior al doble del de puestos a cubrir y se puede incluir en las papeletas un número de candidaturas igual que el de puestos a cubrir; la Presidencia puede, si las circunstancias lo aconsejan, interrumpir por un plazo prudencial el curso de las votaciones (art. 204.5 Reglamento del Congreso). |
| `f6f1c58e3e` | PASS | art. 204.6 Reglamento del Congreso | — | — |
| `3d526f91c0` | PASS | art. 205.1 Reglamento del Congreso | — | — |
| `109a2ae782` | PASS | art. 205.2 Reglamento del Congreso | — | — |
| `1b8511395a` | PASS | art. 205.2 Reglamento del Congreso | — | — |
| `308012413f` | PASS | art. 205.2 Reglamento del Congreso | — | — |
| `89f04d86f9` | PASS | art. 205.2 Reglamento del Congreso | — | — |
| `0e2912a5c5` | PASS | art. 205.2 Reglamento del Congreso | — | — |
| `26a61978e0` | PASS | art. 206 Reglamento del Congreso | — | — |
| `aa98101857` | PASS | art. 207 Reglamento del Congreso | — | — |
| `c3021d2847` | PASS | art. 1.1 Reglamento del Senado | — | — |
| `fba821e90e` | PASS | art. 1.2 Reglamento del Senado | — | — |
| `7cdf1ea088` | FAIL | art. 1.3 Reglamento del Senado | subjectless: where it sits, after the sentence on Senadores designados, «deben» reads as applying only to them; art. 1.3 binds «Los Senadores» | Los Senadores, una vez presentada su credencial, deben formular las declaraciones de actividades, de bienes patrimoniales y rentas, y de intereses económicos del artículo 26 (art. 1.3 Reglamento del Senado). |
| `15591af79c` | PASS | art. 2.1 Reglamento del Senado | — | — |
| `554d7fa601` | PASS | art. 2.2 Reglamento del Senado | — | — |
| `d4db88311e` | PASS | art. 3 Reglamento del Senado | — | — |
| `0f20abd58b` | FAIL | art. 4.1 Reglamento del Senado | «un veinte por ciento o más de sus escaños» measures against the whole Senado; the article measures against «los escaños que éstos [Senadores de elección directa] suponen en el total de la Cámara», and the 80 % is «de Senadores de elección directa … de los mismos» | Tras la formación de la Mesa de edad, el Senado se constituye en forma definitiva, salvo que las impugnaciones formuladas contra la proclamación de Senadores de elección directa afecten a un veinte por ciento o más de los escaños que estos suponen en el total de la Cámara, en cuyo caso su constitución es interina hasta que las impugnaciones resueltas confirmen la proclamación de Senadores de elección directa en número no inferior al ochenta por ciento de los mismos (art. 4.1 Reglamento del Senado). |
| `8356116ea3` | FAIL | art. 4.2 Reglamento del Senado | drops the two routes («por iniciativa parlamentaria o como consecuencia de las comunicaciones del Gobierno») and extends the proposición requirement to every case; the article requires it only «para el ejercicio de aquella iniciativa» | Cuando el Senado está constituido interinamente, solo se ocupa del examen de las incompatibilidades, salvo que, por iniciativa parlamentaria o como consecuencia de las comunicaciones del Gobierno, se estime indispensable deliberar acerca de algún otro tema; para el ejercicio de aquella iniciativa se requiere una proposición firmada por un Grupo parlamentario o por veinticinco Senadores (art. 4.2 Reglamento del Senado). |
| `aec8fc072f` | PASS | art. 4 bis.1 Reglamento del Senado, art. 4 bis.2 Reglamento del Senado, art. 4 bis.3 Reglamento del Senado | — | — |
| `9b73222801` | PASS | art. 5.1 Reglamento del Senado, art. 5.2 Reglamento del Senado | — | — |
| `1ea61e4a43` | PASS | art. 6.1 Reglamento del Senado | — | — |
| `4ac12008af` | PASS | art. 6.2 Reglamento del Senado | — | — |
| `764446749f` | PASS | art. 7.1 Reglamento del Senado | — | — |
| `cd805eb021` | PASS | art. 7.2 Reglamento del Senado | — | — |
| `83ba6e775b` | PASS | arts. 8.1 y 8.2 Reglamento del Senado | — | — |
| `938404aceb` | PASS | art. 9 Reglamento del Senado | — | — |
| `87742ab671` | PASS | art. 10.1 Reglamento del Senado, art. 10.2 Reglamento del Senado, art. 10.3 Reglamento del Senado | — | — |
| `79dd54524f` | PASS | art. 11 bis Reglamento del Senado | — | — |
| `af2746eaa1` | PASS | art. 12.1 Reglamento del Senado | — | — |
| `ee90514343` | PASS | art. 12.1 Reglamento del Senado | — | — |
| `6cf03df036` | PASS | art. 12.1 Reglamento del Senado | — | — |
| `d4bb9ed3fc` | PASS | art. 12.1 Reglamento del Senado | — | — |
| `9da6a40392` | PASS | art. 12.2 Reglamento del Senado | — | — |
| `fae7c3825b` | PASS | art. 13 Reglamento del Senado | — | — |
| `dfb6564f49` | PASS | art. 14 Reglamento del Senado | — | — |
| `b884d81960` | PASS | art. 16.1 Reglamento del Senado | — | — |
| `399ad74107` | PASS | art. 16.2 Reglamento del Senado | — | — |
| `00042484ec` | PASS | art. 16.3 Reglamento del Senado, art. 16.4 Reglamento del Senado | — | — |
| `6470e7bec5` | PASS | art. 16.5 Reglamento del Senado | — | — |
| `c0214ef69d` | PASS | art. 17.1 Reglamento del Senado | — | — |
| `2251c0eeaf` | PASS | art. 17.2 Reglamento del Senado | — | — |
| `b747231595` | PASS | art. 18.1 Reglamento del Senado | — | — |
| `534027a448` | PASS | art. 18.1 Reglamento del Senado | — | — |
| `98720c76ec` | PASS | art. 18.1 Reglamento del Senado | — | — |
| `206015ccfc` | PASS | art. 18.1 Reglamento del Senado | — | — |
| `04dfdad778` | PASS | art. 18.1 Reglamento del Senado | — | — |
| `4338f15994` | PASS | art. 18.1 Reglamento del Senado | — | — |
| `1dfd861418` | PASS | art. 18.1 Reglamento del Senado | — | — |
| `77d90e48b5` | PASS | art. 18.1 Reglamento del Senado | — | — |
| `2593bdccc8` | PASS | art. 18.1 Reglamento del Senado | — | — |
| `23adb1e8e4` | PASS | art. 18.2 Reglamento del Senado | — | — |
| `af029d3c50` | PASS | art. 18.2 Reglamento del Senado | — | — |
| `a87f5a3268` | PASS | art. 18.2 Reglamento del Senado | — | — |
| `7bd3416b10` | PASS | art. 18.2 Reglamento del Senado | — | — |
| `05a8792010` | PASS | art. 19.1 Reglamento del Senado | — | — |
| `c1e025a3e2` | PASS | art. 19.2 Reglamento del Senado | — | — |
| `54f0dd463a` | PASS | art. 20.1 Reglamento del Senado, art. 20.3 Reglamento del Senado | — | — |
| `7a0335de04` | FAIL | art. 20 bis.1 Reglamento del Senado | «que obren en su poder» reads as the Senadores' possession; the article says «que obren en poder de estas» (the Administración and entities) | Previo conocimiento de su Grupo parlamentario, los Senadores pueden recabar de la Administración General del Estado y de cualesquiera organismos públicos y entidades de derecho público vinculados o dependientes de aquella los datos, informes o documentos que obren en poder de estas (art. 20 bis.1 Reglamento del Senado). |
| `bb99feb2fb` | PASS | art. 20 bis.2 Reglamento del Senado | — | — |
| `b13ee5ed7d` | PASS | art. 20 bis.3 Reglamento del Senado | — | — |
| `0c15c01fc0` | PASS | art. 20 bis.4 Reglamento del Senado | — | — |
| `a7a3fa4714` | PASS | art. 20 bis.5 Reglamento del Senado | — | — |
| `043b5ce1cb` | PASS | art. 21 Reglamento del Senado | — | — |
| `ce9853259e` | PASS | art. 22.1 Reglamento del Senado | — | — |
| `b620323299` | PASS | art. 22.2 Reglamento del Senado | — | — |
| `415374a338` | FAIL | art. 22.3 Reglamento del Senado | presents the debate as part of every such session; the article makes it optional («Se podrá abrir debate relativo a la concesión del suplicatorio») | El Senado se reúne en sesión secreta para ser informado del dictamen sobre el suplicatorio, y se puede abrir debate relativo a su concesión, con la presentación del Dictamen por un tiempo máximo de cinco minutos, un turno a favor y uno en contra, y un turno de portavoces, por tiempo de diez minutos cada uno (art. 22.3 Reglamento del Senado). |
| `47926e5a3b` | PASS | art. 22.4 Reglamento del Senado | — | — |
| `d40a21e0c6` | FAIL | art. 22.6 Reglamento del Senado | majority cut: the article says «por mayoría absoluta de sus miembros» | Concedido el suplicatorio y firme el auto de procesamiento, la Cámara puede acordar por mayoría absoluta de sus miembros, y según la naturaleza de los hechos imputados, la suspensión temporal en la condición de Senador, en sesión secreta en la que solo se admiten un turno a favor y uno en contra, y uno de portavoces, de diez minutos cada uno, sin audiencia al Senador interesado, y en su resolución puede acordar la privación de la asignación del Senador hasta su terminación (art. 22.6 Reglamento del Senado). |
| `7d17cdc232` | PASS | art. 23.1 Reglamento del Senado | — | — |
| `5aaa2a124d` | PASS | art. 23.2 Reglamento del Senado | — | — |
| `2e3c9259e0` | PASS | art. 23.3 Reglamento del Senado | — | — |
| `65c40aede2` | PASS | art. 24.1 Reglamento del Senado | — | — |
| `4f1997b711` | PASS | art. 24.2 Reglamento del Senado, art. 24.3 Reglamento del Senado | — | — |
| `4aa250def6` | PASS | art. 25 Reglamento del Senado | — | — |
| `61f2acb763` | PASS | art. 26.1 Reglamento del Senado, art. 26.2 Reglamento del Senado | — | — |
| `c5e9ca24eb` | PASS | art. 26.3 Reglamento del Senado | — | — |
| `ee4e7c0603` | PASS | art. 27.3 Reglamento del Senado | — | — |
| `c6ce02a1b8` | PASS | art. 27.4 Reglamento del Senado, art. 27.5 Reglamento del Senado | — | — |
| `2d80c60b79` | PASS | art. 27.6 Reglamento del Senado | — | — |
| `6f4e2f8b7b` | FAIL | art. 28.1 Reglamento del Senado | drops the plazo «En el término de cinco días hábiles, contados desde la constitución del Senado», which the next sentence (616f3bd85d, «el plazo de cinco días hábiles») presupposes | En el término de cinco días hábiles, contados desde la constitución del Senado, los Senadores que resuelvan constituirse en Grupo parlamentario entregan en la Presidencia de la Cámara la relación nominal de quienes lo integran, suscrita por todos los componentes del Grupo, con la denominación de este y el nombre del Senador que actúa como Portavoz y los de quienes, eventualmente, hayan de sustituirle (art. 28.1 Reglamento del Senado). |
| `616f3bd85d` | PASS | art. 28.2 Reglamento del Senado, art. 28.3 Reglamento del Senado | — | — |
| `18812cbf6d` | PASS | art. 29 Reglamento del Senado | — | — |
| `92bd3b938c` | PASS | art. 30.1 Reglamento del Senado | — | — |
| `c8f4b63991` | PASS | art. 30.2 Reglamento del Senado | — | — |
| `1ed456c566` | PASS | art. 30.3 Reglamento del Senado | — | — |
| `54361c7305` | PASS | art. 31 Reglamento del Senado | — | — |
| `875a012eeb` | PASS | art. 32.1 Reglamento del Senado | — | — |
| `745d1da606` | PASS | art. 32.2 Reglamento del Senado, art. 32.3 Reglamento del Senado | — | — |
| `cfa8713c1f` | PASS | art. 33 Reglamento del Senado | — | — |
| `c046d3147c` | PASS | art. 35 Reglamento del Senado | — | — |
| `2b13d00d90` | PASS | art. 36.1 Reglamento del Senado | — | — |
| `c9ab61a4f9` | PASS | art. 36.1 Reglamento del Senado | — | — |
| `42489607a5` | PASS | art. 36.1 Reglamento del Senado | — | — |
| `b238ebd3c7` | PASS | art. 36.1 Reglamento del Senado | — | — |
| `b1d5af70f0` | PASS | art. 36.1 Reglamento del Senado | — | — |
| `0ace03ca4b` | PASS | art. 36.1 Reglamento del Senado | — | — |
| `b23199f603` | PASS | art. 36.1 Reglamento del Senado | — | — |
| `3473195447` | PASS | art. 36.1 Reglamento del Senado | — | — |
| `56fc5ce929` | PASS | art. 36.1 Reglamento del Senado | — | — |
| `21412b08b1` | PASS | art. 36.1 Reglamento del Senado | — | — |
| `c16f9f12c4` | PASS | art. 36.2 Reglamento del Senado | — | — |
| `e4d43e28ba` | PASS | art. 36.3 Reglamento del Senado | — | — |
| `d520559546` | PASS | art. 37 Reglamento del Senado | — | — |
| `3b65a6f64e` | PASS | art. 37 Reglamento del Senado | — | — |
| `e4b6687279` | PASS | art. 37 Reglamento del Senado | — | — |
| `35f28911d6` | PASS | art. 37 Reglamento del Senado | — | — |
| `78d10040f9` | PASS | art. 37 Reglamento del Senado | — | — |
| `6ca61591e5` | PASS | art. 37 Reglamento del Senado | — | — |
| `ff9a547f7a` | PASS | art. 37 Reglamento del Senado | — | — |
| `d809fb33c4` | PASS | art. 37 Reglamento del Senado | — | — |
| `5b3553ef41` | PASS | art. 37 Reglamento del Senado | — | — |
| `6eb8ef4c2e` | PASS | art. 37 Reglamento del Senado | — | — |
| `375b8b9fee` | PASS | art. 37 Reglamento del Senado | — | — |
| `048a95a40f` | PASS | art. 37 Reglamento del Senado | — | — |
| `c82844861b` | PASS | art. 37 Reglamento del Senado | — | — |
| `fda04fc05f` | PASS | art. 38 Reglamento del Senado | — | — |
| `50b750041c` | PASS | art. 39 Reglamento del Senado | — | — |
| `67603b0fec` | PASS | art. 40 Reglamento del Senado | — | — |
| `3b49b7a7bf` | PASS | art. 41 Reglamento del Senado | — | — |
| `ccf804a738` | PASS | art. 41 Reglamento del Senado | — | — |
| `3d26e3837c` | PASS | art. 41 Reglamento del Senado | — | — |
| `2f0a2b68f1` | PASS | art. 41 Reglamento del Senado | — | — |
| `1c8548e287` | PASS | art. 41 Reglamento del Senado | — | — |
| `1cb7bbc777` | PASS | art. 41 Reglamento del Senado | — | — |
| `3a58899757` | PASS | art. 41 Reglamento del Senado | — | — |
| `9b8b9907ea` | PASS | art. 42 Reglamento del Senado | — | — |
| `4151aece0c` | PASS | art. 43.1 Reglamento del Senado | — | — |
| `42f72f1483` | PASS | art. 43.2 Reglamento del Senado | — | — |
| `8c9d6dc583` | PASS | art. 43.3 Reglamento del Senado | — | — |
| `7e3b1fe982` | PASS | art. 44.1 Reglamento del Senado, art. 44.2 Reglamento del Senado | — | — |
| `2bfead3ef3` | PASS | art. 44 bis.1 Reglamento del Senado, art. 44 bis.2 Reglamento del Senado | — | — |
| `0ca24f37a2` | PASS | art. 45.1 Reglamento del Senado | — | — |
| `6d060eef95` | PASS | art. 45.2 Reglamento del Senado, art. 45.3 Reglamento del Senado | — | — |
| `8ce62082d0` | PASS | art. 46 Reglamento del Senado | — | — |
| `24f160f96d` | PASS | art. 47 Reglamento del Senado | — | — |
| `12cc69e22c` | PASS | art. 48.1 Reglamento del Senado | — | — |
| `e383897211` | PASS | art. 48.2 Reglamento del Senado | — | — |
| `523da83008` | PASS | art. 49.1 Reglamento del Senado | — | — |
| `ff1d26a5a1` | PASS | art. 49.2 Reglamento del Senado | — | — |
| `3ea06f61c1` | PASS | art. 49.3 Reglamento del Senado | — | — |
| `9605018a8a` | PASS | art. 49.4 Reglamento del Senado, art. 49.5 Reglamento del Senado | — | — |
| `b5752985d4` | PASS | art. 50 Reglamento del Senado | — | — |
| `1c61ee5359` | PASS | art. 51.1 Reglamento del Senado | — | — |
| `e0ce0e3387` | PASS | art. 51.2 Reglamento del Senado | — | — |
| `e459a39097` | PASS | art. 51.3 Reglamento del Senado | — | — |
| `5c97f9f0c4` | PASS | art. 51.4 Reglamento del Senado | — | — |
| `e7bb7b99a6` | FAIL | art. 52.1 Reglamento del Senado | drops when the designation happens («Después de la constitución del Senado o cuando durante el transcurso de la Legislatura se cree una nueva Comisión») and the sujeción to art. 51 | Después de la constitución del Senado o cuando durante el transcurso de la Legislatura se cree una nueva Comisión, y dentro del plazo que fije su Presidente, los Grupos parlamentarios comunican por escrito cuáles de sus miembros deben formar parte de las distintas Comisiones, con sujeción a lo dispuesto en el artículo 51 (art. 52.1 Reglamento del Senado). |
| `46fda80578` | PASS | art. 52.2 Reglamento del Senado | — | — |
| `a17575f521` | PASS | art. 53.1 Reglamento del Senado | — | — |
| `671283d1d5` | PASS | art. 53.3 Reglamento del Senado | — | — |
| `e3bc9840ce` | PASS | art. 54 Reglamento del Senado | — | — |
| `62bb23586d` | FAIL | art. 55 Reglamento del Senado | drops the composition the article sets («un Presidente, dos Vicepresidentes y cuatro Secretarios»), which differs from the other Comisiones (two Secretarios, art. 53.2) | La Mesa de la Comisión General de las Comunidades Autónomas está integrada por un Presidente, dos Vicepresidentes y cuatro Secretarios, observándose para su elección las mismas normas establecidas para la elección de la Mesa del Senado; si ningún Grupo parlamentario se opone, la propuesta para cubrir los puestos se puede aprobar por asentimiento, sin necesidad de proceder a la votación por papeletas (art. 55 Reglamento del Senado). |
| `1d8f1dbe93` | PASS | art. 56 Reglamento del Senado | — | — |
| `422eebf90a` | PASS | art. 56 Reglamento del Senado | — | — |
| `581e1b7dfe` | PASS | art. 56 Reglamento del Senado | — | — |
| `68b703b7fc` | PASS | art. 56 Reglamento del Senado | — | — |
| `e04c2da468` | PASS | art. 56 Reglamento del Senado | — | — |
| `f2da469bed` | PASS | art. 56 Reglamento del Senado | — | — |
| `ea5cc4e06a` | PASS | art. 56 Reglamento del Senado | — | — |
| `7cc7d691ca` | PASS | art. 56 Reglamento del Senado | — | — |
| `e4323e36a2` | PASS | art. 56 Reglamento del Senado | — | — |
| `2e76950f21` | PASS | art. 56 Reglamento del Senado | — | — |
| `8fd0f99f90` | PASS | art. 56 Reglamento del Senado | — | — |
| `80128cca55` | PASS | art. 56 Reglamento del Senado | — | — |
| `349c15c473` | PASS | art. 56 Reglamento del Senado | — | — |
| `be918d68c7` | PASS | art. 56 Reglamento del Senado | — | — |
| `b95f7adf60` | PASS | art. 56 Reglamento del Senado | — | — |
| `dee2a68760` | PASS | art. 56 Reglamento del Senado | — | — |
| `43972d0227` | PASS | art. 56 Reglamento del Senado | — | — |
| `490d64c5a1` | PASS | art. 56 Reglamento del Senado | — | — |
| `d748bd14ef` | PASS | art. 56 Reglamento del Senado | — | — |
| `ad164cd579` | PASS | art. 56 Reglamento del Senado | — | — |
| `6cc58cbd11` | PASS | art. 56 Reglamento del Senado | — | — |
| `fe9f46893c` | PASS | art. 56 Reglamento del Senado | — | — |
| `ca8c838137` | PASS | art. 56 Reglamento del Senado | — | — |
| `8133b39f00` | PASS | art. 56 Reglamento del Senado | — | — |
| `2745fe5d4e` | PASS | art. 56 bis.1 Reglamento del Senado | — | — |
| `02e74df97f` | FAIL | art. 56 bis.2 Reglamento del Senado | attaches «representados por su Presidente o por el miembro designado» and the no-accreditation rule to the Gobierno as well (they belong to the Consejos de Gobierno, apartados 2–3) and drops the salvedad of apartado 3 («si bien cuando se le confiera a más de una persona … deberá advertirse … a la Mesa de la Comisión») | El Gobierno puede intervenir en las sesiones de la Comisión General de las Comunidades Autónomas, y también pueden hacerlo los Consejos de Gobierno de las Comunidades Autónomas, representados por su Presidente o por el miembro del correspondiente órgano colegiado de gobierno designado para ello; esa representación no precisa ser acreditada, si bien cuando se confiera a más de una persona para una misma sesión, para intervenir en distintos puntos del orden del día, debe advertirse de ello con anticipación a la Mesa de la Comisión (art. 56 bis.2 Reglamento del Senado). |
| `c00413e46c` | PASS | art. 56 bis.3 Reglamento del Senado | — | — |
| `81432da665` | PASS | art. 56 bis.4 Reglamento del Senado | — | — |
| `71f399fae4` | PASS | art. 56 bis.5 Reglamento del Senado | — | — |
| `262932396e` | PASS | art. 56 bis.6 Reglamento del Senado | — | — |
| `5b1db2f1cf` | PASS | art. 56 bis.7 Reglamento del Senado, art. 56 bis.8 Reglamento del Senado | — | — |
| `dd3effe152` | PASS | art. 56 bis.9 Reglamento del Senado | — | — |
| `318ed50ecc` | PASS | art. 56 ter.1 Reglamento del Senado | — | — |
| `534ab2010f` | FAIL | art. 56 ter.2 Reglamento del Senado | drops «con sujeción a los requisitos del apartado anterior» (two grupos or veinticinco senadores, motivación) for the further proposals, and «inmediata» for the publication | Presentada una propuesta de inclusión de un asunto en el orden del día de la Conferencia de Presidentes, la Presidencia del Senado dispone su inmediata publicación oficial y se abre acto seguido un plazo no superior a quince días en el que, con sujeción a los mismos requisitos, pueden presentarse otras propuestas, que deben versar sustancialmente sobre el mismo objeto o materia que la presentada en primer lugar (art. 56 ter.2 Reglamento del Senado). |
| `f912be6796` | PASS | art. 56 ter.3 Reglamento del Senado, art. 56 ter.4 Reglamento del Senado | — | — |
| `17b83f534c` | PASS | art. 56 ter.5 Reglamento del Senado, art. 56 ter.6 Reglamento del Senado | — | — |
| `0115051068` | PASS | art. 56 quater.1 Reglamento del Senado | — | — |
| `328ab9ed97` | PASS | art. 56 quater.2 Reglamento del Senado | — | — |
| `d6728851d6` | PASS | art. 56 quater.2 Reglamento del Senado | — | — |
| `56a6537d0e` | PASS | art. 56 quater.2 Reglamento del Senado | — | — |
| `e209a23ed5` | PASS | art. 56 quater.2 Reglamento del Senado | — | — |
| `1fa90a3b0b` | PASS | art. 56 quater.2 Reglamento del Senado | — | — |
| `4804a3fc3a` | PASS | art. 56 quater.2 Reglamento del Senado | — | — |
| `fe13f2eabb` | PASS | art. 56 quater.2 Reglamento del Senado | — | — |
| `ea331d4df6` | PASS | art. 56 quater.2 Reglamento del Senado | — | — |
| `539aeb5ce5` | PASS | art. 56 quater.2 Reglamento del Senado | — | — |
| `59928cb1cd` | FAIL | art. 56 quater.2.i) Reglamento del Senado | extraction artefact: after letra i) the row carries the whole text of art. 56 quater.5 (apartados «1.», «2.», «3.»), which is not part of art. 56 quater.2 and renders inside the wrong row | \| i) \| Sin perjuicio de las funciones recogidas en los apartados anteriores, la Comisión General de las Entidades Locales ejercerá todas aquéllas de carácter no legislativo que el Reglamento atribuye de modo genérico a las Comisiones de la Cámara o las que le encomiende la Mesa del Senado, siempre que estén relacionadas con cuestiones locales. \| art. 56 quater.2 Reglamento del Senado \| |
| `08aa703958` | PASS | art. 56 quater.3 Reglamento del Senado | — | — |
| `8d0a136c34` | PASS | art. 56 quater.4 Reglamento del Senado | — | — |
| `41c9c75766` | FAIL | art. 56 quater.5 and 56 quater.6 Reglamento del Senado | glosses by comparison («el mismo registro … que en la Comisión General de las Comunidades Autónomas») instead of the article's rule, and drops the Gobierno's first turn and the Portavoces' turno de fijación de posiciones | Para cada punto del orden del día, los oradores que deseen intervenir se inscriben en un registro que permanece abierto hasta media hora antes del inicio de la sesión; si el Gobierno solicita el uso de la palabra inicia el turno de oradores, y concluidas las intervenciones de cada punto los Portavoces, si lo solicitan, pueden disponer de un turno de fijación de posiciones (art. 56 quater.5 Reglamento del Senado); cuando la Mesa de la Cámara le encomienda la tramitación de iniciativas legislativas, observa en su funcionamiento lo establecido para las demás Comisiones legislativas del Senado (art. 56 quater.6 Reglamento del Senado). |
| `62bc021122` | PASS | art. 57 Reglamento del Senado | — | — |
| `109b097f63` | PASS | art. 58 Reglamento del Senado | — | — |
| `ba9758fb22` | PASS | art. 59.1 Reglamento del Senado, art. 59.2 Reglamento del Senado | — | — |
| `e472779af3` | PASS | art. 60.1 Reglamento del Senado | — | — |
| `3806707c70` | PASS | art. 60.2 Reglamento del Senado | — | — |
| `ef67dd0de2` | PASS | art. 60.3 Reglamento del Senado | — | — |
| `a68c2e590d` | PASS | art. 60.4 Reglamento del Senado | — | — |
| `5c7d7f998c` | PASS | art. 60.5 Reglamento del Senado | — | — |
| `7d49bc945f` | PASS | art. 60.6 Reglamento del Senado | — | — |
| `f299069670` | PASS | art. 61.1 Reglamento del Senado, art. 61.2 Reglamento del Senado | — | — |
| `d1fd68efcf` | PASS | art. 61.3 Reglamento del Senado, art. 61.4 Reglamento del Senado | — | — |
| `69f76b9262` | PASS | art. 61.5 Reglamento del Senado, art. 61.6 Reglamento del Senado | — | — |
| `7b39e63df3` | PASS | art. 61.7 Reglamento del Senado | — | — |
| `1cdd9b8561` | PASS | art. 61.8 Reglamento del Senado, art. 61.9 Reglamento del Senado | — | — |
| `78348a1915` | PASS | art. 61.10 Reglamento del Senado | — | — |
| `2e4eaafe9c` | PASS | art. 62.1 Reglamento del Senado, art. 62.2 Reglamento del Senado | — | — |
| `6f995c43fd` | PASS | art. 63 Reglamento del Senado | — | — |
| `55ba56e230` | PASS | art. 64 Reglamento del Senado | — | — |
| `5d215e2509` | PASS | art. 64 bis Reglamento del Senado | — | — |
| `b0a707c596` | PASS | art. 65.1 Reglamento del Senado | — | — |
| `f2e80a74f0` | PASS | art. 65.2 Reglamento del Senado | — | — |
| `5519305229` | PASS | art. 65.3 Reglamento del Senado | — | — |
| `1c15706665` | PASS | art. 65 bis.1 Reglamento del Senado | — | — |
| `5ed0df4817` | PASS | art. 65 bis.2 Reglamento del Senado, art. 65 bis.3 Reglamento del Senado, art. 65 bis.4 Reglamento del Senado, art. 65 bis.5 Reglamento del Senado | — | — |
| `8b9a051f43` | PASS | art. 65 bis.6 Reglamento del Senado | — | — |
| `31da2b7d88` | PASS | art. 65 bis.7 Reglamento del Senado, art. 65 bis.8 Reglamento del Senado | — | — |
| `5a6e2f69b3` | PASS | art. 65 bis.9 Reglamento del Senado | — | — |
| `e6a8bd819e` | PASS | art. 65 bis.10 Reglamento del Senado | — | — |
| `1821b693fd` | PASS | art. 65 bis.11 Reglamento del Senado | — | — |
| `15cf690171` | PASS | art. 66.1 Reglamento del Senado | — | — |
| `d9889bfde2` | PASS | art. 66.2 Reglamento del Senado | — | — |
| `09b03ea3d6` | PASS | art. 66.3 Reglamento del Senado | — | — |
| `ae57ee6a6b` | PASS | art. 66.4 Reglamento del Senado | — | — |
| `cd815d348a` | PASS | art. 66.5 Reglamento del Senado | — | — |
| `c0b1311617` | PASS | art. 67.1 Reglamento del Senado | — | — |
| `6b023620f7` | PASS | art. 67.2 Reglamento del Senado | — | — |
| `16ee2f1bb9` | PASS | art. 68 Reglamento del Senado | — | — |
| `fce31f9d5e` | PASS | art. 69.1 Reglamento del Senado | — | — |
| `36c19dec04` | PASS | art. 69.2 Reglamento del Senado | — | — |
| `d0d2819bfa` | PASS | art. 70.1 Reglamento del Senado | — | — |
| `b3881c3be4` | PASS | art. 70.2 Reglamento del Senado | — | — |
| `ec9b92c44e` | PASS | art. 71.1 Reglamento del Senado | — | — |
| `38ea470af1` | PASS | art. 71.2 Reglamento del Senado | — | — |
| `eb12cd7d2f` | PASS | art. 71.3 Reglamento del Senado | — | — |
| `05fa4e0e29` | PASS | art. 71.4 Reglamento del Senado | — | — |
| `86cfbaa898` | PASS | art. 72 Reglamento del Senado | — | — |
| `f1866b92ef` | PASS | art. 73 Reglamento del Senado | — | — |
| `bac592d28d` | PASS | art. 74 Reglamento del Senado | — | — |
| `a0514ab82f` | PASS | art. 75.1 Reglamento del Senado | — | — |
| `0fe68c4bd4` | PASS | art. 75.2 Reglamento del Senado | — | — |
| `3645963a6c` | PASS | art. 75.3 Reglamento del Senado | — | — |
| `833664066d` | PASS | art. 76 Reglamento del Senado | — | — |
| `ca9774e163` | PASS | art. 80 Reglamento del Senado | — | — |
| `b9a777d240` | PASS | art. 81.1 Reglamento del Senado | — | — |
| `7be7ddb631` | PASS | art. 82 Reglamento del Senado | — | — |
| `a73748c76e` | PASS | art. 83.1 Reglamento del Senado, art. 83.2 Reglamento del Senado | — | — |
| `0bdcfffe14` | PASS | art. 84.1 Reglamento del Senado | — | — |
| `3e5a051778` | PASS | art. 84.2 Reglamento del Senado | — | — |
| `09a80f4739` | PASS | art. 84.3 Reglamento del Senado | — | — |
| `22eff08d3a` | PASS | art. 84.4 Reglamento del Senado, art. 84.5 Reglamento del Senado | — | — |
| `5c44c09f54` | PASS | art. 85 Reglamento del Senado | — | — |
| `b41c85bb5a` | PASS | art. 86 Reglamento del Senado | — | — |
| `3cb8097021` | PASS | art. 88.1 Reglamento del Senado, art. 88.2 Reglamento del Senado, art. 88.3 Reglamento del Senado | — | — |
| `2baa9fcd95` | FAIL | art. 88.4 Reglamento del Senado | drops the limit the article attaches to the turn («para que, sin entrar en el fondo del asunto en debate, conteste estrictamente a las alusiones realizadas») and «a juicio de la Presidencia» | Cuando, a juicio de la Presidencia, en el desarrollo de un debate se hacen alusiones que afectan a la dignidad de un Grupo parlamentario o de un partido político con el que esté vinculado, la Presidencia puede conceder a un representante de aquel el uso de la palabra por tiempo no superior a tres minutos, para que, sin entrar en el fondo del asunto en debate, conteste estrictamente a las alusiones realizadas (art. 88.4 Reglamento del Senado). |
| `87c32c0f7f` | FAIL | art. 89 Reglamento del Senado | «cualquier documento» drops the article's condition «que pueda conducir a la ilustración del asunto de que se trate» | Cualquier Senador puede pedir, durante la discusión o antes de votar, la lectura de cualquier documento que pueda conducir a la ilustración del asunto de que se trate, y la Presidencia puede denegar o dar por finalizadas las lecturas que considere inoportunas o dilatorias (art. 89 Reglamento del Senado). |
| `143bb8e6bc` | PASS | art. 90.1 Reglamento del Senado, art. 90.2 Reglamento del Senado | — | — |
| `33882086a7` | PASS | art. 91 Reglamento del Senado | — | — |
| `60c30227f1` | PASS | art. 92.1 Reglamento del Senado | — | — |
| `2298d21193` | PASS | art. 92.3 Reglamento del Senado | — | — |
| `832fe44f26` | PASS | art. 92.3 Reglamento del Senado | — | — |
| `84ba5a240d` | PASS | art. 92.3 Reglamento del Senado | — | — |
| `830292e9e0` | PASS | art. 92.3 Reglamento del Senado | — | — |
| `7aa4a8d2f0` | PASS | art. 92.3 Reglamento del Senado | — | — |
| `9fe02d21b2` | PASS | art. 92.3 Reglamento del Senado | — | — |
| `8686dc27fe` | PASS | art. 92.3 Reglamento del Senado | — | — |
| `62f56d14e3` | FAIL | art. 92.3.g) Reglamento del Senado | the closing paragraphs of art. 92.3 («A tal efecto, el Senador cursará la oportuna solicitud…», the voting system, the Mesa's rules) apply to every letra a)–g) but render inside row g); move them after the table as their own sentence with its citation | \| g) \| otras situaciones excepcionales e imprevisibles no contempladas en los apartados anteriores. \| art. 92.3 Reglamento del Senado \| |
| `515bb402e5` | PASS | art. 92.4 Reglamento del Senado | — | — |
| `a6e6727632` | PASS | art. 92.5 Reglamento del Senado, art. 92.6 Reglamento del Senado | — | — |
| `966a2872a1` | PASS | art. 93.1 Reglamento del Senado | — | — |
| `f37a39abf1` | PASS | art. 93.2 Reglamento del Senado | — | — |
| `8bf963e064` | PASS | art. 93.3 Reglamento del Senado | — | — |
| `2eab919f67` | PASS | art. 93.4 Reglamento del Senado, art. 93.5 Reglamento del Senado | — | — |
| `f308b8def3` | PASS | art. 94 Reglamento del Senado | — | — |
| `aeb7455f4b` | PASS | art. 95.1 Reglamento del Senado | — | — |
| `cdf44e710e` | PASS | art. 96.1 Reglamento del Senado | — | — |
| `eebe423973` | PASS | art. 96.2 Reglamento del Senado, art. 96.3 Reglamento del Senado | — | — |
| `9b4edac394` | PASS | art. 97.1 Reglamento del Senado | — | — |
| `8da40e5047` | PASS | art. 97.2 Reglamento del Senado, art. 97.3 Reglamento del Senado | — | — |
| `f009ea429a` | PASS | art. 98 Reglamento del Senado | — | — |
| `58225ad792` | PASS | art. 99.1 Reglamento del Senado | — | — |
| `fd287965b4` | PASS | art. 100.1 Reglamento del Senado | — | — |
| `96f9831137` | PASS | art. 100.3 Reglamento del Senado | — | — |
| `7e09177d5d` | PASS | art. 100.4 Reglamento del Senado | — | — |
| `6fbb8633c1` | PASS | art. 101.1 Reglamento del Senado | — | — |
| `36d358f451` | PASS | art. 101.2 Reglamento del Senado | — | — |
| `1f3f50a1fd` | PASS | art. 101.3 Reglamento del Senado | — | — |
| `2199b18a11` | PASS | art. 102.1 Reglamento del Senado | — | — |
| `131a26916c` | PASS | art. 102.2 Reglamento del Senado | — | — |
| `9ea546e385` | PASS | art. 102.3 Reglamento del Senado | — | — |
| `f817913695` | PASS | art. 102.4 Reglamento del Senado | — | — |
| `ad9b9cecd5` | PASS | art. 103 Reglamento del Senado | — | — |
| `b14a1bb036` | PASS | art. 104.1 Reglamento del Senado | — | — |
| `b148a97613` | PASS | art. 104.2 Reglamento del Senado, art. 104.3 Reglamento del Senado | — | — |
| `91e0b622bd` | PASS | art. 106.1 Reglamento del Senado | — | — |
| `79946c18b3` | PASS | art. 106.2 Reglamento del Senado, art. 106.3 Reglamento del Senado | — | — |
| `1229b36818` | PASS | art. 106.4 Reglamento del Senado | — | — |
| `f81e51c446` | PASS | art. 107.1 Reglamento del Senado | — | — |
| `fc2f68eb84` | PASS | art. 107.2 Reglamento del Senado | — | — |
| `53a77c5e92` | PASS | art. 107.3 Reglamento del Senado | — | — |
| `11671a2033` | PASS | art. 107 bis Reglamento del Senado | — | — |
| `ef3b14bf85` | PASS | art. 108.1 Reglamento del Senado | — | — |
| `37fe4635b1` | FAIL | art. 108.2 Reglamento del Senado | drops «con sujeción a los requisitos del apartado anterior» for the further proposiciones, «inmediata» publication and «que deberán versar sustancialmente» | Presentada una proposición de ley, la Mesa del Senado la califica y, de admitirse, dispone su inmediata publicación oficial, abriéndose acto seguido un plazo no superior a quince días en el que, con sujeción a los requisitos del apartado 1, pueden presentarse otras proposiciones de ley, que deben versar sustancialmente sobre el mismo objeto o materia que la presentada en primer lugar (art. 108.2 Reglamento del Senado). |
| `cce5e1c463` | PASS | art. 108.3 Reglamento del Senado | — | — |
| `b2232d09c2` | PASS | art. 108.4 Reglamento del Senado | — | — |
| `2007907ceb` | PASS | art. 108.5 Reglamento del Senado | — | — |
| `21e95597f2` | PASS | art. 108.6 Reglamento del Senado | — | — |
| `7d808c6da8` | PASS | art. 109 Reglamento del Senado | — | — |
| `d944d50f9c` | PASS | art. 110 Reglamento del Senado | — | — |
| `97c0ec1d8f` | PASS | art. 111 Reglamento del Senado | — | — |
| `82fdcf9f68` | PASS | art. 112 Reglamento del Senado | — | — |
| `4ce9813aed` | PASS | art. 113 Reglamento del Senado | — | — |
| `9da511e2de` | PASS | art. 114.1 Reglamento del Senado | — | — |
| `58a2441c49` | FAIL | arts. 114.2 and 114.3 Reglamento del Senado | drops the conditions on the Presidente's powers: limiting «cuando así lo exija la debida tramitación del texto legislativo» and a different order only «excepcionalmente»; also drops «por el mismo orden expuesto en el apartado anterior» | Si no hay propuestas de veto o no se aprueba ninguna, se efectúa el debate de las enmiendas, con un turno a favor y un turno en contra de cada bloque de enmiendas presentadas por un mismo Senador o Grupo parlamentario, por el mismo orden del apartado anterior, seguido de un turno de portavoces (art. 114.2 Reglamento del Senado); los tiempos de cada turno los fija el Presidente de la Comisión, que puede limitar el número y la duración de las intervenciones cuando así lo exija la debida tramitación del texto legislativo o, excepcionalmente, acordar un orden de debate distinto (art. 114.3 Reglamento del Senado). |
| `329ac67932` | FAIL | art. 115.1 Reglamento del Senado | drops the admission requirements («deberá ser congruente con las enmiendas de las que trae causa y deberá estar suscrita por los autores de las mismas») and the inadmission and reconsideración regime | Durante la sesión de la Comisión, el Presidente puede admitir a trámite enmiendas transaccionales presentadas en ese momento y por escrito, tendentes a alcanzar un acuerdo entre dos o más enmiendas o entre una o varias enmiendas y el texto remitido por el Congreso de los Diputados, que deben ser congruentes con las enmiendas de las que traen causa y estar suscritas por sus autores; las enmiendas en que se sustentan se tienen por sustituidas y no se someten a votación, y frente a la inadmisión cabe solicitar reconsideración ante la Mesa de la Cámara (art. 115.1 Reglamento del Senado). |
| `6060abf2b3` | PASS | art. 115.2 Reglamento del Senado, art. 115.3 Reglamento del Senado | — | — |
| `f15e566579` | FAIL | art. 116.1 Reglamento del Senado | drops the rejection branch («si se rechazase, el Presidente podrá suspender la sesión para que la Ponencia proceda a la propuesta de un nuevo texto en el plazo que determine»), which the next sentence (db4ad1718b, «un nuevo texto en plazo») presupposes | Terminado el debate en la Comisión, el Presidente somete a votación la propuesta de Informe que en ese momento formule la Ponencia; si la Comisión lo aprueba, queda aprobado como Dictamen, y si lo rechaza, el Presidente puede suspender la sesión para que la Ponencia proponga un nuevo texto en el plazo que determine, que se somete a votación (art. 116.1 Reglamento del Senado). |
| `db4ad1718b` | FAIL | art. 116.2 Reglamento del Senado | drops the «salvo»: «a no ser que por el Presidente de la Comisión se decida otro orden»; also drops that the Dictamen is then formed by the enmiendas aprobadas | En caso de rechazo del Informe de la Ponencia o si la Ponencia no llega a un acuerdo sobre un nuevo texto en el plazo establecido, se someten a votación las enmiendas, agrupadas en función de la composición numérica de los Grupos autores, de menor a mayor, votándose en primer lugar las de Senadores individuales, a no ser que el Presidente de la Comisión decida otro orden, y el Dictamen de la Comisión lo constituyen las enmiendas aprobadas, que se elevan al Pleno (art. 116.2 Reglamento del Senado). |
| `8a5b9c2c41` | PASS | art. 116.3 Reglamento del Senado | — | — |

PASS 309 · FAIL 22
