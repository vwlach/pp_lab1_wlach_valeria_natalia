

def sumar_dato_jugador_diccionario(lista_jugadores: dict, key: str, parametro: str ) -> str:
    '''
    recibe una lista,  verifica que se guarde un dict y que  no este vacio, si 
    no lo esta se utiliza un acumulador donde se suma la key
    recibe una lista y un str
    retorna un str
    
    '''
    acumulador_dato = 0
    contador = 0
    for jugadores in lista_jugadores:
        if type(jugadores) == dict and len(lista_jugadores) > 0:
            acumulador_dato += jugadores[key][parametro]
            contador += 1
    
    return (acumulador_dato, contador)

def sumar_dato_jugadores_lista(lista_personajes: list, parametro: str ) -> str:
    '''
    recibe una lista,  verifica que se guarde un dict y que  no este vacio, si no lo esta se utiliza un acumulador donde se suma la key
    recibe una lista y un str
    retorna un str
    
    '''
    acumulador_dato = 0
    contador = 0
    for personajes in lista_personajes:
        if type(personajes) == dict and len(personajes) > 0: 
         acumulador_dato += personajes[parametro]
         contador += 1
    
    return (acumulador_dato, contador)

def dividir(dividendo, divisor):
    '''
    recibe dos numero, diviendo y divisor si el divisor es 0 retorna 0, sino hace la division
    recibe dos numero
    retorna la division

    '''
    if divisor == 0:
        return 0
    else:
        return dividendo / divisor
    
def calcular_promedio(lista_jugadores: dict , key: str, parametro: str) -> float:
    '''
    esta funcion calcula el promedio, llama a la funcion sumar, retorna los
    valores para hacer el promedio y llama a dividir para que haga los calculos 
    recibe la lista y la key de lo que se quiere calcular
    devuelve el resultado

    '''
    
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
