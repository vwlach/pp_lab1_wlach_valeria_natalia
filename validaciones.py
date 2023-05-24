import re

def validar_opcion(string: str) ->str:
    '''
    valida que la encuentre la opcion correcta
    recibe un string
    retorna el string si se equivoca el usuario retorna un  mensaje de error 
    '''

    if re.search(r'(^2[0-3]$|^[0-1]?[0-9]$|([21|22)$)',string ) != None:
        if string.isdigit():
            retorno = int(string)
            return retorno
    else:
        print("------ ERRORRRR ------ Ingrese una opcion correcta (0 - 23)")
        pass

 