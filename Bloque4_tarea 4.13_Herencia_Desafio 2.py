#Se crea la clase usuario y bibliotecario, como especifica el desafio 2
class Usuario:
    def __init__(self,nombre):
        self.nombre = nombre

class Bibliotecario(Usuario):
    def __init__(self, nombre, seccion, años_experiencia):
        super().__init__(nombre)
        self.seccion = seccion
        self.años_experiencia = años_experiencia

#Se crea un objeto bibliotecario y se obtienen sus datos para comrpobar lo especificado por el desafio 2
bibliotecario1 = Bibliotecario("Juan", "Literatura juvenil", "5")
print(f"El bibliotecario {bibliotecario1.nombre} tiene {bibliotecario1.años_experiencia} años de experiencia, trabaja en la seccion de {bibliotecario1.seccion}")