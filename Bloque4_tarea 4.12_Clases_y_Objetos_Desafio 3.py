'''
Para este ejercicio podemos lograr la consigna en base a crear una nueva clase "biblioteca", donde se 
organizaran los autores con sus respectivos libros. Se podran agregar libros a los autores dentro
de esta biblioteca a traves de valernos de una mezcla de metodos propios de la clase bibliteca, como
de usar los propios metodos de los autores y su clase en ello. De la misma forma se podran obtener todos
los libros de un autor, como mostrar todos los autores indexados en la biblioteca.
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

#Ejemplos de uso de lo solicitado por el ejercicio 3

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

#Se muestran los libros de cada autor ya indexado de la biblioteca
biblioteca1.mostrar_libros_por_autor(autor1)
biblioteca1.mostrar_libros_por_autor(autor2)



    




    
