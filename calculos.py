

def sumar_dato_jugador_diccionario(lista_jugadores: dict, key: str, parametro: str ) -> str:
    """
    La función toma un diccionario de jugadores, una clave y un parámetro, y devuelve la suma del
    parámetro para todos los jugadores y el número de jugadores.
    
    :param lista_jugadores: Un diccionario que contiene información sobre los jugadores
    :type lista_jugadores: dict
    :param key: La clave es una cadena que representa la clave del diccionario que contiene los datos
    que queremos resumir
    :type key: str
    :param parametro: La variable parámetro es una cadena que representa la clave específica dentro del
    diccionario de cada jugador que queremos resumir. Por ejemplo, si queremos sumar el número total de
    goles marcados por cada jugador, pasaríamos "goles" como parámetro
    :type parametro: str
    :return: una tupla que contiene el valor acumulado de un parámetro específico para todos los
    jugadores en un diccionario y el número de jugadores que se consideraron en la acumulación.
    """
    
    acumulador_dato = 0
    contador = 0
    for jugadores in lista_jugadores:
        if type(jugadores) == dict and len(lista_jugadores) > 0:
            acumulador_dato += jugadores[key][parametro]
            contador += 1
    
    return (acumulador_dato, contador)

def sumar_dato_jugadores_lista(lista_personajes: list, parametro: str ) -> str:
    """
    La función calcula la suma de un parámetro específico para todos los elementos del diccionario en
    una lista y devuelve la suma y el número de elementos.
    
    :param lista_personajes: una lista de diccionarios que representan personajes en un juego o historia
    :type lista_personajes: list
    :param parametro: El parámetro es una cadena que representa la clave del valor que queremos sumar de
    los diccionarios de la lista. Por ejemplo, si los diccionarios de la lista tienen una clave
    "puntuación", entonces el parámetro sería "puntuación"
    :type parametro: str
    :return: una tupla que contiene la suma de un parámetro específico (especificado por el parámetro de
    entrada "parámetro") para todos los diccionarios en una lista (especificado por el parámetro de
    entrada "lista_personajes") y el número de diccionarios en la lista que tenían el parámetro
    especificado.
    """
    
    acumulador_dato = 0
    contador = 0
    for personajes in lista_personajes:
        if type(personajes) == dict and len(personajes) > 0: 
         acumulador_dato += personajes[parametro]
         contador += 1
    
    return (acumulador_dato, contador)

def dividir(dividendo, divisor):
    """
    La función divide dos números y devuelve el resultado, pero si el divisor es cero, devuelve cero.
    
    :param dividendo: El dividendo, o el número que se divide
    :param divisor: El número que divide el dividendo. No puede ser cero, de lo contrario la función
    devolverá 0
    :return: Si el divisor no es igual a cero, la función devuelve el resultado de dividir el dividendo
    por el divisor. Si el divisor es igual a cero, la función devuelve 0.
    """
    
    if divisor == 0:
        return 0
    else:
        return dividendo / divisor
    
def calcular_promedio(lista_jugadores: dict , key: str, parametro: str) -> float:
    """
    Esta función calcula el valor promedio de un parámetro específico para una tecla dada en un
    diccionario de jugadores.
    
    :param lista_jugadores: El diccionario que contiene información sobre los jugadores
    :type lista_jugadores: dict
    :param key: La clave es una cadena que representa el identificador único de un jugador en el
    diccionario. Se utiliza para acceder a los datos del jugador en el diccionario
    :type key: str
    :param parametro: El parámetro es una cadena que representa el atributo o estadística específica
    para la que queremos calcular el promedio. Por ejemplo, si estamos calculando la puntuación media de
    un jugador, el parámetro podría ser "puntuación"
    :type parametro: str
    :return: una cadena formateada que representa el valor promedio de un parámetro específico para una
    clave dada en un diccionario de jugadores.
    """
    
    
    suma_dato , divisor = sumar_dato_jugador_diccionario(lista_jugadores, key, parametro )
    promedio_dato = dividir(suma_dato, divisor)
    numero_formateado = "{:.2f}".format(promedio_dato)

    return numero_formateado
       
def calcular_promedio_sin_el_menor(lista_jugadores, parametro ):
    """
    Esta función calcula el promedio de un parámetro dado para una lista de jugadores, excluyendo al
    jugador con el valor más bajo para ese parámetro.
    
    :param lista_jugadores: Es una lista de diccionarios que contienen información sobre los jugadores.
    Cada diccionario representa a un jugador y contiene claves como nombre, edad, posición, etc
    :param parametro: El parámetro es una cadena que representa el atributo específico o la estadística
    de los jugadores para los que queremos calcular el promedio. Por ejemplo, podría ser "goles
    marcados" o "asistencias"
    :return: una cadena con formato que representa el valor promedio de un parámetro específico para una
    lista de jugadores, excluyendo al jugador con el valor más bajo para ese parámetro.
    """

    suma_dato , divisor = sumar_dato_jugadores_lista(lista_jugadores, parametro )
    promedio_dato = dividir(suma_dato, divisor)
    numero_formateado = "{:.2f}".format(promedio_dato)

    return numero_formateado
    
def quick_sort_diccionarios(lista_original: list, key,  flag_orden: bool, ) -> list:
    """
    Esta es una función de Python que realiza una clasificación rápida en una lista de diccionarios
    según una clave específica y un orden de clasificación.
    
    :param lista_original: La lista original de diccionarios que deben ordenarse
    :type lista_original: list
    :param flag_orden: Un indicador booleano que determina si la lista debe ordenarse en orden
    ascendente o descendente
    :type flag_orden: bool
    :param key: El parámetro clave se utiliza para especificar una función de un argumento para extraer
    una clave de comparación de cada elemento de la lista. Esta función clave se aplica a cada elemento
    de la lista antes de ordenar, y los elementos se ordenan en función de las claves resultantes
    :return: una lista ordenada de diccionarios basada en una clave específica, utilizando el algoritmo
    de clasificación rápida. La clave específica y el orden de clasificación (ascendente o descendente)
    están determinados por los parámetros de entrada `key` y `flag_orden`, respectivamente.
    """
    
    lista_de = []
    lista_iz = []

    if len(lista_original) <= 1:
        return lista_original
    else:
        pivot = lista_original[0]
        for elemento in lista_original[1:]:
                if elemento[key] > pivot[key]:
                    lista_de.append(elemento)
                else:
                    lista_iz.append(elemento)

    if flag_orden:
        lista_iz = quick_sort_diccionarios(lista_iz,key, True)
        lista_iz.append(pivot) 
        lista_de = quick_sort_diccionarios(lista_de,key,True)
        lista_iz.extend(lista_de) 
        retorno = lista_iz
    else:
        lista_de = quick_sort_diccionarios(lista_de,key,False)
        lista_de.append(pivot) 
        lista_iz = quick_sort_diccionarios(lista_iz,key,False)
        lista_de.extend(lista_iz) 
        retorno = lista_de
        
    return retorno

def calcular_max_min_dato_de_diccionario(lista_personajes: list, key:str, parametro:str, maximo: str):
    """
    Esta función calcula el valor máximo o mínimo de un parámetro especificado en una lista de
    diccionarios y devuelve una lista de diccionarios que contienen el nombre y el valor de los
    caracteres con ese valor máximo o mínimo.
    
    :param lista_personajes: una lista de diccionarios que representan caracteres, cada uno con un
    diccionario anidado de atributos
    :type lista_personajes: list
    :param key: una cadena que representa la clave en el diccionario de cada carácter que contiene el
    parámetro a comparar (por ejemplo, "estadísticas" o "atributos")
    :type key: str
    :param parametro: una cadena que representa el parámetro específico dentro del diccionario de cada
    carácter que queremos comparar (por ejemplo, "vida", "ataque", "defensa")
    :type parametro: str
    :param maximo: Un parámetro booleano que determina si se calcula el valor máximo o mínimo para la
    clave y el parámetro dados en el diccionario. Si es True, la función calculará el valor máximo, y si
    es False, la función calculará el valor mínimo
    :type maximo: str
    :return: La función `calcular_max_min_dato_de_diccionario` devuelve una lista de diccionarios que
    contienen el nombre y el valor máximo o mínimo de un parámetro especificado para una lista de
    caracteres dada. El parámetro a considerar como máximo o mínimo está determinado por el parámetro
    `maximo`, que es un valor booleano. Si `maximo` es True, la función devuelve el diccionario con el
    carácter
    """
    
    if not lista_personajes:
        return -1
    
    indice_maximo_minimo = 0
    lista_auxiliar = []
    
    
    if maximo:
        for indice_actual in range(len(lista_personajes)):
            valor_actual = float(lista_personajes[indice_actual][key][parametro])
            if indice_actual == 0 or valor_actual > valor_maximo_minimo:
                indice_maximo_minimo = indice_actual
                valor_maximo_minimo = valor_actual
        
        for personaje in lista_personajes:
            if float(personaje[key][parametro]) == valor_maximo_minimo:
                diccionario_auxiliar = {}
                diccionario_auxiliar ["nombre"] = personaje["nombre"]
                diccionario_auxiliar[parametro] = valor_maximo_minimo
                lista_auxiliar.append(diccionario_auxiliar)

    elif maximo == False:
        for indice_actual in range(len(lista_personajes)):
            valor_actual = float(lista_personajes[indice_actual][key][parametro])
            if indice_actual == 0 or valor_actual < valor_maximo_minimo:
                indice_maximo_minimo = indice_actual
                valor_maximo_minimo = valor_actual
        
        for personaje in lista_personajes:
            if float(personaje[key][parametro]) == valor_maximo_minimo:
                diccionario_auxiliar = {}
                diccionario_auxiliar ["nombre"] = personaje["nombre"]
                diccionario_auxiliar[parametro] = valor_maximo_minimo
                lista_auxiliar.append(diccionario_auxiliar)
    
    return lista_auxiliar
