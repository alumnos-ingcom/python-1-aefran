################
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir un programa que permita transformar un número solicitado
expresado en grados, minutos y segundos a segundos. 
Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.
"""

# Funciones// def - return - if - print - input - tupla

def sexadecimal_a_decimal(horas, minutos, segundos):
    resultado= horas*3600+minutos*60+segundos
    return resultado
"""
La funcion def sexadecimal_a_decimal pide los valores de las variable horas, minutos y segundos
La funcion def sexadecimal_a_decimal hace la conversion de sexadecimal a decimal y guarda el valor en la variable resultado
La funcion def sexadecimal_a_decimal retorna resultado
"""
def decimal_a_sexadecimal(numero):
    minutos=numero//60
    numero=numero-minutos*60
    horas=minutos//60
    minutos=minutos-horas*60
    resultado=[horas,minutos,numero]
    tupla_resultado=tuple(resultado)
    return tupla_resultado
"""
La funcion def decimal_a_sexadecimal pide el valor de la variable numero
La funcion def decimal_a_sexadecimal hace la conversion de decimal a sexadecimal y guarda el valor en la variable resultado
La funcion def decimal_a_sexadecimal retorna resultado
"""
def principal():
    horas=int(input("ingrese las horas: "))
    minutos=int(input("ingrese las minutos: "))
    segundos=int(input("ingrese los segundos: "))
    segundos_totales=sexadecimal_a_decimal(horas,minutos,segundos)
    print(segundos_totales)
    print(decimal_a_sexadecimal(segundos_totales))
"""
La funcion principal pide que se ingresen 3 valores que seran guardados en las variables horas, minutos y segundos respectivamente
La funcion principal declara la variable segundos_totales guardandole el valor de la funcion sexadecimal_a_decimal
La funcion principal muestra el valor de segundos_totales
La funcion principal muestra el valor de la funcion decimal_a_sexadecimal
"""
if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""