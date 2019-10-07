import numpy as np
import pandas as pd


def calc_min_interval(x, alpha):
    """Internal method to determine the minimum interval of
    a given width
    Assumes that x is sorted numpy array.
    """
    n = len(x)
    cred_mass = 1.0 - alpha

    interval_idx_inc = int(np.floor(cred_mass * n))
    n_intervals = n - interval_idx_inc
    interval_width = x[interval_idx_inc:] - x[:n_intervals]

    if len(interval_width) == 0:
        raise ValueError('Too few elements for interval calculation')

    min_interval_width = interval_width.min()
    limite_inferior = np.arange(x.min(), x.max() - min_interval_width + 2)
    limite_superior = limite_inferior + min_interval_width
    n_dentro = [((inferior<=x) & (x<=superior)).sum() for inferior, superior in zip(limite_inferior,limite_superior)]
    
    max_idx = np.argmax(n_dentro)
    hdi_min = limite_inferior[max_idx]
    hdi_max = limite_superior[max_idx]
    return np.array(hdi_min, hdi_max)

def calculate_interval_from_bar_graph(probabilidad,esfuerzo,limites):
    id_min = len(np.array(probabilidad)) - sum(np.array(probabilidad)>limites[0])
    id_max = len(np.array(probabilidad)) - sum(np.array(probabilidad)>limites[1])
    esfuerzo_necesario = [(esfuerzo_trampas[id_min]+ esfuerzo_trampas[id_min+1])/2,(esfuerzo_trampas[id_max]+esfuerzo_trampas[id_max+1])/2]
    return esfuerzo_necesario