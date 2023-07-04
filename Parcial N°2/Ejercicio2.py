#Desarrolla un sistema de gestión de inventario utilizando listas bidireccionales. Cada artículo del
#inventario tiene un código único, un nombre, una descripción y una cantidad disponible. El
#sistema debe realizar las siguientes operaciones:
#A. Agregar un artículo al inventario, ingresando su código, nombre, descripción y cantidad inicial
#B. Eliminar un artículo del inventario utilizando su código
#C. Buscar un artículo en específico por su código
#D. Actualizar la cantidad disponible de un artículo
#E. Mostrar todos los artículos del inventario en orden ascendente según su código

#Nota: Se solicita no solo implementar las funciones requeridas, sino también probarlas y mostrar los
#resultados obtenidos anteriormente. Esto implica que se deben ejecutar las funciones con datos de
#prueba o ejemplos específicos para demostrar su funcionamiento.


#Se crea una clase Nodo con su fucion 
class Nodo:
    def __init__(self, codigo, nombre, descripcion, cantidad): 
        self.codigo = codigo 
        self.nombre = nombre 
        self.descripcion = descripcion 
        self.cantidad = cantidad 
        self.siguiente = None 
        self.anterior = None 

#Se crea una clase Inventario 
class Inventario: 
    def __init__(self): 
        self.primernodo = None 
        self.ultimonodo = None 


#Se crea la funcion para agregar un articulo
    def agregar_articulo(self, codigo, nombre, descripcion, cantidad):
        nuevo_nodo = Nodo(codigo, nombre, descripcion, cantidad)

#Se crean un if y else para agregar articulos al inventario
        if self.primernodo is None: 
            self.primernodo = nuevo_nodo 
            self.ultimonodo = nuevo_nodo 
        else:
            nuevo_nodo.anterior = self.ultimonodo 
            self.ultimonodo.siguiente = nuevo_nodo 
            self.ultimonodo = nuevo_nodo 

#Se crea funcion para poder Eliminar un articulo
    def eliminar_articulo(self, codigo):
        nodo_actual = self.primernodo

#Un while para poder eliminar artticulos
        while nodo_actual is not None: 
            if nodo_actual.codigo == codigo: 
                if nodo_actual.anterior is None: 
                    self.primernodo = nodo_actual.siguiente 
                else:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente 

                if nodo_actual.siguiente is None: 
                    self.ultimonodo = nodo_actual.anterior 
                else:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior 

                return 
            nodo_actual = nodo_actual.siguiente 
        print("El artículo con el código :", codigo, "no fue encontrado.")

#Se crea funcion para poder buscar un articulo
    def buscar_articulo(self, codigo):
        nodo_actual = self.primernodo

        while nodo_actual is not None:
            if nodo_actual.codigo == codigo:
                return nodo_actual

            nodo_actual = nodo_actual.siguiente

        print("El artículo con el código :", codigo, "no fue encontrado.")
        return None
#Se crear funcion para actualizar la contidad 
    def actualizar_cantidad(self, codigo, nueva_cantidad):
        nodo_actual = self.buscar_articulo(codigo) 

        if nodo_actual is not None:
            nodo_actual.cantidad = nueva_cantidad 

#Se crea funcion para poder mostrar el inventario
    def mostrar_inventario(self): 
        nodo_actual = self.primernodo 

        while nodo_actual is not None: 
            print("Código:", nodo_actual.codigo)  
            print("Nombre:", nodo_actual.nombre)  
            print("Descripción:", nodo_actual.descripcion)  
            print("Cantidad:", nodo_actual.cantidad) 

            nodo_actual = nodo_actual.siguiente 

