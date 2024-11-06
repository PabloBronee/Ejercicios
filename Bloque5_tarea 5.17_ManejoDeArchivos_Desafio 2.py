# Incializacion del archivo de "textos por autores"
with open("libros_por_autor.txt", "w") as archivo:
    archivo.write("Textos:\n")
    archivo.write("Lovecraft: Las montañas de la locura\n")
    archivo.write("Lovecraft: La sombra sobre Insmouth\n")
    archivo.write("Edgar Allan Poe: El gato negro\n")
    archivo.write("Jack Tonsend: Buscando a Vanessa\n")

#Creacion del metodo para buscar libros de un autor concreto
def buscar_libros_por_autor(autor):
    libros_del_autor = []
    hay_libros = False
    with open("libros_por_autor.txt", "r") as archivo:
        for linea in archivo:
            if autor in linea:
                hay_libros = True
                libros_del_autor.append(linea)
    if hay_libros == True:
        print("Se encontro:")
        for x in range(len(libros_del_autor)):
            print(f"-{libros_del_autor[x]}")
    if hay_libros == False:
        print(f"No se encontraron libros de {autor}")

#Prueba de ejemplo
autor_elegido = input("Elige un autor: ")
buscar_libros_por_autor(autor_elegido)