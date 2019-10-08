#!/usr/bin/env python
#
# Calcula los meses necesarios para terminar la erradicacion.

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import json

archivo_capturas = 'inst/extdata/erradicaciones-mamiferos/captura_gatos_socorro.csv'
capturas = pd.read_csv(archivo_capturas)

archivo_posterior = 'resultados/distribucion_posterior_socorro.csv'
posterior = pd.read_csv(archivo_posterior)

factor_conversion = 30 * 5 * 7

# ### Función `calculate_catch_probability`
def calculate_catch_probability(alfa_m, beta_m, esfuerzo_m):
    probabilidad_captura = []
    exp = np.exp(alfa_m + esfuerzo_m * beta_m)
    probabilidad_captura = exp / (1 + exp)
    return np.array(probabilidad_captura)

# ### Actualización de los conjuntos de datos
capturas["esfuerzo_convertido"] = capturas.esfuerzo / factor_conversion
posterior['remanentes'] = posterior.No - capturas.capturas.sum()

# La mediana de las últimas 3
esfuerzo = np.median(capturas.esfuerzo_convertido.iloc[-4:])

# El promedio de los remanentes
posterior.remanentes.mean()


# Coeficiente de crecimiento poblacional propuestos por Leo
r = [0.032, 0.08, 0.126]


posterior['probabilidad_captura'] = calculate_catch_probability(posterior.a, posterior.b, esfuerzo)

print(posterior.probabilidad_captura.median())
meses_faltantes = 1/posterior.probabilidad_captura
#print(meses_faltantes)
print(f'meses faltantes {meses_faltantes.median()} si seguimos con un esfuerzo de {esfuerzo * factor_conversion}')

meses_para_acabe_agno = 3
factor_para_acabar_agno = 1/(meses_para_acabe_agno*posterior.probabilidad_captura.median())
esfuerzo_para_agno = esfuerzo * factor_para_acabar_agno
print(f'Esfuerzo para acabar en el 2019 es {esfuerzo_para_agno * factor_conversion}')
print(f'Este esfuerzo lo lagraríamos con {esfuerzo_para_agno*factor_conversion/900} tramperos')
meses_para_acabe_agno = 9
factor_para_acabar_agno = 1/(meses_para_acabe_agno*posterior.probabilidad_captura.median())
esfuerzo_para_agno = esfuerzo * factor_para_acabar_agno
print(f'Esfuerzo para acabar en el primer semestre 2020 es {esfuerzo_para_agno * factor_conversion}')
print(f'Este esfuerzo lo lograríamos con {esfuerzo_para_agno*factor_conversion/900} tramperos')
diccionario_salida = {
    "meses_faltantes": int(np.ceil(meses_faltantes.median()))
}
with open('json_meses_faltantes.json', 'w') as archivo:
    json.dump(diccionario_salida, archivo)

n_simulacion = 100_000

sum(posterior.probabilidad_captura.sample(n=n_simulacion, replace=True).values > np.random.uniform(0.032, 0.126, size = n_simulacion))/n_simulacion

# ¿Qué es esto?
19/posterior.probabilidad_captura.max()


#plt.figure(figsize = (11,8))
#plt.hist(posterior.probabilidad_captura, bins=30)
#plt.axis([0,0.12,0,120000]) 
#plt.xlabel('Probabilidad de captura', fontsize=14)
#plt.ylabel('Frecuencia', fontsize=14)
#eje = plt.gca() # gca hace referencia al eje actual
#eje.spines['top'].set_visible(False)
#eje.spines['right'].set_visible(False)
#plt.legend()
#plt.savefig('probabilidad_captura.png', dpi = 300)


remanentes = np.random.binomial(200, posterior.probabilidad_captura)

#plt.figure(figsize = (11,8))
#plt.hist(remanentes, bins=30)
#plt.axis([0, 35,0,200000]) 
#plt.xlabel('Capturas', fontsize=14)
#plt.ylabel('Frecuencia', fontsize=14)
#eje = plt.gca() # gca hace referencia al eje actual
#eje.spines['top'].set_visible(False)
#eje.spines['right'].set_visible(False)
#plt.legend()
#plt.savefig('captura_200_p.png', dpi = 300)


reclutamiento = np.ceil(np.random.binomial(200, np.random.uniform(0.032, 0.126, size = n_simulacion)) * (1-0.12))


#plt.figure(figsize = (11,8))
#plt.hist(reclutamiento, bins=16)
#plt.axis([0, 20,0,22500]) 
#plt.xlabel('Reclutamientos', fontsize=14)
#plt.ylabel('Frecuencia', fontsize=14)
#eje = plt.gca() # gca hace referencia al eje actual
#eje.spines['top'].set_visible(False)
#eje.spines['right'].set_visible(False)
#plt.legend()
#plt.savefig('reclutamiento_200_p.png', dpi = 300)


neto = reclutamiento - remanentes[0:100000]

#plt.figure(figsize = (11,8))
#plt.hist(neto, bins=59)
#plt.axis([-20, 30,0,6_000]) 
#plt.xlabel('$N_{t+1} - N_{t}$', fontsize=18)
#plt.xticks(fontsize = 16)
#plt.ylabel('Frecuencia', fontsize=18)
#plt.yticks(fontsize = 16)
#eje = plt.gca() # gca hace referencia al eje actual
#eje.spines['top'].set_visible(False)
#eje.spines['right'].set_visible(False)
#plt.legend()
##plt.savefig('cambio_tres_meses.png', dpi = 300)


neto.max() - neto.min()

sum(neto < 0)/len(neto)