"""
>>> A.poblacionInicial
500
>>> A.probabilidadCaptura,A.numeroIntentos
(0.1, 10)
>>> B.poblacionInicial
700
"""
import os,sys
direccionLocal=os.getcwd()                  #Dirección de la carpeta actual
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..\clases")))
from Captura import Captura
A=Captura()
B=Captura(poblacionInicial=700)
C=Captura(7,0.07,777)
