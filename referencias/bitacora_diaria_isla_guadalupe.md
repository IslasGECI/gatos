Bitácora de actividades - Isla Guadalupe 
---

### David Martínez

**Fecha**: domingo 18 de febrero del 2018

**Localización**: Estación bosque

**Actividades del día**:

- Desembarco. El desembarco inició a las 7:00 horas y concluyó a las 13:00 horas.
- Arrribo a la estación. El arribo a la estación ocurrió a las 16:30 horas.

**Observaciones**:

- No hay observaciones.

--- 

**Fecha**: lunes 19 de febrero del 2018

**Localización**: Estación bosque

**Actividades del día**:

- Reunión informativa general de 8:00 a 9:00 horas.
- Reunión informativa para el equipo de gatos de 9:00 a 10:00 horas. Durante la reunión David Cosío le mencionó al equipo de gatos las cosas que esperan que yo trabaje aquí, entre las que están: morfometría de gatos, transectos nocturnos, cámaras trampa y rutas y marcaje de perros. Preguntaron también si es necesario seguir tomando datos morfométricos de gatos a lo que contesté que por lo pronto sí; que una vez procesados los datos sabremos si ya no es necesario.
- Me instalé en la oficina y verifiqué que la computadora estuviera funcionando en óptimas condiciones.

**Observaciones**:

- La oficina es usada también como almacén y para poner al día los equipos informáticos y de telemetría, por lo que no me será posible trabajar ahí.
- El horario de internet para la carga y descarga de archivos y actualizaciones en la estación bosque es de 23:00 a 3:00 horas. Tendré que usar ese tiempo para mi comunicación con el equipo de AC, descarga de datos y actualización de repositorios.
- Inicio de mal tiempo, por lo que la conexión a internet no fue posible en todo el día.
- Es imperativo que me comunique con el equipo de Análisis para discutir sobre el procesamiento de datos morfométricos de datos. David Cosío sugirió, a modo de pregunta, si yo haría el procesamiento aquí en la isla; yo considero que es conveniente que así sea.

---

**Fecha**: martes 20 de febrero del 2018

**Localización**: Estación bosque

**Actividades del día**:

- Durante la mañana recibimos un taller para manejo de gatos (colocación de gps's), sacrificio de gatos y uso de trampas cepo. Para el manejo y sacrificio de gatos aprendimos, principalmente, las dosis y administración de fármacos; usamos dos gatos vivos que estaban en la estación para la práctica.
- Durante la tarde realicé una caminata de reconocimiento hacia la parte oeste del campamento, cruzando un bosque joven de ciprés y llegando al borde de la isla.

**Observaciones**:

- Hoy tuve que cargar la batería de la computadora nuevamente sin haberla usado demasiado. Parece que se está descargando muy rápido.
- Debido a las condiciones meteorológicas no hay conexión a internet, por lo que no he podido comunicarme con el equipo de AC.

**Observaciones sobre el trabajo en la estación**:

- Falta llevar algún tipo de relación sobre las cosas que se hacen; las provisiones que llegan y se consumen; la gente que se mueve entre estaciones; la gente que entra a la isla y la que baja de la isla.

**Actividades para el día de mañana 21 de febrero**:

- Posible salida a punta sur para reunirnos con el personal de trampeo. De realizarse el traslado no sé cuánto dure el viaje y la instalación en el campamento.

- Crear una copia de la base de datos que se usa en la capacitación y modificarla para crear una base de datos sintéticos que simule los datos de esfuerzo y captura de gatos aquí en la isla.
- Si hay internet, descargar la base de datos de morfometría de gatos. Comunicarme con el equipo de AC para discutir el procesamiento de esta base de datos.
- Hasta ahora no he podido revisar alguna base de datos de esfuerzo y capturas, una base de datos está en una computadora que no tiene el cargador y la otra base de datos está en una máquina en punta sur.

---

**Fecha**: miércoles 21 de febrero del 2018

**Localización**: Estación bosque

**Actividades del día**:

- Diseño de la base de datos para la actividad de monitoreo de trampas y captura de gatos. Trabajé en primer lugar con Salvador Figueroa (Fungi), discutiendo las variables que ellos toman en el campo y las que yo necesitaría para hacer los estudios de esfuerzo y de captura. Enseguida se unió a la discusión David Cosío (Cosío), quien es uno de los coordinadores del proyecto de gatos. De la discusión resultaron dos bases de datos: `DISPOSICION_TRAMPAS_CEPO.XLSX` y `ESFUERZO_CAPTURA_GATOS.XSLX`. La base de datos `DISPOSICION_TRAMPAS_CEPO.XLSX` contendrá la fecha y la hora de colocación de la trampa, el identificador de la trampa y la posición (longitud y latitud); la base de datos `ESFUERZO_CAPTURA_GATOS.XSLX` contendrá la fecha de revisión de la trampa, el identificador de la trampa, las iniciales de la persona que está revisando la trampa, la condición de la trampa (si está activa o inactiva) y si hubo captura o no. A partir de la segunda base de datos es de donde estaremos calculando el esfuerzo, utilizado y la cantidad de capturas.

`DISPOSICION_TRAMPAS_CEPO.XLSX`:

| fecha | ID de trampa | longitud | latitud | 
|-------|--------------|----------|---------| 
| 2018-02-21T00:00:00 | TC-01-001-DN | 123 | 456 | 
| 2018-02-21T00:00:00 | TC-01-002-DN | 123 | 456 | 
| 2018-02-21T00:00:00 | TC-01-003-DN | 123 | 456 | 
| 2018-02-21T00:00:00 | TC-01-004-DN | 123 | 456 | 
| 2018-02-21T00:00:00 | TC-01-005-DN | 123 | 456 | 
| 2018-02-21T00:00:00 | TC-01-006-DN | 123 | 456 | 
| 2018-02-21T00:00:00 | TC-01-007-DN | 123 | 456 | 
| 2018-02-21T00:00:00 | TC-01-008-DN | 123 | 456 | 
| 2018-02-21T00:00:00 | TC-01-009-DN | 123 | 456 | 
| 2018-02-21T00:00:00 | TC-01-010-DN | 123 | 456 | 

`ESFUERZO_CAPTURA_GATOS.XSLX`:

| fecha de revision | ID del personal | ID de trampa | condicion | captura |

|-------------------|-----------------|--------------|-----------|---------|
| 2018-02-22T00:00:00 | DN | TC-01-001-DN | activa | 0 | 
| 2018-02-22T00:00:00 | DN | TC-01-002-DN | activa | 0 | 
| 2018-02-22T00:00:00 | DN | TC-01-003-DN | activa | 0 | 
| 2018-02-22T00:00:00 | DN | TC-01-004-DN | activa | 0 | 
| 2018-02-22T00:00:00 | DN | TC-01-005-DN | activa | 1 | 
| 2018-02-22T00:00:00 | JS | TC-01-006-DN | activa | 0 | 
| 2018-02-22T00:00:00 | JS | TC-01-007-DN | activa | 0 | 
| 2018-02-22T00:00:00 | JS | TC-01-008-DN | activa | 1 | 
| 2018-02-22T00:00:00 | JS | TC-01-009-DN | activa | 1 | 
| 2018-02-22T00:00:00 | JS | TC-01-010-DN | activa | 0 | 

**Observaciones**:

- Resultó bastante productivo haber trabajado con el Fungi, ya que él ha estado más tiempo trabajando con las trampas, y haber trabajado con Cosío, ya que él tiene una visión un poco más amplia del proyecto, aparte que es el tomador de decisiones en ausencia de la directora del proyecto.

- De la discusión resultó que la nomenclatura del identificador de las trampas resultaba confuso, ya que se repetían series de números por persona, teniendo muchas trampas con numeración del 1-30 en el mismo sector (en este momento cada persona está trabajando con 30 trampas); llegamos a un acuerdo para disponer números consecutivos a las trampas por sector, quedando de la siguiente manera: `TT-XX-YYY-AA`, donde: TT es el tipo de trampa; `XX` es el sector que se está trabajando; `YYY` es el número de la trampa (que irá de 1-40 para la primer persona, del 41-80 para la segunda persona, del 81-120 para la tercera persona, y así sucesivamente); y `AA` son las iniciales del personal de trampeo.


- La posible salida a punta sur es el sábado 24 de febrero.

- Debido a las condiciones meteorológicas no fue posible comunicarme con el equipo de AC.

---

**Fecha**: jueves 22 de febrero del 2018

**Localización**: Estación bosque

**Actividades del día**:

- Durante la mañana participé en la práctica de colocación de trampas. La práctica la hicimos en el bosque que está al lado de la estación.

- Trabajé con Cosío y Mauricio Canales en la configuración de los collares de rastreo que usarán los perros y discutimos brevemente sobre la información que se obtiene de los collares.

- Añadí algunos datos sintéticos a las dos bases de datos hasta ahorita diseñadas.

- Durante la tarde hubo una reunión informativa sobre el trabajo de disposición y monitoreo de trampas y trabajo con los perros en punta sur.

**Observaciones**:

- La salida a punta sur será, según las condiciones meteorológicas, el sábado 24 de febrero.

- Yo me trasladaré mañana viernes a punta sur a llevar algunas provisiones y en el camino cambiaremos las memorias de las trampas cámara. El regreso a la estación bosque será mañana mismo.

- Durante la reunión informativa se mencionó que los collares de telemetría llegarán en la avioneta el día 7 de marzo.

- Debido a las condiciones meteorológicas no fue posible comunicarme con el equipo de AC.

---

**Fecha**: viernes 23 de febrero del 2018

**Localización**: Estación punta sur

**Actividades del día**:

- Traslado a la estación de punta sur. Cargamos provisiones justo después de la comida, de 8:00 a 10:00 horas. A las 10:00 horas nos trasladamos a la estación en punta sur, llegando a la 13:00 horas. Descargamos las provisiones de las 13:00 a las 13:30 horas.

**Observaciones**:

- No realizamos el cambio de las memorias de las cámaras trampa ya que no contábamos con las memorias que debíamos colocar.
- Hoy conocí a los albatros adultos y pollos.

---

**Fecha**: sábado 24 de febrero del 2018

**Localización**: Estación punta sur

**Actividades del día**:

- Revisión de trampas cepo. Acompañé a David Nájera a revisar un transecto de trampas; de esta manera conocí el terreno y la forma como revisan las trampas una vez colocadas.

**Observaciones**:

- El terreno es muy abrupto; las trampas están bastante esparcidas debido a esto. Será imposible realizar la verificación de trampas ya sea de forma sistemática o aleatoria.

---

**Fecha**: domingo 25 de febrero del 2018

**Localización**: Estación punta sur

**Actividades del día**:

- Limpieza de la estación.
- Traslado a la estación bosque. Me trasladé a la estación con la finalidad de recoger ropa para regresar a la estación en punta sur.

**Observaciones**:

- No hay observaciones.

---

**Fecha**: lunes 26 de febrero del 2018

**Localización**: Estación bosque

**Actividades del día**:

- Carga de provisiones y herramientas del equipo canino. El equipo canino comenzará a trabajar en punta sur para marcar rastros de gatos.
- Traslado a punta sur.

**Observaciones**:

- Complicaciones en el traslado de perros. Fue complicado trasladar a los perros ya que no teníamos las herramientas ni los implementos necesarios. Fue necesario acondicionar un remolque para el traslado; eso era algo que no estaba previsto. Llegamos a la estación punta sur hacia las 18:00 horas.

---

**Fecha**: martes 27 de febrero del 2018

**Localización**: Estación punta sur

**Actividades del día**:

- Añadí metadatos a las dos bases de datos creadas. Hoy trabajaré con Salvador Figueroa para comenzar a capturar los datos reales.
- Creé el programa `tamano_restante_poblacion.py` que realizará el procesamiento de la base de datos `ESFUERZO_CAPTURA_GATOS.XLSX`. El programa realizará un procesamiento para obtener las variables de esfuerzo acumulado y capturas acumuladas. Usando estas dos últimas variables obtendré el tamaño de la población, para obtener enseguida la cantidad de indivíduos restantes para alcanzar el 90% de la población.
- Al final del día tuve una plática con David Cosío y Salvador Figueroa sobre la base de datos `ESFUERZO_CAPTURA_GATOS.XLSX`. En la plática les comenté que me había percatado que llenar la tabla que había diseñado iba a tomar mucho tiempo, con mucha susceptibilidad de que se cometan errores durante la captura. Hicimos un rediseño de la base de datos. En la nueva base de datos el encargado estará capturando diariamente la fecha del día, la cantidad de trampas activas, la cantidad de inviduos capturados y, en una sola columna, los identificadores de las trampas donde fueron capturados los gatos y observaciones. Con esta tabla igualmente podremos calcular el esfuerzo acumulado y las capturas acumuladas. La tabla quedó de la siguiente manera:

`ESFUERZO_CAPTURA_GATOS.XSLX`:

| fecha de revision | cantidad de trampas | individuos capturados | observaciones |
|-------------------|-----------------|--------------|-----------|
| 2018-02-22T00:00:00 | 145 | 1 | El individuo ... |
| 2018-02-22T00:00:00 | 145 | 2 | SO |
| 2018-02-22T00:00:00 | 145 | 0 | La trampa ... |
| 2018-02-22T00:00:00 | 155 | 1 | SO |
| 2018-02-22T00:00:00 | 165 | 0 | SO |
| 2018-02-22T00:00:00 | 175 | 0 | SO |
| 2018-02-22T00:00:00 | 175 | 3 | Bla bla bla |
| 2018-02-22T00:00:00 | 175 | 5 | SO |
| 2018-02-22T00:00:00 | 175 | 0 | Bla bla bla |
| 2018-02-22T00:00:00 | 175 | 2 | Bla bla bla |

**Observaciones**:

- Me tocó hacer la comida y fui por agua de mar al muelle que está en la estación de los marinos.

---

**Fecha**: miércoles 28 de febrero del 2018

**Localización**: Estación punta sur

**Actividades del día**:

- Inicio del estudio de la morfometría de gatos. Descargué la base de datos durante la noche. Durante el día hice una copia de la base de datos a la cual le estuve haciendo modificaciones, dejando la original intacta. Las modificaciones fueron necesarias ya que la base de datos contenía encabezados y renglones que impedían el procesamiento.
- Una vez modificada la base de datos, creé un programa en `R` para realizar el procesamiento.
- Creé un reporte vacío, el cual contendrá los resultados obtenidos de la base de datos de morfometría de gatos.
- No pude crear un `RMarkdown` ya que hay paquetes  de `R` que necesitan ser actualizados.

**Observaciones**:

- La base de datos requirió de modificaciones extensas. En las variables no numéricas reduje las categorías de la edad, sexo, estado reproductivo y tipos de trampas; en las variables numéricas borré guiones, palabras y caracteres especiales, así como comas o dobles puntos.
- Me tocó hacer nuevamente la comida. Por estar en la estación a la hora de la comida, me dispuse a hacer la comida por segunda ocasión; el personal no se ha organizado para la comida y la cena, no haré la comida nuevamente a menos que me toque en la repartición de labores.

---

**Fecha**: jueves 1 de marzo del 2018

**Localización**: Estación punta sur

**Actividades del día**: 

- Calculé la estadística descriptiva de las variables de interés de la morfometría de gatos, sin hacer alguna distinción por categoría.
- Trabajé en un programa en Matlab para crear una cuadrícula que simule la posición de los cuadrantes de muestreo. Esta cuadrícula podría servir para definir las posiciones donde se colocarán las trampas reales.
- Por la noche descargué los paquetes necesarios para poder crear un `Rmarkdown`.

**Observaciones**:

- Una vez incluídos en el reporte los resultados para cada variable comenzaré a determinar la estadística descriptiva para las categorías de cada variable.
- Creí conveniente comenzar a trabajar en la generación de la malla que simula las posiciones de las trampas ya que la cuadrícula con las posiciones donde se colocarán las trampas no está a la mano. Según esto, David Cosío pidió la cuadrícula a Luciana desde el jueves 22 de enero pero aún no la ha enviado. Me dí cuenta que, aunque la cuadrícula exista, ese problema será recurrente, ya que no están haciendo el diseño de la colocación de las trampas con anticipación. En este momento los puntos donde estarán colocadas las trampas los está creando Carlos Tafoya (un técnico eventual) en ArcGIS; ¿qué pasará cuando no esté Carlos Tafoya?. La malla creada en Matlab se podrá usar traslapando las curvas de nivel para visualizar el terreno y diseñar de una manera óptima la cuadrícula real. El diseño de la cuadrícula para la colocación de las trampas es un trabajo que deberíamos estar haciendo en conjunto con Ana Cárdenas, ya sea aquí en la isla o en Ensenada. Ahorita los puntos para trabajar durante este periodo (por lo menos hasta el siguiente barco) ya están diseñados; debemos prevenirnos para el trabajo en el siguiente sector.

---

**Fecha**: viernes 2 de marzo del 2018

**Localización**: Estación punta sur

**Actividades del día**: 

- Acompañé a Angel Méndez al islote morro prieto para reconocimiento del terreno. La excursión nos llevó desde las 6:00 hasta las 17:00 horas.
- Apoyé en la verificación del estado de los nidos y pollos de albatros y en la búsqueda de madrigueras de aves nocturnas.

**Observaciones**:

- En verdad es un esfuerzo enorme el que se debe hacer para la búsqueda exahustiva de madrigueras.

---

**Fecha:** sábado 3 de marzo del 2018

**Localización:** Estación punta sur

**Actividades del día:**

- Creé el programa `morfometría_gatos_isla_guadalupe.Rmd` donde obtuve la estadística descriptiva de las variables numéricas de la morfometría de gatos. Por el momento no separé las variables por categorías ni por sitios en la isla.
- Trabajé junto con David Cosío y Salvador Figueroa para corregir la nomenclatura designada para cada trampa. El trabajo lo hicimos en excel; yo estuve mayormente como observador, supervisando que el nombre de las trampas quedara como lo habíamos acordado.
- Trabajé junto con Salvador Figueroa y Carlos Tafoya en el diseño de la ubicación de trampas cepo. Exporte una malla a `kml` desde Matlab. Carlos Tafoya importó esta malla en ArcGIS para solamente acomodar los puntos según la conveniencia tomando en cuenta las trampas ya colocadas.

**Observaciones:**

- Me pareció más fácil trabajar en el `.Rmd` y no estar exportando tablas y gráficas para importarlas en el `.tex`.
- Había olvidado que a estas personas les gusta trabajar en hojas de cálculo; es complicado poder explicar por qué quiero las bases de datos en cierto formato y no en cualquier otro.
- Carlos Tafoya estaba creando en ArcGIS un punto a la vez, con una separación de 200 metros de los puntos aledaños. Con la malla importada será más fácil designar la posición de los puntos, ya que solamente tendrá que mover los puntos que ya existen según los puntos anteriores. Falta obtener las curvas de nivel del terreno para que él pueda visualizarlas en el ArcGIS. Yo solamente pude exportar los archivos `shp` y `shx` pero me faltan los otros dos, que en este momento no recuerdo sus extensiones, para que Carlos pueda visualizarlas en ArcGIS.

---

**Fecha:** domingo 4 de marzo del 2018

**Localización:** Estación punta sur

**Actividades del día:**

- Acompañé a la unidad canina en su trabajo con los perros. Los binomios perro-humano estuvieron buscando y marcando rastros en la zona donde los técinos pondrán trampas en los siguientes días. Esa zona aún está dentro del sector 1.
- Me trasladé a la estación bosque.

**Observaciones:**

- Es una travesía estar trasladando a la gente y los perros al mismo tiempo, no existe el equipo ni las unidades adecuadas. Nos tuvimos que trasladar en dos carros y llevar un remolque. Los traslados son tardados debido a eso.

---

**Fecha:** lunes 5 de marzo del 2018

**Localización:** Estación bosque

**Actividades del día:**

- Limpieza de la estación. Aunque el domingo 4 de marzo fue día de limpieza en la estación hoy también hicimos limpieza, ya que mañana martes llegan Julio Montoya y Luciana Luna. A mí me correspondió el almacén donde limpié y acomodé unas cajas de comida y unas hieleras.
- Creé el resumen del reporte. Coloqué el encabezado de la tabla y los pies de las figuras.

**Observaciones:**

---

**Fecha:** martes 6 de marzo del 2018

**Localización:** Estación bosque

**Actividades del día:**

- Envié las bitácoras diarias y semanal.
- Descargué el libro *Learning to program with python* de Richard L. Halterman, edición 2011.
- Estudié el libro *Learning to program with python*.
- Corrí el notebook `tamanio_poblacion.ipybn`.
- Agregué los nombres de las columnas y los metadatos a la tabla de datos `REGISTRO_CAMARAS_TRAMPA.XLSX`.
- Hice una pequeña actualización al README. Moví el resultado de biología/ecología de datos al principio de la sección de resultados esperados. Ya qué será el primer resultado que entregaremos.

**Observaciones:**

- Me percaté que necesito instalar la librería `pymc3` y agregar la variable de entorno `MKL_THREADING_LAYER` con el nombre `GNU`.
- Luciana Luna me entregó el USB que me mandó el equipo de AC, el cual contiene el _docker_ con todo lo necesario para correr el notebook `tamanio_poblacion.ipybn`.

---

**Fecha:** miércoles 7 de marzo del 2018

**Localización:** Estación bosque

**Actividades del día:**

- Traslado a la estación biológica de punta sur.
- Agregué datos a la tabla de datos `POSICION_TRAMPAS_CEPO.XLSX`. Estos datos me los facilitó Carlos Tafoya después de que todo el personal le pasó la actualización de las trampas colocadas.
- Visualicé las trampas cepo colocadas. Creé el programa `visualizacion_posicion_trampas_activas.m` para poder ver las trampas colocadas sobre el mapa de Isla Gpe.
- Ejecuté el contenido del _docker_ siguiente las instrucciones del archivo `guiaDocker.docx` del directorio `Pymc3 with Docker`.

**Observaciones:**

- El archivo `POSICION_TRAMPAS_CEPO.XLSX` ya contiene información de trampas que están inactivas, sin embargo el programa `visualizacion_posicion_trampas_activas.m` no hace distinción entre trampas activas o inactivas.
- No logré correr el contenido del _docker_. Aunque seguí las instrucciones en repetidas ocasiones no fui capaz de correr el archivo deseado del _docker_.

---

**Fecha:** jueves 8 de marzo del 2018

**Localización:** Estación punta sur

**Actividades del día:**

- Revisé, junto con Luciana Luna, las tablas de datos hasta ahora creadas. Revisamos el diseño y contenido de la tabla `POSICION_TRAMPAS_CEPO.XLSX` y el diseño de la tabla `ESFUERZO_CAPTURA_GATOS.XLSX`.
- Visualicé en un mapa, junto con Luciana Luna, el contenido de la tabla `POSICION_TRAMPAS_CEPO.XLSX`. Me comentó sobre el diseño y la ubicación de las trampas y lo que pasará con la cuadrícula cuando pasemos al sector 2.
- Acompañé a todo el equipo de gatos al campo, incluyendo al personal de trampeo,

  coordinadores y directora, donde Miguel Ángel Hernández, el cazador, mostró dos trampas. Esta
  muestra fue con la finalidad de enseñar a los personas sobre lo detalles a los que deben poner
  atención al momento de estar colocando o revisando una trampa. En esta demostración revisamos dos
  trampas.
- Salvador Figueroa me facilitó una tabla de datos con la cual actualicé la tabla `ESFUERZO_CAPTURAS_GATOS.XLSX`. Esta tabla tiene información diaria desde el 25 de diciembre del 2017 hasta el 6 de marzo del 2018, sin embargo la información diaria del 25 de diciembre hasta inicios de noviembre, que es cuando comenzó el trampeo para erradiciación, no está a la mano. Los personas que estaban en la estación y que trabajaron en el inicio del trampeo (noviembre-diciembre) comenzaron a incluir la información faltante.
- David Cosío y Luciana Luna me facilitaron los datos de las rutas de los perros (`Ruta perros 270218` en las extensiones `.GDB`, `.GPX` y `.TXT`); estos datos fueron recolectados durante el trabajo de búsqueda y marcaje de rastros. Me facilitaron también la ruta hecha por Miguel Ángel Hernández durante su excursión nocturna buscando gatos (`Track_MAH`, en las extensiones `.GDB`, `.GPX` Y `.TXT`).

**Observaciones:**

- Trabajé de manera muy fluída con Luciana sobre los diseños de las tablas de datos. Llegamos a acuerdos de manera rápida.

---

**Fecha:** viernes 9 de noviembre del 2018

**Localización:** Estación punta sur

**Actividades del día:**

- Hicimos un inventario del equipo de telemetría: transmisores, receptores, antenas para descarga remota de datos y para descarga de datos en la PC.
- Tuvimos una plática sobre la mejor de usar los collares con los gatos. En la plática participamos: Luciana Luna, David Cosío, Ana Cárdenas y yo.
- Revisamos el manual para verificar el uso de los dispositivos de telemetría, los dispositivos GPS y las antenas para búsqueda y recolección de datos.
- Nos trasladamos a la estación bosque. Durante el traslado hicimos el cambio de las memorias de las cámaras trampa.

**Observaciones:**

- No tenemos a la mano el cd de instalación el software necesario para programar los dispositivos de rastreo y  para descargar los datos colectados. Descargaremos el software en la noche.

---

**Fecha:** sábado 10 de marzo del 2018

**Localización:** Estación bosque

**Actividades del día:**

- Prueba del equipo de telemetría. Luciana me encargó que leyera el manual e hiciera algunas pruebas con los dispositivos de rastreo, los receptores y las antenas.
- Trabajé con la base de datos `POSICION_TRAMPAS.XLSX` para visualizar aquellas trampas en donde ha habido captura de individuos.
- Revisé, junto con Luciana Luna, el contenido de la tabla de datos `ESFUERZO_CAPTURA_GATOS.XLSX`, la cual nos facilitó Salvador Figueroa. La tabla contiene algunas inconsistencias como id de trampas que están mal.

**Observaciones:**

- Descargamos e instalamos el programa que nos permite programar los dispositivos de rastreo. Nos dimos cuenta que nos faltaba el programa que nos permite descargar los datos desde el dispositivo que los almacena, sin embargo, a diferencia del otro programa, este programa no lo encontramos en la página de la compañía que vendió el producto.
- Es mucho más fácil platicar con Luciana  y Salvador que con David Cosío acerca del diseño y contenido de las tablas de datos. Luciana atiende muy rápido mis peticiones (los datos que necesito capturar y otra información de interés); Salvador me atiende rápido, pero en ocasiones parece que no entiende el problema que estamos tratando de resolver en cada sector, lo que hace que la información que me facilita no sea la adecuada; David Cosío parece que sí entiende el problema, pero está demasiado ocupado coordinando la estación así que no es fácil encontrarlo.
