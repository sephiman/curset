# Word banks against the DLE — blind review, step 1 (2026-11-07)

Banks: `backend/src/tradeschool/psicotecnico/lexicon.py` (48 synonym/antonym entries, 34 definitions, 54 spelling pairs, 4 sentences).

## Method

- Every word of the banks (stems, synonyms, antonyms, defined words, right and wrong spellings, the sentence slots) was looked up at `https://dle.rae.es/<palabra>` (24.ª edición). The page is fetched the way `check_pages.py` fetches first: a plain request with its User-Agent, 2 s apart. The Playwright Chromium gets Cloudflare's challenge page (HTTP 403) on dle.rae.es, so the plain request is the only one that works. 508 lookups, all HTTP 200.
- The 458 pages the banks cite are saved stripped under `content/age-auxiliar-c2/sources/otros/dle/` (originals in `~/PycharmProjects/curset-saved-originals/`), each with url, date and sha256 in `fuentes.yaml`.
- `backend/scripts/dle_relations.py` reads the saved pages into `psicotecnico/dle_relations.json`: for each page, whether the DLE has the word, plus each main sense with its number, text and «Sinónimos y afines» / «Antónimos y opuestos» lists (complex forms left out).
- `tests/test_psicotecnico_lexicon.py` checks every bank entry against that file:
  - a synonym is in a DLE list, or is one of the 4 judged pairs;
  - an antonym is in a DLE list for the word or for one of its listed synonyms, or is one of the 10 judged pairs;
  - a definition is the cited DLE sense verbatim;
  - a spelling pair's right form has an entry and its wrong form gets «no está en el Diccionario»;
  - the JSON is rebuilt from the pages.
- Rule applied, from the task: keep what the DLE marks as synonym/antonym or what the definitions show coinciding (or negating); remove anything borderline. A spelling pair is removed when the wrong form is also a DLE word or form (the DLE resolves conjugations: `medico` → `medicar`), or when it is a missing letter rather than a rule of the Ortografía.

## Removed or corrected entries, with the DLE citation

### Synonym clusters and antonyms

| Entry | Change | DLE citation |
|---|---|---|
| hereje | antonym «devoto» removed | devoto 1. «Dedicado con fervor a obras de piedad y religión» does not negate hereje 1.a; the DLE lists only «ortodoxo» |
| erial | antonym «huerta» removed | huerta 1.a/1.b (a kind of farmland); the DLE lists «vergel», not «huerta» |
| sibilino | antonyms «evidente», «diáfano» removed | sibilino 2. «Misterioso u oscuro…» has no antonym list; «claro» stays (enigmático 1.b) |
| acérrimo | antonyms «tibio», «indiferente» removed | not listed; «moderado» stays (acérrimo 3. «Intransigente, fanático, extremado» / moderado 1.c. «Que no es extremista») |
| deslavazado | synonyms «desvaído», «descolorido» and antonyms «intenso», «vistoso» removed; now inconexo, deshilvanado, disperso, insulso / estructurado | deslavazado 1. «Insustancial, insulso», 2. «Desordenado, mal compuesto o inconexo»: no colour sense; the new words are its 1. and 2. lists |
| pródigo | antonym «frugal» removed | frugal 1.a. «Parco en comer y beber» is not the opposite of pródigo 1.a/2 |
| ávido | synonym «voraz», antonym «saciado» removed | voraz 1.a/1.b are about eating; ávido 1. «Ansioso, codicioso»; «saciado» not listed |
| nefasto | synonym «perjudicial», antonyms «favorable», «benéfico» removed; «venturoso» added | nefasto 1.a/1.b lists: funesto, aciago, desastroso / propicio, venturoso |
| abstruso | synonym «recóndito» removed | recóndito 1. «Muy escondido, reservado y oculto» ≠ abstruso 1. «De difícil comprensión» |
| tenue | antonym «denso» removed | tenue 1. antonyms are «grueso», «intenso» |
| frugal | antonym «goloso» removed | goloso 1. «Aficionado a comer golosinas»; frugal's list has «glotón» |
| perspicaz | synonym «astuto» removed | astuto 1.a. «… hábil para engañar…» ≠ perspicaz 1.a. «agudo y penetrativo» |
| conciso | antonym «farragoso» removed | not listed (borderline) |
| austero | antonym «suntuoso» removed | not listed; «lujoso», «ostentoso» are |
| lúcido | synonyms «despejado», «razonable» removed | not listed; despejado 2.a. and razonable 1.a. only touch lúcido 1. (borderline) |
| vehemente | antonym «sosegado» removed | not listed; «apático», «flemático» are |
| escarnio | antonym «respeto» removed | not listed; «elogio», «alabanza» are |
| mediocre | antonym «extraordinario» removed | extraordinario 1.a. «Fuera del orden… común» is not the opposite of mediocre 1.a |
| incipiente | antonyms «consumado», «avanzado», «maduro» removed; no antonym left (the DLE lists none), so the word only appears in synonym items | incipiente 1. «Que empieza»; consumado 1., avanzado 1. and maduro 1.a–1.d do not negate it |
| recio | synonym «resistente» removed | not listed; recio 1.a. «Fuerte, robusto, vigoroso» |
| diáfano | synonym «translúcido» removed | translúcido 1. «… pero que no deja ver nítidamente los objetos» contradicts diáfano 1. |
| ostensible | antonym «disimulado» removed | disimulado 1.a. is about a person who hides what they feel |

### Definitions (36 → 34)

Every definition now quotes the DLE sense verbatim (the exams use the DLE's wording).

- **Removed:** «recelo» (DLE: «Acción y efecto de recelar») and «vetar» («Poner el veto a…»). Both definitions give the word away.
- **Kept as they were** (already the DLE's text): alfaguara 1., ubérrimo 1., inefable 1., cuantioso 1., exiguo 1.
- **Corrected:**

| Word | Before (mine) | Now (DLE, acepción) |
|---|---|---|
| escisión | Rompimiento, rotura o separación. | 1. Desavenencia o riña entre algunas personas. |
| nimio | Insignificante, sin importancia. | 1. Dicho generalmente de algo no material, insignificante, sin importancia. |
| gárrulo | Muy hablador. | 1.b. Dicho de una persona, muy habladora o charlatana. |
| sempiterno | Que durará siempre. | 1. Que durará siempre; que, habiendo tenido principio, no tendrá fin. |
| hontanar | Sitio en que nacen fuentes. | 1. Sitio en que nacen fuentes o manantiales. |
| arcano | Secreto, recóndito, reservado. | 1.a. Dicho especialmente de una cosa, secreta, recóndita, reservada. |
| ínclito | Ilustre, esclarecido, insigne. | 1. Ilustre, esclarecido, afamado. |
| canícula | Período del año en que más aprieta el calor. | 1.a. Período del año en que es más fuerte el calor. |
| parsimonia | Lentitud y sosiego en el modo de obrar. | 1. Lentitud y sosiego en el modo de hablar o de obrar; flema, frialdad de ánimo. |
| cenit | Punto más alto al que llega algo. | 2. Punto culminante o momento de apogeo de alguien o algo. |
| proclive | Inclinado o propenso a algo. | 1. Inclinado o propenso a algo, frecuentemente a lo malo. |
| tesón | Firmeza, perseverancia y constancia. | 1. Decisión y perseverancia que se ponen en la ejecución de algo. |
| letargo | Estado de somnolencia profunda y prolongada. | 2.b. Somnolencia, inactividad. |
| pábulo | Alimento o sustento de algo. | 2. Aquello que sirve para mantener la existencia de algunas cosas o acciones. |
| candor | Sinceridad y sencillez del ánimo. | 1. Sinceridad, sencillez, ingenuidad y pureza del ánimo. |
| acervo | Conjunto de bienes morales o culturales acumulados por tradición o herencia. | 1.a. Conjunto de valores o bienes culturales acumulados por tradición o herencia. |
| mácula | Mancha. | 1.b. Cosa que deslustra y desdora. |
| dilación | Demora o tardanza en hacer algo. | 1. Demora, tardanza o detención de algo por algún tiempo. |
| sinecura | Empleo bien retribuido que da poco trabajo. | 1. Empleo o cargo retribuido que ocasiona poco o ningún trabajo. |
| óbice | Obstáculo o impedimento. | 1. Obstáculo, embarazo, estorbo, impedimento. |
| ardid | Artificio hábil para conseguir un propósito. | 1.a. Artificio, medio empleado hábil y mañosamente para el logro de algún intento. |
| baldío | Dicho de una tierra: que no se cultiva. | 2.a. Dicho de la tierra, que no está labrada ni adehesada. |
| nómada | Que va de un lugar a otro sin domicilio fijo. | 1.b. Que está en constante viaje o desplazamiento. |
| escrutinio | Recuento de los votos en una elección. | 2. Reconocimiento y cómputo de los votos en las elecciones o en otro acto análogo. |
| inquina | Aversión o mala voluntad hacia alguien. | 1. Aversión, mala voluntad. |
| pesquisa | Investigación para averiguar algo. | 1. Información o indagación que se hace de algo para averiguar la realidad de ello o sus circunstancias. |
| holgazán | Que rehúye el trabajo y es perezoso. | 1. Dicho de una persona, vagabunda y ociosa, que no quiere trabajar. |
| colindante | Dicho de un terreno: que linda con otro. | 1.c. Dicho de términos municipales o municipios, limítrofes entre sí. |

The definition items never put these pairs together as key and distractor, since one could pass for the other: alfaguara/hontanar, exiguo/nimio, cuantioso/ubérrimo, dilación/parsimonia (`lexicon.NEAR_DEFINITIONS`).

### Spelling pairs (62 → 54) and sentences

| Pair removed | Why (DLE) |
|---|---|
| médico / medico | `dle.rae.es/medico` → «medicar»: «medico» is a form of the verb |
| tráfico / trafico | → «traficar» |
| sílaba / silaba | → «silabar» |
| vehículo / vehiculo | → «vehicular» |
| conmigo / comigo | «comigo» has its own DLE entry |
| administración / adminitración | a missing letter, not an orthographic rule |
| dificultad / dificutad | a missing letter |
| obvio / obbio | «bb» breaks no b/v rule; a typo |

Sentences:

- Sentence 1 loses «oficna» (a typo).
- Sentence 2 loses «espedientes» (`dle.rae.es/espedientes` resolves to «espedirse») and «medico» (a DLE form). It gains «[revisó|rebisó]» and «[historial|istorial]»; both wrong forms are absent from the DLE.
- Sentence 4 («Se prohibió el vehículo en el ámbito del periódico por una excepción inmediata») made no sense. It now reads «Se prohibió aparcar cualquier vehículo en el ámbito del puerto, sin excepción, los sábados y los miércoles», with slots prohibió, ámbito, excepción, sábados, miércoles. «vehiculo» is no longer a slot because it is a DLE form.

## Generator changes that come from the DLE check

- **verbal-sinonimos:** a distractor is never a word the DLE lists as a synonym of the stem or of one of its synonyms. 21 stems had such collisions with other clusters, e.g. PRÓDIGO/«fecundo», «fértil» (pródigo 3.); ACÉRRIMO/«fuerte», «vigoroso» (acérrimo 2.); LÚCIDO/«agudo», «sagaz», «sutil» (lúcido 1.); EFÍMERO/«breve» (efímero 1.a.). `check_extra` enforces it, so the load-time property tests reject any such item.
- **verbal-antonimos:** no distractor may be a DLE antonym of the stem (`check_extra`); stems without antonyms are skipped.
- **verbal-definicion:** `NEAR_DEFINITIONS` are never key and distractor together.
- **verbal-ortografia:** the word items deal from every other pair, so distractors of the key's length are available (the length-edge guard failed after the bank shrank).

## Changes after the first blind read of the verbal pages

- **Part of speech.**
  - Each synonym entry now carries one (`noun`, `adj`, `verb`), and synonym distractors come only from entries with the same one. Pass 1 found items where the grammar alone left only the key (verbal-sinonimos G2).
  - Defined words take the category of their cited DLE sense: `dle_relations.py` now records the title of the sense's category abbreviation, e.g. «sustantivo femenino». Word-for-definition items deal only words of that category (verbal-definicion G1).
- **Definition levels.** The course declares levels 1/2/3 (5/5/2, as in the index), but the bank had only levels 1 and 2. Level-3 items therefore borrowed level-2 words, and pass 1 saw the same word at two levels (verbal-definicion G2). Following the index («nivel 3 para palabras raras»), pábulo, hontanar, gárrulo, ubérrimo and sinecura are now level 3, and every item takes a word of exactly its own level.
- **Whole-cluster exclusion.** A synonym distractor is now excluded when the DLE ties any word of its cluster to the stem, not only the word itself. Pass 3 found TENUE dealt «Sobrio»: tenue 3. lists «sencillo», which shares the AUSTERO cluster with «sobrio», and sobrio 1.b. «Que carece de adornos superfluos» matches tenue 3.
- **No elimination by meaning.** At most two antonyms among the wrong options, and the other distractors come from distinct clusters, none of them an antonym's cluster. Pass 2 found «Mofa, Irrisión, Befa» for ERIAL and «Consentir, Autorizar, Aprobar» for PROHIBIR.
- **Ordering word list** (administrativo-ordenacion, not a DLE bank): «consiste», a conjugated form, is replaced by «consistorio», a headword (pass 2, B1).

## Citas por entrada

Each citation is `palabra acepción` on the saved page `content/age-auxiliar-c2/sources/otros/dle/<palabra>.html`, whose «Sinónimos y afines» or «Antónimos y opuestos» list contains the other word. «vía X» marks an antonym of a listed synonym; «definiciones» marks a pair the DLE does not list, decided by the senses cited. `tests/test_psicotecnico_lexicon.py` checks every pair against `dle_relations.json`.

### Sinónimos y antónimos (48 entradas)

| Palabra | Nivel | Categoría | Sinónimos (cita) | Antónimos (cita) |
|---|---|---|---|---|
| hereje | 1 | noun | heterodoxo (hereje 1.a.); disidente (definiciones: hereje 1.b. «Persona que disiente…»; disidente 1. «Que diside») | ortodoxo (hereje 1.a.) |
| erial | 1 | noun | páramo (erial 1.); yermo (erial 1.); desierto (erial 1.); descampado (erial 1.) | vergel (erial 1.) |
| ventura | 1 | noun | fortuna (ventura 2.a.); suerte (suerte 1.b.); dicha (ventura 1.) | desdicha (ventura 1.); desgracia (ventura 1.); infortunio (vía fortuna: fortuna 1.c.) |
| sibilino | 2 | adj | enigmático (sibilino 2.); misterioso (sibilino 2.) | claro (vía enigmático: enigmático 1.b.) |
| acérrimo | 2 | adj | tenaz (acérrimo 2.); obstinado (acérrimo 2.) | moderado (definiciones: acérrimo 3. «Intransigente, fanático, extremado»; moderado 1.c. «Que no es extremista») |
| deslavazado | 2 | adj | inconexo (deslavazado 2.); deshilvanado (deslavazado 2.); disperso (deslavazado 2.); insulso (deslavazado 1.) | estructurado (deslavazado 2.) |
| efímero | 1 | adj | pasajero (efímero 1.a.); momentáneo (efímero 1.a.); fugaz (efímero 1.a.); transitorio (efímero 1.a.) | duradero (efímero 1.a.); perenne (vía pasajero: perenne 1.); eterno (efímero 1.a.); permanente (vía pasajero: pasajero 2.) |
| locuaz | 1 | adj | hablador (locuaz 1.); charlatán (locuaz 1.); parlanchín (locuaz 1.) | callado (locuaz 1.); taciturno (taciturno 1.); silencioso (locuaz 1.); reservado (vía hablador: reservado 1.a.) |
| pródigo | 2 | adj | derrochador (pródigo 1.a.); despilfarrador (pródigo 1.a.); malgastador (pródigo 1.a.) | ahorrador (pródigo 1.a.); mezquino (definiciones: pródigo 2. «Muy dadivoso»; mezquino 1.a. «tacaño») |
| taciturno | 2 | adj | callado (taciturno 1.); silencioso (taciturno 1.); reservado (taciturno 1.) | hablador (vía callado: callado 1.a.); locuaz (taciturno 1.); expansivo (definiciones: taciturno 1. «Callado, silencioso…»; expansivo 2. «Franco, comunicativo») |
| perenne | 2 | adj | perpetuo (perenne 1.); imperecedero (perenne 1.); eterno (perenne 1.) | caduco (perenne 2.); efímero (vía perpetuo: perpetuo 1.) |
| ávido | 2 | adj | ansioso (ávido 1.); codicioso (ávido 1.) | desinteresado (vía codicioso: codicioso 1.) |
| nefasto | 1 | adj | funesto (nefasto 1.a.); aciago (nefasto 1.a.); desastroso (nefasto 1.b.) | propicio (nefasto 1.a.); venturoso (nefasto 1.a./1.b.) |
| soslayar | 2 | verb | eludir (soslayar 1.); esquivar (soslayar 1.); evitar (soslayar 1.) | afrontar (soslayar 1.); encarar (vía eludir: encarar 2.); enfrentar (vía eludir: enfrentar 2.a.) |
| abstruso | 2 | adj | incomprensible (abstruso 1.); enrevesado (definiciones: abstruso 1. «De difícil comprensión»; enrevesado 1. «… que con dificultad se puede entender») | claro (abstruso 1.); comprensible (abstruso 1.); sencillo (vía enrevesado: enrevesado 1.) |
| tenue | 1 | adj | fino (tenue 1.); sutil (tenue 1.); delgado (tenue 1.); débil (tenue 1.) | grueso (tenue 1.); intenso (tenue 1.) |
| prolijo | 2 | adj | extenso (prolijo 1.); dilatado (definiciones: prolijo 1. «Largo, dilatado con exceso»); difuso (prolijo 3.) | conciso (conciso 1.); breve (vía extenso: extenso 1.a.); sucinto (prolijo 1.) |
| exiguo | 2 | adj | escaso (exiguo 1.); insuficiente (exiguo 1.); mínimo (exiguo 1.); reducido (exiguo 1.) | abundante (exiguo 1.); copioso (vía escaso: escaso 1.a.); cuantioso (exiguo 1.) |
| dilucidar | 2 | verb | aclarar (dilucidar 1.); esclarecer (dilucidar 1.); explicar (explicar 1.b.) | embrollar (vía aclarar: embrollar 1.); oscurecer (dilucidar 1.); confundir (vía esclarecer: esclarecer 1.b.) |
| abolir | 1 | verb | derogar (abolir 1.); suprimir (abolir 1.); anular (abolir 1.) | instituir (instituir 1.a./1.b.); implantar (abolir 1.); establecer (vía suprimir: establecer 1.) |
| vetusto | 1 | adj | antiguo (vetusto 1.); viejo (vetusto 1.); anticuado (vetusto 1.) | moderno (vetusto 1.); nuevo (vetusto 1.); reciente (vía antiguo: antiguo 1.a./1.b.) |
| frugal | 2 | adj | sobrio (frugal 1.a./1.b.); parco (frugal 1.a./1.b.); moderado (frugal 1.a./1.b.) | glotón (frugal 1.a.); excesivo (vía sobrio: sobrio 1.a.) |
| perspicaz | 1 | adj | agudo (perspicaz 1.b.); sagaz (perspicaz 1.b.); listo (perspicaz 1.b.) | torpe (perspicaz 1.b.); obtuso (perspicaz 1.b.); lerdo (definiciones: perspicaz 1.a. «agudo y penetrativo»; lerdo 1.a. «Tardo y torpe para comprender…») |
| obstinado | 1 | adj | terco (obstinado 1.); testarudo (obstinado 1.); tozudo (obstinado 1.); porfiado (obstinado 1.) | dócil (definiciones: obstinado 1. «Que se obstina»; dócil 1.b. «… que recibe fácilmente la enseñanza»); flexible (obstinado 1.); transigente (obstinado 1.) |
| conciso | 1 | adj | breve (conciso 1.); sucinto (conciso 1.); escueto (conciso 1.); lacónico (conciso 1.) | extenso (conciso 1.); prolijo (conciso 1.) |
| austero | 1 | adj | sobrio (austero 2.); riguroso (austero 1.); sencillo (sencillo 4.a./4.b.); ascético (ascético 2.) | lujoso (austero 2.); ostentoso (austero 2.) |
| lúcido | 1 | adj | claro (definiciones: lúcido 1. «Claro en el razonamiento…»); sensato (lúcido 1.) | confuso (vía claro: claro 6.a./6.b.); ofuscado (definiciones: lúcido 1. «Claro en el razonamiento»; ofuscar 1. «… confundir las ideas»); obnubilado (definiciones: lúcido 1. «Claro en el razonamiento»; obnubilar 1.a. «Ofuscar o confundir la razón…») |
| apacible | 1 | adj | tranquilo (apacible 1.a./1.b.); sereno (apacible 1.b.); sosegado (apacible 1.a.); plácido (apacible 1.a.) | agitado (vía tranquilo: agitado 2.); tormentoso (tormentoso 1.b.); turbulento (vía tranquilo: turbulento 2.a./2.b.) |
| contiguo | 1 | adj | próximo (contiguo 1.); adyacente (contiguo 1.); colindante (contiguo 1.); vecino (contiguo 1.) | alejado (vía próximo: alejado 1.); distante (vía próximo: distante 1.b.); lejano (contiguo 1.) |
| insólito | 1 | adj | raro (insólito 1.); extraño (insólito 1.); inusual (insólito 1.); desacostumbrado (insólito 1.) | habitual (habitual 1.a./1.b.); común (vía extraño: extraño 2.a.); corriente (insólito 1.); ordinario (ordinario 1.a.) |
| vehemente | 2 | adj | apasionado (vehemente 1.b.); impetuoso (vehemente 1.a.); ardiente (vehemente 1.b.); fogoso (vehemente 1.b.) | apático (vía apasionado: apático 1.a./1.b.); flemático (vía fogoso: fogoso 1.) |
| escarnio | 2 | noun | burla (escarnio 1.); mofa (escarnio 1.); befa (escarnio 1.); irrisión (irrisión 1.a.) | elogio (escarnio 1.); alabanza (escarnio 1.) |
| prohibir | 1 | verb | vetar (prohibir 1.); vedar (prohibir 1.); impedir (prohibir 1.) | permitir (prohibir 1.); autorizar (autorizar 1.b.); consentir (consentir 1.a.); aprobar (vía vetar: vetar 1.) |
| ameno | 1 | adj | agradable (ameno 1.a.); grato (ameno 1.b.); entretenido (ameno 1.a.) | tedioso (definiciones: ameno 1.a. «Grato, placentero»; tedioso 1. «Que produce tedio»); aburrido (ameno 1.a.); árido (árido 2.) |
| escasez | 1 | noun | carencia (escasez 1.a.); penuria (escasez 1.b.); falta (falta 1.a./1.b.); insuficiencia (escasez 1.a.) | abundancia (escasez 1.a./1.b.); riqueza (escasez 1.a./1.b.); profusión (profusión 1.a./1.b.) |
| honesto | 1 | adj | honrado (honesto 1.a.); íntegro (honesto 1.a.); recto (honesto 1.a.); decente (honesto 1.a./2.a.) | corrupto (vía honrado: honrado 1.a.); tramposo (vía honrado: tramposo 1.b.); ruin (vía honrado: ruin 1.a.) |
| veraz | 1 | adj | sincero (veraz 1.a.); franco (veraz 1.a.); verídico (veraz 1.a.) | mentiroso (veraz 1.a.); falso (veraz 1.a.); embustero (veraz 1.a.) |
| temerario | 2 | adj | imprudente (temerario 1.a./1.b.); osado (temerario 1.a./1.b.); arriesgado (temerario 1.a./1.b.) | prudente (temerario 1.a./1.b.); cauteloso (vía imprudente: imprudente 1.); precavido (vía imprudente: imprudente 1.) |
| mediocre | 1 | adj | mediano (mediocre 1.b.); regular (mediocre 1.b.); anodino (mediocre 1.b.) | excelente (definiciones: mediocre 1.a. «De poco mérito»; excelente 1. «Que sobresale por sus óptimas cualidades»); sobresaliente (mediocre 1.a./1.b.) |
| escrupuloso | 2 | adj | meticuloso (escrupuloso 1.a.); minucioso (escrupuloso 1.a.); esmerado (escrupuloso 1.a.) | descuidado (escrupuloso 1.a.); negligente (escrupuloso 1.a.); chapucero (escrupuloso 1.a.) |
| atenuar | 1 | verb | disminuir (atenuar 1.a.); mitigar (atenuar 1.a.); suavizar (suavizar 1.); aliviar (atenuar 1.a.) | intensificar (intensificar 1.); agravar (atenuar 1.a.); acentuar (atenuar 1.a.) |
| prolífico | 2 | adj | fecundo (prolífico 1.); fértil (prolífico 1.); productivo (prolífico 2.) | estéril (prolífico 1.); infecundo (prolífico 1.); improductivo (prolífico 2.) |
| incipiente | 2 | adj | naciente (incipiente 1.); inicial (incipiente 1.); embrionario (incipiente 1.) | — |
| recio | 1 | adj | fuerte (recio 1.a.); robusto (recio 1.a.); vigoroso (recio 1.a.) | débil (recio 1.a.); flojo (vía fuerte: fuerte 1.e.); endeble (recio 1.a.); frágil (vía fuerte: fuerte 2.a.) |
| diáfano | 2 | adj | transparente (diáfano 1./2.); cristalino (diáfano 2.) | opaco (diáfano 1.); turbio (vía transparente: turbio 1.a.); borroso (borroso 1.a.) |
| ostensible | 2 | adj | patente (ostensible 1.b.); manifiesto (ostensible 1.b.); evidente (ostensible 1.b.) | oculto (vía patente: patente 1.a./1.b.); latente (vía patente: patente 1.a./1.b.) |
| aludir | 1 | verb | mencionar (aludir 1.); citar (aludir 1.); nombrar (nombrar 1.a.) | omitir (aludir 1.); callar (vía mencionar: callar 1.c.); silenciar (definiciones: aludir 1. «Mencionar…»; silenciar 1. «Callar u omitir algo…») |
| repudiar | 2 | verb | rechazar (repudiar 1.a.); rehusar (rehusar 1.); desdeñar (repudiar 1.a.) | aceptar (repudiar 1.a.); admitir (vía rechazar: admitir 1./3.); acoger (vía rechazar: acoger 1.b.) |

### Definiciones (34)

| Palabra | Nivel | Acepción del DLE | Categoría | Texto (literal) |
|---|---|---|---|---|
| alfaguara | 2 | alfaguara 1. | sustantivo femenino | Manantial copioso que surge con violencia. |
| escisión | 2 | escisión 1. | sustantivo femenino | Desavenencia o riña entre algunas personas. |
| nimio | 1 | nimio 1. | adjetivo | Dicho generalmente de algo no material, insignificante, sin importancia. |
| ubérrimo | 3 | ubérrimo 1. | adjetivo | Muy abundante y fértil. |
| gárrulo | 3 | gárrulo 1.b. | adjetivo | Dicho de una persona, muy habladora o charlatana. |
| sempiterno | 2 | sempiterno 1. | adjetivo | Que durará siempre; que, habiendo tenido principio, no tendrá fin. |
| hontanar | 3 | hontanar 1. | sustantivo masculino | Sitio en que nacen fuentes o manantiales. |
| arcano | 2 | arcano 1.a. | adjetivo | Dicho especialmente de una cosa, secreta, recóndita, reservada. |
| ínclito | 2 | ínclito 1. | adjetivo | Ilustre, esclarecido, afamado. |
| canícula | 1 | canícula 1.a. | sustantivo femenino | Período del año en que es más fuerte el calor. |
| parsimonia | 1 | parsimonia 1. | sustantivo femenino | Lentitud y sosiego en el modo de hablar o de obrar; flema, frialdad de ánimo. |
| cenit | 1 | cenit 2. | sustantivo masculino | Punto culminante o momento de apogeo de alguien o algo. |
| proclive | 1 | proclive 1. | adjetivo | Inclinado o propenso a algo, frecuentemente a lo malo. |
| tesón | 1 | tesón 1. | sustantivo masculino | Decisión y perseverancia que se ponen en la ejecución de algo. |
| letargo | 1 | letargo 2.b. | sustantivo masculino | Somnolencia, inactividad. |
| pábulo | 3 | pábulo 2. | sustantivo masculino | Aquello que sirve para mantener la existencia de algunas cosas o acciones. |
| candor | 1 | candor 1. | sustantivo masculino | Sinceridad, sencillez, ingenuidad y pureza del ánimo. |
| acervo | 2 | acervo 1.a. | sustantivo masculino | Conjunto de valores o bienes culturales acumulados por tradición o herencia. |
| mácula | 2 | mácula 1.b. | sustantivo femenino | Cosa que deslustra y desdora. |
| dilación | 1 | dilación 1. | sustantivo femenino | Demora, tardanza o detención de algo por algún tiempo. |
| perentorio | 2 | perentorio 2. | adjetivo | Urgente, apremiante. |
| sinecura | 3 | sinecura 1. | sustantivo femenino | Empleo o cargo retribuido que ocasiona poco o ningún trabajo. |
| inefable | 2 | inefable 1. | adjetivo | Que no se puede explicar con palabras. |
| óbice | 2 | óbice 1. | sustantivo masculino | Obstáculo, embarazo, estorbo, impedimento. |
| ardid | 1 | ardid 1.a. | sustantivo masculino | Artificio, medio empleado hábil y mañosamente para el logro de algún intento. |
| baldío | 1 | baldío 2.a. | adjetivo | Dicho de la tierra, que no está labrada ni adehesada. |
| nómada | 1 | nómada 1.b. | adjetivo | Que está en constante viaje o desplazamiento. |
| cuantioso | 1 | cuantioso 1. | adjetivo | Grande en cantidad o número. |
| escrutinio | 2 | escrutinio 2. | sustantivo masculino | Reconocimiento y cómputo de los votos en las elecciones o en otro acto análogo. |
| inquina | 2 | inquina 1. | sustantivo femenino | Aversión, mala voluntad. |
| pesquisa | 2 | pesquisa 1. | sustantivo femenino | Información o indagación que se hace de algo para averiguar la realidad de ello o sus circunstancias. |
| exiguo | 1 | exiguo 1. | adjetivo | Insuficiente, escaso. |
| holgazán | 1 | holgazán 1. | adjetivo | Dicho de una persona, vagabunda y ociosa, que no quiere trabajar. |
| colindante | 1 | colindante 1.c. | adjetivo | Dicho de términos municipales o municipios, limítrofes entre sí. |

### Ortografía (54 pares)

| Correcta (página, artículo) | Errónea (página: «no está en el Diccionario») |
|---|---|
| exuberante (dle/exuberante.html, «exuberante») | exhuberante (dle/exhuberante.html) |
| hortaliza (dle/hortaliza.html, «hortaliza») | ortaliza (dle/ortaliza.html) |
| exhausto (dle/exhausto.html, «exhausto, exhausta») | exausto (dle/exausto.html) |
| exhibir (dle/exhibir.html, «exhibir») | exibir (dle/exibir.html) |
| inhibir (dle/inhibir.html, «inhibir») | inibir (dle/inibir.html) |
| prohibir (dle/prohibir.html, «prohibir») | prohivir (dle/prohivir.html) |
| prohibido (dle/prohibido.html, «prohibido, prohibida») | prohivido (dle/prohivido.html) |
| rehén (dle/rehén.html, «rehén») | rehen (dle/rehen.html) |
| atrás (dle/atrás.html, «atrás») | atras (dle/atras.html) |
| había (dle/había.html, «haber1») | habia (dle/habia.html) |
| también (dle/también.html, «también») | tambien (dle/tambien.html) |
| escoger (dle/escoger.html, «escoger») | escojer (dle/escojer.html) |
| coger (dle/coger.html, «coger») | cojer (dle/cojer.html) |
| recoger (dle/recoger.html, «recoger») | recojer (dle/recojer.html) |
| proteger (dle/proteger.html, «proteger») | protejer (dle/protejer.html) |
| dirigir (dle/dirigir.html, «dirigir») | dirijir (dle/dirijir.html) |
| exigir (dle/exigir.html, «exigir») | exijir (dle/exijir.html) |
| abogado (dle/abogado.html, «abogado, abogada») | avogado (dle/avogado.html) |
| bienvenido (dle/bienvenido.html, «bienvenido, bienvenida») | bienbenido (dle/bienbenido.html) |
| envolver (dle/envolver.html, «envolver») | embolver (dle/embolver.html) |
| invertir (dle/invertir.html, «invertir») | imvertir (dle/imvertir.html) |
| inmediato (dle/inmediato.html, «inmediato, inmediata») | immediato (dle/immediato.html) |
| volver (dle/volver.html, «volver») | bolver (dle/bolver.html) |
| ciudadanía (dle/ciudadanía.html, «ciudadanía») | ciudadania (dle/ciudadania.html) |
| desarrollo (dle/desarrollo.html, «desarrollo») | desarollo (dle/desarollo.html) |
| excepción (dle/excepción.html, «excepción») | excepsión (dle/excepsión.html) |
| extranjero (dle/extranjero.html, «extranjero, extranjera») | estranjero (dle/estranjero.html) |
| adolescente (dle/adolescente.html, «adolescente») | adolecente (dle/adolecente.html) |
| yacimiento (dle/yacimiento.html, «yacimiento») | llacimiento (dle/llacimiento.html) |
| atención (dle/atención.html, «atención») | atencion (dle/atencion.html) |
| examen (dle/examen.html, «examen») | exámen (dle/exámen.html) |
| deshonesto (dle/deshonesto.html, «deshonesto, deshonesta») | desonesto (dle/desonesto.html) |
| zanahoria (dle/zanahoria.html, «zanahoria») | zanaoria (dle/zanaoria.html) |
| búho (dle/búho.html, «búho») | buho (dle/buho.html) |
| alcohol (dle/alcohol.html, «alcohol») | alcool (dle/alcool.html) |
| ahora (dle/ahora.html, «ahora») | aora (dle/aora.html) |
| cohete (dle/cohete.html, «cohete») | coete (dle/coete.html) |
| vergüenza (dle/vergüenza.html, «vergüenza») | verguenza (dle/verguenza.html) |
| pingüino (dle/pingüino.html, «pingüino») | pinguino (dle/pinguino.html) |
| lingüística (dle/lingüística.html, «lingüístico, lingüística») | linguistica (dle/linguistica.html) |
| antigüedad (dle/antigüedad.html, «antigüedad») | antiguedad (dle/antiguedad.html) |
| cigüeña (dle/cigüeña.html, «cigüeña») | cigueña (dle/cigueña.html) |
| periódico (dle/periódico.html, «periódico, periódica») | periodico (dle/periodico.html) |
| teléfono (dle/teléfono.html, «teléfono») | telefono (dle/telefono.html) |
| ámbito (dle/ámbito.html, «ámbito») | ambito (dle/ambito.html) |
| análisis (dle/análisis.html, «análisis») | analisis (dle/analisis.html) |
| miércoles (dle/miércoles.html, «miércoles») | miercoles (dle/miercoles.html) |
| sábado (dle/sábado.html, «sábado») | sabado (dle/sabado.html) |
| subvención (dle/subvención.html, «subvención») | subbención (dle/subbención.html) |
| bóveda (dle/bóveda.html, «bóveda») | boveda (dle/boveda.html) |
| hacer (dle/hacer.html, «hacer») | aser (dle/aser.html) |
| hacia (dle/hacia.html, «hacia») | hasia (dle/hasia.html) |
| habilitar (dle/habilitar.html, «habilitar») | abilitar (dle/abilitar.html) |
| honorario (dle/honorario.html, «honorario, honoraria») | onorario (dle/onorario.html) |
