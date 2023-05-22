import random

def generar_matriz(filas, columnas):
    return [[random.randint(1, 10) for _ in range(columnas)] for _ in range(filas)]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def gauss_inversa(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    identidad = [[int(i == j) for j in range(filas)] for i in range(filas)]

    matriz_extendida = [fila + identidad[i] for i, fila in enumerate(matriz)]

    for i in range(filas):
        max_fila = max(range(i, filas), key=lambda x: abs(matriz_extendida[x][i]))
        matriz_extendida[i], matriz_extendida[max_fila] = matriz_extendida[max_fila], matriz_extendida[i]

        pivote = matriz_extendida[i][i]
        matriz_extendida[i] = [elemento / pivote for elemento in matriz_extendida[i]]

        for j in range(i+1, filas):
            factor = matriz_extendida[j][i]
            matriz_extendida[j] = [elem_j - factor * elem_i for elem_i, elem_j in zip(matriz_extendida[i], matriz_extendida[j])]

    for i in range(filas-1, 0, -1):
        for j in range(i-1, -1, -1):
            factor = matriz_extendida[j][i]
            matriz_extendida[j] = [elem_j - factor * elem_i for elem_i, elem_j in zip(matriz_extendida[i], matriz_extendida[j])]

    matriz_inversa = [fila[filas:] for fila in matriz_extendida]
    return matriz_inversa

filas = random.randint(3, 5)
columnas = filas
matriz_original = generar_matriz(filas, columnas)

print("Matriz original:")
imprimir_matriz(matriz_original)

matriz_inversa = gauss_inversa(matriz_original)

print("\nMatriz inversa:")
imprimir_matriz(matriz_inversa)
