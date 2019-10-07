import clases.RemoveCats as rc
import numpy as np
import pandas as pd

nIntentos = 10
alfa = np.random.normal(-5.175, .01, nIntentos)
beta = np.random.normal(0.575, .01, nIntentos)
esfuerzo = np.random.uniform(2, 6, nIntentos)
vector_probabilidad = rc.calculateProbabilityFromAlphaBetaEffort(alfa, beta, esfuerzo)        
probabilidadEmpirica = rc.CalculaProbabilidadEmpirica(vector_probabilidad)
tamanoPoblacion = 47        
gatosRemovidos = rc.getRemovedCats(tamanoPoblacion,probabilidadEmpirica,nIntentos)
resultado = pd.DataFrame({"esfuerzo":esfuerzo, "capturas": gatosRemovidos})
resultado.to_csv("nepo.csv", index=False)
