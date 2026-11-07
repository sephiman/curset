# Lectura de tablas (`tablas-lectura`) — 50 goldens

Generated items for the blind review (ambiguity, realism, key). Each is `seed`, difficulty level, stem, options in the order shown, the key the solver computes and the explanation shown after answering. Regenerate with `uv run python scripts/export_psicotecnico_goldens.py`.

## 1. seed 274797139979144773 · nivel 2

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Segovia | Naturaleza | Tren | 57 | 77 | 29 | 186 |
| Teruel | Deportiva | Minibús | 52 | 95 | 24 | 308 |
| Ronda | Cultural | Autobús | 21 | 72 | 18 | 99 |
| Jaca | Naturaleza | Minibús | 16 | 51 | 21 | 277 |
| Úbeda | Gastronómica | Tren | 41 | 93 | 5 | 344 |
| Lugo | Cultural | Autobús | 35 | 49 | 14 | 293 |
| Cuenca | Naturaleza | Autobús | 50 | 53 | 29 | 384 |
| Toledo | Cultural | Minibús | 28 | 47 | 5 | 76 |
| Mérida | Naturaleza | Autobús | 42 | 66 | 20 | 267 |
| León | Gastronómica | Tren | 44 | 65 | 19 | 40 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuál es el total de duración de los destinos que cumplen estas condiciones: precio por persona inferior a 55 y menos de 336 kilómetros?

a) 40
b) 45
c) 48
d) 35

**Clave: a**

Explicación: Pasan el filtro 3 filas; en ellas, la columna «Duración (horas)» suma 40.

## 2. seed 3493489528897654557 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Iota | Valencia | Pública | 790 | 6 | 198 | 64 |
| Beta | Barcelona | Mixta | 758 | 18 | 387 | 265 |
| Omega | Bilbao | Mixta | 306 | 6 | 131 | 44 |
| Gamma | Valencia | Mixta | 374 | 15 | 372 | 34 |
| Sigma | Bilbao | Pública | 749 | 15 | 93 | 83 |
| Kappa | Sevilla | Mixta | 482 | 7 | 394 | 199 |
| Theta | Sevilla | Privada | 915 | 15 | 340 | 86 |
| Alfa | Madrid | Privada | 227 | 16 | 109 | 194 |
| Lambda | Barcelona | Mixta | 322 | 12 | 138 | 229 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuál es el total de técnicos de los laboratorios que cumplen estas condiciones: menos de 62 informes emitidos y titularidad «Mixta»?

a) 25
b) 27
c) 21
d) 24

**Clave: c**

Explicación: Pasan el filtro 2 filas; en ellas, la columna «Técnicos» suma 21.

## 3. seed 3888289725752918728 · nivel 1

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Irene Pons | Sevilla | Tren | 589 | 168 | 100 | 8 |
| Ana Cortés | Sevilla | Coche | 689 | 413 | 158 | 3 |
| Marta Ríos | Bilbao | Coche | 833 | 476 | 225 | 12 |
| Diego Rubio | Valencia | Autobús | 424 | 358 | 25 | 2 |
| Paula Giner | Bilbao | Tren | 92 | 51 | 17 | 3 |
| Lucía Costa | Madrid | Avión | 533 | 103 | 133 | 12 |
| Rocío Mora | Barcelona | Tren | 698 | 399 | 105 | 7 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Qué empleado tiene el menor cociente entre distancia y tiempo?

a) Rocío Mora.
b) Marta Ríos.
c) Diego Rubio.
d) Irene Pons.

**Clave: c**

Explicación: Se divide distancia entre tiempo en cada fila: el menor cociente es el de «Diego Rubio» (1,18).

## 4. seed 679292652377546788 · nivel 2

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Iván Duarte | Inglés | Tarde | 30 | 10 | 93 | 15 |
| Víctor Ibarra | Informática | Mañana | 53 | 3 | 56 | 2 |
| Jorge Luna | Francés | Noche | 27 | 5 | 66 | 13 |
| Rocío Mora | Inglés | Noche | 40 | 2 | 88 | 0 |
| Raúl Mena | Alemán | Mañana | 43 | 11 | 108 | 8 |
| Nuria Salas | Alemán | Mañana | 37 | 9 | 87 | 3 |
| Marta Ríos | Informática | Mañana | 37 | 6 | 103 | 12 |
| Pablo Vera | Francés | Noche | 23 | 10 | 47 | 8 |
| Ana Cortés | Alemán | Tarde | 45 | 3 | 42 | 15 |
| Irene Pons | Informática | Tarde | 33 | 4 | 57 | 3 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Cuántos alumnos cumplen estas condiciones: más de 2 horas semanales y más de 14 faltas de asistencia?

a) 3
b) 0
c) 2
d) 5

**Clave: c**

Explicación: Cumplen las condiciones (más de 2 horas semanales y más de 14 faltas de asistencia) exactamente 2.

## 5. seed 2618344893097292910 · nivel 2

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Rocío Mora | Barcelona | Coche | 589 | 406 | 147 | 9 |
| Raúl Mena | Valencia | Coche | 510 | 364 | 143 | 6 |
| Carla Nieto | Valencia | Coche | 705 | 572 | 162 | 11 |
| Víctor Ibarra | Sevilla | Autobús | 301 | 235 | 15 | 7 |
| Hugo Beltrán | Valencia | Tren | 741 | 412 | 104 | 5 |
| Pablo Vera | Madrid | Tren | 397 | 170 | 52 | 13 |
| Andrés Peña | Barcelona | Avión | 563 | 64 | 118 | 8 |
| Nuria Salas | Bilbao | Avión | 471 | 57 | 61 | 8 |
| Irene Pons | Sevilla | Tren | 480 | 217 | 67 | 6 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Cuántos empleados cumplen estas condiciones: más de 5 viajes al año y medio «Coche»?

a) 6
b) 2
c) 3
d) 4

**Clave: c**

Explicación: Cumplen las condiciones (más de 5 viajes al año y medio «Coche») exactamente 3.

## 6. seed 995660733233502469 · nivel 2

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Diego Rubio | Francés | Tarde | 47 | 4 | 96 | 4 |
| Luis Parra | Francés | Noche | 44 | 5 | 40 | 8 |
| Óscar Lara | Alemán | Tarde | 46 | 8 | 47 | 6 |
| Iván Duarte | Informática | Mañana | 34 | 12 | 72 | 2 |
| Raúl Mena | Francés | Tarde | 47 | 4 | 108 | 15 |
| Víctor Ibarra | Inglés | Tarde | 32 | 6 | 42 | 4 |
| Pablo Vera | Inglés | Tarde | 38 | 3 | 46 | 12 |
| Nuria Salas | Alemán | Noche | 41 | 5 | 81 | 3 |
| Paula Giner | Alemán | Noche | 19 | 4 | 44 | 8 |
| Andrés Peña | Informática | Noche | 55 | 10 | 103 | 6 |

Responda a la siguiente pregunta según la tabla llamada Academia: Sumando horas semanales por curso, ¿qué curso obtiene el menor total?

a) Francés.
b) Alemán.
c) Informática.
d) Inglés.

**Clave: d**

Explicación: Los valores por curso son Alemán 17, Francés 13, Informática 22, Inglés 9; el menor es Inglés.

## 7. seed 1223983771725134866 · nivel 2

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Rocío Mora | Inglés | Noche | 39 | 7 | 69 | 5 |
| Carla Nieto | Francés | Tarde | 22 | 10 | 86 | 13 |
| Pablo Vera | Informática | Tarde | 54 | 3 | 120 | 8 |
| Víctor Ibarra | Informática | Tarde | 55 | 10 | 41 | 11 |
| Marta Ríos | Informática | Noche | 51 | 4 | 62 | 12 |
| Iván Duarte | Francés | Noche | 19 | 5 | 32 | 6 |
| Elena Soler | Inglés | Mañana | 29 | 4 | 60 | 15 |
| Luis Parra | Alemán | Mañana | 20 | 8 | 95 | 15 |
| Sara Ortiz | Alemán | Mañana | 41 | 11 | 87 | 1 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Qué alumno tiene el mayor cociente entre cuota mensual y horas semanales?

a) Pablo Vera.
b) Rocío Mora.
c) Marta Ríos.
d) Luis Parra.

**Clave: a**

Explicación: Se divide cuota mensual entre horas semanales en cada fila: el mayor cociente es el de «Pablo Vera» (40,00).

## 8. seed 4580581082989247247 · nivel 2

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Irene Pons | Sevilla | Tren | 612 | 168 | 98 | 10 |
| Pablo Vera | Bilbao | Avión | 459 | 58 | 106 | 5 |
| Ana Cortés | Barcelona | Avión | 648 | 94 | 156 | 1 |
| Luis Parra | Madrid | Avión | 350 | 39 | 66 | 4 |
| Rocío Mora | Valencia | Coche | 747 | 439 | 187 | 14 |
| Elena Soler | Sevilla | Autobús | 187 | 158 | 9 | 3 |
| Sara Ortiz | Sevilla | Avión | 772 | 129 | 100 | 12 |
| Nuria Salas | Sevilla | Coche | 358 | 219 | 86 | 6 |
| Marta Ríos | Barcelona | Autobús | 767 | 742 | 69 | 8 |
| Hugo Beltrán | Valencia | Autobús | 152 | 105 | 9 | 14 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Qué empleado tiene el menor cociente entre distancia y tiempo?

a) Irene Pons.
b) Rocío Mora.
c) Marta Ríos.
d) Sara Ortiz.

**Clave: c**

Explicación: Se divide distancia entre tiempo en cada fila: el menor cociente es el de «Marta Ríos» (1,03).

## 9. seed 3910380554785824084 · nivel 1

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Soria | Gastronómica | Minibús | 19 | 76 | 19 | 249 |
| Teruel | Cultural | Tren | 13 | 64 | 21 | 108 |
| Jaca | Naturaleza | Autobús | 50 | 95 | 8 | 478 |
| Toledo | Naturaleza | Tren | 35 | 95 | 16 | 323 |
| León | Cultural | Autobús | 54 | 29 | 7 | 178 |
| Ronda | Deportiva | Minibús | 27 | 87 | 5 | 406 |
| Mérida | Cultural | Autobús | 53 | 50 | 8 | 127 |
| Segovia | Deportiva | Minibús | 34 | 17 | 7 | 123 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: Entre los destinos que cumplen esta condición: transporte «Autobús», ¿cuál tiene el valor más bajo de precio por persona?

a) Teruel.
b) Mérida.
c) Toledo.
d) León.

**Clave: d**

Explicación: Pasan el filtro 3 destinos; entre ellos, «León» tiene el valor más bajo de precio por persona.

## 10. seed 4441628925242482318 · nivel 2

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Pablo Vera | Valencia | Avión | 761 | 83 | 76 | 7 |
| Irene Pons | Bilbao | Coche | 185 | 129 | 41 | 7 |
| Iván Duarte | Sevilla | Autobús | 840 | 840 | 50 | 3 |
| Jorge Luna | Valencia | Avión | 373 | 50 | 90 | 8 |
| Diego Rubio | Madrid | Tren | 121 | 46 | 22 | 3 |
| Sara Ortiz | Sevilla | Avión | 723 | 69 | 159 | 7 |
| Nuria Salas | Madrid | Coche | 627 | 358 | 138 | 8 |
| Ana Cortés | Sevilla | Avión | 384 | 64 | 77 | 2 |
| Raúl Mena | Barcelona | Avión | 691 | 115 | 69 | 8 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Cuál de los siguientes empleados cumple estas condiciones: menos de 3 viajes al año, medio «Avión» y distancia superior a 295?

a) Pablo Vera.
b) Jorge Luna.
c) Ana Cortés.
d) Sara Ortiz.

**Clave: c**

Explicación: Solo «Ana Cortés» cumple las 3 condiciones: menos de 3 viajes al año, medio «Avión» y distancia superior a 295.

## 11. seed 2446871128147784257 · nivel 2

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Teruel | Deportiva | Autobús | 35 | 78 | 4 | 48 |
| Jaca | Naturaleza | Tren | 51 | 68 | 24 | 64 |
| Ronda | Naturaleza | Tren | 15 | 54 | 30 | 256 |
| Úbeda | Cultural | Autobús | 37 | 46 | 12 | 59 |
| Mérida | Gastronómica | Tren | 19 | 37 | 14 | 331 |
| Cuenca | Deportiva | Autobús | 18 | 85 | 12 | 340 |
| Lugo | Deportiva | Minibús | 19 | 89 | 12 | 242 |
| Soria | Gastronómica | Tren | 51 | 62 | 28 | 365 |
| Segovia | Cultural | Minibús | 55 | 73 | 24 | 293 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuántos destinos cumplen estas condiciones: precio por persona superior a 79 y tipo «Deportiva»?

a) 1
b) 5
c) 2
d) 0

**Clave: c**

Explicación: Cumplen las condiciones (precio por persona superior a 79 y tipo «Deportiva») exactamente 2.

## 12. seed 3654112830433712182 · nivel 1

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Víctor Ibarra | Inglés | Noche | 21 | 6 | 60 | 12 |
| Andrés Peña | Alemán | Mañana | 27 | 3 | 51 | 7 |
| Carla Nieto | Francés | Tarde | 45 | 3 | 71 | 5 |
| Pablo Vera | Alemán | Noche | 40 | 6 | 64 | 8 |
| Hugo Beltrán | Francés | Tarde | 50 | 3 | 95 | 11 |
| Diego Rubio | Inglés | Noche | 51 | 7 | 78 | 0 |
| Óscar Lara | Informática | Tarde | 44 | 11 | 33 | 6 |
| Ana Cortés | Informática | Noche | 38 | 7 | 89 | 1 |

Responda a la siguiente pregunta según la tabla llamada Academia: Entre los alumnos que cumplen esta condición: menos de 7 faltas de asistencia, ¿cuál tiene el valor más alto de edad?

a) Andrés Peña.
b) Diego Rubio.
c) Víctor Ibarra.
d) Carla Nieto.

**Clave: b**

Explicación: Pasan el filtro 4 alumnos; entre ellos, «Diego Rubio» tiene el valor más alto de edad.

## 13. seed 327284621952842892 · nivel 3

Tabla «Préstamos»:

| Título | Lugar de edición | Editorial | Año de publicación | Ejemplares disponibles | Ejemplares prestados | Préstamos realizados |
|---|---|---|---|---|---|---|
| Tiempo de ceniza | Madrid | Alfaguara | 1996 | 8 | 8 | 224 |
| El jardín cerrado | Madrid | Alfaguara | 2000 | 9 | 9 | 179 |
| El amante lesbiano | Barcelona | Anagrama | 2001 | 18 | 3 | 113 |
| La isla vacía | Valencia | Planeta | 2005 | 16 | 3 | 165 |
| La temporada de caza | Sevilla | Santillana | 1999 | 7 | 6 | 118 |
| Adiós a las novias | Madrid | Planeta | 2003 | 5 | 4 | 220 |
| Noches de invierno | Sevilla | Destino | 1996 | 16 | 4 | 117 |
| El último tren | Barcelona | Alfaguara | 2002 | 13 | 2 | 167 |
| Los días azules | Madrid | Anagrama | 2003 | 16 | 8 | 217 |
| Entre visillos | Valencia | Planeta | 2000 | 9 | 8 | 334 |
| Contra vosotros | Madrid | Alfaguara | 2002 | 13 | 1 | 291 |

Responda a la siguiente pregunta según la tabla llamada Préstamos: ¿Cuál es la media de ejemplares prestados de todos los títulos?

a) 5,09
b) 7,09
c) 5,60
d) 4,00

**Clave: a**

Explicación: La suma de la columna es 56,00 y hay 11 filas: 5,09.

## 14. seed 3262813409570128271 · nivel 1

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Delta | Sevilla | Privada | 150 | 4 | 244 | 278 |
| Lambda | Barcelona | Mixta | 455 | 6 | 342 | 260 |
| Omega | Valencia | Privada | 798 | 14 | 259 | 34 |
| Iota | Madrid | Mixta | 201 | 11 | 355 | 158 |
| Kappa | Valencia | Privada | 567 | 11 | 374 | 219 |
| Zeta | Sevilla | Privada | 718 | 21 | 289 | 289 |
| Theta | Bilbao | Pública | 477 | 20 | 400 | 184 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuál de los siguientes laboratorios cumple estas condiciones: más de 717 muestras analizadas, menos de 65 informes emitidos y titularidad «Privada»?

a) Kappa.
b) Delta.
c) Theta.
d) Omega.

**Clave: d**

Explicación: Solo «Omega» cumple las 3 condiciones: más de 717 muestras analizadas, menos de 65 informes emitidos y titularidad «Privada».

## 15. seed 1574408861979755188 · nivel 1

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Lugo | Cultural | Tren | 50 | 76 | 26 | 477 |
| Cuenca | Gastronómica | Autobús | 12 | 69 | 4 | 358 |
| Soria | Deportiva | Minibús | 40 | 30 | 10 | 322 |
| Ronda | Cultural | Tren | 16 | 20 | 7 | 283 |
| Mérida | Gastronómica | Minibús | 59 | 69 | 17 | 228 |
| Úbeda | Naturaleza | Minibús | 60 | 19 | 13 | 480 |
| Toledo | Naturaleza | Autobús | 41 | 33 | 9 | 145 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuál de los siguientes destinos cumple estas condiciones: más de 436 kilómetros, precio por persona superior a 69 y tipo «Cultural»?

a) Soria.
b) Mérida.
c) Lugo.
d) Úbeda.

**Clave: c**

Explicación: Solo «Lugo» cumple las 3 condiciones: más de 436 kilómetros, precio por persona superior a 69 y tipo «Cultural».

## 16. seed 2074564667347024303 · nivel 1

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Carla Nieto | Sevilla | Coche | 690 | 583 | 166 | 13 |
| Marta Ríos | Barcelona | Avión | 697 | 76 | 118 | 2 |
| Andrés Peña | Valencia | Tren | 754 | 353 | 121 | 8 |
| Víctor Ibarra | Valencia | Autobús | 724 | 511 | 58 | 9 |
| Lucía Costa | Madrid | Coche | 348 | 207 | 87 | 14 |
| Nuria Salas | Bilbao | Coche | 275 | 209 | 63 | 12 |
| Raúl Mena | Barcelona | Tren | 853 | 277 | 68 | 6 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Cuál de los siguientes empleados cumple estas condiciones: medio «Coche», distancia superior a 618 y más de 12 viajes al año?

a) Andrés Peña.
b) Carla Nieto.
c) Nuria Salas.
d) Lucía Costa.

**Clave: b**

Explicación: Solo «Carla Nieto» cumple las 3 condiciones: medio «Coche», distancia superior a 618 y más de 12 viajes al año.

## 17. seed 1580329207806355028 · nivel 1

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Lucía Costa | Alemán | Mañana | 34 | 4 | 85 | 10 |
| Jorge Luna | Alemán | Mañana | 47 | 2 | 76 | 0 |
| Iván Duarte | Francés | Tarde | 36 | 11 | 79 | 4 |
| Nuria Salas | Alemán | Noche | 54 | 9 | 39 | 8 |
| Sara Ortiz | Inglés | Tarde | 44 | 2 | 120 | 15 |
| Óscar Lara | Francés | Mañana | 21 | 5 | 70 | 2 |
| Marta Ríos | Informática | Tarde | 32 | 4 | 45 | 12 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Cuál de los siguientes alumnos cumple estas condiciones: menos de 3 horas semanales y más de 14 faltas de asistencia?

a) Jorge Luna.
b) Óscar Lara.
c) Sara Ortiz.
d) Marta Ríos.

**Clave: c**

Explicación: Solo «Sara Ortiz» cumple las 2 condiciones: menos de 3 horas semanales y más de 14 faltas de asistencia.

## 18. seed 4157976482641714332 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Kappa | Sevilla | Mixta | 261 | 4 | 130 | 203 |
| Iota | Sevilla | Privada | 890 | 17 | 131 | 59 |
| Delta | Madrid | Pública | 962 | 18 | 339 | 44 |
| Theta | Barcelona | Mixta | 183 | 8 | 109 | 102 |
| Beta | Sevilla | Privada | 775 | 12 | 345 | 117 |
| Épsilon | Barcelona | Privada | 778 | 3 | 196 | 157 |
| Sigma | Bilbao | Mixta | 922 | 18 | 212 | 132 |
| Gamma | Valencia | Mixta | 412 | 9 | 369 | 38 |
| Lambda | Valencia | Privada | 835 | 16 | 50 | 299 |
| Omega | Bilbao | Mixta | 963 | 17 | 68 | 47 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuántos laboratorios cumplen estas condiciones: presupuesto inferior a 169, menos de 235 informes emitidos y ciudad «Sevilla»?

a) 0
b) 2
c) 5
d) 3

**Clave: b**

Explicación: Cumplen las condiciones (presupuesto inferior a 169, menos de 235 informes emitidos y ciudad «Sevilla») exactamente 2.

## 19. seed 345352013983549247 · nivel 2

Tabla «Préstamos»:

| Título | Lugar de edición | Editorial | Año de publicación | Ejemplares disponibles | Ejemplares prestados | Préstamos realizados |
|---|---|---|---|---|---|---|
| La temporada de caza | Madrid | Santillana | 1995 | 11 | 7 | 165 |
| Hija de la fortuna | Barcelona | Santillana | 1996 | 5 | 2 | 309 |
| Los días azules | Madrid | Alfaguara | 2003 | 12 | 6 | 245 |
| El equipaje del viajero | Madrid | Anagrama | 2004 | 18 | 7 | 330 |
| Tiempo de ceniza | Sevilla | Planeta | 1998 | 6 | 7 | 298 |
| Cuaderno de bitácora | Sevilla | Alfaguara | 1996 | 9 | 5 | 172 |
| Contra vosotros | Barcelona | Planeta | 2003 | 16 | 2 | 186 |
| Un calor tan cercano | Valencia | Anagrama | 1996 | 5 | 5 | 153 |
| El amante lesbiano | Madrid | Destino | 2002 | 18 | 8 | 278 |

Responda a la siguiente pregunta según la tabla llamada Préstamos: ¿Cuál es el total de préstamos realizados de los títulos que cumplen estas condiciones: menos de 3 ejemplares prestados y lugar de edición «Barcelona»?

a) 416
b) 495
c) 634
d) 660

**Clave: b**

Explicación: Pasan el filtro 2 filas; en ellas, la columna «Préstamos realizados» suma 495.

## 20. seed 3725810980475735155 · nivel 1

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Iván Duarte | Informática | Tarde | 40 | 3 | 44 | 7 |
| Carla Nieto | Francés | Noche | 19 | 8 | 41 | 0 |
| Diego Rubio | Alemán | Noche | 49 | 11 | 35 | 11 |
| Raúl Mena | Informática | Mañana | 22 | 9 | 97 | 8 |
| Paula Giner | Inglés | Tarde | 34 | 7 | 48 | 12 |
| Marta Ríos | Francés | Tarde | 51 | 6 | 52 | 5 |
| Irene Pons | Inglés | Mañana | 40 | 10 | 61 | 1 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Cuál de los siguientes alumnos cumple estas condiciones: menos de 12 faltas de asistencia, edad superior a 45 y curso «Alemán»?

a) Diego Rubio.
b) Iván Duarte.
c) Paula Giner.
d) Carla Nieto.

**Clave: a**

Explicación: Solo «Diego Rubio» cumple las 3 condiciones: menos de 12 faltas de asistencia, edad superior a 45 y curso «Alemán».

## 21. seed 3689692058427482923 · nivel 1

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Carla Nieto | Bilbao | Coche | 278 | 174 | 83 | 6 |
| Sara Ortiz | Barcelona | Tren | 213 | 61 | 21 | 6 |
| Pablo Vera | Barcelona | Autobús | 340 | 279 | 31 | 10 |
| Víctor Ibarra | Madrid | Avión | 350 | 34 | 42 | 14 |
| Luis Parra | Valencia | Coche | 606 | 449 | 133 | 5 |
| Jorge Luna | Sevilla | Tren | 94 | 44 | 17 | 3 |
| Rocío Mora | Bilbao | Coche | 568 | 337 | 142 | 6 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Cuántos empleados cumplen estas condiciones: tiempo inferior a 225 y distancia inferior a 342?

a) 4
b) 3
c) 2
d) 5

**Clave: b**

Explicación: Cumplen las condiciones (tiempo inferior a 225 y distancia inferior a 342) exactamente 3.

## 22. seed 549857973036573262 · nivel 2

Tabla «Préstamos»:

| Título | Lugar de edición | Editorial | Año de publicación | Ejemplares disponibles | Ejemplares prestados | Préstamos realizados |
|---|---|---|---|---|---|---|
| El amante lesbiano | Madrid | Planeta | 1999 | 14 | 1 | 119 |
| La temporada de caza | Sevilla | Santillana | 1999 | 7 | 9 | 275 |
| La casa del lago | Sevilla | Alfaguara | 2002 | 11 | 3 | 135 |
| Aranmanoth | Valencia | Santillana | 2003 | 3 | 2 | 299 |
| El último tren | Barcelona | Alfaguara | 1996 | 16 | 1 | 183 |
| La isla vacía | Madrid | Santillana | 2004 | 4 | 4 | 226 |
| El jardín cerrado | Valencia | Planeta | 1998 | 8 | 7 | 263 |
| Hija de la fortuna | Valencia | Destino | 1997 | 11 | 7 | 154 |
| Contra vosotros | Madrid | Anagrama | 1999 | 12 | 4 | 283 |
| Tiempo de ceniza | Sevilla | Anagrama | 1995 | 16 | 5 | 273 |

Responda a la siguiente pregunta según la tabla llamada Préstamos: ¿Cuál de los siguientes títulos cumple estas condiciones: más de 277 préstamos realizados, lugar de edición «Valencia», editorial «Santillana» y menos de 4 ejemplares disponibles?

a) La isla vacía.
b) Contra vosotros.
c) Hija de la fortuna.
d) Aranmanoth.

**Clave: d**

Explicación: Solo «Aranmanoth» cumple las 4 condiciones: más de 277 préstamos realizados, lugar de edición «Valencia», editorial «Santillana» y menos de 4 ejemplares disponibles.

## 23. seed 3911690445701389361 · nivel 1

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Pablo Vera | Alemán | Mañana | 23 | 9 | 96 | 4 |
| Andrés Peña | Francés | Mañana | 36 | 11 | 113 | 14 |
| Marta Ríos | Inglés | Mañana | 24 | 5 | 119 | 6 |
| Óscar Lara | Francés | Noche | 24 | 9 | 59 | 0 |
| Irene Pons | Alemán | Tarde | 43 | 9 | 120 | 9 |
| Lucía Costa | Francés | Tarde | 19 | 9 | 120 | 15 |
| Raúl Mena | Informática | Tarde | 42 | 10 | 108 | 15 |
| Iván Duarte | Inglés | Tarde | 44 | 12 | 57 | 10 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Cuántos alumnos cumplen estas condiciones: curso «Alemán» y menos de 10 horas semanales?

a) 1
b) 0
c) 2
d) 3

**Clave: c**

Explicación: Cumplen las condiciones (curso «Alemán» y menos de 10 horas semanales) exactamente 2.

## 24. seed 4092711762427273095 · nivel 3

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Irene Pons | Inglés | Mañana | 29 | 12 | 41 | 4 |
| Iván Duarte | Inglés | Mañana | 19 | 8 | 64 | 11 |
| Lucía Costa | Alemán | Mañana | 44 | 6 | 57 | 3 |
| Elena Soler | Inglés | Noche | 33 | 10 | 48 | 7 |
| Víctor Ibarra | Inglés | Tarde | 37 | 5 | 83 | 2 |
| Pablo Vera | Alemán | Noche | 51 | 7 | 61 | 7 |
| Ana Cortés | Inglés | Tarde | 37 | 8 | 79 | 8 |
| Nuria Salas | Alemán | Tarde | 34 | 10 | 93 | 9 |
| Raúl Mena | Francés | Tarde | 21 | 11 | 90 | 12 |
| Hugo Beltrán | Francés | Noche | 46 | 11 | 89 | 3 |
| Andrés Peña | Informática | Mañana | 28 | 7 | 91 | 4 |
| Óscar Lara | Francés | Tarde | 28 | 9 | 69 | 6 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Qué porcentaje del total de horas semanales corresponde a los alumnos con turno «Noche»?

a) 26,92 %
b) 25,85 %
c) 25,00 %
d) 34,46 %

**Clave: a**

Explicación: Los alumnos con turno «Noche» suman 28 de un total de 104: 26,92 %.

## 25. seed 2736979108388417725 · nivel 2

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Andrés Peña | Informática | Noche | 40 | 9 | 109 | 14 |
| Víctor Ibarra | Informática | Mañana | 51 | 12 | 83 | 15 |
| Nuria Salas | Alemán | Mañana | 43 | 5 | 69 | 12 |
| Lucía Costa | Alemán | Tarde | 45 | 10 | 83 | 7 |
| Raúl Mena | Alemán | Noche | 42 | 11 | 66 | 11 |
| Óscar Lara | Informática | Tarde | 54 | 8 | 111 | 13 |
| Elena Soler | Francés | Noche | 45 | 8 | 78 | 15 |
| Ana Cortés | Informática | Noche | 43 | 12 | 35 | 0 |
| Marta Ríos | Inglés | Mañana | 47 | 12 | 33 | 7 |
| Jorge Luna | Informática | Mañana | 37 | 7 | 120 | 3 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Cuál es el total de horas semanales de los alumnos que cumplen estas condiciones: curso «Alemán» y cuota mensual inferior a 76?

a) 19
b) 16
c) 12
d) 18

**Clave: b**

Explicación: Pasan el filtro 2 filas; en ellas, la columna «Horas semanales» suma 16.

## 26. seed 4163390447536696390 · nivel 1

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Diego Rubio | Inglés | Tarde | 26 | 12 | 116 | 5 |
| Óscar Lara | Inglés | Mañana | 54 | 10 | 44 | 15 |
| Rocío Mora | Informática | Tarde | 49 | 7 | 120 | 14 |
| Elena Soler | Informática | Noche | 46 | 7 | 45 | 13 |
| Sara Ortiz | Alemán | Noche | 37 | 2 | 120 | 10 |
| Lucía Costa | Alemán | Mañana | 20 | 11 | 89 | 7 |
| Hugo Beltrán | Francés | Tarde | 34 | 7 | 30 | 8 |
| Andrés Peña | Francés | Tarde | 31 | 7 | 89 | 4 |

Responda a la siguiente pregunta según la tabla llamada Academia: Entre los alumnos que cumplen esta condición: edad inferior a 35, ¿cuál tiene el valor más alto de cuota mensual?

a) Andrés Peña.
b) Diego Rubio.
c) Lucía Costa.
d) Elena Soler.

**Clave: b**

Explicación: Pasan el filtro 4 alumnos; entre ellos, «Diego Rubio» tiene el valor más alto de cuota mensual.

## 27. seed 1586508015396871889 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Iota | Valencia | Mixta | 324 | 12 | 385 | 34 |
| Épsilon | Sevilla | Mixta | 230 | 18 | 284 | 127 |
| Sigma | Barcelona | Privada | 304 | 16 | 375 | 48 |
| Gamma | Barcelona | Mixta | 511 | 20 | 321 | 127 |
| Beta | Madrid | Mixta | 512 | 22 | 190 | 124 |
| Theta | Madrid | Pública | 835 | 9 | 261 | 63 |
| Alfa | Bilbao | Privada | 947 | 3 | 236 | 116 |
| Lambda | Sevilla | Mixta | 214 | 4 | 77 | 213 |
| Omega | Sevilla | Mixta | 690 | 20 | 160 | 291 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Qué laboratorio tiene el mayor cociente entre presupuesto y técnicos?

a) Alfa.
b) Theta.
c) Épsilon.
d) Gamma.

**Clave: a**

Explicación: Se divide presupuesto entre técnicos en cada fila: el mayor cociente es el de «Alfa» (78,67).

## 28. seed 3588842099432019975 · nivel 2

Tabla «Préstamos»:

| Título | Lugar de edición | Editorial | Año de publicación | Ejemplares disponibles | Ejemplares prestados | Préstamos realizados |
|---|---|---|---|---|---|---|
| Entre visillos | Barcelona | Destino | 2001 | 5 | 3 | 281 |
| El amante lesbiano | Sevilla | Alfaguara | 1996 | 19 | 2 | 168 |
| Tiempo de ceniza | Madrid | Anagrama | 2004 | 10 | 7 | 161 |
| Mano de sombra | Barcelona | Planeta | 1996 | 6 | 3 | 191 |
| Hija de la fortuna | Valencia | Destino | 1997 | 19 | 2 | 276 |
| La casa del lago | Barcelona | Santillana | 2000 | 14 | 8 | 104 |
| El último tren | Madrid | Planeta | 2003 | 6 | 1 | 260 |
| Los días azules | Valencia | Planeta | 1997 | 3 | 1 | 262 |
| La isla vacía | Sevilla | Planeta | 1999 | 6 | 3 | 158 |

Responda a la siguiente pregunta según la tabla llamada Préstamos: Sumando préstamos realizados por lugar de edición, ¿qué lugar de edición obtiene el menor total?

a) Sevilla.
b) Madrid.
c) Barcelona.
d) Valencia.

**Clave: a**

Explicación: Los valores por lugar de edición son Barcelona 576, Madrid 421, Sevilla 326, Valencia 538; el menor es Sevilla.

## 29. seed 4110580552696902388 · nivel 2

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Andrés Peña | Alemán | Tarde | 38 | 12 | 72 | 9 |
| Víctor Ibarra | Informática | Tarde | 51 | 12 | 76 | 9 |
| Hugo Beltrán | Inglés | Mañana | 47 | 12 | 70 | 14 |
| Elena Soler | Informática | Noche | 31 | 8 | 63 | 12 |
| Diego Rubio | Francés | Tarde | 32 | 9 | 95 | 8 |
| Irene Pons | Inglés | Noche | 48 | 12 | 81 | 5 |
| Lucía Costa | Francés | Tarde | 38 | 7 | 62 | 2 |
| Carla Nieto | Alemán | Mañana | 36 | 7 | 44 | 9 |
| Rocío Mora | Alemán | Mañana | 52 | 9 | 83 | 13 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Cuántos alumnos cumplen estas condiciones: edad inferior a 33, más de 7 horas semanales y menos de 13 faltas de asistencia?

a) 4
b) 5
c) 1
d) 2

**Clave: d**

Explicación: Cumplen las condiciones (edad inferior a 33, más de 7 horas semanales y menos de 13 faltas de asistencia) exactamente 2.

## 30. seed 3556477018594785593 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Delta | Valencia | Pública | 287 | 17 | 260 | 122 |
| Omega | Barcelona | Privada | 881 | 20 | 79 | 143 |
| Beta | Barcelona | Pública | 768 | 3 | 148 | 246 |
| Iota | Madrid | Mixta | 860 | 7 | 355 | 250 |
| Sigma | Bilbao | Privada | 616 | 4 | 352 | 37 |
| Theta | Sevilla | Mixta | 793 | 12 | 199 | 121 |
| Zeta | Barcelona | Mixta | 721 | 11 | 290 | 241 |
| Kappa | Bilbao | Pública | 730 | 23 | 62 | 83 |
| Épsilon | Sevilla | Pública | 978 | 14 | 283 | 209 |
| Alfa | Bilbao | Privada | 454 | 4 | 351 | 228 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuántos laboratorios cumplen estas condiciones: titularidad «Mixta» y presupuesto superior a 254?

a) 5
b) 1
c) 2
d) 3

**Clave: c**

Explicación: Cumplen las condiciones (titularidad «Mixta» y presupuesto superior a 254) exactamente 2.

## 31. seed 2381850757681049524 · nivel 2

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Mérida | Deportiva | Tren | 29 | 55 | 14 | 312 |
| Jaca | Naturaleza | Tren | 49 | 72 | 20 | 108 |
| León | Gastronómica | Minibús | 12 | 55 | 30 | 299 |
| Úbeda | Gastronómica | Minibús | 39 | 69 | 15 | 138 |
| Segovia | Naturaleza | Autobús | 60 | 27 | 10 | 380 |
| Cuenca | Gastronómica | Tren | 18 | 53 | 27 | 332 |
| Ronda | Deportiva | Autobús | 36 | 79 | 15 | 138 |
| Lugo | Deportiva | Tren | 46 | 23 | 28 | 93 |
| Teruel | Cultural | Minibús | 23 | 66 | 9 | 182 |
| Ávila | Gastronómica | Minibús | 42 | 28 | 15 | 327 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuál de los siguientes destinos cumple estas condiciones: menos de 18 participantes, precio por persona superior a 48, transporte «Minibús» y menos de 334 kilómetros?

a) Ronda.
b) León.
c) Mérida.
d) Teruel.

**Clave: b**

Explicación: Solo «León» cumple las 4 condiciones: menos de 18 participantes, precio por persona superior a 48, transporte «Minibús» y menos de 334 kilómetros.

## 32. seed 3706174181096166754 · nivel 1

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Andrés Peña | Alemán | Noche | 43 | 7 | 95 | 8 |
| Lucía Costa | Informática | Tarde | 27 | 8 | 42 | 10 |
| Paula Giner | Francés | Noche | 55 | 8 | 109 | 1 |
| Luis Parra | Inglés | Tarde | 52 | 4 | 66 | 2 |
| Hugo Beltrán | Informática | Mañana | 41 | 2 | 41 | 9 |
| Diego Rubio | Inglés | Noche | 54 | 9 | 85 | 4 |
| Carla Nieto | Inglés | Mañana | 26 | 12 | 80 | 1 |
| Elena Soler | Alemán | Tarde | 44 | 7 | 68 | 11 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Qué alumno tiene el menor cociente entre faltas de asistencia y horas semanales?

a) Elena Soler.
b) Diego Rubio.
c) Andrés Peña.
d) Carla Nieto.

**Clave: d**

Explicación: Se divide faltas de asistencia entre horas semanales en cada fila: el menor cociente es el de «Carla Nieto» (0,083).

## 33. seed 3614112383633376201 · nivel 3

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Marta Ríos | Inglés | Tarde | 20 | 7 | 40 | 4 |
| Nuria Salas | Inglés | Mañana | 28 | 7 | 101 | 12 |
| Iván Duarte | Inglés | Mañana | 37 | 7 | 112 | 10 |
| Luis Parra | Informática | Mañana | 49 | 3 | 48 | 3 |
| Óscar Lara | Inglés | Mañana | 50 | 3 | 51 | 10 |
| Víctor Ibarra | Informática | Mañana | 41 | 4 | 65 | 4 |
| Sara Ortiz | Alemán | Mañana | 20 | 3 | 83 | 11 |
| Jorge Luna | Inglés | Tarde | 24 | 10 | 97 | 15 |
| Elena Soler | Inglés | Noche | 45 | 9 | 90 | 15 |
| Raúl Mena | Alemán | Tarde | 36 | 2 | 67 | 13 |
| Diego Rubio | Inglés | Tarde | 41 | 7 | 48 | 13 |
| Andrés Peña | Francés | Mañana | 37 | 10 | 43 | 1 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Cuál de los siguientes alumnos cumple estas condiciones: turno «Tarde», curso «Inglés», edad inferior a 23 y cuota mensual inferior a 49?

a) Luis Parra.
b) Marta Ríos.
c) Óscar Lara.
d) Jorge Luna.

**Clave: b**

Explicación: Solo «Marta Ríos» cumple las 4 condiciones: turno «Tarde», curso «Inglés», edad inferior a 23 y cuota mensual inferior a 49.

## 34. seed 1166747531291222478 · nivel 2

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Pablo Vera | Inglés | Noche | 47 | 3 | 93 | 6 |
| Andrés Peña | Alemán | Noche | 33 | 12 | 99 | 13 |
| Ana Cortés | Francés | Mañana | 27 | 5 | 83 | 5 |
| Paula Giner | Alemán | Noche | 36 | 10 | 54 | 7 |
| Iván Duarte | Inglés | Tarde | 51 | 10 | 94 | 8 |
| Irene Pons | Informática | Tarde | 52 | 4 | 82 | 5 |
| Carla Nieto | Alemán | Noche | 32 | 8 | 116 | 13 |
| Jorge Luna | Alemán | Noche | 40 | 8 | 118 | 12 |
| Diego Rubio | Inglés | Noche | 41 | 10 | 58 | 0 |
| Rocío Mora | Inglés | Noche | 36 | 8 | 70 | 0 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Cuántos alumnos cumplen estas condiciones: turno «Noche» y más de 6 faltas de asistencia?

a) 6
b) 4
c) 3
d) 7

**Clave: b**

Explicación: Cumplen las condiciones (turno «Noche» y más de 6 faltas de asistencia) exactamente 4.

## 35. seed 1690837818924781736 · nivel 2

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Lucía Costa | Madrid | Tren | 199 | 83 | 34 | 11 |
| Hugo Beltrán | Sevilla | Autobús | 335 | 223 | 20 | 6 |
| Diego Rubio | Barcelona | Autobús | 256 | 248 | 23 | 6 |
| Iván Duarte | Sevilla | Avión | 350 | 44 | 80 | 9 |
| Jorge Luna | Madrid | Avión | 782 | 115 | 188 | 8 |
| Pablo Vera | Bilbao | Coche | 213 | 130 | 45 | 2 |
| Andrés Peña | Barcelona | Autobús | 315 | 233 | 22 | 4 |
| Luis Parra | Madrid | Tren | 733 | 344 | 59 | 2 |
| Paula Giner | Barcelona | Coche | 321 | 203 | 83 | 5 |
| Ana Cortés | Valencia | Avión | 771 | 124 | 123 | 2 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Cuántos empleados cumplen estas condiciones: medio «Autobús» y más de 5 viajes al año?

a) 2
b) 0
c) 3
d) 5

**Clave: a**

Explicación: Cumplen las condiciones (medio «Autobús» y más de 5 viajes al año) exactamente 2.

## 36. seed 3525112190121478594 · nivel 1

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Lambda | Madrid | Privada | 481 | 4 | 296 | 49 |
| Gamma | Barcelona | Privada | 127 | 10 | 249 | 87 |
| Delta | Madrid | Mixta | 716 | 24 | 98 | 60 |
| Kappa | Bilbao | Pública | 653 | 16 | 341 | 224 |
| Zeta | Madrid | Pública | 285 | 18 | 300 | 142 |
| Sigma | Valencia | Pública | 369 | 9 | 398 | 255 |
| Épsilon | Sevilla | Pública | 170 | 24 | 55 | 295 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuál de los siguientes laboratorios cumple estas condiciones: más de 643 muestras analizadas, presupuesto superior a 56 y ciudad «Madrid»?

a) Gamma.
b) Sigma.
c) Delta.
d) Kappa.

**Clave: c**

Explicación: Solo «Delta» cumple las 3 condiciones: más de 643 muestras analizadas, presupuesto superior a 56 y ciudad «Madrid».

## 37. seed 778671632053513995 · nivel 1

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Cuenca | Cultural | Minibús | 49 | 21 | 19 | 116 |
| Ávila | Gastronómica | Tren | 49 | 67 | 18 | 351 |
| Segovia | Gastronómica | Tren | 53 | 60 | 9 | 268 |
| León | Gastronómica | Minibús | 13 | 59 | 30 | 268 |
| Toledo | Naturaleza | Autobús | 50 | 20 | 20 | 444 |
| Soria | Cultural | Autobús | 59 | 86 | 29 | 397 |
| Úbeda | Gastronómica | Minibús | 15 | 18 | 24 | 158 |
| Jaca | Deportiva | Autobús | 48 | 79 | 20 | 155 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuántos destinos cumplen estas condiciones: menos de 18 participantes, transporte «Minibús» y tipo «Gastronómica»?

a) 2
b) 3
c) 5
d) 4

**Clave: a**

Explicación: Cumplen las condiciones (menos de 18 participantes, transporte «Minibús» y tipo «Gastronómica») exactamente 2.

## 38. seed 232616239795612045 · nivel 2

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Nuria Salas | Barcelona | Tren | 510 | 214 | 61 | 6 |
| Ana Cortés | Barcelona | Autobús | 107 | 99 | 9 | 11 |
| Luis Parra | Bilbao | Tren | 104 | 41 | 8 | 12 |
| Marta Ríos | Valencia | Coche | 884 | 737 | 194 | 7 |
| Irene Pons | Valencia | Avión | 414 | 46 | 95 | 6 |
| Pablo Vera | Sevilla | Avión | 792 | 104 | 103 | 3 |
| Iván Duarte | Madrid | Tren | 147 | 56 | 15 | 8 |
| Rocío Mora | Sevilla | Avión | 871 | 107 | 157 | 11 |
| Jorge Luna | Bilbao | Coche | 744 | 480 | 193 | 9 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: Entre los empleados que cumplen estas condiciones: tiempo inferior a 301 y distancia inferior a 607, ¿cuál tiene el valor más alto de coste?

a) Luis Parra.
b) Marta Ríos.
c) Pablo Vera.
d) Irene Pons.

**Clave: d**

Explicación: Pasan el filtro 5 empleados; entre ellos, «Irene Pons» tiene el valor más alto de coste.

## 39. seed 1177092152084991428 · nivel 1

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Lambda | Valencia | Mixta | 764 | 16 | 58 | 229 |
| Theta | Madrid | Pública | 421 | 21 | 230 | 248 |
| Omega | Sevilla | Mixta | 575 | 23 | 142 | 269 |
| Iota | Sevilla | Privada | 845 | 17 | 364 | 63 |
| Gamma | Barcelona | Mixta | 547 | 18 | 162 | 194 |
| Zeta | Valencia | Mixta | 726 | 23 | 205 | 171 |
| Kappa | Barcelona | Mixta | 916 | 15 | 239 | 195 |
| Sigma | Bilbao | Mixta | 430 | 9 | 100 | 87 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuál de los siguientes laboratorios cumple estas condiciones: menos de 491 muestras analizadas, presupuesto superior a 62 y menos de 112 informes emitidos?

a) Sigma.
b) Gamma.
c) Omega.
d) Kappa.

**Clave: a**

Explicación: Solo «Sigma» cumple las 3 condiciones: menos de 491 muestras analizadas, presupuesto superior a 62 y menos de 112 informes emitidos.

## 40. seed 2300311533501968391 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Kappa | Sevilla | Mixta | 928 | 15 | 359 | 134 |
| Theta | Madrid | Pública | 948 | 21 | 179 | 147 |
| Beta | Sevilla | Privada | 859 | 4 | 301 | 89 |
| Gamma | Valencia | Pública | 185 | 15 | 309 | 120 |
| Zeta | Barcelona | Privada | 312 | 9 | 362 | 275 |
| Alfa | Sevilla | Pública | 416 | 17 | 313 | 138 |
| Sigma | Bilbao | Pública | 311 | 15 | 257 | 237 |
| Lambda | Madrid | Privada | 434 | 15 | 297 | 90 |
| Omega | Madrid | Privada | 771 | 8 | 109 | 261 |
| Delta | Sevilla | Mixta | 766 | 15 | 266 | 298 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuántos laboratorios cumplen estas condiciones: más de 94 informes emitidos, más de 13 técnicos y presupuesto superior a 278?

a) 5
b) 3
c) 1
d) 4

**Clave: b**

Explicación: Cumplen las condiciones (más de 94 informes emitidos, más de 13 técnicos y presupuesto superior a 278) exactamente 3.

## 41. seed 4561429966377530467 · nivel 3

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Gamma | Madrid | Privada | 466 | 10 | 171 | 63 |
| Zeta | Bilbao | Pública | 543 | 20 | 208 | 99 |
| Épsilon | Madrid | Privada | 486 | 3 | 68 | 181 |
| Omega | Bilbao | Pública | 685 | 11 | 190 | 222 |
| Lambda | Sevilla | Mixta | 436 | 8 | 208 | 52 |
| Alfa | Madrid | Pública | 552 | 14 | 145 | 229 |
| Delta | Bilbao | Pública | 657 | 20 | 349 | 64 |
| Kappa | Bilbao | Pública | 878 | 11 | 251 | 153 |
| Beta | Barcelona | Pública | 169 | 13 | 51 | 170 |
| Theta | Bilbao | Mixta | 723 | 16 | 126 | 171 |
| Sigma | Bilbao | Mixta | 714 | 6 | 335 | 59 |
| Iota | Valencia | Privada | 313 | 16 | 363 | 164 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Qué porcentaje del total de informes emitidos corresponde a los laboratorios con titularidad «Pública»?

a) 50,68 %
b) 57,59 %
c) 42,41 %
d) 73,72 %

**Clave: b**

Explicación: Los laboratorios con titularidad «Pública» suman 937 de un total de 1627: 57,59 %.

## 42. seed 279218220529479154 · nivel 1

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Gamma | Barcelona | Mixta | 733 | 19 | 242 | 275 |
| Kappa | Sevilla | Privada | 554 | 19 | 179 | 154 |
| Sigma | Valencia | Privada | 743 | 19 | 53 | 280 |
| Omega | Bilbao | Pública | 429 | 15 | 62 | 162 |
| Alfa | Sevilla | Pública | 200 | 18 | 392 | 139 |
| Beta | Valencia | Mixta | 544 | 8 | 152 | 223 |
| Delta | Bilbao | Pública | 952 | 13 | 380 | 271 |
| Épsilon | Madrid | Privada | 884 | 13 | 229 | 50 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuál de los siguientes laboratorios cumple estas condiciones: menos de 523 muestras analizadas y ciudad «Bilbao»?

a) Gamma.
b) Delta.
c) Omega.
d) Kappa.

**Clave: c**

Explicación: Solo «Omega» cumple las 2 condiciones: menos de 523 muestras analizadas y ciudad «Bilbao».

## 43. seed 2042550028401227693 · nivel 2

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Toledo | Gastronómica | Autobús | 29 | 72 | 4 | 446 |
| Lugo | Gastronómica | Minibús | 35 | 31 | 11 | 172 |
| Segovia | Naturaleza | Autobús | 48 | 17 | 15 | 450 |
| Ronda | Naturaleza | Minibús | 14 | 51 | 24 | 448 |
| Cuenca | Gastronómica | Autobús | 43 | 40 | 21 | 474 |
| León | Cultural | Autobús | 30 | 16 | 18 | 300 |
| Mérida | Gastronómica | Autobús | 28 | 19 | 14 | 322 |
| Ávila | Deportiva | Minibús | 20 | 40 | 6 | 184 |
| Úbeda | Deportiva | Tren | 58 | 60 | 20 | 435 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuántos destinos cumplen estas condiciones: tipo «Deportiva» y menos de 472 kilómetros?

a) 2
b) 3
c) 0
d) 4

**Clave: a**

Explicación: Cumplen las condiciones (tipo «Deportiva» y menos de 472 kilómetros) exactamente 2.

## 44. seed 1065444377732371285 · nivel 3

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Sigma | Barcelona | Pública | 907 | 24 | 163 | 279 |
| Delta | Sevilla | Mixta | 282 | 7 | 163 | 169 |
| Beta | Valencia | Privada | 694 | 10 | 183 | 74 |
| Omega | Bilbao | Privada | 171 | 19 | 294 | 212 |
| Gamma | Bilbao | Pública | 330 | 4 | 152 | 94 |
| Kappa | Bilbao | Pública | 641 | 16 | 209 | 136 |
| Theta | Barcelona | Pública | 226 | 8 | 258 | 148 |
| Zeta | Bilbao | Mixta | 503 | 15 | 290 | 250 |
| Épsilon | Sevilla | Pública | 778 | 13 | 387 | 139 |
| Iota | Madrid | Mixta | 966 | 22 | 294 | 47 |
| Alfa | Valencia | Mixta | 219 | 21 | 107 | 286 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Qué porcentaje del total de muestras analizadas corresponde a los laboratorios con ciudad «Valencia»?

a) 19,16 %
b) 13,41 %
c) 15,97 %
d) 12,78 %

**Clave: c**

Explicación: Los laboratorios con ciudad «Valencia» suman 913 de un total de 5717: 15,97 %.

## 45. seed 2719097753412396217 · nivel 2

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Soria | Naturaleza | Minibús | 34 | 25 | 14 | 389 |
| Segovia | Gastronómica | Tren | 60 | 93 | 27 | 132 |
| Ávila | Gastronómica | Tren | 16 | 76 | 20 | 205 |
| Teruel | Gastronómica | Tren | 41 | 37 | 16 | 116 |
| Ronda | Naturaleza | Autobús | 40 | 20 | 9 | 207 |
| Cuenca | Naturaleza | Minibús | 34 | 68 | 17 | 342 |
| Jaca | Cultural | Autobús | 31 | 52 | 19 | 470 |
| Mérida | Naturaleza | Tren | 56 | 28 | 5 | 343 |
| Lugo | Naturaleza | Minibús | 33 | 72 | 29 | 287 |
| León | Deportiva | Minibús | 47 | 35 | 27 | 165 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuál es el total de duración de los destinos que cumplen estas condiciones: transporte «Minibús» y menos de 38 participantes?

a) 60
b) 48
c) 46
d) 70

**Clave: a**

Explicación: Pasan el filtro 3 filas; en ellas, la columna «Duración (horas)» suma 60.

## 46. seed 3969796563389545576 · nivel 2

Tabla «Préstamos»:

| Título | Lugar de edición | Editorial | Año de publicación | Ejemplares disponibles | Ejemplares prestados | Préstamos realizados |
|---|---|---|---|---|---|---|
| Un calor tan cercano | Madrid | Anagrama | 2003 | 15 | 5 | 175 |
| Mano de sombra | Barcelona | Santillana | 1997 | 6 | 4 | 186 |
| Noches de invierno | Barcelona | Destino | 2000 | 15 | 3 | 251 |
| Contra vosotros | Madrid | Anagrama | 2005 | 17 | 6 | 144 |
| El amante lesbiano | Valencia | Alfaguara | 2000 | 4 | 1 | 142 |
| El jardín cerrado | Sevilla | Santillana | 2001 | 12 | 2 | 250 |
| Los días azules | Valencia | Planeta | 2005 | 3 | 2 | 181 |
| La casa del lago | Madrid | Anagrama | 1996 | 20 | 6 | 129 |
| Hija de la fortuna | Barcelona | Alfaguara | 2000 | 9 | 5 | 291 |
| Adiós a las novias | Madrid | Santillana | 2003 | 14 | 5 | 212 |

Responda a la siguiente pregunta según la tabla llamada Préstamos: ¿Cuál es el total de ejemplares disponibles de los títulos que cumplen estas condiciones: editorial «Santillana» y menos de 232 préstamos realizados?

a) 18
b) 20
c) 35
d) 19

**Clave: b**

Explicación: Pasan el filtro 2 filas; en ellas, la columna «Ejemplares disponibles» suma 20.

## 47. seed 2439017718913394027 · nivel 2

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Raúl Mena | Inglés | Tarde | 28 | 7 | 91 | 7 |
| Ana Cortés | Francés | Noche | 46 | 11 | 69 | 2 |
| Jorge Luna | Francés | Tarde | 32 | 8 | 114 | 4 |
| Sara Ortiz | Informática | Mañana | 28 | 9 | 80 | 8 |
| Iván Duarte | Francés | Tarde | 42 | 5 | 93 | 1 |
| Víctor Ibarra | Francés | Tarde | 51 | 5 | 38 | 4 |
| Nuria Salas | Alemán | Mañana | 48 | 2 | 66 | 0 |
| Elena Soler | Francés | Tarde | 35 | 4 | 120 | 8 |
| Andrés Peña | Alemán | Noche | 33 | 6 | 52 | 2 |
| Irene Pons | Francés | Noche | 45 | 10 | 56 | 15 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Cuál es el total de cuota mensual de los alumnos que cumplen estas condiciones: turno «Tarde» y más de 6 horas semanales?

a) 274
b) 262
c) 205
d) 180

**Clave: c**

Explicación: Pasan el filtro 2 filas; en ellas, la columna «Cuota mensual» suma 205.

## 48. seed 2169652614732583283 · nivel 2

Tabla «Préstamos»:

| Título | Lugar de edición | Editorial | Año de publicación | Ejemplares disponibles | Ejemplares prestados | Préstamos realizados |
|---|---|---|---|---|---|---|
| Mano de sombra | Madrid | Alfaguara | 2005 | 14 | 2 | 180 |
| El último tren | Madrid | Destino | 1995 | 5 | 3 | 227 |
| Adiós a las novias | Barcelona | Anagrama | 1997 | 6 | 6 | 199 |
| La isla vacía | Valencia | Alfaguara | 1998 | 9 | 8 | 138 |
| Entre visillos | Madrid | Planeta | 2004 | 14 | 3 | 336 |
| Hija de la fortuna | Valencia | Destino | 2001 | 14 | 8 | 192 |
| Tiempo de ceniza | Madrid | Santillana | 2002 | 18 | 1 | 185 |
| El amante lesbiano | Sevilla | Anagrama | 1998 | 19 | 9 | 199 |
| Los días azules | Valencia | Alfaguara | 2000 | 14 | 6 | 217 |
| La temporada de caza | Sevilla | Planeta | 1999 | 7 | 9 | 291 |

Responda a la siguiente pregunta según la tabla llamada Préstamos: ¿Cuántos títulos cumplen estas condiciones: más de 7 ejemplares prestados y más de 13 ejemplares disponibles?

a) 5
b) 1
c) 2
d) 0

**Clave: c**

Explicación: Cumplen las condiciones (más de 7 ejemplares prestados y más de 13 ejemplares disponibles) exactamente 2.

## 49. seed 4533545574814537803 · nivel 3

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| León | Deportiva | Minibús | 13 | 22 | 11 | 152 |
| Soria | Cultural | Autobús | 59 | 40 | 22 | 157 |
| Segovia | Cultural | Autobús | 25 | 24 | 19 | 430 |
| Jaca | Gastronómica | Tren | 28 | 82 | 6 | 421 |
| Teruel | Cultural | Minibús | 38 | 63 | 14 | 353 |
| Úbeda | Gastronómica | Autobús | 51 | 22 | 16 | 260 |
| Ronda | Naturaleza | Minibús | 58 | 44 | 23 | 250 |
| Toledo | Deportiva | Minibús | 38 | 94 | 14 | 251 |
| Ávila | Deportiva | Autobús | 47 | 25 | 15 | 414 |
| Lugo | Gastronómica | Autobús | 31 | 49 | 24 | 375 |
| Cuenca | Naturaleza | Autobús | 27 | 90 | 5 | 45 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuál es la media de participantes de todos los destinos?

a) 38,80
b) 37,73
c) 41,50
d) 38,00

**Clave: b**

Explicación: La suma de la columna es 415,00 y hay 11 filas: 37,73.

## 50. seed 3814695743816065413 · nivel 2

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Toledo | Naturaleza | Minibús | 44 | 36 | 11 | 159 |
| Soria | Naturaleza | Minibús | 34 | 19 | 26 | 74 |
| Úbeda | Gastronómica | Minibús | 50 | 45 | 22 | 200 |
| Mérida | Cultural | Autobús | 34 | 47 | 27 | 225 |
| Cuenca | Cultural | Tren | 46 | 22 | 29 | 325 |
| Teruel | Cultural | Minibús | 13 | 25 | 27 | 138 |
| Jaca | Gastronómica | Autobús | 60 | 76 | 23 | 212 |
| Lugo | Gastronómica | Tren | 15 | 75 | 6 | 179 |
| Ávila | Deportiva | Tren | 16 | 74 | 23 | 419 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuál es el total de kilómetros de los destinos que cumplen estas condiciones: precio por persona superior a 67 y menos de 21 participantes?

a) 478
b) 526
c) 757
d) 598

**Clave: d**

Explicación: Pasan el filtro 2 filas; en ellas, la columna «Kilómetros» suma 598.
