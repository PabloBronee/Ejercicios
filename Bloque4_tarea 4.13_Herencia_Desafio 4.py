# Creamos la clase Escritor
class Escritor:
    def __init__(self, nombre, genero):
         self.nombre = nombre
         self.genero = genero

# Creamos la clase Academico
class Academico:
    def __init__(self, universidad):
        self.universidad = universidad

''' 
Creamos la clase EscritorAcademico, que hereda tanto de escritor como de academico,
incluyendo un nuevo metodo para publicar articulos academicos como pide el desafio 4
''' 
class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, universidad):
        #En esta seccion, al esta clase heredar directamente de dos clases, se debe especificar el upper de ambas clases padre
        Escritor.__init__(self, nombre, genero)
        Academico.__init__(self, universidad) 

    def publicar_articulo_academico(self, articulo):
        print(f"El autor {self.nombre} publica el articulo {articulo}")
        
#Se crea un objeto EscritorAcademico, y se utiliza el metodo pedido por el desafio 4 desde este
escritor_academico1 = EscritorAcademico("Howard Philips Lovecraft", "horror lovecraftiano", "Providence Academy")

escritor_academico1.publicar_articulo_academico("La decadencia del horro del siglo 19")
    

