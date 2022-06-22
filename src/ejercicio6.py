################
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que a partir de tres variables de tipo
entero retorne una tupla con dichos valores ordenados de 
menor a mayor. Y Viceversa
"""

# Funciones// def - if - return - print - input - tupla

def ordenar_mayor_a_menor(uno, dos, tres):
    if uno>dos:
        if dos > tres:
            resultado=[uno,dos,tres]
        elif uno>tres:
            resultado=[uno,tres,dos]
        else:
            resultado=[tres,uno,dos]
    elif dos>uno:
        if uno>tres:
            resultado = [dos,uno,tres]
        elif dos>tres:
            resultado = [dos,tres,uno]
        else:
            resultado = [tres,dos,uno]
    else:
        resultado=[uno,dos,tres]
    tupla_resultado=tuple(resultado)
    return tupla_resultado
"""
La funcion def ordenar_mayor_a_menor llama a las valores de las variables uno, dos y tres
La funcion def ordenar_mayor_a_menor acomoda los valores de las variables de mayor a menor y los guarda en la variable resultado
La funcion def ordenar_mayor_a_menor retorna resultado
"""
def ordenar_menor_a_mayor(uno, dos, tres):
    if uno<dos:
        if dos < tres:
            resultado=[uno,dos,tres]
        elif uno<tres:
            resultado=[uno,tres,dos]
        else:
            resultado=[tres,uno,dos]
    elif dos<uno:
        if uno<tres:
            resultado = [dos,uno,tres]
        elif dos<tres:
            resultado = [dos,tres,uno]
        else:
            resultado = [tres,dos,uno]
    else:
        resultado=[uno,dos,tres]

    tupla_resultado=tuple(resultado)
    return tupla_resultado
"""
La funcion def ordenar_menor_a mayor llama a los valores de las variables uno, dos y tres
La funcion def ordenar_menor_a mayor ordena los valores de las variables de menor a mayor y luego los guarda en la variable resultado
La funcion def ordenar_menor_a mayor returnea resultado
"""
def principal():
    numero_uno=int(input("ingrese un numero: "))
    numero_dos=int(input("ingrese otro numero: "))
    numero_tres=int(input("ingrese un ultimo numero: "))
    print(ordenar_mayor_a_menor(numero_uno,numero_dos,numero_tres))
    print(ordenar_menor_a_mayor(numero_uno,numero_dos,numero_tres))
"""
La funcion def principal pide el ingreso de 3 valores que seran guardados en las variable numero_uno, numero_dos y numero_tres respectivamente
La funcion se encarga de mostrar los valores almacenados en las funciones ordenar_mayor_a_menor y ordenar_menor_a_mayor    
"""

if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""