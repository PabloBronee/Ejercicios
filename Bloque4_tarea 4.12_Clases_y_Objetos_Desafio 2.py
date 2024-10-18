'''
Para este ejercicio podemos lograr la consigna en base a crear una clase para los propios libros, y
directamente hacer que la clase autor trabaje tambien con objetos tipo "libro" de dicha clase.
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
    
#Ejemplos de uso de lo solicitado por el ejercicio 2

#Se crea el objeto "autor1" y se asignan sus valores basicos en el constructor
autor1 = Autor("Mario Benedetti", "Uruguayo") 

#Se crean dos objetos libro, y se le asignan sus valores basicos a su constructor
libro1 = Libro("Gracias por el fuego", "Novela", "001")
libro2 = Libro("La muerte y otras sorpresas", "Novela", "002")

#Se agregan los dos objetos libros creados al objeto autor, con el metodo creado para ello
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)

#Se muestra el objeto autor, tras haberse actualizado su repertorio de libros
autor1.mostrar_autor()

#Se elimina uno de los libros agregados y se muestra el autor nuevamente tras la actualizacion
autor1.eliminar_libro(libro1)
autor1.mostrar_autor()


    




    
