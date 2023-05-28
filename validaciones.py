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
    """
    Esta función valida si una cadena determinada se puede convertir en un número entero entre 0 y 11.
    
    :param string: Una cadena que representa la entrada del usuario para una opción de menú
    :type string: str
    :return: un valor entero que representa la opción validada ingresada como una cadena. Si la cadena
    de entrada no es un entero válido o si no está dentro del rango de 0 a 11, se imprime un mensaje de
    error y la función devuelve Ninguno.
    """

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

def validar_int_o_float(string_ingresado: str):

    if string_ingresado.isdigit():
        return int(string_ingresado)
    elif re.match(r'^\d+(\.\d+)?$', string_ingresado):
        return float(string_ingresado)
    else:
        print("Ingrese un valor numérico válido (entero o decimal).")
        
