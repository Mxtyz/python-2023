class Cancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

class ListaCanciones:
    def __init__(self):
        self.inicio = None
        self.final = None

    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)
        if self.inicio is None:
            self.inicio = nuevo_nodo
            self.final = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.final
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def mostrar(self):
        nodo_actual = self.inicio

        while nodo_actual is not None:
            cancion = nodo_actual.cancion
            print("Título:", cancion.titulo)
            print("Artista:", cancion.artista)
            print()
            nodo_actual = nodo_actual.siguiente

    def reproducir_cancion(self):
        nodo_actual = self.inicio
        while nodo_actual is None:
            cancion = nodo_actual.cancion
            print("Reproduciendo:", cancion.titulo, "por", cancion.artista)
            nodo_actual = nodo_actual.siguiente
               
a = ListaCanciones()

w1 = Cancion("Ghost", "Desconocido")
w2 = Cancion("Despacito", "Luis Fonsi")
w3 = Cancion("Dream on", "Aerosmith")

a.agregar_cancion(w1)
a.agregar_cancion(w2)
a.agregar_cancion(w3)

print("Lista de canciones:")
a.mostrar()

print("Reproduciendo:")
a.reproducir_cancion()