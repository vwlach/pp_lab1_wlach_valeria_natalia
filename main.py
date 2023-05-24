from funciones_menu import *

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
    
