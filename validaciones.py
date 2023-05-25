import re

def validar_opcion(string: str) -> int:
    '''
    Valida que se ingrese una opción correcta.
    Recibe un string y retorna un entero si es una opción válida.
    Si el usuario se equivoca, muestra un mensaje de error y retorna -1.
    '''

    if string.isdigit():
        opcion = int(string)
        if opcion >= 0 and opcion <= 23 and opcion != 21 and opcion != 22:
            return opcion
        else: 
            print("------ ERROR ------ Ingrese una opción válida (0 - 23 [NO 21-22])")
    else:
        print("------ ERROR ------ Ingrese una opción válida (0 - 23 [NO 21-22])")
def validar_opcion_2(string: str) -> int:

    if string.isdigit():
        opcion = int(string)
        if opcion >= 0 and opcion <= 11:
            return opcion
        else: 
            print("------ ERROR ------ Ingrese una opción válida (0 - 11)")
            pass
    else:
        print("------ ERROR ------ Ingrese una opción válida (0 - 11)")
        pass

 