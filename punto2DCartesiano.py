# Importacion de paquetes, clases y bibliotecas
import math

class Punto2DCartesiano():
    """
        Clase que representa un punto con dos componentes (X,Y) en el plano XY o plano Cartesiano
    """

    def __init__(self, x:float, y:float):
        """
            Contruye e inicializa un punto en el plano XY, con dos componentes, (X,Y)
        """
        self._x = x
        self._y = y
        
    def __str__(self):
        """
            Retorna una cadena de caracteres como representación del punto (X,Y)
        """
        return f'Punto en el plano XY, con coordenadas: ({str(self.getX())},{str(self.getY())})'
    
    def __abs__(self):
        """
            Retorna la distancia desde el origen hacia el punto
        """
        return math.sqrt( (self._x**2) + (self._y**2) )
    
    def getAngle(self) -> float:
        """
            Retorna el ángulo con respecto al eje X del punto
        """
        return math.atan2( self._y, self._x )
    
    def getX(self) -> float:
        """
            Retorna el valor de la componente X, del punto (X,Y)
        """
        return self._x

    def getY(self) -> float:
        """
            Retorna el valor de la componente Y, del punto (X,Y)
        """
        return self._y

    def getDistancia(self, puntoXY:'Point2D') -> float:
        """
            Calcular la distacia a otro punto en el plano XY
        """
        return math.sqrt( ((self.getX() - puntoXY.getX())**2) + ((self.getY() - puntoXY.getY())**2) )