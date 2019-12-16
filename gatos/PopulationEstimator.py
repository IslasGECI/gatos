# Clase encargada de encontrar el tama~no de la población de gatos

from pymc import Uniform, deterministic, MCMC, Binomial, Normal
from pymc import stochastic, DiscreteUniform, binomial_like
from pymc.utils import hpd
import numpy as np
import os
import shutil
import pandas as pd


class PopulationEstimator:
    # region Documentación
    ''' Clase encargada de encontrar el tamaño inicial de la población utilizando
    el método de Ramsey

    Para inicializar el estimador se le debe pasar la información necesaria para
    encontrar el tamaño de la población.        

    # Parámetros
    `esfuerzo np.array`

    Esfuerzo de la erradicación

    `capturas np.array`

    Número de iteraciones utilizadas en la simulación de series de Markov Monte Carlo

    ## Nota:
    Para borrar los archivos temporales se debe llamar al método
    `remove_temporal_data()`
    '''
    # endregion

    def __init__(self, esfuerzo: np.array, capturas: np.array, nombre_archivo):
        self.esfuerzo = esfuerzo
        self.capturas = capturas
        self._nombre_archivo = nombre_archivo
        self.tamanios_poblacion = None

    def run(self, repeticiones: int=3, iteraciones: int=6000000, n_datos_descartados: int=30000):
        # region documentación
        ''' Método encargado de correr el modelo de Ramsey una cierta cantidad de
        repeticiones para determinar el tamaño de la población.

        En cada iteración guarda las distribuciones posteriores y a partir de estas
        se calcula el tamaño de la población.

        # Parámetros
        `repeticiones int`

        Número de repeticiones que se utilizarán para encontrar el tamaño inicial
        de la población.

        `iter int`

        Número de iteraciones utilizadas en la simulación de series de Markov Monte Carlo

        `burn int`

        Número de iteraciones que se van a deshechar

        ## Nota:
        Para borrar los archivos temporales se debe llamar al método
        `remove_temporal_data()`
        '''
        # endregion
        repeticion: int = 0
        Modelo_gatitos: MCMC = MCMC(self._Ramsey_model(self.esfuerzo, self.capturas))
        while repeticion < repeticiones:
            Modelo_gatitos.sample(iter=iteraciones, burn=n_datos_descartados)
            a = pd.Series(Modelo_gatitos.trace('a_captura')[:])
            b = pd.Series(Modelo_gatitos.trace('b_captura')[:])
            No = pd.Series(Modelo_gatitos.trace('N_o')[:])
            repeticion += 1
        print("\n")
        pd.DataFrame({"a": a, "b": b, "No": No}).to_csv(
            self._nombre_archivo, index=False)

    def plot_Vmp_histogram(self):
        self.tamanios_poblacion.Vmp.hist()

    def _Ramsey_model(self, v_effort, v_captures):
        ''' Modelo jerarquico utilizado para determinar el tamaño de la población '''
        alpha = Normal('a_captura', mu=.00, tau=1/(2.50*2.50))
        beta = Normal('b_captura', mu=.00, tau=1/(2.50*2.50))
        No = DiscreteUniform('N_o', lower=sum(v_captures), upper=22000)

        @deterministic
        def catchProbability(alfa_m=alpha, beta_m=beta, esfuerzo_m=v_effort):
            probabilidadCaptura = []
            probabilidadCaptura = np.exp(
                alfa_m + esfuerzo_m * beta_m) / (1 + np.exp(alfa_m + esfuerzo_m * beta_m))
            return np.array(probabilidadCaptura)

        @stochastic(observed=True)
        def captures(p=catchProbability, nInicial=No, value=v_captures):
            salida = 0
            nAux = nInicial + 0
            for iEvento in range(len(v_captures)):
                salida += binomial_like(x=value[iEvento], n=nAux, p=p[iEvento])
                nAux -= value[iEvento]
            return salida

        return locals()


def _find_quartil_hpd(archivo: str, porcentaje_datos_excluidos: float=0.95):
    # region Documentación
    ''' Función para encontrar el cuartil 2.5 y el Valor más probable del tamaño
    inicial de la población.

    # Parámetros
    `archivo str`

    Dirección del archivo donde se encuentra la distribución posterior de `No`.

    `porcentaje_datos_excluidos float`

    Porcentaje de los datos que no se va a considerar. `default=0.95`, esto quiere
    decir que solo se considera el 5% de los datos.
    '''
    # endregion
    datos: pd.DataFrame = pd.read_csv(archivo)
    intervalo = hpd(datos.No, alpha=porcentaje_datos_excluidos)
    return {"q": datos.No.quantile(q=0.025), "Vmp": intervalo.mean(), "max": intervalo.max(), "min": intervalo.min()}


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
    limite_inferior = np.array(
        range(x.min(), x.max() - min_interval_width + 2))
    limite_superior = limite_inferior + min_interval_width
    n_dentro = [((inferior <= x) & (x <= superior)).sum()
                for inferior, superior in zip(limite_inferior, limite_superior)]

    max_idx = np.argmax(n_dentro)
    hdi_min = limite_inferior[max_idx]
    hdi_max = limite_superior[max_idx]
    return hdi_min, hdi_max
