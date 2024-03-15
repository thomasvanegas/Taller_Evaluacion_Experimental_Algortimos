# Importacion de clases, paquetes y librerias
import time


def medir_tiempo(numero_estaciones, numero_personas, k):
    medidas = 0
    for i in range(k + 1):
        tiempo_inicio = time.time()

        asignar_estaciones(numero_personas,numero_estaciones)
        t_fin = time.time()
        t_ejecucion = t_fin - t_inicio
        print(f"--- Tiempo de Ejecucion ---> {t_ejecucion}")
        medidas += t_ejecucion

    t_promedio = mediciones / k


    print(f"--- Medidas Tomadas ---> {medidas}")
    print(f"--- Numéro de Estaciones ---> {numero_estaciones}\n\n")  
    print(f"--- Numéro de Personas ---> {numero_personas}\n\n")
    print(f"--- Tiempo Promedio ---> {t_promedio}")

medir_tiempo(10, 100, 5)
