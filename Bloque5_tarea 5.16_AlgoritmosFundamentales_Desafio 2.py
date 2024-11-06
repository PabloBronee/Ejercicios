index_materias = ["lengua", "matematicas", "fisica"]
index_estudiantes = ["Lucas", "Pablo", "Eugenia"]

def buscar_calificacion(matriz, calificacion_buscada):
    # Recorremos cada fila y cada columna en la matriz
    for i, fila_estudiante in enumerate(matriz):
        for j, calificacion in enumerate(fila_estudiante):
            if calificacion == calificacion_buscada:
                return f"Calificación encontrada en el estudiante {index_estudiantes[i]}, materia {index_materias[j]}"
    
    return "Calificación no encontrada"

# Ejemplo de uso
# Matriz de ejemplo, donde cada fila es un estudiante y cada columna es una materia
calificaciones = [
    [85, 92, 78],   # Estudiante 1 (Lucas)
    [88, 90, 95],   # Estudiante 2 (Pablo)
    [75, 85, 89],   # Estudiante 3 (Eugenia)
     #lengua(1)     # Alumnos en orden de filas
         #matematicas(2)
              #fisica(3)
     # Materias en orden de columnas
]
    
calificacion_buscada = 90
resultado = buscar_calificacion(calificaciones, calificacion_buscada)
print(resultado)
