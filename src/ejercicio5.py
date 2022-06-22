################
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
"""

# Funciones// def - return - while - print - input - if

def division_lenta(dividendo, divisor):
    resultado=0
    operador=dividendo
    while operador>=divisor:
        operador=operador-divisor
        resultado+=1
    resto=dividendo-(divisor*resultado)
    return resultado,resto
"""
La funcion division_lenta toma los valores de las variables dividendo y divisor 
La funcion division_lenta define las variables resultado y operador
La funcion division_lenta utiliza las variables dentro de un while utilando restas sucesivas, guardando los resultados en las variables resultado y resto
La funcion division_lenta retorna las varibles resultado y resto
"""
def principal():
    
    dividendo=int(input("ingrese un numero: "))
    divisor=int(input("ingrese otro numero: "))
    print(division_lenta(dividendo,divisor))
    
    """
    La funcion def principal pide los valores para las variables dividendo y divisor
    La funcion muestra los valores guardados en la funcion division_lenta 
    """
    pass

if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""