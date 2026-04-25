class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar(valor, self.raiz)

    def _agregar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._agregar(valor, nodo.izq)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._agregar(valor, nodo.der)

    def preorden(self):
        self._preorden(self.raiz)

    def _preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self._preorden(nodo.izq)
            self._preorden(nodo.der)

    def inorden(self):
        self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izq)
            print(nodo.valor, end=" ")
            self._inorden(nodo.der)

    def postorden(self):
        self._postorden(self.raiz)

    def _postorden(self, nodo):
        if nodo:
            self._postorden(nodo.izq)
            self._postorden(nodo.der)
            print(nodo.valor, end=" ")

arbol = ArbolBinario()

arbol.agregar(2)
arbol.agregar(9)
arbol.agregar(4)
arbol.agregar(0)
arbol.agregar(3)

print("Preorden:")
arbol.preorden()

print("\nInorden:")
arbol.inorden()

print("\nPostorden:")
arbol.postorden()