class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # INSERTAR
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

    # RECORRIDOS
    def preorden(self):
        self._preorden(self.raiz)
        print()

    def _preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self._preorden(nodo.izq)
            self._preorden(nodo.der)

    def inorden(self):
        self._inorden(self.raiz)
        print()

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izq)
            print(nodo.valor, end=" ")
            self._inorden(nodo.der)

    def postorden(self):
        self._postorden(self.raiz)
        print()

    def _postorden(self, nodo):
        if nodo:
            self._postorden(nodo.izq)
            self._postorden(nodo.der)
            print(nodo.valor, end=" ")

    # ELIMINAR
    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izq = self._eliminar(nodo.izq, valor)

        elif valor > nodo.valor:
            nodo.der = self._eliminar(nodo.der, valor)

        else:
            # Caso 1: sin hijos
            if nodo.izq is None and nodo.der is None:
                return None

            # Caso 2: un hijo
            elif nodo.izq is None:
                return nodo.der

            elif nodo.der is None:
                return nodo.izq

            # Caso 3: dos hijos
            sucesor = self._minimo(nodo.der)
            nodo.valor = sucesor.valor
            nodo.der = self._eliminar(nodo.der, sucesor.valor)

        return nodo

    def _minimo(self, nodo):
        while nodo.izq is not None:
            nodo = nodo.izq
        return nodo

    # BUSCAR
    def buscar(self, valor):
        return self._buscar(self.raiz, valor, None)

    def _buscar(self, nodo, valor, padre):
        if nodo is None:
            return None, None

        if nodo.valor == valor:
            return nodo, padre

        elif valor < nodo.valor:
            return self._buscar(nodo.izq, valor, nodo)

        else:
            return self._buscar(nodo.der, valor, nodo)

    # ACTUALIZAR
    def actualizar(self, valor_viejo, valor_nuevo):
        nodo, padre = self.buscar(valor_viejo)

        if nodo is not None:
            self.eliminar(valor_viejo)
            self.agregar(valor_nuevo)
            return True
        else:
            return False

    # ALTURA
    def altura(self, nodo):
        if nodo is None:
            return -1

        return 1 + max(self.altura(nodo.izq),
                       self.altura(nodo.der))