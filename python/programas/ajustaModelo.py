import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os

import toolboxes
archivoDatos = toolboxes.findInDataPath("erradicacion-cabra-feral-Nov04-May05.xlsx")
datos = pd.read_excel(archivoDatos)

# Función para corregir el formato de las fechas
def dateNumber2Date(fecha): 
    # Representación de la fecha en cadena
    fechaStr = str(fecha)
    dia = fechaStr[:2]
    mes = fechaStr[2:4]
    anio = fechaStr[4:]    
    return "-".join([dia,mes,anio]) 
# Se corrige el formato de las fechas
funcionAcomodarFecha = lambda f: dateNumber2Date(f)
datos["Fecha"] = pd.to_datetime(datos["Fecha"].map(funcionAcomodarFecha))

# Función para filtrar los datos por año
filtroDatosPorAnio = lambda y: (datos["Fecha"] > "{}-01-01".format(y)) & (datos["Fecha"] < "{}-12-31".format(y))
# Suma acumulada de los datos del 2004
blancosAcumulados = datos.loc[filtroDatosPorAnio(2004), "Blancos"].cumsum()
# A los blancosAcumulados se agregan los datos del 2005 
blancosAcumulados = blancosAcumulados.append(datos.loc[filtroDatosPorAnio(2005), "Blancos"].cumsum() + blancosAcumulados.max())
# Hace el mismo ajuste para la variable independiente (horas de vuelo)
datos.loc[filtroDatosPorAnio(2005), "Tiempo hrs (acum)"] = datos.loc[filtroDatosPorAnio(2005), "Tiempo hrs (acum)"] + datos.loc[filtroDatosPorAnio(2004), "Tiempo hrs (acum)"].max()

class ModeloExponencialTamanoPoblacion:
    
    def fit(self,esfuerzo,individuosCapturados):
        self.esfuerzo = esfuerzo
        self.individuosCapturados = individuosCapturados
        self.media, self.desplazamiento, self.tamanoPoblacion = curve_fit(self.ModeloConConstante, esfuerzo, individuosCapturados, p0=[1,1,1])[0]

    # Función bla bla
    def getPopulationSize(self):
        return self.tamanoPoblacion

    # Función cdf exponencial que se ajustará a los datos
    def ModeloConConstante(self,x, media, desplazamiento,constante):
        return (1-np.exp(-(x-desplazamiento)/media))*constante

    def predict(self,variableIndependiente):
        variableDependiente = self.ModeloConConstante(variableIndependiente,self.media,self.desplazamiento,self.tamanoPoblacion)
        return variableDependiente

modeloExponencial = ModeloExponencialTamanoPoblacion()
modeloExponencial.fit(datos["Tiempo hrs (acum)"], blancosAcumulados)
modeloExponencial.getPopulationSize()

horasVuelo = np.linspace(datos["Tiempo hrs (acum)"].min(), datos["Tiempo hrs (acum)"].max(), 1000)
capturasAcumuladasPredichas = modeloExponencial.predict(horasVuelo)

plt.figure(figsize=(10,6))
# Modelo
plt.plot(horasVuelo, capturasAcumuladasPredichas, color="blue", alpha=0.5)
# Datos
plt.plot(datos["Tiempo hrs (acum)"], blancosAcumulados, 'k')
plt.xlabel("Horas de vuelo acumuladas")
plt.ylabel("Blancos acumulados")

if not "resultados" in os.listdir("../../"):
    os.mkdir("../../resultados")
plt.tight_layout()
plt.savefig("../../resultados/modelo_cdf_ajustado_blancos_acumulados.png")