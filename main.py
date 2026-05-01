from modelos.arbol_bst import ArbolBST
arbol = ArbolBST()

arbol.agregar(2)
arbol.agregar(9)
arbol.agregar(4)
arbol.agregar(0)
arbol.agregar(3)

print("Preorden:")
print(arbol.preorden())

print("Inorden:")
print(arbol.inorden())

print("Postorden:")
print(arbol.postorden())