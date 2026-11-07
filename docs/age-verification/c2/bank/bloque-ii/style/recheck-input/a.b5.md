# Strict recheck input — group a, batch 5 (60 candidates)

## m02-l05-q080
¿Qué comprueba un router en los paquetes de información que recibe para decidir por qué ruta serán enviados?
- a) Las direcciones de origen de los paquetes, con listas blancas de remitentes.
- b) Las direcciones de destino, con cabeceras y tablas de comparación.  ✓
- c) El contenido de los ficheros adjuntos, con firmas de antivirus actualizadas.
- d) El nombre del usuario que los envía, con su certificado digital.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Router»
Explicación: El glosario del INCIBE dice que el router comprueba las direcciones de destino de los paquetes y decide por qué ruta serán enviados; para el mejor camino usa cabeceras y tablas de comparación. El glosario no le atribuye mirar la dirección de origen, los ficheros adjuntos ni el nombre o el certificado del remitente.

## m02-l05-q081
¿Cuál de los siguientes términos se usa en español como sinónimo de router, el dispositivo que distribuye tráfico entre redes?
- a) Servidor
- b) Cortafuegos
- c) Proxy
- d) Encaminador  ✓
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Router»
Explicación: El glosario del INCIBE da como sinónimos de router «Enrutador, Encaminador, Rúter». El servidor provee y gestiona datos para otras máquinas. El cortafuegos permite y limita el tráfico según unas normas. El proxy hace de intermediario en las peticiones de los equipos de una LAN hacia Internet. Los tres tienen su propia entrada en el mismo glosario.

## m02-l05-q082
En términos domésticos, ¿qué es el router, según el glosario de términos de ciberseguridad del INCIBE?
- a) El programa que hace de intermediario entre la LAN doméstica e Internet.
- b) El dispositivo del proveedor que une la LAN doméstica con la red del ISP.  ✓
- c) El equipo que aloja los sitios web y el correo electrónico del hogar.
- d) La tecnología que extiende la LAN doméstica sobre Internet con cifrado.
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Router»
Explicación: El glosario del INCIBE dice que, en términos domésticos, el router es el dispositivo que proporciona el proveedor de servicios de telefonía (o ISP) y que conecta la LAN doméstica con la red del ISP. Hacer de intermediario entre la LAN e Internet es la definición de proxy; alojar sitios web y correo es lo que hace un servidor; extender una LAN sobre Internet con cifrado es la red privada virtual.

## m02-l05-q084
En el modelo SaaS de distribución de software, ¿quién es generalmente el tercero en cuyos servidores se alojan el software y sus datos?
- a) El cliente que usa el software.
- b) El proveedor de acceso a Internet.
- c) La autoridad de certificación del cliente.
- d) El fabricante del propio software.  ✓
Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «SaaS»
Explicación: Según el glosario del INCIBE, en SaaS el software y sus datos se alojan en servidores de un tercero, «generalmente el fabricante del software». El cliente no es un tercero: accede vía Internet. El proveedor de acceso da acceso a las redes de telecomunicaciones, y la autoridad de certificación genera certificados digitales; ninguno de los dos es el tercero que nombra la definición.

## m02-l05-q085
¿Qué usa la minería de datos, el proceso de detectar información accionable en grandes conjuntos de datos, para derivar patrones y tendencias?
- a) Análisis matemáticos de los datos.  ✓
- b) Cifrado de los datos con claves de 256 bits.
- c) Replicación de los datos en varias bases.
- d) Compresión de los datos en el sistema de archivos.
Cita: fuente: `ms-mineria-datos.html`; «Conceptos de minería de datos»
Explicación: La página dice que la minería de datos usa análisis matemáticos para derivar patrones y tendencias que existen en los datos. El cifrado protege los datos, la replicación los copia y sincroniza entre bases de datos y la compresión del sistema de archivos sirve para almacenar más datos en un volumen; ninguno deriva patrones.

## m02-l05-q086
¿Por qué los patrones que detecta la minería de datos normalmente no se pueden detectar mediante la exploración de datos tradicional?
- a) Porque los datos están cifrados y la exploración tradicional no los lee.
- b) Porque las relaciones son demasiado complejas o porque hay demasiados datos.  ✓
- c) Porque los datos deben estar en un cubo OLAP y no en una base relacional.
- d) Porque la exploración tradicional solo admite datos de libros de Excel.
Cita: fuente: `ms-mineria-datos.html`; «Conceptos de minería de datos»
Explicación: La página dice que estos patrones normalmente no se pueden detectar con la exploración de datos tradicional porque las relaciones son demasiado complejas o porque hay demasiados datos. No habla de cifrado, y añade que los datos de la minería no necesitan estar en un cubo OLAP ni en una base relacional y que pueden venir de libros de Excel.

## m02-l05-q087
¿Cuál de las siguientes afirmaciones sobre las unidades de estado sólido (SSD) es correcta, según Microsoft?
- a) No tienen partes móviles y almacenan los datos en circuitos pequeños.  ✓
- b) Usan discos magnetizados que giran rápido y un brazo con una cabeza lectora.
- c) Necesitan energía para conservar los datos que almacenan.
- d) Almacenan los datos en una cinta magnética que se rebobina.
Cita: fuente: `ms-learn-equipos-almacenamiento.html`; «Unidades de estado sólido»
Explicación: La página dice que las SSD no tienen partes móviles y almacenan datos en circuitos pequeños en lugar de discos magnetizados. Los discos que giran con un brazo y una cabeza son la unidad de disco duro; la cinta que se rebobina es el almacenamiento de los primeros equipos; y el almacenamiento a largo plazo guarda datos sin necesitar energía.

## m02-l05-q088
¿Cómo lee y escribe la información una unidad de disco duro (HDD), uno de los tipos de almacenamiento a largo plazo?
- a) Con circuitos pequeños, sin ninguna parte móvil en la unidad.
- b) Con una cinta magnética que debe rebobinarse o avanzarse.
- c) Con memoria de acceso aleatorio, que se borra al apagar el equipo.
- d) Con discos que giran rápido y un brazo con una cabeza.  ✓
Cita: fuente: `ms-learn-equipos-almacenamiento.html`; «Unidades de disco duro»
Explicación: La página describe el HDD como discos que giran rápido y usan un brazo y una cabeza para leer y escribir información, «algo así como un tocadiscos». Los circuitos sin partes móviles son la SSD, la cinta que se rebobina es el soporte anterior y la RAM es memoria a corto plazo, no almacenamiento.

## m02-l05-q089
¿Cuál de las siguientes ventajas atribuye Microsoft a las unidades de estado sólido (SSD) por no tener partes móviles?
- a) Tienden a romperse más, aunque son más ligeras y más pequeñas.
- b) Pesan más, pero son más pequeñas y se rompen menos.
- c) Tienden a romperse menos, son más ligeras y más pequeñas.  ✓
- d) Son más grandes, pero tienden a romperse menos y pesan menos.
Cita: fuente: `ms-learn-equipos-almacenamiento.html`; «Unidades de estado sólido»
Explicación: La página dice que, como no tienen partes móviles, las SSD tienden a romperse menos, son más ligeras y tienden a ser más pequeñas. Cada distractor cambia uno de esos tres rasgos: que se rompan más, que pesen más o que sean más grandes.

## m02-l05-q090
¿Qué tienen en común las unidades de disco duro (HDD) y las unidades de estado sólido (SSD), según Microsoft?
- a) Usan discos que giran y un brazo con una cabeza para leer y escribir.
- b) Pueden contener mucha información y se conectan al equipo de maneras similares.  ✓
- c) Solo conservan los datos mientras el equipo permanece encendido.
- d) No tienen partes móviles y almacenan los datos en circuitos pequeños.
Cita: fuente: `ms-learn-equipos-almacenamiento.html`; «Tanto las unidades de disco duro como las unidades de estado sólido pueden contener mucha información.»
Explicación: En «Similitudes», la página dice que las dos pueden contener mucha información, hasta terabytes, y que se conectan al equipo de maneras similares. Los discos que giran son solo del HDD, los circuitos sin partes móviles solo de la SSD, y las dos guardan datos sin necesitar energía.

## m02-l05-q091
Comparadas con las unidades de disco duro (HDD), muchas unidades de estado sólido (SSD), según la página de Microsoft:
- a) Son más lentas, duran menos y tienden a usar más potencia.
- b) Son más rápidas, pero duran menos y tienden a usar más potencia.
- c) Son más rápidas, duran más y tienden a usar menos potencia.  ✓
- d) Son igual de rápidas, pero duran menos y usan la misma potencia.
Cita: fuente: `ms-learn-equipos-almacenamiento.html`; «Unidades de estado sólido»
Explicación: La página dice que muchas SSD son más rápidas y duran más que los discos duros, y que tienden a usar menos potencia. Los distractores invierten uno o varios de esos rasgos.

## m02-l05-q092
¿Cuál de las siguientes afirmaciones sobre el almacenamiento a largo plazo, como el HDD o la SSD, es correcta?
- a) Almacena datos sin necesitar energía, a diferencia de la memoria RAM.  ✓
- b) Solo está activo con el equipo encendido, como la memoria RAM.
- c) Pierde los datos cuando la batería del equipo se queda sin carga.
- d) También se denomina memoria a corto plazo o de acceso aleatorio.
Cita: fuente: `ms-learn-equipos-almacenamiento.html`; «El almacenamiento a largo plazo es diferente, almacenando datos sobre cosas que no necesitan energía.»
Explicación: La página dice que el almacenamiento a largo plazo guarda datos sobre cosas que no necesitan energía, a diferencia de la RAM, que solo está activa con el equipo encendido y pierde lo que contiene al apagarlo o al agotarse la batería. «Memoria a corto plazo» es el otro nombre que la página da a la RAM.

## m02-l05-q093
¿Por qué los usuarios usan cada vez menos las unidades de disco duro (HDD), según la página de Microsoft sobre el almacenamiento?
- a) Porque los HDD ya no pueden contener terabytes de datos.
- b) Porque las SSD han bajado de tamaño y de coste y almacenan más.  ✓
- c) Porque los HDD solo acceden a los datos en orden, como la cinta.
- d) Porque los HDD se conectan al equipo de forma distinta a las SSD.
Cita: fuente: `ms-learn-equipos-almacenamiento.html`; «Unidades de disco duro»
Explicación: La página dice que los discos duros se usan menos porque el tamaño físico y el coste de las SSD han bajado mientras su capacidad ha aumentado. Según la misma página, los HDD pueden contener terabytes, obtienen la información esté donde esté en el disco y se conectan al equipo de maneras similares a las SSD.

## m02-l05-q094
¿Cuál de las siguientes afirmaciones sobre los discos duros (HDD), comparados con la cinta magnética, es correcta?
- a) Son más lentos que la cinta, pero se rompen menos que ella.
- b) Igual que la cinta, deben rebobinarse para llegar a un dato.
- c) A diferencia de la cinta, no usan imanes para guardar los datos.
- d) Son más rápidos y obtienen la información esté donde esté en el disco.  ✓
Cita: fuente: `ms-learn-equipos-almacenamiento.html`; «Unidades de disco duro»
Explicación: La página dice que, a diferencia de la cinta, los HDD son mucho más rápidos, no se rompen tanto y permiten obtener la información rápidamente, independientemente de dónde se encuentre en el disco. También dice que los HDD usan pequeños imanes, como la cinta, y rebobinar era la desventaja de la cinta.

## m02-l05-q095
Señale la afirmación correcta sobre el sistema de archivos NTFS en Windows 11, según la documentación de Microsoft:
- a) Solo admite volúmenes de hasta 256 TB en las versiones actuales de Windows.
- b) Es el sistema de archivos predeterminado del sistema operativo moderno basado en Windows.  ✓
- c) Solo permite montar un volumen en una carpeta que ya contenga archivos.
- d) Necesita desconectar el volumen para reparar cualquier daño del sistema de archivos, aunque sea menor.
Cita: fuente: `ms-win-ntfs.html`; «Introducción a NTFS»
Explicación: La página dice que NTFS es el sistema de archivos predeterminado para el sistema operativo moderno basado en Windows, y se aplica a Windows 11. Los 256 TB son el límite de versiones anteriores de Windows; un volumen se monta en una carpeta vacía; y NTFS de recuperación automática repara daños menores sin desconectar el volumen.

## m02-l05-q097
¿Cuál de las siguientes afirmaciones sobre los permisos del sistema de archivos NTFS en Windows 11 es correcta?
- a) Indican qué usuarios y grupos tienen acceso y el tipo de acceso, como lectura o escritura.  ✓
- b) Se asignan a las carpetas, pero no a cada archivo por separado.
- c) Se asignan a cada usuario por separado, pero nunca a grupos de usuarios.
- d) Se asignan con el cifrado de unidad BitLocker, no con listas de control de acceso (ACL).
Cita: fuente: `ms-win-ntfs.html`; «Mayor seguridad»
Explicación: La página dice que NTFS permite asignar permisos detallados a archivos y carpetas mediante listas de control de acceso (ACL), indicando qué usuarios y grupos tienen acceso y el tipo de acceso, como lectura, escritura o modificación. BitLocker cifra los volúmenes; no es el mecanismo de los permisos.

## m02-l05-q098
¿Cuál de las siguientes características de seguridad basadas en hardware aplica BitLocker, el cifrado de unidad que funciona con NTFS en Windows 11?
- a) La memoria caché de nivel 2 o 3.
- b) La tarjeta gráfica con DirectX 12.
- c) El módulo de plataforma segura (TPM).  ✓
- d) El controlador de dispositivo WDDM 2.0.
Cita: fuente: `ms-win-ntfs.html`; «Mayor seguridad»
Explicación: La página dice que BitLocker aplica características de seguridad basadas en hardware como el módulo de plataforma segura (TPM) para cifrar los dispositivos. La caché de nivel 2 o 3 es una propiedad del procesador, y la tarjeta gráfica con DirectX 12 y el controlador WDDM 2.0 son requisitos gráficos de Windows 11; ninguno es una función de BitLocker.

## m02-l05-q099
En Windows 11, si se produce un error del sistema, ¿cómo restaura NTFS la coherencia del sistema de archivos?
- a) Reasigna el clúster afectado a otro y lo marca como inutilizable.
- b) Ejecuta chkdsk con el volumen desconectado hasta acabar la reparación.
- c) Restaura la versión anterior de cada archivo desde el Historial de versiones de Office.
- d) Usa su archivo de registro basado en transacciones durante el siguiente inicio.  ✓
Cita: fuente: `ms-win-ntfs.html`; «Mayor confiabilidad»
Explicación: La página dice que NTFS mantiene un archivo de registro basado en transacciones y, si se produce un error del sistema, lo usa para restaurar automáticamente la coherencia durante el siguiente inicio. Reasignar el clúster es lo que hace ante un sector incorrecto; chkdsk repara manteniendo el volumen en línea; el Historial de versiones es la herramienta de Office para recuperar versiones de un archivo.

## m02-l05-q100
¿Qué hace el sistema de archivos NTFS de Windows 11 cuando detecta un sector incorrecto en el disco?
- a) Desconecta el volumen hasta que chkdsk termina de repararlo.
- b) Reasigna el clúster afectado a uno correcto y marca el original como inutilizable.  ✓
- c) Borra el clúster afectado junto con los datos que contiene.
- d) Reproduce su registro de transacciones en el siguiente inicio del equipo y del volumen.
Cita: fuente: `ms-win-ntfs.html`; «Mayor confiabilidad»
Explicación: La página dice que, cuando se detecta un sector incorrecto, NTFS reasigna dinámicamente el clúster afectado a uno correcto, marca el original como inutilizable y conserva los datos. No borra esos datos ni desconecta el volumen, y reproducir el registro de transacciones es lo que hace tras un bloqueo del sistema.

## m02-l05-q101
En Windows 11, la característica del sistema de archivos NTFS denominada «NTFS de recuperación automática»:
- a) Repara daños menores, pero solo después de desconectar el volumen.
- b) Restaura una versión anterior del volumen desde una instantánea del servicio VSS.
- c) Detecta y repara daños menores en segundo plano, sin desconectar el volumen.  ✓
- d) Cifra el volumen con BitLocker en cuanto detecta un daño menor.
Cita: fuente: `ms-win-ntfs.html`; «Mayor confiabilidad»
Explicación: La página dice que NTFS de recuperación automática detecta y repara automáticamente daños menores del sistema de archivos en segundo plano, sin necesidad de que el volumen se desconecte. No restaura versiones desde instantáneas ni cifra el volumen; BitLocker es el cifrado de unidad.

## m02-l05-q102
Para daños más significativos en un volumen NTFS de Windows 11, ¿cuál de las siguientes acciones realiza la utilidad chkdsk?
- a) Examina y repara el volumen mientras lo mantiene en línea.  ✓
- b) Examina el volumen, pero solo lo repara después de formatearlo.
- c) Mantiene el volumen desconectado durante todo el examen y la reparación.
- d) Traslada todos los clústeres del volumen a otro disco del equipo.
Cita: fuente: `ms-win-ntfs.html`; «Mayor confiabilidad»
Explicación: La página dice que, para daños más significativos, chkdsk puede examinar y reparar volúmenes NTFS mientras los mantiene en línea; el único período en que el volumen podría no estar disponible es la fase de restaurar la coherencia de los datos. No formatea el volumen, no lo mantiene desconectado todo el tiempo y no traslada clústeres a otro disco.

## m02-l05-q103
En un volumen NTFS con un tamaño de clúster de 64 KB, ¿cuál es el mayor tamaño de volumen y de archivo que admite, según Microsoft?
- a) 16 TB
- b) 128 TB
- c) 8 PB
- d) 256 TB  ✓
Cita: fuente: `ms-win-ntfs.html`; «64 KB (máx. anterior) — 256 TB»
Explicación: La tabla de la página da, para un clúster de 64 KB (el máximo anterior), un volumen y un archivo de hasta 256 TB. Los 16 TB corresponden al clúster de 4 KB, los 128 TB al de 32 KB y los 8 PB al de 2048 KB, el tamaño máximo.

## m02-l05-q104
¿Cuál es el tamaño de clúster predeterminado de un volumen NTFS, según la tabla de tamaños de volumen y archivo de Microsoft?
- a) 4 KB  ✓
- b) 8 KB
- c) 64 KB
- d) 2048 KB
Cita: fuente: `ms-win-ntfs.html`; «Compatibilidad con volúmenes grandes»
Explicación: La tabla de la página marca 4 KB como «tamaño predeterminado», con un volumen y un archivo de hasta 16 TB. Los 8 KB son otra fila de la tabla, 64 KB es el «máx. anterior» y 2048 KB el «tamaño máx.».

## m02-l05-q105
¿Cómo mantiene NTFS la compatibilidad con los sistemas de archivos que imponen un límite 8.3 en los nombres de archivo y las extensiones?
- a) Recorta los nombres largos a ocho caracteres y tres de extensión, sin conservarlos.
- b) Almacena en el disco un alias 8.3, en Unicode, de cada nombre largo.  ✓
- c) Impide crear nombres de archivo de más de ocho caracteres.
- d) Guarda los nombres largos en la nube y los cortos en el disco.
Cita: fuente: `ms-win-ntfs.html`; «Nombre y ruta de acceso máximos de un archivo»
Explicación: La página dice que NTFS admite nombres de archivo largos y almacena en el disco un alias 8.3, en Unicode, para ser compatible con los sistemas que imponen ese límite. Recortar los nombres a ocho caracteres sin conservarlos contradice «admite nombres de archivo largos»: el nombre largo se mantiene y el alias va aparte. Impedir los nombres de más de ocho caracteres contradice lo mismo. Y el alias se almacena «en el disco», no en la nube.

## m02-l05-q106
¿Cuál de las siguientes formas de trabajar con la capacidad de almacenamiento ofrece NTFS cuando el espacio de un volumen está limitado?
- a) Montar un volumen en cualquier carpeta vacía de un volumen NTFS local.  ✓
- b) Montar un volumen solo en la raíz de una unidad con letra asignada.
- c) Aumentar el volumen solo con espacio sin asignar de otro disco distinto.
- d) Reducir automáticamente el tamaño de los archivos de usuario más antiguos.
Cita: fuente: `ms-win-ntfs.html`; «Asignación flexible de capacidad»
Explicación: Entre las formas de trabajar con la capacidad, la página cita montar un volumen en cualquier carpeta vacía de un volumen NTFS local, por ejemplo si se agotan las letras de unidad. También cita aumentar un volumen con espacio sin asignar del mismo disco o de otro, no solo de otro. No habla de reducir archivos antiguos.

## m02-l05-q107
En el sistema de archivos NTFS de Windows 11, ¿para qué sirven las cuotas de disco de un volumen?
- a) Para cifrar con BitLocker los datos confidenciales guardados en el volumen.
- b) Para seguir y controlar el uso del espacio de disco de cada usuario.  ✓
- c) Para comprimir los datos y almacenar más en el mismo volumen.
- d) Para asignar permisos de lectura y escritura a los grupos.
Cita: fuente: `ms-win-ntfs.html`; «Asignación flexible de capacidad»
Explicación: La página dice que las cuotas de disco sirven para realizar el seguimiento y controlar el uso del espacio de disco en volúmenes NTFS para usuarios individuales. El cifrado es BitLocker, almacenar más datos es la compresión del sistema de archivos y los permisos se asignan con listas de control de acceso.

## m02-l05-q108
¿Cuál de las siguientes funciones tiene la compresión del sistema de archivos NTFS cuando el espacio de un volumen está limitado?
- a) Controlar el uso del espacio de disco que hace cada usuario.
- b) Montar el volumen en una carpeta vacía de otro volumen NTFS local.
- c) Agregar espacio sin asignar del mismo disco o de otro disco al volumen.
- d) Maximizar la cantidad de datos que se pueden almacenar en el volumen.  ✓
Cita: fuente: `ms-win-ntfs.html`; «Asignación flexible de capacidad»
Explicación: La página dice que la compresión del sistema de archivos sirve para maximizar la cantidad de datos que se pueden almacenar. Las otras tres son formas distintas de trabajar con la capacidad que cita la misma lista: las cuotas de disco controlan el uso por usuario, el montaje en carpeta vacía da acceso a espacio desde una carpeta y agregar espacio sin asignar aumenta el tamaño del volumen.

## m02-l05-q109
¿Cuáles son los dos tipos principales de almacenamiento que distingue la formación de Microsoft sobre el almacenamiento de los equipos?
- a) El almacenamiento local y el almacenamiento en la nube.
- b) La memoria a corto plazo y la memoria a largo plazo.
- c) El almacenamiento en cinta y el almacenamiento en disco duro.
- d) El almacenamiento magnético y el almacenamiento digital.  ✓
Cita: fuente: `ms-learn-equipos-almacenamiento.html`; «Tipos de almacenamiento»
Explicación: La página dice: «los dos tipos principales que veremos son el almacenamiento magnético y el almacenamiento digital». Local y nube no es ese par: la frase fija los dos tipos, y son otros. Corto y largo plazo separan la RAM del almacenamiento, no son dos tipos de almacenamiento: «Este tipo de memoria, memoria de acceso aleatorio, también se denomina memoria a corto plazo» y el almacenamiento es «el segundo tipo de memoria». Cinta y disco duro son ambos magnéticos, pues los discos duros «usan pequeños imanes para contener datos como una cinta»; el digital son las unidades de estado sólido, que «almacenan datos en circuitos pequeños en lugar de discos magnetizados».

## m02-l05-q110
En Windows 11, ¿cuál de las siguientes afirmaciones sobre las características avanzadas del sistema de archivos NTFS es correcta, según Microsoft?
- a) Solo admite nombres de archivo de ocho caracteres y extensión de tres letras.
- b) Incluye descriptores de seguridad, cifrado, cuotas de disco y metadatos enriquecidos.  ✓
- c) Limita el tamaño de cada archivo a 4 GiB, igual que hace el sistema FAT32.
- d) Carece de cuotas de disco y de cifrado, que solo ofrece el cifrado BitLocker.
Cita: fuente: `ms-win-ntfs.html`; «Introducción a NTFS»
Explicación: La página dice que NTFS proporciona características avanzadas, incluidos descriptores de seguridad, cifrado, cuotas de disco y compatibilidad con metadatos enriquecidos. NTFS admite nombres de archivo largos con un alias 8.3 para compatibilidad, y la tabla de comparación da para NTFS un tamaño de archivo máximo de 2^64–1 bytes, mientras que los 4 GiB son el límite de FAT32.

## m02-l05-q111
¿Con qué se integra NTFS para permitir un almacenamiento de alta disponibilidad al que acceden a la vez varios nodos de un clúster de conmutación por error, según Microsoft?
- a) Con las listas de control de acceso (ACL).
- b) Con los volúmenes compartidos de clúster (CSV).  ✓
- c) Con el cifrado de unidad BitLocker.
- d) Con las cuotas de disco de cada usuario.
Cita: fuente: `ms-win-ntfs.html`; «Introducción a NTFS»
Explicación: La página dice que NTFS se integra con los volúmenes compartidos de clúster (CSV), lo que permite un almacenamiento de alta disponibilidad al que varios nodos de un clúster de conmutación por error pueden acceder simultáneamente. BitLocker cifra los datos, las ACL asignan permisos y las cuotas controlan el espacio por usuario.

## m02-l05-q112
¿Cuál de los siguientes conjuntos recoge los cuatro sistemas de archivos principales de Windows que compara la documentación de Microsoft?
- a) NTFS, exFAT, ext4 y FAT32.
- b) NTFS, HFS+, UDF y FAT32.
- c) NTFS, APFS, exFAT y UDF.
- d) NTFS, exFAT, UDF y FAT32.  ✓
Cita: fuente: `ms-win-sistemas-archivos.html`; «Comparación de la funcionalidad del sistema de archivos»
Explicación: La página compara «los cuatro sistemas de archivos principales de Windows, NTFS, exFAT, UDF y FAT32». Ext4, HFS+ y APFS no figuran en esa comparación, así que ninguna de las otras series coincide con los cuatro que da Microsoft.

## m02-l05-q113
Según la comparación de Microsoft de los sistemas de archivos de Windows, el tamaño de archivo máximo que admite FAT32 es de:
- a) 2 GiB.
- b) 4 GiB.  ✓
- c) 16 TB.
- d) 2^64–1 bytes.
Cita: fuente: `ms-win-sistemas-archivos.html`; «Tamaño de archivo máximo — 2^64–1 bytes — 2^64–1 bytes — 2^64–1 bytes — 4 GiB»
Explicación: En la tabla de límites, el tamaño de archivo máximo de FAT32 es de 4 GiB, mientras que NTFS, exFAT y UDF admiten 2^64–1 bytes. La tabla de límites da 4 GiB para FAT32, no 2 GiB. Los 16 TB son un límite de volumen de NTFS con clústeres de 4 KB, no el tamaño de archivo de FAT32. Los 2^64–1 bytes son el máximo de NTFS, exFAT y UDF, no el de FAT32.

## m02-l05-q114
¿Cuántos caracteres admite como máximo el nombre de un archivo en UDF, según la comparación de Microsoft de sistemas de archivos?
- a) 255 caracteres Unicode o 127 ASCII.
- b) 254 caracteres Unicode o 127 ASCII.
- c) 32 760 caracteres Unicode o 254 ASCII.
- d) 127 caracteres Unicode o 254 ASCII.  ✓
Cita: fuente: `ms-win-sistemas-archivos.html`; «Longitud máxima del nombre del archivo — 255 caracteres Unicode — 255 caracteres Unicode — 127 Caracteres Unicode o 254 ASCII — 255 caracteres Unicode»
Explicación: La tabla de límites da a UDF una longitud máxima de nombre de archivo de 127 caracteres Unicode o 254 ASCII, y 255 caracteres Unicode a NTFS, exFAT y FAT32. La opción de 255 caracteres Unicode es la de los otros tres sistemas. La de 254 caracteres Unicode invierte las cifras de UDF. Los 32 760 caracteres Unicode son el máximo del nombre de la ruta, no el del nombre del archivo.

## m02-l05-q115
¿Cuál de los siguientes sistemas de archivos de Windows ofrece cifrado de nivel de sistema de archivos, según la comparación de Microsoft?
- a) NTFS.  ✓
- b) exFAT.
- c) UDF.
- d) FAT32.
Cita: fuente: `ms-win-sistemas-archivos.html`; «Cifrado de nivel de sistema de archivos — Sí — No — No — No»
Explicación: En la tabla de seguridad, solo NTFS tiene «Sí» en cifrado de nivel de sistema de archivos; exFAT, UDF y FAT32 tienen «No».

## m02-l05-q116
¿Cuál de las siguientes características ofrecen los cuatro sistemas de archivos principales de Windows, NTFS, exFAT, UDF y FAT32, según la comparación de Microsoft?
- a) Listas de control de acceso.
- b) Compresión integrada.
- c) Marcas de tiempo de creación.  ✓
- d) Enlaces simbólicos.
Cita: fuente: `ms-win-sistemas-archivos.html`; «Marcas de tiempo de creación — Sí — Sí — Sí — Sí»
Explicación: En la tabla de funcionalidad, las marcas de tiempo de creación llevan «Sí» en los cuatro sistemas de archivos. Las listas de control de acceso, la compresión integrada y los enlaces simbólicos llevan «Sí» solo en NTFS.

## m02-l05-q117
¿Cuál de las siguientes características de los sistemas de archivos de Windows ofrece solo NTFS, de los cuatro principales, según la comparación de Microsoft?
- a) Conservación de mayúsculas y minúsculas.
- b) Marcas de tiempo de último cambio.
- c) Oplocks.
- d) Compresión integrada.  ✓
Cita: fuente: `ms-win-sistemas-archivos.html`; «Compresión integrada — Sí — No — No — No»
Explicación: La tabla de compresión da «Sí» a la compresión integrada en NTFS y «No» en exFAT, UDF y FAT32. La conservación de mayúsculas y minúsculas, las marcas de tiempo de último cambio y los oplocks llevan «Sí» en los cuatro sistemas.

## m02-l05-q118
¿Cuál de las siguientes combinaciones de cuotas de espacio en disco incorpora NTFS directamente, según la comparación de Microsoft de los sistemas de archivos de Windows?
- a) El de usuario, pero no el de directorio.  ✓
- b) El de directorio, pero no el de usuario.
- c) Los dos, el de usuario y el de directorio.
- d) Ninguno de los dos niveles.
Cita: fuente: `ms-win-sistemas-archivos.html`; «Comparación de la funcionalidad del sistema de archivos»
Explicación: La tabla de cuotas da «Sí» al espacio en disco de nivel de usuario y «No» al de nivel de directorio, que según la nota solo está disponible a través del servidor de archivos Resource Manager. Por eso no valen ni la opción del nivel de directorio sin el de usuario, ni la de los dos niveles, ni la de ninguno.

## m02-l05-q119
¿Cuál de las siguientes parejas de sistemas de archivos de Windows admite vínculos físicos, según la comparación de Microsoft de funcionalidades?
- a) NTFS y exFAT.
- b) exFAT y FAT32.
- c) UDF y FAT32.
- d) NTFS y UDF.  ✓
Cita: fuente: `ms-win-sistemas-archivos.html`; «Vínculos físicos — Sí — No — Sí — No»
Explicación: En la tabla de funcionalidad, los vínculos físicos llevan «Sí» en NTFS y UDF, y «No» en exFAT y FAT32. La tabla marca «No» a los vínculos físicos en exFAT. La tabla marca «No» a los vínculos físicos en exFAT y en FAT32. La tabla marca «No» a los vínculos físicos en FAT32.

## m02-l05-q120
¿Cuál de las siguientes parejas de sistemas de archivos de Windows distingue entre mayúsculas y minúsculas, según la comparación de Microsoft, aunque en uno de ellos solo como opción?
- a) exFAT y FAT32.
- b) NTFS, como opción, y FAT32.
- c) NTFS, como opción, y UDF.  ✓
- d) exFAT y UDF.
Cita: fuente: `ms-win-sistemas-archivos.html`; «Distingue mayúsculas y minúsculas — Sí (opción) — No — Sí — No»
Explicación: La tabla da «Sí (opción)» a NTFS y «Sí» a UDF en «Distingue mayúsculas y minúsculas», y «No» a exFAT y FAT32. La tabla marca «No» a esa característica en exFAT y en FAT32. La tabla marca «No» a esa característica en FAT32. La tabla marca «No» a esa característica en exFAT.

## m02-l05-q121
Según la comparación de Microsoft, la longitud máxima del nombre de la ruta en NTFS es de 32 760 caracteres Unicode, con cada componente de ruta de acceso no superior a:
- a) 127 caracteres.
- b) 255 caracteres.  ✓
- c) 512 caracteres.
- d) 32 760 caracteres.
Cita: fuente: `ms-win-sistemas-archivos.html`; «Comparación de la funcionalidad del sistema de archivos»
Explicación: La tabla de límites da a NTFS una ruta de hasta 32 760 caracteres Unicode, con cada componente no superior a 255 caracteres. La tabla fija en 255 caracteres el máximo de cada componente de la ruta, no en 127. La tabla fija en 255 caracteres el máximo de cada componente de la ruta, no en 512. Los 32 760 caracteres son el máximo de la ruta completa, no el de cada componente.

## m02-l05-q122
¿Cuál de las siguientes opciones recoge los sistemas de archivos de Windows que admiten enlaces simbólicos y puntos de montaje, según la comparación de Microsoft de funcionalidades?
- a) Solo NTFS.  ✓
- b) NTFS y UDF.
- c) NTFS y exFAT.
- d) Los cuatro sistemas.
Cita: fuente: `ms-win-sistemas-archivos.html`; «Enlaces simbólicos — Sí — No — No — No»
Explicación: En la tabla de funcionalidad, enlaces simbólicos y puntos de montaje llevan «Sí» solo en NTFS. La tabla marca «No» a los enlaces simbólicos en UDF. La tabla marca «No» a los puntos de montaje en exFAT. La tabla marca «No» a los enlaces simbólicos en exFAT, UDF y FAT32.

## m02-l05-q123
Según la página de Microsoft Azure sobre qué es el almacenamiento en la nube, este guarda los datos:
- a) en el disco duro del equipo, sincronizado con la red local.
- b) en hardware local de la organización, con copia en Internet.
- c) en servidores remotos a los que se accede online.  ✓
- d) en unidades de memoria de la propia aplicación móvil.
Cita: fuente: `azure-almacenamiento-nube.html`; «¿Qué es el almacenamiento en la nube?»
Explicación: La página define el almacenamiento en la nube como el que «guarda datos en servidores remotos a los que se accede online, en lugar de en hardware local». La página dice que se guardan en servidores remotos en lugar de en equipos locales o discos duros físicos. La página dice que se guardan en servidores remotos en lugar de en hardware local. La aplicación móvil solo es una vía de acceso mediante una API; los datos están en servidores remotos.

## m02-l05-q124
¿Cuántos modelos de almacenamiento en la nube distingue la página de Microsoft Azure sobre qué es el almacenamiento en la nube?
- a) Dos: público y privado.
- b) Tres: público, privado e híbrido.
- c) Cuatro: público, privado, híbrido y multinube.  ✓
- d) Cinco: público, privado, híbrido, multinube y comunitario.
Cita: fuente: `azure-almacenamiento-nube.html`; «¿Qué es el almacenamiento en la nube?»
Explicación: La página dice: «Hay cuatro modelos diferentes de almacenamiento en la nube: nubes públicas, privadas e híbridas, así como opciones multinube». Dos modelos dejan fuera el híbrido y el multinube, que la página enumera. Tres dejan fuera el multinube. Y cinco añaden un modelo comunitario que no está en la enumeración de la página, que cierra la lista en cuatro.

## m02-l05-q125
¿Cuál de los siguientes tipos de almacenamiento en la nube organiza los datos en unidades discretas, cada una con sus propios metadatos?
- a) El almacenamiento de archivos.
- b) El almacenamiento en bloque.
- c) El almacenamiento de objetos.  ✓
- d) El almacenamiento en multinube.
Cita: fuente: `azure-almacenamiento-nube.html`; «¿Qué es el almacenamiento en la nube?»
Explicación: La página dice que «el almacenamiento de objetos organiza los datos en unidades discretas u objetos, cada uno con sus propios metadatos». El almacenamiento de archivos mantiene una estructura jerárquica de carpetas y directorios. El almacenamiento en bloque divide los datos en bloques de tamaño fijo. La multinube no es un tipo de almacenamiento sino un modelo, que usa servicios de varios proveedores.

## m02-l05-q126
¿Cuál de los siguientes usos resulta adecuado para el almacenamiento en bloque, según la página de Microsoft Azure sobre el almacenamiento en la nube?
- a) Para sistemas de archivos compartidos y aplicaciones colaborativas.
- b) Para grandes cantidades de datos no estructurados, como imágenes o vídeos.
- c) Para mantener la información regulada en un entorno privado.
- d) Para bases de datos y aplicaciones de alto rendimiento.  ✓
Cita: fuente: `azure-almacenamiento-nube.html`; «¿Qué es el almacenamiento en la nube?»
Explicación: Según la página, el almacenamiento en bloque divide los datos en bloques de tamaño fijo que «se pueden recuperar rápidamente, lo que hace que este tipo sea adecuado para bases de datos y aplicaciones de alto rendimiento». Los sistemas de archivos compartidos y las aplicaciones colaborativas son el uso del almacenamiento de archivos. Los datos no estructurados como imágenes y vídeos son el uso ideal del almacenamiento de objetos. Mantener la información regulada en un entorno privado es una característica del modelo de nube híbrida.

## m02-l05-q127
¿Cuál de los siguientes modelos de almacenamiento en la nube está dedicado a una sola organización y puede hospedarse de forma local o mediante un proveedor de servicios?
- a) La nube privada.  ✓
- b) La nube pública.
- c) La nube híbrida.
- d) La multinube.
Cita: fuente: `azure-almacenamiento-nube.html`; «¿Qué es el almacenamiento en la nube?»
Explicación: La página dice que el almacenamiento en la nube privada «está dedicado a una sola organización» y que «se puede hospedar de forma local o mediante un proveedor de servicios». En la nube pública, proveedores de terceros entregan el almacenamiento a través de Internet y las organizaciones comparten recursos. La nube híbrida combina modelos públicos y privados. La multinube usa servicios de varios proveedores.

## m02-l05-q128
¿Cuál de los siguientes modelos de almacenamiento en la nube permite que la información confidencial o regulada permanezca en un entorno privado y las cargas menos críticas pasen a la nube pública?
- a) La nube pública.
- b) La nube híbrida.  ✓
- c) La nube privada.
- d) La multinube.
Cita: fuente: `azure-almacenamiento-nube.html`; «¿Qué es el almacenamiento en la nube?»
Explicación: La página dice que la nube híbrida «combina modelos públicos y privados»: la información confidencial o regulada puede permanecer en un entorno privado y las cargas menos críticas se mueven a la nube pública. En la nube pública las organizaciones comparten recursos con otras personas, aunque aisladas en el nivel de datos. La nube privada está dedicada a una sola organización y no combina modelos. La multinube sirve para evitar el bloqueo del proveedor, optimizar costes o cumplir requisitos regionales.

## m02-l05-q129
¿Cuál de las siguientes opciones es un beneficio del almacenamiento en la nube, según la página de Microsoft Azure?
- a) La rentabilidad: la organización solo paga por el almacenamiento que usa.  ✓
- b) El gasto de capital inicial que supone comprar y mantener hardware propio.
- c) Una capacidad fija, que no puede expandirse ni contraerse con la demanda.
- d) Los datos alojados en un único servidor, sin replicar entre regiones.
Cita: fuente: `azure-almacenamiento-nube.html`; «¿Qué es el almacenamiento en la nube?»
Explicación: Entre los beneficios, la página cita la rentabilidad: «las organizaciones solo pagan por el almacenamiento que usan, lo que evita el gasto de capital de comprar y mantener hardware». La página dice que se evita el gasto de capital de comprar y mantener hardware. La página dice que la capacidad puede expandirse o contraerse rápidamente. La página dice que los datos se distribuyen y replican entre servidores y regiones.

## m02-l05-q130
¿Cuál de las siguientes definiciones corresponde a la durabilidad en el almacenamiento en la nube, según la página de Microsoft Azure?
- a) La capacidad de ampliar o reducir el espacio según la demanda.
- b) La capacidad de conservar los datos a lo largo del tiempo sin pérdida.  ✓
- c) La capacidad de pagar solo por el almacenamiento que se usa.
- d) La capacidad de recuperar las copias en ubicaciones independientes.
Cita: fuente: `azure-almacenamiento-nube.html`; «¿Qué es el almacenamiento en la nube?»
Explicación: La página define la durabilidad como «la capacidad de conservar los datos a lo largo del tiempo sin pérdida», que se aumenta replicando los datos entre regiones. Ampliar o reducir el espacio según la demanda es la escalabilidad. Pagar solo por lo que se usa es la rentabilidad. Almacenar copias en ubicaciones independientes es lo que la página relaciona con mantener la disponibilidad.

## m02-l05-q131
En el sistema operativo Windows, ¿cuál de los siguientes administradores del modo kernel administra la memoria física, según la documentación de Microsoft?
- a) El administrador de memoria.  ✓
- b) El administrador de objetos.
- c) El administrador de E/S.
- d) El administrador de energía.
Cita: fuente: `ms-win-componentes-kernel.html`; «Guía de diseño de la arquitectura del controlador en modo kernel»
Explicación: El administrador de memoria del modo kernel de Windows «administra la memoria física para el sistema operativo». El administrador de objetos administra archivos, dispositivos, mecanismos de sincronización y claves del Registro. El administrador de E/S administra la comunicación entre las aplicaciones y las interfaces de los controladores de dispositivo. El administrador de energía administra el cambio ordenado en el estado de energía de los dispositivos.

## m02-l05-q132
¿Qué función cumple el administrador de procesos y subprocesos en modo kernel de Windows, según la documentación de Microsoft?
- a) Administra la memoria física para el sistema operativo.
- b) Administra la comunicación entre las aplicaciones y los controladores de dispositivo.
- c) Controla la ejecución de todos los subprocesos de un proceso.  ✓
- d) Implementa el procesamiento de transacciones en modo kernel.
Cita: fuente: `ms-win-componentes-kernel.html`; «Guía de diseño de la arquitectura del controlador en modo kernel»
Explicación: La documentación dice que el administrador de procesos y subprocesos «controla la ejecución de todos los subprocesos de un proceso». Administrar la memoria física es la función del administrador de memoria; la comunicación entre las aplicaciones y los controladores de dispositivo, la del administrador de E/S; y el procesamiento de transacciones, la del administrador de transacciones kernel.

## m02-l05-q133
En el modo kernel de Windows, ¿cuál de los siguientes administradores gestiona la comunicación entre las aplicaciones y las interfaces proporcionadas por los controladores de dispositivo?
- a) El administrador de Plug and Play.
- b) El administrador de E/S.  ✓
- c) El administrador de memoria.
- d) El administrador de energía.
Cita: fuente: `ms-win-componentes-kernel.html`; «Guía de diseño de la arquitectura del controlador en modo kernel»
Explicación: La documentación dice que el administrador de E/S «administra la comunicación entre las aplicaciones y las interfaces proporcionadas por los controladores de dispositivo». El administrador de Plug and Play permite al equipo reconocer cuándo se agrega un dispositivo; la documentación lo describe como subsistema del de E/S. El administrador de memoria administra la memoria física. El administrador de energía administra el cambio ordenado en el estado de energía de los dispositivos.

## m02-l05-q134
¿Cuál de los siguientes administradores del modo kernel de Windows administra objetos como archivos, dispositivos, mecanismos de sincronización y claves del Registro?
- a) El administrador de memoria.
- b) El administrador de energía.
- c) El administrador de transacciones kernel.
- d) El administrador de objetos.  ✓
Cita: fuente: `ms-win-componentes-kernel.html`; «Guía de diseño de la arquitectura del controlador en modo kernel»
Explicación: La documentación dice que el administrador de objetos «administra objetos: archivos, dispositivos, mecanismos de sincronización, claves del Registro, etc.». El administrador de memoria administra la memoria física. El administrador de energía administra el cambio ordenado en el estado de energía de los dispositivos. El administrador de transacciones kernel implementa el procesamiento de transacciones.

## m02-l05-q135
En Windows, ¿cuál de los siguientes administradores permite a un equipo reconocer cuándo se agrega un dispositivo al sistema, según la documentación de Microsoft sobre el modo kernel?
- a) El administrador de energía.
- b) El administrador de Plug and Play.  ✓
- c) El administrador de configuración.
- d) El monitor de referencia de seguridad.
Cita: fuente: `ms-win-componentes-kernel.html`; «Guía de diseño de la arquitectura del controlador en modo kernel»
Explicación: La documentación dice que el administrador de Plug and Play «permite a un equipo reconocer cuándo se agrega un dispositivo al sistema». El administrador de energía administra el cambio ordenado en el estado de energía de los dispositivos. El administrador de configuración administra el registro. El monitor de referencia de seguridad proporciona rutinas para trabajar con el control de acceso.

## m02-l05-q136
¿Qué administra el administrador de energía en modo kernel de Windows, según la documentación de Microsoft?
- a) El registro de Windows y la supervisión de sus cambios.
- b) La memoria física que usa el sistema operativo.
- c) El cambio ordenado del estado de energía de los dispositivos.  ✓
- d) La ejecución de todos los subprocesos de un proceso en marcha.
Cita: fuente: `ms-win-componentes-kernel.html`; «Guía de diseño de la arquitectura del controlador en modo kernel»
Explicación: El administrador de energía «administra el cambio ordenado en el estado de energía de todos los dispositivos que admiten cambios de estado de energía». Administrar el registro es la función del administrador de configuración. Administrar la memoria física es la función del administrador de memoria. Controlar la ejecución de los subprocesos es la función del administrador de procesos y subprocesos.

## m02-l05-q137
En el modo kernel de Windows, ¿cuál de los siguientes administradores administra el registro, por ejemplo supervisando sus cambios?
- a) El administrador de configuración.  ✓
- b) El administrador de memoria.
- c) El administrador de E/S.
- d) El administrador de energía.
Cita: fuente: `ms-win-componentes-kernel.html`; «Guía de diseño de la arquitectura del controlador en modo kernel»
Explicación: La documentación dice que el administrador de configuración «administra el registro, como la supervisión de cambios en el registro o el registro de devoluciones de llamada en datos específicos del Registro». El administrador de memoria administra la memoria física. El administrador de E/S administra la comunicación entre las aplicaciones y los controladores de dispositivo. El administrador de energía administra el cambio ordenado en el estado de energía de los dispositivos.

## m02-l05-q138
¿Cuál de los siguientes componentes del modo kernel de Windows proporciona rutinas para que el controlador funcione con el control de acceso?
- a) El administrador de transacciones kernel.
- b) El administrador de energía.
- c) El administrador de configuración.
- d) El monitor de referencia de seguridad.  ✓
Cita: fuente: `ms-win-componentes-kernel.html`; «Guía de diseño de la arquitectura del controlador en modo kernel»
Explicación: La documentación dice que el monitor de referencia de seguridad «proporciona rutinas para que el controlador funcione con el control de acceso». El administrador de transacciones kernel implementa el procesamiento de transacciones. El administrador de energía administra el cambio ordenado en el estado de energía de los dispositivos. El administrador de configuración administra el registro.

## m02-l05-q139
Según la documentación de Microsoft sobre el modo kernel de Windows, ¿qué proporciona el kernel de Microsoft Windows?
- a) Una capa de abstracción de hardware para el desarrollo de controladores.
- b) Un sistema de registro transaccional, el sistema de archivos de registro común.
- c) Operaciones básicas de bajo nivel, como programar hilos o enrutar interrupciones.  ✓
- d) Una biblioteca de acceso directo a memoria para desarrolladores de controladores.
Cita: fuente: `ms-win-componentes-kernel.html`; «Guía de diseño de la arquitectura del controlador en modo kernel»
Explicación: La documentación dice que «el kernel de Microsoft Windows proporciona operaciones básicas de bajo nivel, como programar hilos o enrutamiento de interrupciones de hardware». La capa de abstracción de hardware es la función de la biblioteca HAL, no la del kernel. El sistema de registro transaccional es la función de la biblioteca CLFS, no la del kernel. La biblioteca de acceso directo a memoria es la función de la biblioteca DMA, no la del kernel.

## m02-l05-q140
Según la página de soporte técnico de Apple, el sistema operativo del ordenador Mac se llama:
- a) Time Machine.
- b) macOS.  ✓
- c) Windows.
- d) Recuperación de macOS.
Cita: fuente: `apple-macos.html`; «Soporte para macOS»
Explicación: La página dice que Recuperación de macOS sirve para «reinstalar el sistema operativo del Mac», y su título es «Soporte para macOS». Time Machine es la herramienta de copia de seguridad automática del Mac, no su sistema operativo. El sistema operativo que reinstala Recuperación de macOS es el del Mac, al que la página llama macOS, no Windows. Recuperación de macOS es la herramienta para reinstalar el sistema operativo, no el sistema operativo.

## m02-l05-q141
¿Qué herramienta de macOS permite hacer una copia de seguridad automática de los datos en un dispositivo de almacenamiento externo conectado al Mac?
- a) Time Machine.  ✓
- b) Recuperación de macOS.
- c) Copias de seguridad de Windows.
- d) Historial de archivos.
Cita: fuente: `apple-macos.html`; «Soporte para macOS»
Explicación: La página dice que, con un dispositivo de almacenamiento externo conectado al Mac, «podrás usar Time Machine para hacer una copia de seguridad automática de tus datos». Recuperación de macOS sirve para reinstalar el sistema operativo, no para hacer copias de seguridad. Copias de seguridad de Windows es la herramienta de los equipos Windows, no de macOS. El Historial de archivos es una función de Windows, no de macOS.
