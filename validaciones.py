import re

def validar_opcion_del_menu(string: str) -> int:
    """
    Esta función valida si una cadena dada es una opción de menú válida (entero entre 0 y 23, excluyendo
    21 y 22) y devuelve el valor entero si es válido.
    
    :param string: una cadena que representa la entrada del usuario para una opción de menú
    :type string: str
    :return: un número entero que representa una opción válida de un menú, o Ninguno si la cadena de
    entrada no es una opción válida.
    """
   

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
    """
    La función valida si una entrada de cadena es un número entero o flotante válido y devuelve el valor
    correspondiente.
    
    :param string_ingresado: una cadena que representa un número, ya sea un entero o un flotante
    :type string_ingresado: str
    :return: un valor entero o flotante dependiendo de la cadena de entrada. Si la cadena de entrada se
    puede convertir en un número entero, devuelve un valor entero. Si la cadena de entrada se puede
    convertir en un valor flotante, devuelve un valor flotante. Si la cadena de entrada no es un valor
    numérico válido, imprime un mensaje que solicita al usuario que ingrese un valor numérico válido.
    """

    if string_ingresado.isdigit():
        return int(string_ingresado)
    elif re.match(r'^\d+(\.\d+)?$', string_ingresado):
        return float(string_ingresado)
    else:
        print("Ingrese un valor numérico válido (entero o decimal).")

def limpiar_cadena_de_no_alfanumericos(cadena):
    """
    La función toma una cadena como entrada y elimina todos los caracteres no alfanuméricos,
    reemplazándolos con espacios.
    
    :param cadena: una cadena que puede contener caracteres no alfanuméricos que deben eliminarse
    :return: la cadena limpia con todos los caracteres no alfanuméricos reemplazados por un espacio.
    """
    
    cadena_limpia = re.sub(r'[^a-zA-Z0-9]', ' ', cadena)

    return cadena_limpia
