class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolExpresion:
    def __init__(self):
        self.operadores = {'+', '-', '*', '/'}
        self.precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}

    def es_operador(self, c):
        return c in self.operadores

    def infijo_a_postfijo(self, expresion):
        salida = []
        pila = []

        tokens = expresion.split()
        for token in tokens:
            if token.isdigit():
                salida.append(token)
            elif token in self.operadores:
                while (pila and pila[-1] in self.operadores and
                       self.precedencia[pila[-1]] >= self.precedencia[token]):
                    salida.append(pila.pop())
                pila.append(token)
            elif token == '(':
                pila.append(token)
            elif token == ')':
                while pila and pila[-1] != '(':
                    salida.append(pila.pop())
                pila.pop()  # Quitar el '('

        while pila:
            salida.append(pila.pop())

        return " ".join(salida)

    def construir_arbol(self, expresion):
        # Convertir la expresión infija a postfija
        expresion_postfija = self.infijo_a_postfijo(expresion)
        tokens = expresion_postfija.split()
        pila = []

        for token in tokens:
            if not self.es_operador(token):
                nodo = Nodo(int(token))
                pila.append(nodo)
            else:
                nodo = Nodo(token)
                nodo.derecho = pila.pop()
                nodo.izquierdo = pila.pop()
                pila.append(nodo)

        return pila.pop()

    def evaluar(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierdo is None and nodo.derecho is None:
            return nodo.valor

        izquierdo = self.evaluar(nodo.izquierdo)
        derecho = self.evaluar(nodo.derecho)

        if nodo.valor == '+':
            return izquierdo + derecho
        elif nodo.valor == '-':
            return izquierdo - derecho
        elif nodo.valor == '*':
            return izquierdo * derecho
        elif nodo.valor == '/':
            return izquierdo / derecho

# Prueba del programa
expresion = "5 + 3 * 4"
arbol = ArbolExpresion()
raiz = arbol.construir_arbol(expresion)
resultado = arbol.evaluar(raiz)
print("El resultado de la expresión es:", resultado)
