def buscar_estudiante(lista_estudiantes, nombre):
    # Definimos los índices inicial y final para la búsqueda binaria
    inicio = 0
    fin = len(lista_estudiantes) - 1
    
    while inicio <= fin:
        # Calculamos el índice del punto medio
        medio = (inicio + fin) // 2
        # Obtenemos el nombre en el índice medio
        nombre_medio = lista_estudiantes[medio]
        
        # Comparamos el nombre buscado con el nombre en la posición media
        if nombre_medio == nombre:
            return f"{nombre} encontrado en la posición {medio + 1}"
        elif nombre < nombre_medio:
            fin = medio - 1  # Buscamos en la mitad izquierda
        else:
            inicio = medio + 1  # Buscamos en la mitad derecha
    
    return f"{nombre} no se encuentra en la lista"

# Ejemplo de uso
# Lista de estudiantes ordenada alfabéticamente
estudiantes = ["Ana", "Carlos", "Daniel", "Fernanda", "Luis", "Sofía"]
    
nombre_busqueda = "Luis"
resultado = buscar_estudiante(estudiantes, nombre_busqueda)
print(resultado)

# Prueba con un nombre no existente
nombre_busqueda = "María"
resultado = buscar_estudiante(estudiantes, nombre_busqueda)
print(resultado)
