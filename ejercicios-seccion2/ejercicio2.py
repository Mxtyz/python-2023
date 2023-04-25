import random

# Ingresar la cantidad de filas y columnas de la matriz
filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

# Ingresar el escalar
escalar = int(input("Ingrese un escalar: "))

# Crear la matriz con valores aleatorios
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(random.randint(0, 10))
    matriz.append(fila)

# Multiplicar la matriz por el escalar
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] *= escalar

# Mostrar la matriz final
print("Matriz resultante:")
for fila in matriz:
    print(fila)
