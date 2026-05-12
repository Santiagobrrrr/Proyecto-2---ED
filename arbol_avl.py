class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 0

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        if nodo is None:
            return -1
        return nodo.altura

    def insertar(self, valor):
        print("\nInsertando:", valor)
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):

        # 1. INSERTAR COMO ABB
        if nodo is None:
            print("Se creó el nodo:", valor)
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        else:
            nodo.derecha = self._insertar(nodo.derecha, valor)

        # 2. ACTUALIZAR ALTURA
        nodo.altura = 1 + max(
            self.obtener_altura(nodo.izquierda),
            self.obtener_altura(nodo.derecha)
        )

        # 3. CALCULAR BALANCE
        balance = (
            self.obtener_altura(nodo.izquierda)
            - self.obtener_altura(nodo.derecha)
        )

        print("Nodo:", nodo.valor, "Balance:", balance)

        # SI ESTÁ BALANCEADO
        if balance >= -1 and balance <= 1:
            print("El nodo", nodo.valor, "está balanceado")

        # DESBALANCE HACIA LA IZQUIERDA
        if balance > 1:

            print("Desbalance hacia la izquierda en nodo", nodo.valor)

            # CASO IZQUIERDA - IZQUIERDA
            if valor < nodo.izquierda.valor:
                print("Caso izquierda-izquierda")
                print("Rotación simple a la derecha")

                return self.rotar_derecha(nodo)

            # CASO IZQUIERDA - DERECHA
            else:
                print("Caso izquierda-derecha")
                print("Rotación doble izquierda-derecha")

                nodo.izquierda = self.rotar_izquierda(nodo.izquierda)

                return self.rotar_derecha(nodo)

        # DESBALANCE HACIA LA DERECHA
        if balance < -1:

            print("Desbalance hacia la derecha en nodo", nodo.valor)

            # CASO DERECHA - DERECHA
            if valor > nodo.derecha.valor:
                print("Caso derecha-derecha")
                print("Rotación simple a la izquierda")

                return self.rotar_izquierda(nodo)

            # CASO DERECHA - IZQUIERDA
            else:
                print("Caso derecha-izquierda")
                print("Rotación doble derecha-izquierda")

                nodo.derecha = self.rotar_derecha(nodo.derecha)

                return self.rotar_izquierda(nodo)

        return nodo

    # ROTACIÓN SIMPLE A LA DERECHA
    def rotar_derecha(self, z):

        print("Aplicando rotación derecha en", z.valor)

        y = z.izquierda
        T3 = y.derecha

        # ROTACIÓN
        y.derecha = z
        z.izquierda = T3

        # ACTUALIZAR ALTURAS
        z.altura = 1 + max(
            self.obtener_altura(z.izquierda),
            self.obtener_altura(z.derecha)
        )

        y.altura = 1 + max(
            self.obtener_altura(y.izquierda),
            self.obtener_altura(y.derecha)
        )

        return y

    # ROTACIÓN SIMPLE A LA IZQUIERDA
    def rotar_izquierda(self, z):

        print("Aplicando rotación izquierda en", z.valor)

        y = z.derecha
        T2 = y.izquierda

        # ROTACIÓN
        y.izquierda = z
        z.derecha = T2

        # ACTUALIZAR ALTURAS
        z.altura = 1 + max(
            self.obtener_altura(z.izquierda),
            self.obtener_altura(z.derecha)
        )

        y.altura = 1 + max(
            self.obtener_altura(y.izquierda),
            self.obtener_altura(y.derecha)
        )

        return y

    # MOSTRAR ÁRBOL
    def mostrar(self, nodo, nivel=0):

        if nodo is not None:

            self.mostrar(nodo.derecha, nivel + 1)

            print("   " * nivel + str(nodo.valor))

            self.mostrar(nodo.izquierda, nivel + 1)