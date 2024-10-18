class Libro:
    def __init__(self, titulo, autor, isbn):
        # Atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
    
    # Métodos getter
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_isbn(self):
        return self.__isbn

    # Métodos setter
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def set_autor(self, autor):
        self.__autor = autor
    
    def set_isbn(self, isbn):
        self.__isbn = isbn

class Autor:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = [] 

    def get_nombre(self):
        return self.__nombre
    
    def get_libros(self):
        return self.__libros

    def agregar_libros(self, libro):
        if isinstance(libro, Libro):
            print(f"El libro {libro.get_titulo()} se agrego correctamente al autor {self.get_nombre()}")
            self.__libros.append(libro)
        else:
            print("El libro no es valido para indexarse en el autor")

    def mostrar_libros(self):
        print("Libros del autor:")
        for libro in self.get_libros():  # Usamos el getter para obtener la lista
            print(f"- {libro.get_titulo()}") # Usamos el getter del propio objeto libro para obtener su titulo

# Ejemplo de lo solicitado por el desafio 2:

#Creamos un objeto libro y asisgnamos sus valores base
libro1 = Libro("Las montañas de la locura", "Howard Phillips Lovecraft", "001")

#Creamos un objeto autor y asisgnamos sus valores base
autor1 = Autor("Howard Phillips Lovecraft")

#Agregamos un libro al autor
autor1.agregar_libros(libro1)

#Mostramos los libros del autor
autor1.mostrar_libros()


   
