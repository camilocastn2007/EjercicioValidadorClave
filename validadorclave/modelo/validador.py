# TODO: Implementa el código del ejercicio aquí
from abc import ABC,abstractmethod,
class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada:int):
        self._longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave):
        return any(a.isupper() for a in clave)

    def _contiene_minuscula(self, clave):
        return any(a.islower() for a in clave)


    def _contiene_numero(self,clave):
        return any(a.isdigit() for a in clave)

