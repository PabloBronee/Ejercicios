def contar_platanos(pilas, pila_actual=0, conteo_actual=0, total_acumulado=0):
    # Caso base: si ya no hay más pilas que contar, devuelve el total acumulado
    if pila_actual >= len(pilas):
        return total_acumulado
    
    # Caso recursivo: el mono cuenta plátanos uno a uno en la pila actual
    conteo_actual += 1
    
    # Si termina de contar la pila actual
    if conteo_actual >= pilas[pila_actual]:
        # Actualiza el total acumulado
        total_acumulado += conteo_actual
        
        # Pasa a la siguiente pila, reseteando el conteo actual a cero
        return contar_platanos(pilas, pila_actual + 1, 0, total_acumulado)
    
    # Sigue contando en la pila actual
    return contar_platanos(pilas, pila_actual, conteo_actual, total_acumulado)

# Ejemplo de uso
pilas_de_platanos = [5, 3, 7]  # El mono cuenta 5 plátanos, luego 3 y finalmente 7
total = contar_platanos(pilas_de_platanos)
print(f"El total acumulado de plátanos contados es: {total}")  # Debería ser 15