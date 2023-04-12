import click

# Programa para crear `json`` del tamaño de la población a partir de archivos
# que contienen las distribuciones posteriores.

import numpy as np  # type: ignore
import pandas as pd


from gatos.PopulationEstimator import PopulationEstimator
import metadatatools  # type: ignore


# @click.group(cls=DefaultGroup, default="create", default_if_no_args=True)
@click.group()
def cli():
    pass


@cli.command(short_help="Cálcula la distribución posterior para el tamaño de la población inicial")
@click.option("--resource", "-r", type=click.Path(), help="Nombre del recurso csv")
@click.option("--output-file", "-o", type=click.Path(), help="Nombre del archivo de salida csv")
@click.option("--iterations", "-i", default=1_000_000, type=int, help="Número de iteraciones")
@click.option("--datapackage", "-d", default=True, type=bool, help="Read data from datapackage")
def calculate(**argumentos):
    run_population_estimator(argumentos)


def run_population_estimator(argumentos):
    trapps_per_person = 30
    number_of_trappers = 7
    working_days = 5
    man_days = trapps_per_person * number_of_trappers * working_days
    if argumentos["datapackage"]:
        esfuerzo, capturas = get_effort_and_captures_with_datapackage(argumentos, man_days)
    else:
        esfuerzo, capturas = get_effort_and_captures_without_datapackage(argumentos, man_days)

    # Se busca el tamaño de la población
    iteraciones = argumentos["iterations"]
    estimador_poblacion_inicial: PopulationEstimator = PopulationEstimator(
        esfuerzo, capturas, argumentos["output_file"]
    )
    estimador_poblacion_inicial.run(
        iteraciones=iteraciones,
        n_datos_descartados=int(np.ceil(iteraciones * 0.1)),
    )
    estimador_poblacion_inicial.run_model_diagnostics()


def get_effort_and_captures_without_datapackage(argumentos, man_days):
    monthly_summary = pd.read_csv(argumentos["resource"])
    esfuerzo = monthly_summary.Esfuerzo.to_numpy() / man_days
    capturas = monthly_summary.Capturas.to_numpy()
    return esfuerzo, capturas


def get_effort_and_captures_with_datapackage(argumentos, man_days):
    DatosSocorro = metadatatools.import_tabular_data_resource(argumentos["resource"])
    nombre_esfuerzo: str = "Esfuerzo"
    nombre_capturas: str = "Capturas"
    esfuerzo: np.array = np.array(DatosSocorro.get_value(nombre_esfuerzo) / man_days)
    capturas: np.array = np.array(DatosSocorro.get_value(nombre_capturas))
    return esfuerzo, capturas
