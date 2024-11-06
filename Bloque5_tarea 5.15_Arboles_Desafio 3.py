class Nodo:
    def __init__(self, key):
        self.izq = None
        self.der = None
        self.val = key

# Crear el nodo raíz
raiz = Nodo(1)

# Añadir nodos hijos
raiz.izq = Nodo(2)
raiz.der = Nodo(3)

# Añadir nodos hijos al nodo izquierdo del raíz
raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)

# Añadir nodos hijos al nodo derecho del raíz
raiz.der.izq = Nodo(6)
raiz.der.der = Nodo(7)

# Añadir nodos hijos al nodo hijo derecho del hijo izquierdo del raíz
raiz.izq.der.izq = Nodo(8)
raiz.izq.der.der = Nodo(9)

# Añadir nodos hijos al nodo hijo derecho del hijo derecho del raíz
raiz.der.der.izq = Nodo(10)
raiz.der.der.der = Nodo(11)

# Función para encontrar el valor máximo en postorden
def max_postorden(raiz):
    if raiz is None:
        return float('-inf')  # Valor mínimo posible para comparación

    # Llamadas recursivas en postorden: izquierda, derecha, raíz
    max_izq = max_postorden(raiz.izq)
    max_der = max_postorden(raiz.der)
    
    # Devolver el máximo entre el valor del nodo actual y los valores máximos de los subárboles
    return max(raiz.val, max_izq, max_der)

# Llamada a la función y resultado
resultado = max_postorden(raiz)
print(f"El valor máximo en el árbol es: {resultado}")