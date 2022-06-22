################
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Numeros Positivos y Negativos
Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.
"""

# Funciones// def - return - if - print - input 



def signo(numero):
    sum=numero+numero

    if(sum>numero):
        resultado="es positivo"
    elif sum<numero:
        resultado= "es negativo"
    else:
        resultado="es cero"

    return resultado
    pass
"""
La funcion def signo llama a la varible numero
La funcion def signo suma la variable numero con sigo mismo y guarda el valor reultante en la variable sum
La funcion def signo compara la sumatoria de los numero para determina si la misma es negativa, positica o cero, guardando dicho valor en la variable resultado
La funcion retorna el valor de resultado
"""
def principal():
    numero=int(input("Ingrese un numero: "))
    print(signo)
"""
La funcion def principal se encarga de pedir el ingreso de valor que se le asignara a variable numero
La funcion def principal mostrara el valor de signo
"""
if __name__ == "__main__":
    signo()
"""
Se encarga de ejecutar el programa principal
"""