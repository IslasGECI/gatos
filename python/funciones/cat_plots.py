'''
Este módulo contiene las funciones para generar las graficas utilizadas en los
reportes de erradicación de gatos.
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def _quit_spines():
    ''' Función para quita las línea superior y la del lado derecho de la figura
    actual.
    '''
    eje = plt.gca()
    eje.spines["top"].set_visible(False)
    eje.spines["right"].set_visible(False)

def plot_time_serie_captures_per_effort(fechas: pd.Series, captura_por_esfuerzo: np.array):
    ''' Función para generar la gráfica de captura por esfuerzo

    # Parámetros
    `fechas pd.Series`
    Serie de pandas que contiene la columna de las fechas.

    `captura_por_esfuerzo np.array`
    Serie de pandas que contiene las capturas dividida por unidad de esfuerzo.
    '''
    plt.plot(fechas, captura_por_esfuerzo, "o")
    plt.ylabel("Catch per effort unit (cats/trap$\cdot$night)")    
    _quit_spines()

def plot_time_serie_cumulative_captures(fechas: pd.Series, capturas_acumuladas: np.array):
    ''' Función para generar la gráfica de captura por esfuerzo

    # Parámetros
    `fechas pd.Series`
    Serie de pandas que contiene la columna de las fechas.

    `capturas_acumuladas np.array`
    Serie de pandas que contiene las capturas acumuladas.
    '''
    plt.plot(fechas, capturas_acumuladas, "o")
    plt.ylabel("Accumulated catch (cats)")    
    _quit_spines()

def plot_cumulative_effort_vs_cumulative_captures(esfuerzo_acumuladas: np.array, capturas_acumuladas: np.array):
    ''' Función para generar la gráfica de captura por esfuerzo

    # Parámetros
    `esfuerzo_acumuladas np.array`
    Serie de pandas que contiene el esfuerzo acumulado

    `capturas_acumuladas np.array`
    Serie de pandas que contiene las capturas acumuladas.
    '''
    plt.plot(esfuerzo_acumuladas, capturas_acumuladas, "o")
    plt.ylabel("Accumulated catch (cats)")
    plt.xlabel("Accumulated effort (trap-night)")
    _quit_spines()

def plot_cumulative_effort_vs_captures_per_effort(esfuerzo_acumuladas: np.array, captura_por_esfuerzo: np.array):
    ''' Función para generar la gráfica de captura por esfuerzo en función del
    esfuerzo acumulado.

    # Parámetros
    `esfuerzo_acumuladas np.array`
    Serie de pandas que contiene el esfuerzo acumulado

    `capturas_acumuladas np.array`
    Serie de pandas que contiene las capturas acumuladas.
    '''
    plt.plot(esfuerzo_acumuladas, captura_por_esfuerzo, "o")
    plt.ylabel("Catch per effort unit (cats/trap$\cdot$night)")
    plt.xlabel("Accumulated effort (trap-night)")
    _quit_spines()
