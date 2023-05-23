#Obtener la determinante de una matriz de 3 x 3 con sus elementos aleatorios (5
#al 10, enteros positivos). Se pueden utilizar librerías para resolver el algoritmo.

#Importar libreria random
import random

#Definir la matriz con sus filas y columnas 3x3
matriz = [[random.randint(5,10)for i in range(3) for j in range(3)]]

#Imprimir la matriz resultante
print("La matriz es:",matriz)

