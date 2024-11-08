# Definición de la clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Creao un árbol binario con 3 niveles
def construir_arbol():
    # Nivel 1 (raíz)
    raiz = Nodo(1)
    
    # Nivel 2
    raiz.izquierda = Nodo(2)
    raiz.derecha = Nodo(3)
    
    # Nivel 3
    raiz.izquierda.izquierda = Nodo(4)
    raiz.izquierda.derecha = Nodo(5)
    raiz.derecha.izquierda = Nodo(6)
    raiz.derecha.derecha = Nodo(7)
    
    return raiz

# Realizar un recorrido en preorden
def recorrido_preorden(nodo):
    if nodo:
        # Primero se procesa la raíz
        print(nodo.valor, end=" ")
        # Luego se recorre el subárbol izquierdo
        recorrido_preorden(nodo.izquierda)
        # Finalmente se recorre el subárbol derecho
        recorrido_preorden(nodo.derecha)

# Construcción del árbol y recorrido en preorden
raiz_arbol = construir_arbol()
print("Recorrido en preorden del árbol:")
recorrido_preorden(raiz_arbol)
