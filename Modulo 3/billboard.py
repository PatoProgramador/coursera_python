# Funcion para mostrar detalles de las canciones
# Recibe por parametro la cancion(diccionario) a imprimir y
# Recibe por parametro un booleano para imprimir o no la letra
def mostrar_detalles_cancion(cancion: dict, letra: bool) -> None:
    nombre = cancion['nombre_cancion']
    artista = cancion['nombre_artista']
    anio = cancion['anio']
    posicion = cancion['posicion']
    
    if letra :
        letra = cancion['letra'] 
        print("-"*80)
        print(f'Nombre: {nombre} - Ranking: {posicion}')
        print(f'Artista: {artista} - Año: {anio}')
        print(f'Letra: {letra}')
        print("-"*80)
    else:
        print("-"*80)
        print(f'Nombre: {nombre} - Ranking: {posicion}')
        print(f'Artista: {artista} - Año: {anio}')
        print("-"*80)

# Funcion 1: de leer el archivo
# Se retornan un array de diccionarios
# El modelo de las canciones:
# cancion = {
#   posicion: posicion de la cancion en el rank,
#   nombre_cancion: nombre de la cancion,
#   nombre_artista: artista de la cancion,
#   anio: año de la cancion,
#   letra: letra de la cancion
# }
def cargar_canciones(archivo: str) -> list :
    # Se pasa por parametro el nombre del archivo
    canciones = []
    # Se usan las funciones de leer el archivo
    archivo = open(archivo)
    archivo.readline()
    
    linea = archivo.readline()
    # Ciclo para pasar linea por linea creando un diccionario por canción
    while len(linea) > 0:
        datos = linea.split(',')
        cancion = {
            'posicion':datos[0],
            'nombre_cancion':datos[1],
            'nombre_artista':datos[2],
            'anio':datos[3],
            'letra':datos[4]
        }
        linea = archivo.readline()
        canciones.append(cancion)
        
    archivo.close()
    return canciones

# Funcion 2: para buscar una cancion
def buscar_cancion(canciones:list, nombre: str, anio: int) -> dict:
    # Recibe por parametros una lista de canciones, el nombre y el año de la canción a buscar
    findSong = {}
    # Ciclo for de busqueda de la canción
    for cancion in canciones:
        if cancion['nombre_cancion'] == nombre and int(cancion['anio']) == anio:
            findSong = cancion
    # En caso de no encontrarse la canción se retorna None
    if findSong == {} :
        findSong = None
    return findSong

# Funcion 3: para organizar canciones por un año dado
def buscar_canciones_anio(canciones: list, anio: int) -> list:
    # Recibe por parametros las canciones y el año
    anio_songs = []
    # ciclo for para buscar las canciones que tengan el mismo año
    for cancion in canciones:
        if int(cancion['anio']) == anio:
            # se copian todas las clave-valor del diccionario original menos la letra
            newDic = cancion.copy()
            newDic.pop('letra')
            anio_songs.append(newDic)
    return anio_songs

# Funcion 4: para lista las canciones de un artista en un rango de año
def buscar_canciones_artista(canciones:list, artista: str, anio_inicial: int, anio_final: int) -> list :
    artista_canciones = []
    for cancion in canciones:
        # Condicion para verificar el nombre del artista y si el año esta sobre el rango del año inicial y final
        if cancion['nombre_artista']  == artista and int(cancion['anio']) >= anio_inicial and int(cancion['anio']) <= anio_final:
            # se copian todas las clave-valor del diccionario original menos la letra
            newDic = cancion.copy()
            newDic.pop('letra')
            artista_canciones.append(newDic)
    return artista_canciones

# Funcion 5: buscar lista de cancion de un artista
def buscar_canciones_artista_unico(canciones:list, artista: str) -> list :
    artista_canciones = []
    for cancion in canciones:
        # Condicion para verificar el nombre del artista
        if cancion['nombre_artista']  == artista:
            # se copian todas las clave-valor del diccionario original menos la letra
            newDic = cancion.copy()
            newDic.pop('letra')
            artista_canciones.append(newDic)
    return artista_canciones

# Funcion 6: buscar artistas que interpretan una cancion
def buscar_artistas_interpretes(canciones:list, nombre_cancion: str) -> list :
    nombres = []
    # se busca en la lista de canciones aquellas que tengan el mismo nombre y se pushea el nombre del artista a la lista
    for cancion in canciones :
        if cancion['nombre_cancion'] == nombre_cancion:
            nombres.append(cancion['nombre_artista'])
    return nombres

# Funcion 7: buscar numero dado de canciones por artista
def buscar_cantidad_canciones(canciones:list, numero_canciones:int) -> list:
    artistas = {}
    artFilter = {}
    # se arma primero un diccionario con todas las canciones que se repiten por artista.
    for cancion in canciones :
        artista = cancion['nombre_artista']
        if artista in artistas:
            artistas[artista] += 1
        else:
            artistas[artista] = 1
    # Si filtran solo aquellos que cumplan la condicion minima de canciones
    for art in artistas:
        if artistas[art] >= numero_canciones :
            artFilter[art] = artistas[art]
    return artFilter
# Funcion 8: buscar artista estrella
def buscar_artista_estrella(canciones:list) -> dict:
    artistas = {}
    # se arma primero un diccionario con todas las canciones que se repiten por artista.
    for cancion in canciones :
        artista = cancion['nombre_artista']
        if artista in artistas:
            artistas[artista] += 1
        else:
            artistas[artista] = 1
    # Se busca el artista..
    artista = max(artistas, key=artistas.get)
    # Se crea el diccionario
    artista_Dic = {artista: artistas[artista]}
    return artista_Dic

# Funcion 9: diccionario de artistas con sus canciones
def buscar_artistas_y_canciones(canciones:list) -> dict:
    artistas = {}
    # se arma primero un diccionario con todas las canciones que se repiten por artista.
    for cancion in canciones :
        artista = cancion['nombre_artista']
        nombre_cancion = cancion['nombre_cancion']
        # se valida que no se repitan artistas
        if artista in artistas:
            # se valida que no se repitan canciones
            if nombre_cancion not in artistas[artista]:
                artistas[artista].append(nombre_cancion)
        else:
            artistas[artista] = [cancion['nombre_cancion']]
    return artistas
# Funcion 10: promedio de canciones por artista
def promedio_canciones_por_artista(canciones:list) -> float:
    # artistas sin repetir
    artistas = buscar_artistas_y_canciones(canciones)
    cancionesF = []
    # canciones sin repetir...
    for cancion in canciones:
        nombre_cancion = cancion['nombre_cancion']
        if nombre_cancion not in cancionesF :
            cancionesF.append(nombre_cancion)

    promedio = len(cancionesF) / len(artistas)
    return promedio