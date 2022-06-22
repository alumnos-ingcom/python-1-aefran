# Franco Roma - @aefran
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si una palabra o frase
ingresada se trata de un palindromo. Palíndromo, es si se lee
igual de derecha a izquierda que de izquierda a derecha.
"""

# Funciones// def - while - if - print - input - return
def es_palindromo(texto):
    i=0
    coincidencias=0
    while i<=(len(texto)//2):
        if texto[i]==texto[-(1+i)]:
            coincidencias+=1
        i+=1
    return coincidencias>(len(texto)//2)
"""
La funcion def es_palindromo pide el valor que esta guardado en la variable texto
La funcion def es_palindromo declara 2 variables i y coincidencias
La funcion def es_palindromo verifica si las palabra ingresada en la variable texto puede escribirse igual de derecha a izquierda que de izquierda a derecha
La funcion def es_palindroma retorna que en caso de que coincidencias>(len(texto)//2) te devolvera True y en caso de que no se cumpla te devolvera false
"""
def principal():
    texto=str(input("ingrese una cadena de texto: "))
    print(es_palindromo(texto))
"""
La funcion def principal pide que se ingrese una cadena de texto y guardara dicha cadena en la variable texto
La funcion def principal mostrara el contenido de la funcion es_palindromo
"""
if __name__ == "__main__":
    principal()
"""
Se encarga de ejecutar el programa principal
"""