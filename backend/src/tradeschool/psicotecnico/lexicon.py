# SPDX-License-Identifier: AGPL-3.0-only
"""The word banks of the verbal generators, each entry backed by a saved DLE page (`dle_relations.json`)."""

from __future__ import annotations

import json
from dataclasses import dataclass
from functools import cache
from importlib.resources import files
from typing import TypedDict

# word | level | synonyms | antonyms | part of speech of the whole entry (noun, adj, verb)
_ENTRIES = """
hereje|1|heterodoxo,disidente|ortodoxo|noun
erial|1|páramo,yermo,desierto,descampado|vergel|noun
ventura|1|fortuna,suerte,dicha|desdicha,desgracia,infortunio|noun
sibilino|2|enigmático,misterioso|claro|adj
acérrimo|2|tenaz,obstinado|moderado|adj
deslavazado|2|inconexo,deshilvanado,disperso,insulso|estructurado|adj
efímero|1|pasajero,momentáneo,fugaz,transitorio|duradero,perenne,eterno,permanente|adj
locuaz|1|hablador,charlatán,parlanchín|callado,taciturno,silencioso,reservado|adj
pródigo|2|derrochador,despilfarrador,malgastador|ahorrador,mezquino|adj
taciturno|2|callado,silencioso,reservado|hablador,locuaz,expansivo|adj
perenne|2|perpetuo,imperecedero,eterno|caduco,efímero|adj
ávido|2|ansioso,codicioso|desinteresado|adj
nefasto|1|funesto,aciago,desastroso|propicio,venturoso|adj
soslayar|2|eludir,esquivar,evitar|afrontar,encarar,enfrentar|verb
abstruso|2|incomprensible,enrevesado|claro,comprensible,sencillo|adj
tenue|1|fino,sutil,delgado,débil|grueso,intenso|adj
prolijo|2|extenso,dilatado,difuso|conciso,breve,sucinto|adj
exiguo|2|escaso,insuficiente,mínimo,reducido|abundante,copioso,cuantioso|adj
dilucidar|2|aclarar,esclarecer,explicar|embrollar,oscurecer,confundir|verb
abolir|1|derogar,suprimir,anular|instituir,implantar,establecer|verb
vetusto|1|antiguo,viejo,anticuado|moderno,nuevo,reciente|adj
frugal|2|sobrio,parco,moderado|glotón,excesivo|adj
perspicaz|1|agudo,sagaz,listo|torpe,obtuso,lerdo|adj
obstinado|1|terco,testarudo,tozudo,porfiado|dócil,flexible,transigente|adj
conciso|1|breve,sucinto,escueto,lacónico|extenso,prolijo|adj
austero|1|sobrio,riguroso,sencillo,ascético|lujoso,ostentoso|adj
lúcido|1|claro,sensato|confuso,ofuscado,obnubilado|adj
apacible|1|tranquilo,sereno,sosegado,plácido|agitado,tormentoso,turbulento|adj
contiguo|1|próximo,adyacente,colindante,vecino|alejado,distante,lejano|adj
insólito|1|raro,extraño,inusual,desacostumbrado|habitual,común,corriente,ordinario|adj
vehemente|2|apasionado,impetuoso,ardiente,fogoso|apático,flemático|adj
escarnio|2|burla,mofa,befa,irrisión|elogio,alabanza|noun
prohibir|1|vetar,vedar,impedir|permitir,autorizar,consentir,aprobar|verb
ameno|1|agradable,grato,entretenido|tedioso,aburrido,árido|adj
escasez|1|carencia,penuria,falta,insuficiencia|abundancia,riqueza,profusión|noun
honesto|1|honrado,íntegro,recto,decente|corrupto,tramposo,ruin|adj
veraz|1|sincero,franco,verídico|mentiroso,falso,embustero|adj
temerario|2|imprudente,osado,arriesgado|prudente,cauteloso,precavido|adj
mediocre|1|mediano,regular,anodino|excelente,sobresaliente|adj
escrupuloso|2|meticuloso,minucioso,esmerado|descuidado,negligente,chapucero|adj
atenuar|1|disminuir,mitigar,suavizar,aliviar|intensificar,agravar,acentuar|verb
prolífico|2|fecundo,fértil,productivo|estéril,infecundo,improductivo|adj
incipiente|2|naciente,inicial,embrionario||adj
recio|1|fuerte,robusto,vigoroso|débil,flojo,endeble,frágil|adj
diáfano|2|transparente,cristalino|opaco,turbio,borroso|adj
ostensible|2|patente,manifiesto,evidente|oculto,latente|adj
aludir|1|mencionar,citar,nombrar|omitir,callar,silenciar|verb
repudiar|2|rechazar,rehusar,desdeñar|aceptar,admitir,acoger|verb
"""

# word | level | definition (the DLE sense, verbatim) | sense number
_DEFINITIONS = """
alfaguara|2|Manantial copioso que surge con violencia.|1.
escisión|2|Desavenencia o riña entre algunas personas.|1.
nimio|1|Dicho generalmente de algo no material, insignificante, sin importancia.|1.
ubérrimo|3|Muy abundante y fértil.|1.
gárrulo|3|Dicho de una persona, muy habladora o charlatana.|1.b.
sempiterno|2|Que durará siempre; que, habiendo tenido principio, no tendrá fin.|1.
hontanar|3|Sitio en que nacen fuentes o manantiales.|1.
arcano|2|Dicho especialmente de una cosa, secreta, recóndita, reservada.|1.a.
ínclito|2|Ilustre, esclarecido, afamado.|1.
canícula|1|Período del año en que es más fuerte el calor.|1.a.
parsimonia|1|Lentitud y sosiego en el modo de hablar o de obrar; flema, frialdad de ánimo.|1.
cenit|1|Punto culminante o momento de apogeo de alguien o algo.|2.
proclive|1|Inclinado o propenso a algo, frecuentemente a lo malo.|1.
tesón|1|Decisión y perseverancia que se ponen en la ejecución de algo.|1.
letargo|1|Somnolencia, inactividad.|2.b.
pábulo|3|Aquello que sirve para mantener la existencia de algunas cosas o acciones.|2.
candor|1|Sinceridad, sencillez, ingenuidad y pureza del ánimo.|1.
acervo|2|Conjunto de valores o bienes culturales acumulados por tradición o herencia.|1.a.
mácula|2|Cosa que deslustra y desdora.|1.b.
dilación|1|Demora, tardanza o detención de algo por algún tiempo.|1.
perentorio|2|Urgente, apremiante.|2.
sinecura|3|Empleo o cargo retribuido que ocasiona poco o ningún trabajo.|1.
inefable|2|Que no se puede explicar con palabras.|1.
óbice|2|Obstáculo, embarazo, estorbo, impedimento.|1.
ardid|1|Artificio, medio empleado hábil y mañosamente para el logro de algún intento.|1.a.
baldío|1|Dicho de la tierra, que no está labrada ni adehesada.|2.a.
nómada|1|Que está en constante viaje o desplazamiento.|1.b.
cuantioso|1|Grande en cantidad o número.|1.
escrutinio|2|Reconocimiento y cómputo de los votos en las elecciones o en otro acto análogo.|2.
inquina|2|Aversión, mala voluntad.|1.
pesquisa|2|Información o indagación que se hace de algo para averiguar la realidad de ello o sus circunstancias.|1.
exiguo|1|Insuficiente, escaso.|1.
holgazán|1|Dicho de una persona, vagabunda y ociosa, que no quiere trabajar.|1.
colindante|1|Dicho de términos municipales o municipios, limítrofes entre sí.|1.c.
"""

# right | wrong (the wrong form is no DLE word or form, and breaks a rule of the Ortografía)
_SPELLING = """
exuberante|exhuberante
hortaliza|ortaliza
exhausto|exausto
exhibir|exibir
inhibir|inibir
prohibir|prohivir
prohibido|prohivido
rehén|rehen
atrás|atras
había|habia
también|tambien
escoger|escojer
coger|cojer
recoger|recojer
proteger|protejer
dirigir|dirijir
exigir|exijir
abogado|avogado
bienvenido|bienbenido
envolver|embolver
invertir|imvertir
inmediato|immediato
volver|bolver
ciudadanía|ciudadania
desarrollo|desarollo
excepción|excepsión
extranjero|estranjero
adolescente|adolecente
yacimiento|llacimiento
atención|atencion
examen|exámen
deshonesto|desonesto
zanahoria|zanaoria
búho|buho
alcohol|alcool
ahora|aora
cohete|coete
vergüenza|verguenza
pingüino|pinguino
lingüística|linguistica
antigüedad|antiguedad
cigüeña|cigueña
periódico|periodico
teléfono|telefono
ámbito|ambito
análisis|analisis
miércoles|miercoles
sábado|sabado
subvención|subbención
bóveda|boveda
hacer|aser
hacia|hasia
habilitar|abilitar
honorario|onorario
"""

# sentences with [right|wrong] slots; the plain words are spelt right
SENTENCES = (
    "Ayer [había|habia] que [exigir|exijir] a la [comisión|comision] el [desarrollo|desarollo] del [archivo|archibo] "
    "[también|tambien] en la oficina central.",
    "El médico del servicio [recogió|recojió] los expedientes, [revisó|rebisó] el [historial|istorial] y [exhibió|exibió] "
    "la [documentación|documentacion] ante el tribunal.",
    "Con [vergüenza|verguenza] y sin [atención|atencion] alguna, el [extranjero|estranjero] [volvió|bolvió] "
    "a la oficina para [reivindicar|reibindicar] su derecho.",
    "Se [prohibió|prohivió] aparcar cualquier vehículo en el [ámbito|ambito] del puerto, sin "
    "[excepción|excepsión], los [sábados|sabados] y los [miércoles|miercoles].",
)


# Pairs the DLE does not list but whose definitions coincide (synonyms) or negate each other (antonyms);
# the sense that decides it. Every other pair is in a DLE list, or an antonym of a word the DLE lists as synonym.
JUDGED_SYNONYMS: dict[tuple[str, str], str] = {
    ("hereje", "disidente"): "hereje 1.b. «Persona que disiente…»; disidente 1. «Que diside»",
    (
        "abstruso",
        "enrevesado",
    ): "abstruso 1. «De difícil comprensión»; enrevesado 1. «… que con dificultad se puede entender»",
    ("prolijo", "dilatado"): "prolijo 1. «Largo, dilatado con exceso»",
    ("lúcido", "claro"): "lúcido 1. «Claro en el razonamiento…»",
}
JUDGED_ANTONYMS: dict[tuple[str, str], str] = {
    (
        "acérrimo",
        "moderado",
    ): "acérrimo 3. «Intransigente, fanático, extremado»; moderado 1.c. «Que no es extremista»",
    ("pródigo", "mezquino"): "pródigo 2. «Muy dadivoso»; mezquino 1.a. «tacaño»",
    ("taciturno", "expansivo"): "taciturno 1. «Callado, silencioso…»; expansivo 2. «Franco, comunicativo»",
    (
        "perspicaz",
        "lerdo",
    ): "perspicaz 1.a. «agudo y penetrativo»; lerdo 1.a. «Tardo y torpe para comprender…»",
    (
        "obstinado",
        "dócil",
    ): "obstinado 1. «Que se obstina»; dócil 1.b. «… que recibe fácilmente la enseñanza»",
    ("lúcido", "ofuscado"): "lúcido 1. «Claro en el razonamiento»; ofuscar 1. «… confundir las ideas»",
    (
        "lúcido",
        "obnubilado",
    ): "lúcido 1. «Claro en el razonamiento»; obnubilar 1.a. «Ofuscar o confundir la razón…»",
    ("ameno", "tedioso"): "ameno 1.a. «Grato, placentero»; tedioso 1. «Que produce tedio»",
    (
        "mediocre",
        "excelente",
    ): "mediocre 1.a. «De poco mérito»; excelente 1. «Que sobresale por sus óptimas cualidades»",
    ("aludir", "silenciar"): "aludir 1. «Mencionar…»; silenciar 1. «Callar u omitir algo…»",
}
# Definitions close enough that one could pass for the other: never key and distractor of the same item.
NEAR_DEFINITIONS = (
    ("alfaguara", "hontanar"),
    ("exiguo", "nimio"),
    ("cuantioso", "ubérrimo"),
    ("dilación", "parsimonia"),
)


class DleSense(TypedDict):
    n: str
    category: str
    text: str
    syn: list[str]
    ant: list[str]


class DlePage(TypedDict):
    file: str
    absent: bool
    lemmas: list[str]
    senses: list[DleSense]


@cache
def dle_pages() -> dict[str, DlePage]:
    raw = files("tradeschool.psicotecnico").joinpath("dle_relations.json").read_text(encoding="utf-8")
    pages: dict[str, DlePage] = json.loads(raw)["pages"]
    return pages


def dle_list(word: str, kind: str) -> frozenset[str]:
    """The heads of every «Sinónimos y afines» (`syn`) or «Antónimos y opuestos» (`ant`) list of the word."""
    page = dle_pages().get(word.lower())
    if page is None:
        return frozenset()
    return frozenset(head for sense in page["senses"] for head in sense["syn" if kind == "syn" else "ant"])


def dle_related(a: str, b: str, kind: str) -> bool:
    a, b = a.lower(), b.lower()
    return b in dle_list(a, kind) or a in dle_list(b, kind)


_CATEGORIES = {"sustantivo": "noun", "adjetivo": "adj", "verbo": "verb"}


def part_of_speech(word: str) -> str:
    """A cluster word takes its entry's; a defined word, the DLE category of the cited sense."""
    for entry in entries():
        if word in (entry.word, *entry.synonyms, *entry.antonyms):
            return entry.part_of_speech
    for definition in definitions():
        if definition.word == word:
            sense = next(s for s in dle_pages()[word]["senses"] if s["n"] == definition.sense)
            return _CATEGORIES.get(sense["category"].split(" ")[0], sense["category"])
    raise KeyError(word)


def near_definitions(word: str) -> set[str]:
    return {other for pair in NEAR_DEFINITIONS if word in pair for other in pair if other != word}


@dataclass(frozen=True)
class Entry:
    word: str
    level: int
    synonyms: tuple[str, ...]
    antonyms: tuple[str, ...]
    part_of_speech: str


@dataclass(frozen=True)
class Definition:
    word: str
    level: int
    text: str
    sense: str


def _rows(raw: str) -> list[list[str]]:
    return [line.split("|") for line in raw.strip().splitlines()]


@cache
def entries() -> tuple[Entry, ...]:
    return tuple(
        Entry(w, int(level), tuple(syn.split(",")), tuple(ant.split(",")) if ant else (), pos)
        for w, level, syn, ant, pos in _rows(_ENTRIES)
    )


@cache
def definitions() -> tuple[Definition, ...]:
    return tuple(Definition(w, int(level), text, sense) for w, level, text, sense in _rows(_DEFINITIONS))


@cache
def spelling() -> tuple[tuple[str, str], ...]:
    return tuple((right, wrong) for right, wrong in _rows(_SPELLING))


@cache
def _clusters() -> dict[str, int]:
    parent: dict[str, str] = {}

    def find(word: str) -> str:
        parent.setdefault(word, word)
        while parent[word] != word:
            parent[word] = parent[parent[word]]
            word = parent[word]
        return word

    for entry in entries():
        for word in entry.synonyms:
            parent[find(word)] = find(entry.word)
    roots = {find(w): i for i, w in enumerate(sorted({find(w) for w in list(parent)}))}
    return {word: roots[find(word)] for word in list(parent)}


def cluster_of(word: str) -> int | None:
    return _clusters().get(word.lower())


def synonyms_of(word: str) -> set[str]:
    cluster = cluster_of(word)
    if cluster is None:
        return set()
    return {w for w, c in _clusters().items() if c == cluster and w != word.lower()}


def antonyms_of(word: str) -> set[str]:
    cluster = cluster_of(word)
    out: set[str] = set()
    for entry in entries():
        if cluster is not None and cluster_of(entry.word) == cluster:
            out.update(entry.antonyms)
        if word.lower() in entry.antonyms:
            out.update(synonyms_of(entry.word) | {entry.word})
    return out


@cache
def wrong_spellings() -> frozenset[str]:
    forms = {wrong for _, wrong in spelling()}
    for sentence in SENTENCES:
        forms.update(part.split("|")[1] for part in sentence.split("[")[1:] for part in [part.split("]")[0]])
    return frozenset(forms)


@cache
def right_spellings() -> frozenset[str]:
    forms = {right for right, _ in spelling()}
    for sentence in SENTENCES:
        forms.update(part.split("|")[0] for part in sentence.split("[")[1:] for part in [part.split("]")[0]])
    return frozenset(forms)
