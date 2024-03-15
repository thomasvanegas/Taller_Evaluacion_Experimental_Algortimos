# Importación de Paquetes y Clases
from Punto2DCartesiano import Puntot2DCartesiano


# Definicion del ADT Estacion
class Estacion:

    """
        Contructor: Clase Estacion
    """
    def __init__(self, componente_x:int, componente_y:int, nombre_torre: str):
        self._id = 0
        self._nombre = nombre
        self._componente_x = componente_x
        self._componente_y = componente_y