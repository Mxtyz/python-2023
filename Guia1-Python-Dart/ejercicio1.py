import random

matriz = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]
for fila in matriz:
    print(fila)

sumas_columnas = [sum(columna) for columna in zip(*matriz)]
suma_maxima = max(sumas_columnas)
print("La suma más alta entre las columnas es:", suma_maxima)

sumas_filas = [sum(fila) for fila in matriz]
suma_minima = min(sumas_filas)
print("La suma más baja entre todas las filas es:", suma_minima)
