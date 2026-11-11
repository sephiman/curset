# SPDX-License-Identifier: AGPL-3.0-only
"""The printed tables of the Auxiliar questionnaires, transcribed once, and the questions that use each."""

from __future__ import annotations

from dataclasses import dataclass

Row = tuple[str, ...]


@dataclass(frozen=True)
class PrintedTable:
    key: str
    title_parts: tuple[str, ...]
    header: Row
    rows: tuple[Row, ...]
    # The line of the layout where the table starts; everything from there to the next question is the table.
    cut_pattern: str | None
    #: Printed beside the table, not part of it; appended to the title without being matched in the PDF text.
    side_note: str = ""


@dataclass(frozen=True)
class TableUse:
    exam_code: str
    section: str
    first: int
    last: int
    table_key: str


PRESTAMOS = PrintedTable(
    key="prestamos",
    title_parts=("Responda a las siguientes preguntas según la tabla llamada Préstamos",),
    header=(
        "Título",
        "Autor",
        "Lugar edición",
        "Año de publicación",
        "Editorial",
        "Ejemplares disponibles",
        "Ejemplares prestados",
        "Préstamos realizados",
    ),
    rows=(
        ("Aranmanoth", "Matute, Ana María", "Barcelona", "2000", "Destino", "5", "2", "249"),
        ("Contra Vosotros", "Soriano, Mercedes", "Madrid", "1998", "Alfaguara", "5", "4", "114"),
        ("Mano de sombra", "Marías, Javier", "Madrid", "1997", "Santillana", "7", "5", "311"),
        ("Adiós a las novias", "Puértolas, Soledad", "Barcelona", "1998", "Anagrama", "14", "6", "201"),
        ("La temporada de caza", "Camilleri, Andrea", "Barcelona", "2000", "Anagrama", "15", "5", "154"),
        ("El equipaje del viajero", "Saramago, José", "Madrid", "1999", "Alfaguara", "11", "3", "248"),
        ("El amante lesbiano", "Sampedro, José Luis", "Barcelona", "2000", "Plaza & Janés", "8", "7", "130"),
        ("Entre visillos", "Martín Gaite, Carmen", "Barcelona", "1998", "Destino", "10", "3", "268"),
        ("Un calor tan cercano", "Torres, Maruja", "Madrid", "1997", "Santillana", "15", "5", "290"),
        ("Hija de la fortuna", "Allende, Isabel", "Barcelona", "1999", "Plaza & Janés", "13", "7", "206"),
    ),
    cut_pattern=r"^Préstamos$",
)

# The «Dieta / Euros» block and the «Combustible» line print beside the table, not in it: in the title.
DESPLAZAMIENTOS = PrintedTable(
    key="desplazamientos",
    title_parts=("Responda a las siguientes preguntas según la tabla llamada Desplazamientos",),
    header=("Proyecto", "Departamento", "Oficina", "Duración días", "Kilómetros", "Peajes/Euros"),
    rows=(
        ("A-115", "Administración", "Zaragoza", "1", "505", "40,64"),
        ("M-254", "Marketing", "Zaragoza", "0,5", "721", "16,60"),
        ("C-491", "Administración", "Valencia", "2", "678", "10,84"),
        ("A-115", "Marketing", "Tarragona", "1", "1.425", "38,90"),
        ("M-254", "Técnico", "Bilbao", "2", "1.250", "30,40"),
        ("C-510", "Comercial", "Valencia", "3", "707", "22,34"),
        ("C-510", "Marketing", "Bilbao", "0,5", "1.388", "11,78"),
        ("M-254", "Técnico", "Málaga", "3", "962", "35,87"),
        ("C-510", "Comercial", "Tarragona", "2", "1.104", "5,97"),
        ("A-115", "Comercial", "Málaga", "2", "1.541", "22,72"),
    ),
    cut_pattern=r"^Desplazamientos$",
    side_note="Dieta: Media (0,5 días) 24,50 €, Día 55,45 €. Combustible: 0,2 €/Km",
)

BIBLIOTECA = PrintedTable(
    key="biblioteca",
    title_parts=("Cuadro Biblioteca",),
    header=(
        "Tema: Materia",
        "Tema: Clasificación",
        "Ubicación: Planta",
        "Ubicación: Clasificación",
        "Ubicación: Pasillo",
        "Ubicación: Estanterías",
        "Títulos: Total",
        "Títulos: En uso",
    ),
    rows=(
        ("Derecho", "Económico", "1", "A-M", "2 izquierda", "2 a 5", "45", "28"),
        ("Derecho", "Económico", "1", "N-Z", "3 derecha", "1 a 5", "58", "11"),
        ("Derecho", "Laboral", "2", "A-G", "1 izquierda", "2 a 4", "39", "17"),
        ("Derecho", "Laboral", "2", "H-O", "2 derecha", "3 a 5", "62", "9"),
        ("Derecho", "Laboral", "2", "P-Z", "2 izquierda", "1 a 3", "47", "8"),
        ("Geografía", "Física", "2", "A-O", "3 derecha", "2 a 4", "55", "15"),
        ("Geografía", "Física", "3", "P-Z", "1 derecha", "1 a 5", "31", "6"),
        ("Geografía", "Política", "3", "A-L", "1 izquierda", "1 a 4", "40", "12"),
        ("Geografía", "Política", "3", "M-Z", "2 derecha", "3 a 5", "53", "20"),
        ("Geografía", "Cartografía", "4", "A-J", "1 izquierda", "1 a 3", "54", "19"),
    ),
    cut_pattern=r"^Cuadro Biblioteca$",
)

ACADEMIA = PrintedTable(
    key="academia",
    title_parts=("Tabla Academia", "Todos los alumnos con pelo fueron rubios, morenos o pelirrojos"),
    header=("Mes", "Total de alumnos", "Rubios", "Morenos", "Pelirrojos", "Alumnos impagados"),
    rows=(
        ("Enero", "6521", "321", "245", "7", "201"),
        ("Febrero", "5364", "290", "255", "8", "603"),
        ("Marzo", "5287", "267", "232", "6", "103"),
        ("Abril", "6002", "241", "241", "9", "497"),
        ("Mayo", "5781", "222", "187", "15", "417"),
        ("Junio", "3057", "175", "97", "12", "300"),
        ("Julio", "3825", "152", "88", "11", "300"),
    ),
    cut_pattern=r"^TABLA ACADEMIA$",
)

# The first column holds the digit of each code position; it prints no heading.
ARCHIVOS = PrintedTable(
    key="archivos",
    title_parts=(
        "Tabla Archivos",
        "Un bibliotecario decide clasificar sus archivos según la estructura de la siguiente tabla",
        "De manera que un archivo con el código 111111 representa un libro en castellano, situado en el"
        " primer estante del primer pasillo, de color rojo que, es el primer ejemplar de un libro",
    ),
    header=("", "Idioma", "Pasillo", "Estante", "Color Tapa", "Soporte", "Ejemplar"),
    rows=(
        ("1", "Castellano", "Primer Pasillo", "Primer Estante", "Rojo", "Libro", "Primer Ejemplar"),
        ("2", "Catalán", "Segundo Pasillo", "Segundo Estante", "Azul", "CD", "Segundo Ejemplar"),
        ("3", "Ingles", "Tercer Pasillo", "Tercer Estante", "Negro", "Memoria", "Tercer Ejemplar"),
        ("4", "Frances", "Cuarto Pasillo", "Cuarto Estante", "Amarillo", "Libreta", "Cuarto Ejemplar"),
    ),
    cut_pattern=r"^TABLA ARCHIVOS$",
)

PONENCIAS = PrintedTable(
    key="ponencias",
    title_parts=(
        "Tabla Ponencias",
        "El material para cada ponencia es entregado a cada ponente y alumno",
        "Los asistentes a cada ponencia son los ponentes y alumnos",
    ),
    header=("Turno", "Sala", "Tema", "Tipo", "Material", "Alumnos", "Ponentes"),
    rows=(
        ("Mañana 1º", "1", "Comercial", "Charla", "Pdf", "41", "4"),
        ("Mañana 1º", "2", "Contabilidad", "Mesa redonda", "Word", "52", "17"),
        ("Mañana 2º", "1", "Recursos Humanos", "Charla", "Cd", "48", "6"),
        ("Mañana 2º", "3", "Administración", "Laboratorio", "Cd", "41", "2"),
        ("Mañana 3º", "3", "Comercial", "Laboratorio", "Pdf", "42", "11"),
        ("Tarde 1º", "1", "Administración", "Charla", "Pdf", "56", "13"),
        ("Tarde 1º", "2", "Contabilidad", "Laboratorio", "Cd", "39", "9"),
        ("Tarde 2º", "1", "Comercial", "Laboratorio", "Pdf", "48", "2"),
        ("Tarde 2º", "3", "Recursos Humanos", "Laboratorio", "Cd", "51", "5"),
        ("Tarde 3º", "3", "Administración", "Charla", "Pdf", "43", "5"),
        ("Tarde 3º", "2", "Contabilidad", "Mesa redonda", "Word", "54", "15"),
        ("Tarde 3º", "1", "Comercial", "Charla", "Pdf", "37", "3"),
    ),
    cut_pattern=r"^TABLA PONENCIAS:$",
)

# Printed as three tables that share the «Flor» column in the same order: one table with every column.
FLORES = PrintedTable(
    key="flores",
    title_parts=("Tablas Flores",),
    header=(
        "Flor",
        "Colores",
        "Tipos de ramos (unidades)",
        "Pétalos",
        "Peso en gramos",
        "Estambres",
        "Precio unidad",
        "Fragancia potente",
        "Entrega domicilio",
        "Pequeña",
        "En promoción",
        "Duradera",
    ),
    rows=(
        ("Margarita", "blanco y amarillo", "3", "2", "2", "2", "3", "NO", "SI", "NO", "SI", "SI"),
        ("Rosa", "blanco, amarillo y rosa", "6", "4", "5", "4", "2", "NO", "NO", "SI", "SI", "SI"),
        ("Clavel", "amarillo y rosa", "3 y 6", "3", "1", "6", "5", "SI", "NO", "NO", "NO", "NO"),
        ("Salvia", "rosa", "3, 6 y 12", "1", "6", "3", "2", "SI", "SI", "SI", "SI", "NO"),
        ("Crisantemo", "blanco y rosa", "3, 6 y 12", "4", "4", "8", "5", "NO", "NO", "SI", "SI", "NO"),
        ("Tulipán", "amarillo", "3, 6 y 12", "5", "5", "5", "4", "SI", "SI", "NO", "NO", "SI"),
        ("Cardo", "blanco", "3", "4", "1", "4", "5", "NO", "NO", "SI", "SI", "NO"),
        ("Lirio", "blanco y amarillo", "6", "3", "5", "6", "4", "SI", "NO", "NO", "NO", "SI"),
        ("Orquídea", "blanco y rosa", "3, 6 y 12", "4", "6", "8", "3", "NO", "SI", "SI", "SI", "NO"),
        ("Gerbera", "amarillo y rosa", "3 y 6", "5", "1", "7", "5", "SI", "NO", "SI", "SI", "NO"),
    ),
    cut_pattern=r"^TABLAS FLORES:$",
)

SALAS = PrintedTable(
    key="salas",
    title_parts=(
        "En la tabla siguiente se exponen las características principales de las salas de un edificio que se"
        " utilizan para la organización de cursos",
        "En relación con la información indicada en ella, responda las seis preguntas siguientes",
    ),
    header=(
        "Nombre Sala",
        "Tipo",
        "Disponibilidad",
        "Capacidad alumnos (número)",
        "Equipación",
        "Toma de red (Sí o No existe)",
        "Equipos informáticos (número)",
        "Superficie (en metros cuadrados)",
        "Tipo de Decoración",
    ),
    rows=(
        ("Nueva York", "Sala de reuniones", "Mañanas", "6", "No", "No", "8", "15", "Estándar"),
        ("Tokio", "Sala de reuniones", "Tardes", "17", "Proyector", "Sí", "12", "45", "Estándar"),
        (
            "Tijuana",
            "Sala de reuniones",
            "Mañanas",
            "26",
            "Proyector y Megafonía",
            "Sí",
            "12",
            "50",
            "Ejecutiva",
        ),
        ("Dubái", "Sala de reuniones", "Mañanas", "28", "Megafonía", "No", "13", "52", "Ejecutiva"),
        ("Madrid", "Sala de clases", "Mañanas y Tardes", "9", "Proyector", "No", "3", "25", "Estándar"),
        ("Las Vegas", "Sala de reuniones", "Mañanas y Tardes", "10", "No", "No", "14", "28", "Estándar"),
        ("Múnich", "Sala de clases", "Tardes", "13", "Proyector", "No", "7", "30", "Estándar"),
        ("Seúl", "Sala de clases", "Mañanas y Tardes", "22", "Proyector", "No", "15", "48", "Ejecutiva"),
        ("Londres", "Sala de clases", "Mañanas y Tardes", "30", "Proyector", "Sí", "30", "53", "Ejecutiva"),
        (
            "Barcelona",
            "Sala de reuniones",
            "Tardes",
            "18",
            "Proyector y Megafonía",
            "Sí",
            "7",
            "47",
            "Ejecutiva",
        ),
    ),
    cut_pattern=r"^31 a 36\.",
)

ACADEMIA_IDIOMAS = PrintedTable(
    key="academia-idiomas",
    title_parts=(
        "En la siguiente tabla se ofrecen los datos de una academia de idiomas en cuanto al número de clases"
        " de inglés impartidas, la edad de los estudiantes y los libros que han vendido en diversos meses"
        " del año de su actividad económica",
        "Responda las seis preguntas siguientes",
    ),
    header=("Mes", "Clases de inglés", "Estudiantes adolescentes", "Estudiantes adultos", "Libros vendidos"),
    rows=(
        ("Enero", "7.150", "407", "531", "843"),
        ("Febrero", "5.860", "367", "498", "802"),
        ("Marzo", "4.865", "320", "462", "732"),
        ("Abril", "6.108", "323", "528", "835"),
        ("Mayo", "5.744", "289", "429", "654"),
        ("Junio", "4.500", "220", "405", "539"),
        ("Septiembre", "6.540", "186", "620", "800"),
        ("Octubre", "8.390", "189", "587", "738"),
        ("Noviembre", "9.120", "194", "553", "720"),
        ("Diciembre", "9.640", "158", "560", "698"),
    ),
    cut_pattern=r"^44 a 49\.",
)

DIGITALIZACION = PrintedTable(
    key="digitalizacion",
    title_parts=(
        "Tabla Digitalización",
        "En la tabla siguiente se exponen los datos obrantes en una empresa sobre los trabajos de"
        " digitalización que debe realizar, describiendo sus características principales que deberán ser"
        " tenidas en cuenta",
        "En relación con ella deberá responder una serie de cuestiones",
    ),
    header=(
        "Título",
        "Autor",
        "Año primera publicación",
        "Forma",
        "Materia",
        "Imágenes (Sí o No constan)",
        "Calidad del original",
        "Revisión",
        "Estado de la Digitalización",
    ),
    rows=(
        (
            "Diccionario biográfico americano",
            "Cortés, José Domingo",
            "1876",
            "Facsímil",
            "Diccionario",
            "Sí",
            "Media",
            "Terminada",
            "Terminada",
        ),
        (
            "Breve diccionario valenciano-castellano",
            "Ros, Carlos Mariner",
            "1739",
            "Libro",
            "Diccionario",
            "Sí",
            "Baja",
            "En proceso",
            "En proceso",
        ),
        (
            "Carácter convencional del ritmo",
            "Bigorra, Sebastián",
            "2006",
            "Documento",
            "Retórica y Poética",
            "No",
            "Alta",
            "Terminada",
            "Aprobada",
        ),
        (
            "Diccionario Castellano-Valenciano",
            "Lamarca, Luis",
            "1839",
            "Libro",
            "Diccionario",
            "No",
            "Media",
            "En proceso",
            "Aprobada",
        ),
        (
            "Diccionario histórico abreviado",
            "Ladvocat, Jean-Baptiste",
            "1753",
            "Manuscrito",
            "Diccionario",
            "Sí",
            "Alta",
            "Terminada",
            "En espera",
        ),
        (
            "Dictionarium ex hispaniensi in latinum sermonem",
            "Nebrija, Antonio de",
            "1581",
            "Facsímil",
            "Diccionario",
            "No",
            "Media",
            "Terminada",
            "En proceso",
        ),
        (
            "El Lenguaje poético como lenguaje absoluto",
            "Lázaro Carreter, Fernando",
            "2011",
            "Documento",
            "Retórica y Poética",
            "No",
            "Alta",
            "En proceso",
            "Aprobada",
        ),
        (
            "Manual de retórica y poética",
            "Milà i Fontanals, Manuel",
            "1848",
            "Manuscrito",
            "Retórica y Poética",
            "Sí",
            "Baja",
            "Terminada",
            "Terminada",
        ),
        (
            "Oratoria sacra seu Modus concionandi",
            "Diego de Estella (O.F.M.)",
            "1772",
            "Facsímil",
            "Retórica y Poética",
            "Sí",
            "Alta",
            "Terminada",
            "Terminada",
        ),
        (
            "Rhetorica",
            "Mayans y Siscar, Gregorio",
            "1752",
            "Facsímil",
            "Retórica y Poética",
            "Sí",
            "Baja",
            "En proceso",
            "En espera",
        ),
    ),
    cut_pattern=r"^46 a 51\.",
)

EXCURSIONES = PrintedTable(
    key="excursiones",
    title_parts=(
        "Tabla Excursiones",
        "En la siguiente tabla se ofrecen los datos económicos de una empresa en cuanto al número de"
        " turistas y al número de distintos tipos de excursiones realizadas en diversos meses del año de"
        " actividad",
        "Suponiendo que, para los siguientes meses, cada turista ha realizado los tres tipos de excursiones"
        " (temáticas, autobús y barco), responda a las preguntas realizadas en base a estos datos",
    ),
    header=("Mes", "Turistas", "Excursiones temáticas", "Excursiones autobús", "Excursiones barco"),
    rows=(
        ("Marzo", "5.785", "482", "231", "317"),
        ("Abril", "5.935", "421", "111", "209"),
        ("Mayo", "5.739", "368", "164", "217"),
        ("Junio", "7.465", "409", "227", "129"),
        ("Julio", "7.630", "585", "275", "341"),
        ("Agosto", "6.102", "567", "183", "326"),
        ("Septiembre", "5.817", "346", "184", "125"),
        ("Octubre", "6.028", "305", "132", "138"),
        ("Noviembre", "5.699", "298", "169", "224"),
        ("Diciembre", "6.420", "256", "158", "253"),
    ),
    cut_pattern=r"^55 a 60\.",
)

LABORATORIOS_HEADER: Row = (
    "Profesor",
    "Materia",
    "Día",
    "Hora",
    "Inscritos",
    "Planta",
    "Aula",
    "Capacidad",
)

TABLES: dict[str, PrintedTable] = {
    table.key: table
    for table in (
        PRESTAMOS,
        DESPLAZAMIENTOS,
        BIBLIOTECA,
        ACADEMIA,
        ARCHIVOS,
        PONENCIAS,
        FLORES,
        SALAS,
        ACADEMIA_IDIOMAS,
        DIGITALIZACION,
        EXCURSIONES,
    )
}

TABLE_USES: tuple[TableUse, ...] = (
    TableUse("conv2025_A", "P1", 49, 54, "prestamos"),
    TableUse("conv2025_A", "P1", 55, 60, "desplazamientos"),
    TableUse("conv2025_B", "P1", 49, 54, "prestamos"),
    TableUse("conv2025_B", "P1", 55, 60, "desplazamientos"),
    TableUse("conv2024_A", "P1", 49, 54, "biblioteca"),
    TableUse("conv2024_A", "P1", 55, 60, "laboratorios"),
    TableUse("conv2024_B", "P1", 49, 54, "biblioteca"),
    TableUse("conv2024_B", "P1", 55, 60, "laboratorios"),
    TableUse("conv2024_X", "P1", 49, 54, "academia"),
    TableUse("conv2024_X", "P1", 55, 60, "archivos"),
    TableUse("conv2022", "P1", 49, 54, "ponencias"),
    TableUse("conv2022", "P1", 55, 60, "flores"),
    TableUse("conv2020", "P1", 31, 36, "salas"),
    TableUse("conv2020", "P1", 44, 49, "academia-idiomas"),
    TableUse("conv2020_X", "P1", 46, 51, "digitalizacion"),
    TableUse("conv2020_X", "P1", 55, 60, "excursiones"),
)
