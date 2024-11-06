class NodoABB:
    def __init__(self, promedio, estudiante):
        self.promedio = promedio          # Promedio de calificaciones
        self.estudiantes = [estudiante]   # Lista de estudiantes con este promedio
        self.izquierda = None             # Nodo izquierdo
        self.derecha = None               # Nodo derecho

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, promedio, estudiante):
        """Inserta un estudiante en el árbol según su promedio."""
        if self.raiz is None:
            self.raiz = NodoABB(promedio, estudiante)
            print(f"Insertado: {estudiante} con promedio {promedio} como raíz.")
        else:
            self._insertar_recursivo(self.raiz, promedio, estudiante)

    def _insertar_recursivo(self, nodo, promedio, estudiante):
        if promedio < nodo.promedio:
            if nodo.izquierda is None:
                nodo.izquierda = NodoABB(promedio, estudiante)
                print(f"Insertado: {estudiante} con promedio {promedio} a la izquierda de {nodo.promedio}.")
            else:
                self._insertar_recursivo(nodo.izquierda, promedio, estudiante)
        elif promedio > nodo.promedio:
            if nodo.derecha is None:
                nodo.derecha = NodoABB(promedio, estudiante)
                print(f"Insertado: {estudiante} con promedio {promedio} a la derecha de {nodo.promedio}.")
            else:
                self._insertar_recursivo(nodo.derecha, promedio, estudiante)
        else:
            # Si el promedio ya existe, agregamos el estudiante a la lista
            nodo.estudiantes.append(estudiante)
            print(f"Agregado: {estudiante} al nodo existente con promedio {promedio}.")

    def recorrido_en_inorden(self):
        """Realiza un recorrido en inorden del árbol y devuelve una lista de estudiantes ordenados."""
        estudiantes_ordenados = []
        self._recorrido_inorden_recursivo(self.raiz, estudiantes_ordenados)
        return estudiantes_ordenados

    def _recorrido_inorden_recursivo(self, nodo, lista):
        if nodo:
            self._recorrido_inorden_recursivo(nodo.izquierda, lista)
            for estudiante in nodo.estudiantes:
                lista.append((estudiante, nodo.promedio))
            self._recorrido_inorden_recursivo(nodo.derecha, lista)

# Ejemplo de uso
# Crear una instancia del árbol
arbol = ArbolBinarioBusqueda()

# Lista de estudiantes con sus promedios
estudiantes_promedios = [
    ("Ana", 85.5),
    ("Carlos", 90.3),
    ("Daniel", 78.2),
    ("Fernanda", 92.7),
    ("Luis", 88.9),
    ("Sofía", 95.4),
    ("María", 90.3),     # Estudiante con el mismo promedio que Carlos
    ("Pedro", 85.5),     # Estudiante con el mismo promedio que Ana
    ]

# Insertar estudiantes en el árbol
for estudiante, promedio in estudiantes_promedios:
    arbol.insertar(promedio, estudiante)

print("\nEstudiantes en orden ascendente de promedio:")
estudiantes_ordenados = arbol.recorrido_en_inorden()
for estudiante, promedio in estudiantes_ordenados:
    print(f"{estudiante}: {promedio}")
