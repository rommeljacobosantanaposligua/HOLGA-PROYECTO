#  Interfaces y Abstract Base Class (ABC)
from abc import ABC, abstractmethod

#  Abstracción: Definimos los conceptos generales sin entrar en detalles
class IEntidadAcademica(ABC):
    
    @abstractmethod
    def mostrar_info(self):
        """Método abstracto que obliga a las clases hijas a implementarlo"""
        pass
