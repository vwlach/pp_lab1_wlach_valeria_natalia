from validaciones import *
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

def mostrar_nombre_y_parametro(lista_o_diccionario: list or dict, parametro: str):
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
            print("{0}: {1}".format(clave.capitalize(), valor))

    return 

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
                diccionario_jugador = mostrar_informacion_jugador(lista_jugadores)
                bandera_opcion_3 = False
            case 3:
                if bandera_opcion_3:
                    guardar_estisticas_en_csv(r"C:\\Users\\blair\\Documents\\GitHub\\pp_lab1_wlach_valeria_natalia\\jugador_estadistica.csv", diccionario_jugador)
                elif bandera_opcion_3 == True:
                    print("------ ERROR ------ Debe ingresar primero a la opcion 2 del menu")
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
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
