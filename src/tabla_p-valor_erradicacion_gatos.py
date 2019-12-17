#!/usr/bin/env python
#
# Calcula el p valor de haber terminado la erradicación

from calculator_p_value import *
import json
from cliRutaArchivoEntradaSalida import ruta_archivos

rutas = ruta_archivos()

datos_captura = pd.read_csv(f'{rutas.entrada[0][0]}')
total_capturas = datos_captura.capturas.sum()

calculador = CalculatorPValue()
calculador.set_total_capturas(total_capturas)
calculador.read_posterior(f'{rutas.entrada[1][0]}')
calculador.calculate_range_remanented_cats()
calculador.calculate_high_probability()
calculador.calculate_remanented_cat_more_probably()
calculador.probability()

print("El total de capturas es: ",total_capturas)
print("Probabilidades: ",calculador.probabilidades)
print("Gatos remanentes mas probable: ",calculador.remanented_cat_more_probably)

diccionario_salida = {
    "gatos_capturados": int(total_capturas),
    "probabilidades": calculador.probabilidades.tolist(),
    "gatos_remanentes": int(calculador.remanented_cat_more_probably)
}
with open(f"{rutas.salida[0][0]}", 'w') as archivo:
    json.dump(diccionario_salida, archivo)