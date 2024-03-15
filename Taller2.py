# Importacion de Paquetes, Clases y Librerias.
import random
from Estacion import Estacion
from Persona import Persona
from Punto2DCartesiano import Punto2DCartesiano
from asignarEstaciones import asignarEstaciones

"""
    Ejecución del programa principal
"""

# El programa se ejecuta en un area de 10km x 10km <=> el origen es (0,0) y el punto mas alejado del origen es (10000, 10000)

if __name__ == "__main__":

    # Creacion de listas para personas y estaciones
    personas = []
    estaciones = []

    print("\n--- Bienvenido al Taller Experimental sobre Análisis de Algoritmos --- \n")
    print(f'--- Proyecto Realizado por: ---\n1. Thomas Vanegas\n2.Alejandro Gomez\n')
    
    # Solicitud de la cantidad N de personas
    n_personas = int(input("Ingresar la cantidad de personas: "))

    # Solicitud de la cantidad M de personas
    m_estaciones = int(input("Ingresar la cantidad de estaciones: "))

    # Confirmacion de datos
    print(f'\nLa cantidad de Personas ingresadas fue: {n_personas}\n')
    print(f'La cantidad de Estaciones ingresadas fue: {m_estaciones}\n')

    # Instanciamiento de N Personas
    for i in range(n_personas):
        componente_x, componente_y = random.randint(0, 10000), random.randint(0, 10000)
        persona = Persona(componente_x, componente_y)
        personas.append(persona)

    # Instanciamiento de M Estaciones
    for i in range(m_estaciones):
        componente_x, componente_y = random.randint(0, 10000), random.randint(0, 10000)
        estacion = Estacion(componente_x, componente_y)
        estaciones.append(estacion)

    # --- ASIGNACION DE LAS ESTACIONES A LAS PERSONAS ---
    asignarEstaciones(personas, estaciones)

    # Imprimir la informacion de todas las personas
    print("\n---  Información de la colección de Personas --- \n")
    for i, persona in enumerate(personas):
        print(persona)

    # Imprimir la informacion de todas las estaciones
    print("\n---  Información de la colección de Estaciones --- \n")
    for estacion in estaciones:
        print(estacion)