class NodoGrado:
    def __init__(self, grado, estudiantes):
        self.grado = grado          # Número o nombre del grado (ej. "Grado 12")
        self.estudiantes = estudiantes  # Lista de estudiantes en este grado
        self.hijos = []             # Lista de nodos hijos (grados inferiores)

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def recorrido_por_niveles(raiz):
    if not raiz:
        return

    # Usamos una lista como cola para el recorrido por niveles
    cola = [raiz]

    while cola:
        # Sacamos el nodo actual de la cola (en el índice 0)
        nodo_actual = cola.pop(0)

        # Imprimimos el grado y los estudiantes en este grado
        print(f"{nodo_actual.grado}: {', '.join(nodo_actual.estudiantes)}")

        # Agregamos los hijos del nodo actual a la cola para el siguiente nivel
        for hijo in nodo_actual.hijos:
            cola.append(hijo)

# Ejemplo de uso
# Creamos nodos de grados con listas de estudiantes
grado12 = NodoGrado("Grado 12", ["Ana", "Luis"])
grado11 = NodoGrado("Grado 11", ["Carlos", "Sofía"])
grado10 = NodoGrado("Grado 10", ["Mario", "Laura"])
grado9 = NodoGrado("Grado 9", ["José", "Lucía"])

# Construimos la estructura de árbol
grado12.agregar_hijo(grado11)
grado11.agregar_hijo(grado10)
grado10.agregar_hijo(grado9)

# Ejecutamos el recorrido por niveles
recorrido_por_niveles(grado12)
