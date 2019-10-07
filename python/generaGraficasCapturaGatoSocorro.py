# Programa para crear las Series de tiempo de capturas y las graficas de capturas
# en función del esfuerzo acumulado, de gato feral en Isla Socorro.

# region Se importan las librerías 

import pandas as pd
from clases.DataAndMetadataCats import DataAndMetadataCats
from funciones import cat_plots
import matplotlib.pyplot as plt
import datatools
# endregion

# region Se cargan los datos y se crean las variables que se van a graficar 

carpeta_data_package: str = "./inst/extdata/erradicaciones-mamiferos/"
carpeta_resultados: str = "./resultados/"
nombre_archivo: str = 'captura_gatos.csv'

GatosConMetadatos: DataAndMetadataCats = DataAndMetadataCats(carpeta_data_package, nombre_archivo)
nombre_columna_esfuerzo: str = GatosConMetadatos.glosario['esfuerzo']
nombre_columna_capturas: str = GatosConMetadatos.glosario['capturas']
datos_gatos: pd.DataFrame = GatosConMetadatos.getData()

captura_por_esfuerzo: pd.Series = datos_gatos[nombre_columna_capturas].values / datos_gatos[nombre_columna_esfuerzo].values
capturas_acumuladas: pd.Series = datos_gatos[nombre_columna_capturas].cumsum()
esfuerzo_acumulado: pd.Series = datos_gatos[nombre_columna_esfuerzo].cumsum()

# endregion

# region Se crean las gráficas 
plt.figure(figsize=(10, 5))
cat_plots.plot_time_serie_captures_per_effort(datos_gatos.tiempo_listo, captura_por_esfuerzo)
plt.ylim([0.0, 0.1])
plt.savefig(carpeta_resultados + "catch-per-unit-effort_time-serie.png")
plt.clf()

cat_plots.plot_time_serie_cumulative_captures(datos_gatos.tiempo_listo, capturas_acumuladas)
plt.ylim([0.0, 650])
plt.savefig(carpeta_resultados + "accumulated-catch_time-serie.png")
plt.clf()

cat_plots.plot_cumulative_effort_vs_cumulative_captures(esfuerzo_acumulado, capturas_acumuladas)
plt.ylim([0.0, 650])
plt.savefig(carpeta_resultados + "accumulated-catch_accumulated-effort.png")
plt.clf()

cat_plots.plot_cumulative_effort_vs_captures_per_effort(esfuerzo_acumulado, captura_por_esfuerzo)
plt.ylim([0.0, 0.1])
plt.savefig(carpeta_resultados + "catch-per-unit-effort_accumulated-effort.png")
plt.clf()
# endregion