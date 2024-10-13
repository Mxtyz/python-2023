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
        self.nodos = [self.raiz]  # Lista para mantener los nodos en orden de inserción

    # def agregar_nodo(self, valor_hijo):
    #     nuevo_nodo = NodoGeneral(valor_hijo)
    #     for nodo in self.nodos:
    #         if len(nodo.hijos) < 2:  # Aquí definimos un máximo de 2 hijos 
    #             nodo.agregar_hijo(nuevo_nodo)
    #             self.nodos.append(nuevo_nodo)
    #             return
    #     print("No se encontró un nodo adecuado para insertar el nuevo nodo.")

    def agregar_nodo(self, valor_hijo):
        nuevo_nodo = NodoGeneral(valor_hijo)
        i = 0
        while i < len(self.nodos):
            nodo = self.nodos[i]
            if len(nodo.hijos) < 2:
                nodo.agregar_hijo(nuevo_nodo)
                self.nodos.append(nuevo_nodo)
                return
            i += 1
        print("No se encontró un nodo adecuado para insertar el nuevo nodo.")


    # def eliminar_nodo(self, valor_hijo):
    #     nodo_a_eliminar = None
    #     nodo_padre = None

    #     # Buscar el nodo a eliminar y su padre
    #     for nodo in self.nodos:
    #         for hijo in nodo.hijos:
    #             if hijo.valor == valor_hijo:
    #                 nodo_a_eliminar = hijo
    #                 nodo_padre = nodo
    #                 break
    #         if nodo_a_eliminar:
    #             break

    #     if nodo_a_eliminar:
    #         if nodo_a_eliminar.hijos:
    #             print("El nodo tiene hijos y no puede ser eliminado.")
    #         else:
    #             nodo_padre.eliminar_hijo(nodo_a_eliminar)
    #             self.nodos.remove(nodo_a_eliminar)
    #             print(f"Nodo {valor_hijo} eliminado correctamente.")
    #     else:
    #         print(f"Nodo {valor_hijo} no encontrado.")

    def eliminar_nodo(self, valor_hijo):
        nodo_a_eliminar = None
        nodo_padre = None

        # Variables para controlar los índices en lugar de usar bucles for
        i = 0
        j = 0
        encontrando = True

        # Buscar el nodo a eliminar y su padre usando while
        while i < len(self.nodos) and encontrando:
            nodo = self.nodos[i]
            j = 0
            while j < len(nodo.hijos):
                hijo = nodo.hijos[j]
                if hijo.valor == valor_hijo:
                    nodo_a_eliminar = hijo
                    nodo_padre = nodo
                    encontrando = False
                    break
                j += 1
            i += 1

        if nodo_a_eliminar:
            if nodo_a_eliminar.hijos:
                print("El nodo tiene hijos y no puede ser eliminado.")
            else:
                nodo_padre.eliminar_hijo(nodo_a_eliminar)
                self.nodos.remove(nodo_a_eliminar)
                print(f"Nodo {valor_hijo} eliminado correctamente.")
        else:
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
