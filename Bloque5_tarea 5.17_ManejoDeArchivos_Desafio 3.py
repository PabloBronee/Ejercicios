import csv

# Se crea el archivo CSV para el inventario
with open("inventario.csv", "w", newline="") as inventario_csv:
    escritor_csv = csv.writer(inventario_csv)
    escritor_csv.writerow(["Libros", "Cantidad de copias"])
    escritor_csv.writerow(["It", "1"])
    escritor_csv.writerow(["Buscando a vanessa", "2"])
    escritor_csv.writerow(["El rey de amarillo", "3"])

#Se crea el metodo para actualizar la cantidad de copias de un libro en especifico
def actualizar_copias(titulo, cantidad_actualizada):
    filas = []
    # Leer el archivo CSV y guardar las filas en una lista
    with open("inventario.csv", "r") as inventario_csv:
        lector_csv = csv.reader(inventario_csv)
        for fila in lector_csv:
            if fila[0] == titulo:
                # Actualizar la cantidad de copias
                fila[1] = str(cantidad_actualizada)
            filas.append(fila)
    
    # Escribir el archivo CSV con las filas actualizadas
    with open("inventario.csv", "w", newline="") as inventario_csv:
        escritor_csv = csv.writer(inventario_csv)
        escritor_csv.writerows(filas)

    # Imprimir el inventario actualizado en consola
    print("Inventario actualizado:")
    for fila in filas:
        print(f"{fila[0]}|{fila[1]}")

#Prueba de ejemplo:
actualizar_copias("It", "2")