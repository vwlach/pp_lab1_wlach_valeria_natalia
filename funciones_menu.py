from validaciones import *
import json
import re




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
    
def principal(lista_personajes):

    '''
    esta funcion tiene una bandera que no deja que ingrese a la ocpion 6 sin ingresar primero a las opciones
    [1-4] dentro de un bucle llama al menu principal y normaliza los datos y recibe la opcion
    que hace que ingrese en cada opcion del menu donde llama a las funciones
    recibe la lista de personajes

    '''

while True:
    opcion = menu_principal()
    
    match (opcion): 
            case 1:   
                pass
            case 2:
                pass
            case 3:
                pass
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
