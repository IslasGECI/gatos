import click
from click_default_group import DefaultGroup

from gatos.calculator_p_value import *
import json

@click.group(cls=DefaultGroup, default="create", default_if_no_args=True)
def cli():
    pass

# region Se cargan los datos y se extraen los datos de interes
# Se guarda una referencia a la carpeta de resultados
@cli.command(short_help="Programa para generar los parámetros utilizados en el reporte de gatos")
@click.option("--resource", "-r", type=click.Path(),
    help="Nombre del recurso csv")
@click.option("--posterior", "-p", type=click.Path(),
    help="Ruta del archivo csv de las posteriores")
@click.option("--output-file", "-o", type=click.Path(),
    help="Nombre del archivo de salida csv")
def calculate(**argumentos):
    datos_captura = pd.read_csv(argumentos["resource"])
    total_capturas = datos_captura.capturas.sum()

    calculador = CalculatorPValue()
    calculador.set_total_capturas(total_capturas)
    calculador.read_posterior(argumentos["posterior"])
    calculador.calculate_range_remanented_cats()
    calculador.calculate_high_probability()
    calculador.calculate_remanented_cat_more_probably()
    calculador.probability()

    diccionario_salida = {
        "gatos_capturados": int(total_capturas),
        "probabilidades": calculador.probabilidades.tolist(),
        "gatos_remanentes": int(calculador.remanented_cat_more_probably)
    }
    with open(argumentos["output_file"], 'w') as archivo:
        json.dump(diccionario_salida, archivo)