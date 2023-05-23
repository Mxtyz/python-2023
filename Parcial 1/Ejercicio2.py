#Crear dos matrices donde la cantidad de filas y columnas serán 3 x 3. Los
#elementos de estas matrices deben ser generados de forma aleatoria (-5 a -10).
#Luego se deben multiplicar ambas matrices e imprimir la matriz resultante.
#Agregar una condición para que las dimensiones sean acordes para realizar la
#multiplicación entre ambas matrices.
#Esta matriz resultado se debe multiplicar por una matriz identidad, e imprimir la matriz final.
#Se pueden utilizar librerías para resolver todo el ejercicio.

#Importar librerias random y numpy 
import random
import numpy as np

#Definir las matrices con sus cantidades de filas y comlumnas 3x3
matriz1 = [[random.randrange(-10,-5)for i in range(3) for j in range(3)]]
matriz2 = [[random.randrange(-10,-5)for i in range(3) for j in range(3)]] 

#Imprimir ambas matrices 
print("La matriz1 es:",matriz1)
print("La matriz2 es:",matriz2)

#Multiplicar ambas matrices
matriz_multi = np.multiply(matriz1,matriz2)

#Imprimir el resultado de las matrices
print("La multiplicacion de las matrices es:",matriz_multi)

#Matriz identidad
identidad = [1,0,0,0,1,0,0,0,1]

#Imprimir la Matriz identidad
matriz_identidad = np.multiply(matriz_multi,identidad)
print("La matriz identidad es:",matriz_identidad)
