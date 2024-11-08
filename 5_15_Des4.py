class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def insertar(nodo, valor):
    # Si el árbol está vacío, crea el nodo raíz
    if nodo is None:
        return Nodo(valor)
    
    # Si el valor es menor que el nodo actual, se inserta en el subárbol izquierdo
    if valor < nodo.valor:
        nodo.izquierdo = insertar(nodo.izquierdo, valor)
    # Si el valor es mayor que el nodo actual, se inserta en el subárbol derecho
    elif valor > nodo.valor:
        nodo.derecho = insertar(nodo.derecho, valor)
    
    # Retorna el nodo (no cambia si ya está insertado)
    return nodo

def construir_abb(numeros):
    raiz = None
    for numero in numeros:
        raiz = insertar(raiz, numero)
    return raiz

def buscar(nodo, valor):
    # Si el nodo es None, el valor no está en el árbol
    if nodo is None:
        return False
    
    # Si el valor es igual al nodo actual, el valor se encuentra en el árbol
    if valor == nodo.valor:
        return True
    # Si el valor es menor, buscar en el subárbol izquierdo
    elif valor < nodo.valor:
        return buscar(nodo.izquierdo, valor)
    # Si el valor es mayor, buscar en el subárbol derecho
    else:
        return buscar(nodo.derecho, valor)

# Conjunto de números para construir el ABB
numeros = [15, 10, 20, 8, 12, 17, 25]

# Construir el ABB
raiz = construir_abb(numeros)

# Buscar valores en el ABB
print(buscar(raiz, 12))  # Devuelve True, ya que 12 está en el árbol
print(buscar(raiz, 5))   # Devuelve False, ya que 5 no está en el árbol
