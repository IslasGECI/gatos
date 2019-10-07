# Programa para crear `json`` del tamaño de la población a partir de archivos
# que contienen las distribuciones posteriores.

# region Se importan las librerías
import argparse  # Librería para obtener los argumentos de entrada
import json  # Librería para el manejo de los archivos json
import numpy as np  # Librería para manejar vectores facilmente
import sys  # Esta librería se usa para obtener una referencia a la terminal
# Esta librería se utiliza para verificar si existe el archivo de eventos (.log)
import os
# Librerías creadas para este repositorio
from gatos.PopulationEstimator import PopulationEstimator
import datatools
# endregion

# region Se cargan los datos y se extraen los datos de interes
# Se guarda una referencia a la carpeta de resultados
analizador_entrada = argparse.ArgumentParser()
analizador_entrada.add_argument("-r", "--resource", required=True,
                help="Nombre del recurso csv", type=str)
analizador_entrada.add_argument("-o", "--output-file", required=True,
                type=str)
argumentos = vars(analizador_entrada.parse_args())

DatosSocorro = datatools.import_tabular_data_resource(argumentos["resource"])
nombre_esfuerzo: str = DatosSocorro.get_variable_name_from_standard_name(datatools.StandardName.effort)
nombre_capturas: str = "capturas"
esfuerzo: np.array = np.array(DatosSocorro.get_value(
    nombre_esfuerzo)/(30 * 7 * 5))  # Días hombre: 30 trampas, 7 tramperos, 5 días
capturas: np.array = np.array(DatosSocorro.get_value(nombre_capturas))
# endregion

# region Se busca el tamaño de la población
repeticiones = 3
iteraciones = 1_000_000
estimador_poblacion_inicial: PopulationEstimator = PopulationEstimator(
    esfuerzo, capturas, argumentos["output_file"])
estimador_poblacion_inicial.run(
    repeticiones=repeticiones, iteraciones=iteraciones, n_datos_descartados=iteraciones*0.1)
# endregion
