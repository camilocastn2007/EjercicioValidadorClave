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

   @abstractmethod
    def es_valida(self, clave):
        pass

class ReglaValidacionGanimedes(ReglaValidacion):
    CARACTERES_ESPECIALES = '@_#$%'

    def __init__(self):
        super().__init__(8)  # La longitud esperada es mayor a 8

    def _contiene_caracter_especial(self, clave):
        return any(c in self.CARACTERES_ESPECIALES for c in clave)

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise Exception("La clave debe tener una longitud de más de 8 caracteres")
        if not self._contiene_mayuscula(clave):
            raise Exception("La clave debe contener al menos una letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise Exception("La clave debe contener al menos una letra minúscula")
        if not self._contiene_numero(clave):
            raise Exception("La clave debe contener al menos un número")
        if not self._contiene_caracter_especial(clave):
            raise Exception("La clave debe contener al menos un caracter especial (@, _, #, $, %)")
        return True

def _contiene_calisto(self, clave):
    calisto = 'calisto'
    mayusculas = sum(1 for c in clave if c.isupper())
    return 'calisto' in clave.lower() and 2 <= mayusculas < 6
