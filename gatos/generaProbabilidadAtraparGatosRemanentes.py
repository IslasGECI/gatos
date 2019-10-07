import click
from click_default_group import DefaultGroup
import pandas as pd
import numpy as np
import gatos as dmc
from gatos.CatchEffortSimulator import CatchEffortSimulator
import datatools

@click.group(cls=DefaultGroup, default="create", default_if_no_args=True)
def cli():
    pass

# region Se cargan los datos y se extraen los datos de interes
# Se guarda una referencia a la carpeta de resultados
@cli.command(short_help="Cálcula la probabilidad de captura de gatos remanentes")
@click.option("--resource", "-r", type=click.Path(),
    help="Nombre del recurso csv")
@click.option("--initial-population-posterior-distribution", "-ippd", type=click.Path(),
    help="Dirección de la distribución posterior de la población inicial csv")
@click.option("--output-file", "-o", type=click.Path(),
    help="Nombre del archivo de salida csv")
def remanent_cats(**argumentos): 
    #directorio_resultados: str = 'resultados/'
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
        argumentos["output_file"])

@cli.command(short_help="Cálcula la derivada de las captura con respecto al esfuerzo")
@click.option("--resource", "-r", type=click.Path(),
    help="Nombre del recurso csv")
@click.option("--initial-population-posterior-distribution", "-ippd", type=click.Path(),
    help="Dirección de la distribución posterior de la población inicial csv")
@click.option("--output-file", "-o", type=click.Path(),
    help="Nombre del archivo de salida csv")
def derivate_effort(**argumentos): 
    #directorio_resultados: str = 'resultados/'
    Datos_captura_gatos = datatools.import_tabular_data_resource(argumentos["resource"])
    distribuciones_posteriores: pd.DataFrame = pd.read_csv(
        argumentos["initial_population_posterior_distribution"])

    nombre_capturas: str = "capturas"
    total_capturas: int = np.array(
        Datos_captura_gatos.get_value(nombre_capturas)).sum()
    simulador_esfurzo_captura: CatchEffortSimulator = CatchEffortSimulator(
        distribuciones_posteriores, total_capturas)
    simulador_esfurzo_captura.run()
    simulador_esfurzo_captura.makeDerivate()
    simulador_esfurzo_captura.saveDerivateAndEffort_to_derivate(
        argumentos["output_file"])