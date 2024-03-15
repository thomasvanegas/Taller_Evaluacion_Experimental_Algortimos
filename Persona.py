# Importacion de Paquetes y Clases
from Estacion import Estacion
from Punto2DCartesiano import Punto2DCartesiano

# Definicion del ADT Persona
class Persona(Punto2DCartesiano):
    
    # Variable contadora de ID's de las personas
    _contador_id = 1

    """
        Contructor: Clase Persona
    """
    def __init__(self, x: float, y: float):
        super().__init__(x = x, y = y)
        self._id = self._contador_id
        self._estacion_asociada = None

        # Incremento de la variable ID
        Persona._contador_id += 1

    def getId(self):
        return self._id

        def setEstacion(self, estacion: "Estacion"):
            self._estacion_asociada = estacion.getId()

    # Sobreescribiendo la función print()
    def __str__(self):
        return f'Soy la persona con ID: {self._id}, Estación asociada: {self._estacion_asociada}, Poseo la Coordenada: ({self.getX()},{self.getY()})'