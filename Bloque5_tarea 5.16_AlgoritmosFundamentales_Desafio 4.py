def ordenar_por_promedio(estudiantes):
    # Recorremos toda la lista de estudiantes
    for i in range(len(estudiantes)):
        # Suponemos que el índice `i` tiene el promedio más alto en esta iteración
        max_indice = i
        # Encontramos el estudiante con el promedio más alto en la sublista que queda
        for j in range(i + 1, len(estudiantes)):
            if estudiantes[j][1] > estudiantes[max_indice][1]:  # Comparamos promedios
                max_indice = j

        # Intercambiamos el estudiante con el promedio más alto encontrado con la posición `i`
        estudiantes[i], estudiantes[max_indice] = estudiantes[max_indice], estudiantes[i]

# Ejemplo de uso
# Lista de estudiantes con sus promedios
estudiantes = [
    ("Ana", 85.5),
    ("Carlos", 90.3),
    ("Daniel", 78.2),
    ("Fernanda", 92.7),
    ("Luis", 88.9),
    ("Sofía", 95.4)
    ]

ordenar_por_promedio(estudiantes)

# Imprimimos los estudiantes ordenados de mayor a menor promedio
for estudiante, promedio in estudiantes:
    print(f"{estudiante}: {promedio}")
