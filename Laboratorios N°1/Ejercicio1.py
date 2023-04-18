#(intento del codigo) Se pide las filas y columnas de la matriz
filas = input("Ingrese cuantas filas para la matriz:")
columnas = input("Ingrese cuantas columnas para la matriz:")
filas = []
columnas = []



matriz1 = []
matriz2 = []
#(intentode codigo) Se ingresan los elementos de la matriz 1 por 1 
for i in range(4):
    matriz1 = input("Ingrese los elementos de la matriz 1:")
    matriz2 = input("Ingrese los elementos de la matriz 2:") 

matriz = matriz1 + matriz2
matri = matriz1 - matriz2

print(matriz)
print(matri)