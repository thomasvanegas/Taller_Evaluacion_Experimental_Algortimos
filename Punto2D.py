# Importacion de paquetes y clases
import math

class Punto2D:
    """
        Clase que representa un punto en el plano XY
    """

    def calcularDistacia(self, other:'Point2D') -> float:
        """
            Calcular la distacia a otro punto en el plano XY
        """
        return math.sqrt( (self.getX() - other.getX())**2 + (self.getY() - other.getY())**2 )
    
    def __abs__(self) -> float:
        """
            Retorna la distancia desde el origen hasta el punto (Magnitud)
        """
        return None
    
    def angle(self) -> float:
        """Returns the angle to the x axis
        
        Not defined, must be implemented in subclasses
        """
        return None
    
    def getX(self) -> float:
        """Returns the x component
        
        Not defined, must be implemented in subclasses
        """
        return None

    def getY(self) -> float:
        """Returns the y component
        
        Not defined, must be implemented in subclasses
        """
        return None
    
    def __eq__(self, other:'Point2D') -> bool:
        """Returns True if self==other (or very close to)
        """
        if self.distance(other)<1E-15:
            return True
        return False