class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class Arbol:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor, padre=None):
        nuevo_nodo = Nodo(valor)
        if padre is None:
            self.raiz = nuevo_nodo
        else:
            padre.hijos.append(nuevo_nodo)

    def peso(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        resultado = 1
        for hijo in nodo.hijos:
            resultado += self.peso(hijo)
        return resultado

    def orden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if not nodo.hijos:
            return 0
        max_hijos = len(nodo.hijos)
        for hijo in nodo.hijos:
            max_hijos = max(max_hijos, self.orden(hijo))
        return max_hijos

    def altura(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if not nodo.hijos:
            return 1
        max_altura = 0
        for hijo in nodo.hijos:
            max_altura = max(max_altura, self.altura(hijo))
        return 1 + max_altura
arbol = Arbol()
arbol.agregar(1)
arbol.agregar(2, arbol.raiz)
arbol.agregar(3, arbol.raiz)
arbol.agregar(4, arbol.raiz.hijos[0])
arbol.agregar(5, arbol.raiz.hijos[0])
arbol.agregar(6, arbol.raiz.hijos[0].hijos[0])
arbol.agregar(7, arbol.raiz.hijos[1])
print("peso del árbol:", arbol.peso())
print("orden del árbol:", arbol.orden())
print("altura del árbol:", arbol.altura())

