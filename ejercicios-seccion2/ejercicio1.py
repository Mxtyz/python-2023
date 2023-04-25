import numpy as np
import random

# Solicitar la cantidad de filas y columnas de las matrices
filas = int(input("Ingrese la cantidad de filas de la matriz:"))
comlumnas = int(input("Ingrese la cantidad de columnas de la matriz:"))

# Crear las dos primeras matrices con valores aleatorios
m1 = [[random.randint(0, 5) for j in range(comlumnas)] for i in range(filas)]
m2 = [[random.randint(0, 5) for j in range(comlumnas)] for i in range(filas)]

# Sumar las dos matrices
matriz_suma = np.add(m1, m2)

# Crear la tercera matriz con valores aleatorios
filas2 = int(input("Ingrese la cantidad de filas de la matriz a restar:"))
comlumnas2 = int(input("Ingrese la cantidad de columnas de la matriz a restar:"))

# Crear la tercera matrices con valores aleatorias
m3 = [[random.randint(0, 5) for j in range(comlumnas)] for i in range(filas)]

# Restar la tercera matriz a la matriz resultante de la suma anterior
matriz_resultante = np.subtract(matriz_suma, m3)

# Mostrar la matriz resultante
print("Matriz resultante:")
print(matriz_resultante)
