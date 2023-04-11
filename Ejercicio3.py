#Se ingresa una palabra aleatoria
palabra = input("Ingrese una palabra: ")
vocales = ["a", "e", "i", "o", "u"]
vocales_contador = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

# Se recorre cada letra de la palabra utilizando un bucle
# Si la letra es una vocal, se incrementa el contador 
for letra in palabra:
    if letra.lower() in vocales:
        vocales_contador[letra.lower()] += 1

#Imprime la contida de cada vocales que contenga la palabra
print("La palabra", palabra, "contiene:")
for vocal, contador in vocales_contador.items():
    print("-", contador, "veces la vocal", vocal)