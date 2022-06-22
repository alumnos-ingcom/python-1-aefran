################
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""

# Funcion// def - if - return - input - print
def compara(numero, otro_numero):
    if numero+numero>numero+otro_numero:
        resultado=1
    elif numero+numero<numero+otro_numero:
        resultado=-1
    else: 
        resultado=0

    return resultado
"""
La funcion def compara pide los valores guardados en las variables numero y otro_numero
La funcion def compara, suma el valor de numero con si mismo para luego compararlo con la suma de numero con otro_numero determinando si es 1,-1 o 0 guardandolo en la variable resultado
La funcion retorna el valor guardado en resultado 
"""
def principal():
    numero=int(input("ingrese un numero"))
    otro_numero=int(input("ingrese otro numero"))
    print(compara(numero,otro_numero))
"""
La funcion def principal se encarga de pedir los valores a guardar en las variables numero y otro_numero respectivamente
La funcion def muestra el valor guardado en la funcion compara
"""
if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""