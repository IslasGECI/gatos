#!/usr/bin/env python
#
# Calcula el p valor de haber terminado la erradicación

from calculator_p_value import *
import json

datos_captura = pd.read_csv('inst/extdata/erradicaciones-mamiferos/captura_gatos_socorro.csv')
total_capturas = datos_captura.capturas.sum()

calculador = CalculatorPValue()
calculador.set_total_capturas(total_capturas)
calculador.read_posterior('resultados/distribucion_posterior_socorro.csv')
calculador.calculate_range_remanented_cats()
calculador.calculate_high_probability()
calculador.calculate_remanented_cat_more_probably()
calculador.probability()

diccionario_salida = {
    "gatos_capturados": int(total_capturas),
    "probabilidades": calculador.probabilidades.tolist(),
    "gatos_remanentes": int(calculador.remanented_cat_more_probably)
}
with open('reports/non-tabular/json_p-valor.json', 'w') as archivo:
    json.dump(diccionario_salida, archivo)