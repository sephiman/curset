# Lectura de tablas (`tablas-lectura`) — 50 goldens

Generated items for the blind review (ambiguity, realism, key). Each is `seed`, difficulty level, stem, options in the order shown, the key the solver computes and the explanation shown after answering. Regenerate with `uv run python scripts/export_psicotecnico_goldens.py`.

## 1. seed 274797139979144773 · nivel 2

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Segovia | Naturaleza | Tren | 57 | 72 | 23 | 384 |
| Teruel | Deportiva | Barco | 43 | 72 | 15 | 172 |
| Ronda | Cultural | Autobús | 30 | 29 | 12 | 171 |
| Jaca | Naturaleza | Barco | 52 | 23 | 14 | 61 |
| Úbeda | Gastronómica | Tren | 58 | 51 | 19 | 76 |
| Lugo | Cultural | Autobús | 54 | 83 | 23 | 283 |
| Cuenca | Naturaleza | Autobús | 52 | 74 | 25 | 247 |
| Toledo | Cultural | Barco | 52 | 73 | 29 | 299 |
| Mérida | Naturaleza | Autobús | 45 | 93 | 13 | 267 |
| León | Gastronómica | Tren | 21 | 22 | 29 | 296 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuántos destinos tienen duración inferior a 25, participantes superior a 50 y precio por persona inferior a 81?

a) 3
b) 4
c) 6
d) 2

**Clave: a**

Explicación: Cumplen las condiciones (duración inferior a 25, participantes superior a 50 y precio por persona inferior a 81) exactamente 3.

## 2. seed 3493489528897654557 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Iota | Valencia | Pública | 790 | 6 | 93 | 86 |
| Beta | Barcelona | Mixta | 221 | 8 | 93 | 83 |
| Omega | Bilbao | Mixta | 436 | 3 | 221 | 253 |
| Gamma | Valencia | Mixta | 189 | 10 | 106 | 99 |
| Sigma | Bilbao | Pública | 758 | 15 | 394 | 194 |
| Kappa | Sevilla | Mixta | 618 | 23 | 340 | 131 |
| Theta | Sevilla | Privada | 814 | 3 | 368 | 181 |
| Alfa | Madrid | Privada | 591 | 22 | 209 | 128 |
| Lambda | Barcelona | Mixta | 306 | 15 | 234 | 229 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuál es el total de técnicos de los laboratorios que tienen informes emitidos inferior a 111 y titularidad Mixta?

a) 23
b) 24
c) 18
d) 16

**Clave: c**

Explicación: Pasan el filtro 2 filas; sus técnicos suman 18.

## 3. seed 3888289725752918728 · nivel 1

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Irene Pons | Sevilla | Tren | 589 | 133 | 202 | 6 |
| Ana Cortés | Sevilla | Coche | 690 | 413 | 160 | 13 |
| Marta Ríos | Bilbao | Coche | 662 | 300 | 135 | 4 |
| Diego Rubio | Valencia | Autobús | 531 | 179 | 106 | 1 |
| Paula Giner | Bilbao | Tren | 699 | 436 | 76 | 12 |
| Lucía Costa | Madrid | Avión | 689 | 384 | 183 | 13 |
| Rocío Mora | Barcelona | Tren | 491 | 118 | 47 | 3 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Cuál de los siguientes empleados tiene destino Madrid, tiempo superior a 336 y distancia superior a 603?

a) Lucía Costa.
b) Marta Ríos.
c) Rocío Mora.
d) Irene Pons.

**Clave: a**

Explicación: Solo «Lucía Costa» cumple las 3 condiciones: destino Madrid, tiempo superior a 336 y distancia superior a 603.

## 4. seed 679292652377546788 · nivel 2

Tabla «Préstamos»:

| Título | Lugar de edición | Editorial | Año de publicación | Ejemplares disponibles | Ejemplares prestados | Préstamos realizados |
|---|---|---|---|---|---|---|
| La isla vacía | Valencia | Santillana | 2000 | 9 | 5 | 340 |
| La casa del lago | Barcelona | Planeta | 1998 | 18 | 5 | 222 |
| Adiós a las novias | Madrid | Anagrama | 1996 | 3 | 7 | 226 |
| El amante lesbiano | Valencia | Planeta | 2000 | 16 | 7 | 228 |
| Aranmanoth | Valencia | Alfaguara | 2003 | 11 | 6 | 227 |
| El último tren | Valencia | Anagrama | 1995 | 8 | 7 | 160 |
| El equipaje del viajero | Valencia | Planeta | 2005 | 7 | 8 | 319 |
| Noches de invierno | Sevilla | Destino | 1999 | 14 | 5 | 144 |
| Mano de sombra | Barcelona | Alfaguara | 2002 | 6 | 4 | 214 |
| Un calor tan cercano | Sevilla | Santillana | 2002 | 16 | 7 | 157 |

Responda a la siguiente pregunta según la tabla llamada Préstamos: ¿Qué título tiene el mayor cociente entre año de publicación y ejemplares prestados?

a) Mano de sombra.
b) La isla vacía.
c) La casa del lago.
d) Aranmanoth.

**Clave: a**

Explicación: Se divide año de publicación entre ejemplares prestados en cada fila: el mayor cociente es el de «Mano de sombra» (500,50).

## 5. seed 2618344893097292910 · nivel 2

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Teruel | Gastronómica | Tren | 58 | 22 | 4 | 446 |
| Mérida | Cultural | Autobús | 49 | 72 | 27 | 475 |
| Jaca | Naturaleza | Autobús | 14 | 69 | 9 | 409 |
| Úbeda | Gastronómica | Tren | 46 | 51 | 9 | 110 |
| Segovia | Deportiva | Tren | 39 | 51 | 29 | 206 |
| Ávila | Gastronómica | Barco | 12 | 81 | 15 | 75 |
| Ronda | Cultural | Tren | 15 | 89 | 7 | 225 |
| Cuenca | Gastronómica | Autobús | 31 | 59 | 25 | 384 |
| León | Gastronómica | Tren | 36 | 94 | 12 | 78 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuál es el total de kilómetros de los destinos que tienen precio por persona superior a 83 y duración inferior a 13?

a) 303
b) 327
c) 364
d) 218

**Clave: a**

Explicación: Pasan el filtro 2 filas; sus kilómetros suman 303.

## 6. seed 995660733233502469 · nivel 2

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Carla Nieto | Valencia | Coche | 486 | 99 | 104 | 4 |
| Hugo Beltrán | Valencia | Coche | 583 | 430 | 67 | 9 |
| Elena Soler | Barcelona | Tren | 116 | 68 | 193 | 8 |
| Pablo Vera | Madrid | Tren | 341 | 498 | 77 | 5 |
| Nuria Salas | Sevilla | Autobús | 441 | 60 | 189 | 6 |
| Jorge Luna | Madrid | Avión | 298 | 508 | 223 | 3 |
| Víctor Ibarra | Madrid | Autobús | 603 | 389 | 24 | 5 |
| Iván Duarte | Bilbao | Avión | 467 | 472 | 47 | 7 |
| Marta Ríos | Bilbao | Avión | 302 | 198 | 141 | 6 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Cuál es el total de distancia de los empleados que tienen coste superior a 91 y tiempo inferior a 111?

a) 1168
b) 1043
c) 1252
d) 1626

**Clave: b**

Explicación: Pasan el filtro 3 filas; sus distancia suman 1043.

## 7. seed 1223983771725134866 · nivel 2

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Marta Ríos | Francés | Noche | 30 | 8 | 82 | 4 |
| Pablo Vera | Francés | Mañana | 43 | 6 | 81 | 10 |
| Óscar Lara | Inglés | Mañana | 48 | 7 | 73 | 2 |
| Raúl Mena | Alemán | Mañana | 49 | 8 | 104 | 6 |
| Luis Parra | Informática | Tarde | 44 | 4 | 44 | 12 |
| Hugo Beltrán | Francés | Tarde | 25 | 12 | 63 | 9 |
| Víctor Ibarra | Francés | Tarde | 32 | 7 | 30 | 9 |
| Diego Rubio | Francés | Tarde | 48 | 11 | 67 | 13 |
| Ana Cortés | Inglés | Noche | 22 | 9 | 40 | 6 |
| Carla Nieto | Inglés | Mañana | 55 | 10 | 74 | 14 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Cuál de los siguientes alumnos tiene cuota mensual superior a 64, faltas de asistencia inferior a 3 y edad inferior a 54?

a) Luis Parra.
b) Pablo Vera.
c) Óscar Lara.
d) Marta Ríos.

**Clave: c**

Explicación: Solo «Óscar Lara» cumple las 3 condiciones: cuota mensual superior a 64, faltas de asistencia inferior a 3 y edad inferior a 54.

## 8. seed 4580581082989247247 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Omega | Valencia | Pública | 452 | 7 | 93 | 166 |
| Épsilon | Madrid | Privada | 649 | 17 | 256 | 279 |
| Gamma | Sevilla | Privada | 477 | 24 | 125 | 179 |
| Zeta | Madrid | Privada | 571 | 17 | 121 | 276 |
| Beta | Madrid | Pública | 266 | 9 | 165 | 172 |
| Theta | Valencia | Mixta | 447 | 11 | 223 | 106 |
| Delta | Madrid | Pública | 136 | 4 | 199 | 200 |
| Iota | Barcelona | Pública | 237 | 17 | 75 | 187 |
| Kappa | Bilbao | Privada | 274 | 23 | 300 | 77 |
| Sigma | Sevilla | Mixta | 867 | 24 | 82 | 152 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Qué laboratorio tiene el menor cociente entre informes emitidos y técnicos?

a) Gamma.
b) Sigma.
c) Kappa.
d) Theta.

**Clave: c**

Explicación: Se divide informes emitidos entre técnicos en cada fila: el menor cociente es el de «Kappa» (3,35).

## 9. seed 3910380554785824084 · nivel 1

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Iván Duarte | Sevilla | Autobús | 550 | 512 | 180 | 4 |
| Lucía Costa | Valencia | Tren | 336 | 345 | 96 | 6 |
| Carla Nieto | Madrid | Autobús | 663 | 430 | 105 | 4 |
| Marta Ríos | Valencia | Coche | 861 | 240 | 135 | 11 |
| Paula Giner | Barcelona | Avión | 475 | 155 | 161 | 2 |
| Nuria Salas | Bilbao | Autobús | 297 | 82 | 154 | 11 |
| Hugo Beltrán | Barcelona | Avión | 451 | 112 | 181 | 13 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Cuántos empleados tienen tiempo superior a 98, medio Avión y destino Barcelona?

a) 5
b) 2
c) 0
d) 3

**Clave: b**

Explicación: Cumplen las condiciones (tiempo superior a 98, medio Avión y destino Barcelona) exactamente 2.

## 10. seed 4441628925242482318 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Gamma | Madrid | Mixta | 572 | 6 | 228 | 55 |
| Zeta | Barcelona | Pública | 973 | 21 | 353 | 205 |
| Delta | Bilbao | Mixta | 305 | 11 | 358 | 141 |
| Omega | Valencia | Pública | 402 | 12 | 312 | 175 |
| Lambda | Barcelona | Mixta | 845 | 15 | 317 | 123 |
| Iota | Sevilla | Mixta | 511 | 5 | 189 | 287 |
| Sigma | Barcelona | Privada | 898 | 6 | 230 | 166 |
| Épsilon | Valencia | Pública | 799 | 15 | 73 | 63 |
| Kappa | Madrid | Pública | 393 | 16 | 66 | 179 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: Entre los laboratorios que tienen técnicos inferior a 16 y informes emitidos superior a 108, ¿cuál tiene el valor más alto de presupuesto?

a) Omega.
b) Gamma.
c) Delta.
d) Sigma.

**Clave: c**

Explicación: Pasan el filtro 5 laboratorios; entre ellos, «Delta» tiene el valor más alto de presupuesto.

## 11. seed 2446871128147784257 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Sigma | Madrid | Privada | 167 | 18 | 120 | 201 |
| Iota | Madrid | Pública | 162 | 23 | 266 | 256 |
| Zeta | Sevilla | Mixta | 521 | 24 | 148 | 236 |
| Omega | Valencia | Pública | 750 | 9 | 107 | 197 |
| Beta | Bilbao | Mixta | 871 | 12 | 166 | 204 |
| Alfa | Barcelona | Privada | 442 | 10 | 76 | 297 |
| Delta | Sevilla | Mixta | 418 | 11 | 169 | 278 |
| Épsilon | Barcelona | Privada | 616 | 18 | 325 | 265 |
| Gamma | Bilbao | Pública | 631 | 6 | 274 | 154 |
| Theta | Bilbao | Mixta | 464 | 11 | 186 | 148 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: Entre los laboratorios que tienen técnicos superior a 10 y muestras analizadas superior a 366, ¿cuál tiene el valor más bajo de presupuesto?

a) Sigma.
b) Zeta.
c) Iota.
d) Delta.

**Clave: b**

Explicación: Pasan el filtro 5 laboratorios; entre ellos, «Zeta» tiene el valor más bajo de presupuesto.

## 12. seed 3654112830433712182 · nivel 1

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Mérida | Naturaleza | Tren | 21 | 88 | 20 | 237 |
| Cuenca | Deportiva | Autobús | 15 | 75 | 10 | 213 |
| Úbeda | Naturaleza | Barco | 22 | 46 | 15 | 355 |
| Ronda | Deportiva | Autobús | 58 | 64 | 12 | 183 |
| Segovia | Cultural | Tren | 60 | 17 | 25 | 463 |
| Toledo | Gastronómica | Autobús | 41 | 38 | 8 | 168 |
| Lugo | Gastronómica | Barco | 17 | 62 | 25 | 179 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuál de los siguientes destinos tiene precio por persona inferior a 72 y tipo Deportiva?

a) Mérida.
b) Úbeda.
c) Lugo.
d) Ronda.

**Clave: d**

Explicación: Solo «Ronda» cumple las 2 condiciones: precio por persona inferior a 72 y tipo Deportiva.

## 13. seed 327284621952842892 · nivel 3

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Épsilon | Madrid | Privada | 533 | 22 | 202 | 260 |
| Sigma | Sevilla | Privada | 266 | 18 | 50 | 119 |
| Delta | Madrid | Privada | 538 | 21 | 365 | 167 |
| Gamma | Sevilla | Mixta | 793 | 10 | 336 | 68 |
| Iota | Madrid | Pública | 685 | 20 | 361 | 71 |
| Omega | Madrid | Pública | 521 | 6 | 91 | 282 |
| Kappa | Valencia | Mixta | 258 | 18 | 286 | 299 |
| Alfa | Barcelona | Pública | 368 | 24 | 146 | 37 |
| Theta | Sevilla | Privada | 977 | 22 | 236 | 43 |
| Beta | Bilbao | Privada | 647 | 7 | 354 | 119 |
| Zeta | Sevilla | Pública | 596 | 14 | 224 | 31 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuál es la media de técnicos de todos los laboratorios?

a) 11,91
b) 21,18
c) 18,00
d) 16,55

**Clave: d**

Explicación: La suma de la columna es 182,00 y hay 11 filas: 16,55.

## 14. seed 3262813409570128271 · nivel 1

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Alfa | Bilbao | Privada | 942 | 21 | 278 | 174 |
| Kappa | Madrid | Mixta | 681 | 15 | 207 | 232 |
| Delta | Madrid | Pública | 628 | 5 | 122 | 216 |
| Beta | Bilbao | Mixta | 373 | 8 | 171 | 38 |
| Iota | Valencia | Mixta | 695 | 5 | 200 | 57 |
| Omega | Barcelona | Pública | 569 | 10 | 266 | 173 |
| Sigma | Sevilla | Mixta | 219 | 9 | 159 | 209 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Qué laboratorio tiene el mayor cociente entre informes emitidos y muestras analizadas?

a) Sigma.
b) Kappa.
c) Delta.
d) Omega.

**Clave: a**

Explicación: Se divide informes emitidos entre muestras analizadas en cada fila: el mayor cociente es el de «Sigma» (0,95).

## 15. seed 1574408861979755188 · nivel 1

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Sigma | Madrid | Privada | 298 | 5 | 185 | 184 |
| Theta | Barcelona | Mixta | 443 | 3 | 118 | 278 |
| Épsilon | Madrid | Mixta | 176 | 20 | 197 | 161 |
| Delta | Sevilla | Mixta | 698 | 19 | 216 | 162 |
| Gamma | Madrid | Privada | 832 | 9 | 216 | 213 |
| Alfa | Bilbao | Pública | 505 | 16 | 363 | 143 |
| Beta | Valencia | Pública | 248 | 21 | 164 | 71 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuál de los siguientes laboratorios tiene presupuesto superior a 318 y informes emitidos superior a 126?

a) Sigma.
b) Épsilon.
c) Theta.
d) Alfa.

**Clave: d**

Explicación: Solo «Alfa» cumple las 2 condiciones: presupuesto superior a 318 y informes emitidos superior a 126.

## 16. seed 2074564667347024303 · nivel 1

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Lugo | Cultural | Autobús | 35 | 63 | 28 | 401 |
| León | Gastronómica | Barco | 18 | 52 | 19 | 145 |
| Ávila | Gastronómica | Tren | 53 | 95 | 6 | 220 |
| Úbeda | Deportiva | Barco | 59 | 78 | 26 | 449 |
| Toledo | Naturaleza | Tren | 50 | 34 | 25 | 50 |
| Jaca | Gastronómica | Tren | 48 | 58 | 9 | 208 |
| Ronda | Naturaleza | Barco | 27 | 67 | 6 | 254 |
| Cuenca | Deportiva | Autobús | 53 | 70 | 9 | 368 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuál de los siguientes destinos tiene tipo Deportiva y precio por persona inferior a 78?

a) Cuenca.
b) Jaca.
c) León.
d) Ronda.

**Clave: a**

Explicación: Solo «Cuenca» cumple las 2 condiciones: tipo Deportiva y precio por persona inferior a 78.

## 17. seed 1580329207806355028 · nivel 1

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Beta | Bilbao | Pública | 479 | 20 | 42 | 163 |
| Lambda | Bilbao | Mixta | 312 | 22 | 354 | 146 |
| Iota | Valencia | Mixta | 783 | 14 | 326 | 81 |
| Épsilon | Barcelona | Privada | 498 | 17 | 177 | 159 |
| Sigma | Madrid | Pública | 819 | 14 | 131 | 186 |
| Theta | Sevilla | Mixta | 734 | 13 | 157 | 30 |
| Delta | Sevilla | Privada | 120 | 13 | 306 | 58 |
| Gamma | Bilbao | Privada | 227 | 18 | 241 | 261 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuál de los siguientes laboratorios tiene informes emitidos superior a 140, presupuesto inferior a 199 y titularidad Privada?

a) Épsilon.
b) Beta.
c) Theta.
d) Sigma.

**Clave: a**

Explicación: Solo «Épsilon» cumple las 3 condiciones: informes emitidos superior a 140, presupuesto inferior a 199 y titularidad Privada.

## 18. seed 4157976482641714332 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Gamma | Barcelona | Mixta | 412 | 7 | 84 | 185 |
| Kappa | Madrid | Mixta | 540 | 15 | 355 | 261 |
| Delta | Madrid | Mixta | 776 | 7 | 334 | 215 |
| Épsilon | Barcelona | Mixta | 287 | 24 | 142 | 122 |
| Iota | Bilbao | Privada | 158 | 12 | 258 | 71 |
| Zeta | Bilbao | Privada | 226 | 12 | 133 | 78 |
| Alfa | Madrid | Pública | 609 | 15 | 390 | 109 |
| Lambda | Valencia | Pública | 518 | 22 | 281 | 101 |
| Omega | Sevilla | Privada | 690 | 15 | 285 | 153 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuál es el total de presupuesto de los laboratorios que tienen técnicos superior a 11 y informes emitidos inferior a 79?

a) 469
b) 282
c) 407
d) 391

**Clave: d**

Explicación: Pasan el filtro 2 filas; sus presupuesto suman 391.

## 19. seed 345352013983549247 · nivel 2

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Carla Nieto | Valencia | Coche | 358 | 89 | 53 | 4 |
| Hugo Beltrán | Barcelona | Avión | 807 | 275 | 127 | 2 |
| Diego Rubio | Bilbao | Coche | 784 | 468 | 151 | 10 |
| Lucía Costa | Sevilla | Autobús | 360 | 193 | 72 | 13 |
| Irene Pons | Sevilla | Tren | 244 | 324 | 243 | 12 |
| Elena Soler | Sevilla | Avión | 524 | 269 | 28 | 1 |
| Paula Giner | Valencia | Tren | 454 | 471 | 259 | 2 |
| Raúl Mena | Barcelona | Autobús | 664 | 79 | 105 | 6 |
| Pablo Vera | Madrid | Autobús | 683 | 402 | 150 | 14 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Cuántos empleados tienen distancia superior a 315, viajes al año inferior a 14 y tiempo inferior a 217?

a) 3
b) 5
c) 1
d) 6

**Clave: a**

Explicación: Cumplen las condiciones (distancia superior a 315, viajes al año inferior a 14 y tiempo inferior a 217) exactamente 3.

## 20. seed 3725810980475735155 · nivel 1

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Pablo Vera | Madrid | Avión | 387 | 508 | 34 | 2 |
| Luis Parra | Valencia | Tren | 524 | 103 | 143 | 10 |
| Óscar Lara | Bilbao | Coche | 160 | 505 | 227 | 6 |
| Irene Pons | Bilbao | Autobús | 807 | 138 | 38 | 5 |
| Hugo Beltrán | Sevilla | Coche | 786 | 436 | 136 | 3 |
| Carla Nieto | Valencia | Avión | 623 | 494 | 26 | 4 |
| Jorge Luna | Barcelona | Coche | 797 | 498 | 165 | 6 |
| Andrés Peña | Valencia | Autobús | 800 | 115 | 21 | 3 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Qué empleado tiene el mayor cociente entre viajes al año y distancia?

a) Óscar Lara.
b) Luis Parra.
c) Jorge Luna.
d) Pablo Vera.

**Clave: a**

Explicación: Se divide viajes al año entre distancia en cada fila: el mayor cociente es el de «Óscar Lara» (0,04).

## 21. seed 3689692058427482923 · nivel 1

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Lucía Costa | Informática | Tarde | 44 | 8 | 60 | 5 |
| Raúl Mena | Francés | Tarde | 51 | 12 | 98 | 7 |
| Irene Pons | Alemán | Noche | 51 | 12 | 91 | 11 |
| Iván Duarte | Alemán | Tarde | 33 | 6 | 65 | 2 |
| Andrés Peña | Informática | Noche | 35 | 5 | 63 | 1 |
| Rocío Mora | Francés | Mañana | 21 | 9 | 81 | 11 |
| Nuria Salas | Inglés | Tarde | 48 | 5 | 83 | 9 |
| Sara Ortiz | Alemán | Noche | 51 | 8 | 79 | 2 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Cuál de los siguientes alumnos tiene horas semanales superior a 11, curso Alemán y edad superior a 45?

a) Irene Pons.
b) Sara Ortiz.
c) Iván Duarte.
d) Raúl Mena.

**Clave: a**

Explicación: Solo «Irene Pons» cumple las 3 condiciones: horas semanales superior a 11, curso Alemán y edad superior a 45.

## 22. seed 549857973036573262 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Beta | Valencia | Pública | 300 | 3 | 153 | 273 |
| Theta | Madrid | Mixta | 466 | 11 | 312 | 133 |
| Alfa | Sevilla | Privada | 532 | 10 | 235 | 135 |
| Zeta | Valencia | Pública | 551 | 7 | 159 | 132 |
| Sigma | Barcelona | Privada | 746 | 19 | 52 | 84 |
| Épsilon | Sevilla | Privada | 906 | 18 | 311 | 181 |
| Iota | Madrid | Pública | 647 | 8 | 272 | 111 |
| Delta | Bilbao | Privada | 457 | 7 | 216 | 270 |
| Lambda | Madrid | Pública | 917 | 5 | 391 | 49 |
| Omega | Sevilla | Mixta | 708 | 14 | 181 | 113 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuántos laboratorios tienen ciudad Sevilla, presupuesto inferior a 264 y técnicos superior a 9?

a) 2
b) 0
c) 4
d) 3

**Clave: a**

Explicación: Cumplen las condiciones (ciudad Sevilla, presupuesto inferior a 264 y técnicos superior a 9) exactamente 2.

## 23. seed 3911690445701389361 · nivel 1

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Hugo Beltrán | Inglés | Noche | 49 | 7 | 69 | 14 |
| Elena Soler | Alemán | Tarde | 41 | 6 | 95 | 7 |
| Marta Ríos | Informática | Noche | 48 | 5 | 80 | 11 |
| Nuria Salas | Francés | Noche | 27 | 7 | 82 | 3 |
| Carla Nieto | Informática | Tarde | 32 | 4 | 56 | 6 |
| Óscar Lara | Inglés | Mañana | 27 | 10 | 63 | 5 |
| Irene Pons | Alemán | Noche | 21 | 6 | 42 | 4 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Cuántos alumnos tienen edad inferior a 30 y cuota mensual superior a 56?

a) 5
b) 3
c) 2
d) 4

**Clave: c**

Explicación: Cumplen las condiciones (edad inferior a 30 y cuota mensual superior a 56) exactamente 2.

## 24. seed 4092711762427273095 · nivel 3

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Víctor Ibarra | Bilbao | Tren | 497 | 115 | 49 | 7 |
| Raúl Mena | Valencia | Autobús | 278 | 196 | 224 | 14 |
| Irene Pons | Bilbao | Avión | 471 | 248 | 98 | 13 |
| Rocío Mora | Madrid | Autobús | 536 | 103 | 73 | 4 |
| Diego Rubio | Barcelona | Coche | 364 | 372 | 218 | 14 |
| Iván Duarte | Valencia | Coche | 503 | 436 | 131 | 8 |
| Ana Cortés | Valencia | Autobús | 639 | 135 | 232 | 1 |
| Lucía Costa | Sevilla | Tren | 142 | 104 | 119 | 3 |
| Luis Parra | Sevilla | Autobús | 846 | 198 | 42 | 10 |
| Paula Giner | Barcelona | Tren | 834 | 379 | 197 | 8 |
| Elena Soler | Bilbao | Tren | 350 | 379 | 178 | 7 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Cuál es el total de distancia de los empleados que tienen viajes al año superior a 7 y medio Coche?

a) 624
b) 503
c) 867
d) 763

**Clave: c**

Explicación: Pasan el filtro 2 filas; sus distancia suman 867.

## 25. seed 2736979108388417725 · nivel 2

Tabla «Préstamos»:

| Título | Lugar de edición | Editorial | Año de publicación | Ejemplares disponibles | Ejemplares prestados | Préstamos realizados |
|---|---|---|---|---|---|---|
| Hija de la fortuna | Valencia | Planeta | 1996 | 19 | 1 | 314 |
| Un calor tan cercano | Barcelona | Destino | 1999 | 7 | 6 | 205 |
| Aranmanoth | Sevilla | Anagrama | 2000 | 6 | 4 | 163 |
| Contra vosotros | Sevilla | Anagrama | 2004 | 5 | 6 | 231 |
| El jardín cerrado | Barcelona | Santillana | 2001 | 17 | 6 | 212 |
| Tiempo de ceniza | Sevilla | Destino | 1999 | 13 | 7 | 271 |
| Mano de sombra | Valencia | Santillana | 2002 | 10 | 4 | 131 |
| Adiós a las novias | Madrid | Alfaguara | 2004 | 18 | 9 | 337 |
| Cuaderno de bitácora | Barcelona | Anagrama | 1997 | 11 | 1 | 120 |

Responda a la siguiente pregunta según la tabla llamada Préstamos: ¿Cuántos títulos tienen ejemplares disponibles superior a 5 y préstamos realizados inferior a 183?

a) 3
b) 6
c) 1
d) 2

**Clave: a**

Explicación: Cumplen las condiciones (ejemplares disponibles superior a 5 y préstamos realizados inferior a 183) exactamente 3.

## 26. seed 4163390447536696390 · nivel 1

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Lambda | Madrid | Privada | 438 | 15 | 123 | 71 |
| Zeta | Madrid | Pública | 897 | 6 | 137 | 45 |
| Delta | Barcelona | Mixta | 126 | 17 | 124 | 293 |
| Gamma | Sevilla | Pública | 837 | 9 | 318 | 300 |
| Iota | Valencia | Pública | 541 | 24 | 108 | 89 |
| Omega | Barcelona | Mixta | 859 | 11 | 75 | 91 |
| Épsilon | Barcelona | Mixta | 826 | 23 | 71 | 281 |
| Kappa | Bilbao | Privada | 221 | 24 | 196 | 96 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuántos laboratorios tienen muestras analizadas superior a 752, titularidad Mixta y técnicos superior a 10?

a) 2
b) 3
c) 0
d) 5

**Clave: a**

Explicación: Cumplen las condiciones (muestras analizadas superior a 752, titularidad Mixta y técnicos superior a 10) exactamente 2.

## 27. seed 1586508015396871889 · nivel 2

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Nuria Salas | Valencia | Autobús | 799 | 151 | 30 | 10 |
| Marta Ríos | Barcelona | Tren | 785 | 145 | 78 | 8 |
| Luis Parra | Bilbao | Avión | 695 | 105 | 211 | 13 |
| Ana Cortés | Sevilla | Avión | 291 | 302 | 138 | 9 |
| Óscar Lara | Barcelona | Autobús | 646 | 432 | 77 | 4 |
| Carla Nieto | Barcelona | Tren | 558 | 201 | 71 | 9 |
| Irene Pons | Sevilla | Coche | 486 | 109 | 121 | 14 |
| Pablo Vera | Bilbao | Autobús | 489 | 119 | 156 | 6 |
| Raúl Mena | Madrid | Coche | 586 | 466 | 85 | 12 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Cuál de los siguientes empleados tiene viajes al año inferior a 5, destino Barcelona, medio Autobús y distancia inferior a 726?

a) Óscar Lara.
b) Marta Ríos.
c) Ana Cortés.
d) Luis Parra.

**Clave: a**

Explicación: Solo «Óscar Lara» cumple las 4 condiciones: viajes al año inferior a 5, destino Barcelona, medio Autobús y distancia inferior a 726.

## 28. seed 3588842099432019975 · nivel 2

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Andrés Peña | Informática | Mañana | 36 | 7 | 114 | 7 |
| Ana Cortés | Informática | Noche | 33 | 4 | 74 | 14 |
| Pablo Vera | Francés | Tarde | 37 | 11 | 75 | 6 |
| Hugo Beltrán | Alemán | Noche | 27 | 12 | 89 | 2 |
| Marta Ríos | Francés | Mañana | 43 | 11 | 100 | 7 |
| Elena Soler | Francés | Noche | 30 | 12 | 49 | 1 |
| Nuria Salas | Informática | Tarde | 49 | 5 | 92 | 7 |
| Raúl Mena | Francés | Noche | 21 | 2 | 55 | 7 |
| Jorge Luna | Francés | Tarde | 20 | 11 | 109 | 0 |
| Diego Rubio | Inglés | Tarde | 49 | 2 | 96 | 11 |

Responda a la siguiente pregunta según la tabla llamada Academia: Sumando edad por curso, ¿qué curso obtiene el menor total?

a) Informática.
b) Inglés.
c) Alemán.
d) Francés.

**Clave: c**

Explicación: Los valores por curso son Alemán 27, Francés 151, Informática 118, Inglés 49; el menor es Alemán.

## 29. seed 4110580552696902388 · nivel 2

Tabla «Préstamos»:

| Título | Lugar de edición | Editorial | Año de publicación | Ejemplares disponibles | Ejemplares prestados | Préstamos realizados |
|---|---|---|---|---|---|---|
| La temporada de caza | Sevilla | Alfaguara | 1999 | 16 | 6 | 206 |
| Adiós a las novias | Valencia | Alfaguara | 2003 | 11 | 6 | 210 |
| Hija de la fortuna | Madrid | Planeta | 2005 | 15 | 5 | 293 |
| Mano de sombra | Madrid | Santillana | 2000 | 10 | 2 | 304 |
| Noches de invierno | Barcelona | Santillana | 1999 | 18 | 5 | 213 |
| Cuaderno de bitácora | Barcelona | Santillana | 2002 | 19 | 6 | 350 |
| La casa del lago | Valencia | Destino | 2005 | 11 | 2 | 176 |
| Los días azules | Sevilla | Destino | 2000 | 18 | 5 | 278 |
| El equipaje del viajero | Barcelona | Planeta | 2002 | 15 | 9 | 154 |
| El amante lesbiano | Sevilla | Anagrama | 1998 | 8 | 8 | 342 |

Responda a la siguiente pregunta según la tabla llamada Préstamos: Sumando ejemplares prestados por editorial, ¿qué editorial obtiene el mayor total?

a) Alfaguara.
b) Destino.
c) Planeta.
d) Anagrama.

**Clave: c**

Explicación: Los valores por editorial son Alfaguara 12, Anagrama 8, Destino 7, Planeta 14, Santillana 13; el mayor es Planeta.

## 30. seed 3556477018594785593 · nivel 2

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Irene Pons | Sevilla | Avión | 485 | 205 | 77 | 10 |
| Rocío Mora | Madrid | Autobús | 618 | 422 | 255 | 2 |
| Jorge Luna | Barcelona | Avión | 509 | 339 | 136 | 5 |
| Diego Rubio | Sevilla | Tren | 484 | 246 | 42 | 14 |
| Lucía Costa | Valencia | Autobús | 736 | 142 | 227 | 7 |
| Luis Parra | Valencia | Avión | 876 | 205 | 59 | 9 |
| Paula Giner | Valencia | Tren | 251 | 230 | 101 | 4 |
| Óscar Lara | Sevilla | Coche | 639 | 132 | 188 | 7 |
| Marta Ríos | Bilbao | Autobús | 519 | 468 | 69 | 11 |
| Hugo Beltrán | Barcelona | Avión | 589 | 130 | 88 | 11 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: Entre los empleados que tienen medio Avión y tiempo inferior a 381, ¿cuál tiene el valor más alto de viajes al año?

a) Hugo Beltrán.
b) Rocío Mora.
c) Irene Pons.
d) Luis Parra.

**Clave: a**

Explicación: Pasan el filtro 4 empleados; entre ellos, «Hugo Beltrán» tiene el valor más alto de viajes al año.

## 31. seed 2381850757681049524 · nivel 2

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Carla Nieto | Francés | Mañana | 44 | 4 | 32 | 6 |
| Sara Ortiz | Inglés | Tarde | 44 | 8 | 86 | 12 |
| Óscar Lara | Informática | Mañana | 37 | 5 | 84 | 13 |
| Jorge Luna | Alemán | Tarde | 24 | 4 | 98 | 7 |
| Lucía Costa | Informática | Noche | 45 | 2 | 111 | 14 |
| Nuria Salas | Francés | Noche | 55 | 7 | 61 | 1 |
| Andrés Peña | Informática | Tarde | 48 | 4 | 87 | 5 |
| Elena Soler | Alemán | Tarde | 19 | 11 | 34 | 12 |
| Iván Duarte | Inglés | Tarde | 53 | 3 | 85 | 2 |
| Ana Cortés | Francés | Mañana | 48 | 5 | 31 | 3 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Qué alumno tiene el mayor cociente entre cuota mensual y faltas de asistencia?

a) Andrés Peña.
b) Iván Duarte.
c) Lucía Costa.
d) Nuria Salas.

**Clave: d**

Explicación: Se divide cuota mensual entre faltas de asistencia en cada fila: el mayor cociente es el de «Nuria Salas» (61,00).

## 32. seed 3706174181096166754 · nivel 1

Tabla «Préstamos»:

| Título | Lugar de edición | Editorial | Año de publicación | Ejemplares disponibles | Ejemplares prestados | Préstamos realizados |
|---|---|---|---|---|---|---|
| La temporada de caza | Madrid | Destino | 1997 | 4 | 9 | 253 |
| Hija de la fortuna | Barcelona | Planeta | 2001 | 13 | 5 | 268 |
| La casa del lago | Valencia | Alfaguara | 2005 | 17 | 4 | 210 |
| Noches de invierno | Sevilla | Santillana | 1995 | 4 | 1 | 177 |
| La isla vacía | Valencia | Planeta | 1997 | 15 | 5 | 115 |
| Mano de sombra | Madrid | Anagrama | 2004 | 7 | 4 | 290 |
| Entre visillos | Madrid | Alfaguara | 2004 | 6 | 1 | 212 |

Responda a la siguiente pregunta según la tabla llamada Préstamos: Entre los títulos que tienen préstamos realizados superior a 222, ¿cuál tiene el valor más bajo de ejemplares prestados?

a) Entre visillos.
b) Noches de invierno.
c) Mano de sombra.
d) La isla vacía.

**Clave: c**

Explicación: Pasan el filtro 3 títulos; entre ellos, «Mano de sombra» tiene el valor más bajo de ejemplares prestados.

## 33. seed 3614112383633376201 · nivel 3

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Omega | Sevilla | Pública | 765 | 22 | 350 | 49 |
| Sigma | Barcelona | Mixta | 528 | 12 | 384 | 53 |
| Iota | Sevilla | Privada | 401 | 11 | 188 | 123 |
| Alfa | Valencia | Pública | 267 | 12 | 362 | 49 |
| Beta | Madrid | Mixta | 393 | 21 | 61 | 162 |
| Delta | Bilbao | Mixta | 427 | 22 | 350 | 277 |
| Gamma | Valencia | Mixta | 621 | 7 | 46 | 199 |
| Theta | Madrid | Privada | 563 | 14 | 393 | 116 |
| Zeta | Valencia | Pública | 947 | 5 | 195 | 61 |
| Kappa | Barcelona | Privada | 820 | 18 | 69 | 30 |
| Lambda | Barcelona | Pública | 797 | 10 | 315 | 179 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Qué laboratorio tiene el mayor cociente entre presupuesto y técnicos?

a) Zeta.
b) Theta.
c) Alfa.
d) Delta.

**Clave: a**

Explicación: Se divide presupuesto entre técnicos en cada fila: el mayor cociente es el de «Zeta» (39,00).

## 34. seed 1166747531291222478 · nivel 2

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Cuenca | Deportiva | Tren | 18 | 55 | 12 | 127 |
| Toledo | Gastronómica | Autobús | 34 | 53 | 19 | 111 |
| León | Gastronómica | Autobús | 46 | 26 | 4 | 84 |
| Jaca | Deportiva | Barco | 28 | 50 | 9 | 249 |
| Ronda | Naturaleza | Autobús | 45 | 54 | 5 | 131 |
| Úbeda | Cultural | Barco | 41 | 73 | 4 | 427 |
| Teruel | Gastronómica | Autobús | 52 | 23 | 8 | 444 |
| Ávila | Deportiva | Tren | 29 | 92 | 25 | 438 |
| Segovia | Cultural | Tren | 52 | 50 | 26 | 268 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuál es el total de precio por persona de los destinos que tienen kilómetros superior a 115 y participantes superior a 40?

a) 255
b) 200
c) 240
d) 160

**Clave: b**

Explicación: Pasan el filtro 4 filas; sus precio por persona suman 200.

## 35. seed 1690837818924781736 · nivel 2

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Segovia | Deportiva | Autobús | 59 | 47 | 27 | 440 |
| Ronda | Deportiva | Tren | 30 | 92 | 12 | 415 |
| Úbeda | Deportiva | Tren | 26 | 40 | 9 | 441 |
| Jaca | Gastronómica | Tren | 58 | 16 | 14 | 183 |
| Lugo | Cultural | Autobús | 26 | 89 | 14 | 372 |
| Toledo | Naturaleza | Barco | 28 | 84 | 27 | 128 |
| Mérida | Gastronómica | Barco | 24 | 20 | 25 | 426 |
| Teruel | Naturaleza | Autobús | 37 | 47 | 24 | 93 |
| Soria | Naturaleza | Barco | 35 | 67 | 16 | 238 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuántos destinos tienen precio por persona superior a 42 y transporte Autobús?

a) 6
b) 2
c) 4
d) 3

**Clave: d**

Explicación: Cumplen las condiciones (precio por persona superior a 42 y transporte Autobús) exactamente 3.

## 36. seed 3525112190121478594 · nivel 1

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Épsilon | Sevilla | Mixta | 660 | 20 | 112 | 258 |
| Delta | Madrid | Mixta | 349 | 22 | 190 | 113 |
| Kappa | Bilbao | Pública | 972 | 15 | 265 | 54 |
| Zeta | Bilbao | Privada | 401 | 15 | 190 | 160 |
| Lambda | Barcelona | Privada | 188 | 17 | 368 | 35 |
| Alfa | Sevilla | Mixta | 269 | 5 | 277 | 109 |
| Iota | Valencia | Privada | 604 | 23 | 224 | 290 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Qué laboratorio tiene el mayor cociente entre presupuesto y muestras analizadas?

a) Lambda.
b) Épsilon.
c) Alfa.
d) Zeta.

**Clave: a**

Explicación: Se divide presupuesto entre muestras analizadas en cada fila: el mayor cociente es el de «Lambda» (1,96).

## 37. seed 778671632053513995 · nivel 1

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Teruel | Gastronómica | Barco | 20 | 91 | 17 | 346 |
| Segovia | Gastronómica | Tren | 28 | 41 | 14 | 162 |
| Ávila | Naturaleza | Barco | 45 | 74 | 15 | 433 |
| Jaca | Gastronómica | Autobús | 22 | 49 | 21 | 235 |
| León | Deportiva | Barco | 47 | 80 | 29 | 334 |
| Úbeda | Naturaleza | Tren | 32 | 42 | 15 | 221 |
| Cuenca | Cultural | Tren | 42 | 89 | 15 | 292 |
| Soria | Deportiva | Barco | 30 | 21 | 23 | 40 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: Entre los destinos que tienen transporte Barco, ¿cuál tiene el valor más bajo de kilómetros?

a) Soria.
b) Teruel.
c) Segovia.
d) Ávila.

**Clave: a**

Explicación: Pasan el filtro 4 destinos; entre ellos, «Soria» tiene el valor más bajo de kilómetros.

## 38. seed 232616239795612045 · nivel 2

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Lugo | Gastronómica | Tren | 54 | 49 | 27 | 235 |
| Teruel | Deportiva | Barco | 34 | 34 | 17 | 343 |
| Cuenca | Naturaleza | Tren | 29 | 70 | 16 | 386 |
| Ronda | Naturaleza | Barco | 38 | 15 | 4 | 344 |
| Soria | Cultural | Autobús | 50 | 80 | 4 | 150 |
| Úbeda | Gastronómica | Barco | 26 | 95 | 17 | 186 |
| Ávila | Deportiva | Barco | 23 | 86 | 19 | 59 |
| León | Deportiva | Tren | 51 | 31 | 21 | 304 |
| Mérida | Gastronómica | Barco | 20 | 15 | 29 | 184 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Cuál de los siguientes destinos tiene transporte Barco, participantes inferior a 22 y tipo Gastronómica?

a) Ávila.
b) Ronda.
c) Lugo.
d) Mérida.

**Clave: d**

Explicación: Solo «Mérida» cumple las 3 condiciones: transporte Barco, participantes inferior a 22 y tipo Gastronómica.

## 39. seed 1177092152084991428 · nivel 1

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Lambda | Valencia | Mixta | 764 | 14 | 346 | 195 |
| Theta | Madrid | Pública | 553 | 16 | 73 | 171 |
| Omega | Sevilla | Mixta | 881 | 17 | 253 | 232 |
| Iota | Sevilla | Privada | 853 | 23 | 291 | 229 |
| Gamma | Barcelona | Mixta | 156 | 9 | 162 | 195 |
| Zeta | Valencia | Mixta | 519 | 17 | 204 | 185 |
| Kappa | Barcelona | Mixta | 421 | 17 | 343 | 128 |
| Sigma | Bilbao | Mixta | 723 | 23 | 363 | 90 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Qué laboratorio tiene el menor cociente entre muestras analizadas y informes emitidos?

a) Omega.
b) Kappa.
c) Theta.
d) Gamma.

**Clave: d**

Explicación: Se divide muestras analizadas entre informes emitidos en cada fila: el menor cociente es el de «Gamma» (0,80).

## 40. seed 2300311533501968391 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Omega | Valencia | Mixta | 297 | 23 | 217 | 137 |
| Iota | Bilbao | Privada | 239 | 23 | 61 | 100 |
| Zeta | Madrid | Privada | 643 | 20 | 388 | 226 |
| Theta | Sevilla | Privada | 927 | 15 | 192 | 250 |
| Delta | Barcelona | Privada | 364 | 24 | 158 | 156 |
| Lambda | Madrid | Pública | 369 | 21 | 184 | 123 |
| Gamma | Madrid | Pública | 674 | 20 | 244 | 265 |
| Épsilon | Sevilla | Privada | 206 | 18 | 71 | 89 |
| Alfa | Madrid | Privada | 505 | 14 | 271 | 35 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Qué laboratorio tiene el menor cociente entre técnicos y informes emitidos?

a) Gamma.
b) Delta.
c) Omega.
d) Theta.

**Clave: d**

Explicación: Se divide técnicos entre informes emitidos en cada fila: el menor cociente es el de «Theta» (0,06).

## 41. seed 4561429966377530467 · nivel 3

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Óscar Lara | Barcelona | Coche | 684 | 223 | 44 | 9 |
| Andrés Peña | Bilbao | Autobús | 894 | 428 | 35 | 3 |
| Luis Parra | Bilbao | Avión | 834 | 427 | 79 | 1 |
| Paula Giner | Madrid | Avión | 630 | 352 | 54 | 4 |
| Elena Soler | Sevilla | Coche | 832 | 150 | 238 | 2 |
| Ana Cortés | Bilbao | Avión | 436 | 389 | 243 | 13 |
| Sara Ortiz | Madrid | Avión | 346 | 251 | 20 | 8 |
| Carla Nieto | Barcelona | Tren | 535 | 449 | 95 | 4 |
| Marta Ríos | Valencia | Coche | 144 | 245 | 32 | 8 |
| Raúl Mena | Valencia | Coche | 518 | 517 | 130 | 4 |
| Víctor Ibarra | Madrid | Autobús | 738 | 454 | 32 | 2 |
| Jorge Luna | Sevilla | Tren | 870 | 511 | 90 | 7 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Cuál es la media de tiempo de todos los empleados?

a) 293,07
b) 366,33
c) 399,64
d) 468,91

**Clave: b**

Explicación: La suma de la columna es 4396,00 y hay 12 filas: 366,33.

## 42. seed 279218220529479154 · nivel 1

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Gamma | Barcelona | Mixta | 733 | 19 | 247 | 242 |
| Kappa | Sevilla | Privada | 834 | 11 | 62 | 116 |
| Sigma | Valencia | Privada | 645 | 10 | 362 | 142 |
| Omega | Bilbao | Pública | 525 | 22 | 172 | 223 |
| Alfa | Sevilla | Pública | 780 | 19 | 80 | 204 |
| Beta | Valencia | Mixta | 610 | 3 | 282 | 271 |
| Delta | Bilbao | Pública | 554 | 18 | 392 | 194 |
| Épsilon | Madrid | Privada | 870 | 12 | 149 | 219 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Qué laboratorio tiene el mayor cociente entre muestras analizadas y informes emitidos?

a) Gamma.
b) Omega.
c) Sigma.
d) Kappa.

**Clave: d**

Explicación: Se divide muestras analizadas entre informes emitidos en cada fila: el mayor cociente es el de «Kappa» (7,19).

## 43. seed 2042550028401227693 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Omega | Barcelona | Privada | 940 | 10 | 46 | 75 |
| Zeta | Valencia | Privada | 177 | 20 | 364 | 65 |
| Beta | Madrid | Mixta | 711 | 16 | 137 | 125 |
| Lambda | Madrid | Mixta | 454 | 7 | 260 | 189 |
| Delta | Sevilla | Pública | 437 | 9 | 67 | 143 |
| Épsilon | Madrid | Privada | 453 | 14 | 246 | 138 |
| Gamma | Madrid | Privada | 515 | 5 | 328 | 161 |
| Theta | Bilbao | Mixta | 170 | 18 | 273 | 204 |
| Sigma | Valencia | Privada | 127 | 10 | 227 | 94 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Qué laboratorio tiene el mayor cociente entre informes emitidos y presupuesto?

a) Theta.
b) Delta.
c) Gamma.
d) Omega.

**Clave: b**

Explicación: Se divide informes emitidos entre presupuesto en cada fila: el mayor cociente es el de «Delta» (2,13).

## 44. seed 1065444377732371285 · nivel 3

Tabla «Excursiones»:

| Destino | Tipo | Transporte | Participantes | Precio por persona (€) | Duración (horas) | Kilómetros |
|---|---|---|---|---|---|---|
| Úbeda | Deportiva | Barco | 48 | 41 | 17 | 369 |
| Lugo | Gastronómica | Barco | 37 | 79 | 16 | 236 |
| Teruel | Deportiva | Tren | 25 | 19 | 16 | 174 |
| Toledo | Gastronómica | Tren | 23 | 40 | 27 | 423 |
| Soria | Cultural | Autobús | 33 | 42 | 25 | 255 |
| Cuenca | Cultural | Autobús | 44 | 16 | 10 | 418 |
| Mérida | Cultural | Autobús | 30 | 44 | 11 | 278 |
| Segovia | Gastronómica | Tren | 25 | 94 | 25 | 134 |
| Ronda | Cultural | Tren | 53 | 49 | 14 | 280 |
| Jaca | Naturaleza | Tren | 15 | 17 | 30 | 308 |
| Ávila | Gastronómica | Tren | 55 | 41 | 9 | 397 |

Responda a la siguiente pregunta según la tabla llamada Excursiones: ¿Qué porcentaje del total de kilómetros corresponde a tipo Deportiva?

a) 13,28 %
b) 16,60 %
c) 21,24 %
d) 14,60 %

**Clave: b**

Explicación: Tipo Deportiva suma 543 de un total de 3272: 16,60 %.

## 45. seed 2719097753412396217 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Kappa | Madrid | Privada | 663 | 14 | 204 | 295 |
| Gamma | Valencia | Privada | 643 | 5 | 263 | 75 |
| Beta | Bilbao | Pública | 531 | 9 | 364 | 182 |
| Épsilon | Valencia | Pública | 126 | 17 | 243 | 140 |
| Alfa | Barcelona | Mixta | 952 | 17 | 72 | 228 |
| Lambda | Sevilla | Mixta | 208 | 20 | 227 | 235 |
| Iota | Sevilla | Pública | 519 | 8 | 173 | 106 |
| Sigma | Madrid | Mixta | 661 | 5 | 233 | 220 |
| Theta | Sevilla | Privada | 447 | 21 | 44 | 284 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: Sumando presupuesto por ciudad, ¿qué ciudad obtiene el menor total?

a) Barcelona.
b) Sevilla.
c) Bilbao.
d) Madrid.

**Clave: a**

Explicación: Los valores por ciudad son Barcelona 72, Bilbao 364, Madrid 437, Sevilla 444, Valencia 506; el menor es Barcelona.

## 46. seed 3969796563389545576 · nivel 2

Tabla «Desplazamientos»:

| Empleado | Destino | Medio | Distancia (km) | Tiempo (min) | Coste (€) | Viajes al año |
|---|---|---|---|---|---|---|
| Raúl Mena | Sevilla | Tren | 216 | 382 | 215 | 5 |
| Óscar Lara | Barcelona | Tren | 679 | 368 | 243 | 11 |
| Paula Giner | Barcelona | Avión | 838 | 348 | 128 | 10 |
| Hugo Beltrán | Bilbao | Coche | 474 | 202 | 109 | 4 |
| Diego Rubio | Barcelona | Coche | 445 | 145 | 38 | 9 |
| Irene Pons | Bilbao | Autobús | 306 | 479 | 52 | 10 |
| Lucía Costa | Madrid | Avión | 828 | 75 | 99 | 6 |
| Andrés Peña | Valencia | Avión | 556 | 130 | 72 | 1 |
| Ana Cortés | Madrid | Avión | 866 | 285 | 138 | 10 |

Responda a la siguiente pregunta según la tabla llamada Desplazamientos: ¿Cuál de los siguientes empleados tiene coste inferior a 81, tiempo inferior a 146 y viajes al año inferior a 2?

a) Paula Giner.
b) Andrés Peña.
c) Lucía Costa.
d) Diego Rubio.

**Clave: b**

Explicación: Solo «Andrés Peña» cumple las 3 condiciones: coste inferior a 81, tiempo inferior a 146 y viajes al año inferior a 2.

## 47. seed 2439017718913394027 · nivel 2

Tabla «Academia»:

| Alumno | Curso | Turno | Edad | Horas semanales | Cuota mensual | Faltas de asistencia |
|---|---|---|---|---|---|---|
| Andrés Peña | Alemán | Mañana | 34 | 11 | 66 | 14 |
| Raúl Mena | Francés | Noche | 52 | 2 | 32 | 7 |
| Ana Cortés | Informática | Tarde | 37 | 10 | 116 | 2 |
| Óscar Lara | Inglés | Mañana | 45 | 9 | 120 | 12 |
| Carla Nieto | Informática | Tarde | 37 | 4 | 101 | 7 |
| Iván Duarte | Informática | Noche | 29 | 11 | 74 | 8 |
| Víctor Ibarra | Inglés | Mañana | 32 | 2 | 87 | 11 |
| Diego Rubio | Alemán | Mañana | 30 | 10 | 108 | 4 |
| Rocío Mora | Inglés | Tarde | 40 | 4 | 53 | 2 |
| Lucía Costa | Inglés | Tarde | 31 | 4 | 90 | 12 |

Responda a la siguiente pregunta según la tabla llamada Academia: ¿Cuál de los siguientes alumnos tiene horas semanales superior a 10, cuota mensual inferior a 83 y edad inferior a 32?

a) Diego Rubio.
b) Lucía Costa.
c) Andrés Peña.
d) Iván Duarte.

**Clave: d**

Explicación: Solo «Iván Duarte» cumple las 3 condiciones: horas semanales superior a 10, cuota mensual inferior a 83 y edad inferior a 32.

## 48. seed 2169652614732583283 · nivel 2

Tabla «Préstamos»:

| Título | Lugar de edición | Editorial | Año de publicación | Ejemplares disponibles | Ejemplares prestados | Préstamos realizados |
|---|---|---|---|---|---|---|
| Un calor tan cercano | Madrid | Planeta | 1998 | 7 | 2 | 175 |
| El amante lesbiano | Barcelona | Destino | 2003 | 7 | 1 | 222 |
| Hija de la fortuna | Madrid | Planeta | 2003 | 13 | 3 | 210 |
| Adiós a las novias | Madrid | Alfaguara | 2003 | 4 | 8 | 344 |
| Cuaderno de bitácora | Sevilla | Santillana | 2005 | 7 | 7 | 213 |
| Noches de invierno | Madrid | Destino | 1997 | 4 | 9 | 181 |
| Tiempo de ceniza | Valencia | Santillana | 2001 | 5 | 1 | 118 |
| El jardín cerrado | Barcelona | Santillana | 1997 | 11 | 2 | 133 |
| Entre visillos | Barcelona | Alfaguara | 2001 | 4 | 6 | 235 |
| Aranmanoth | Valencia | Anagrama | 2004 | 15 | 2 | 107 |

Responda a la siguiente pregunta según la tabla llamada Préstamos: ¿Cuál de los siguientes títulos tiene año de publicación inferior a 2253, lugar de edición Madrid, ejemplares disponibles inferior a 5 y préstamos realizados superior a 301?

a) El amante lesbiano.
b) Noches de invierno.
c) Hija de la fortuna.
d) Adiós a las novias.

**Clave: d**

Explicación: Solo «Adiós a las novias» cumple las 4 condiciones: año de publicación inferior a 2253, lugar de edición Madrid, ejemplares disponibles inferior a 5 y préstamos realizados superior a 301.

## 49. seed 4533545574814537803 · nivel 3

Tabla «Préstamos»:

| Título | Lugar de edición | Editorial | Año de publicación | Ejemplares disponibles | Ejemplares prestados | Préstamos realizados |
|---|---|---|---|---|---|---|
| Entre visillos | Madrid | Alfaguara | 1999 | 15 | 8 | 310 |
| Hija de la fortuna | Barcelona | Santillana | 2002 | 18 | 7 | 324 |
| El amante lesbiano | Barcelona | Planeta | 1998 | 9 | 6 | 313 |
| Aranmanoth | Madrid | Planeta | 2002 | 14 | 7 | 321 |
| Contra vosotros | Madrid | Anagrama | 2000 | 5 | 4 | 264 |
| La temporada de caza | Sevilla | Anagrama | 2003 | 9 | 5 | 262 |
| Tiempo de ceniza | Sevilla | Planeta | 1997 | 20 | 9 | 346 |
| El jardín cerrado | Madrid | Alfaguara | 2004 | 5 | 7 | 243 |
| Cuaderno de bitácora | Barcelona | Alfaguara | 2001 | 11 | 5 | 343 |
| La casa del lago | Valencia | Destino | 1996 | 4 | 9 | 178 |
| El último tren | Sevilla | Santillana | 2001 | 20 | 7 | 263 |

Responda a la siguiente pregunta según la tabla llamada Préstamos: ¿Qué título tiene el menor cociente entre ejemplares disponibles y año de publicación?

a) Cuaderno de bitácora.
b) La casa del lago.
c) La temporada de caza.
d) El amante lesbiano.

**Clave: b**

Explicación: Se divide ejemplares disponibles entre año de publicación en cada fila: el menor cociente es el de «La casa del lago» (0,00).

## 50. seed 3814695743816065413 · nivel 2

Tabla «Laboratorios»:

| Laboratorio | Ciudad | Titularidad | Muestras analizadas | Técnicos | Presupuesto (miles de €) | Informes emitidos |
|---|---|---|---|---|---|---|
| Sigma | Sevilla | Mixta | 876 | 15 | 71 | 99 |
| Lambda | Valencia | Mixta | 928 | 15 | 232 | 42 |
| Alfa | Sevilla | Mixta | 702 | 5 | 295 | 182 |
| Zeta | Valencia | Mixta | 517 | 7 | 200 | 172 |
| Iota | Barcelona | Privada | 597 | 5 | 166 | 166 |
| Omega | Bilbao | Mixta | 242 | 16 | 78 | 88 |
| Beta | Madrid | Privada | 433 | 10 | 205 | 222 |
| Épsilon | Valencia | Privada | 661 | 20 | 238 | 146 |
| Kappa | Bilbao | Pública | 538 | 14 | 119 | 32 |

Responda a la siguiente pregunta según la tabla llamada Laboratorios: ¿Cuántos laboratorios tienen informes emitidos inferior a 164 y ciudad Valencia?

a) 1
b) 4
c) 3
d) 2

**Clave: d**

Explicación: Cumplen las condiciones (informes emitidos inferior a 164 y ciudad Valencia) exactamente 2.
