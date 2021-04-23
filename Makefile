# I. Definición del _phony_ *all* que enlista todos los objetivos principales
# ===========================================================================

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
	cd reports & del *.pythontex
	rm --force reports\pythontex-files-cabras-guadalupe
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
	cd reports & del *.pythontex
	rm --force reports\pythontex-files-estimacion_poblacion_inicial
	cd reports & pdflatex estimacion_poblacion_inicial.tex
	cd reports & bibtex estimacion_poblacion_inicial
	cd reports & pythontex estimacion_poblacion_inicial.tex
	cd reports & pdflatex estimacion_poblacion_inicial.tex
	cd reports & pdflatex estimacion_poblacion_inicial.tex

# Escritura de presentacion con nombre metodo_Ramsey.pdf
# Los archivos que utiliza son los resultadosEstimacionPoblacionInicial (gráficas y datos-objetivo.json).
# Los archivos que utiliza son los archivoPresentacion (título y las diapositivas).
# Primero borra los archivos generados por pythontex para que se actualicen los datos.
# Corre bibtex y pythontex, genera el archivo pdf y los muestra.
reports/presentacion/metodo_ramsey.pdf: $(texMetodoRamsey) \
    $(resultadosEstimacionPoblacionInicial) $(imagenesMetodoRamsey) python/bayes.py \
    $(referenciasLatex)
	cd reports/presentacion & del *.pythontex
	rm --force reports\presentacion\pythontex-files-metodo_ramsey
	cd reports/presentacion & pdflatex metodo_ramsey.tex
	cd reports/presentacion & bibtex metodo_ramsey
	cd reports/presentacion & pythontex metodo_ramsey.tex
	cd reports/presentacion & pdflatex metodo_ramsey.tex
	cd reports/presentacion & pdflatex metodo_ramsey.tex

# Escritura de la presentación del artículo de cámaras trmapa sin identificación de individuos
reports/camaras-trampa.pdf: $(texCamarasTrampa) $(imagenesCamarasTrampa) $(referenciasLatex)
	cd reports & pdflatex camaras-trampa.tex
	cd reports & bibtex camaras-trampa
	cd reports & pdflatex camaras-trampa.tex
	cd reports & pdflatex camaras-trampa.tex

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
#===============================================================================================
# 5 II Declaracion de las variables

# V Reglas del resto de los phonies
# =================================
all: mutants

repo = gatos
codecov_token = 92c09c8a-f80e-4220-af6d-1b8bb79be8f1

.PHONY: all clean format install lint mutants tests

check:
	black --check --line-length 100 ${repo}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${repo}
	flake8 --max-line-length 100 tests
	mypy ${repo}
	mypy tests

format:
	black --line-length 100 ${repo}
	black --line-length 100 tests

install:
	pip install --editable .

lint:
	flake8 --max-line-length 100 ${repo}
	flake8 --max-line-length 100 tests
	pylint ${repo}
	pylint tests

mutants: install
	mutmut run --paths-to-mutate ${repo}


tests: install
	pytest --verbose

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
	rm --force --recursive reports/pythontex*
	rm --force .mutmut-cache
	rm --recursive --force ${repo}.egg-info
	rm --recursive --force ${repo}/__pycache__
	rm --recursive --force ${repo}/**/__pycache__
	rm --recursive --force tests/__pycache__