from modelos.nodo import Nodo

class ArbolBST:
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
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._agregar(valor, nodo.der)
        else:
            # No insertamos duplicados
            pass

    def preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden(nodo.izq, resultado)
            self._preorden(nodo.der, resultado)

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izq, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.der, resultado)

    def postorden(self):
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self, nodo, resultado):
        if nodo:
            self._postorden(nodo.izq, resultado)
            self._postorden(nodo.der, resultado)
            resultado.append(nodo.valor)