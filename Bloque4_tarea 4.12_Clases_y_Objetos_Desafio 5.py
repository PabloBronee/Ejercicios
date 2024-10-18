'''
Arovechando las ventajas de la programacion orientada a objetos, este ejercicio podria realizarse
desde varios enfoques distintos. Ya fuera buscando el libro por su titulo, por su genero, o incluso
por su isbn. Lo mismo con su autor, pudiendo buscarlo por nombre o nacionaldiad. Sin embargo, para
este ejercicio voy a decantarme por la simplicidad de buscar libros por su titulo, valiendome de la 
ya armada estructura de biblioteca->Autor->Libro. Para ello creare un nuevo metodo "buscar_libros_por_titulo".
que se ubicara en la clase biblioteca, y hara lo dicho partiendo de buscar entre los libros de
cada autor indexado.
'''

class Autor:
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = [] #Ahora esta lista se encargara de almacenar objetos tipo libro, en lugar de strings

    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print("Libros del autor:")
        for libro in self.libros: #Se muestran todos los libros del autor
            print(f"- {libro.titulo}({libro.genero}, {libro.isbn})")

    #Se crea un metodo para agregar libros a la lista de libros. 
    def agregar_libro(self, libro):
        if isinstance(libro, Libro): #Se comprueba que el libro elegido pertenezca a la clase "Libro"
            self.libros.append(libro)
            print(f"Se agrego '{libro.titulo}' a la lista de libros.")
        else:
            print(f"{libro} no es un libro valido para ser registrado")

    #Se crea un metodo para eliminar libros a la lista de libros
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Se ha eliminado '{libro.titulo}' de la lista de libros")
        else:
            print(f"No se ha encontrado '{libro}' en la lista")

class Libro: #Se instancia con la primer letra en maysucula para identificar su tipo de objeto en el codigo
    def __init__(self, titulo, genero, isbn):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn

    def mostrar_libro(self):
        print(f"Título: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"ISBN: {self.isbn}")
    
class Biblioteca:
    def __init__(self):
        self.autores = [] #Lista para trabajar con objetos tipo autor

    def agregar_autor(self, autor):
        if isinstance(autor, Autor):
            self.autores.append(autor)
            print(f"El autor {autor.nombre} fue indexado correctamente")
        else:
            print(f"El autor {autor} no cumple los requisitos para indexarse")
    
    def mostrar_autores(self):
        for autor in self.autores:
            print(f"- {autor.nombre} ({autor.nacionalidad})")
    
    def agregar_libro_a_autor(self, libro, autor):
        if isinstance(autor, Autor) and isinstance(libro, Libro):
            autor.agregar_libro(libro)
            print(f"El libro {libro.titulo} fue añadido a los libros del autor {autor.nombre} correctamente")
        else:
            print("El libro no cumple los requisitos para ser indexado, o el autor no se encontro")
    
    def mostrar_libros_por_autor(self, autor):
        if isinstance(autor, Autor):
            print(f"Libros del autor {autor.nombre}: ")
            for libro in autor.libros:
                print(f"- {libro.titulo} ({libro.genero}, ISBN: {libro.isbn})")
        else:
            print(f"El autor {autor} no se encontro")
    
    def buscar_libros_por_titulo(self):
        titulo_libro = input("Que libro buscas?: ").lower()
        encontrado = False
        for autor in self.autores:
            for libro in autor.libros:
                if libro.titulo.lower() == titulo_libro:
                    print(f"Libro encontrado: {libro.titulo} ({libro.genero}, ISBN: {libro.isbn}) - Autor: {autor.nombre}")
                    encontrado = True
        if encontrado:
            print("")
        else:
            print(f"Libro {titulo_libro} no encontrado en la biblioteca")


#Ejemplos de uso de lo solicitado por el ejercicio 5

#Se crean dos autores en forma de objeto, y se asignan sus valores basicos en el constructor de autores
autor1 = Autor("Mario Benedetti", "Uruguayo") 
autor2 = Autor("Jack Townsend", "Estadounidense")

#Se crean dos objetos libro, y se le asignan sus valores basicos a su constructor
libro1 = Libro("Gracias por el fuego", "Novela", "001")
libro2 = Libro("Tales from the Gas Station", "Novela", "002")

#Se crea el objeto "biblioteca"
biblioteca1 = Biblioteca()

#Se añaden los dos autores creados a la biblioteca
biblioteca1.agregar_autor(autor1)
biblioteca1.agregar_autor(autor2)

#Se le agrega un libro creado a cada autor ya indexado en la biblioteca
biblioteca1.agregar_libro_a_autor(libro1, autor1)
biblioteca1.agregar_libro_a_autor(libro2, autor2)

#Se muestran los autores ya indexados en la biblioteca
biblioteca1.mostrar_autores()

'''
Como solicita el ejercicio 5, se utiliza una funcion de busqueda. En este caso, a traves del titulo
Ingresar "Gracias por el fuego" o "Tales from the Gas Station", o un libro no agregado, para comprobar resultado
'''
biblioteca1.buscar_libros_por_titulo() 



    




    
