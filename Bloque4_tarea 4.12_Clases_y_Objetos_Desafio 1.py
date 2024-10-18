class Autor:
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = [] #Lista para almacenar los libros del autor

    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print("Libros del autor:")
        for libro in self.libros: #Se muestran todos los libros del autor
            print(f"- {libro}")

    #Se crea un metodo para agregar libros a la lista de libros
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Se agrego '{libro}' a la lista de libros.")

    #Se crea un metodo para eliminar libros a la lista de libros, con precauciones en caso de no encontrarse dicho libro en la lista
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Se ha eliminado '{libro}' de la lista de libros")
        else:
            print(f"No se ha encontrado '{libro}' en la lista")

#Ejemplos de uso de lo solicitado por el ejercicio 1

#Se crea el objeto "autor1" y se asignan sus valores basicos en el constructor
autor1 = Autor("Mario Benedetti", "Uruguayo") 
#Se agregan dos libros al objeto autor1, con el metodo creado para ello
autor1.agregar_libro("Gracias por el fuego") 
autor1.agregar_libro("La muerte y otras sorpresas") 
#Se muestran todos los datos tras las adiciones
autor1.mostrar_autor() 
#Se actualiza la lista de libros borrando unb libro añadido, y se muestra nuevamente tras dicha actualizacion
autor1.eliminar_libro("La muerte y otras sorpresas") 
autor1.mostrar_autor()

    




    
