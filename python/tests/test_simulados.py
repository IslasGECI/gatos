import unittest
import os
import sys
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..\clases")))
import RemoveCats as rc

class SimuladorTest(unittest.TestCase):
    def setUp(self):
        self.nIntentos = 15  
        self.tamanoPoblacion = 1000  
        np.random.seed(0)

    def test_probabilidadFija(self):             
        probabilidadFija = rc.CalculaProbabilidadFija(0.1)
        nIntentos = len(rc.getRemovedCats(self.tamanoPoblacion, probabilidadFija, self.nIntentos))
        self.assertEqual(self.nIntentos, nIntentos)

    def test_gatosRemovidosProbabilidadFijaMenorAPoblacionInicial(self):
        probabilidadFija = rc.CalculaProbabilidadFija(0.1)
        gatosRemovidos = rc.getRemovedCats(self.tamanoPoblacion, probabilidadFija, self.nIntentos)
        self.assertLessEqual(sum(gatosRemovidos), self.tamanoPoblacion)

    def test_gatosRemovidosProbabilidadAleatoriaMenorAPoblacionInicial(self):
        probabilidadAleatoria = rc.CalculaProbabilidadAleatoria(self.nIntentos)
        gatosRemovidos = rc.getRemovedCats(self.tamanoPoblacion, probabilidadAleatoria, self.nIntentos)
        self.assertLessEqual(sum(gatosRemovidos), self.tamanoPoblacion)

    def test_pruebaNepo(self):
        nIntentos = 10
        alfa = np.random.normal(-5.175, .01, nIntentos)
        beta = np.random.normal(0.575, .01, nIntentos)
        esfuerzo = np.random.uniform(2, 6, nIntentos)
        vector_probabilidad = rc.calculateProbabilityFromAlphaBetaEffort(alfa, beta, esfuerzo)        
        probabilidadEmpirica = rc.CalculaProbabilidadEmpirica(vector_probabilidad)
        tamanoPoblacion = 47        
        gatosRemovidos = rc.getRemovedCats(tamanoPoblacion,probabilidadEmpirica,nIntentos)
        print(gatosRemovidos)
        self.assertLessEqual(sum(gatosRemovidos), tamanoPoblacion)
