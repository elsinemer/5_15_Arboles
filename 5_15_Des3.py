# Definición de la clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para recorrer el árbol en inorden y calcular la suma de los nodos
def suma_inorden(nodo):
    if nodo is None:
        return 0
    # Suma en inorden: izquierda, raíz, derecha
    suma_izquierda = suma_inorden(nodo.izquierda)
    suma_raiz = nodo.valor
    suma_derecha = suma_inorden(nodo.derecha)
    
    # Retornar la suma total en este nivel del árbol
    return suma_izquierda + suma_raiz + suma_derecha

# Función para construir un árbol de ejemplo
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

# Construcción del árbol y cálculo de la suma
raiz_arbol = construir_arbol()
resultado_suma = suma_inorden(raiz_arbol)
print("La suma de todos los valores en el árbol es:", resultado_suma)
