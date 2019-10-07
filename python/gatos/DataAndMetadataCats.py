import pandas as pd
import numpy as np
import json


class DataAndMetadataCats(object):
    ''' Clase encargada de cargar los datos de erradicación de mamíferos.
    '''

    def __init__(self, direccion_datapackage: str, datos_csv: str):
        direccion_datos = f"{direccion_datapackage}/{datos_csv}"
        self._datos = pd.read_csv(direccion_datos)
        direccion_metadatos = direccion_datapackage + "/datapackage.json"
        metadatos = pd.read_json(direccion_metadatos)
        self.set_resource(metadatos, datos_csv)
        self.set_glossary()
        self.set_time_ready()

    def set_glossary(self):
        ''' Método encargado de generar un diccionario con el nombre de las columnas de interés.

        # Parámetros

        '''
        tiempo: str = self.get_name_from_axis('T')
        capturas: str = self.get_name_from_standardname('captures')
        esfuerzo: str = self.get_name_from_axis('E')
        self.glosario: dict = {"tiempo": tiempo,
                               "capturas": capturas, "esfuerzo": esfuerzo}

    def set_resource(self, metadatos, nombre):
        recursos = metadatos.resource
        indice = 0
        for iRecurso in recursos:
            if iRecurso['data'] == [nombre]:
                indiceInteres = indice
            indice += 1
        self.metadatos = metadatos.resource[indiceInteres]

    def set_time_ready(self):
        tiempo: str = self.glosario["tiempo"]
        self._datos["tiempo_listo"] = pd.to_datetime(self._datos[tiempo])

    def get_data(self):
        return self._datos

    def get_name_from_axis(self, eje: str):
        ''' Método encargado de obtener el nombre de una columna a partir de la etiqueta del eje.

        # Parámetros
        `eje str`

        '''
        columnas = self.metadatos['schema']['fields']
        for iColumna in columnas:
            if iColumna['axis'] == eje:
                nombreInteres = iColumna['name']
        return nombreInteres

    def get_name_from_standardname(self, nombre_estandar: str):
        ''' Método encargado de obtener el nombre de una columna a partir del nombre estándar.

        # Parámetros
        `nombre_estandar str`

        '''
        columnas = self.metadatos['schema']['fields']
        for iColumna in columnas:
            if iColumna['standard_name'] == nombre_estandar:
                nombreInteres = iColumna['name']
        return nombreInteres

    def get_value(self, nombre_variable):
        columna = self._datos[nombre_variable]
        return columna

    def write_glossary(self, carpeta_resultados):
        with open(carpeta_resultados + "glosario.json", "w") as archivo_glosario:
            json.dump(self.glosario, archivo_glosario)
