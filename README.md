---
output:
  pdf_document: default
---

Erradicación de gato feral en Isla Guadalupe
====

### Tamaño inicial de la población

1. Corremos varias veces (>30?) el modelo y guardamos las distribuciones de probabilidad posterior
1. Calculamos el cuantil 0.025 de cada distribución de probabilidad posterior y calculamos su mediana
1. Calculamos el promedio de los límites del intervalo del 1% más alto de cada distribución de probabilidad posterior (HPD) y calculamos su mediana
1. Usamos el máximo de las dos medianas anteriores para reportarlo como (la cota inferior del) tamaño inicial de la población (No).
1. Restamos a No el total de capturas acumuladas para calcular (la cota inferir de) la cantidad de gatos remanentes Ni

\subsection*{Entrega a donantes: fecha tentativa en marzo del 2019}
\section*{Fecha de entrega Análisis Científico: no hay acuerdo}

\noindent\rule{15cm}{0.4pt}

\setlength{\parindent}{10ex} $\checkmark$ Ya se entregó \hspace{2cm} $\times$ No se hará \hspace{2cm} $\square$ Pendiente

\subsection{Resultados esperados}

\begin{itemize}
    \item \textbf{Biología/ecología de datos} \newline
    \textit{Se calcularán los intervalos de confianza (IC) de los parámetros morfométricos de los gatos mediante un diseño estratificado para diferentes zonas de la islas, así como para diferentes temporadas del año. Se declarará completo el análisis morfométrico cuando se obtenga un márgen de error porcentual menor a 10\%.}
        \begin{itemize}
            \item[$\checkmark$] Análisis exploratorio de datos de morfometría de gatos
                \begin{itemize}
                    \item Los datos que estamos usando se encuentran en el archivo `control-de-gato-IG-2005-2017-rev-JH-070218.xlsx` \newline
                \end{itemize}
            \item[$\square$] Gráfica con información del sexo de los individuos capturados
        \end{itemize}
\end{itemize}

\begin{itemize}
    \item \textbf{Ámbito hogareño (5-8 collares GPS)} \newline
    \textit{Se conocerá el esfuerzo de trampeo necesario por unidad de área (el espacio entre trampas)}
        \begin{itemize}
            \item[$\square$] Mapas de densidad kernel utilizando datos de collares GPS (aún no colocados). 
                \begin{itemize}
                    \item Ya existen datos de un collar; se esperan datos de un segundo collar.
                    \item Se utilizarán datos con una resolución temporal baja (intervalos de tiempo largos entre datos) para determinar el rango de distribución.
                \end{itemize}
        \end{itemize}
\end{itemize}

\begin{itemize}
    \item \textbf{Densidad poblacional / Distribución espacial: Trampas-cámara y monitoreo nocturno} \newline
    \textit{Se calculará el tamaño inicial de la población de gatos}
        \begin{itemize}
            \item[$\square$]  Densidad sin identificar individuos (\href{http://dx.doi.org/10.1111/j.1365-2664.2008.01473.x}{doi: 10.1111/j.1365-2664.2008.01473.x})
                \begin{itemize}
                    \item Se utilizarán datos de collares GPS con una resolución temporal alta (intervalos de tiempo cortos entre datos; aún no se colocan los collares) para determinar la distancia recorrida en un día por un gato.
                    \item Datos sintéticos de trampas-cámaras (los reales están pendientes).
                        \begin{itemize}
                            \item Parámetros de trampas-cámara
                        \end{itemize}
                    \item Parámetros para estimar densidad
                \end{itemize}
            \item[$\square$] Perfil de avistamientos a partir de datos de monitoreo nocturno.
                \begin{itemize}
                    \item Ana Cárdenas y David Cosío tienen datos de monitoreos nocturnos. \newline
                \end{itemize}
        \end{itemize}
\end{itemize}

\begin{itemize}
    \item \textbf{Éxito de captura por unidad de esfuerzo} \newline
    \textit{Para determinar cuándo el esfuerzo se vuelve mayor que el éxito de captura. Esto significa que el método de captura se vuelve más caro y por lo tanto se debe cambiar de método.}
        \begin{itemize}
            \item[$\square$] Estimación del tamaño de población de cabras en la zona 1 (y tal vez en la 2).
                \begin{itemize}
                    \item Datos sintéticos de costos de monitoreo
                \end{itemize}
        \end{itemize}
\end{itemize}

\begin{itemize}
    \item \textbf{Rapid Eradication Assessment (REA)} \newline
    \textit{Monitoreo post-erradicación para confirmar la ausencia de gatos}
        \begin{itemize}
            \item[$\square$] Artículo de Ara (\href{http://onlinelibrary.wiley.com/doi/10.1111/1365-2664.12753/abstract}{doi: 10.1111/1365-2664.12753}) \newline
        \end{itemize}
\end{itemize}

----

\subsection{Descripción del proyecto}

\subsubsection{¿Cuál es el objetivo general del proyecto?}
Conservar las especies de aves marinas en Isla Guadalupe a través de la erradicación del gato feral en la isla.


\subsubsection{¿Cuáles son los objetivos específicos?}
\begin{enumerate}
    \item Disminuir el tamaño de la población del gato feral en Isla Guadalupe al 1% de su tamaño inicial.
    \item Erradicar la población de gato feral en la isla.
    \item Aumentar el porcentaje de confianza (de 0\% a 90-95\%) de la erradicación de la población de gato feral en la isla.
\end{enumerate}


\subsubsection{¿Cuáles son los indicadores de cada objetivo específico?}
\begin{enumerate}
    \item \ 
        \begin{itemize}
            \item Cantidad de gatos capturados por temporada de cacería. 
            \item Diferencia en la densidad de población de gatos entre temporadas de cacería.
            \item Cantidad de noches-trampa (esfuerzo de monitoreo) con ausencia de gatos.
        \end{itemize}
    \item \ 
        \begin{itemize}
            \item Cantidad de días sin captura de gatos.
        \end{itemize}
\end{enumerate}


\subsubsection{¿Cuál es el estado actual de este respositorio?}
En el pizarrón \href{https://trello.com/b/TG23qRK2/}{\textbf{I. Gpe. (LL)}} de Trello se encuentran los reportes más recientes de este proyecto.


\subsubsection{¿Cuál es la siguiente actividad más pequeña posible?}

\begin{itemize}
	\item Crear gráfica de las capturas acumuladas en función del esfuerzo acumulado
	\item Crear gráfica de las capturas vs tiempo
	\item Incluir gráfica de blancos acumulados en función de las horas de vuelo acumuladas en reporte \texttt{cabras-guadalupe.pdf} de la tarjeta \textbf{\href{https://trello.com/c/K5dcSd7A/}{Erradación de cabras}} en Trello.
\end{itemize}


\subsubsection{¿En qué orden se esperan los resultados?}

Debido a la disponibilidad de datos, los resultados se esperan en el siguiente
orden:

\begin{enumerate}
    \item Estimación del tamaño de población de cabras
        \begin{itemize}
            \item Método de Ricker, descrito en Krebs (1999)
            \item Ajustar modelo con datos de cabras en Isla Guadalupe (Efren)
        \end{itemize}

 \item Biología/ecología de datos de gatos
    \begin{itemize}
      \item Morfometría
      \item Se podrían utilizar datos de ratones en Espíritu Santo e islas Marías
    \end{itemize}
  
  \item Monitoreo nocturno de gatos
    \begin{itemize}
      \item Perfil de avistamientos
      \item Se podrían utilizar datos de gorriones en San Benito
    \end{itemize}
  
  \item Densidad sin identificar poblacional
    \begin{itemize}
      \item Tamaño inicial de la población de gatos (densidad sin indentificar individuos)
      \item Se podrían utilizar datos de trampas-cámara para fauna nativa en Espíritu Santo 
    \end{itemize}

  \item Ámbito hogareño
        \begin{itemize}
        \item Mapas de densidad kernel
  \end{itemize}

  \item Éxito de captura por unidad de esfuerzo
    \begin{itemize}
      \item Método de erradicación de gatos en Isla San Nicolás (método de Ramsey)
    \end{itemize}

  \item Rapid Eradication Assessment (REA) \newline
    \begin{itemize}
        \item Método de Ramsey
    \end{itemize}

\end{enumerate}

----

## Información general:

Para realizar la erradicación de gato feral la isla se dividirá en ocho sectores. Los sectores que sean adyacentes no serán excluyentes entre sí (e.g. el final del sector uno estará traslapado con el inicio del sector dos; el final del sector dos estará traslapado con el inicio del sector tres). Una nota importante es que las tres fases de erradicación sucederán en cada sector, por lo que podríamos pensar que haremos ocho erradicaciones independientes.

1. Colecta de datos.

- Para poder realizar la estadística bayesiana necesitaremos datos de esfuerzo y posición de las trampas.
- ¿Qué datos debemos tener para poder contestar las preguntas de la sección dos? Para esto es necesario comenzar a trabajar con datos sintéticos, al mismo tiempo que nos estemos comunicando con los coordinadores, para poder llegar a esta repuesta.

2. Resultados esperados.

### El analista deberá contestar tres preguntas en tiempo real.

- Hay un esfuerzo dado y hemos limpiado cierta cantidad de área, si mantenemos el mismo esfuerzo, ¿en cuánto tiempo terminaremos de limpiar el área completa? Esta pregunta está relacionada con la gráfica de capturas acumuladas vs esfuerzo acumulado.
- Si queremos reducir el tiempo en que limpiaremos el área completa, ¿cómo debo aumentar el esfuerzo?
- ¿Dónde falta esfuerzo? Para contestar esta pregunta el analista deberá verificar un subconjunto de las trampas dispuestas en el campo (¿cuál es la menor cantidad de trampas que se deben verificar para asegurar que los datos son correctos?).

### Preguntas para el final de la fase 2.

- Debemos realizar una prueba en donde pasemos de la fase 2 a la fase 3. Para esto es necesario trabajar con datos sintéticos (quizás se pueda trabajar con los datos de erradicación de gatos en Socorro).

3. Relación con coordinadores.

- El analista deberá poner atención en actuar al servicio de los coordinadores y hacerlos ver bien frente a sus colaboradores.
- El analista deberá verificar que, una vez él abandone la isla, los coordinadores se hagan cargo de la verificación de la toma correcta de datos. El analista supervisará que los coordinadores comprendan la metodología de la toma de datos.

## Notas finales.

- Disponemos de 12 cámaras y horas-hombre para poder realizar un diseño de experimento en Cedros. Dividiremos la zona en 3 sectores y pondremos 4 cámaras en cada sector de manera aleatoria.
- Falta discutir cómo será el seguimiento del experimento.
- Realizaremos una simulación computacional usando catbots.
	- Pondremos determinada cantidad de catbots de manera aleatoria sobre un dominio definido.
	- Los catbots tendrán un movimiento browniano (aunque preferimos que se muevan de manera determinística).
	- Colocaremos dospositivos de detección de catbots.
	- Calcularemos la densidad de catbots usando los dispositivos de detección.
	- Compararemos la densidad caculada con la densidad real.

\newpage

# Contenido del directorio
La carpeta que contiene este archivo que estás leyendo además contiene
los siguientes archivos:

Archivo                               | Descripción                            |
--------------------------------------|----------------------------------------|
`cronograma.gan`                      |Archivo que contiene el cronograma de las entregas y del plan de trabajo.|
`Makefile`                            |Archivo con el cual se generan automáticamente los reportes que se encuentren dentro de la carpeta `entrega` y el contenido de la carpeta `resultados`.|

El resto de los archivos se encuentran distribuidos en subcarpetas.

## Lista de archivos en cada carpeta

### entrega

Archivo                           | Descripción                               |
----------------------------------|-------------------------------------------|
`albatrosSinGatos.tex`            | Reporte donde se proyecta el éxito reproductivo del albatros de Laysan en Isla Guadalupe esperado en el 2021 tras un proyecto de 4 años para la erradicación de gatos. |
`cabras-guadalupe.tex`            | Este reporte actualmente hace una revisión de los datos de cabras en Isla Guadalupe del 2004-2005 (del archivo `erradicacion-de-cabras-guadalupe.csv`). Se utilizarán estos datos para ajustar algún modelo a la gráfica de blancos acumulados en función de las horas de vuelo acumuladas. |
`camaras-trampa.tex`              | Fuente para generar la presentación del artículo de trampas-cámara de Rowcliffe _et al._ |
`camaras-trampa_diapositivas.tex` | Diapositivas de la presentación del artículo de trampas-cámara de Rowcliffe _et al._     |
`estilo_referencias.bst`          | Es el archivo que defiene el `estilo_referencias` con las que se generan las referencias. |
`estimacion_poblacion_inicial.tex`| Es el archivo fuente que genera el reporte de la introducción del método de Ramsey.|
`referencias.bib`                 | Es el archivo con la información para generar las referencias utilizado por los archivos `tex`.|
`presentacion\metodo_ramsey.tex`  | Es el archivo fuente que genera la presentación del método de Ramsey.|
`presentacion\metodo_ramsey_txt.tex`| Es el archivo fuente de las diapositivas.|

\newpage
### inst/extdata
Archivo                           | Descripción                                      |
----------------------------------|--------------------------------------------------|
`datapackage.json`                 | Archivo que contiene los metadatos de `erradicacion_cabras_guadalupe.csv`|
`erradicacion_cabras_guadalupe.csv`| Archivo con los datos de cabras retiradas en Isla Guadalupe en el 2004 y 2005.|

### MATLAB/demostraciones
Archivo              | Descripción                                                            |
---------------------|------------------------------------------------------------------------|
`graficaN.m`         | Programa que genera los resultados del reporte `albatrosSinGatos.pdf`. |

### MATLAB/funciones
Archivo              | Descripción                                                            |
---------------------|------------------------------------------------------------------------|
`estimateN.m`        | Función que calcula algún elemento de una ecuación diferencial (no estoy segura cuál elemento). Se usa en el programa `graficaN.m`. |
`estimateR.m`        | Función que calcula algún elemento de una ecuación diferencial (no estoy segura cuál elemento). Creo que se iba a usar esta función en el programa `graficaN.m` pero no aparece en él. |

### python
Archivo                               | Descripción                            |
--------------------------------------|----------------------------------------|
`bayes.py`                            | Programa que calcula la distribución de probabilidad de la probabildad de captura. |

### python/clases
Archivo                               | Descripción                            |
--------------------------------------|----------------------------------------|
`clases\Captura.py`                   |                                        |

### python/tests
Archivo                               | Descripción                            |
--------------------------------------|----------------------------------------|
`tests\test_unidad-pruebas.py`        |                                        |

\newpage
### referencias
| Archivo                                             | Descripción                                               |
|-----------------------------------------------------|-----------------------------------------------------------|
| `Ecological_Methodology_Second_Edition.pdf`         | Libro que explica la estimación del tamaño de una población mediante una regresión lineal (tema 3.1.4). |
| `RamseySan NicCats.pdf`                             | Artículo de la erradicación de gatos en Isla San Nicolás. |
| `Rowcliffe_et_al-2008-Journal_of_Applied_Ecology_EniarEvaristo.pdf` |                                        |
|                                                     | Artículo de la estimación de densidad de una población sin identificación de individuos con cámaras trampa. |
