#Se crea la clase Libro como especifica el desafio 3
class Libro:
    def __init__(self,titulo):
        self.titulo = titulo

    def mostrar_info(self):
        return(f"El titulo es {self.titulo}")

#Se crea la clase libro digital, añadiendo lo correspondiente, y heredando de libro como especifica el desafio
class LibroDigital(Libro):
    def __init__(self, titulo, formato, tamaño_archivo):
        super().__init__(titulo)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

#Se crea la sublclase ebook, la cual sobreescribe el metodo para mostrar informacion, agregando enlace de descarga
class EBook(LibroDigital):
    def __init__(self, titulo, formato, tamaño_archivo, enlace_descarga):
        super().__init__(titulo, formato, tamaño_archivo)
        self.enlace_descarga = enlace_descarga

    def mostrar_info(self):
        return(f"El titulo es {self.titulo}, y su enlace de descarga: {self.enlace_descarga}")
    
#Se crea un objeto Ebook y luego se muestra el metodo de mostrar info que sobreescribe, para comprobar el desafio 3
ebook1 = EBook("Las montañas de la locura", "pdf", "2mb", "https/urlinventada.com")

print(f"{ebook1.mostrar_info()}")