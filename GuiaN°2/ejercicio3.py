import math

class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

class Listasimple:
    def __init__(self):
        self.inicio = None

    def agregar_dato(self, dato):
        nuevo_dato = Nodo(dato)

        if self.inicio is None:
            self.inicio = nuevo_dato
        
        else:
            nodo_actual = self.inicio
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_actual