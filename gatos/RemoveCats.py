import numpy as np

def getRemovedCats(tamanoPoblacion,ProbabilidadCaptura,nIntentos):
    capturas = []
    auxiliarTamanoPoblacion = tamanoPoblacion
    for iIntento in range(nIntentos):
        capturas.append(np.random.binomial(auxiliarTamanoPoblacion,ProbabilidadCaptura.findProbability()))
        auxiliarTamanoPoblacion -= capturas[iIntento]
    return np.array(capturas)

def calculateProbabilityFromAlphaBetaEffort(alpha: np.array, beta: np.array, esfuerzo: np.array):
    vectorProbabilidad = np.exp(alpha + beta * esfuerzo)/(1 + np.exp(alpha + beta * esfuerzo))
    return vectorProbabilidad

class CalculaProbabilidadFija:
    def __init__(self,probabilidad):
        self.probabilidad = probabilidad

    def findProbability(self):
        return self.probabilidad

class CalculaProbabilidadAleatoria:
    def __init__(self,nIntentos: int):
        self.probabilidad: np.array = np.random.rand(nIntentos)
        self.iIntento = 0

    def findProbability(self):
        self.iIntento += 1
        return self.probabilidad[self.iIntento - 1]

class CalculaProbabilidadEmpirica:
    def __init__(self,vectorProbabilidad):
        self.probabilidad = vectorProbabilidad
        self.iIntento = 0

    def findProbability(self):
        self.iIntento += 1
        return self.probabilidad[self.iIntento - 1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()