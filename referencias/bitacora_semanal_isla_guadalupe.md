Proyecto de erradicación de gato feral en Isla Guadalupe
------

#### David Martínez
##### Dirección de Análisis Científico

---

#### Reporte semanal del 06 al 10 de marzo del 2018

**¿Cuál fue el aprendizaje más valioso o útil de la semana?**

- Aprendí sobre el uso de los instrumentos de telemetría.

**¿Qué resultados obtuve durante la semana?**

- Recibí y acomodé en una tabla los datos de capturas obtenidos de las cámaras trampa. Estos datos aún les falta cierto tratamiento, como separar por fecha y hora cada captura obtenida.
- Obtuve la visualización de la posición de las trampas cepo y las trampas donde ha habido captura de individuos.
- Recibí y acomodé los datos, aunque todavía están incompletos, del esfuerzo y capturas actualizado de forma diaria.
- Después de platicar un par de ocasiones con Luciana Luna sobre la tabla `POSICION_TRAMPAS_CEPO.XLSX`, terminamos con un diseño que les ayudará a los tramperos a tener cierto control sobre la información diaria de las trampas y nos permitirá a nosotros hacer el procesamiento. 

**¿Con quién trabajé y cómo fue el trato?**

- Trabajé con Salvador Figueroa y Luciana Luna con los datos de las cámaras trampa. El trabajo fue de forma separada. Por un lado, Salvador me entrego una tabla de datos que contiene la fecha de revisión de la cámara y las capturas realizadas; por otro lado, platiqué con Luciana sobre la manera en que se estarán contabilizando las capturas (esto ya lo había hablado con Salvador y David Cosío).
- Trabajé con Luciana Luna con los datos del archivo `ESFUERZO_CAPTURAS_GATOS.XLSX`. Una vez que Salvador nos facilitó la tabla de datos más actualizada Luciana y yo comenzamos a revisarla. En la revisión encontramos algunas inconsistencias con la nomenclatura de las trampas, detectando más de 30 capturas que no podemos relacionarla con alguna trampa directamente. Salvador está trabajando en corregir las nomenclaturas.
- Trabajé con Luciana revisando la información de la tabla `POSICION_TRAMPAS_CEPO.XLSX`. Revisamos el diseño de la tabla de datos y luego le mostré la visualización de las trampas en el mapa. Más adelante pudimos ver la posición de algunas trampas en donde han ocurrido capturas.

**¿Cuáles serán mis actividades de los próximos días?**

- Trabajaré con David Nájera y Carlos Tafoya para acordar el seguimiento de la actualización de los datos dentro de los archivos. David Nájera se quedará a cargo del equipo de tramperos y acordaré con él delegar a Carlos Tafoya la función de actualizar las tablas de datos.
- Trabajaré con Salvador, David Nájera y Carlos Tafoya para terminar la corrección de la nomenclatura de las trampas y dejar listo el archivo `POSICION_TRAMPAS_CEPO.XLSX`.
- Trabajaré con Salvador, David Nájera y Carlos Tafoya para terminar de capturar los datos que estarán en el archivo `ESFUERZO_CAPTURAS_GATOS.XLSX`.
- Trabajaré con Salvador, David Nájera y Carlos Tafoya en el desglose de la información de las cámaras trampa que irá dentro del archivo `REGISTRO_CAMARAS_TRAMPA.XLSX`.
- Trabajaré junto con David Cosío, David Nájera y algunos tramperos más en una práctica para la toma de datos de los transectos nocturnos para avistamiento de gatos.

**¿Qué pude haber hecho diferente en mis actividades de la semana?**

- Aunque Ana Cárdenas llegó con Luciana Luna, no me he enterado correctamente sobre su función en el proyecto. Pude haberla incluído en las actividades sobre la toma de datos para que estuviera enterada al respecto.

---

#### Reporte semanal del 24 de febrero al 05 de marzo del 2018

**¿Cuáles fueron mis actividades de la semana?**

Sábado:

- Acompañé a David Nájera a revisar un transecto de trampas.

Domingo:

- Me trasladé a la estación bosque para recoger ropa para regresar a la estación punta sur.

Lunes:

- Me trasladé a la estación punta sur con el equipo canino.

Martes:

- Añadí metadatos a las bases de datos creadas.
- Creé el programa `tamano_restante_poblacion.py` para realizar el procesamiento de la base de datos `ESFUERZO_CAPTURA_GATOS.XLSX`. El programa obtendrálas variables de esfuerzo acumulado y capturas acumuladas. Con estas últimas dos variables obtendré el tamaño de la población para obtener, enseguida, la cantidad de individuos restantes para alcanzar el 90% de la población.
- Platiqué con David Cosío y Salvador Figueroa sobre la base de datos `ESFUERZO_CAPTURA_GATOS.XLSX`. A partir de la plática concluimos que se modificará la base de datos, de manera que el encargado de llenarla estará capturando diariamente la fecha del día, la cantidad de trampas activas, la cantidad de inviduos capturados, los identificadores de las trampas donde fueron capturados los gatos y las observaciones pertinentes, quedando de la siguiente manera:

| fecha de revision	| cant. de trampas activas | individuos capturados | ID de trampas | observaciones |
|-------------------|----------|----------|--------------------------------|-------------|
2018-02-21T00:00:00	| 145 | 1 | [TC-01-129-AG] |  El individuo ... | 		
2018-02-22T00:00:00	| 145 | 1 | [TC-01-080-DN] | | 		
2018-02-23T00:00:00	| 155 | 0 | | La trampa ... | 		
2018-02-24T00:00:00	| 165 | 2 | TC-01-055-SF,TC-01-037-SF] | |		
2018-02-25T00:00:00	| 175 | 0 | | |

Miércoles:

- Inicié con el estudio de la morfometría de gatos. Descargué la base de datos durante la noche y realicé una copia de la base de datos para poder hacer modificaciones, dejando la base de datos original intacta. Las modificaciones fueron necesarias ya que la base de datos contenía encabezados y cálculos que impedían el procesamiento.
- Creé un programa de extensión `.R` para realizar el procesamiento. La idea de esto fue exportar las gráficas y tablas para importarlas en un `.tex`.
- Creé un reporte vació, el cual contendrá los resultados obtenidos de la base de datos de morfometría de gatos.

Jueves:

- Calculé la estadística descriptiva del peso de los gatos. No hice ninguna distinción por categoría ni por zonas de la isla.
- Trabajé en la creación de una malla que simula las posiciones de las trampas, ya que la cuadrícula con las posiciones donde se colocarán las trampas no está a la mano; David Cosío pidió la cuadrícula a Luciana el jueves 22 de febrero sin embargo, hasta la fecha, Luciana no la ha mandado. Me di cuenta que, aunque esta cuadrícula exista, este problema será recurrente, ya que no están haciendo el diseño de la posición de las trampas con anticipación. En este momento los puntos donde serán colocadas las trampas los está creando Carlos Tafoya en ArcGIS pero, ¿qué pasará cuando no esté Carlos? Debemos trabajar en conjunto con Ana Cárdenas para involucrarnos en este diseño; debemos prevenirnos para el trabajo en el sector 2.
- Actualicé los paquetes en `R` para poder crear un `Rmd`.

Viernes:

- Excursión de reconocimiento a el islote morro prieto. Acompañé a Ángel Méndez al morro prieto para reconocimiento del terreno. Apoyé en la verificación del estado de los nidos y pollos de albatros y en la búsqueda de madrigueras.

Sábado:

- Creé el programa `morfometría_gatos_isla_guadalupe.Rmd` donde obtuve la estadística descriptiva de las variables numéricas de la morfometría de gatos. Por el momento no separé las variables por categorías ni por sitios en la isla.
- Trabajé en conjunto con David Cosío y Salvador Figueroa para corregir la nomenclatura designada para cada trampa. Supervisé que el nombre de las trampas quedara como habíamos acordado, quedando de la siguiente manera: `TT-XX-YYY-AA`, donde: TT es el tipo de trampa; `XX` es el sector que se está trabajando; `YYY` es el número de la trampa (que irá de 1-40 para el primer trampero, del 41-80 para el segundo trampero, del 81-120 para el tercer trampero, y así sucesivamente); y `AA` son las iniciales del trampero. Pretendo que esta nomenclatura no cambie, con la finalidad de poder hacer validaciones.
- Exporté desde matlab una malla en `kml`. Carlos Tafoya importó esta malla en ArcGIS para acomodar los puntos tomando en cuenta las trampas ya colocadas. Esta malla tiene una resolución de 200 $\times$ 200 metros.

Domingo:

- Excursión con la unidad canina. Acompañé a la unidad canina para conocer el trabajo de rastreo y marcaje.
- Me trasladé a la estación bosque.

Lunes:

- Limpieza de la estación. Aunque el domingo 4 de marzo fue día de limpieza en la estación, también el lunes se hizo limpieza ya que el martes 6 llegan Julio Montoya y Luciana Luna. A mí me tocó el almacén donde limpié y acomodé unas cajas de comida y unas hieleras.
- Trabajé en el reporte del análisis exploratorio de datos de la morfometría de gatos. Creé el resumen del reporte y coloqué el encabezado de las tablas y los pies de las figuras.

**¿Qué resultados obtuve?**

- Conocí el terreno donde se están colocando las trampas, dándome cuenta que es muy abrupto. Conocí la manera en que realizan la revisión de las trampas una vez colocadas. La idea de revisar trampas de manera aleatoria o sistemática queda descartada ya que es imposible recorrer todo el terreno trabajado para verificar el desempeño de los tramperos; tendremos que buscar una forma más eficiente para hacer esa verificación.
- Avancé en el diseño de la base de datos que contendrá el esfuerzo y captura de gatos y la base de datos que contendrá la localización de las trampas colocadas. Añadí metadatos a las bases de datos. Comencé a pensar qué tan conveniente sería hacer un TDP para estas bases de datos.
- Creé un archivo `Rmd` para realizar el estudio de la morfometría de gatos.
- Hice una malla cuadriculada que intenta ayudar al diseño de la posición de las trampas en el sector 1. Este trabajo fue necesario ya según la cuadrícula existe pero no está a la mano (no la han envidado desde Ensenada).
- Conocí el terreno en el morro prieto dándome cuenta, de esta manera, de la necesidad de realizar muestreos en lugar de búsquedas exahustivas.
- Hice un análisis exploratorio de datos para las variables numéricas del archivo que contiene la morfometría de gatos.
- Conocí el trabajo de la unidad canina.
- Trabajé en el reporte que contiene los resultados de la estadística descriptiva de la morfometría de gatos.

**¿Con quién trabajé y cómo fue el trato?**

- Trabajé con Salvador Figueroa y David Cosío dándo seguimiento a las bases de datos diseñadas y arreglando el nombre de las trampas. Trabajé con Salvador Figueroa y Carlos Tafoya en el diseño de la localización de las trampas.
- Mi trato con los tres fue eficiente. Salvador estuvo disponible siempre para el trabajo con las bases de datos. Carlos Tafoya entiende sobre datos georeferenciados y que él trabaje con ArcGIS resultó ser una ventaja, en este caso, ya que pude esquivar ese trabajo improvisado que, de no estar él, me habría tocado a mí. Aunque David Cosío tiene la visión general del proyecto y en particular del trampeo de gatos, no siempre está disponible debido a su rol de coordinador de la estación y su trabajo con la unidad canina. Aunque Salvador es el encargado del personal que está trabajando en el sector 1, David Cosío se comunica con David Nájera para recibir noticias y dar información sobre el trabajo.

**¿Cuáles serán mis actividades para los próximos días?**

- Terminaré el reporte que contiene el análisis exploratorio de datos de la morfometría de gatos, el cual se genera a partir del archivo `morfometria_gatos_isla_guadalupe.Rmd`.
- Revisaré los datos ya capturados que estarán dentro del archivo `ESFUERZO_CAPTURA_GATOS.XLSX`.
- Acomodaré los datos de localización de trampas en el archivo `POSICION_TRAMPAS_CEPO.XLSX`.
- Iniciaré el procesamiento de los datos del archivo `ESFUERZO_CAPTURA_GATOS.XLSX` para obtener esfuerzo acumulado y capturas acumuladas y crearé las gráficas correspondientes para visualizar los resultados.
- Platicaré con David Cosío acerca de los datos que estarán contenidos en el archivo `REGISTRO_CAMARAS_TRAMPA.XLSX` (este archivo existe en el canal de datos aunque está vacío).
- Es posible que realicemos un transecto nocturno el 10 de marzo

**¿Qué pude haber hecho diferente en mis actividades de la semana?**

- Pude haber subido al directorio de datos en drive los archivos `ESFUERZO_CAPTURA_GATOS.XLSX` y `POSICION_TRAMPAS_CEPO.XLSX` justo al momento de deseñarlas. Me di cuenta, durante la semana, que mis compañeros en Ensenada dedicaron tiempo para crear bases de datos a partir de los bosquejos que están en las bitácoras, siendo que yo ya tenía los archivos `.xlsx` creados.
- Debí haber estado (debo estar) solicitando el apoyo de David Cosío y Salvador Figueroa para obtener los datos que ya están capturados. Aunque la comunicación es buena y el trabajo ha sido eficiente siento que la captura en las bases de datos diseñadas va lenta.

---

#### Reporte semanal del 19 - 23 de febrero del 2018

**¿Cuáles fueron las actividades de la semana?**

Lunes:

- Atendí una reunión informativa acerca de las actividades generales 
del campamento.
- Atendí una reunión informativa para el equipo de gatos. Durante la reunión 
David Cosío mencionó que las cosas que yo trabajaré en mi estancia son: morfometría de gatos, transectos nocturnos y rutas y marcaje de perros.
- Me instalé en la oficina y verifiqué que la computadora estuviera 
funcionando en óptimas condiciones.

Martes:

- Atendí un taller para el manejo de gatos (colocación de gps's), 
sacrificio de gatos y uso de trampas cepo. Para el manejo y sacrifico 
de gatos aprendimos, principalmente, las medidas de las dosis y 
administración de fármacos.
- Caminata de reconocimiento hacia la parte oeste del campamento, cruzando
el bosque joven de ciprés.

Miércoles:

- Trabajé en el diseño de una base de datos para el monitoreo de trampas, que 
incluye la captura de gatos, y una base de datos que contendrá la localización
de las trampas cepo colocadas.

`DISPOSICION_TRAMPAS_CEPO.XLSX`:

| fecha | ID de trampa | longitud | latitud | 
|-------|--------------|----------|---------| 
| 2018-02-21T16:46:00 | TC01001DN | 123 | 456 | 
| 2018-02-21T16:46:01 | TC01002DN | 123 | 456 | 
| 2018-02-21T16:46:02 | TC01003DN | 123 | 456 | 
| 2018-02-21T16:46:03 | TC01004DN | 123 | 456 | 
| 2018-02-21T16:46:04 | TC01005DN | 123 | 456 | 
| 2018-02-21T16:46:05 | TC01006DN | 123 | 456 | 

`ESFUERZO_CAPTURA_GATOS.XSLX`:

| fecha de revision | ID del trampero | ID de trampa | condicion | captura |
|-------------------|-----------------|--------------|-----------|---------|
| 2018-02-21T16:12:00 | DN | TC01001DN | activa | 0 | 
| 2018-02-21T16:12:01 | DN | TC01002DN | activa | 0 | 
| 2018-02-21T16:12:02 | DN | TC01003DN | activa | 0 | 
| 2018-02-21T16:12:03 | DN | TC01004DN | activa | 0 | 
| 2018-02-21T16:12:04 | DN | TC01005DN | activa | 1 | 
| 2018-02-22T12:00:00 | JS | TC01006DN | activa | 0 | 
| 2018-02-22T12:00:01 | JS | TC01007DN | activa | 0 | 
| 2018-02-22T12:00:02 | JS | TC01008DN | activa | 1 | 
| 2018-02-22T12:00:03 | JS | TC01009DN | activa | 1 | 
| 2018-02-22T12:00:04 | JS | TC01010DN | activa | 0 | 

Jueves:

- Atendí una práctica de colocación de trampas en el bosque al lado de la 
estación.
- Apoyé en la configuración de los collares de rastreo de los perros y 
platiqué con David Cosío y Mauricio Canales sobre la información que se 
obtiene de los collares.
- Añadí datos sintéticos a las bases de datos diseñadas.
- Atendí una reunión informativa sobre la colocación y el monitoreo de 
trampas y el trabajo con los perros.

Viernes:

- Me trasladé a punta sur para llevar gente y provisiones.

**¿Qué resultados obtuve?**

- Aprendí sobre el funcionamiento general del campamento.
- Aprendí sobre el manejo de las trampas cepo en el campo.
- Aprendí sobre el manejo de los fármacos para el sacrifico de los gatos.
- Me enteré que, aparte de los datos que estaré procesando, quieren que trabaje con morfometría de gatos, transectos nocturnos, cámaras trampa y rutas y marcaje de perros.
- Inicié con el diseño de dos bases de datos, una de ellas es para incorporar la información de la colocación de las trampas cepo; la otra es para el monitoreo de trampas e incorporar las capturas de gatos.

**¿Con quién trabajé y cómo fue el trato?**

- Para el diseño de las bases de datos aproveché la llegada de Salvador Figueroa a la estación bosque para que me ayudara a conocer los datos que están tomando en el campo; eventualmente David Cosío se unió a la discusión y concluímos, entre los tres, en las dos bases de datos arriba mencionadas; también participaron en la discusión, de manera secundaria, dos personas (David Nájera y Antonio Gorriño), que estuvieron trabajando en la temporada pasada, quienes colocaron las trampas que actualmente se están monitoreando.
- El trato con los cuatro fue bueno y eficiente. David Cosío y Salvador Figueroa tienen una visión general del trabajo, mientras que David Nájera y Antonio Gorriño tienen una visión particular del trabajo. De esta manera pudimos discutir sobre el formato general de las bases de datos y sobre el formato del identificador de las trampas cepo.

**¿Cuáles serán mis actividades para la próxima semana?**

- Mañana sábado acompañaré a una persona en la revisión de las trampas cepos ya dispuestas con la finalidad de conocer el terreno y la manera en que registran los datos.
- Revisaré, con Salvador Figueroa o David Cosío, las bases de datos que ya existen sobre los monitoreos de trampas cepo, con la finalidad de comenzar a incorporar los datos en las bases de datos que he diseñado.
- Platicaré con Salvador Figueroa y David Cosío sobre los transectos nocturnos con la finalidad de diseñar una base de datos para ese monitoreo. Los acompañaré en el transecto nocturno, si acaso realizan alguno en la semana.
- Comenzaré a procesar los datos de morfometría de gatos.

**¿Qué habría hecho diferente sobre mis actividades de la semana?**

- Aparte de platicar con David Cosío y Salvador Figueroa, me habría apoyado más en las personas que ya han trabajado en la colocación de trampas haciendo preguntas sobre el trabajo que hacen y los datos que capturan.

---

