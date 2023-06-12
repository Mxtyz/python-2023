#Crear clase
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def agregar_producto(self, producto):
        self.items.append(producto)

    def eliminar_producto(self):
        if not self.esta_vacia():
            return self.items.pop(0)

    def mostrar_productos(self):
        if self.esta_vacia():
            print("La cola está vacía.")
        else:
            print("Productos en la cola:")
            for producto in self.items:
                print(producto)

    def invertir_cola(self):
        self.items = self.items[::-1]

    def vaciar_cola(self):
        self.items = []


#Agregar un producto a la cola
def agregar_producto(cola, producto):
    cola.agregar_producto(producto)

#Eliminar el primer producto de la cola
def eliminar_producto(cola):
    return cola.eliminar_producto()

#Mostrar los productos en la cola sin modificarla
def mostrar_productos(cola):
    cola.mostrar_productos()

#Invertir el orden de los productos en la cola
def invertir_cola(cola):
    cola.invertir_cola()

#Eliminar todos los productos de la cola
def vaciar_cola(cola):
    cola.vaciar_cola()


#Crear cola de productos
cola_productos = Cola()

#Agregar productos a la cola
agregar_producto(cola_productos, "Leche")
agregar_producto(cola_productos, "Pan")
agregar_producto(cola_productos, "Arroz")
agregar_producto(cola_productos, "Huevos")
agregar_producto(cola_productos, "Carne")
agregar_producto(cola_productos, "Frutas")

#Mostrar productos en la cola
mostrar_productos(cola_productos)

#Eliminar el primer producto de la cola
producto_eliminado = eliminar_producto(cola_productos)
print("Producto eliminado:", producto_eliminado)

mostrar_productos(cola_productos)
invertir_cola(cola_productos)
mostrar_productos(cola_productos)
vaciar_cola(cola_productos)
mostrar_productos(cola_productos)
