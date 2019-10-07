# La ecritura del README.pdf, albatrosSinGatos.pdf y albatrosSinGatos.docx
all: README.pdf entrega/albatrosSinGatos.pdf\
	entrega/albatrosSinGatos.docx\
	entrega/cabras-guadalupe.pdf\
	entrega/estimacion_poblacion_inicial.pdf\
	entrega/presentacion/metodo_ramsey.pdf\
	entrega/camaras-trampa.pdf\
	entrega/erradicacion_gatos_socorro.html

datapackageCapturaGatosSocorro = \
	//$(COMPUTERNAME)/datos-texto/datapackage/erradicaciones-mamiferos/captura_gatos_socorro.csv

datapackageCapturaGatosGuadalupe = \
	//$(COMPUTERNAME)/datos-texto/datapackage/erradicaciones-mamiferos/captura_gatos_guadalupe.csv

# Gráficas generadas en MATLAB
figurasAlbatrosSinGatos = \
  resultados/LAAL_para_Scott.png

# Resultados del escrito: estimacion_poblacion_inicial
# El archivo `datos-objetivo.json` tiene los datos sintéticos
# Los archivos *.png son los histogramas de No y p
# Los archivos *.csv tienen la información con la que se pueden generar los histogramas
# los archivos metadatos_*.json contienen los metadatos de los archivos *.csv
resultadosEstimacionPoblacionInicial = \
	resultados\datos-objetivo.json\
	resultados\probabilidad_captura.png\
	resultados\tamagno_inicial.png\
	resultados\datos_histograma_No.csv\
	resultados\datos_histograma_q.csv\
	resultados\metadatos_histograma_q.json\
	resultados\metadatos_histograma_No.json

# Ingredientes del `estimacion_poblacion_inicial.pdf`.
# El archivo `referencias.bib` tiene la información de las referencias citadas.
# El archivo `estilo_referencias.bst` tiene el estilo de las referencias.
referenciasLatex = \
	entrega\referencias.bib\
	entrega\estilo_referencias.bst

# Ingredientes de la presentación: metodo_Ramsey
# El archivo `metodo_ramsey.tex` tiene el título de la presentación.
# El archivo `metodo_ramsey_txt.tex` tiene las diapositivas de la presentación.
texMetodoRamsey = \
	entrega\presentacion\metodo_ramsey.tex\
	entrega\presentacion\metodo_ramsey_txt.tex

# Gráficas copiadas desde la carpeta compartida de datos. Estas imágenes no se
# están generando en algún programa.
imagenesMetodoRamsey = \
	referencias/imagenes/cangrejito_playero.png

# Ingredientes de la presentación: camaras-trampa
# El archivo `camaras-trampa.tex` tiene el título de la presentación.
# El archivo `camaras-trampa_diapositivas.tex` tiene las diapositivas de la
# presentación.
texCamarasTrampa = \
	entrega\camaras-trampa.tex\
	entrega\camaras-trampa_diapositivas.tex

imagenesCamarasTrampa = \
	referencias/imagenes/figura1_rowcliffe.png \
	referencias/imagenes/figura2a_rowcliffe.png \
	referencias/imagenes/figura2b_rowcliffe.png \
	referencias/imagenes/figura3_rowcliffe.pdf \
	referencias/imagenes/figura4a_rowcliffe.pdf \
	referencias/imagenes/figura4bc_rowcliffe.pdf \
	referencias/imagenes/figura5_rowcliffe.pdf \
	referencias/imagenes/tabla1_rowcliffe.png \
	referencias/imagenes/tabla2_rowcliffe.png

# Resultados para reporte de Socorro
pngGraficasCapturaGatoSocorro = \
	resultados/accumulated-catch_accumulated-effort.png \
	resultados/accumulated-catch_time-serie.png \
	resultados/catch-per-unit-effort_accumulated-effort.png \
	resultados/catch-per-unit-effort_time-serie.png 

csvDistribucionPosteriorSocorro = \
	resultados/distribucion_posterior_socorro.csv

csvProbabilidadCapturaGatosSocorro = \
	resultados/probabilidad_captura_remanentes_socorro.csv \
	resultados/derivada_captura_esfuerzo_socorro.csv

jsonValoresReporteGatosSocorro = \
	resultados/tabla_valores_socorro.json

# Resutlados para reporte de guadalupe
pngGraficasGatosGuadalupe = \
	resultados/accumulated_catch_accumulated_effort_guadalupe.png \
	resultados/accumulated_catch_time_serie_guadalupe.png \
	resultados/catch_per_unit_effort_accumulated_effort_guadalupe.png \
	resultados/catch_per_unit_effort_time_serie_guadalupe.png 

csvDistribucionPosteriorGuadalupe = \
	resultados/distribucion_posterior_guadalupe.csv

csvProbabilidadCapturaGatosGuadalupe = \
	resultados/probabilidad_captura_remanentes_guadalupe.csv \
	resultados/derivada_captura_esfuerzo_guadalupe.csv

jsonValoresReporteGatosGuadalupe = \
	resultados/tabla_valores_guadalupe.json

# Escritura del README.ped
README.pdf: README.md
	pandoc README.md -o README.pdf
	start "" /max "README.pdf"

referencias/bitacora-diaria-isla-guadalupe.pdf: referencias/bitacora_diaria_isla_guadalupe.md
	pandoc referencias/bitacora_diaria_isla_guadalupe.md -o referencias/bitacora-diaria-isla-guadalupe.pdf 
	start "" /max "referencias\bitacora-diaria-isla-guadalupe.pdf"

referencias/bitacora-semanal-isla-guadalupe.pdf: referencias/bitacora_semanal_isla_guadalupe.md
	pandoc referencias/bitacora_semanal_isla_guadalupe.md -o referencias/bitacora-semanal-isla-guadalupe.pdf
	start "" /max "referencias\bitacora-semanal-isla-guadalupe.pdf"

# Escritura de albatrosSinGatos.pdf
entrega/albatrosSinGatos.pdf: entrega/albatrosSinGatos.tex $(figurasAlbatrosSinGatos)
	pdflatex -output-directory=entrega -include-directory=entrega entrega\albatrosSinGatos.tex
	pdflatex -output-directory=entrega -include-directory=entrega entrega\albatrosSinGatos.tex
	start "" /max "entrega\albatrosSinGatos.pdf"

# Escritura de albatrosSinGatos.docx
entrega/albatrosSinGatos.docx: entrega/albatrosSinGatos.tex $(figurasAlbatrosSinGatos)
	pandoc entrega/albatrosSinGatos.tex -o entrega/albatrosSinGatos.docx

# Escritura de cabras-guadalupe.pdf
entrega/cabras-guadalupe.pdf: entrega/cabras-guadalupe.tex
	cd entrega & del *.pythontex                            #borra dependencia pythontex
	if exist "entrega\pythontex-files-cabras-guadalupe" del /S /Q entrega\pythontex-files-cabras-guadalupe
	cd entrega & pdflatex cabras-guadalupe.tex
	cd entrega & bibtex cabras-guadalupe
	cd entrega & pythontex cabras-guadalupe.tex
	cd entrega & pdflatex cabras-guadalupe.tex
	cd entrega & pdflatex cabras-guadalupe.tex
	start "" /max "entrega\cabras-guadalupe.pdf"

# Los archivos que utiliza son las resultadosEstimacionPoblacionInicial (gráficas y
# datos-objetivo.json).
# Los archivos que utiliza son las referenciasLatex (referencias.bib y
# estilo_referencias.bst).
# Primero borra los archivos generados por pythontex para que se actualicen los
# datos.
# Corre bibtex y pythontex, genera el archivo pdf y los muestra.
entrega/estimacion_poblacion_inicial.pdf: entrega/estimacion_poblacion_inicial.tex \
		$(referenciasLatex) $(resultadosEstimacionPoblacionInicial) python/bayes.py
	cd entrega & del *.pythontex                            #borra dependencia pythontex
	if exist "entrega\pythontex-files-estimacion_poblacion_inicial" del /Q entrega\pythontex-files-estimacion_poblacion_inicial\* #borra dependencia pythontex
	cd entrega & pdflatex estimacion_poblacion_inicial.tex
	cd entrega & bibtex estimacion_poblacion_inicial
	cd entrega & pythontex estimacion_poblacion_inicial.tex
	cd entrega & pdflatex estimacion_poblacion_inicial.tex
	cd entrega & pdflatex estimacion_poblacion_inicial.tex
	start "" /max "entrega\estimacion_poblacion_inicial.pdf"

# Escritura de presentacion con nombre metodo_Ramsey.pdf
# Los archivos que utiliza son los resultadosEstimacionPoblacionInicial (gráficas y datos-objetivo.json).
# Los archivos que utiliza son los archivoPresentacion (título y las diapositivas).
# Primero borra los archivos generados por pythontex para que se actualicen los datos.
# Corre bibtex y pythontex, genera el archivo pdf y los muestra.
entrega/presentacion/metodo_ramsey.pdf: $(texMetodoRamsey) \
		$(resultadosEstimacionPoblacionInicial) $(imagenesMetodoRamsey) python/bayes.py \
		$(referenciasLatex)
	cd entrega/presentacion & del *.pythontex                            #borra dependencia pythontex
	if exist "entrega\presentacion\pythontex-files-metodo_ramsey" del /Q entrega\presentacion\pythontex-files-metodo_ramsey\* #borra dependencia pythontex
	cd entrega/presentacion & pdflatex metodo_ramsey.tex
	cd entrega/presentacion & bibtex metodo_ramsey
	cd entrega/presentacion & pythontex metodo_ramsey.tex
	cd entrega/presentacion & pdflatex metodo_ramsey.tex
	cd entrega/presentacion & pdflatex metodo_ramsey.tex
	start "" /max "entrega\presentacion\metodo_ramsey.pdf"

# Escritura de la presentación del artículo de cámaras trmapa sin identificación de individuos
entrega/camaras-trampa.pdf: $(texCamarasTrampa) $(imagenesCamarasTrampa) $(referenciasLatex)
	cd entrega & pdflatex camaras-trampa.tex
	cd entrega & bibtex camaras-trampa
	cd entrega & pdflatex camaras-trampa.tex
	cd entrega & pdflatex camaras-trampa.tex
	start "" /max "entrega\camaras-trampa.pdf"

entrega/erradicacion_gatos_socorro.html: python/generaReporteErradicacionGatosSocorro.py python/gatos/bokeh_plots.py $(jsonValoresReporteGatosSocorro)
	if not exist "entrega" mkdir entrega
	python python/generaReporteErradicacionGatosSocorro.py -r $(datapackageCapturaGatosSocorro) -ippd $(csvDistribucionPosteriorSocorro) -posf $(csvProbabilidadCapturaGatosSocorro) -rv $(jsonValoresReporteGatosSocorro) -o $(@) --espaniol
	start "" /max "$(@)"

entrega/erradicacion_gatos_guadalupe.pdf: entrega/erradicacion_gatos_guadalupe.html entrega/erradicacion_gatos_guadalupe.tex
	cd entrega & pdflatex erradicacion_gatos_guadalupe.tex
	cd entrega && pythontex erradicacion_gatos_guadalupe.tex
	cd entrega & pdflatex erradicacion_gatos_guadalupe.tex
	start "" /max "$(@)"

entrega/erradicacion_gatos_guadalupe.html: python/generaReporteErradicacionGatosSocorro.py python/gatos/bokeh_plots.py $(jsonValoresReporteGatosGuadalupe)
	if not exist "entrega" mkdir entrega
	python python/generaReporteErradicacionGatosSocorro.py -r $(datapackageCapturaGatosGuadalupe) -ippd $(csvDistribucionPosteriorGuadalupe) -posf $(csvProbabilidadCapturaGatosGuadalupe) -rv $(jsonValoresReporteGatosGuadalupe) -o $(@)
	start "" /max "$(@)"
 
# Generación de las figuras para albatrosSinGatos.pdf
$(figurasAlbatrosSinGatos): MATLAB/demostraciones/graficaN.m
	if not exist "$(subst /,\,$(@D))" mkdir $(subst /,\,$(@D))
	runMatlab "MATLAB\demostraciones\graficaN.m"

# Escritura de estimacion_poblacion_inicial.pdf
# Generación de las figuras para estimacion_poblacion_inicial.pdf
# Generación de los datos y los metadatos que generan esas figuras
# Y los datos sintéticos que se utilizan para generar esas figuras.
$(resultadosEstimacionPoblacionInicial): python\bayes.py
	if not exist "$(subst /,\,$(@D))" mkdir $(subst /,\,$(@D))
	python "python\bayes.py"

# Copia la imagen de cangrejito playero.
$(imagenesMetodoRamsey):
	if not exist "$(subst /,\,$(@D))" mkdir $(subst /,\,$(@D))
	copy \\%COMPUTERNAME%\Datos\$(@F) referencias\imagenes\

# Copia las imágenes del reporte de Rowcliffe et al. sobre trampas-cámara
$(imagenesCamarasTrampa):
	if not exist "$(subst /,\,$(@D))" mkdir $(subst /,\,$(@D))
	copy \\%COMPUTERNAME%\Datos\$(@F) referencias\imagenes\

# Objetivos para generar resultados de Socorro
$(pngGraficasCapturaGatoSocorro): python/generaGraficasCapturaGatoSocorro.py
	if not exist "$(subst /,\,$(@D))" mkdir $(subst /,\,$(@D))
	python python/generaGraficasCapturaGatoSocorro.py

$(csvDistribucionPosteriorSocorro): python/generaTamanioPoblacionGatos.py $(datapackageCapturaGatosSocorro)
	if not exist "$(subst /,\,$(@D))" mkdir $(subst /,\,$(@D))
	python python/generaTamanioPoblacionGatos.py -r $(datapackageCapturaGatosSocorro) -o $(@)

$(csvProbabilidadCapturaGatosSocorro): python/generaProbabilidadAtraparGatosRemanentes.py $(csvDistribucionPosteriorSocorro)
	if not exist "$(subst /,\,$(@D))" mkdir $(subst /,\,$(@D))
	python python/generaProbabilidadAtraparGatosRemanentes.py -r $(datapackageCapturaGatosSocorro) -ippd $(csvDistribucionPosteriorSocorro) -o $(csvProbabilidadCapturaGatosSocorro)

$(jsonValoresReporteGatosSocorro): python/generaValoresReporte.py $(csvProbabilidadCapturaGatosSocorro)
	if not exist "$(subst /,\,$(@D))" mkdir $(subst /,\,$(@D))
	python python/generaValoresReporte.py -r $(datapackageCapturaGatosSocorro) -ippd $(csvDistribucionPosteriorSocorro) -posf $(csvProbabilidadCapturaGatosSocorro) -o $(@)

# Objetivos para generar resultados de Guadalupe
$(csvDistribucionPosteriorGuadalupe): python/generaTamanioPoblacionGatos.py $(datapackageCapturaGatosGuadalupe)
	if not exist "$(subst /,\,$(@D))" mkdir $(subst /,\,$(@D))
	python python/generaTamanioPoblacionGatos.py -r $(datapackageCapturaGatosGuadalupe) -o $(@)

$(csvProbabilidadCapturaGatosGuadalupe): python/generaProbabilidadAtraparGatosRemanentes.py $(csvDistribucionPosteriorGuadalupe)
	if not exist "$(subst /,\,$(@D))" mkdir $(subst /,\,$(@D))
	python python/generaProbabilidadAtraparGatosRemanentes.py -r $(datapackageCapturaGatosGuadalupe) -ippd $(csvDistribucionPosteriorGuadalupe) -o $(csvProbabilidadCapturaGatosGuadalupe)

$(jsonValoresReporteGatosGuadalupe): python/generaValoresReporte.py $(csvProbabilidadCapturaGatosGuadalupe)
	if not exist "$(subst /,\,$(@D))" mkdir $(subst /,\,$(@D))
	python python/generaValoresReporte.py -r $(datapackageCapturaGatosGuadalupe) -ippd $(csvDistribucionPosteriorGuadalupe) -posf $(csvProbabilidadCapturaGatosGuadalupe) -o $(@)

# Esta sección las pruebas y demostraciones
pruebas: # Corre las pruebas de las funciones
	python -m doctest -v python/tests/test_unidad-pruebas.py

# Elimina PDFs, PNGs y residuos de LaTeX
clean:
	del README.pdf
	del /S /Q entrega\erradicacion_gatos_socorro.html
	del /S /Q entrega\*.pdf
	del /S /Q entrega\*.aux
	del /S /Q entrega\*.bbl
	del /S /Q entrega\*.bcf
	del /S /Q entrega\*.blg
	del /S /Q entrega\*.log
	del /S /Q entrega\*.out
	del /S /Q entrega\*.run.xml
	del /S /Q entrega\*.toc
	del /S /Q entrega\*.nav
	del /S /Q entrega\*.snm
	del /S /Q entrega\*.fdb_latexmk
	del /S /Q entrega\*.fls
	del /S /Q entrega\*.pytxcode
	del /S /Q entrega\*.synctex.gz
	del /S /Q resultados\*.csv
	del /S /Q resultados\*.json
