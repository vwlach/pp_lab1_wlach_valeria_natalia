from validaciones import *
from calculos import *
import json
import re

def parse_json(ruta_json:str):
    """
    La función "parse_json" lee un archivo JSON y devuelve una lista de jugadores.
    
    :param ruta_json: El parámetro "ruta_json" es una cadena que representa la ruta del archivo de un
    archivo JSON que contiene un diccionario con una clave "jugadores" que tiene una lista de jugadores.
    La función "parse_json" lee el archivo JSON y devuelve la lista de jugadores
    :type ruta_json: str
    :return: una lista de jugadores (jugadores) analizada desde un archivo JSON ubicado en la ruta
    especificada (ruta_json).
    """

    lista_vacia = []
    with open(ruta_json, 'r', encoding="utf-8") as archivo:
        diccionario = json.load(archivo)
        lista_vacia = diccionario["jugadores"]

    return lista_vacia

ruta_json = r"C:\\Users\\blair\\Documents\\GitHub\\pp_lab1_wlach_valeria_natalia\\dt.json"

lista_jugadores = parse_json(ruta_json)

def mostrar_nombre_parametro_y_valor(lista_o_diccionario: list or dict, parametro: str ): #PUNTO 1
    """
    La función toma una lista o diccionario y un parámetro, e imprime el nombre de cada elemento y su
    valor de parámetro correspondiente.
    
    :param lista_o_diccionario: Una lista o diccionario que contiene datos para mostrar
    :type lista_o_diccionario: list or dict
    :param parametro: Una cadena que representa el parámetro que se mostrará en la salida
    :type parametro: str
    :return: nada (es decir, Ninguno).
    """
    
    if type(lista_o_diccionario) == list:
        for jugadores in lista_o_diccionario:
            nombre = jugadores["nombre"]
            valor = jugadores[parametro]
            print("{0} - {1}: {2}".format(nombre, parametro.capitalize(), valor))

    elif type(lista_o_diccionario) == dict:
        for clave in lista_o_diccionario:
            valor = lista_o_diccionario[clave]
            print("{0} - {1}: {2}".format(clave.capitalize(), parametro.capitalize(),  valor))

    return 

def mostrar_informacion_jugador(lista_jugadores: list) -> dict: #PUNTO 2
    """
    Esta función toma una lista de jugadores de baloncesto y permite al usuario seleccionar un jugador
    por índice y muestra sus estadísticas en formato de diccionario.
    
    :param lista_jugadores: Una lista de diccionarios que contienen información sobre jugadores de
    baloncesto. Cada diccionario representa a un jugador y contiene su nombre y estadísticas
    :type lista_jugadores: list
    :return: Un diccionario que contiene información sobre un jugador de baloncesto seleccionado por el
    usuario.
    """
    diccionario_jugador = {}

    print("0 - Michael Jordan")
    print("1 - Magic Johnson")
    print("2 - Larry Bird")
    print("3 - Charles Barkley")
    print("4 - Scottie Pippen")
    print("5 - David Robinson")
    print("6 - Patrick Ewing")
    print("7 - Karl Malone")
    print("8 - John Stockton")
    print("9 - Clyde Drexler")
    print("10 - Chris Mullin")
    print("11 - Christian Laettner")

    
    string = input("Ingrese el indice del jugador del que quiera ver su informacion: ")
    opcion_validada = validar_opcion_2(string)
    indice = opcion_validada

    for i in range(len(lista_jugadores)):
        if indice == i:
            lista_auxiliar = []
            diccionario_jugador["nombre"] = lista_jugadores[i]["nombre"]
            diccionario_jugador["temporadas"] = lista_jugadores[i]["estadisticas"]["temporadas"]
            diccionario_jugador["puntos totales"] = lista_jugadores[i]["estadisticas"]["puntos_totales"]
            diccionario_jugador["promedio puntos por partido"] = lista_jugadores[i]["estadisticas"]["promedio_puntos_por_partido"]
            diccionario_jugador["rebotes totales"] = lista_jugadores[i]["estadisticas"]["rebotes_totales"]
            diccionario_jugador["promedio rebotes por partido"] = lista_jugadores[i]["estadisticas"]["promedio_rebotes_por_partido"]
            diccionario_jugador["asistencias totales"] = lista_jugadores[i]["estadisticas"]["asistencias_totales"]
            diccionario_jugador["promedio asistencias por partido"] = lista_jugadores[i]["estadisticas"]["promedio_asistencias_por_partido"]
            diccionario_jugador["robos totales"] = lista_jugadores[i]["estadisticas"]["robos_totales"]
            diccionario_jugador["bloqueos totales"] = lista_jugadores[i]["estadisticas"]["bloqueos_totales"]
            diccionario_jugador["porcentaje tiros de campo"] = lista_jugadores[i]["estadisticas"]["porcentaje_tiros_de_campo"]
            diccionario_jugador["porcentaje de tiros libres"] = lista_jugadores[i]["estadisticas"]["porcentaje_tiros_libres"]
            diccionario_jugador["porcentaje tiros triples"] = lista_jugadores[i]["estadisticas"]["porcentaje_tiros_triples"]
            lista_auxiliar.append(diccionario_jugador)
           
   
    for clave, valor in diccionario_jugador.items():
        print(clave, valor)
   
    return diccionario_jugador

def guardar_estadisticas_en_csv(ruta_file:str, contenido:dict): # PUNTO 3
    """
    Esta función toma un diccionario y guarda sus claves y valores como valores separados por comas en
    un archivo CSV en una ruta específica.
    
    :param ruta_file: La ruta del archivo donde se guardará el archivo CSV
    :type ruta_file: str
    :param contenido: El parámetro "contenido" es un diccionario que contiene las estadísticas a guardar
    en el archivo CSV. Las claves del diccionario representan los encabezados de columna y los valores
    representan los valores correspondientes para cada fila
    :type contenido: dict
    """
   

    
    lista_claves = []
    lista_valores = []
   
    for clave, valor in contenido.items():
        lista_claves.append(clave)
        lista_valores.append(str(valor))

    claves_str = ", ".join(lista_claves)
    valores_str = ",       ".join(lista_valores)

    with open(ruta_file, 'w+') as archivo:
        archivo.write("{0}\n {1}".format(claves_str, valores_str))
        

    if len(contenido) > 0:
        print("Se creó el archivo con éxito")
    else:
        print("Error al crear el archivo")

def buscar_jugador_mostrar_logros(lista_jugadores, parametro):
    """
    Esta función busca el nombre de un jugador en una lista de jugadores y muestra sus logros en función
    de un parámetro dado.
    
    :param lista_jugadores: una lista de diccionarios que contienen información sobre los jugadores,
    incluidos sus nombres y logros
    :param parametro: El parámetro es una cadena que representa el logro o atributo específico de un
    jugador que el usuario quiere ver, como "puntos" (puntos) o "asistencias" (asistencias)
    :return: nada (es decir, ninguno).
    """

    flag = False
    diccionario_aux = {}
    for jugadores in lista_jugadores:
        print(jugadores["nombre"])

    nombre_ingresado = input("Ingrese el nombre del jugador que quiera ver sus logros: ")
    expresion_regular= r'\b'+nombre_ingresado+r'\b|\b'+nombre_ingresado+r'[a-zA-Z]{1,}\b|\b[a-zA-Z]{1,}'+nombre_ingresado+r'\b'
    
    for jugador in lista_jugadores:
        nombre = jugador["nombre"].lower()
        if re.search(expresion_regular, nombre) != None:
            diccionario_aux[ jugador["nombre"]] = jugador[parametro]
            flag = True
    if flag == False:
        print("---- ERROR ---- Ingrese un nombre correcto")
    
    return diccionario_aux

def calcular_mostrar_promedio_de_puntos_ordenado(lista_jugadores, key , parametro): # PUNTO 5
    """
    Esta función calcula y muestra el promedio de puntos por juego para una lista de jugadores y luego
    ordena y muestra los nombres de los jugadores y su promedio de puntos por juego en orden ascendente.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa un jugador y
    sus estadísticas
    :param key: La clave es una cadena que representa la clave en el diccionario de cada jugador que
    queremos usar para los cálculos. Por ejemplo, si queremos calcular la media de puntos por partido,
    la clave sería "estadisticas"
    :param parametro: El parámetro que se usará para calcular el promedio de puntos por juego para cada
    jugador en la lista
    :return: nada (es decir, Ninguno).
    """

    resultado = calcular_promedio(lista_jugadores, key, parametro)
    print("El promedio de puntos por partido es: {0}".format(resultado))
    lista_auxiliar = []
    for jugadores in lista_jugadores:
       diccionario_auxiliar = {}
       diccionario_auxiliar["nombre"] = jugadores["nombre"]
       diccionario_auxiliar["promedio_puntos_por_partido"] = jugadores["estadisticas"]["promedio_puntos_por_partido"]
       lista_auxiliar.append(diccionario_auxiliar)
    
    retorno_quick = quick_sort_diccionarios(lista_auxiliar,"nombre", flag_orden = True)
    mostrar_nombre_parametro_y_valor(retorno_quick, "promedio_puntos_por_partido")
    
    return 

def mostrar_jugadores__salon_fama(lista_jugadores, parametro): #PUNTO 6
    """
    La función toma una lista de jugadores y un parámetro, busca los logros de los jugadores e imprime
    si cada jugador tiene el parámetro especificado o no.
    
    :param lista_jugadores: una lista de diccionarios que contienen información sobre los jugadores
    :param parametro: El parámetro es una cadena que representa un determinado logro o característica
    que puede tener un jugador. La función buscará en una lista de jugadores y sus logros para
    determinar qué jugadores tienen el parámetro especificado e imprimirá un mensaje indicando si lo
    tienen o no
    :return: nada (es decir, ninguno).
    """

    diccionario = buscar_jugador_mostrar_logros(lista_jugadores, "logros")
    lista_valor = []
    for i in diccionario:
        lista_valor.append(diccionario[i])
    
    for i in lista_valor:
        if parametro in i:
            print("Este jugador es {0}".format(parametro))
        else:
            print("Este jugador no es {0}". format(parametro))

    return 

def calcular_mostrar_maximo_parametro(lista_jugadores, key, parametro, maximo): #PUNTO 7, 8, 9, 13, 14, 19
    """
    Esta función calcula y muestra el jugador con el valor más alto para un parámetro dado en una lista
    de diccionarios.
    
    :param lista_jugadores: Es una lista de diccionarios que contienen información sobre los jugadores
    :param key: La clave es una cadena que representa la clave en el diccionario que queremos usar para
    comparar los valores de los jugadores. Por ejemplo, si tenemos un diccionario de jugadores con
    claves como "nombre", "edad", "puntuación", etc., elegiríamos una de estas claves para comparar el
    :param parametro: El parámetro que se analiza para encontrar el valor máximo
    :param maximo: El parámetro "maximo" es probablemente un valor que se utiliza para determinar el
    valor máximo de un determinado parámetro en un diccionario. No está claro en el código dado qué
    valor específico o tipo de datos debe ser "maximo"
    :return: nada (es decir, Ninguno).
    """


    lista_jugador_maximo_parametro = calcular_max_min_dato_de_diccionario(lista_jugadores, key, parametro, maximo)
    parametro_limpio = limpiar_cadena_de_no_alfanumericos(parametro)

    
    if len(lista_jugador_maximo_parametro) == 1:
        print("El jugador con la mayor cantidad de {0} es: ".format(parametro_limpio))
        mostrar_nombre_parametro_y_valor(lista_jugador_maximo_parametro,  parametro )
    else: 
        print("El jugador con la mayor cantidad de {0} son: ".format(parametro_limpio))
        mostrar_nombre_parametro_y_valor(lista_jugador_maximo_parametro,  parametro )
        
    return 

def comparar_y_mostrar_valor_usuario_con_parametro(lista_jugadores, key, parametro, posicion): # PUNTO 10, 11, 12, 15, 18, 20
    """
    Esta función compara un valor ingresado por el usuario con un parámetro específico de cada jugador
    en una lista de jugadores e imprime los nombres de los jugadores cuyo valor de parámetro es mayor
    que el valor ingresado por el usuario.
    
    :param lista_jugadores: una lista de diccionarios que contienen información sobre los jugadores
    :param key: La clave es una cadena que representa la clave en el diccionario de cada jugador que
    queremos comparar. Por ejemplo, si queremos comparar la "edad" de cada jugador, la clave sería
    "edad"
    :param parametro: El parámetro "parámetro" es una variable que representa la clave específica dentro
    del diccionario anidado de la información de cada jugador con la que la función comparará el valor
    ingresado por el usuario. Por ejemplo, si el diccionario anidado de cada jugador incluye claves para
    "edad", "altura" y "peso", el "
    :return: nada (es decir, ninguno).
    """

    numero_ingresado = input("Ingrese valor que quiera comparar: ")
    numero_formateado = validar_int_o_float(numero_ingresado)
    parametro_formateado = limpiar_cadena_de_no_alfanumericos(parametro)
    
    lista_auxiliar = []
    print("Los jugadores que tienen mayor valor que el ingresado son:\n")
    
    if posicion == False:
        for jugadores in lista_jugadores:
            diccionario_auxiliar = {}
            if numero_formateado <= jugadores[key][parametro]:
                diccionario_auxiliar["nombre"]= jugadores["nombre"]
                diccionario_auxiliar[parametro_formateado] = jugadores[key][parametro]
                lista_auxiliar.append(diccionario_auxiliar) 
        mostrar_nombre_parametro_y_valor(lista_auxiliar, parametro_formateado)

    elif posicion == True:
        for jugadores in lista_jugadores:
            diccionario_auxiliar = {}
            if numero_formateado <= jugadores[key][parametro]:
                diccionario_auxiliar["nombre"]= jugadores["nombre"]
                diccionario_auxiliar["posicion"] = jugadores["posicion"]
                lista_auxiliar.append(diccionario_auxiliar)
        retorno = quick_sort_diccionarios(lista_auxiliar, "posicion", flag_orden = True)
        mostrar_nombre_parametro_y_valor(retorno, "posicion")
        
        return 

def calcular_mostrar_promedio_de_puntos_ordenado_sin_el_menor(lista_jugadores, key , parametro): # PUNTO 16
    """
    Esta función calcula y muestra el promedio de puntos por juego para una lista de jugadores,
    ordenados por nombre, excluyendo al jugador con el promedio de puntos más bajo.
    
    :param lista_jugadores: Una lista de diccionarios que representan a jugadores de baloncesto, cada
    uno con una tecla "nombre" (cadena) y una tecla "estadisticas" (diccionario) que contiene varias
    estadísticas, incluido "promedio_puntos_por_partido" (flotante)
    :param key: "estadisticas"
    :param parametro: El parámetro es una cadena que representa la clave del valor que se utilizará para
    calcular el promedio. Se utiliza en la función "calcular_promedio"
    :return: Ninguno.
    """
    

    lista_auxiliar = []
    for jugadores in lista_jugadores:
       diccionario_auxiliar = {}
       diccionario_auxiliar["nombre"] = jugadores["nombre"]
       diccionario_auxiliar["promedio_puntos_por_partido"] = jugadores[key][parametro]
       lista_auxiliar.append(diccionario_auxiliar)
    
    lista_sin_el_menor = []
    lista_retorno = calcular_max_min_dato_de_diccionario(lista_jugadores, key, parametro, maximo= False)
    for personajes in lista_auxiliar:
        for persona in lista_retorno:
            if personajes["nombre"] != persona["nombre"]:
                lista_sin_el_menor.append(personajes)
                
    retorno_quick = quick_sort_diccionarios(lista_sin_el_menor,"nombre", flag_orden = True)
    mostrar_nombre_parametro_y_valor(retorno_quick, parametro)

    resultado = calcular_promedio_sin_el_menor(lista_sin_el_menor,  parametro)
    print("\nEl promedio de puntos por partido es: {0}".format(resultado))
    return 

def calcular_mostrar_mayor_cantidad_logros(lista_jugadores, key ): # PUNTO 17
    """
    Esta función calcula y muestra el jugador con el mayor número de logros en una lista de jugadores.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene información como su nombre y logros
    :param key: El parámetro "clave" es una cadena que representa el tipo de logros que la función está
    calculando y comparando para cada jugador en la "lista_jugadores" (lista de jugadores). Podría ser
    algo así como "puntos" (puntos), "goles" (goles
    :return: nada (es decir, ninguno). Solo está imprimiendo un mensaje a la consola.
    """

    jugador_mayor_logros = None
    logros = []

    jugadores_mayor_logros = []
    cantidad_max_logros = 0
    
    for jugador in lista_jugadores:
        logros = jugador["logros"]
        num_logros = len(logros)
        if num_logros > cantidad_max_logros:
            jugador_mayor_logros = jugador["nombre"]
            cantidad_max_logros = num_logros
        elif num_logros == cantidad_max_logros:
            jugadores_mayor_logros.append(jugador["nombre"])

    print("El jugador con mayor cantidad de logros es {0} con: {1} {2}".format(jugador_mayor_logros, cantidad_max_logros, key))

    return 


def imprimir_menu():
    """
    Esta función imprime un menú con 20 opciones diferentes para que el usuario elija, cada una
    relacionada con estadísticas e información sobre los jugadores de baloncesto del Dream Team.
    """
   
    print("\n______ Menú de opciones ______")
    print("1. Mostrar la lista de todos los jugadores del Dream Team")
    print("2. Seleccionar un jugador por su índice y mostrar sus estadísticas completas")
    print("3. Guardar las estadísticas de ese jugador en un archivo CSV")
    print("4. Buscar un jugador por su nombre y mostrar sus logros")
    print("5. Calcular y mostrar el promedio de puntos por partido de todo el"
           "equipo del Dream Team, ordenado por nombre de manera ascendente.")
    print("6. ingresar el nombre de un jugador y mostrar si ese jugador es"
          " miembro del Salón de la Fama del Baloncesto.")
    print("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales")
    print("8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo")
    print("9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.")
    print("10. ingresar un valor y mostrar los jugadores que han promediado más "
          "puntos por partido que ese valor.")
    print("11. ingresar un valor y mostrar los jugadores que han promediado" 
          "más rebotes por partido que ese valor.")
    print("12. ingresar un valor y mostrar los jugadores que han promediado"
          " más asistencias por partido que ese valor.")
    print("13. Calcular y mostrar el jugador con la mayor cantidad de robos totales")
    print("14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.")
    print("15. ingresar un valor y mostrar los jugadores que hayan tenido un "
          "porcentaje de tiros libres superior a ese valor.")
    print("16. Calcular y mostrar el promedio de puntos por partido del equipo" 
          "excluyendo al jugador con la menor cantidad de puntos por partido.")
    print("17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.")
    print("18. ingresar un valor y mostrar los jugadores que hayan tenido un "
          "porcentaje de tiros triples superior a ese valor.")
    print("19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.")
    print("20. ingresar un valor y mostrar los jugadores , ordenados por "
    "posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.")
    print("23. Calcular de cada jugador cuál es su posición en cada uno de los "
          "siguientes ranking: Puntos,Rebotes,Asistencias, Robos.")
    print("0. Salir")

def menu_principal():
    """
    Esta función muestra un menú y solicita al usuario que ingrese una opción, que luego se valida y se
    devuelve.
    :return: la opción validada seleccionada del menú.
    """
    
    while True:
        imprimir_menu()
        string = input("\nIngrese la opción deseada: ")
        opcion_validado = validar_opcion_del_menu(string)
        return opcion_validado
    
def principal(lista_jugadores):
    """
    Esta es la función principal de un programa de estadísticas de baloncesto que muestra un menú de
    opciones para que el usuario elija y realiza varias operaciones en una lista de datos de jugadores
    de baloncesto en función de la entrada del usuario.

    :param lista_jugadores: Es una lista de diccionarios que contienen información sobre los jugadores
    de baloncesto, incluidas sus estadísticas y logros
    """

bandera_opcion_3 = 0
while True:
    opcion = menu_principal()
    match opcion: 
            case 1:   
                mostrar_nombre_parametro_y_valor(lista_jugadores, "posicion")
            case 2:
                diccionario_jugador = mostrar_informacion_jugador(lista_jugadores)
                if len(diccionario_jugador) > 0:
                    bandera_opcion_3 = 1
            case 3:
                if bandera_opcion_3 == 0:
                    print("------ ERROR ------ Debe ingresar primero a la opcion 2 del menu")
                elif bandera_opcion_3 == 1: 
                    guardar_estadisticas_en_csv(r"C:\\Users\\blair\\Documents\\GitHub\\pp_lab1_wlach_valeria_natalia\\jugador_estadistica.csv", diccionario_jugador) 
            case 4:
                diccionario_logros = buscar_jugador_mostrar_logros(lista_jugadores, "logros")
                mostrar_nombre_parametro_y_valor(diccionario_logros,"logros" )
            case 5:
                calcular_mostrar_promedio_de_puntos_ordenado(lista_jugadores, "estadisticas", "promedio_puntos_por_partido")
            case 6:
                mostrar_jugadores__salon_fama(lista_jugadores, "Miembro del Salon de la Fama del Baloncesto")
            case 7:
                calcular_mostrar_maximo_parametro(lista_jugadores, "estadisticas", "rebotes_totales", maximo = True)
            case 8:
                calcular_mostrar_maximo_parametro(lista_jugadores, "estadisticas", "porcentaje_tiros_de_campo", maximo = True)
            case 9:
                calcular_mostrar_maximo_parametro(lista_jugadores, "estadisticas", "asistencias_totales", maximo = True)
            case 10:
                comparar_y_mostrar_valor_usuario_con_parametro(lista_jugadores, "estadisticas", "promedio_puntos_por_partido", posicion = False )
            case 11:
                comparar_y_mostrar_valor_usuario_con_parametro(lista_jugadores, "estadisticas", "promedio_rebotes_por_partido", posicion = False )
            case 12:
                comparar_y_mostrar_valor_usuario_con_parametro(lista_jugadores, "estadisticas", "promedio_asistencias_por_partido", posicion = False )
            case 13:
                calcular_mostrar_maximo_parametro(lista_jugadores, "estadisticas", "robos_totales", maximo = True)
            case 14:
                calcular_mostrar_maximo_parametro(lista_jugadores, "estadisticas", "bloqueos_totales", maximo = True)
            case 15:
                comparar_y_mostrar_valor_usuario_con_parametro(lista_jugadores, "estadisticas", "porcentaje_tiros_libres", posicion = False)
            case 16:
                calcular_mostrar_promedio_de_puntos_ordenado_sin_el_menor(lista_jugadores, "estadisticas", "promedio_puntos_por_partido")
            case 17:
                calcular_mostrar_mayor_cantidad_logros(lista_jugadores, "logros" )
            case 18:
                comparar_y_mostrar_valor_usuario_con_parametro(lista_jugadores, "estadisticas", "porcentaje_tiros_triples", posicion = False)
            case 19:
                calcular_mostrar_maximo_parametro(lista_jugadores, "estadisticas", "temporadas", maximo = True)
            case 20:
                comparar_y_mostrar_valor_usuario_con_parametro(lista_jugadores, "estadisticas", "porcentaje_tiros_de_campo", posicion = True )
            case 23:
                print("Lo siento, prefiero tener todo lo mas correcto posible :)")
            case 0:
                print("___________________________________________________________________\n")
                print("________ SALIENDO________")
                print("___________________________________________________________________\n\n\n")
                break
