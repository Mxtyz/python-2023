import random

class Almacen:
    def __init__(self): 
        self.productos_recibidos = []
        self.productos_despachar = []

    def agregarproducto(self, producto): 
        self.productos_recibidos.append(producto)

    def despacharproducto(self): 
        if len(self.productos_despachar) > 0:
            producto = self.productos_despachar.pop(0)
            print(f"Despachando producto: {producto}")
        else:
            print("No hay productos disponibles para despachar.")

    def verificarpilavacia(self): 
        if len(self.productos_recibidos) == 0:
            print("La pila de productos recibidos está vacía.")
        else:
            print("La pila de productos recibidos no está vacía.")

    def verificarcolavacia(self): 
        if len(self.productos_despachar) == 0:
            print("La cola de productos para despachar está vacía.")
        else:
            print("La cola de productos para despachar no está vacía.")

    def imprimirproductosrecibidos(self): 
        print("Lista de productos recibidos:")
        for producto in self.productos_recibidos: 
            print(producto)
 
    def imprimirproductosdespachar(self): 
        print("Lista de productos para despachar:")
        for producto in self.productos_despachar:
            print(producto)

    def mostrarcantidadtotalproductos(self):
        total_productos = len(self.productos_recibidos) + len(self.productos_despachar)
        print(f"Cantidad total de productos en el almacén: {total_productos}")

almacen = Almacen()

# Agregar productos al almacén
almacen.agregarproducto("Producto 1") 
almacen.agregarproducto("Producto 2")
almacen.agregarproducto("Producto 3") 
almacen.agregarproducto("Producto 4")
almacen.agregarproducto("Producto 5") 

# Despachar productos
almacen.despacharproducto() 
almacen.despacharproducto() 

# Verificar si la pila de productos recibidos está vacía
almacen.verificarpilavacia() 

# Verificar si la cola de productos para despachar está vacía
almacen.verificarcolavacia() 

# Imprimir lista de productos recibidos
almacen.imprimirproductosrecibidos() 

# Imprimir lista de productos para despachar
almacen.imprimirproductosdespachar() 

# Mostrar cantidad total de productos en el almacén
almacen.mostrarcantidadtotalproductos() 