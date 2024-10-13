class NodoGeneral:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

    def eliminar_hijo(self, nodo_hijo):
        self.hijos.remove(nodo_hijo)

    def __repr__(self, nivel=0):
        ret = "\t" * nivel + repr(self.valor) + "\n"
        for hijo in self.hijos:
            ret += hijo.__repr__(nivel + 1)
        return ret

class ArbolGeneral:
    def __init__(self, valor_raiz):
        self.raiz = NodoGeneral(valor_raiz)

    def agregar_nodo_recursivo(self, nodo, nuevo_nodo):
        if len(nodo.hijos) < 2:  # Aquí definimos un máximo de 2 hijos para balancear (modificable)
            nodo.agregar_hijo(nuevo_nodo)
            return True
        else:
            for hijo in nodo.hijos:
                if self.agregar_nodo_recursivo(hijo, nuevo_nodo):
                    return True
        return False

    def agregar_nodo(self, valor_hijo):
        nuevo_nodo = NodoGeneral(valor_hijo)
        if not self.agregar_nodo_recursivo(self.raiz, nuevo_nodo):
            print("No se encontró un nodo adecuado para insertar el nuevo nodo.")

    def eliminar_nodo_recursivo(self, nodo, valor_hijo):
        for hijo in nodo.hijos:
            if hijo.valor == valor_hijo:
                if hijo.hijos:
                    print("El nodo tiene hijos y no puede ser eliminado.")
                    return False
                else:
                    nodo.eliminar_hijo(hijo)
                    return True
            if self.eliminar_nodo_recursivo(hijo, valor_hijo):
                return True
        return False

    def eliminar_nodo(self, valor_hijo):
        if not self.eliminar_nodo_recursivo(self.raiz, valor_hijo):
            print(f"Nodo {valor_hijo} no encontrado.")

    def __repr__(self):
        return repr(self.raiz)

# Función para interactuar con el usuario y construir el árbol
def construir_arbol():
    valor_raiz = input("Ingrese el valor de la raíz: ")
    arbol = ArbolGeneral(valor_raiz)

    while True:
        accion = input("Ingrese 'a' para agregar un nodo, 'e' para eliminar un nodo, o 'q' para salir: ").lower()
        if accion == 'q':
            break
        elif accion == 'a':
            valor_hijo = input("Ingrese el valor del nuevo nodo: ")
            arbol.agregar_nodo(valor_hijo)
            print("Nodo agregado correctamente.")
        elif accion == 'e':
            valor_hijo = input("Ingrese el valor del nodo a eliminar: ")
            arbol.eliminar_nodo(valor_hijo)
        else:
            print("Acción no válida.")
        print("Árbol actual:\n", arbol)

    return arbol

# Construir el árbol interactivamente
arbol = construir_arbol()
print("\nÁrbol final:\n", arbol)
