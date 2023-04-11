import random

# Generamos un número aleatorio entre 10 y 30 para el tamaño del arreglo
size = random.randint(10, 30)

# Creamos un arreglo aleatorio de tamaño size
arr = [random.randint(0, 30) for i in range(size)]

# Imprimimos el arreglo
print("Arreglo generado:", arr)

# Pedimos al usuario que ingrese el número a buscar
target = int(input("Ingrese el número que desea buscar en el arreglo: "))

# Buscamos el número en el arreglo
if target in arr:
    print(f"El número {target} se encuentra en el arreglo.")
else:
    print(f"El número {target} no se encuentra en el arreglo.")
    