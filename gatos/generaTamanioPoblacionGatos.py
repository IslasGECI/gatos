import click
from click_default_group import DefaultGroup

# Programa para crear `json`` del tamaño de la población a partir de archivos
# que contienen las distribuciones posteriores.

import numpy as np


from gatos.PopulationEstimator import PopulationEstimator
import metadatatools


@click.group(cls=DefaultGroup, default="create", default_if_no_args=True)
def cli():
    pass


def calculate(**argumentos): 
    DatosSocorro = datatools.import_tabular_data_resource(argumentos["resource"])
    nombre_esfuerzo: str = DatosSocorro.get_variable_name_from_standard_name(datatools.StandardName.effort)
    nombre_capturas: str = "capturas"
    esfuerzo: np.array = np.array(DatosSocorro.get_value(
        nombre_esfuerzo)/(30 * 7 * 5))  # Días persona: 30 trampas, 7 personas, 5 días
    capturas: np.array = np.array(DatosSocorro.get_value(nombre_capturas))

    # region Se busca el tamaño de la población
    repeticiones = 3
    iteraciones = argumentos["iterations"]
    estimador_poblacion_inicial: PopulationEstimator = PopulationEstimator(
        esfuerzo, capturas, argumentos["output_file"]
    )
    estimador_poblacion_inicial.run(
        repeticiones=repeticiones, iteraciones=iteraciones, n_datos_descartados=iteraciones * 0.1
    )
