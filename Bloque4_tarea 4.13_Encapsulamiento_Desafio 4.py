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
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = [] 

    # Getter para 'nombre' usando property
    @property
    def nombre(self):
        return self.__nombre
    
    # Setter para 'nombre' usando property
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Getter para 'Nacionalidad' usando property
    @property
    def nacionalidad(self):
        return self.__nacionalidad
    
    # Setter para 'Nacionalidad' usando property
    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        self.__nacionalidad = nueva_nacionalidad
    
    def get_libros(self):
        return self.__libros

    def agregar_libros(self, libro):
        if isinstance(libro, Libro):
            print(f"El libro {libro.get_titulo()} se agrego correctamente al autor {self.nombre}")
            self.__libros.append(libro)
        else:
            print("El libro no es valido para indexarse en el autor")

    def mostrar_libros(self):
        print("Libros del autor:")
        for libro in self.get_libros():  # Usamos el getter para obtener la lista
            print(f"- {libro.get_titulo()}") # Usamos el getter del propio objeto libro para obtener su titulo

# Ejemplo de lo solicitado por el desafio 4:

#Creamos un objeto autor y asisgnamos sus valores base
autor1 = Autor("Howard Phillips Lovecraft", "Estadounidense")

#Creamos una serie de objetos libro y le  asignamos sus valores base
libro1 = Libro("Las montañas de la locura", "HP Lovecraft", "001")
libro2 = Libro("La sombra sobre Insmouth", "HP Lovecraft", "002")
libro3 = Libro("El color que callo del cielo", "HP Lovecraft", "003")

#Asignamos los libros creados al autor creado
autor1.agregar_libros(libro1)
autor1.agregar_libros(libro2)
autor1.agregar_libros(libro3)

#Creamos y ejecutamos el algoritmo solicitado por el desafio 4
def obtener_titulos_de_autor(autor):
    if isinstance(autor, Autor):
        return [libro.get_titulo() for libro in autor.get_libros()]
    
print(f"Todos los libros del autor son: {obtener_titulos_de_autor(autor1)}")
   
