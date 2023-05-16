import random
#Se ingresan las filas y columnas de cada matriz
filas= int(input("Ingrese la cantidad de filas: ")) 
columnas= int(input("Ingrese la cantidad de columnas: ")) 

matriz1 = [[0 for j in range(columnas)] for i in range(filas)] 
matriz2 = [[0 for j in range(columnas)] for i in range(filas)] 

for i in range(filas): 
    for j in range(columnas): 
        matriz1[i][j] = random.randint(1, 5) 
        matriz2[i][j] = random.randint(1, 5) 
#se suman las dos matrices
matrizsuma = [[0 for j in range(columnas)] for i in range(filas)] 
  
for i in range(filas): 
    for j in range(columnas): 
        matrizsuma[i][j] = matriz1[i][j] + matriz2[i][j] 
 
print("La matriz de suma es:")
for fila in matrizsuma:
    print(fila)
#Intento sobre que la matriz se multiplique por un escalar 
escalar = input("Ingrese un escalar entre el 1 al 10:")
