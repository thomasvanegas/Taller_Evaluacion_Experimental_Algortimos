# Importacion de Paquetes y Clases
from Estacion import Estacion
from Punto2DCartesiano import Puntot2DCartesiano

# Definicion del ADT Persona
class Persona:

    """
        Contructor: Clase Persona
    """
    def __init__(self, componente_x: int, componente_y: int, nombre: str):
        self._nombre = nombre
        self._estacion_base_asociada = None
        self._componente_x = componente_x
        self._componente_y = componente_y