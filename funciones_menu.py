from validaciones import *
from calculos import *
import json
import re

def parse_json(ruta_json:str):

    lista_vacia = []
    with open(ruta_json, 'r', encoding="utf-8") as archivo:
        diccionario = json.load(archivo)
        lista_vacia = diccionario["jugadores"]

    return lista_vacia

ruta_json = r"C:\\Users\\blair\\Documents\\GitHub\\pp_lab1_wlach_valeria_natalia\\dt.json"

lista_jugadores = parse_json(ruta_json)

def mostrar_nombre_y_parametro(lista_o_diccionario: list or dict, parametro: str ):
    """
    recibe la lista de jugadores y un parametro y los imprime y parsea el parametro
    recibe una lista
    no retona nada, imprime por pantalla
    """
    if type(lista_o_diccionario) == list:
        for jugadores in lista_o_diccionario:
            nombre = jugadores["nombre"]
            x_parametro = jugadores[parametro]
            print("{0} - {1}: {2}".format(nombre, parametro.capitalize(), x_parametro))

    elif type(lista_o_diccionario) == dict:
        for clave in lista_o_diccionario:
            valor = lista_o_diccionario[clave]
            print("{0} - {1}: {2}".format(clave.capitalize(), parametro.capitalize(),  valor))

    return 
def limpiar_cadena_de_no_alfanumericos(cadena):
    
    cadena_limpia = re.sub(r'[^a-zA-Z0-9]', ' ', cadena)

    return cadena_limpia

def mostrar_informacion_jugador(lista_jugadores: list) -> dict:
    '''
    muestra los jugadores para que el usuario pueda elegir cual desea imprimir por pantalla ingresando su indice y a la vez
    se guarda la informacion para ser utilizada porteriormente
    recibe una lista 
    retorna un diccionario

    '''

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
            
    mostrar_nombre_y_parametro(diccionario_jugador, None )
    
    return diccionario_jugador

def guardar_estisticas_en_csv(ruta_file:str, contenido:dict):
    """
    La función es básicamente un bucle que recorre las claves y valores del diccionario 
    contenido y los escribe en el archivo CSV de forma formateada. Luego, muestra un mensaje
    indicando que el archivo se creó correctamente.
    recibe 
    recibe un str con la ruda donde se va a guardar el csv
    no retorna nada, imprime por pantalla si se logra crear el archivo
    """
    with open(ruta_file, 'w+') as archivo:
        for clave in contenido:
            valor = contenido[clave]
            archivo.write("{0}: {1}\n".format(clave.capitalize(), valor))
    if len(contenido) > 0:
        print("Se creo el archivo con exito")
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

def calcular_mostrar_promedio_de_puntos_ordenado(lista_jugadores, key , parametro):
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
    mostrar_nombre_y_parametro(retorno_quick, "promedio_puntos_por_partido")
    
    return 

def mostrar_jugadores__salon_fama(lista_jugadores, parametro):
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

def calcular_mostrar_maximo_parametro(lista_jugadores, key, parametro, maximo):
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


    jugador_maximo_parametro = calcular_max_min_dato_de_diccionario(lista_jugadores, key, parametro, maximo)
    parametro_limpio = limpiar_cadena_de_no_alfanumericos(parametro)
    print("El jugador con la mayor cantidad de {0} es: {1}".format(parametro_limpio, jugador_maximo_parametro ))

    return 

def imprimir_menu():
    '''
    imprime  las opciones del menu
    '''
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
    '''
    funcion principal donde llama a imprimir menu, y le pide al usuarioq ingrese una opcion
    y llama a una funcion para validarla
    devuelve la opcion validada 
    '''
    
    while True:
        imprimir_menu()
        string = input("\nIngrese la opción deseada: ")
        opcion_validado = validar_opcion(string)
        return opcion_validado
    
def principal(lista_jugadores):

    '''
    esta funcion tiene una bandera que no deja que ingrese a la ocpion 6 sin ingresar primero a las opciones
    [1-4] dentro de un bucle llama al menu principal y normaliza los datos y recibe la opcion
    que hace que ingrese en cada opcion del menu donde llama a las funciones
    recibe la lista de personajes

    '''

while True:
    opcion = menu_principal()
    bandera_opcion_3 = True

    match opcion: 
            case 1:   
               mostrar_nombre_y_parametro(lista_jugadores, "posicion")
            case 2:
                #mirar esto
                diccionario_jugador = mostrar_informacion_jugador(lista_jugadores)
                bandera_opcion_3 = False
            case 3:
                if bandera_opcion_3: #volver a ver lo de la bandera
                    guardar_estisticas_en_csv(r"C:\\Users\\blair\\Documents\\GitHub\\pp_lab1_wlach_valeria_natalia\\jugador_estadistica.csv", diccionario_jugador)
                elif bandera_opcion_3 == True:
                    print("------ ERROR ------ Debe ingresar primero a la opcion 2 del menu")
            case 4:
                diccionario_logros = buscar_jugador_mostrar_logros(lista_jugadores, "logros")
                mostrar_nombre_y_parametro(diccionario_logros,"logros" )
                
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
                pass
            case 11:
                pass
            case 12:
                pass
            case 13:
                pass
            case 14:
                pass
            case 15:
                pass
            case 16:
                pass
            case 17:
                pass
            case 18:
                pass
            case 19:
                pass
            case 20:
                pass
            case 23:
                pass
            case 0:
                print("___________________________________________________________________\n")
                print("________ SALIENDO________")
                print("___________________________________________________________________\n\n\n")
                break
