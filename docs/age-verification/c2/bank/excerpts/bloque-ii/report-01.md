# Blind excerpt check — bloque-ii, batch 01

Labels verified against the saved file: HTML as rendered text (tags stripped, entities decoded, whitespace runs collapsed;
table rows as cells joined by « — »), PDF via pdftotext (raw and `-layout`, whitespace collapsed), `.txt` with line wraps
joined by one space. Every label below was found exactly once per occurrence by `grep -F` on that rendering.

n | key | verdict | label or none: reason | flags
---|---|---|---|---
1 | m02-l03-q059 | yes | |
2 | m02-l03-q061 | yes | |
3 | m02-l05-q012 | no | none: spread — the L2 and L3 sentences are in separate property paragraphs; the excerpt shows only L2 |
4 | m02-l05-q023 | no | one gigabyte — 1 GB = 109 B = 1 000 000 000 B | no excerpt
5 | m02-l05-q024 | no | none: spread — needs the 1 MB row and the 1 GB row | no excerpt
6 | m02-l05-q025 | no | none: spread — peta (103)5 and exa (103)6 sit in two different rows (pebi and exbi); the symbol E is not on the page | no excerpt
7 | m02-l05-q029 | no | Ese correo/mensaje suele tener un enlace (o fichero que contiene ese enlace) a un sitio web que suplanta al legítimo y que usan para engañarlo. | excerpt is not the unit its heading names: under «Phishing» it shows another entry (look-alike URL attack); in `-layout` text a pull quote interleaves with the entry
8 | m02-l05-q055 | no | 230 — gibi — Gi — gigabinary: (210)3 — giga: (103)3 | no excerpt; superscripts flatten (230 = 2^30)
9 | m02-l05-q056 | no | It is important to recognize that the new prefixes for binary multiples are not part of the International System of Units (SI), the modern metric system. | no excerpt
10 | m02-l05-q057 | no | However, for ease of understanding and recall, they were derived from the SI prefixes for positive powers of ten. | no excerpt; the «adding the letter "i,"» sentence ends in a quote mark, so the label is another sentence of the same paragraph
11 | m02-l05-q058 | no | one mebibyte — 1 MiB = 220 B = 1 048 576 B | no excerpt
12 | m02-l05-q059 | no | one kibibit — 1 Kibit = 210 bit = 1024 bit | no excerpt
13 | m02-l05-q061 | no | In December 1998 the International Electrotechnical Commission (IEC), the leading international organization for worldwide standardization in electrotechnology, approved as an IEC International Standard names and symbols for prefixes for binary multiples for use in the fields of data processing and data transmission. | no excerpt
14 | m02-l05-q062 | yes | | garbled: excerpt runs three paragraphs together with the heading «Historical context*» inside; 2^10 shows as «210»
15 | m02-l05-q075 | yes | |
16 | m02-l05-q090 | no | none: spread — «mucha información» and «se conectan al equipo de maneras similares» are two separate paragraphs; excerpt shows only the first |
17 | m02-l05-q118 | no | none: spread — user level (Sí) and directory level (No) are two rows of the Cuotas table; excerpt shows only the note | excerpt is a note, not the comparison its heading names
18 | m02-l05-q122 | no | none: spread — «Enlaces simbólicos» and «Puntos de montaje» are two rows; excerpt shows only the first |
19 | m02-l05-q159 | yes | | garbled: entry number inside, and the definition is cut to its last sentence («Estos sistemas suelen poseer…»)
20 | m02-l05-q168 | no | Con su lanzamiento en 1971, el 4004 sentó las bases del camino de la computación moderna con microprocesadores, los “cerebros” que hacen posible casi toda la tecnología actual, desde la nube hasta el edge. | no excerpt
21 | m02-l05-q171 | no | Al final, el 4004, con el tamaño de una uña humana, ofrecía la misma potencia de cálculo que el primer ordenador electrónico fabricado en 1946, el cuál llenaba una habitación entera. | no excerpt; page furniture («Ir al contenido principal») sits just before this paragraph
22 | m02-l05-q177 | no | Mantén todo bajo control estableciendo fechas de vencimiento y recordatorios para cada tarea, y "destaca" tus tareas más importantes. | excerpt is page furniture («Se aplica a»)
23 | m02-l05-q181 | no | It uses all bits of an octet, but has the quality of preserving the full US-ASCII [US-ASCII] range: US-ASCII characters are encoded in one octet having the normal US-ASCII value, and any octet with such a value can only stand for a US-ASCII character, and nothing else. | no excerpt
24 | m02-l05-q182 | no | A direct consequence is that a plain ASCII string is also a valid UTF-8 string. | no excerpt
25 | m02-l05-q183 | no | The first octet of a multi-octet sequence indicates the number of octets in the sequence. | no excerpt
26 | m02-l05-q184 | no | UTF-8 having a single-octet encoding unit, this last function is useless and the BOM will always appear as the octet sequence EF BB BF. | no excerpt; the paragraph is split by a page break, the label is wholly after it
27 | m02-l05-q185 | no | The UCS character U+FEFF "ZERO WIDTH NO-BREAK SPACE" is also known informally as "BYTE ORDER MARK" (abbreviated "BOM"). | no excerpt
28 | m02-l05-q186 | no | ISO/IEC 10646 [ISO.10646] defines a large character set called the Universal Character Set (UCS), which encompasses most of the world's writing systems. | no excerpt
29 | m02-l05-q216 | no | none: no admissible label — the fact is only the bullet «1 GB de memoria interna» (five words, no final punctuation) | excerpt is an unrelated bullet («Disponible en 610 mm…»)
30 | m02-l05-q220 | no | El sistema numérico más común es decimal, que tiene un valor base de 10 y un juego de caracteres simbólico de 0, 1, 2, 3, 4, 5, 6, 7, 8 y 9. | excerpt is page furniture («Se aplica a…» product list)
31 | m02-l05-q264 | no | > SeleccionarInicio Configuración>:Windows UpdateHistorial>de actualizaciones>Desinstalar actualizaciones . | excerpt is page furniture («Se aplica a»); the label itself is garbled on the page (icons between steps), Windows 11 list item
32 | m02-l05-q306 | no | 0000 0800-0000 FFFF — 1110xxxx 10xxxxxx 10xxxxxx | no excerpt; the file writes this row with «\|» between its two cells
33 | m02-l05-q307 | no | UTF-8 was devised in September 1992 by Ken Thompson, guided by design criteria specified by Rob Pike, with the objective of defining a UCS transformation format usable in the Plan9 operating system in a non- disruptive manner. | no excerpt; «non-» is hyphenated across a line break in the file
34 | m02-l05-q313 | no | none: heading only — «VMware» is a one-word list item; that it is third-party comes only from the subheading «Módulos de terceros» | excerpt is page furniture («Comentarios»)
35 | m02-l05-q339 | no | Suma de comprobación/ECC — No — Metadatos — Metadatos — No | excerpt is page furniture («Comentarios»)
36 | m02-l06-q089 | no | none: no admissible label — the shortcut is only the unpunctuated list item «Presionar la tecla + Windows W»; the intro «Para abrir el panel de widgets, puede:» does not hold it | excerpt joins the intro with the first list item only
37 | m02-l06-q094 | no | none: spread — red, volumen and batería are three separate list items under «El área Configuración rápida consta de:» |
38 | m02-l06-q100 | no | none: no admissible label — the shortcut is only the unpunctuated list item «Presione la tecla + de Windows N» |
39 | m02-l06-q124 | no | none: spread — the two values are two separate list items; excerpt shows only «En todos los escritorios» |
40 | m02-l06-q130 | no | CTRL+Esc — Abre el menú Inicio. | no excerpt
41 | m02-l06-q132 | no | none: spread — «Configuración de la barra de tareas» and «Expanda los comportamientos de la barra de tareas» are separate steps; excerpt lacks the second |
42 | m02-l06-q160 | no | Ctrl+Alt+Supr — Cambie a la pantalla de seguridad, donde puede bloquear el escritorio, cambiar de usuario, cerrar sesión, cambiar una contraseña o abrir el Administrador de tareas. | excerpt is the section intro only
43 | m02-l06-q202 | no | none: spread — «TAB — Avanzar por las opciones.» and «Mayús+Tab — Retroceder por las opciones.» are two rows; excerpt shows only Mayús+Tab | excerpt glues the section intro to one row
44 | m02-l07-q037 | yes | |
45 | m02-l07-q135 | no | Tecla Windows + Pausa — Abre la aplicación Configuraciónen la> páginaSistema Acerca de. | excerpt shows the Windows+V row; label text is garbled on the page
46 | m02-l07-q202 | yes | |
47 | m02-l07-q246 | no | Mayús+arrastrar un archivo con el mouse — Cuando suelte el archivo, muévalo a esa ubicación. | excerpt shows the Alt+drag row
48 | m02-l07-q247 | no | F5 — Actualice la ventana. | excerpt shows the Ctrl+U row
49 | m02-l07-q248 | no | F11 — Maximizar o minimizar la ventana activa. | excerpt shows the Ctrl+U row; the row occurs twice (Windows 11 and Windows 10 sections), identical
50 | m02-l07-q251 | no | Ctrl+Tab — Desplazarse a la pestaña siguiente. | excerpt shows the Alt+Flecha derecha row
51 | m02-l07-q298 | no | bat — Archivo de lotes de PC | excerpt is the list intro; the row occurs twice, identical
52 | m02-l07-q303 | no | sldx — Diapositiva de Microsoft PowerPoint | excerpt is the list intro; the row occurs twice, identical
53 | m02-l07-q311 | yes | | excerpt glues the section intro to the row
54 | m02-l07-q315 | no | Tecla Windows + I — Abrir configuración. | excerpt is the section intro; the row occurs twice (Windows 11 and 10), identical
55 | m02-l08-q143 | no | none: not on page in usable form — the only route is the garbled five-word list item «Vaya aPersonalizar cintade opciones>de archivo>.», which never names Opciones | excerpt is an unrelated paragraph
56 | m02-l08-q149 | no | none: spread — «seleccione Importar o exportar.» and «Seleccione Exportar todas las personalizaciones.» are two steps; excerpt shows only the first |
57 | m02-l08-q194 | no | none: spread — Archivo › Información, Comprobar si hay problemas and Comprobar accesibilidad are three separate steps | excerpt is page furniture («Se aplica a…»)
58 | m02-l08-q200 | no | none: no admissible label — the route is only the garbled four-word step «Seleccione Accesibilidaden Opciones>dearchivo>.» | excerpt is page furniture («Se aplica a…»)
59 | m02-l08-q219 | no | Sin embargo, la característica insertar texto de ejemplo está deshabilitada cuando la opción Reemplazar texto mientras escribe está desactivada. | excerpt is the page intro
60 | m02-l09-q060 | no | none: spread — pestaña Número, categoría Fecha and Tipo are three separate steps; excerpt shows only the Tipo step |

## Counts

- items: 60
- yes: 8
- no with a label: 33
- no with none: 19
  - spread: 13 (3, 5, 6, 16, 17, 18, 37, 39, 41, 43, 56, 57, 60)
  - heading only: 1 (34)
  - not on page in usable form: 1 (55)
  - no admissible label (fact only in a short or unpunctuated fragment): 4 (29, 36, 38, 58)
