class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def es_operador(c):
    return c in {'+', '-', '*', '/'}

def construir_arbol(tokens):
    pila_valores = []
    pila_operadores = []

    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}

    def aplicar_operador():
        operador = pila_operadores.pop()
        derecho = pila_valores.pop()
        izquierdo = pila_valores.pop()
        nodo = Nodo(operador)
        nodo.izquierdo = izquierdo
        nodo.derecho = derecho
        pila_valores.append(nodo)

    for token in tokens:
        if token.isdigit():
            pila_valores.append(Nodo(int(token)))
        elif es_operador(token):
            while (pila_operadores and pila_operadores[-1] != '(' and
                   precedencia[pila_operadores[-1]] >= precedencia[token]):
                aplicar_operador()
            pila_operadores.append(token)
        elif token == '(':
            pila_operadores.append(token)
        elif token == ')':
            while pila_operadores[-1] != '(':
                aplicar_operador()
            pila_operadores.pop()

    while pila_operadores:
        aplicar_operador()

    return pila_valores[0]

def evaluar_arbol(nodo):
    if not nodo:
        return 0
    if not nodo.izquierdo and not nodo.derecho:
        return nodo.valor
    izquierdo_valor = evaluar_arbol(nodo.izquierdo)
    derecho_valor = evaluar_arbol(nodo.derecho)

    if nodo.valor == '+':
        return izquierdo_valor + derecho_valor
    elif nodo.valor == '-':
        return izquierdo_valor - derecho_valor
    elif nodo.valor == '*':
        return izquierdo_valor * derecho_valor
    elif nodo.valor == '/':
        return izquierdo_valor / derecho_valor

def parsear_expresion(expresion):
    tokens = []
    i = 0
    while i < len(expresion):
        if expresion[i].isdigit():
            num = ""
            while i < len(expresion) and expresion[i].isdigit():
                num += expresion[i]
                i += 1
            tokens.append(num)
            continue
        elif expresion[i] in {'+', '-', '*', '/', '(', ')'}:
            tokens.append(expresion[i])
        i += 1
    return tokens

# Probamos con la expresión "5 + 3 * 4"
expresion = "5 + 3 * 4"
tokens = parsear_expresion(expresion)
arbol = construir_arbol(tokens)
resultado = evaluar_arbol(arbol)
print("El resultado de la expresión es:", resultado)
