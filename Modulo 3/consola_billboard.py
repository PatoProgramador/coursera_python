# -*- coding: utf-8 -*-
"""
Ejercicio nivel 3: Billboard.
Interfaz basada en consola para la interacción con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos

@author: Cupi2
"""

import billboard as bb

def ejecutar_cargar_canciones() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    las canciones y las carga.
    Retorno: list
        La lista de canciones con la información del archivo.
    """
    canciones = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con las canciones: ")
    # Retorna una lista de canciones
    canciones = bb.cargar_canciones(archivo)
    # Validacion en caso de tener una lista vacia
    if len(canciones) == 0:
        print("El archivo seleccionado no es válido. No se pudieron cargar las canciones del Ranking")
    else:
        print("Se cargaron", len(canciones), "canciones a partir del archivo.")
    return canciones

def ejecutar_buscar_cancion(canciones:list)->None:
    """ Ejecuta la opción de buscar una canción dado el nombre y el año del 
    ranking al cual pertenece 
    """
    cancion = input("Por favor ingrese el nombre de la canción que desea buscar: ")
    anio = int(input("Por favor ingrese el año de la canción que desea buscar: "))
    # Retorna un diccionario
    cancion = bb.buscar_cancion(canciones, cancion, anio)
    # validacion en caso de que no exista la cancion
    if cancion:
        bb.mostrar_detalles_cancion(cancion, True)
    else :
        print('No se pudo encontrar la cancion, por favor intentalo con una canción y año válidos')

def ejecutar_canciones_anio(canciones:list)->None:
    """ Ejecuta la opción de consultar las canciones de un año dado 
    """
    anio = int(input("Por favor ingrese el año que desea consultar: "))
    # Retorna una lista de canciones
    anio_canciones = bb.buscar_canciones_anio(canciones, anio)
    # Validacion en caso de tener una lista vacia
    if len(anio_canciones) > 0:
        for cancion in anio_canciones:
            bb.mostrar_detalles_cancion(cancion, False)
    else:
        print('No hay canciones con el año dado, por favor intente con uno diferente.')

def ejecutar_canciones_artista_periodo(canciones:list)->None:
    """ Ejecuta la opción de consultar las canciones de un artista dado en 
    un periodo de tiempo definido 
    """
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")
    anio_inic = int(input("Por favor ingrese el año inicial que desea buscar: "))
    anio_fin = int(input("Por favor ingrese el año final que desea buscar: "))
    # Retorna una lista de canciones
    artista_canciones = bb.buscar_canciones_artista(canciones, artista, anio_inic, anio_fin)
    # Validacion en caso de tener una lista vacia
    if len(artista_canciones) > 0:
        for cancion in artista_canciones:
            bb.mostrar_detalles_cancion(cancion, False)
    else:
        print('No se encontraron canciones con los parametros dados, por favor verifica la información.')

def ejecutar_todas_canciones_artista(canciones:list)->None:
    """ Ejecuta la opción de consultar todas las canciones de un artista dado 
    """
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")
    # Retorna la lista de canciones del artista
    artista_canciones = bb.buscar_canciones_artista_unico(canciones,artista)
    # validacion en caso de no encontrar canciones
    if len(artista_canciones) :
        for cancion in artista_canciones :
            bb.mostrar_detalles_cancion(cancion, False)
    else:
        print('No se encontraron canciones relacionadas al artista, por favor verifica la información.')

def ejecutar_todos_artistas_cancion(canciones:list)->None:
    """ Ejecuta la opción de consultar todos los artistas que han interpretado 
    una canción dada 
    """
    min = input("Por favor ingrese el nombre de la canción que desea buscar: ")
    # Retorna la lista de strings
    artistas = bb.buscar_artistas_interpretes(canciones, min)
    # validacion de que se hayan encontrado o no
    if len(artistas) > 0:
        print("-"*80)
        print(artistas)
        print("-"*80)
    else :
        print('No se encontraron artistas relacionados a la canción, por favor verifica la información.')

def ejecutar_artistas_mas_populares(canciones:list)->None:
    """ Ejecuta la opción de consultar los artistas más populares 
    """
    min = int(input("Por favor ingrese la cantidad mínima de canciones que desea buscar: "))
    # diccionario de artistas
    artistas = bb.buscar_cantidad_canciones(canciones, min)
    if len(artistas) > 0:
        print("-"*80)
        print('Artista-número de canciones')
        for key, value in artistas.items():
            print(f'{key}:{value}')
        print("-"*80)
    else :
        print('No se encontraron artistas con la cantidad de canciones dadas en el billboard. por favor intenta con otro valor')

def ejecutar_artista_estrella(canciones:list)->None:
    """ Ejecuta la opción de consultar el artista estrella de todos los tiempos 
    """
    artista = bb.buscar_artista_estrella(canciones)
    if artista:
        # Se saca clave y valor del diccionario para imprimir
        clave, valor = next(iter(artista.items()))
        print(f'El artista estrella de todos los tiempos es {clave} con {valor} canciones.')
    else :
        print('Ocurrió un error encontrando el artista')

def ejecutar_artistas_y_sus_canciones(canciones:list)->None:
    """ Ejecuta la opción de consultar la lista completa de artistas del Billboard 
    junto con sus canciones 
    """
    artistas = bb.buscar_artistas_y_canciones(canciones)
    print("-"*80)
    print('Artista-canciones')
    for key, value in artistas.items():
        print(f'{key}:{value}')
        print("-"*80)

def ejecutar_promedio_canciones_por_artista(canciones:list)->None:
    """ Ejecuta la opción de consultar la cantidad promedio de canciones que los 
    artistas tienen en el listado de Billboard 
    """
    promedio = bb.promedio_canciones_por_artista(canciones)
    print(f'El promedio de canciones por artista es: {promedio}')
    
    
def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de canciones")
    print("2. Buscar una canción")
    print("3. Consultar las canciones de un año")
    print("4. Consultar las canciones de un artista en un periodo")
    print("5. Consultar todas las canciones de un artista")
    print("6. Consultar todos los artistas que han interpretado una canción")
    print("7. Consultar los artistas más populares")
    print("8. Consultar el artista estrella de todos los tiempos")
    print("9. Consultar los artistas y sus canciones")    
    print("10. Consultar la cantidad promedio de canciones por artista")
    print("11. Salir.")

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    canciones = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            canciones=ejecutar_cargar_canciones()
        elif opcion_seleccionada == 2:
            ejecutar_buscar_cancion(canciones)
        elif opcion_seleccionada == 3:
            ejecutar_canciones_anio(canciones)
        elif opcion_seleccionada == 4:
            ejecutar_canciones_artista_periodo(canciones)
        elif opcion_seleccionada == 5:
            ejecutar_todas_canciones_artista(canciones)
        elif opcion_seleccionada == 6:
            ejecutar_todos_artistas_cancion(canciones)
        elif opcion_seleccionada == 7:
            ejecutar_artistas_mas_populares(canciones)
        elif opcion_seleccionada == 8:
            ejecutar_artista_estrella(canciones)
        elif opcion_seleccionada == 9:
            ejecutar_artistas_y_sus_canciones(canciones)
        elif opcion_seleccionada == 10:
            ejecutar_promedio_canciones_por_artista(canciones)            
        elif opcion_seleccionada == 11:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

