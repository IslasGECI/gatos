import click
from click_default_group import DefaultGroup  # type: ignore

# Programa para crear `json`` del tamaño de la población a partir de archivos
# que contienen las distribuciones posteriores.

import numpy as np  # type: ignore


from gatos.PopulationEstimator import PopulationEstimator
import metadatatools  # type: ignore


@click.group(cls=DefaultGroup, default="create", default_if_no_args=True)
def cli():
    pass


@cli.command(short_help="Cálcula la distribución posterior para el tamaño de la población inicial")
@click.option("--resource", "-r", type=click.Path(), help="Nombre del recurso csv")
@click.option("--output-file", "-o", type=click.Path(), help="Nombre del archivo de salida csv")
@click.option("--iterations", "-i", default=1_000_000, type=int, help="Número de iteraciones")
def calculate(**argumentos):
    DatosSocorro = metadatatools.import_tabular_data_resource(argumentos["resource"])
    nombre_esfuerzo: str = "Esfuerzo"
    nombre_capturas: str = "Capturas"
    esfuerzo: np.array = np.array(
        DatosSocorro.get_value(nombre_esfuerzo) / (30 * 7 * 5)
    )  # Días hombre: 30 trampas, 7 tramperos, 5 días
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
