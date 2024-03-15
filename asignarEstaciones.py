# Importacion de paquetes, clases y librerias
from Estacion import Estacion
from Persona import Persona
from Punto2DCartesiano import Punto2DCartesiano

def asignarEstaciones(lista_personas: list[Persona], lista_estaciones: list[Estacion]):
    """
        Función que asigna a cada persona de la coleccion de personas la estación mas cercana a ella.
        Objetivo: Recorrer la lista personas, y calcular su distancia con cada una de las estaciones y almacenar la menor distancia.
    """

    for persona in lista_personas:

        # Inicializamos la distancia mínima como 0
        distancia_minima = float('inf')
        
        # Calculamos la distancia de la persona a cada estación
        for estacion in lista_estaciones:
            # Utilizando el metodo .getDistancia() que se hereda de la clase Punto2DCartesiano
            distancia = persona.getDistancia(estacion)
            print(f"La distacia de la persona ID:{persona.getId()} a la estacion ID:{estacion.getId()} es de: {distancia}\n")
            if distancia < distancia_minima:
                distancia_minima = distancia
                persona.setEstacion(estacion)

    print("--- Asignación de estaciones completada. ---")