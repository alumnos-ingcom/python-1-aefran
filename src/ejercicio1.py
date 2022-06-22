###############
# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir las funciones para convertir la temperatura en grados centigrados
en fahrenheit como un número decimal, utilice esta formula para calcular 
los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""

# Funciones// def- return - print - input

def convertir_a_fahrenheit(centigrados):
    fahrenheit = centigrados*1.8 + 32
    return fahrenheit
    """
    La funcion def convertir_a_fahrenheit llama a el valor de la variable centigrados
    La funcion def convertir_a_fahrenheit se encarga de realizar la conversion de grados centigrados a grados fahrenheit guardando el resultado en la variable fahrenheit
    La funcion retorna el nuevo valor de fahrenheit
    """

def convertir_a_centigrados(fahrenheit):
    centigrados= (fahrenheit-32)/1.8
    return centigrados
    """
    La funcion def convertir_a_centigrados llama a el valor de la variable fahrenheit 
    La funcion def convertir_a_centigrados se encarga de realizar la conversion de grados fahrenheite a grados centigrados guardando el resultado en la variable centigrados
    La funcion retorna el nuevo valor de centigrados
    """

    pass
def principal():
    centigrados=int(input("Ingrese una temperatura en grados centigrados: "))
    fahrenheit=int(input("Ingrese una temperatura en grados fahrenheit: "))
    centigrados=convertir_a_fahrenheit(centigrados)
    fahrenheit=convertir_a_centigrados(fahrenheit)
    print(centigrados)
    print(fahrenheit)
"""
La funcion def principal se encarga de pedir los valores que seran guardados en las variables centigrados o fahrenheit respectivamente
La funcion def principal se encarga de tomar los valores transformados guardados de las funciones convertir_a_fahrenheit o convertir_a_centigrados
La funcion def principal se encarga de mostrar los valores de las variables centigrados y fahrenheit
"""

if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""