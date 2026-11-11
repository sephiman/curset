# SPDX-License-Identifier: AGPL-3.0-only
"""Recompute every table question of the stored Auxiliar official exams and compare it with its key."""

from __future__ import annotations

import re
import sys
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path

import yaml

_BACKEND = Path(__file__).resolve().parent.parent
if str(_BACKEND) not in sys.path:
    sys.path.insert(0, str(_BACKEND))

from scripts.build_c2_official_exams import EXAMS, EXERCISES_DIR  # noqa: E402

Record = dict[str, str]
Solver = Callable[[list[Record], list[str]], list[int]]

_TOLERANCE = 1e-9


def number(cell: str) -> float:
    text = cell.strip().rstrip(".").removesuffix("%").strip()
    text = re.sub(r"[^\d.,-]+.*$", "", text)
    if re.fullmatch(r"-?\d{1,3}(\.\d{3})+", text):
        text = text.replace(".", "")
    return float(text.replace(",", "."))


def decimals(cell: str) -> int:
    text = cell.strip().rstrip(".")
    return len(text.split(",")[1].split()[0]) if "," in text else 0


def numeric_option(value: float) -> Solver:
    def solve(_rows: list[Record], options: list[str]) -> list[int]:
        return [
            i
            for i, option in enumerate(options)
            if abs(number(option) - value) <= 0.5 * 10 ** -decimals(option) + _TOLERANCE
        ]

    return solve


def label(option: str) -> str:
    return option.strip().rstrip(".").casefold()


def best_label(scores: Mapping[str, float], options: list[str], *, highest: bool = True) -> list[int]:
    folded = {label(k): v for k, v in scores.items()}
    candidates = [(folded[label(o)], i) for i, o in enumerate(options) if label(o) in folded]
    target = max(v for v, _ in candidates) if highest else min(v for v, _ in candidates)
    return [i for v, i in candidates if abs(v - target) < _TOLERANCE]


def label_option(text: str) -> Solver:
    return lambda _rows, options: [i for i, o in enumerate(options) if label(o) == label(text)]


def group_sum(rows: list[Record], by: str, column: str) -> dict[str, float]:
    sums: dict[str, float] = {}
    for row in rows:
        sums[row[by]] = sums.get(row[by], 0.0) + number(row[column])
    return sums


def group_mean(rows: list[Record], by: str, column: str) -> dict[str, float]:
    counts: dict[str, int] = {}
    for row in rows:
        counts[row[by]] = counts.get(row[by], 0) + 1
    return {k: v / counts[k] for k, v in group_sum(rows, by, column).items()}


def top_group_sum(by: str, column: str, *, highest: bool = True) -> Solver:
    return lambda rows, options: best_label(group_sum(rows, by, column), options, highest=highest)


def top_group_mean(by: str, column: str) -> Solver:
    return lambda rows, options: best_label(group_mean(rows, by, column), options)


def top_row(key: str, score: Callable[[Record], float], *, highest: bool = True) -> Solver:
    return lambda rows, options: best_label({r[key]: score(r) for r in rows}, options, highest=highest)


def where(rows: list[Record], **equals: str) -> list[Record]:
    return [r for r in rows if all(r[column] == value for column, value in equals.items())]


# ---------------------------------------------------------------- Préstamos / Desplazamientos

PRESTAMOS: list[tuple[str, Solver]] = [
    (
        r"editoriales acumula un mayor número de ejemplares disponibles",
        top_group_sum("Editorial", "Ejemplares disponibles"),
    ),
    (
        r"editoriales acumula un mayor número de préstamos realizados",
        top_group_sum("Editorial", "Préstamos realizados"),
    ),
    (
        r"editorial de Barcelona, en un año posterior a 1998",
        lambda rows, options: [
            i
            for i, o in enumerate(options)
            for r in rows
            if label(r["Título"]) == label(o)
            and r["Lugar edición"] == "Barcelona"
            and number(r["Año de publicación"]) > 1998
            and number(r["Ejemplares disponibles"]) > 10
        ],
    ),
    (
        r"editoriales acumula un mayor número de ejemplares prestados",
        top_group_sum("Editorial", "Ejemplares prestados"),
    ),
    (
        r"títulos tiene un mayor porcentaje de ejemplares prestados con respecto a los disponibles",
        top_row("Título", lambda r: number(r["Ejemplares prestados"]) / number(r["Ejemplares disponibles"])),
    ),
    (
        r"autores tiene un mayor porcentaje de ejemplares prestados con respecto al total de préstamos",
        top_row("Autor", lambda r: number(r["Ejemplares prestados"]) / number(r["Préstamos realizados"])),
    ),
]


def peajes_per_km(rows: list[Record], options: list[str]) -> list[int]:
    peajes = group_sum(rows, "Proyecto", "Peajes/Euros")
    km = group_sum(rows, "Proyecto", "Kilómetros")
    return best_label({p: peajes[p] / km[p] for p in peajes}, options)


def km_share(column: str, value: str) -> Solver:
    def solve(rows: list[Record], options: list[str]) -> list[int]:
        total = sum(number(r["Kilómetros"]) for r in rows)
        part = sum(number(r["Kilómetros"]) for r in rows if r[column] == value)
        return numeric_option(100 * part / total)(rows, options)

    return solve


DESPLAZAMIENTOS: list[tuple[str, Solver]] = [
    (r"oficinas ha realizado un mayor número de kilómetros", top_group_sum("Oficina", "Kilómetros")),
    (r"departamentos tiene una media mayor de duración", top_group_mean("Departamento", "Duración días")),
    (
        r"departamentos tiene una media mayor de pago en euros por peaje",
        top_group_mean("Departamento", "Peajes/Euros"),
    ),
    (r"proyectos ha tenido un mayor pago de peajes por kilómetro", peajes_per_km),
    (r"porcentaje de kilómetros realizados por la oficina de Tarragona", km_share("Oficina", "Tarragona")),
    (r"porcentaje de kilómetros realizados en el proyecto A-115", km_share("Proyecto", "A-115")),
]

# ---------------------------------------------------------------- Biblioteca / Laboratorios


def shelf_of(rows: list[Record], tema: str, name: str) -> Record | None:
    initial = name.strip().strip('"“”').upper()[0]
    for r in rows:
        low, high = r["Ubicación: Clasificación"].split("-")
        if (
            label(f"{r['Tema: Materia']} {r['Tema: Clasificación']}") == label(tema)
            and low <= initial <= high
        ):
            return r
    return None


def place_of(r: Record | None) -> tuple[str, str, str] | None:
    return (
        None if r is None else (r["Ubicación: Planta"], r["Ubicación: Pasillo"], r["Ubicación: Estanterías"])
    )


def place_for_title(tema: str, name: str) -> Solver:
    def solve(rows: list[Record], options: list[str]) -> list[int]:
        expected = place_of(shelf_of(rows, tema, name))
        parsed = [
            re.findall(r"Planta: (\d+)\.? Pasillo: ([^.]+)\. Estanterías: ([^.]+)\.", o)[0] for o in options
        ]
        return [i for i, p in enumerate(parsed) if tuple(x.strip() for x in p) == expected]

    return solve


def title_for_place(planta: str, pasillo: str, estanterias: str) -> Solver:
    def solve(rows: list[Record], options: list[str]) -> list[int]:
        found = []
        for i, option in enumerate(options):
            tema, name = re.findall(r'Tema: ([^.]+)\. Nombre: "([^"]+)', option)[0]
            if place_of(shelf_of(rows, tema, name)) == (planta, pasillo, estanterias):
                found.append(i)
        return found

    return solve


def tema_totals(rows: list[Record]) -> dict[str, float]:
    totals: dict[str, float] = {}
    for r in rows:
        tema = f"{r['Tema: Materia']} {r['Tema: Clasificación']}"
        totals[tema] = totals.get(tema, 0.0) + number(r["Títulos: Total"])
    return totals


def above_average_tema(rows: list[Record], options: list[str]) -> list[int]:
    totals = tema_totals(rows)
    mean = sum(totals.values()) / len(totals)
    return [
        i for i, o in enumerate(options) if totals[next(k for k in totals if label(k) == label(o))] > mean
    ]


BIBLIOTECA: list[tuple[str, Solver]] = [
    (
        r'Nombre: "Trabajo temporal\. Tributación"',
        place_for_title("Derecho Económico", "Trabajo temporal. Tributación"),
    ),
    (r"planta 3, pasillo 1 izquierda, estanterías 1 a 4", title_for_place("3", "1 izquierda", "1 a 4")),
    (
        r"temas tiene un mayor número total de títulos",
        lambda rows, options: best_label(tema_totals(rows), options),
    ),
    (r"superior a la media", above_average_tema),
    (r'Nombre: "Cordilleras\s+asiáticas"', place_for_title("Geografía Física", "Cordilleras asiáticas")),
    (r"planta 2, pasillo 1 izquierda, estanterías 2 a 4", title_for_place("2", "1 izquierda", "2 a 4")),
]

HOUR = {"10:00": 10, "11:00": 11, "12:00": 12, "13:00": 13}
DAY_ORDER = {"Lunes": 1, "Martes": 2, "Miércoles": 3, "Jueves": 4, "Viernes": 5}


def room_floor_total(rows: list[Record], options: list[str]) -> list[int]:
    totals = group_sum(rows, "Planta", "Capacidad")
    return best_label({f"Planta {k}": v for k, v in totals.items()}, options, highest=False)


def room_above_second_floor(rows: list[Record], options: list[str]) -> list[int]:
    upper = [r for r in rows if number(r["Planta"]) > 2]
    return best_label({r["Aula"]: number(r["Inscritos"]) for r in upper}, options)


def subject_large_late_floor3(rows: list[Record], options: list[str]) -> list[int]:
    fits = {
        r["Materia"]
        for r in rows
        if number(r["Capacidad"]) > 45 and DAY_ORDER[r["Día"]] > DAY_ORDER["Martes"] and r["Planta"] == "3"
    }
    return [i for i, o in enumerate(options) if o.strip().rstrip(".") in fits]


def latest_floor2_teacher(rows: list[Record], options: list[str]) -> list[int]:
    ends = {r["Profesor"]: HOUR[r["Hora"]] + 1 for r in rows if r["Planta"] == "2"}
    return best_label(ends, options)


def earliest_room2_teacher(rows: list[Record], options: list[str]) -> list[int]:
    starts = {
        r["Profesor"]: HOUR[r["Hora"]] for r in rows if r["Aula"] == "2" and number(r["Capacidad"]) > 40
    }
    return best_label(starts, options, highest=False)


LABORATORIOS: list[tuple[str, Solver]] = [
    (r"qué día hay mayor asistencia", top_group_sum("Día", "Inscritos")),
    (r"menor capacidad total", room_floor_total),
    (r"aulas, situada por encima de la segunda planta", room_above_second_floor),
    (r"materias cuenta con un laboratorio de más de 45", subject_large_late_floor3),
    (r"planta 2 y termina más tarde", latest_floor2_teacher),
    (r"aula número 2, con una capacidad superior a 40", earliest_room2_teacher),
]

# ---------------------------------------------------------------- Academia / Archivos (conv2024_X)


def ratio_top(part: str, *, highest: bool = True) -> Solver:
    return top_row("Mes", lambda r: number(r[part]) / number(r["Total de alumnos"]), highest=highest)


def bald_students(rows: list[Record], options: list[str]) -> list[int]:
    hairless = {
        r["Mes"]: number(r["Total de alumnos"])
        - sum(number(r[c]) for c in ("Rubios", "Morenos", "Pelirrojos"))
        for r in rows
    }
    return best_label(hairless, options)


def july_remainder(rows: list[Record], options: list[str]) -> list[int]:
    unpaid = number(where(rows, Mes="Julio")[0]["Alumnos impagados"])
    return numeric_option(unpaid * (1 - 0.52 - 0.07 - 0.03))(rows, options)


ACADEMIA: list[tuple[str, Solver]] = [
    (
        r"media de alumnos con impago al mes",
        lambda rows, options: numeric_option(sum(number(r["Alumnos impagados"]) for r in rows) / len(rows))(
            rows, options
        ),
    ),
    (r"alumnos rubios han supuesto un mayor porcentaje", ratio_top("Rubios")),
    (r"resto de alumnos ese mes", july_remainder),
    (r"mayor porcentaje de impagos en relación con el número de alumnos", ratio_top("Alumnos impagados")),
    (r"más alumnos sin pelo", bald_students),
    (r"alumnos morenos han supuesto un menor porcentaje", ratio_top("Morenos", highest=False)),
]

CODE_FIELDS = ("Idioma", "Pasillo", "Estante", "Color Tapa", "Soporte", "Ejemplar")
# Each option states some attributes of a code, as the 1-based row of the Archivos table in that position.
ATTRIBUTES = {
    "inglés": ("Idioma", 3),
    "catalán": ("Idioma", 2),
    "francés": ("Idioma", 4),
    "segundo pasillo": ("Pasillo", 2),
    "cuarto pasillo": ("Pasillo", 4),
    "primer estante": ("Estante", 1),
    "segundo estante": ("Estante", 2),
    "tercer estante": ("Estante", 3),
    "rojo": ("Color Tapa", 1),
    "azul": ("Color Tapa", 2),
    "negro": ("Color Tapa", 3),
    "cd": ("Soporte", 2),
    "libreta": ("Soporte", 4),
    "tercer ejemplar": ("Ejemplar", 3),
    "cuarto ejemplar": ("Ejemplar", 4),
}


def statement_holds(code: str, statement: str) -> bool:
    digits = dict(zip(CODE_FIELDS, (int(c) for c in code), strict=True))
    text = statement.casefold()
    required = {ATTRIBUTES[k] for k in ATTRIBUTES if k in text}
    return all(digits[field] == value for field, value in required)


def code_statements(code: str, *, want_true: bool) -> Solver:
    def solve(_rows: list[Record], options: list[str]) -> list[int]:
        return [i for i, o in enumerate(options) if statement_holds(code, o) is want_true]

    return solve


def hamlet_barraca(_rows: list[Record], options: list[str]) -> list[int]:
    # «Hamlet» is English (3) and «La barraca» Spanish (1): the first digit (idioma) cannot coincide.
    return [i for i, o in enumerate(options) if "primer número" in o]


ARCHIVOS: list[tuple[str, Solver]] = [
    (
        r"clave es 421134 es FALSO",
        lambda rows, options: code_statements("421134", want_true=False)(rows, options[:3]),
    ),
    (r"Hamlet", hamlet_barraca),
    (r"La colmena", label_option("121112")),
    (r"clave es 321324 es falso", code_statements("321324", want_true=False)),
    (r"clave es 241243 es falso", code_statements("241243", want_true=False)),
    (
        r"clave es 423123 es cierto",
        lambda rows, options: (
            [3] if len(code_statements("423123", want_true=True)(rows, options[:3])) == 3 else []
        ),
    ),
]

# ---------------------------------------------------------------- Ponencias / Flores (conv2022)


def attendees(r: Record) -> float:
    return number(r["Alumnos"]) + number(r["Ponentes"])


def sum_where(column: Callable[[Record], float], predicate: Callable[[Record], bool]) -> Solver:
    return lambda rows, options: numeric_option(sum(column(r) for r in rows if predicate(r)))(rows, options)


def afternoon(r: Record) -> bool:
    return r["Turno"].startswith("Tarde")


def second_shift(r: Record) -> bool:
    return r["Turno"].endswith("2º")


PONENCIAS: list[tuple[str, Solver]] = [
    (
        r"alumnos hay para cada ponente en la ponencia comercial del segundo turno de tarde",
        lambda rows, options: numeric_option(
            number(where(rows, Turno="Tarde 2º", Tema="Comercial")[0]["Alumnos"])
            / number(where(rows, Turno="Tarde 2º", Tema="Comercial")[0]["Ponentes"])
        )(rows, options),
    ),
    (
        r"ponentes del segundo turno en mañana y tarde",
        sum_where(
            lambda r: number(r["Ponentes"]),
            lambda r: second_shift(r) and r["Tema"] == "Recursos Humanos" and r["Material"] == "Cd",
        ),
    ),
    (
        r"asistentes hay que requieren con material Pdf",
        sum_where(attendees, lambda r: afternoon(r) and r["Sala"] == "1" and r["Material"] == "Pdf"),
    ),
    (
        r"mínimo de asistentes por la tarde",
        lambda rows, options: numeric_option(
            min(attendees(r) for r in rows if afternoon(r) and r["Tipo"] == "Charla")
        )(rows, options),
    ),
    (
        r"total de asistentes en el segundo turno",
        sum_where(
            attendees,
            lambda r: second_shift(r) and r["Tipo"] == "Laboratorio" and r["Tema"] != "Recursos Humanos",
        ),
    ),
    (
        r"asistentes acuden en la tarde en la sala 1",
        sum_where(attendees, lambda r: afternoon(r) and r["Sala"] == "1"),
    ),
]


def flower_names(rows: list[Record], options: list[str], predicate: Callable[[Record], bool]) -> list[int]:
    names = {r["Flor"] for r in rows if predicate(r)}
    return [i for i, o in enumerate(options) if o.strip().rstrip(".") in names]


def count_flowers(predicate: Callable[[Record], bool]) -> Solver:
    return lambda rows, options: numeric_option(sum(1 for r in rows if predicate(r)))(rows, options)


FLORES: list[tuple[str, Solver]] = [
    (
        r"flores de color rosa están disponibles con entrega a domicilio en ramos de media docena",
        count_flowers(
            lambda r: (
                "rosa" in r["Colores"]
                and r["Entrega domicilio"] == "SI"
                and "6" in r["Tipos de ramos (unidades)"]
            )
        ),
    ),
    (
        r"fragancia potente se ofrece en ramos de una docena y es pequeña",
        lambda rows, options: flower_names(
            rows,
            options,
            lambda r: (
                r["Fragancia potente"] == "SI"
                and "12" in r["Tipos de ramos (unidades)"]
                and r["Pequeña"] == "SI"
            ),
        ),
    ),
    (
        r"más de dos pétalos están en promoción y no son duraderas",
        count_flowers(
            lambda r: number(r["Pétalos"]) > 2 and r["En promoción"] == "SI" and r["Duradera"] == "NO"
        ),
    ),
    (
        r"cantidad total de estambres",
        sum_where(
            lambda r: number(r["Estambres"]),
            lambda r: "blanco" in r["Colores"] and r["Entrega domicilio"] == "NO",
        ),
    ),
    (
        r"flor pequeña que no posee fragancia potente es más barata",
        lambda rows, options: flower_names(
            [r for r in rows if r["Pequeña"] == "SI" and r["Fragancia potente"] == "NO"],
            options,
            lambda r: (
                number(r["Precio unidad"])
                == min(
                    number(x["Precio unidad"])
                    for x in rows
                    if x["Pequeña"] == "SI" and x["Fragancia potente"] == "NO"
                )
            ),
        ),
    ),
    (
        r"pequeña flor de color rosa no es duradera",
        lambda rows, options: flower_names(
            rows,
            options,
            lambda r: (
                r["Pequeña"] == "SI"
                and "rosa" in r["Colores"]
                and r["Duradera"] == "NO"
                and number(r["Pétalos"]) > 3
                and number(r["Precio unidad"]) < 5
            ),
        ),
    ),
]

# ---------------------------------------------------------------- Salas / Academia de idiomas (conv2020)


def room_names(predicate: Callable[[Record], bool]) -> Solver:
    def solve(rows: list[Record], options: list[str]) -> list[int]:
        names = {r["Nombre Sala"] for r in rows if predicate(r)}
        return [i for i, o in enumerate(options) if re.sub(r"^La sala ", "", o.strip().rstrip(".")) in names]

    return solve


def projector(r: Record) -> bool:
    return "Proyector" in r["Equipación"]


def morning(r: Record) -> bool:
    return r["Disponibilidad"] in ("Mañanas", "Mañanas y Tardes")


def afternoon_room(r: Record) -> bool:
    return r["Disponibilidad"] in ("Tardes", "Mañanas y Tardes")


def mean_capacity(rows: list[Record], options: list[str]) -> list[int]:
    chosen = [
        r
        for r in rows
        if projector(r)
        and r["Toma de red (Sí o No existe)"] == "Sí"
        and r["Tipo de Decoración"] == "Ejecutiva"
    ]
    return numeric_option(sum(number(r["Capacidad alumnos (número)"]) for r in chosen) / len(chosen))(
        rows, options
    )


def largest_class_room(rows: list[Record], options: list[str]) -> list[int]:
    chosen = {
        r["Nombre Sala"]: number(r["Capacidad alumnos (número)"])
        for r in rows
        if r["Tipo"] == "Sala de clases" and projector(r) and morning(r)
    }
    return best_label({f"La sala {k}": v for k, v in chosen.items()}, options)


SALAS: list[tuple[str, Solver]] = [
    (
        r"disponen de proyector, tienen decoración estándar y cuentan con toma de red",
        count_flowers(
            lambda r: (
                projector(r)
                and r["Tipo de Decoración"] == "Estándar"
                and r["Toma de red (Sí o No existe)"] == "Sí"
            )
        ),
    ),
    (
        r"disponible por las mañanas, con capacidad para más de 15",
        room_names(
            lambda r: (
                morning(r)
                and number(r["Capacidad alumnos (número)"]) > 15
                and number(r["Equipos informáticos (número)"]) >= number(r["Capacidad alumnos (número)"])
            )
        ),
    ),
    (
        r"metros cuadrados en total hay disponibles",
        sum_where(
            lambda r: number(r["Superficie (en metros cuadrados)"]),
            lambda r: projector(r) and r["Tipo de Decoración"] == "Ejecutiva" and afternoon_room(r),
        ),
    ),
    (r"salas de clases que cuentan con proyector y disponibilidad por las mañanas", largest_class_room),
    (r"media de capacidad de alumnos", mean_capacity),
    (
        r"sala de reuniones, que no cuenta con toma de red",
        room_names(
            lambda r: (
                r["Tipo"] == "Sala de reuniones"
                and r["Toma de red (Sí o No existe)"] == "No"
                and morning(r)
                and r["Tipo de Decoración"] == "Estándar"
            )
        ),
    ),
]


def students(r: Record) -> float:
    return number(r["Estudiantes adolescentes"]) + number(r["Estudiantes adultos"])


IDIOMAS: list[tuple[str, Solver]] = [
    (
        r"estudiantes adolescentes de las clases de inglés han supuesto un mayor porcentaje",
        top_row("Mes", lambda r: number(r["Estudiantes adolescentes"]) / students(r)),
    ),
    (
        r"de media más libros a los estudiantes",
        top_row("Mes", lambda r: number(r["Libros vendidos"]) / students(r)),
    ),
    (
        r"media menor de clases de inglés por estudiante",
        top_row("Mes", lambda r: number(r["Clases de inglés"]) / students(r), highest=False),
    ),
    (r"qué mes hubo más estudiantes", top_row("Mes", students)),
    (r"en qué mes hubo menos estudiantes", top_row("Mes", students, highest=False)),
    (
        r"62% de los estudiantes adultos",
        lambda rows, options: numeric_option(0.62 * sum(number(r["Estudiantes adultos"]) for r in rows))(
            rows, options
        ),
    ),
]

# ---------------------------------------------------------------- Digitalización / Excursiones (conv2020_X)


def titles(predicate: Callable[[Record], bool]) -> Solver:
    def solve(rows: list[Record], options: list[str]) -> list[int]:
        found = {label(r["Título"]) for r in rows if predicate(r)}
        return [i for i, o in enumerate(options) if label(o) in found]

    return solve


def years(predicate: Callable[[Record], bool]) -> Solver:
    def solve(rows: list[Record], options: list[str]) -> list[int]:
        found = {number(r["Año primera publicación"]) for r in rows if predicate(r)}
        return [i for i, o in enumerate(options) if number(o) in found]

    return solve


def form_of_nineteenth_century_dictionary(rows: list[Record], options: list[str]) -> list[int]:
    forms = {
        r["Forma"]
        for r in rows
        if 1801 <= number(r["Año primera publicación"]) <= 1900
        and r["Materia"] == "Diccionario"
        and r["Imágenes (Sí o No constan)"] == "No"
    }
    return [i for i, o in enumerate(options) if label(o) in {label(f) for f in forms}]


DIGITALIZACION: list[tuple[str, Solver]] = [
    (
        r"títulos de materia Diccionario tienen la revisión terminada",
        count_flowers(lambda r: r["Materia"] == "Diccionario" and r["Revisión"] == "Terminada"),
    ),
    (
        r"siglo XVIII cuentan con imágenes y su forma es facsímil",
        count_flowers(
            lambda r: (
                1701 <= number(r["Año primera publicación"]) <= 1800
                and r["Imágenes (Sí o No constan)"] == "Sí"
                and r["Forma"] == "Facsímil"
            )
        ),
    ),
    (
        r"facsímil con imágenes, la revisión terminada",
        years(
            lambda r: (
                r["Forma"] == "Facsímil"
                and r["Imágenes (Sí o No constan)"] == "Sí"
                and r["Revisión"] == "Terminada"
                and r["Materia"] == "Retórica y Poética"
            )
        ),
    ),
    (
        r"diccionario, cuya forma no es Libro",
        years(
            lambda r: (
                r["Materia"] == "Diccionario"
                and r["Forma"] != "Libro"
                and r["Calidad del original"] == "Media"
                and r["Estado de la Digitalización"] == "En proceso"
            )
        ),
    ),
    (
        r"forma facsímil, su calidad original es media",
        titles(
            lambda r: (
                r["Forma"] == "Facsímil"
                and r["Calidad del original"] == "Media"
                and r["Estado de la Digitalización"] == "Terminada"
            )
        ),
    ),
    (
        r"forma del título que tiene la primera fecha de publicación en el siglo XIX",
        form_of_nineteenth_century_dictionary,
    ),
]


def tourists_per(column: str, *, highest: bool = True) -> Solver:
    return top_row("Mes", lambda r: number(r["Turistas"]) / number(r[column]), highest=highest)


def all_excursions(r: Record) -> float:
    return sum(number(r[c]) for c in ("Excursiones temáticas", "Excursiones autobús", "Excursiones barco"))


def tourist_share(rows: list[Record], options: list[str]) -> list[int]:
    total = sum(number(r["Turistas"]) for r in rows)
    return best_label({r["Mes"]: number(r["Turistas"]) / total for r in rows}, options)


EXCURSIONES: list[tuple[str, Solver]] = [
    (r"mayor ratio de turistas por excursión temática", tourists_per("Excursiones temáticas")),
    (
        r"menor ratio de turistas respecto al total de excursiones",
        top_row("Mes", lambda r: number(r["Turistas"]) / all_excursions(r), highest=False),
    ),
    (
        r"mayor porcentaje de excursiones en barco",
        top_row("Mes", lambda r: number(r["Excursiones barco"]) / all_excursions(r)),
    ),
    (r"hubo más excursiones", top_row("Mes", all_excursions)),
    (r"porcentaje de turistas mayor respecto al total", tourist_share),
    (
        r"media de turistas",
        lambda rows, options: numeric_option(sum(number(r["Turistas"]) for r in rows) / len(rows))(
            rows, options
        ),
    ),
]

SOLVERS_BY_TITLE_PART: list[tuple[str, list[tuple[str, Solver]]]] = [
    ("tabla llamada Préstamos", PRESTAMOS),
    ("tabla llamada Desplazamientos", DESPLAZAMIENTOS),
    ("Cuadro Biblioteca", BIBLIOTECA),
    ("Cuadro Laboratorios", LABORATORIOS),
    ("Tabla Academia", ACADEMIA),
    ("Tabla Archivos", ARCHIVOS),
    ("Tabla Ponencias", PONENCIAS),
    ("Tablas Flores", FLORES),
    ("salas de un edificio", SALAS),
    ("academia de idiomas", IDIOMAS),
    ("Tabla Digitalización", DIGITALIZACION),
    ("Tabla Excursiones", EXCURSIONES),
]


@dataclass(frozen=True)
class Check:
    exam_code: str
    tag: str
    key: str
    computed: str
    ok: bool


def solvers_for(title: str) -> list[tuple[str, Solver]]:
    return next(solvers for part, solvers in SOLVERS_BY_TITLE_PART if part in title)


def check_exam(slug: str) -> list[Check]:
    document = yaml.safe_load((EXERCISES_DIR / f"{slug}.yaml").read_text(encoding="utf-8"))
    checks = []
    for variant in document["variants"]:
        table = variant.get("table")
        if table is None:
            continue
        records = [dict(zip(table["header"], row, strict=True)) for row in table["rows"]]
        options = [o["text"]["es"] for o in variant["options"]]
        prompt = variant["prompt"]["es"]
        matching = [solve for pattern, solve in solvers_for(table["title"]) if re.search(pattern, prompt)]
        assert len(matching) == 1, f"{slug} {variant['tags']}: {len(matching)} solvers for {prompt!r}"
        found = "".join("abcd"[i] for i in matching[0](records, options))
        key = next(o["id"] for o in variant["options"] if o["correct"])
        checks.append(Check(variant["tags"][0], variant["tags"][1], key, found, found == key))
    return checks


def check_all() -> list[Check]:
    return [check for exam in EXAMS for check in check_exam(exam.slug)]


def main() -> None:
    checks = check_all()
    for check in checks:
        if not check.ok:
            print(
                f"MISMATCH {check.exam_code} {check.tag}: key {check.key}, computed {check.computed or '-'}"
            )
    print(f"{sum(c.ok for c in checks)} of {len(checks)} table questions match the official key")


if __name__ == "__main__":
    main()
