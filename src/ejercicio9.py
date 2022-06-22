# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
"""
# Funciones// tuple - def - return - while - if - print - input

def factores_primos(numero):
    divisor=2
    i=0
    factores=[]
    numerito=numero
    while divisor*divisor<numero:
        if numerito%divisor==0:
            numerito=numerito//divisor
            factores=factores+[divisor]
            divisor=1
        divisor+=1
    factores=factores+[numerito]
    tupla_de_factores=tuple(factores)
    return tupla_de_factores
"""
La funcion def factores_primo pide el valor guardado en la varibale numero
La funcion def factores_primo declara las variables divisor, i, factores y numerito
La funcion def factores_primo varifica que numeros son factores primos del numero y los va guardando en una tupla
La funcion def factores_primo retorna el valor guardado en tupla_de_factores
"""

def principal():
    numero=int(input("Ingrese un numero entero positivo: "))
    print(factores_primos(numero))
"""
La funcion def principal pide que se ingrese un valor entero positivo y lo guarda en la varibale numero
La funcion def principal muestra la funcion factores_primos
"""
if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""