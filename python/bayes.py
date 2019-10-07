# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#==========================Imporatación de librerias============================
# En esta sección se cargan las librerias de python que se utilizarán
import numpy as np
import scipy.stats as st
import scipy.misc as cb
import matplotlib.pyplot as Grafica
import json
import csv
import os

pathLocal=os.getcwd()                  #Dirección de la carpeta actual
#===============Valores aleatorios para los datos sintéticos===================
# Aquí se generan los valores objetivos y los datos sintéticos de señales
a=1;b=3                         #Parámetros de la distribución beta
No=st.uniform.rvs(100,200)      #valor objetivo q
q=st.beta.rvs(a,b)              #valor objetivo No
nDatos=30
datos=st.binom.rvs(No,q,size=nDatos) #Observaciones sintéticas
print(datos)
print(No)
print(q)
#=========Características del muestreo y asignación de memoria (AM)=============
# Se asigna las memoria, las variables auxiliares y listas y diccionarios que se
# utilizarán en la programa (no sé si eso ayuda a la velocidad de cálculo)
nCicloInterno=10                       #número de ciclos internos
nCiclo=500                             #cuántas muestras se guardarán
NoMuestrasGibbs=[0 for i in range(nCiclo)]     #(AM) muestras del tamaño de población (TP)
qMuestrasGibbs =[0 for i in range(nCiclo)]     #(AM) muestras de la probabilidad (q)
diccionarioDatos={}
diccionarioCampo={}
diccionarioAuxiliar={}                      #Diccionario auxiliar para diversos
listaAuxiliar=[]                            #Lista auxiliar para diversos
NoMetadatosVariables={}                      #metadatos variables para TM
qMetadatosVariables={}                      #metadatos variables para q
NoMetadatosGlobales={}                       #metadatos globales para TM
qMetadatosGlobales={}                        #metadatos globales para q
#datos_MnCMC=np.zeros((100,10))
#======================Escritura de datos sintéticos============================
# Los datos sintéticos se guardarán el los un archivo `json`. Para hacer eso
# se usa la función `json.dump` que utiliza diccionarios como valores de
# entrada, pero no identifica numpy.arrays, por lo tanto se tiene que cambiar
# el formato.
listaAuxiliar.append(q)                     #Lista para agregar al diccionario
listaAuxiliar.append(No)                    #Lista para agragar al diccionario
for iDatos in range(nDatos):           #Ciclo de los datos sintéticos
    listaAuxiliar.append(int(datos[iDatos]))#Se cambia formato para utilizar json.dump
#============metadatos globales de los datos isntéticos y objetivos=============
diccionarioAuxiliar={
"name":"datos-sinteticos",
"title":"objective and synthetic data",
"titulo":"datos objetivos y sinteticos",
"institution":"GECI",
"source":"son generados por el programa `bayes.py`",
"history":"son generados a partir de las funciones beta.rvs y uniform.rvs de la libreria scipy.stats",
"references":"Ramsey2009",
}
#===========Metadatos de las variables de los datos sintéticos==================
diccionarioCampo={
"fields": [
  {
    "name": "q",
    "units": "",
    "long_name": "probabilidad de encontrar una se\\~nal",
    "standard_name": "probabilidad"
  },
  {
    "name": "No",
    "units": "blancos",
    "long_name": "poblaci\\'on inicial",
    "standard_name": "poblaci\\'on inicial"
  },
  {
    "name": "datos",
    "units": "",
    "long_name": "datos sint\\'eticos de los individuos vistos",
    "standard_name": "individuos vistos"
  },
  {
    "name": "nDatos",
    "units": "",
    "long_name": "n\\'umero de datos sinti\\'eticos",
    "standard_name": "n\\'umero de datos"
  }
]
}
#==========Cambio de tipo de datos para usar la función `json.dump`=============
# Aquí se guardan los datos objetivos y sintéticos en un diccionario para poder
# ser exportados con la función `json.dump` al archivo `resultados\datos-objetivo.json`
diccionarioDatos['Metadata']=diccionarioAuxiliar
diccionarioDatos['q']={
    "data": round(float(listaAuxiliar[0]),3),
    "units": "",
    "description": "probabilidad de detección de un individuo",
    "nombre_largo": "probabilidad de encontrar una señal",
    "standard_name": "detection_probability"
}
diccionarioDatos['No']={
    "data": int(listaAuxiliar[1]),
    "units": "individuos",
    "description": "el valor objetivo de la población inicial",
    "nombre_largo": "población inicial",
    "standard_name":"initial_population"
}
diccionarioDatos['datos']={
    "data": listaAuxiliar[2:nDatos+2],
    "units": "observaciones",
    "nombre_largo": "datos sint\\'eticos de los individuos vistos",
    "description": "son los datos sint\\'eticos de las observaciones",
    "standard_name":"sign_count"
}
diccionarioDatos['nDatos']={
    "data": nDatos,
    "units": "muestras",
    "nombre_largo": "n\\'umero de datos sint\\'eticos",
    "description": "n\\'umero de obseracines sint\\'eticas",
    "standard_name":"sign_sample"
}
#auxDiccionario['data']=diccionarioData
#auxDiccionario['schema']=diccionarioFields
nombreArchivo=pathLocal+'\\resultados\\datos-objetivo.json';
with open(nombreArchivo,'w') as salidaJson:
    json.dump(diccionarioDatos,salidaJson,indent=2)
#========================Muestreo de Gibbs=====================================
# Aquí se hacen dos ciclos para obtener las muestras de Gibbs para las hipótesis
# TP y q. El ciclo interno nos dice cada cuantos intentes se guarda una muestra
NoMuestrasGibbs[0]=int(st.uniform.rvs(max(datos),300-max(datos))) #Valor inicial No
qMuestrasGibbs [0]=st.uniform.rvs(0,1)                            #Valor inicial q

for iCiclo in range(1,nCiclo):
    NoAnterior=NoMuestrasGibbs[iCiclo-1];
    for iCicloInterno in range(1,nCicloInterno):
    # Una muestra de q
        qAuxiliar=0.
        #ciclo de los datos sinéticos
        for iDatos in range(0,nDatos):
            a1=a+datos[iDatos];b1=b+NoAnterior-datos[iDatos]
            qAuxiliar=qAuxiliar+st.beta.rvs(a1,b1) # q ~ beta(a+dato,b+N-datos)
        qAuxiliar=qAuxiliar/nDatos
    # Tamaño inicial de muestra
        NoAuxiliar=0.
        #ciclo de los datos sintéticos.
        for iDatos in range(0,nDatos):
            NoAuxiliar=NoAuxiliar+st.binom.rvs(NoAnterior,qAuxiliar)
            min=NoAuxiliar/nDatos
            if min < max(datos):
                min=max(datos)
        NoAnterior=int(st.uniform.rvs(min,300-min))
    NoMuestrasGibbs[iCiclo]=NoAnterior
    qMuestrasGibbs[iCiclo] =qAuxiliar

#======================Graficado===============================================
#==============================================================================
qEtiqueta=[]
for i in range(100):
    qEtiqueta.append(i*0.01)
NoEtiqueta=[]
for i in range(40,300):
    NoEtiqueta.append(i)
#================Primer Histograma=============================================
NoMetadatosGlobales={
"name":"histograma-de-la-poblacion-inicial",
"title":"initial population histogram",
"titulo":"histograma de la poblacion inicial",
"institution":"GECI",
"source":"son generados por el programa `bayes.py`",
"history":"",
"references":"Ramsey2009",
}
NoMetadatosVariables["eje_x"]={
"name":"initial_size",
"type":"integer",
"units":"cabras",
"standard_name":"initial population size",
"long_name":"Initial population",
"nombre_largo":"Población inicial",
"axis":""}
NoMetadatosVariables["eje_y"]={
"name":"repetition_event",
"type":"integer",
"units":"",
"standard_name":"repetition of the event",
"long_name":"Repetitions",
"nombre_largo":"Repeticiones",
"axis":""}
Grafica.figure(1)
NoHistograma=Grafica.hist(NoMuestrasGibbs,bins=NoEtiqueta);
Grafica.title(NoMetadatosGlobales['titulo']);
Grafica.xlabel(NoMetadatosVariables["eje_x"]["nombre_largo"]);
Grafica.ylabel(NoMetadatosVariables["eje_y"]["nombre_largo"]);
#grc.show();
Grafica.savefig(pathLocal+'\\resultados\\tamagno_inicial.png')
#==================Segundo histograma==========================================
qMetadatosGlobales={
"name":"histograma-de-la-probabilidad-de-deteccion",
"title":"probability of detection histogram",
"titulo":"histograma de la probabilidad de detección",
"institution":"GECI",
"source":"son generados por el programa `bayes.py`",
"history":"",
"references":"Ramsey2009",
}
qMetadatosVariables["eje_x"]={
"name":"probability_sign",
"type":"float",
"units":"",
"standard_name":"probability of detecting sign",
"long_name":"probability of detection",
"nombre_largo":"probabilidad de detección",
"axis":""}
qMetadatosVariables["eje_y"]={
"name":"repetition_event",
"type":"integer",
"units":"",
"standard_name":"repetition of the event",
"long_name":"Repetitions",
"nombre_largo":"Repeticiones",
"axis":""}
Grafica.figure(2)
qHistograma=Grafica.hist(qMuestrasGibbs,bins=qEtiqueta);
Grafica.title(qMetadatosGlobales['titulo']);
Grafica.xlabel(qMetadatosVariables["eje_x"]["nombre_largo"]);
Grafica.ylabel(qMetadatosVariables["eje_y"]["nombre_largo"]);#grc.show();
Grafica.savefig(pathLocal+'\\resultados\\probabilidad_captura.png')

#=======================Captura de datos========================================
#==========================datos_histograma_No.csv=========================================
NoMetadatosGlobales["data"]='datos_histograma_No.csv'
nombreCSV= pathLocal+'\\resultados\\'+NoMetadatosGlobales["data"]
with open(nombreCSV,'w') as salidaCSV:
    write=csv.writer(salidaCSV,lineterminator='\n')
    write.writerow([NoMetadatosVariables["eje_x"]["name"],NoMetadatosVariables["eje_y"]["name"]])
    for i in range(np.size(NoHistograma[0])):
        write.writerow([NoHistograma[1][i],int(NoHistograma[0][i])])
nombreArchivoAuxiliar='metadatos_histograma_No.json'
NoMetadatosGlobales["fields"]=NoMetadatosVariables
nombreArchivo=pathLocal+'\\resultados\\'+nombreArchivoAuxiliar;
with open(nombreArchivo,'w') as salidaJson:
    json.dump(NoMetadatosGlobales,salidaJson,indent=2)
#==========================datos_histograma_q.csv==========================================
qMetadatosGlobales["data"]='datos_histograma_q.csv'
nombreCSV=pathLocal+'\\resultados\\'+qMetadatosGlobales["data"]
with open(nombreCSV,'w') as salidaCSV:
    write=csv.writer(salidaCSV,lineterminator='\n')
    write.writerow([qMetadatosVariables["eje_x"]["name"],qMetadatosVariables["eje_y"]["name"]])
    for i in range(np.size(qHistograma[0])):
        write.writerow([qHistograma[1][i],int(qHistograma[0][i])])
nombreArchivoAuxiliar='metadatos_histograma_q.json'
qMetadatosGlobales["fields"]=qMetadatosVariables
nombreArchivo=pathLocal+'\\resultados\\'+nombreArchivoAuxiliar;
with open(nombreArchivo,'w') as salidaJson:
    json.dump(qMetadatosGlobales,salidaJson,indent=2)
