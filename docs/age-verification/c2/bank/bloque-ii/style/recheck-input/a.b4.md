# Strict recheck input — group a, batch 4 (60 candidates)

## m02-l05-q018
¿Con cuál de los siguientes nombres se refiere también la formación de Microsoft sobre almacenamiento a la memoria de acceso aleatorio (RAM)?
- a) Memoria a largo plazo.
- b) Memoria a corto plazo.  ✓
- c) Almacenamiento magnético.
- d) Almacenamiento digital.
Cita: fuente: `ms-learn-equipos-almacenamiento.html`; «Comprender el almacenamiento»
Explicación: La página dice: «Este tipo de memoria, memoria de acceso aleatorio, también se denomina memoria a corto plazo». La memoria a largo plazo es el «almacenamiento», el segundo tipo de memoria, y el almacenamiento magnético y el digital son los dos tipos principales de ese almacenamiento.

## m02-l05-q019
Señale la afirmación correcta sobre la memoria RAM frente a las demás partes de un equipo, según la formación de Microsoft sobre la memoria de acceso aleatorio:
- a) Tiende a ser lenta, aunque es la parte más barata.
- b) Tiende a ser rápida y es la parte más barata.
- c) Tiende a ser rápida, pero puede costar bastante dinero.  ✓
- d) Tiende a ser lenta y conviene comprar la mínima.
Cita: fuente: `ms-learn-equipos-ram.html`; «Examen de la memoria de acceso aleatorio»
Explicación: La página dice que la RAM «tiende a ser rápida» pero «puede costar dinero significativo en relación con las otras partes del equipo», y aconseja comprar «lo máximo que uno pueda permitirse». Las opciones que la describen como lenta o como la parte más barata, o que aconsejan comprar la mínima, contradicen esas frases.

## m02-l05-q020
Según la documentación de Microsoft sobre las funciones de manipulación de bits, ¿cuántos valores distintos puede tomar un bit y cuáles son?
- a) Ocho valores: del 0 al 7.
- b) Diez valores: del 0 al 9.
- c) Dieciséis valores: del 0 al 15.
- d) Dos valores: 1 o 0.  ✓
Cita: fuente: `ms-sql-bits.html`; «Funciones de manipulación de bits»
Explicación: La página dice: «Un bit tiene dos valores (1 o 0, que representan on o off, o true o false)». Ocho, diez o dieciséis valores no corresponden a un bit; ocho es el número de bits de un byte.

## m02-l05-q021
¿Cuál de las siguientes definiciones de byte da la documentación de Microsoft sobre las funciones de manipulación de bits de SQL Server?
- a) Una secuencia de 8 bits.  ✓
- b) Una secuencia de 2 bits.
- c) Una secuencia de 10 bits.
- d) Una secuencia de 16 bits.
Cita: fuente: `ms-sql-bits.html`; «Funciones de manipulación de bits»
Explicación: La página dice: «Un byte se compone de una secuencia de 8 bits». Dos, diez o dieciséis bits son cifras distintas; dos es el número de valores que puede tomar un bit.

## m02-l05-q022
Según la documentación de Microsoft sobre manipulación de bits, ¿a qué número decimal equivale la secuencia binaria 00000111, calculada con potencias de 2?
- a) Al número 3.
- b) Al número 7.  ✓
- c) Al número 111.
- d) Al número 8.
Cita: fuente: `ms-sql-bits.html`; «Funciones de manipulación de bits»
Explicación: La página lo calcula así: 00000111 = 2^2 + 2^1 + 2^0 = 4 + 2 + 1 = 7. El 3 suma solo dos de los tres bits a 1, el 111 lee la secuencia como si fuera decimal y el 8 es 2^3, un bit que en esta secuencia vale 0.

## m02-l05-q023
Con el prefijo decimal giga del Sistema Internacional de Unidades, y no con el prefijo binario gibi, ¿cuántos bytes son 1 gigabyte (1 GB)?
- a) 1.073.741.824 bytes (2^30).
- b) 1.000.000 bytes (10^6).
- c) 1.000.000.000 bytes (10^9).  ✓
- d) 1.048.576 bytes (2^20).
Cita: fuente: `nist-prefijos-binarios.html`; «Examples and comparisons with SI prefixes»
Explicación: El NIST da 1 GB = 10^9 B = 1.000.000.000 B. 1.073.741.824 bytes es 1 GiB, con el prefijo binario gibi (2^30) que el enunciado excluye; 1.000.000 bytes es 1 MB; y 1.048.576 bytes es 1 MiB (2^20).

## m02-l05-q024
¿Cuál de las siguientes igualdades es correcta si se usan los prefijos decimales del Sistema Internacional de Unidades para los múltiplos del byte?
- a) 1 GB equivale a 1.000 KB.
- b) 1 MB equivale a 1.000 GB.
- c) 1 TB equivale a 1.000 MB.
- d) 1 GB equivale a 1.000 MB.  ✓
Cita: fuente: `nist-prefijos-binarios.html`; «Examples and comparisons with SI prefixes»
Explicación: El NIST da 1 MB = 10^6 B y 1 GB = 10^9 B, así que 1 GB son 10^9 / 10^6 = 1.000 MB. Con kilo = 10^3, 1 GB son 1.000.000 KB, no 1.000; 1 MB es la milésima parte de un GB, no mil GB; y tera = (10^3)^4 hace que 1 TB sean 1.000.000 MB.

## m02-l05-q025
¿Qué prefijo del Sistema Internacional de Unidades sigue inmediatamente al prefijo peta en la escala de múltiplos del byte, según la tabla del NIST?
- a) Exa (E), de factor (10^3)^6.  ✓
- b) Exbi (Ei), de factor (2^10)^6.
- c) Pebi (Pi), de factor (2^10)^5.
- d) Giga (G), de factor (10^3)^3.
Cita: fuente: `nist-prefijos-binarios.html`; «Prefixes for binary multiples»
Explicación: En la tabla del NIST, peta vale (10^3)^5 y exa vale (10^3)^6: exa es el siguiente prefijo decimal. Exbi y pebi son prefijos binarios, que según el NIST no forman parte del Sistema Internacional; y giga, (10^3)^3, está por debajo de peta.

## m02-l05-q026
Señale qué ocurre con una directiva de la organización cuando se restauran los firewalls a los valores predeterminados en Windows 11:
- a) Se vuelve a aplicar tras restaurar el firewall.  ✓
- b) Se elimina de forma definitiva del dispositivo.
- c) Se ignora hasta que se reinicia el equipo.
- d) Se sustituye por la configuración de la red pública.
Cita: fuente: `ms-win-firewall.html`; «Firewall y protección de red en la aplicación Seguridad de Windows»
Explicación: La página dice que, al restaurar los valores predeterminados, «si su organización ha aplicado alguna directiva para configurar el firewall, se volverá a aplicar». La directiva no se elimina, no espera a un reinicio y no se sustituye por la configuración de la red pública.

## m02-l05-q028
¿Cuál de los siguientes elementos suele contener el correo o mensaje de un phishing, según el glosario de ciberseguridad del INCIBE?
- a) Un código de un solo uso generado por la entidad suplantada en ese momento.
- b) Un certificado digital emitido por una Autoridad Certificadora reconocida.
- c) Un enlace, o un fichero que lo contiene, a un sitio web que suplanta al legítimo.  ✓
- d) Un programa que cifra los ficheros del equipo a cambio de un rescate económico para devolverlos.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Phishing»
Explicación: El glosario dice que ese correo o mensaje «suele tener un enlace (o fichero que contiene ese enlace) a un sitio web que suplanta al legítimo y que usan para engañarlo». Una contraseña de un solo uso es otra figura del glosario, que se genera en un dispositivo o aplicación en el momento de su utilización. El certificado digital es un fichero que asocia datos de identidad, y el glosario no lo relaciona con el contenido del mensaje de phishing. Cifrar o secuestrar a cambio de un rescate es el ransomware, no el contenido que el glosario atribuye al phishing.

## m02-l05-q029
¿Cuál de los siguientes términos aparece en el glosario de ciberseguridad del INCIBE como sinónimo de phishing?
- a) Pharming.
- b) Smishing.  ✓
- c) Spoofing.
- d) Scam.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Phishing»
Explicación: El glosario da como sinónimos de phishing «vishing» y «smishing». El glosario define el pharming como un ataque que aprovecha una vulnerabilidad de los servidores DNS, no como sinónimo de phishing. El glosario define el spoofing como una técnica de suplantación de identidad en la Red, no como sinónimo de phishing. El glosario define el scam como una estafa por medios electrónicos, no como sinónimo de phishing.

## m02-l05-q030
Según el glosario de ciberseguridad del INCIBE, ¿cuál de las siguientes definiciones corresponde al spear phishing?
- a) Una modalidad de phishing dirigida contra un usuario u organización en concreto.  ✓
- b) Una modalidad de phishing que se envía de forma masiva a cualquier usuario.
- c) Un ataque que modifica el archivo del servidor DNS para redirigir al usuario.
- d) Una estafa por medios electrónicos que ofrece productos o servicios falsos a las víctimas.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Spear phishing»
Explicación: El glosario define el spear phishing como una «modalidad de phishing dirigido contra un usuario u organización en concreto», con un correo que aparenta ser de un amigo o de una empresa conocida. Modificar el archivo del servidor de nombres de dominio para redirigir al usuario es el pharming, y la estafa por medios electrónicos con productos o servicios falsos es el scam.

## m02-l05-q031
¿Cuál de las siguientes expresiones corresponde, en español, a las siglas CAPTCHA, según el glosario de ciberseguridad del INCIBE?
- a) La herramienta o troyano de administración remota que usan habitualmente los ciberdelincuentes.
- b) El número de identificación personal, un tipo de contraseña generalmente de cuatro dígitos.
- c) La prueba de Turing completamente automática y pública que diferencia ordenadores de humanos.  ✓
- d) El identificador de conjunto de servicios que distingue una red wifi de otras de la zona.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Captcha»
Explicación: El glosario define CAPTCHA como acrónimo de Completely Automated Public Turing test to tell Computers and Humans Apart, en español «prueba de Turing completamente automática y pública para diferenciar ordenadores de humanos». El glosario define esas siglas como Remote Administration Tool, herramienta o troyano de administración remota; son las de RAT. El glosario define esas siglas como Personal Identification Number, número de identificación personal; son las de PIN. El glosario define esas siglas como Service Set Identifier, identificador de conjunto de servicios; son las de SSID.

## m02-l05-q032
¿Cuál de los siguientes tipos de pruebas consiste en realizar un CAPTCHA, según el glosario de ciberseguridad del INCIBE?
- a) Pruebas de carga que miden la velocidad de una red.
- b) Pruebas de intrusión que buscan vulnerabilidades del sistema.
- c) Pruebas de cifrado que comprueban la clave del usuario.
- d) Pruebas desafío-respuesta controladas por máquinas.  ✓
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Captcha»
Explicación: El glosario define el CAPTCHA como «un tipo de medida de seguridad que consiste en la realización de pruebas desafío-respuesta controladas por máquinas». Medir la velocidad y calidad de una red es lo que hace la utilidad Ping, y las pruebas de intrusión y de cifrado no figuran en esa definición.

## m02-l05-q033
Según el glosario de ciberseguridad del INCIBE, un certificado digital lo genera una entidad denominada:
- a) la Autoridad Certificadora (CA).  ✓
- b) la autoridad de validación.
- c) el proveedor de acceso.
- d) el sello de confianza.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Certificado digital»
Explicación: El glosario define el certificado digital como «un fichero informático generado por una entidad denominada Autoridad Certificadora (CA)» que asocia unos datos de identidad a una persona física, organismo o empresa. El glosario dice que la autoridad de validación informa de la vigencia y validez de los certificados, no que los genere. El glosario define el proveedor de acceso como el prestador de servicios que proporciona a sus usuarios acceso a redes de telecomunicaciones. El glosario define los sellos de confianza como distintivos de calidad de una actividad comercial en Internet.

## m02-l05-q034
Según el glosario de ciberseguridad del INCIBE, ¿cuál de las siguientes funciones es la principal de un certificado digital?
- a) Cifrar las comunicaciones, aunque también puede autenticar al poseedor.
- b) Firmar digitalmente, aunque también puede autenticar al poseedor del certificado.
- c) Autenticar al poseedor, aunque también puede cifrar comunicaciones y firmar digitalmente.  ✓
- d) Proteger el equipo frente al software malicioso, aunque también puede autenticar.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Certificado digital»
Explicación: El glosario dice que el certificado digital «tiene como función principal autenticar al poseedor pero puede servir también para cifrar las comunicaciones y firmar digitalmente». Cifrar y firmar son, por tanto, funciones posibles y no la principal, y proteger frente al software malicioso es la función del antivirus.

## m02-l05-q035
¿Por qué es necesaria la colaboración de un tercero de confianza en un certificado digital, según el glosario de ciberseguridad del INCIBE?
- a) Porque el certificado autentica a un usuario o sitio web ante las partes de la comunicación.  ✓
- b) Porque el tercero cifra todas las comunicaciones del usuario con el sitio web que visita.
- c) Porque el tercero conserva la contraseña de cada usuario que posee un certificado.
- d) Porque el tercero sustituye al usuario cuando este no dispone de conexión a Internet.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Certificado digital»
Explicación: El glosario dice que el certificado digital «es válido para autenticar la existencia y validez de un usuario o sitio web, por lo que es necesaria la colaboración de un tercero que sea de confianza para cualquiera de las partes que participe en la comunicación». El tercero se justifica por esa autenticación, y no por cifrar las comunicaciones, guardar contraseñas o sustituir al usuario.

## m02-l05-q036
Según el glosario de ciberseguridad del INCIBE, ¿cuál de las siguientes opciones puede ser la Autoridad Certificadora que genera un certificado digital?
- a) Solo un organismo público de la Administración del Estado.
- b) Un organismo público o una empresa reconocida en Internet.  ✓
- c) Solo una empresa privada con licencia de software propio.
- d) Cualquier usuario que disponga de un equipo conectado a Internet.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Certificado digital»
Explicación: El glosario dice que la Autoridad Certificadora puede ser «un organismo público o empresa reconocida en Internet». Por eso no es solo un organismo público, ni solo una empresa privada, ni cualquier usuario: es una entidad de confianza.

## m02-l05-q037
¿Cuál de las siguientes descripciones corresponde a una contraseña robusta, según el glosario de ciberseguridad del INCIBE?
- a) Corta y generada por defecto o con nombres propios y fechas significativas.
- b) Asignada por el fabricante de un dispositivo a todos los aparatos que fabrica.
- c) Válida para un solo uso, generada por un dispositivo o aplicación al usarla.
- d) Larga, creada al azar o con mayúsculas, minúsculas, números y caracteres especiales.  ✓
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Contraseña robusta»
Explicación: El glosario define la contraseña robusta como la «suficientemente larga, que se crea al azar o mediante la combinación de caracteres alfanuméricos (letras mayúsculas y minúsculas, números y caracteres especiales)». Corta y generada por defecto es la contraseña débil, asignada por el fabricante es la predeterminada y válida para un solo uso es la contraseña de un solo uso.

## m02-l05-q038
Señale la característica de una contraseña débil, según la definición del glosario de ciberseguridad del INCIBE:
- a) Es larga y se crea al azar combinando letras, números y caracteres especiales.
- b) Se cifra y se guarda en un programa integrado en los principales navegadores.
- c) Es corta y se genera por defecto o con nombres propios o fechas significativas.  ✓
- d) Solo sirve una vez y la genera un dispositivo en el momento de utilizarla.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Contraseña débil»
Explicación: El glosario describe la contraseña débil como la «corta» y «generada por defecto o mediante el uso de nombres propios, variaciones del nombre del usuario o fechas significativas», que se puede adivinar de forma rápida con diccionarios. Larga y creada al azar es la contraseña robusta, cifrada y guardada en un programa es lo que hace el gestor de contraseñas, y valer para un solo uso es la contraseña de un solo uso.

## m02-l05-q039
¿Cuál de las siguientes recomendaciones da el glosario de ciberseguridad del INCIBE sobre las contraseñas asignadas por el fabricante de un dispositivo o software?
- a) Conservarlas, porque el fabricante las ha generado de forma segura.
- b) Cambiarlas siempre, porque se consideran una vulnerabilidad.  ✓
- c) Cambiarlas solo cuando el dispositivo se conecta a Internet.
- d) Anotarlas en el manual de puesta en marcha del dispositivo.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Contraseña predeterminada»
Explicación: El glosario dice que las contraseñas predeterminadas se consideran «una vulnerabilidad, aprovechada por los ciberdelincuentes a menudo para acceder a los dispositivos sin autorización», y que «la recomendación es cambiar siempre las contraseñas por defecto». El glosario las considera una vulnerabilidad y recomienda cambiarlas siempre. El glosario recomienda cambiarlas siempre, no solo en un caso. El glosario dice que figuran en los manuales de puesta en marcha, y de ahí la vulnerabilidad: recomienda cambiarlas.

## m02-l05-q040
¿Cuál de las siguientes definiciones corresponde a un gestor de contraseñas, según el glosario de ciberseguridad del INCIBE?
- a) Programa integrable en los navegadores que genera contraseñas robustas y las guarda cifradas.  ✓
- b) Software de protección que evita que se ejecute software malicioso en el equipo infectado.
- c) Fichero generado por una Autoridad Certificadora que asocia datos de identidad a personas.
- d) Prueba de desafío-respuesta que distingue a un humano de un programa automático o bot.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Gestor de contraseñas»
Explicación: El glosario define el gestor de contraseñas como un «programa o aplicación que se puede integrar en los principales navegadores y que permite generar contraseñas robustas y almacenarlas cifradas». Evitar que se ejecute software malicioso es la función del antivirus, asociar datos de identidad es la del certificado digital y distinguir a un humano de un bot es la del CAPTCHA.

## m02-l05-q041
¿Cuál de las siguientes contraseñas basta recordar al usar un gestor de contraseñas, según el glosario de ciberseguridad del INCIBE?
- a) La contraseña de cada sitio web y aplicación.
- b) El nombre de usuario y la contraseña de cada servicio.
- c) El código de un solo uso de cada inicio de sesión.
- d) Solo la contraseña de acceso al gestor.  ✓
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Gestor de contraseñas»
Explicación: El glosario dice que el gestor permite tener contraseñas diferentes por cada sitio «con la facilidad de tener que recordar solo la contraseña de acceso al gestor». El glosario dice que basta recordar solo la contraseña de acceso al gestor, y no la de cada sitio. El glosario dice que el gestor almacena los nombres de usuario junto con las contraseñas y basta recordar solo la de acceso al gestor. El glosario dice que basta recordar solo la contraseña de acceso al gestor, no códigos de un solo uso.

## m02-l05-q042
Según el glosario de ciberseguridad del INCIBE, ¿para qué es requerido el certificado digital en algunas administraciones públicas y empresas privadas?
- a) Para ciertos trámites con intercambio de información sensible entre las partes.  ✓
- b) Para acceder a cualquier página web que use el protocolo HTTP sin cifrar.
- c) Para instalar software con licencia legal en cualquier equipo de la organización.
- d) Para enviar correos electrónicos a otros usuarios de la propia organización.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Certificado digital»
Explicación: El glosario dice que el certificado digital, en algunas administraciones públicas y empresas privadas, es requerido «para poder realizar ciertos trámites que involucren intercambio de información sensible entre las partes». No se exige para acceder a cualquier página web ni para enviar correos, y lo que acompaña a un software con licencia legal es el certificado de autenticidad (COA), una etiqueta.

## m02-l05-q043
¿Qué ocurre en Windows 11 con algunas actualizaciones de Windows si el dispositivo tiene una conexión de uso medido, según la página de preguntas frecuentes de Windows Update?
- a) Se instalan automáticamente, pero sin reiniciar.
- b) Se descargan más rápido que con otras conexiones.
- c) No se instalan automáticamente en ese dispositivo.  ✓
- d) Se desinstalan para ahorrar datos del plan.
Cita: fuente: `ms-win-update.html`; «Windows Update: Preguntas más frecuentes»
Explicación: La página dice que, con una conexión de uso medido, «algunas actualizaciones de Windows no se instalarán automáticamente». No se instalan sin reiniciar, ni se descargan más rápido, ni se desinstalan.

## m02-l05-q044
¿Qué objetivos tiene una actualización de seguridad en un dispositivo, según el glosario de ciberseguridad del INCIBE?
- a) Únicamente añadir nuevas funcionalidades al software instalado en el dispositivo del usuario.
- b) Solo identificar un tipo de malware en concreto mediante una base de datos.
- c) Solo duplicar la información de un soporte a otro para poder recuperarla.
- d) Corregir fallos de seguridad y de funcionamiento, y mejorar funciones y rendimiento.  ✓
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Actualización de seguridad»
Explicación: El glosario define la actualización de seguridad como las modificaciones que se aplican en el software «con el objetivo de corregir fallos de seguridad, errores de funcionamiento o bien para dotar a los dispositivos de nuevas funcionabilidades, así como incorporar mejoras de rendimiento». Identificar tipos de malware es lo que hace la firma antivirus y duplicar información de un soporte a otro es la copia de seguridad.

## m02-l05-q045
Según el glosario de ciberseguridad del INCIBE, un sinónimo de «actualización de seguridad», la modificación del software, es:
- a) Parches de seguridad.  ✓
- b) Firmas antivirus.
- c) Copias de seguridad.
- d) Contraseñas predeterminadas.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Actualización de seguridad»
Explicación: El glosario da como sinónimo de la actualización de seguridad los «parches de seguridad». La firma antivirus es una entrada de la base de datos del antivirus, la copia de seguridad duplica información de un soporte a otro y las contraseñas predeterminadas son las asignadas por el fabricante.

## m02-l05-q046
¿Cómo descarga e instala Windows 11 las actualizaciones, según la página de preguntas frecuentes de Windows Update?
- a) Solo cuando el usuario las solicita desde Configuración o Windows Update.
- b) Solo cuando el usuario conecta el dispositivo a una red doméstica.
- c) Solo cuando el usuario reinicia el dispositivo cada día de la semana.
- d) Automáticamente, para que el dispositivo sea seguro y esté actualizado.  ✓
Cita: fuente: `ms-win-update.html`; «Windows Update: Preguntas más frecuentes»
Explicación: La página dice que Windows 11 «descarga e instala actualizaciones automáticamente para asegurarse de que tu dispositivo sea seguro y esté actualizado». No espera a que el usuario las solicite, ni a una red doméstica, ni a un reinicio diario.

## m02-l05-q047
En Windows 11, ¿qué ruta lleva a buscar actualizaciones manualmente, según la página de preguntas frecuentes de Windows Update?
- a) Inicio › Configuración › Cuentas › Windows Update
- b) Inicio › Configuración › Windows Update  ✓
- c) Inicio › Configuración › Sistema › Windows Update
- d) Inicio › Configuración › Seguridad de Windows › Windows Update
Cita: fuente: `ms-win-update.html`; «Windows Update: Preguntas más frecuentes»
Explicación: La página dice que, para buscar actualizaciones manualmente, se selecciona Inicio, Configuración y Windows Update. Windows Update está directamente en Configuración, no dentro de Cuentas, Sistema ni Seguridad de Windows.

## m02-l05-q048
En Windows 11, ¿qué opción de Windows Update permite detener temporalmente la descarga e instalación de las actualizaciones?
- a) Programar el reinicio.
- b) Historial de actualizaciones.
- c) Pausar actualizaciones.  ✓
- d) Buscar actualizaciones.
Cita: fuente: `ms-win-update.html`; «Windows Update: Preguntas más frecuentes»
Explicación: La página dice que, en Windows 11, junto a «Pausar actualizaciones» se selecciona la duración de pausa que se prefiera. Programar el reinicio sirve para elegir un momento conveniente para reiniciar, no para detener la descarga. El historial de actualizaciones muestra las actualizaciones instaladas y cuándo se instalaron. Buscar actualizaciones comprueba manualmente si hay actualizaciones, no las detiene.

## m02-l05-q049
En Windows 11, ¿qué opción de Windows Update permite elegir un momento conveniente para reiniciar el dispositivo e instalar una actualización?
- a) Pausar actualizaciones.
- b) Programar el reinicio.  ✓
- c) Desinstalar actualizaciones.
- d) Ver el historial de actualizaciones.
Cita: fuente: `ms-win-update.html`; «Windows Update: Preguntas más frecuentes»
Explicación: La página dice que, para programar el reinicio, se selecciona «Programar el reinicio» y se elige un momento conveniente. Pausar actualizaciones detiene temporalmente la descarga e instalación, con la duración que se elija. Desinstalar actualizaciones quita una actualización ya instalada. El historial de actualizaciones muestra las actualizaciones instaladas y cuándo se instalaron.

## m02-l05-q050
¿Cuál de las siguientes series recoge los tres tipos de factor de la autenticación multifactor de Microsoft Entra?
- a) Algo que sabes, algo que firmas y algo que eres.
- b) Algo que sabes, algo que tienes y algo que eres.  ✓
- c) Algo que sabes, algo que tienes y algo que ves.
- d) Algo que usas, algo que tienes y algo que eres.
Cita: fuente: `ms-entra-mfa.html`; «El funcionamiento de la autenticación multifactor de Microsoft Entra se basa en exigir uno o varios de los siguientes métodos de autenticación:»
Explicación: La página de Microsoft Entra enumera tres métodos: algo que tú sabes, normalmente una contraseña; algo que tiene, como un teléfono o una clave de hardware; y algo que eres, biometría como una huella digital o un escaneo facial. La serie con «algo que firmas» cambia el segundo método y la de «algo que ves» cambia el tercero, y ninguno aparece en la lista de la página. La serie con «algo que usas» sustituye al primero, que la página define como algo que sabes.

## m02-l05-q051
En Windows 11, ¿cuál de las siguientes series recoge los tres perfiles de red que se pueden seleccionar en el Firewall de Windows?
- a) Red de dominio, red privada y red pública.  ✓
- b) Red de dominio, red doméstica y red pública.
- c) Red corporativa, red privada y red pública.
- d) Red de dominio, red privada y red de invitados.
Cita: fuente: `ms-win-firewall.html`; «Selecciona un perfil de red: Red de dominio, Red privada, o Red pública.»
Explicación: La página de Seguridad de Windows dice: «Selecciona un perfil de red: Red de dominio, Red privada, o Red pública». La serie con «red doméstica» cambia el perfil de red privada, que es el que la página ilustra con la red doméstica como ejemplo. La serie con «red corporativa» cambia el perfil de red de dominio, y la de «red de invitados» sustituye al perfil de red pública. Ninguno de esos tres nombres es un perfil de la página.

## m02-l05-q052
Según el glosario de ciberseguridad del INCIBE, un certificado digital asocia unos datos de identidad a:
- a) un equipo informático, un programa instalado o una red local.
- b) una carpeta, un fichero o una unidad de almacenamiento.
- c) una dirección de correo, una contraseña o un código PIN.
- d) una persona física, un organismo o una empresa.  ✓
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Un certificado digital es un fichero informático generado por una entidad denominada Autoridad Certificadora (CA) que asocia unos datos de identidad a una persona física, organismo o empresa confirmando de esta manera su identidad digital en Internet.»
Explicación: El glosario del INCIBE dice que el certificado digital, generado por una Autoridad Certificadora, asocia unos datos de identidad a una persona física, organismo o empresa, y así confirma su identidad digital en Internet. Un equipo, un programa o una red, una carpeta, un fichero o una unidad, y una dirección de correo, una contraseña o un PIN no figuran entre lo que el glosario dice que el certificado identifica.

## m02-l05-q053
En Windows 11, ¿qué ocurre cuando se alcanza el límite de pausa de las actualizaciones de Windows Update?
- a) La pausa se renueva sola otro periodo igual sin instalar nada.
- b) Hay que instalar las últimas actualizaciones para poder volver a pausarlas.  ✓
- c) Windows Update se desactiva de forma permanente en el dispositivo.
- d) Las actualizaciones pendientes se eliminan y dejan de ofrecerse.
Cita: fuente: `ms-win-update.html`; «Ten en cuenta que una vez que se alcance el límite de pausa, tendrás que instalar las últimas actualizaciones para poder volver a pausar las actualizaciones.»
Explicación: La página de Windows Update dice que, una vez alcanzado el límite de pausa, hay que instalar las últimas actualizaciones para poder volver a pausarlas. La renovación automática de la pausa sin instalar nada contradice esa frase. Que Windows Update se desactive de forma permanente o que se eliminen las pendientes contradice la página, que dice que las actualizaciones no se pueden detener por completo y que finalmente será necesario descargarlas e instalarlas.

## m02-l05-q054
¿Cuál de los siguientes ejemplos corresponde al método «algo que eres» de la autenticación multifactor de Microsoft Entra?
- a) Una contraseña elegida por el usuario.
- b) Un teléfono de confianza del usuario.
- c) Una clave de hardware del usuario.
- d) Una huella digital del usuario.  ✓
Cita: fuente: `ms-entra-mfa.html`; «El funcionamiento de la autenticación multifactor de Microsoft Entra se basa en exigir uno o varios de los siguientes métodos de autenticación:»
Explicación: La página define «algo que eres» como «biometría como una huella digital o un escaneo facial». La contraseña es el ejemplo de «algo que tú sabes», y el teléfono y la clave de hardware son ejemplos de «algo que tiene», un dispositivo de confianza que no se puede duplicar con facilidad.

## m02-l05-q055
Según la norma de la Comisión Electrotécnica Internacional que recoge el NIST para los múltiplos binarios, ¿qué factor corresponde al prefijo gibi (Gi)?
- a) 10^9, es decir, (10^3)^3.
- b) 2^30, es decir, (2^10)^3.  ✓
- c) 2^20, es decir, (2^10)^2.
- d) 2^40, es decir, (2^10)^4.
Cita: fuente: `nist-prefijos-binarios.html`; «Prefixes for binary multiples»
Explicación: En la tabla del NIST, gibi vale 2^30 = (2^10)^3, el «gigabinary». 10^9 es el factor del prefijo decimal giga, 2^20 es el de mebi y 2^40 el de tebi.

## m02-l05-q056
Señale la afirmación correcta sobre los prefijos para múltiplos binarios (kibi, mebi, gibi y siguientes) según la página del NIST que los recoge:
- a) Forman parte del Sistema Internacional desde que la IEC los aprobó en 1998.
- b) Tienen el mismo valor que los prefijos decimales kilo, mega y giga.
- c) No forman parte del Sistema Internacional, aunque se derivaron de sus prefijos decimales.  ✓
- d) Su nombre se forma añadiendo «bi» al nombre completo del prefijo decimal.
Cita: fuente: `nist-prefijos-binarios.html`; «Prefixes for binary multiples»
Explicación: El NIST dice que los nuevos prefijos binarios «no son parte del Sistema Internacional de Unidades», aunque se derivaron de los prefijos del SI. La IEC los aprobó en 1998 como norma de la IEC, no del SI; kibi vale 2^10 y kilo 10^3, así que no valen lo mismo; y el nombre conserva solo las dos primeras letras del prefijo decimal y añade «bi».

## m02-l05-q057
Según el NIST, ¿cómo se forma el símbolo de cada prefijo para múltiplos binarios a partir del símbolo del prefijo decimal correspondiente?
- a) Añadiendo las letras «bi», que recuerdan la palabra binario.
- b) Duplicando la letra del símbolo del prefijo decimal.
- c) Escribiendo en minúscula el símbolo del prefijo decimal.
- d) Añadiendo la letra «i», que recuerda la palabra binario.  ✓
Cita: fuente: `nist-prefijos-binarios.html`; «Prefixes for binary multiples»
Explicación: El NIST dice que el símbolo de cada prefijo binario se obtiene del símbolo del prefijo del SI «añadiendo la letra "i"». Las letras «bi» se añaden al nombre, no al símbolo; no se duplica ninguna letra; y la minúscula tampoco es la regla: para 2^10 se usa Ki, con mayúscula, y no ki.

## m02-l05-q058
Según los ejemplos del NIST para los prefijos de múltiplos binarios, un mebibyte (1 MiB), es decir, 2^20 bytes, equivale exactamente a:
- a) 1.048.576 bytes.  ✓
- b) 1.000.000 bytes.
- c) 1.024.000 bytes.
- d) 1.073.741.824 bytes.
Cita: fuente: `nist-prefijos-binarios.html`; «Examples and comparisons with SI prefixes»
Explicación: El NIST da 1 MiB = 2^20 B = 1.048.576 B. 1.000.000 bytes es 1 MB, con el prefijo decimal; 1.024.000 bytes es el megabyte con que se formatea el disquete de «1,44 MB»; y 1.073.741.824 bytes es 1 GiB.

## m02-l05-q059
Según los ejemplos del NIST, que comparan los prefijos binarios con los del Sistema Internacional, ¿cuántos bits son un kibibit (1 Kibit)?
- a) 1.000 bits.
- b) 1.024 bits.  ✓
- c) 8 bits.
- d) 1.048.576 bits.
Cita: fuente: `nist-prefijos-binarios.html`; «Examples and comparisons with SI prefixes»
Explicación: El NIST da 1 Kibit = 2^10 bit = 1.024 bit. 1.000 bits es un kilobit (1 kbit), con el prefijo decimal; 8 bits son un byte; y 1.048.576 es 2^20, el factor de mebi.

## m02-l05-q060
¿Cuál de los siguientes valores dan normalmente al megabyte los fabricantes de dispositivos de almacenamiento, según el contexto histórico que recoge el NIST?
- a) 1.048.576 bytes, es decir, 2^20 bytes.
- b) 1.024.000 bytes, como en el disquete.
- c) 1.000.000 bytes, es decir, 10^6 bytes.  ✓
- d) 1.024 bytes, como en el antiguo kilobyte.
Cita: fuente: `nist-prefijos-binarios.html`; «Historical context»
Explicación: El NIST cuenta que la mayoría de los fabricantes de memoria usan el megabyte como 2^20 = 1.048.576 bytes, pero que los fabricantes de dispositivos de almacenamiento «normalmente» lo usan como 1.000.000 bytes. 1.024.000 bytes es el megabyte del disquete de «1,44 MB» y 1.024 bytes es el kilobyte que usaban los profesionales de la informática.

## m02-l05-q061
Según el NIST, ¿qué organismo aprobó en diciembre de 1998 los nombres y símbolos de los prefijos para múltiplos binarios como norma internacional?
- a) El Instituto de Ingenieros Eléctricos y Electrónicos (IEEE).
- b) El Comité Internacional de Pesas y Medidas (CIPM).
- c) El Instituto Nacional de Estándares y Tecnología (NIST).
- d) La Comisión Electrotécnica Internacional (IEC).  ✓
Cita: fuente: `nist-prefijos-binarios.html`; «Prefixes for binary multiples»
Explicación: El NIST dice que en diciembre de 1998 la IEC, la Comisión Electrotécnica Internacional, aprobó como norma internacional los nombres y símbolos de esos prefijos. El IEEE y el CIPM apoyaron su desarrollo, pero no los aprobaron, y el NIST solo publica la página que lo cuenta.

## m02-l05-q062
Según el contexto histórico que recoge el NIST, ¿por qué empezaron los profesionales de la informática a usar el prefijo «kilo» con el valor de 1.024?
- a) Porque 2^10 está muy cerca de 1.000.  ✓
- b) Porque el Sistema Internacional define kilo como 2^10.
- c) Porque la IEC lo aprobó así como norma en 1998.
- d) Porque un byte está formado por 1.024 bits.
Cita: fuente: `nist-prefijos-binarios.html`; «Historical context»
Explicación: El NIST cuenta que los profesionales de la informática vieron que 2^10 era «muy cercano a 1000» y empezaron a usar «kilo» para 1.024. En el SI kilo vale 10^3; lo que la IEC aprobó en 1998 fueron prefijos binarios distintos, como kibi; y un byte tiene 8 bits.

## m02-l05-q064
Según el ejemplo de Microsoft sobre Plug and Play en Windows, ¿qué puede hacer un usuario que acopla su equipo portátil a una estación de acoplamiento?
- a) Usar el teclado, el ratón y el monitor de la estación tras instalar a mano sus controladores.
- b) Usar el teclado, el ratón y el monitor de la estación sin cambios de configuración manuales.  ✓
- c) Usar solo el monitor de la estación, porque el teclado y el ratón exigen configuración manual.
- d) Usar el teclado, el ratón y el monitor de la estación tras configurarlos en el firmware.
Cita: fuente: `ms-win-plug-and-play.html`; «Introducción a Plug and Play»
Explicación: La página pone este ejemplo: un usuario puede acoplar un portátil «y usar el teclado, el mouse y el monitor de la estación de acoplamiento sin realizar cambios de configuración manuales». Instalar a mano los controladores, configurar el teclado y el ratón o pasar por el firmware son justo la configuración manual que PnP evita.

## m02-l05-q065
¿Cuál de las siguientes funciones proporciona, según Microsoft, la compatibilidad del software del sistema con Plug and Play junto con los controladores PnP?
- a) El cifrado del disco a nivel del sistema de archivos.
- b) La copia de las carpetas del usuario en OneDrive.
- c) La carga de los controladores adecuados.  ✓
- d) El control del arranque antes de pasar a Windows.
Cita: fuente: `ms-win-plug-and-play.html`; «Introducción a Plug and Play»
Explicación: Entre las funciones que la página atribuye al software del sistema con los controladores PnP está la «carga de controladores adecuados», junto al reconocimiento automático del hardware y la asignación de recursos. El cifrado a nivel del sistema de archivos es de NTFS, la copia de carpetas en OneDrive es de Copias de seguridad de Windows y el control del arranque es de la interfaz del firmware.

## m02-l05-q066
Según Microsoft, en Windows con Plug and Play, ¿quién determina y asigna los recursos de hardware de cada dispositivo, como los puertos de entrada/salida?
- a) El controlador de cada dispositivo PnP.
- b) El usuario, mediante configuración manual.
- c) La interfaz del firmware UEFI.
- d) El administrador de Plug and Play (PnP).  ✓
Cita: fuente: `ms-win-plug-and-play.html`; «Introducción a Plug and Play»
Explicación: La página dice que «el administrador de PnP determina los recursos de hardware solicitados por cada dispositivo (por ejemplo, puertos de entrada/salida…) y asigna los recursos». Precisa que «los controladores para dispositivos PnP no asignan recursos»; PnP evita la configuración manual; y el firmware controla el arranque, no esta asignación.

## m02-l05-q067
¿Cuál de las siguientes afirmaciones describe, según Microsoft, cómo trata el administrador de Plug and Play de Windows a los dispositivos heredados?
- a) Les asigna los recursos primero, porque no se configuran dinámicamente.  ✓
- b) Les asigna los recursos en último lugar, cuando ya no quedan otros.
- c) No les asigna ningún recurso, porque no admiten la configuración dinámica.
- d) Deja que sus controladores asignen los recursos que necesiten.
Cita: fuente: `ms-win-plug-and-play.html`; «Introducción a Plug and Play»
Explicación: La página dice: «Los recursos no se pueden configurar dinámicamente para los dispositivos heredados, por lo que el administrador de PnP asigna primero recursos a los dispositivos heredados». Asignarlos en último lugar o no asignarlos contradice esa frase, y la página precisa que los controladores no asignan recursos.

## m02-l05-q068
Según la documentación de Microsoft sobre Plug and Play en Windows, ¿con qué elementos requiere compatibilidad PnP para que funcione?
- a) Solo con el hardware del dispositivo, sin depender de sus controladores ni del software del sistema.
- b) Con el hardware del dispositivo, el software del sistema y los controladores.  ✓
- c) Solo con el software del sistema, sin depender del hardware.
- d) Solo con los controladores, sin depender del software del sistema.
Cita: fuente: `ms-win-plug-and-play.html`; «Introducción a Plug and Play»
Explicación: La página dice: «PnP requiere compatibilidad con el hardware del dispositivo, el software del sistema y los controladores». Las otras tres dejan fuera uno o dos de esos elementos.

## m02-l05-q069
¿Cuál de las siguientes listas recoge solo dispositivos señaladores, según la documentación de Microsoft sobre la entrada en las aplicaciones de Windows?
- a) Pantalla táctil, ratón, memoria RAM y panel táctil.
- b) Ratón, lápiz óptico, placa base y panel táctil.
- c) Pantalla táctil, ratón, lápiz óptico y panel táctil.  ✓
- d) Pantalla táctil, lápiz óptico, CPU y memoria caché.
Cita: fuente: `ms-win-dispositivos-entrada.html`; «Puntero»
Explicación: La página habla de los datos de entrada «procedentes de dispositivos señaladores, como la pantalla táctil, el ratón, el lápiz óptico y el panel táctil». La memoria RAM, la placa base, la CPU y la memoria caché son componentes internos que guardan datos, conectan chips o procesan instrucciones, no dispositivos de entrada.

## m02-l05-q070
Según la documentación de Microsoft sobre entrada e interacciones en Windows, ¿qué tipo de dispositivo es el lápiz óptico que se usa con un equipo?
- a) Un dispositivo que guarda datos temporalmente, como la RAM.
- b) Un procesador que muestra gráficos en pantalla, como la GPU.
- c) Una placa de circuito que conecta chips, como la placa base.
- d) Un dispositivo señalador de entrada, como el ratón.  ✓
Cita: fuente: `ms-win-dispositivos-entrada.html`; «Puntero»
Explicación: Dentro de los dispositivos de entrada, la página cita el lápiz óptico entre los «dispositivos señaladores», junto a la pantalla táctil, el ratón y el panel táctil. Guardar datos temporalmente es la función de la RAM, mostrar los gráficos la de la GPU y conectar los chips la de la placa base.

## m02-l05-q071
Según la documentación de Microsoft sobre entrada en las aplicaciones de Windows, la entrada del teclado es una parte esencial de la experiencia de interacción e indispensable para:
- a) la accesibilidad.  ✓
- b) la entrada por mirada.
- c) la entrada multitáctil indirecta.
- d) el movimiento panorámico.
Cita: fuente: `ms-win-dispositivos-entrada.html`; «Keyboard»
Explicación: La página dice que la entrada del teclado es «una parte esencial de la experiencia de interacción e indispensable para la accesibilidad». La entrada por mirada tiene su propio apartado en la página: sigue la ubicación y el movimiento de los ojos y la cabeza. La multitáctil indirecta es la del panel táctil, que la página describe en otro apartado como una combinación con la precisión de un dispositivo apuntador. El movimiento panorámico es una interacción distinta, con sus propias directrices.

## m02-l05-q072
¿Cuál de las siguientes series recoge propiedades de entrada específicas del lápiz, según la documentación de Microsoft sobre la entrada en las aplicaciones de Windows?
- a) Los clics de botón, la rueda de desplazamiento y el movimiento del puntero.
- b) La presión, la inclinación, el botón del cuerpo y la detección del borrador.  ✓
- c) La ubicación y el movimiento de los ojos y de la cabeza del usuario.
- d) La entrada multitáctil indirecta con la precisión de un dispositivo apuntador.
Cita: fuente: `ms-win-dispositivos-entrada.html`; «Lápiz y Windows Ink»
Explicación: La página dice que el apartado del lápiz administra «propiedades de entrada específicas del lápiz, como la presión, la inclinación, el botón del cuerpo del lápiz y la detección del borrador». Los clics, la rueda y el movimiento del puntero son la entrada del ratón; los ojos y la cabeza, la entrada por mirada; y la entrada multitáctil indirecta, la del panel táctil.

## m02-l05-q073
¿Cuál de las siguientes descripciones corresponde a la entrada del panel táctil, según la documentación de Microsoft sobre la entrada en las aplicaciones de Windows?
- a) La entrada del teclado con el seguimiento de los ojos y de la cabeza.
- b) La presión y la inclinación del lápiz con la detección del borrador.
- c) La entrada multitáctil indirecta con la precisión de un dispositivo apuntador.  ✓
- d) Los clics de botón del ratón con la entrada del mando de Xbox.
Cita: fuente: `ms-win-dispositivos-entrada.html`; «Panel táctil»
Explicación: La página dice que la entrada del panel táctil «combina la entrada multitáctil indirecta con la precisión de un dispositivo apuntador». El seguimiento de ojos y cabeza es la entrada por mirada, la presión, la inclinación y el borrador son propiedades del lápiz, y el mando de Xbox es la entrada del controlador para juegos.

## m02-l05-q074
Según Microsoft, ¿qué pueden hacer los controladores y el código en modo de usuario gracias a Plug and Play respecto a los eventos de hardware?
- a) Registrarse y recibir notificaciones de determinados eventos de hardware.  ✓
- b) Asignar por sí mismos los recursos que solicita cada dispositivo.
- c) Pasar por alto al administrador de PnP al enumerar un dispositivo.
- d) Configurar a mano el hardware que se agrega al equipo.
Cita: fuente: `ms-win-plug-and-play.html`; «Introducción a Plug and Play»
Explicación: La página dice que PnP permite a los controladores y al código en modo de usuario registrarse y recibir notificaciones de determinados eventos de hardware. Los controladores para dispositivos PnP no asignan recursos, la asignación la hace el administrador de PnP, y el objetivo de PnP es evitar la configuración manual del hardware.

## m02-l05-q075
Según el NIST, ¿qué valor tiene mega en los estándares del IEEE, salvo que se señale expresamente el uso de la definición de base dos?
- a) 1.000.000  ✓
- b) 1.024.000
- c) 1.048.576
- d) 1.073.741.824
Cita: fuente: `nist-prefijos-binarios.html`; «Historical context»
Explicación: El NIST cuenta que el Consejo de Normas del IEEE decidió usar las definiciones convencionales de los prefijos del Sistema Internacional, de modo que mega significa 1 000 000; la definición de base dos solo puede usarse si se señala expresamente. 1.048.576 es el megabyte de la memoria del ordenador, 1.024.000 el del disquete de «1,44 MB» y 1.073.741.824 es un gibibyte.

## m02-l05-q076
¿Cuál de los siguientes valores tiene el megabyte con el que se formatea el disquete de 3 1/2 pulgadas de «1,44 MB», según el contexto histórico del NIST?
- a) 1.000.000 bytes.
- b) 1.024.000 bytes.  ✓
- c) 1.048.576 bytes.
- d) 1.073.741.824 bytes.
Cita: fuente: `nist-prefijos-binarios.html`; «Historical context»
Explicación: El NIST dice que un tercer megabyte, de 1 024 000 bytes, es el que se usa para formatear el disquete de 90 mm (3 1/2 pulgadas) de «1,44 MB». Los 1.000.000 bytes son el megabyte de los fabricantes de dispositivos de almacenamiento, los 1.048.576 el de la memoria y 1.073.741.824 bytes son un gibibyte.

## m02-l05-q077
Según el contexto histórico del NIST, ¿qué valor usan todos los ingenieros de telecomunicaciones para el megabit por segundo?
- a) 10^6 bit/s, es decir, 1.000.000 bit/s.  ✓
- b) 2^20 bit/s, es decir, 1.048.576 bit/s.
- c) 1.024.000 bit/s.
- d) 10^9 bit/s, es decir, 1.000.000.000 bit/s.
Cita: fuente: `nist-prefijos-binarios.html`; «Historical context»
Explicación: El NIST cuenta que algunos diseñadores de redes de área local han usado el megabit por segundo como 1 048 576 bit/s, pero todos los ingenieros de telecomunicaciones lo usan como 10^6 bit/s. 1.024.000 es el megabyte del disquete y 10^9 corresponde al prefijo giga.

## m02-l05-q078
¿Cuál de las siguientes definiciones corresponde a un router (enrutador) en una red de ordenadores?
- a) Equipo que almacena una información y la gestiona para ofrecerla a otras máquinas.
- b) Tecnología que extiende de forma segura una red local sobre una red pública.
- c) Dispositivo que distribuye el tráfico de red entre dos o más redes diferentes.  ✓
- d) Prestador de servicios que da a sus clientes acceso a redes de telecomunicaciones.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Router»
Explicación: El glosario del INCIBE define el router como un dispositivo que distribuye tráfico de red entre dos o más redes diferentes. Almacenar información y gestionarla para ofrecerla a otras máquinas es lo que hace un servidor. Extender una red local sobre una red pública de forma segura es la red privada virtual (VPN). Dar acceso a redes de telecomunicaciones es lo que hace el proveedor de acceso (ISP).

## m02-l05-q079
¿A cuántas redes está conectado, como mínimo, un router, el dispositivo que redirige el tráfico de una red hacia otra?
- a) Al menos a dos redes, generalmente LAN o WAN.  ✓
- b) A una sola red, generalmente la red LAN.
- c) Al menos a tres redes, generalmente LAN o WAN.
- d) A una sola red, generalmente la red WAN.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Router»
Explicación: Según el glosario del INCIBE, el router está conectado al menos a dos redes, generalmente LAN o WAN, y el tráfico que recibe de una red lo redirige hacia la otra u otras. Con una sola red no habría hacia dónde redirigirlo, y el mínimo que da el glosario es dos, no tres.
