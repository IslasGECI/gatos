import scipy.stats as st
class Captura(object):
    """Define la clase de los objetos capturas"""
    def __init__(self, numeroIntentos=10,probabilidadCaptura=0.1,\
    poblacionInicial=500):
        '''Método inicilizador de los objetos de clase jugador'''
        self.numeroIntentos=numeroIntentos#Número de intentos de camputará
        self.probabilidadCaptura=probabilidadCaptura   #Probabilidad de captura
        self.poblacionInicial=poblacionInicial#Tamaño inicial de la población
        aux=0
        ind=0
        self.capturas=[]
    def SetInitialPopulations(self,poblacionInicial):
        """Método que guarda el tamaño inicial de la población"""
        self.poblacionInicial=poblacionInicial
    def SetCaptureProbability(self,probabilidadCaptura):
        """Método que guarda la probabilidad de captura"""
        self.probabilidadCaptura=probabilidadCaptura
    def MakeCaptures(self):
        """Método que guarda la probabilidad de captura"""
        aux=0
        ind=0
        self.capturas=[]
        for iIntentos in range(self.numeroIntentos):
            self.capturas.append(st.binom.rvs(self.poblacionInicial-aux,\
            self.probabilidadCaptura,1))#Las capturas por intento
            aux=aux+self.capturas[ind]
