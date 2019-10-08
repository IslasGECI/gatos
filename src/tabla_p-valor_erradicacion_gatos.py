#!/usr/bin/env python
#
# Calcula el p valor de haber terminado la erradicación

import pandas as pd
import numpy as np
import json

datos_captura = pd.read_csv('inst/extdata/erradicaciones-mamiferos/captura_gatos_socorro.csv')
total_capturas = datos_captura.capturas.sum()

class CalculatorPValue:
    def __init__(self):
        pass

    def read_posterior(self, archivo):
        self.datos = pd.read_csv(archivo)
        self.remanented_cats = self.datos.No - self.capturas
    
    def set_total_capturas(self, capturas):
        self.capturas = capturas
        
    def calculate_range_remanented_cats(self):
        n_bins = max(self.datos.No.unique()) - min(self.datos.No.unique()) 
        self.hist, self.bins = np.histogram(self.remanented_cats, bins = n_bins)
    
    def calculate_high_probability(self):
        self.maximo = max(self.hist)
        self.indice_mas_probable = np.where(self.hist == self.maximo)[0]
        
    def calculate_remanented_cat_more_probably(self):
        self.remanented_cat_more_probably = self.bins[self.indice_mas_probable][0]
        
    def probability(self):
        hist, bin_edges = np.histogram(self.remanented_cats, 
                                       bins = [0, 1, self.remanented_cat_more_probably + 1, 10_000_000_000]
                                      )
        self.probabilidades = (hist/hist.sum())*100


calculador = CalculatorPValue()
calculador.set_total_capturas(total_capturas)
calculador.read_posterior('resultados/distribucion_posterior_socorro.csv')
calculador.calculate_range_remanented_cats()
calculador.calculate_high_probability()
calculador.calculate_remanented_cat_more_probably()
calculador.probability()

print(total_capturas)
print(calculador.probabilidades)
print(calculador.remanented_cat_more_probably)

diccionario_salida = {
    "gatos_capturados": int(total_capturas),
    "probabilidades": calculador.probabilidades.tolist(),
    "gatos_remanentes": int(calculador.remanented_cat_more_probably)
}
with open('json_p-valor.json', 'w') as archivo:
    json.dump(diccionario_salida, archivo)