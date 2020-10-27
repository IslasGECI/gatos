import click
from click_default_group import DefaultGroup

# Programa para crear `json`` del tamaño de la población a partir de archivos
# que contienen las distribuciones posteriores.

# region Se importan las librerías
import json  # Librería para el manejo de los archivos json
import numpy as np  # Librería para manej  aar vectores facilmente
import sys  # Esta librería se usa para obtener una referencia a la terminal

# Esta librería se utiliza para verificar si existe el archivo de eventos (.log)
import os

# Librerías creadas para este repositorio
from gatos.PopulationEstimator import PopulationEstimator
import metadatatools

# endregion
@click.group(cls=DefaultGroup, default="create", default_if_no_args=True)
def cli():
    pass


# region Se cargan los datos y se extraen los datos de interes
# Se guarda una referencia a la carpeta de resultados
@cli.command(short_help="Cálcula la distribución posterior para el tamaño de la población inicial")
@click.option("--resource", "-r", type=click.Path(), help="Nombre del recurso csv")
@click.option("--output-file", "-o", type=click.Path(), help="Nombre del archivo de salida csv")
def calculate(**argumentos):
    DatosSocorro = metadatatools.import_tabular_data_resource(argumentos["resource"])
    nombre_esfuerzo: str = "Esfuerzo"
    nombre_capturas: str = "Capturas"
    esfuerzo: np.array = np.array(
        DatosSocorro.get_value(nombre_esfuerzo) / (30 * 7 * 5)
    )  # Días hombre: 30 trampas, 7 tramperos, 5 días
    capturas: np.array = np.array(DatosSocorro.get_value(nombre_capturas))
    # endregion

    # region Se busca el tamaño de la población
    repeticiones = 3
    iteraciones = 1_000_000
    estimador_poblacion_inicial: PopulationEstimator = PopulationEstimator(
        esfuerzo, capturas, argumentos["output_file"]
    )
    estimador_poblacion_inicial.run(
        repeticiones=repeticiones, iteraciones=iteraciones, n_datos_descartados=iteraciones * 0.1
    )


# endregion
