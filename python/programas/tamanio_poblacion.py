
# coding: utf-8


import pymc3 as pm
import matplotlib.pyplot as plt
import numpy as np
import math
import theano.tensor as tt
import pandas as pd

direccion_datos_gatos = "inst/extdata/captura_gatos.csv"
datos_gatos = pd.read_csv(direccion_datos_gatos)
datos_gatos["capturas_acumuladas"] = datos_gatos["capturas"].cumsum()
datos_gatos["esfuerzo_acumulado"] = datos_gatos["esfuerzo"].cumsum()



def calculate_posterior_distribution(blancos_acumulados, esfuerzo, numero_muestra=6000):
    with pm.Model() as modeloPoblacion:
        alpha = 1.0/blancos_acumulados.mean()
        loc = pm.Normal("loc", mu=alpha, sd = 20)
        s = pm.Normal("s", mu=alpha, sd = 20)
        N = pm.Normal("N", mu=blancos_acumulados.max(), sd = 20)
        F = pm.Deterministic("F", N*(1 - tt.exp(-(esfuerzo-loc)/s)))
        valoresObservados = pm.Normal("valores_observados", F, observed=blancos_acumulados)
        start = pm.find_MAP()
        step = pm.Metropolis()
        trace = pm.sample(numero_muestra, step=step, start=start)
    return trace[numero_muestra//2:]



burnOut = calculate_posterior_distribution(datos_gatos["capturas_acumuladas"].values, datos_gatos["esfuerzo_acumulado"].values)

"""
loc_probable = burnOut.get_values('loc').mean()
s_probable = burnOut.get_values('s').mean()
N_probable = burnOut.get_values('N').mean()
print(N_probable)
pm.plots.traceplot(trace=burnOut, varnames=["s"])
pm.plots.plot_posterior(trace=burnOut, varnames=["s"], alpha_level=0.1, text_size=17)



pm.plots.traceplot(trace=burnOut, varnames=["N"])
pm.plots.plot_posterior(trace=burnOut, varnames=["N"], alpha_level=0.1, text_size=17)


IC = np.percentile(burnOut["N"][:],[2.5,97.5])

blancos_acumulados = datos_gatos["capturas_acumuladas"]
esfuerzo = datos_gatos["esfuerzo_acumulado"]

gatosRestantes = math.ceil(IC[-1] * .99 - blancos_acumulados[-1])



pm.plots.traceplot(trace=burnOut, varnames=["loc"])
pm.plots.plot_posterior(trace=burnOut, varnames=["loc"], alpha_level=0.1, text_size=17)



loc_probable = burnOut.get_values('loc').mean()
s_probable = burnOut.get_values('s').mean()
N_probable = burnOut.get_values('N').mean()


y = N_probable*(1-np.exp(-(esfuerzo-loc_probable) /s_probable))


plt.plot(esfuerzo, y)
plt.scatter(esfuerzo,blancos_acumulados)



y = N_probable*(np.exp(-(esfuerzo-loc_probable) /s_probable))/s_probable



plt.plot(esfuerzo, y)
plt.scatter(esfuerzo,blancos/esfuerzo_no_acumulado)



esfuerzo_requerido = math.ceil(loc_probable - s_probable * math.log(0.05))



esfuerzoFaltante = math.ceil(esfuerzo_requerido - esfuerzo[-1])


plt.show()
"""
