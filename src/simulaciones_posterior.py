#!/usr/bin/env python
#
# Calcula los meses necesarios para terminar la erradicacion.

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import json 
import math
import datetime as dt
from dateutil.relativedelta import relativedelta

archivo_capturas = 'inst/extdata/erradicaciones-mamiferos/captura_gatos_socorro.csv'
capturas = pd.read_csv(archivo_capturas)

archivo_posterior = 'resultados/distribucion_posterior_socorro.csv'
posterior = pd.read_csv(archivo_posterior)

factor_conversion = 30 * 5 * 7

#### Función `calculate_catch_probability`
def calculate_catch_probability(alfa_m, beta_m, esfuerzo_m):
    probabilidad_captura = []
    exp = np.exp(alfa_m + esfuerzo_m * beta_m)
    probabilidad_captura = exp / (1 + exp)
    return np.array(probabilidad_captura)

def check_probability(probabilidad):
  if math.ceil(1/probabilidad) < 0:
    return 9999
  else:
    return math.ceil(1/probabilidad)

# ### Actualización de los conjuntos de datos
capturas["esfuerzo_convertido"] = capturas.esfuerzo / factor_conversion
posterior['remanentes'] = posterior.No - capturas.capturas.sum()

# La mediana de las últimas 3
esfuerzo = np.median(capturas.esfuerzo_convertido.iloc[-4:])

# El promedio de los remanentes
gatos_remanentes = posterior.remanentes.median()

posterior['probabilidad_captura'] = calculate_catch_probability(posterior.a, posterior.b, esfuerzo)

diccionario_salida = {}
print(posterior.probabilidad_captura.median())
meses_faltantes = 1/posterior.probabilidad_captura
print(f'meses faltantes {meses_faltantes.median()} si seguimos con un esfuerzo de {esfuerzo * factor_conversion} \n')
diccionario_salida["esfuerzo_actual"] = int(esfuerzo * factor_conversion)
diccionario_salida["meses_faltantes_esfuerzo_actual"] = int(np.ceil(meses_faltantes.median()))

# para acabar en el primer semestre del 2020
fecha= dt.date.today()
final_primer_semestre = dt.datetime(2020,7,1)
meses_para_acabe_agno = relativedelta(final_primer_semestre,fecha).months + relativedelta(final_primer_semestre,fecha).days/31
factor_para_acabar_agno = 1/(meses_para_acabe_agno*posterior.probabilidad_captura.median())
esfuerzo_para_agno = esfuerzo * factor_para_acabar_agno
print(f'Esfuerzo para acabar en el primer semestre 2020 es {esfuerzo_para_agno * factor_conversion}')
diccionario_salida["esfuerzo_primer_semestre"] = int(esfuerzo_para_agno * factor_conversion)
print(f'Este esfuerzo lo lograríamos con {esfuerzo_para_agno*factor_conversion/900} tramperos \n')
diccionario_salida["tramperos_primer_semestre"] = int(esfuerzo_para_agno*factor_conversion/900)

# Con tres capacidades de cargas distintas
# Coeficiente de crecimiento poblacional propuestos por Leo
r = [0.032, 0.08, 0.126] # ¿Es correcata esa tasa de crecimiento?
capacidad_carga = [200, 400, 800]
correccion_capacidad = r[1]*(1 - gatos_remanentes/capacidad_carga)
print(f'La corrección es {correccion_capacidad}')
probabilidad_corregida = posterior.probabilidad_captura.median() - correccion_capacidad
print(f'La probabilidad corregida es {probabilidad_corregida}')
print(f'Meses para acabar {math.ceil(1/probabilidad_corregida[1])}')

diccionario_salida["meses_faltantes_k_baja"] = check_probability(probabilidad_corregida[0])
diccionario_salida["meses_faltantes_k_media"] = check_probability(probabilidad_corregida[1])
diccionario_salida["meses_faltantes_k_alta"] = check_probability(probabilidad_corregida[2])

diccionario_salida["capacidad_carga"] = capacidad_carga

# Escritura del archivo de salida
with open('reports/non-tabular/json_meses_faltantes.json', 'w') as archivo:
    json.dump(diccionario_salida, archivo)
