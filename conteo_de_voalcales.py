cadena = "hola mundo"
vocales = "aeiouáéíóú"
contador = sum(1 for letra in cadena if letra in vocales)
print("El número de vocales en la cadena es:", contador)
