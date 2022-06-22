#################
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que haga la suma entre dos números enteros
sin hacer la operación de manera directa. Esto quiere decir que 
para hacer la suma entre 4 y 3, las operaciones resultantes
deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""

# Funciones// def - if - while - print - input - return

def suma_lenta(numero, otro_numero):
    sumas=0
    if otro_numero<0:
        while sumas > otro_numero:
            numero=numero-1
            sumas=sumas-1
    else:
        while sumas < otro_numero:
            numero=numero+1
            sumas=sumas+1
    return numero
"""
La funcion def suma_lenta pide los valores guardados en las variables numero y otro_numero
La funcion def suma_lenta declara la varible sumas
La funcion def suma_lenta compara el valor de la varible otro_numero para luego por suma lenta ir guardando los valores de la suma en la variable sumas
La funcion retorna el valor de numero
"""
def principal():
    numero=int(input("ingrese un numero: "))
    otro_numero=int(input("ingrese otro numero: "))
    print(suma_lenta(numero,otro_numero))
"""
La funcion def principal pide que se ingresen valores para las varibles numero y otro_numero respectivamente
La funcion muestra el valor guardado en la funcion suma_lenta 
"""


if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""