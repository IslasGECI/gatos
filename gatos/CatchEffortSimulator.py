import numpy as np
import pandas as pd

class CatchEffortSimulator:
    def __init__(self, distribuciones_posteriores: pd.DataFrame, total_capturas: int):
        self._probabilidad = []
        self._remanentes_capturados = []
        self._Df = np.array([])
        self._esfuerzo_graficar = np.array([])
        self._distribuciones_posteriores = distribuciones_posteriores
        self._total_capturas = total_capturas  
        _esfuerzo_dias_hombre = 5 * 30 * 7
        self._esfuerzo_trampas =  np.array(range(1,1001,1))*0.1 * _esfuerzo_dias_hombre      

    @property
    def probability(self):
        if self._total_capturas is None:
            # TODO Lanzar un error
            pass
        return self._probabilidad

    @property
    def remanent_cats(self):
        if self._total_capturas is None:
            # TODO Lanzar un error
            pass
        return self._remanentes_capturados

    @property
    def derivate(self):
        if self._total_capturas is None:
            # TODO Lanzar un error
            pass
        return self._Df

    @property
    def effort_to_derivate(self):
        if self._total_capturas is None:
            # TODO Lanzar un error
            pass
        return self._esfuerzo_graficar

    def run(self, muestra:int=100_000):
        ''' Método que corre la simulación, este se debe llamar
        antes de utilizar las propiedades `probability` y `remanent_cats` o
        lanzará un error.

        # Argumentos
        `muestra int`

        Número de muestras que se toman de la distribución posterior. '''
        columnas_DataFrame = self._distribuciones_posteriores.columns
        assert ("No" in columnas_DataFrame and "a" in columnas_DataFrame and "b" in columnas_DataFrame), "Se espera que la distribución posterior tenga los valores de No, a y b."
        for iEsfuerzo in range(1,1160):
            No = self._distribuciones_posteriores.No.sample(n=muestra, replace=True).values.astype(np.int32) - self._total_capturas
            beta = self._distribuciones_posteriores.b.sample(n=muestra, replace=True).values
            alpha = self._distribuciones_posteriores.a.sample(n=muestra, replace=True).values
            esfuerzo = iEsfuerzo * 0.1
            exp = np.exp(alpha + beta * esfuerzo)
            p = exp/(1+exp)
            individuos_capturados = np.random.binomial(No, p)
            self._probabilidad.append(1 - sum(individuos_capturados < No)/muestra)
            self._remanentes_capturados.append(np.mean(individuos_capturados))
        self._probabilidad = np.array(self._probabilidad)
        self._remanentes_capturados = np.array(self._remanentes_capturados)

    def makeDerivate(self, ventana: int = 20):        
        remanentes_derivar =np.convolve(self._remanentes_capturados, np.ones((ventana,))/ventana, mode='valid')
        esfuerzo_graficar = np.convolve(self._esfuerzo_trampas, np.ones((ventana,))/ventana, mode='valid')
        self._esfuerzo_graficar = (esfuerzo_graficar[:-1] + esfuerzo_graficar[1:])/2
        df = np.diff(remanentes_derivar)
        dx = self._esfuerzo_graficar[1] - self._esfuerzo_graficar[0]
        self._Df = df/dx

    def saveProbabilityAndRemanent_cats(self, nombre_salida: str):
        diccionario_auxiliar : dict = {
            "probabilidad": self.probability, 
            "remanentes_capturados": self.remanent_cats,
            "esfuerzo_capturas": self._esfuerzo_trampas
        }
        self.saveDictToCSV(diccionario_auxiliar, nombre_salida)

    def saveDerivateAndEffort_to_derivate(self, nombre_salida: str):
        diccionario_auxiliar : dict = {
            "derivada": self.derivate, 
            "esfuerzo_derivada": self.effort_to_derivate
        }
        self.saveDictToCSV(diccionario_auxiliar, nombre_salida)

    def saveDictToCSV(self, diccionario : dict, nombre_salida : str):
        dataframe_auxiliar : pd.DataFrame = pd.DataFrame(diccionario)
        dataframe_auxiliar.to_csv(nombre_salida, index=False)