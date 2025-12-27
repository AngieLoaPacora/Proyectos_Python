"""
Funcion any()
"""


def ejemplo_any_001():
    valores = [False, False, True]
    resultado_001 = any(valores)
    print(resultado_001)


def ejemplo_any_002():
    numeros = [0, 0, 0, 5]
    resultado = any(numeros)
    print(resultado)


vacia = []


def ejemplo_any_003():
    resultado = any(vacia)
    print(resultado)


def verificar_contrasena(contrasena):
    # Verificar longitud minima (8 caracteres)
    if len(contrasena) < 8:
        return False
    #Verificar si ontiene al menos un numero
    if not any(char.isdigit() for char in contrasena):
        return False
    #si tiene al menos una letra mayuscula
    if not any(char.isdigit() for char in contrasena):
        return False
    #Verificar si contiene al menos un caracter especial(@, #, $, etc)
    especiales="@#$%^()-_+=¡"
    if not any(char in especiales for char in contrasena):
        return False
    #todo si pasa todas las verificaciones, la contrasena es segura
    return True
#todo Ejemplo de Uso
clave="Segur@123"
print(verificar_contrasena(clave))

