# Programa encargado de generar el reporte en formato html de gatos en Socorro.

# region Se importan las librerías
import argparse
from jinja2 import Environment, PackageLoader, select_autoescape, Template
import json
import numpy as np
from datetime import datetime
import numpy as np
import pandas as pd
import time
import locale
from bokeh.embed import components
import bokeh.io as bi
import bokeh.models as bm
import bokeh.plotting as bp
import os

import gatos as dmc
import gatos.CredibleIntervals as ci
import gatos.bokeh_plots as g_bp
from bokeh.models import NumeralTickFormatter
import datatools
# endregion

# region Se declaran las variables a los archivos de datos

locale.setlocale(locale.LC_TIME, 'es-MX')

ap = argparse.ArgumentParser()
ap.add_argument("-r", "--resource", required=True,
                help="Nombre del recurso csv", type=str)
ap.add_argument("-o", "--output-file", required=True)
ap.add_argument(
    "-ippd", "--initial-population-posterior-distribution", required=True, type=str)
ap.add_argument("-posf", "--probability-of-success-file", required=True,
                type=str, nargs='+')
ap.add_argument("-rv", "--report-values", required=True,
                type=argparse.FileType('r'))
ap.add_argument('--espaniol', dest='es_espaniol', action='store_true')
ap.add_argument('--ingles', dest='es_espaniol', action='store_false')
ap.set_defaults(es_espaniol=True)
argumentos = vars(ap.parse_args())

directorio_resultados: str = 'resultados/'
# endregion

# region Se cargan los datos y se extraen algunos metadatos
Datos_captura_gatos = datatools.import_tabular_data_resource(argumentos["resource"])
distribuciones_posteriores: pd.DataFrame = pd.read_csv(
    argumentos["initial_population_posterior_distribution"])
distribucion_posterior_No: pd.Series = distribuciones_posteriores.No
nombre_esfuerzo: str = Datos_captura_gatos.get_variable_name_from_standard_name(datatools.StandardName.effort)
nombre_capturas: str = "capturas"
datos_probabilidad_captura = pd.read_csv(
    argumentos["probability_of_success_file"][0])
probabilidad = datos_probabilidad_captura.probabilidad.values
esfuerzo_trampas = datos_probabilidad_captura.esfuerzo_capturas.values
remanentes_capturados = datos_probabilidad_captura.remanentes_capturados.values
datos_derivada_captura = pd.read_csv(
    argumentos["probability_of_success_file"][1])
derivada = datos_derivada_captura.derivada.values
esfuerzo_para_derivada = datos_derivada_captura.esfuerzo_derivada.values
valores_reporte = json.load(argumentos["report_values"])
# endregion

# region Se encuentran los valores de interes
esfuerzo: np.array = np.array(Datos_captura_gatos.get_value(nombre_esfuerzo))
capturas: np.array = np.array(Datos_captura_gatos.get_value(nombre_capturas))
capturas_por_esfuerzo = capturas / esfuerzo
capturas_acumuladas = capturas.cumsum()
esfuerzo_acumulado = esfuerzo.cumsum()
distribucion_gatos_remanentes: np.array = distribucion_posterior_No.values - \
    valores_reporte["total_capturas"]
# endregion

# region gráfica captura_remanentes

# Encontramos el esfuerzo necesario para erradicar el 95% del total de gatos remanentes
id_min = len(probabilidad) - (probabilidad > 0.025).sum()
id_max = len(probabilidad) - (probabilidad > 0.975).sum()
intervalo_probabilidad_terminar_remanentes = [
    (esfuerzo_trampas[id_min] + esfuerzo_trampas[id_min+1])/2, (esfuerzo_trampas[id_max]+esfuerzo_trampas[id_max+1])/2]

# Cada trampero utiliza 30 trampas y la expedición dura 25 días
trampero_por_expedicion = 30*25
graficas_capturas_gatos_remanentes = g_bp.RemanentCatCatchesPlotter(
    esfuerzo_trampas/trampero_por_expedicion, remanentes_capturados, derivada*trampero_por_expedicion, esfuerzo_para_derivada/trampero_por_expedicion)
graficas_capturas_remanentes = graficas_capturas_gatos_remanentes.show_remanent_catch_effort_plots()
# endregion

# region cdf_exito_erradicacion
grafica_cdf_exito_erradicacion = bp.figure(x_axis_label="Effort (trap∙nights)", y_axis_label='Probability of succes',
                                           y_range=(0, 1), x_range=(0, 100000))
grafica_cdf_exito_erradicacion.grid.visible = False

margen_del_eje_y = 1000
margen_del_eje_x = 0.01
margen_linea_y = 0.05
margen_linea_x = 8000
grafica_cdf_exito_erradicacion.line(
    esfuerzo_trampas, probabilidad, line_width=3, color=g_bp.AZUL_GECI)
grafica_cdf_exito_erradicacion.line([0, valores_reporte["esfuerzo_trampas_mayor_95"]], [
                                    0.95, 0.95], line_width=3, line_color="#D95B43")
grafica_cdf_exito_erradicacion.line([valores_reporte["esfuerzo_trampas_mayor_95"], valores_reporte["esfuerzo_trampas_mayor_95"]], [
                                    0, 0.95], line_width=3, line_color="#D95B43")
grafica_cdf_exito_erradicacion.text(x=[margen_del_eje_y], y=[
                                    0.95-0.1], text=["0.95"], text_color='black', text_font_size="16pt")
grafica_cdf_exito_erradicacion.text(x=[valores_reporte["esfuerzo_trampas_mayor_95"]-13000], y=[margen_del_eje_x+0.001], text=[
                                    f"{np.ceil(valores_reporte['esfuerzo_trampas_mayor_95']/1000)*1000:0.0f}"], text_color='black', text_font_size="16pt")

g_bp.set_plot_format(grafica_cdf_exito_erradicacion)
bi.export_png(grafica_cdf_exito_erradicacion,
              filename=directorio_resultados+"cdf_exito_erradicacion.png")
# endregion

# region pdf_exito_erradicacion
dt = 20
derivada = np.array(probabilidad[0:-1:dt])
derivada[1:] -= derivada[:-1].copy()
esfuerzo_trampas_menor_paso = esfuerzo_trampas[0:-1:dt]  # Cambio de paso

vmp_derivada_para_grafica = derivada.max()
vmp_esfuerzo_para_grafica = esfuerzo_trampas_menor_paso[derivada >=
                                                        derivada.max()][0]

indice_min_derivada = int(np.floor(id_min/20))+1
indice_max_derivada = int(np.floor(id_max/20))+1

grafica_pdf_exito_erradicacion = bp.figure(x_axis_label='Effort (trap∙nights)', y_axis_label='Probability', y_range=(0, 0.12))
grafica_pdf_exito_erradicacion.vbar(
    x=esfuerzo_trampas_menor_paso, top=derivada,  bottom=0, width=1800, fill_color=g_bp.AZUL_GECI)
grafica_pdf_exito_erradicacion.vbar(x=esfuerzo_trampas_menor_paso[:indice_min_derivada], top=derivada[:indice_min_derivada],
                                    bottom=0, width=1800, fill_color=g_bp.VERDE_GECI, line_color=g_bp.VERDE_GECI)
grafica_pdf_exito_erradicacion.vbar(x=esfuerzo_trampas_menor_paso[indice_max_derivada:], top=derivada[indice_max_derivada:],
                                    bottom=0, width=1800, fill_color=g_bp.VERDE_GECI, line_color=g_bp.VERDE_GECI)
grafica_pdf_exito_erradicacion.grid.visible = False

grafica_pdf_exito_erradicacion.xaxis.formatter = NumeralTickFormatter(
    format="0,0")

grafica_pdf_exito_erradicacion.line([vmp_esfuerzo_para_grafica, vmp_esfuerzo_para_grafica], [
    0, vmp_derivada_para_grafica], line_width=5, line_color="DarkOrange")
g_bp.set_plot_format(grafica_pdf_exito_erradicacion)
bi.export_png(grafica_pdf_exito_erradicacion,
              filename=directorio_resultados+"pdf_exito_erradicacion.png")
# endregion

# region crea instancias de los graficadores
Graficador_capturas_esfuerzo: g_bp.CatchPerEffortPlotter = g_bp.CatchPerEffortPlotter(
    esfuerzo_acumulado, capturas_acumuladas, capturas_por_esfuerzo)
Graficador_estado_gatos: g_bp.RemanentCatPlotter = g_bp.RemanentCatPlotter(
    distribucion_posterior_No, valores_reporte["total_capturas"], valores_reporte["vmp_gatos_remanentes"], np.array(valores_reporte["intervalo_gatos_remanentes"]))
grafica_exito_erradicacion = bp.gridplot(
    [[grafica_pdf_exito_erradicacion, grafica_cdf_exito_erradicacion]], toolbar_options={'logo': None})
# endregion

# region Se crea el reporte con las gráficas
nombre_template_reporte: str = "template.html"
nombre_reporte_salida: str = "entrega/erradicacion_gatos_socorro.html"
configuracion_jinja: Environment = Environment(
    loader=PackageLoader('gatos', 'templates'),
    autoescape=select_autoescape(['html'])
)
configuracion_jinja.filters['commafy'] = lambda v: "{:,}".format(v)
template: Template = configuracion_jinja.get_template(nombre_template_reporte)
# endregion

# region crea los componentes de las gráficas
script_grafica_captura_por_esfuerzo, div_grafica_captura_por_esfuerzo = components(
    Graficador_capturas_esfuerzo.show_catch_effort_plots())
script_pdf, pdf = components(Graficador_estado_gatos.get_cat_status_plots())
script_grafica_exito_erradicacion, div_grafica_exito_erradicacion = components(
    grafica_exito_erradicacion)
script_grafica_capturas_remanentes, div_grafica_capturas_remanentes = components(
    graficas_capturas_remanentes)
# endregion

datos_reporte = {"titulo": "Erradicación de Gato Feral en Isla Socorro",
                 "fecha": datetime.now().strftime("%d de %B, %Y")}

with open(argumentos["output_file"], mode='w', encoding='utf-8') as reporte_html:

    html_generado: str = template.render(script_grafica_capturas_remanentes=script_grafica_capturas_remanentes, div_grafica_capturas_remanentes=div_grafica_capturas_remanentes,
                                         datos_reporte=datos_reporte, script_pdf=script_pdf, pdf=pdf, estado_gatos=valores_reporte,
                                         script_grafica_captura_por_esfuerzo=script_grafica_captura_por_esfuerzo, div_grafica_captura_por_esfuerzo=div_grafica_captura_por_esfuerzo,
                                         script_grafica_exito_erradicacion=script_grafica_exito_erradicacion, div_grafica_exito_erradicacion=div_grafica_exito_erradicacion,
                                         es = argumentos["es_espaniol"])

    reporte_html.write(html_generado)
# endregion
