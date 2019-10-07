''' Programa para generar los parámetros utilizados en el reporte de gatos '''

# region Se importan las librerías necesarias
import argparse  # Módulo para facilitar que se le pasen argumentos de entrada al programa
import json  # Módulo para facilitar la creación de archivos json
import os  # Este módulo se utilizó para manejar los paths

import numpy as np  # Módulo para poder manejar operaciones vectorizadas
import pandas as pd  # Módulo para crear DataFrames

# Módulo de gatos, aquí se encuentra el método para poder cargar los metadatos
import gatos as dmc
# Módulo que contiene método para calcular el valor más probable
import gatos.CredibleIntervals as ci
import datatools
import gatos.Rounder as rd
# endregion

# region Se agregan las rutas a los datos
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--resource", required=True,
                help="Nombre del recurso csv", type=str)
ap.add_argument("-o", "--output-file", required=True,
                type=argparse.FileType('w'), help="Nombre del archivo de salida")
ap.add_argument("-ippd", "--initial-population-posterior-distribution",
                help="Nombre del archivo donde se encuentras las distribuciones posteriores")
ap.add_argument("-posf", "--probability-of-success-file", required=True,
                type=str, nargs='+',
                help="Nombre de los archivos donde se encuentra la probabilidad de acabar con los gatos remanentes")
# Se crear un diccionario con los argumentos (este diccionario lanza un error si se intenta modificar)
ARGUMENTOS = vars(ap.parse_args())
# endregion

# region Se cargan los datos y se extraen algunos metadatos
# Se cargan los datos de las distribuciones posteriores
Datos_captura_gatos = datatools.import_tabular_data_resource(ARGUMENTOS["resource"])
distribuciones_posteriores: pd.DataFrame = pd.read_csv(
    ARGUMENTOS["initial_population_posterior_distribution"])
distribucion_posterior_No: pd.Series = distribuciones_posteriores.No
# Se obtiene el nombre de las columnas de esfuerzo y captura
nombre_columna_esfuerzo: str = Datos_captura_gatos.get_variable_name_from_standard_name(datatools.StandardName.effort)
nombre_columna_capturas: str = "capturas"

datos_probabilidad_captura: pd.DataFrame = pd.read_csv(
    ARGUMENTOS["probability_of_success_file"][0])
probabilidad: np.array = datos_probabilidad_captura.probabilidad.values
esfuerzo_trampas: np.array = datos_probabilidad_captura.esfuerzo_capturas.values
remanentes_capturados: np.array = datos_probabilidad_captura.remanentes_capturados.values
datos_derivada_captura: pd.DataFrame = pd.read_csv(
    ARGUMENTOS["probability_of_success_file"][1])
derivada: np.array = datos_derivada_captura.derivada.values
esfuerzo_para_derivada: np.array = datos_derivada_captura.esfuerzo_derivada.values
# endregion

# region Se encuentran los valores de interes
esfuerzo: np.array = np.array(
    Datos_captura_gatos.get_value(nombre_columna_esfuerzo))
capturas: np.array = np.array(
    Datos_captura_gatos.get_value(nombre_columna_capturas))
total_capturas: int = int(
    np.array(Datos_captura_gatos.get_value(nombre_columna_capturas)).sum())
poblacion_inicial: int = int(ci.calc_min_interval(
    np.sort(distribucion_posterior_No.values), alpha=0.95).mean().round())
distribucion_gatos_remanentes: np.array = distribucion_posterior_No.values - total_capturas
gatos_para_knockdown: int = int(np.ceil(poblacion_inicial * 0.99))
esfuerzo_trampas_mayor_95: int = int(
    esfuerzo_trampas[probabilidad >= 0.95].min())
id_min = len(probabilidad) - (probabilidad > 0.025).sum()
id_max = len(probabilidad) - (probabilidad > 0.975).sum()
intervalo_probabilidad_terminar_remanentes = [
    rd.Rounder.round((esfuerzo_trampas[id_min] + esfuerzo_trampas[id_min+1])/2), rd.Rounder.round((esfuerzo_trampas[id_max]+esfuerzo_trampas[id_max+1])/2)]

# endregion

# region Se guardan los datos en un archivo json
diccionario_resultados: dict = {}
diccionario_resultados["total_capturas"] = total_capturas
diccionario_resultados["poblacion_inicial"] = poblacion_inicial
diccionario_resultados["intervalo_gatos_remanentes"] = np.percentile(
    distribucion_gatos_remanentes, [2.5, 97.5]).astype(int).tolist()
diccionario_resultados["intervalo_trampas_gatos_remanentes"] = intervalo_probabilidad_terminar_remanentes
diccionario_resultados["vmp_gatos_remanentes"] = poblacion_inicial - \
    total_capturas
diccionario_resultados["gatos_para_knockdown"] = gatos_para_knockdown
diccionario_resultados["gatos_Mop_up"] = poblacion_inicial - gatos_para_knockdown
diccionario_resultados["gatos_para_Mop_up"] = gatos_para_knockdown - total_capturas
diccionario_resultados["porcentaje_removidos"] = int(
    np.ceil(total_capturas * 100 / poblacion_inicial))
diccionario_resultados["porcentaje_remanentes"] = int(
    np.ceil(100 - (total_capturas * 100 / poblacion_inicial)))
diccionario_resultados["porcentaje_remanentes"] = int(
    np.ceil(poblacion_inicial - gatos_para_knockdown))
diccionario_resultados["esfuerzo_trampas_mayor_95"] = rd.Rounder.round(esfuerzo_trampas_mayor_95)
diccionario_resultados["dias_esfuerzo_trampas_mayor_95"] = int(np.ceil(esfuerzo_trampas_mayor_95/(10*30)))
diccionario_resultados["tramperos_100_dias"] = int(np.ceil(esfuerzo_trampas_mayor_95/(100*30)))
json.dump(diccionario_resultados, ARGUMENTOS["output_file"])
# endregion
