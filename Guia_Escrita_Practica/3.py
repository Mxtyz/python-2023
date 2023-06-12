#Crear clase pila
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def obtener_tope(self):
        if not self.esta_vacia():
            return self.items[-1]

#Documentos
documentos = ["Informe Final", "Guia de Estudio", "Tesis 4", "Seminario Osorno"]

#Imprimir el listado de documentos actual de la pila
def imprimir_pila(pila):
    if pila.esta_vacia():
        print("La pila está vacía.")
    else:
        print("Listado de documentos en la pila:")
        for documento in reversed(pila.items):
            print(documento)

#Crear pila de documentos
pila_documentos = Pila()

for documento in documentos:
    pila_documentos.apilar(documento)

#Agregar los documentos "Avance Tesis" y "Proyecto Integrador"
pila_documentos.apilar("Avance Tesis")
pila_documentos.apilar("Proyecto Integrador")

#Obtener el último elemento superior de la pila
ultimo_elemento = pila_documentos.obtener_tope()
print("Último elemento superior de la pila:", ultimo_elemento)

#Eliminar el documento de la parte superior
documento_eliminado = pila_documentos.desapilar()
print("Documento eliminado de la parte superior:", documento_eliminado)

#Imprimir la pila de documentos actualizadas
imprimir_pila(pila_documentos)

if pila_documentos.esta_vacia():
    print("La pila de documentos está vacía.")
else:
    print("La pila de documentos no está vacía.")
