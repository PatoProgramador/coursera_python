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

# Funcion 4: para lista las canciones de un artista
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
