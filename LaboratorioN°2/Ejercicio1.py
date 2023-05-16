import random

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

matriz1 = [[0 for j in range(columnas)] for i in range(filas)]
matriz2 = [[0 for j in range(columnas)] for i in range(filas)]

for i in range(filas):
    for j in range(columnas):
        matriz1[i][j] = random.randint(1, 5)
        matriz2[i][j] = random.randint(1, 5)

matrizsuma = [[0 for j in range(columnas)] for i in range(filas)]

for i in range(filas):
    for j in range(columnas):
        matrizsuma[i][j] = matriz1[i][j] + matriz2[i][j]

print("Matriz de suma:")
for fila in matrizsuma:
    print(fila)
