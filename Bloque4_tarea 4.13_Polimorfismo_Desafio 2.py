
# Se crea la clase Autor con un método biografía
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def biografia(self):
        return f"{self.nombre} es un autor de {self.nacionalidad}."

# Se crea la clase Escritor, que hereda de Autor y sobrescribe el método biografía
class Escritor(Autor):
    def __init__(self, nombre, nacionalidad, genero_literario):
        super().__init__(nombre, nacionalidad)
        self.genero_literario = genero_literario

    # Sobrescribimos el método biografía para dar más detalles
    def biografia(self):
        return f"{ super().biografia()} Esta especializado en {self.genero_literario}."

# Instancia un objeto de la clase Escritor
escritor1 = Escritor("Howard philips lovecraft", "Estadounidense", "Terror lovecraftiano")

# Mostrar cómo acceder al método biografia sobrescrito y el original
print(escritor1.biografia())  # Llamamos al método sobrescrito en Escritor

# Si quisieras llamar al método original de la clase Autor directamente:
print(Autor.biografia(escritor1))  # Llamamos al método biografía de Autor pasando el objeto escritor1
