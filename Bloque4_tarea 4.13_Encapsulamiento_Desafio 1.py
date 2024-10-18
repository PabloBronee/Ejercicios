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

# Ejemplo de uso de los getters:
libro1 = Libro("Las montañas de la locura", "Howard Phillips Lovecraft", "001")
print(libro1.get_titulo())  
print(libro1.get_autor())   
print(libro1.get_isbn())    

# Cambiar el isbn para ejemplificar los setters
libro1.set_isbn("002")
print(libro1.get_isbn())