# I. Definición del _phony_ *all* que enlista todos los objetivos principales
# ===========================================================================
all: \
    reports/albatrosSinGatos.pdf \
    reports/erradicacion_gatos_socorro_es.html \

# 1. Erradicación de gato en Isla Socorro
# 1.II Declaracion de las variables
csvDistribucionPosteriorSocorro = \
    resultados/distribucion_posterior_socorro.csv

csvProbabilidadCapturaGatosSocorro = \
    resultados/probabilidad_captura_remanentes_socorro.csv \
    resultados/derivada_captura_esfuerzo_socorro.csv

datapackageCapturaGatosSocorro = \
    inst/extdata/erradicaciones-mamiferos/datapackage.json\
    inst/extdata/erradicaciones-mamiferos/captura_gatos_socorro.csv

jsonValoresReporteGatosSocorro = \
    resultados/tabla_valores_socorro.json

pngGraficasCapturaGatoSocorro = \
    resultados/accumulated-catch_accumulated-effort.png \
    resultados/accumulated-catch_time-serie.png \
    resultados/catch-per-unit-effort_accumulated-effort.png \
    resultados/catch-per-unit-effort_time-serie.png

resultadosEstimacionPoblacionInicial = \
    resultados\datos-objetivo.json\
    resultados\probabilidad_captura.png\
    resultados\tamagno_inicial.png\
    resultados\datos_histograma_No.csv\
    resultados\datos_histograma_q.csv\
    resultados\metadatos_histograma_q.json\
    resultados\metadatos_histograma_No.json

versionDatos = f17d337c20f9

# 1.III. Reglas para construir los objetivos principales
# ====================================================
reports/erradicacion_gatos_socorro_es.html: python/generaReporteErradicacionGatosSocorro.py $(jsonValoresReporteGatosSocorro)
	if [ ! -d $(@D) ]; then mkdir -p $(@D); fi
	python python/generaReporteErradicacionGatosSocorro.py -r inst/extdata/erradicaciones-mamiferos/captura_gatos_socorro.csv --initial-population-posterior-distribution $(csvDistribucionPosteriorSocorro) --probability-of-success-file $(csvProbabilidadCapturaGatosSocorro) --report-values $(jsonValoresReporteGatosSocorro) -o $(@) --espaniol

reports/erradicacion_gatos_socorro_en.html: python/generaReporteErradicacionGatosSocorro.py $(jsonValoresReporteGatosSocorro)
	if [ ! -d $(@D) ]; then mkdir -p $(@D); fi
	python python/generaReporteErradicacionGatosSocorro.py -r inst/extdata/erradicaciones-mamiferos/captura_gatos_socorro.csv --initial-population-posterior-distribution $(csvDistribucionPosteriorSocorro) --probability-of-success-file $(csvProbabilidadCapturaGatosSocorro) --report-values $(jsonValoresReporteGatosSocorro) -o $(@) --ingles

# 1.IV. Reglas para construir las dependencias de los objetivos principales
# =======================================================================
$(datapackageCapturaGatosSocorro):
	if [ ! -d $(@D) ]; then mkdir -p $(@D); fi
	curl --output $@ --user ${BITBUCKET_USERNAME}:${BITBUCKET_PASSWORD} https://bitbucket.org/IslasGECI/datos-texto/raw/$(versionDatos)/datapackage/erradicaciones-mamiferos/$(@F)

$(csvDistribucionPosteriorSocorro): $(datapackageCapturaGatosSocorro) log/install_requirements.log
	if [ ! -d $(@D) ]; then mkdir -p $(@D); fi
	crea_tamagno_poblacion_gatos calculate -r inst/extdata/erradicaciones-mamiferos/captura_gatos_socorro.csv -o $(@)

resultados/probabilidad_captura_remanentes_socorro.csv: $(csvDistribucionPosteriorSocorro)
	if [ ! -d $(@D) ]; then mkdir -p $(@D); fi
	crea_probabilidad_atrapar_gatos remanent_cats -r inst/extdata/erradicaciones-mamiferos/captura_gatos_socorro.csv --initial-population-posterior-distribution $(csvDistribucionPosteriorSocorro) -o resultados/probabilidad_captura_remanentes_socorro.csv

resultados/derivada_captura_esfuerzo_socorro.csv: $(csvDistribucionPosteriorSocorro)
	if [ ! -d $(@D) ]; then mkdir -p $(@D); fi
	crea_probabilidad_atrapar_gatos derivate_effort -r inst/extdata/erradicaciones-mamiferos/captura_gatos_socorro.csv --initial-population-posterior-distribution $(csvDistribucionPosteriorSocorro) -o resultados/derivada_captura_esfuerzo_socorro.csv

$(jsonValoresReporteGatosSocorro): $(csvProbabilidadCapturaGatosSocorro)
	if [ ! -d $(@D) ]; then mkdir -p $(@D); fi
	crea_valores_reporte calculate -r inst/extdata/erradicaciones-mamiferos/captura_gatos_socorro.csv --initial-population-posterior-distribution $(csvDistribucionPosteriorSocorro) --probability-of-success-file resultados/probabilidad_captura_remanentes_socorro.csv  --derivate-effort-file resultados/derivada_captura_esfuerzo_socorro.csv -o $(@)

# 3. Albatros sin gatos
# 3.II. Declaración de las variables
# ================================
figurasAlbatrosSinGatos = \
  resultados/LAAL_para_Scott.png


# 3.III. Reglas para construir los objetivos principales
# ====================================================
reports/albatrosSinGatos.pdf: reports/albatrosSinGatos.tex $(figurasAlbatrosSinGatos)
	pdflatex -output-directory=reports -include-directory=reports reports\albatrosSinGatos.tex
	pdflatex -output-directory=reports -include-directory=reports reports\albatrosSinGatos.tex
	start "" /max "reports\albatrosSinGatos.pdf"

reports/albatrosSinGatos.docx: reports/albatrosSinGatos.tex $(figurasAlbatrosSinGatos)
	pandoc reports/albatrosSinGatos.tex -o reports/albatrosSinGatos.docx

# 3.IV. Reglas para construir las dependencias de los objetivos principales
# =======================================================================
# Generación de las figuras para albatrosSinGatos.pdf
$(figurasAlbatrosSinGatos): MATLAB/demostraciones/graficaN.m
	if not exist "$(subst /,\,$(@D))" mkdir $(subst /,\,$(@D))
	runMatlab "MATLAB\demostraciones\graficaN.m"

# 4. No análisis
# 4.II. Declaración de las variables
# ================================
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

imagenesMetodoRamsey = \
    referencias/imagenes/cangrejito_playero.png

# Ingredientes del `estimacion_poblacion_inicial.pdf`.
# El archivo `referencias.bib` tiene la información de las referencias citadas.
# El archivo `estilo_referencias.bst` tiene el estilo de las referencias.
referenciasLatex = \
    reports\referencias.bib\
    reports\estilo_referencias.bst

# Ingredientes de la presentación: metodo_Ramsey
# El archivo `metodo_ramsey.tex` tiene el título de la presentación.
# El archivo `metodo_ramsey_txt.tex` tiene las diapositivas de la presentación.
texMetodoRamsey = \
    reports\presentacion\metodo_ramsey.tex\
    reports\presentacion\metodo_ramsey_txt.tex

# Ingredientes de la presentación: camaras-trampa
# El archivo `camaras-trampa.tex` tiene el título de la presentación.
# El archivo `camaras-trampa_diapositivas.tex` tiene las diapositivas de la
# presentación.
texCamarasTrampa = \
    reports\camaras-trampa.tex\
    reports\camaras-trampa_diapositivas.tex
	
# 4.III. Reglas para construir los objetivos principales
# ====================================================
README.pdf: README.md
	pandoc README.md -o README.pdf
	start "" /max "README.pdf"` 

referencias/bitacora-diaria-isla-guadalupe.pdf: referencias/bitacora_diaria_isla_guadalupe.md
	pandoc referencias/bitacora_diaria_isla_guadalupe.md -o referencias/bitacora-diaria-isla-guadalupe.pdf 
	start "" /max "referencias\bitacora-diaria-isla-guadalupe.pdf"

referencias/bitacora-semanal-isla-guadalupe.pdf: referencias/bitacora_semanal_isla_guadalupe.md
	pandoc referencias/bitacora_semanal_isla_guadalupe.md -o referencias/bitacora-semanal-isla-guadalupe.pdf
	start "" /max "referencias\bitacora-semanal-isla-guadalupe.pdf"

# Escritura de cabras-guadalupe.pdf
reports/cabras-guadalupe.pdf: reports/cabras-guadalupe.tex
	cd reports & del *.pythontex                            #borra dependencia pythontex
	if exist "reports\pythontex-files-cabras-guadalupe" rm --force reports\pythontex-files-cabras-guadalupe
	cd reports & pdflatex cabras-guadalupe.tex
	cd reports & bibtex cabras-guadalupe
	cd reports & pythontex cabras-guadalupe.tex
	cd reports & pdflatex cabras-guadalupe.tex
	cd reports & pdflatex cabras-guadalupe.tex
	start "" /max "reports\cabras-guadalupe.pdf"

# Los archivos que utiliza son las resultadosEstimacionPoblacionInicial (gráficas y
# datos-objetivo.json).
# Los archivos que utiliza son las referenciasLatex (referencias.bib y
# estilo_referencias.bst).
# Primero borra los archivos generados por pythontex para que se actualicen los
# datos.
# Corre bibtex y pythontex, genera el archivo pdf y los muestra.
reports/estimacion_poblacion_inicial.pdf: reports/estimacion_poblacion_inicial.tex \
    $(referenciasLatex) $(resultadosEstimacionPoblacionInicial) python/bayes.py
	cd reports & del *.pythontex                            #borra dependencia pythontex
	if exist "reports\pythontex-files-estimacion_poblacion_inicial" del /Q reports\pythontex-files-estimacion_poblacion_inicial\* #borra dependencia pythontex
	cd reports & pdflatex estimacion_poblacion_inicial.tex
	cd reports & bibtex estimacion_poblacion_inicial
	cd reports & pythontex estimacion_poblacion_inicial.tex
	cd reports & pdflatex estimacion_poblacion_inicial.tex
	cd reports & pdflatex estimacion_poblacion_inicial.tex
	start "" /max "reports\estimacion_poblacion_inicial.pdf"

# Escritura de presentacion con nombre metodo_Ramsey.pdf
# Los archivos que utiliza son los resultadosEstimacionPoblacionInicial (gráficas y datos-objetivo.json).
# Los archivos que utiliza son los archivoPresentacion (título y las diapositivas).
# Primero borra los archivos generados por pythontex para que se actualicen los datos.
# Corre bibtex y pythontex, genera el archivo pdf y los muestra.
reports/presentacion/metodo_ramsey.pdf: $(texMetodoRamsey) \
    $(resultadosEstimacionPoblacionInicial) $(imagenesMetodoRamsey) python/bayes.py \
    $(referenciasLatex)
	cd reports/presentacion & del *.pythontex                            #borra dependencia pythontex
	if exist "reports\presentacion\pythontex-files-metodo_ramsey" del /Q reports\presentacion\pythontex-files-metodo_ramsey\* #borra dependencia pythontex
	cd reports/presentacion & pdflatex metodo_ramsey.tex
	cd reports/presentacion & bibtex metodo_ramsey
	cd reports/presentacion & pythontex metodo_ramsey.tex
	cd reports/presentacion & pdflatex metodo_ramsey.tex
	cd reports/presentacion & pdflatex metodo_ramsey.tex
	start "" /max "reports\presentacion\metodo_ramsey.pdf"

# Escritura de la presentación del artículo de cámaras trmapa sin identificación de individuos
reports/camaras-trampa.pdf: $(texCamarasTrampa) $(imagenesCamarasTrampa) $(referenciasLatex)
	cd reports & pdflatex camaras-trampa.tex
	cd reports & bibtex camaras-trampa
	cd reports & pdflatex camaras-trampa.tex
	cd reports & pdflatex camaras-trampa.tex
	start "" /max "reports\camaras-trampa.pdf"

# 4.IV. Reglas para construir las dependencias de los objetivos principales
# =======================================================================
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


#5 Reporte estimación de esfuerzo para acabar la erradicación de gato feral en Isla Socorro

# 5 II Declaracion de las variables

pngHistogramaCapturasGatosSocorroPorAnio = \
	reports/figures/TotalCapturasPorAnioGatosSocorro.png

csvCapturasGatosSocorro = \
	data/raw/captura_gatos_socorro.csv

# 5 III. Reglas para construir los objetivos principales

reports/cantidad_individuos_remanentes_en.pdf: reports/cantidad_individuos_remanentes_en.tex $(csvCapturasGatosSocorro) $(pngHistogramaCapturasGatosSocorroPorAnio)
	cd $(<D) && pdflatex $(<F)
	cd $(<D) && pdflatex $(<F)

# 5 IV. Reglas para construir las dependencias de los objetivos principales

$(csvCapturasGatosSocorro): log/install_requirements.log
	if [ ! -d $(@D) ]; then mkdir -p $(@D); fi
	descarga_datos $(@F) $(@D)

$(pngHistogramaCapturasGatosSocorroPorAnio):$(csvCapturasGatosSocorro) src/histogramaCapturasPorAnioGatosSocorro
	if [ ! -d $(@D) ]; then mkdir -p $(@D); fi
	src/histogramaCapturasPorAnioGatosSocorro $< $@

# 4.V Reglas del resto de los phonies
# =================================
datos: $(datapackageCapturaGatosSocorro)

# Esta sección las pruebas y demostraciones
pruebas: # Corre las pruebas de las funciones
	python -m doctest -v python/tests/test_unidad-pruebas.py

log/install_requirements.log: src/install_requirements.sh
	if [ ! -d $(@D) ]; then mkdir -p $(@D); fi
	$< > $@

# Elimina PDFs, PNGs y residuos de LaTeX
clean:
	rm --force README.pdf
	rm --force reports/*.aux
	rm --force reports/*.bbl
	rm --force reports/*.bcf
	rm --force reports/*.blg
	rm --force reports/*.fdb_latexmk
	rm --force reports/*.fls
	rm --force reports/*.html
	rm --force reports/*.log
	rm --force reports/*.nav
	rm --force reports/*.out
	rm --force reports/*.pdf
	rm --force reports/*.pytxcode
	rm --force reports/*.run.xml
	rm --force reports/*.snm
	rm --force reports/*.synctex.gz
	rm --force reports/*.toc