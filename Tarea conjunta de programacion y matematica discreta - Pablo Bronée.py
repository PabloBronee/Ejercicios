class Grafo:
    def __init__(self, num_nodos):
        # Inicializa el número inicial de nodos y la matriz de adyacencia
        self.num_nodos = num_nodos
        self.matriz_adyacencia = [[float('inf')] * num_nodos for _ in range(num_nodos)]
        
        # Inicializa la diagonal principal a 0 (distancia de un nodo a si mismo es 0)
        for i in range(num_nodos):
            self.matriz_adyacencia[i][i] = 0

    def agregar_nodo(self):
        # Incrementa el número de nodos
        self.num_nodos += 1
        
        # Agrega una nueva fila con valores "inf" para el nuevo nodo
        for fila in self.matriz_adyacencia:
            fila.append(float('inf'))
        
        # Agrega una nueva columna con valores "inf" para el nuevo nodo
        nueva_fila = [float('inf')] * self.num_nodos
        nueva_fila[-1] = 0  # La distancia del nodo a sí mismo es 0
        self.matriz_adyacencia.append(nueva_fila)

    def agregar_arista(self, nodo1, nodo2, peso):
        # Establece el peso de la arista entre nodo1 y nodo2 en la matriz de adyacencia
        self.matriz_adyacencia[nodo1][nodo2] = peso

    def mostrar_matriz_adyacencia(self):
        # Imprime la matriz de adyacencia, reemplazando "inf" por "X" para mayor claridad
        print("Matriz de adyacencia:")
        for fila in self.matriz_adyacencia:
            fila_mostrada = ['X' if valor == float('inf') else valor for valor in fila]
            print(fila_mostrada)

    def dijkstra(self, nodo_inicial):
        # Inicializa las distancias y nodos visitados
        distancias = [float('inf')] * self.num_nodos
        distancias[nodo_inicial] = 0
        visitados = [False] * self.num_nodos

        for _ in range(self.num_nodos):
            # Encuentra el nodo con la menor distancia que aún no ha sido visitado
            min_dist = float('inf')
            min_nodo = -1
            for nodo in range(self.num_nodos):
                if not visitados[nodo] and distancias[nodo] < min_dist:
                    min_dist = distancias[nodo]
                    min_nodo = nodo

            # Marca el nodo como visitado
            visitados[min_nodo] = True

            # Actualiza las distancias a los nodos adyacentes
            for nodo_adyacente in range(self.num_nodos):
                if (self.matriz_adyacencia[min_nodo][nodo_adyacente] != float('inf') and 
                    not visitados[nodo_adyacente]):
                    nueva_distancia = distancias[min_nodo] + self.matriz_adyacencia[min_nodo][nodo_adyacente]
                    if nueva_distancia < distancias[nodo_adyacente]:
                        distancias[nodo_adyacente] = nueva_distancia

        # Imprime los resultados
        self.mostrar_resultados(nodo_inicial, distancias)

    def mostrar_resultados(self, nodo_inicial, distancias):
        # Imprime las distancias calculadas desde el nodo inicial a cada nodo
        print(f"Distancias desde el nodo {nodo_inicial}:")
        for nodo in range(self.num_nodos):
            if distancias[nodo] == float('inf'):
                print(f"Distancia a nodo {nodo}: X")
            else:
                print(f"Distancia a nodo {nodo}: {distancias[nodo]}")

# Ejemplo de uso
grafo = Grafo(5)

grafo.agregar_arista(0, 1, 7)
grafo.agregar_arista(0, 4, 3)
grafo.agregar_arista(1, 3, 6)
grafo.agregar_arista(2, 3, 2)
grafo.agregar_arista(3, 4, 8)
grafo.agregar_arista(1, 2, 4)
grafo.agregar_arista(4, 2, 5)

grafo.mostrar_matriz_adyacencia()
grafo.dijkstra(0)

# Ahora se agrega un nuevo nodo y luego se muestra la matriz adyacente nuevamente
print("\nDespués de agregar un nuevo nodo:")
grafo.agregar_nodo()
grafo.mostrar_matriz_adyacencia()
