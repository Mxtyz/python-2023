#Tuplas de frutas
frutas = ("manzana", "platano", "pera", "naranja", "frutilla", "manzana")

#Eliminar los elementos repetidos de la tupla
frutas_sin_repetir = tuple(set(frutas))

print("Tupla de frutas sin repetir:", frutas_sin_repetir)

#Agregar la fruta "mango" por teclado o otra 
fruta_agregar = input("Ingrese la fruta que desea agregar: ")
frutas = frutas + (fruta_agregar,)

print("Tupla de frutas con la fruta agregada:", frutas)

#Eliminar la fruta "platano"
frutas = tuple(f for f in frutas if f != "platano")

print("Tupla de frutas sin la fruta platano:", frutas)

#Calcular la cantidad de frutas
cantidad_frutas = len(frutas)

print("Cantidad de frutas:", cantidad_frutas)
