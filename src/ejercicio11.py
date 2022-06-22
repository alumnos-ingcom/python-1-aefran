################
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un número entero es multiplo de otro, utilizando sumas y restas.
"""

# Funciones// def - print - while - return - if - input


def signo(numero,multiplo):
    sum=0
    while sum!=multiplo and sum<multiplo:
        sum=sum+numero
        print(sum)
    
    return sum==multiplo
"""
La funcion def signo pide los valores de numero y multiplo
La funcion def signo declara la variable sum 
La funcion def signo determina los dominios de la funcion dentro de un while
La funcion def signo muestra los reltudos parciales de suma
La funcion def signo determina si la varible suma es igual a multiplo y lo retorna 
"""
def principal():
    numero=int(input("ingrese un numero: "))
    multiplo=int(input("ingrese un numero para verificar si es multiplo del anterior: "))
    print(signo(numero,multiplo))
"""
La funcion def principal se encarga de pedir los valores para las varibles numero y multiplo respectivamente
La funcion se encarga de mostrar los resultados de la funcion signo
"""

if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""