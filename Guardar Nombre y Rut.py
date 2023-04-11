# Crear dos arreglos vacíos para guardar los nombres y RUT de las personas
nombres = []
rut = []

# Pedir al usuario que ingrese la información de cada persona
for i in range(5):
    nombre = input("Ingrese el nombre de la persona {}: ".format(i+1))
    rut_persona = input("Ingrese el RUT de la persona {}: ".format(i+1))
    nombres.append(nombre)
    rut.append(rut_persona)

# Imprimir los arreglos de nombres y RUT
print("Nombres ingresados:", nombres)
print("RUT ingresados:", rut)

# Ordenar los arreglos alfabéticamente y ascendentemente
nombres.sort()
rut.sort()

# Imprimir los arreglos ordenados
print("Nombres ordenados alfabéticamente:", nombres)
print("RUT ordenados ascendentemente:", rut)