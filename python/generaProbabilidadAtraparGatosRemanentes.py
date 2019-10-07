import argparse
import pandas as pd
import numpy as np
import os
import gatos as dmc
from gatos.CatchEffortSimulator import CatchEffortSimulator
import datatools

ap = argparse.ArgumentParser()
ap.add_argument("-r", "--resource", required=True,
                help="Nombre del recurso csv", type=str)
ap.add_argument("-ippd", "--initial-population-posterior-distribution",
                default="distribucion_posterior.csv")
ap.add_argument("-o", "--output-file", required=True,
                type=str, nargs='+')
argumentos = vars(ap.parse_args())

directorio_resultados: str = 'resultados/'
Datos_captura_gatos = datatools.import_tabular_data_resource(argumentos["resource"])
distribuciones_posteriores: pd.DataFrame = pd.read_csv(
    argumentos["initial_population_posterior_distribution"])

nombre_capturas: str = "capturas"
total_capturas: int = np.array(
    Datos_captura_gatos.get_value(nombre_capturas)).sum()
simulador_esfurzo_captura: CatchEffortSimulator = CatchEffortSimulator(
    distribuciones_posteriores, total_capturas)
simulador_esfurzo_captura.run()
simulador_esfurzo_captura.saveProbabilityAndRemanent_cats(
    argumentos["output_file"][0])
simulador_esfurzo_captura.makeDerivate()
simulador_esfurzo_captura.saveDerivateAndEffort_to_derivate(
    argumentos["output_file"][1])
