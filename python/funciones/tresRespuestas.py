"""
>>> tamanoPoblacion = PoblacionInicial(573)
>>> getRemainentCats(tamanoPoblacion,20,.9)
496

>>> tamanoPoblacion = IntervaloPoblacionInicial(509,64)
>>> getRemainentCats(tamanoPoblacion,20,.9)
496
"""
# Importa paqueterías necesarias
import numpy as np
import math

# Crea función para determinar los individuos que faltan para llegar al 90%
# del tamaño de la población. El primer argumento de entrada es un objeto que
# tiene el método maxPopulation; el segundo y tercer argumento son escalares
def getRemainentCats(tamanoPoblacionInicial,individuosRetirados,porcentajeDeCambio):
    individuosRemantentes = math.ceil(tamanoPoblacionInicial.maxPopulation()*porcentajeDeCambio-individuosRetirados)
    return individuosRemantentes

# Crea clase que obtiene el tamaño de la población a partir de su valor puntual.
# En este caso la función maxPopulation regresa el mismo valor
class PoblacionInicial:
    def __init__(self,tamanoPoblacionInicial):
        self.tamanoPoblacionInicial = tamanoPoblacionInicial

    def maxPopulation(self):
        return self.tamanoPoblacionInicial

# Crea clase que obtiene los límites del intervalo de confianza a partir de
# el valor medio y el margen de error. La función maxPopulation regresa como 
# salida los límites superior.
class IntervaloPoblacionInicial:
    def __init__(self,valorCentral,margenError):
        self.valorCentral = valorCentral
        self.margenError = margenError

    def maxPopulation(self):
        limiteSuperior = self.valorCentral + self.margenError
        limiteInferior = self.valorCentral - self.margenError
        return limiteSuperior

if __name__ == "__main__":
    import doctest
    doctest.testmod()