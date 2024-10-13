import pygraphviz as pgv
G = pgv.AGraph(directed=True)
class ArbolGeneral:
    def __init__(self,d):
        self.dato=d
        self.raiz = None
        self.hijos = []
        G.add_node(d)

    def es_vacio(self):
        return self.raiz 

    def raiz(self):
        return self.raiz

    def hijos_ob(self):
        return [h.raiz for h in self.hijos]

    def nuevo_hijo(self, e):
        if self.es_vacio():
            self.raiz = e
        else:
            self.hijos.append(ArbolGeneral(e))
            G.add_edge(self.dato, e)

    def nuevo_hijo_arbol(self, a):
        if a != self and not a.es_vacio():
            self.hijos.append(a)

    def localiza(self, ob):
        if not self.es_vacio():
            if self.raiz == ob:
                return self
            else:
                for hijo in self.hijos:
                    resultado = hijo.localiza(ob)
                    if not resultado.es_vacio():
                        return resultado
        return ArbolGeneral(ob)

    def pertenece(self, ob):
        return not self.localiza(ob).es_vacio()

    def eliminar(self, dato):
        if not self.es_vacio():
            if self.raiz == dato:
                self.raiz = None
                self.hijos = []
            else:
                self.hijos = [hijo for hijo in self.hijos if hijo.raiz != dato]
                for hijo in self.hijos:
                    hijo.eliminar(dato)

    def padre(self, ob):
        if not self.es_vacio():
            if ob in self.hijos_ob():
                return self
            else:
                for hijo in self.hijos:
                    resultado = hijo.padre(ob)
                    if not resultado.es_vacio():
                        return resultado
        return ArbolGeneral()

    def _str_(self, espacios=0):
        resultado = ""
        if not self.es_vacio():
            resultado += "\t" * espacios + str(self.raiz) + "\n"
            for hijo in self.hijos:
                resultado += hijo._str_(espacios + 1)
        return resultado


    def profundidad(self, a):
        if self.es_vacio():
            return -1
        elif self == a:
            return 0
        else:
            profundidad_hijos = [hijo.profundidad(a) for hijo in self.hijos]
            if any(profundidad_hijos) != -1:
                return 1 + max(profundidad_hijos)
            else:
                return -1

    def es_hoja(self):
        return not self.es_vacio() and not self.hijos

    def _eq_(self, a):
        if not isinstance(a, ArbolGeneral):
            return False
        if self.es_vacio() and a.es_vacio():
            return True
        if self == a:
            return True
        return False

    def rec_anchura(self):
        rec = []
        if not self.es_vacio():
            ar = [self]
            for p in ar:
                rec.append(p.raiz)
                ar.extend(p.hijos)
        return rec



# Creación de un árbol
arbol = ArbolGeneral(1)
arbol.nuevo_hijo(2)
arbol.nuevo_hijo(3)
arbol.hijos[0].nuevo_hijo(4)
arbol.hijos[0].nuevo_hijo(5)
arbol.hijos[1].nuevo_hijo(6)
arbol.hijos[1].nuevo_hijo(0)
arbol.hijos[0].hijos[0].nuevo_hijo(9)
arbol.eliminar(9)
output_file = "ArbolGeneral.png"
G.draw(output_file, prog="dot")
print(f"Árbol general guardado en {output_file}")

#print(arbol)
# arbol.eliminar(9)

# print(arbol)