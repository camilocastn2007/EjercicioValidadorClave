# TODO: Implementa el código del ejercicio aquí
from abc import ABC,abstractmethod,
class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada:int):
        self._longitud_esperada: int = longitud_esperada
