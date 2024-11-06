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

def suma_inorder(raiz):
    if raiz is None:
        return 0
    # Sumar el valor del nodo actual al resultado de la suma de los subárboles izquierdo y derecho
    return suma_inorder(raiz.izq) + raiz.val + suma_inorder(raiz.der)

# Llamar a la función y mostrar el resultado
resultado = suma_inorder(raiz)
print(f"La suma de los valores en el árbol es: {resultado}")

