# Crear el archivo 'libros.txt' con contenido de prueba
with open("libros.txt", "w", encoding="utf-8") as archivo:
    archivo.write("El Quijote es un libro muy famoso.\n")
    archivo.write("Cien Años de Soledad es otro gran libro.\n")
    archivo.write("Orgullo y Prejuicio es una novela clásica.\n")
    archivo.write("1984 es una obra distópica.\n")

def contar_palabras(file_name):
    # Contenedor para las palabras y su contador
    palabra_contador = {}

    # Abrir el archivo para leerlo línea por línea
    with open(file_name, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # Convertir a minúsculas y eliminar signos de puntuación
            linea = linea.lower().strip()  # Convertimos a minúsculas y eliminamos espacios extras al inicio y al final
            palabra = ""

            # Reemplazar todos los caracteres no alfanuméricos por espacios
            for char in linea:
                if char.isalnum() or char.isspace():  # Solo letras, números y espacios
                    palabra += char
                else:
                    palabra += ' '  # Reemplazar cualquier otro carácter por espacio

            # Dividir la línea en palabras
            lista_palabras = palabra.split()

            # Contar las palabras
            for palabra in lista_palabras:
                if palabra in palabra_contador:
                    palabra_contador[palabra] += 1
                else:
                    palabra_contador[palabra] = 1

    # Ordenar las palabras por frecuencia y obtener las 5 más comunes
    palabras_ordenadas = sorted(palabra_contador.items(), key=lambda item: item[1], reverse=True)

    # Diagnóstico: Mostrar todas las palabras y su frecuencia
    print("\nPalabras ordenadas por frecuencia (solo las primeras 10):")
    for i in range(min(10, len(palabras_ordenadas))):  # Mostrar solo las primeras 10 palabras
        print(f"{palabras_ordenadas[i][0]}: {palabras_ordenadas[i][1]}")

    # Mostrar las 5 palabras más comunes
    print("\nLas 5 palabras más comunes son:")
    for i in range(min(5, len(palabras_ordenadas))):  # En caso de que haya menos de 5 palabras
        print(f"{palabras_ordenadas[i][0]}: {palabras_ordenadas[i][1]}")

# Llamada a la función con el archivo 'libros.txt'
contar_palabras("libros.txt")

