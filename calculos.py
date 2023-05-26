

def sumar_dato_jugador(lista_jugadores: list, key: str, parametro: str ) -> str:
    '''
    recibe una lista,  verifica que se guarde un dict y que  no este vacio, si 
    no lo esta se utiliza un acumulador donde se suma la key
    recibe una lista y un str
    retorna un str
    
    '''
    acumulador_dato = 0
    contador = 0
    for jugadores in lista_jugadores:
        if type(jugadores) == dict and len(jugadores) > 0:
         acumulador_dato += jugadores [key][parametro]
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
    
def calcular_promedio(lista_jugadores:list, key: str, parametro: str) -> float:
    '''
    esta funcion calcula el promedio, llama a la funcion sumar, retorna los
    valores para hacer el promedio y llama a dividir para que haga los calculos 
    recibe la lista y la key de lo que se quiere calcular
    devuelve el resultado

    '''

    suma_dato , divisor = sumar_dato_jugador(lista_jugadores, key, parametro )
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
    '''
    recorre la lista y determina el minimo y el maximo por x parametro y guarda su nombre
    recibe una lista, una categoria y un booleano
    devuelve un string con el nombre del personaje
    
    '''
    if not lista_personajes:
        return -1
    
    indice_maximo_minimo = 0
    
    if maximo:
        for indice_actual in range(len(lista_personajes)):
            if indice_actual == 0 or float(lista_personajes[indice_maximo_minimo][key][parametro])< float(lista_personajes[indice_actual][key][parametro]):
                indice_maximo_minimo = indice_actual
                nombre = lista_personajes[indice_maximo_minimo]["nombre"]
    elif maximo == False:
        for indice_actual in range(len(lista_personajes)):
            if indice_actual == 0 or float(lista_personajes[minimo_altura_indice][key][parametro])> float(lista_personajes[indice_actual][key][parametro]):
                minimo_altura_indice = indice_actual
                nombre = lista_personajes[indice_maximo_minimo]["nombre"]

    
    return nombre
