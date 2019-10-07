import math
class Rounder:
  def __init__(self):
    pass

  @staticmethod
  def round(numero):
    base = int(math.log10(numero))-1
    factor = 10**base
    redondeado = math.ceil(numero/factor)*factor
    return redondeado