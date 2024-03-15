# Importación de Paquetes y Clases
from Punto2DCartesiano import Punto2DCartesiano


# Definicion del ADT Estacion
class Estacion(Punto2DCartesiano):
    
    # Variable contadora de ID's de las torres
    _contador_id = 1

    """
        Contructor: Clase Estacion
    """
    def __init__(self, x: float, y: float):
        super().__init__(x = x, y = y)
        self._id = self._contador_id

        # Incremento de la variable ID
        Estacion._contador_id += 1

    def getId(self):
        return self._id

    # Sobreescribiendo la función print()
    def __str__(self):
        return f'Soy la estación con ID: {self._id}, Poseo la Coordenada: ({self.getX()},{self.getY()})'