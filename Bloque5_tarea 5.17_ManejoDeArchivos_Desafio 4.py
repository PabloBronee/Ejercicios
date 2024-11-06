# Crear el archivo de préstamos con algunos registros iniciales
with open("prestamos.txt", "w") as archivo:
    archivo.write("Préstamo de 'El rey de amarillo' a Martina\n")
    archivo.write("Préstamo de 'Relatos de Gasolinera' a Eugenia\n")
    archivo.write("Préstamo de 'Buscando a Vanessa' a Pablo\n")
    archivo.write("Préstamo de 'Las montañas de la locura' a Lucas\n")

def mostrar_prestamos():
    print("Registros de préstamos actuales:")
    with open("prestamos.txt", "r") as archivo:
        prestamos = archivo.readlines()
        for idx, prestamo in enumerate(prestamos, start=1):
            print(f"{idx}. {prestamo.strip()}")
    return prestamos

def eliminar_prestamo():
    # Mostrar los préstamos actuales
    prestamos = mostrar_prestamos()

    # Verificar si hay préstamos para eliminar
    if not prestamos:
        print("No hay registros de préstamos para eliminar.")
        return

    # Solicitar al usuario que elija un préstamo para eliminar
    numero = int(input("Ingrese el número del préstamo que desea eliminar: "))
    if numero < 1 or numero > len(prestamos):
        print("Número de préstamo inválido.")
        return

    # Eliminar el préstamo seleccionado de la lista
    prestamos.pop(numero - 1)

    # Reescribir el archivo sin el préstamo eliminado
    with open("prestamos.txt", "w") as archivo:
        archivo.writelines(prestamos)

    print("\nEl préstamo ha sido eliminado con éxito.")
    # Mostrar el archivo actualizado
    mostrar_prestamos()

# Ejecución del programa
eliminar_prestamo()
