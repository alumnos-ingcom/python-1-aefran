################
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un numero indicado es Primo.
"""

# Funciones// def - while - if - return - print - input 

def es_primo(numero):
    divisor=numero
    divisores=0
    while divisor>0:
        if numero%divisor==0:
            divisores+=1
        divisor-=1
    return divisores<3
"""
La funcion def es_primo pide el valor de la variable numero
La funcion def es_primo declara las variables divisor y divisores
La funcion def es_primo prueba para todos los valores entre el numero ingresado y 1, y cuenta cuantos de ellos son divisores 
La funcion def es_primo retorna la variable divisores<3 
"""
def principal():
    numero = int(input("ingrese un numero: "))
    print(es_primo(numero))
"""
La funcion def principal pide que se ingrese un valor que se guardara en la variable numero
La funcion mostrara el valor de la funcion es_primo
"""

if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""