# SPDX-License-Identifier: AGPL-3.0-only
"""The word banks of the verbal generators; synonym clusters keep a distractor from being a synonym."""

from __future__ import annotations

from dataclasses import dataclass
from functools import cache

# word | level | synonyms | antonyms
_ENTRIES = """
hereje|1|heterodoxo,disidente|ortodoxo,devoto
erial|1|páramo,yermo,desierto,descampado|vergel,huerta
ventura|1|fortuna,suerte,dicha|desdicha,desgracia,infortunio
sibilino|2|enigmático,misterioso|claro,evidente,diáfano
acérrimo|2|tenaz,obstinado|tibio,moderado,indiferente
deslavazado|2|desvaído,descolorido|intenso,vistoso
efímero|1|pasajero,momentáneo,fugaz,transitorio|duradero,perenne,eterno,permanente
locuaz|1|hablador,charlatán,parlanchín|callado,taciturno,silencioso,reservado
pródigo|2|derrochador,despilfarrador,malgastador|ahorrador,frugal,mezquino
taciturno|2|callado,silencioso,reservado|hablador,locuaz,expansivo
perenne|2|perpetuo,imperecedero,eterno|caduco,efímero
ávido|2|ansioso,codicioso,voraz|saciado,desinteresado
nefasto|1|funesto,aciago,desastroso,perjudicial|benéfico,propicio,favorable
soslayar|2|eludir,esquivar,evitar|afrontar,encarar,enfrentar
abstruso|2|incomprensible,enrevesado,recóndito|claro,comprensible,sencillo
tenue|1|fino,sutil,delgado,débil|grueso,intenso,denso
prolijo|2|extenso,dilatado,difuso|conciso,breve,sucinto
exiguo|2|escaso,insuficiente,mínimo,reducido|abundante,copioso,cuantioso
dilucidar|2|aclarar,esclarecer,explicar|embrollar,oscurecer,confundir
abolir|1|derogar,suprimir,anular|instituir,implantar,establecer
vetusto|1|antiguo,viejo,anticuado|moderno,nuevo,reciente
frugal|2|sobrio,parco,moderado|glotón,goloso,excesivo
perspicaz|1|agudo,sagaz,astuto,listo|torpe,obtuso,lerdo
obstinado|1|terco,testarudo,tozudo,porfiado|dócil,flexible,transigente
conciso|1|breve,sucinto,escueto,lacónico|extenso,prolijo,farragoso
austero|1|sobrio,riguroso,sencillo,ascético|lujoso,suntuoso,ostentoso
lúcido|1|claro,despejado,razonable,sensato|confuso,ofuscado,obnubilado
apacible|1|tranquilo,sereno,sosegado,plácido|agitado,tormentoso,turbulento
contiguo|1|próximo,adyacente,colindante,vecino|alejado,distante,lejano
insólito|1|raro,extraño,inusual,desacostumbrado|habitual,común,corriente,ordinario
vehemente|2|apasionado,impetuoso,ardiente,fogoso|apático,flemático,sosegado
escarnio|2|burla,mofa,befa,irrisión|respeto,elogio,alabanza
prohibir|1|vetar,vedar,impedir|permitir,autorizar,consentir,aprobar
ameno|1|agradable,grato,entretenido|tedioso,aburrido,árido
escasez|1|carencia,penuria,falta,insuficiencia|abundancia,riqueza,profusión
honesto|1|honrado,íntegro,recto,decente|corrupto,tramposo,ruin
veraz|1|sincero,franco,verídico|mentiroso,falso,embustero
temerario|2|imprudente,osado,arriesgado|prudente,cauteloso,precavido
mediocre|1|mediano,regular,anodino|excelente,sobresaliente,extraordinario
escrupuloso|2|meticuloso,minucioso,esmerado|descuidado,negligente,chapucero
atenuar|1|disminuir,mitigar,suavizar,aliviar|intensificar,agravar,acentuar
prolífico|2|fecundo,fértil,productivo|estéril,infecundo,improductivo
incipiente|2|naciente,inicial,embrionario|consumado,avanzado,maduro
recio|1|fuerte,robusto,vigoroso,resistente|débil,flojo,endeble,frágil
diáfano|2|transparente,cristalino,translúcido|opaco,turbio,borroso
ostensible|2|patente,manifiesto,evidente|oculto,latente,disimulado
aludir|1|mencionar,citar,nombrar|omitir,callar,silenciar
repudiar|2|rechazar,rehusar,desdeñar|aceptar,admitir,acoger
"""

# word | level | definition
_DEFINITIONS = """
alfaguara|2|Manantial copioso que surge con violencia.
escisión|2|Rompimiento, rotura o separación.
nimio|1|Insignificante, sin importancia.
ubérrimo|2|Muy abundante y fértil.
gárrulo|2|Muy hablador.
sempiterno|2|Que durará siempre.
hontanar|2|Sitio en que nacen fuentes.
arcano|2|Secreto, recóndito, reservado.
ínclito|2|Ilustre, esclarecido, insigne.
canícula|1|Período del año en que más aprieta el calor.
parsimonia|1|Lentitud y sosiego en el modo de obrar.
cenit|1|Punto más alto al que llega algo.
proclive|1|Inclinado o propenso a algo.
tesón|1|Firmeza, perseverancia y constancia.
letargo|1|Estado de somnolencia profunda y prolongada.
pábulo|2|Alimento o sustento de algo.
candor|1|Sinceridad y sencillez del ánimo.
recelo|1|Temor o sospecha de algo.
acervo|2|Conjunto de bienes morales o culturales acumulados por tradición o herencia.
mácula|2|Mancha.
dilación|1|Demora o tardanza en hacer algo.
perentorio|2|Urgente, apremiante.
sinecura|2|Empleo bien retribuido que da poco trabajo.
inefable|2|Que no se puede explicar con palabras.
óbice|2|Obstáculo o impedimento.
ardid|1|Artificio hábil para conseguir un propósito.
baldío|1|Dicho de una tierra: que no se cultiva.
nómada|1|Que va de un lugar a otro sin domicilio fijo.
cuantioso|1|Grande en cantidad o número.
escrutinio|2|Recuento de los votos en una elección.
inquina|2|Aversión o mala voluntad hacia alguien.
vetar|1|Poner el veto a algo.
pesquisa|2|Investigación para averiguar algo.
exiguo|1|Insuficiente, escaso.
holgazán|1|Que rehúye el trabajo y es perezoso.
colindante|1|Dicho de un terreno: que linda con otro.
"""

# right | wrong
_SPELLING = """
exuberante|exhuberante
hortaliza|ortaliza
exhausto|exausto
exhibir|exibir
inhibir|inibir
prohibir|prohivir
prohibido|prohivido
vehículo|vehiculo
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
conmigo|comigo
obvio|obbio
volver|bolver
ciudadanía|ciudadania
desarrollo|desarollo
excepción|excepsión
extranjero|estranjero
adolescente|adolecente
yacimiento|llacimiento
atención|atencion
administración|adminitración
examen|exámen
dificultad|dificutad
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
sílaba|silaba
tráfico|trafico
médico|medico
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
    "[también|tambien] en la [oficina|oficna] central.",
    "El [médico|medico] del servicio [recogió|recojió] los [expedientes|espedientes] y [exhibió|exibió] "
    "la [documentación|documentacion] ante el tribunal.",
    "Con [vergüenza|verguenza] y sin [atención|atencion] alguna, el [extranjero|estranjero] [volvió|bolvió] "
    "a la oficina para [reivindicar|reibindicar] su derecho.",
    "Se [prohibió|prohivió] el [vehículo|vehiculo] en el [ámbito|ambito] del [periódico|periodico] por una "
    "[excepción|excepsión] [inmediata|immediata].",
)


@dataclass(frozen=True)
class Entry:
    word: str
    level: int
    synonyms: tuple[str, ...]
    antonyms: tuple[str, ...]


@dataclass(frozen=True)
class Definition:
    word: str
    level: int
    text: str


def _rows(raw: str) -> list[list[str]]:
    return [line.split("|") for line in raw.strip().splitlines()]


@cache
def entries() -> tuple[Entry, ...]:
    return tuple(
        Entry(w, int(level), tuple(syn.split(",")), tuple(ant.split(",")))
        for w, level, syn, ant in _rows(_ENTRIES)
    )


@cache
def definitions() -> tuple[Definition, ...]:
    return tuple(Definition(w, int(level), text) for w, level, text in _rows(_DEFINITIONS))


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
