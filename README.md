<img src="https://www.islas.org.mx/img/logo.svg" align="right" width="256" />

# Erradicación de gato feral (islas Socorro y Guadalupe)

[![codecov](https://codecov.io/gh/IslasGECI/gatos/branch/develop/graph/badge.svg?token=5AF7UHZUSZ)](https://codecov.io/gh/IslasGECI/gatos)

Herramientas para dar seguimiento a la erradicación de gatos ferales en las islas Socorro y Guadalupe.

## Qué hace

Convierte los registros de campo de capturas y esfuerzo en tablas y gráficas que muestran el avance del trabajo. También calcula estimaciones del tamaño de la población y de la probabilidad de que la erradicación haya terminado.

## Uso

Los programas leen sus archivos de datos y guardan los resultados en los archivos que usted indique: tablas resumen, gráficas anuales y cálculos de probabilidad. En `DOCS.md` están los programas disponibles, sus opciones y el formato de los archivos de entrada y salida.

## Antes de empezar

Necesita sus registros de campo en archivos CSV (tablas de texto) y una carpeta donde guardar los resultados. Para usar Docker solo necesita tenerlo instalado; para ejecutar los programas directamente necesita Python 3.10 o posterior.

## Ejecutar el proyecto

### Con Docker (recomendado)

Desde la carpeta del proyecto:

```bash
docker compose run --rm islasgeci bash
```

La primera vez, dentro del contenedor ejecute `make setup` para preparar el proyecto y las carpetas de resultados. Después ya puede usar los programas descritos en `DOCS.md`.

El entorno para quienes mantienen el proyecto se abre con `docker compose run --rm islasgeci_dev opencode`.

### Sin Docker

Instale los requisitos y prepare las carpetas de resultados con `make setup` desde la carpeta del proyecto. A continuación puede usar los programas descritos en `DOCS.md`.
