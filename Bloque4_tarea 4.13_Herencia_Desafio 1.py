# Definimos la clase base Autor
class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

# Creamos una subclase Escritor que hereda de Autor
class Escritor(Autor):
    def __init__(self, nombre, genero):
        super().__init__(nombre)
        self.genero = genero

#Creamos la clase poeta, con las especificaciones del ejercicio 1
class Poeta(Escritor):
    def __init__(self, nombre, genero, tipo_de_poesia):
        super().__init__(nombre, genero)
        self.tipo_de_poesia = tipo_de_poesia

# Instanciamos un objeto de la subclase Poeta, como lo especifica el ejercicio 1
poeta1 = Poeta("Pablo Neruda", "Poesía", "Poesia Pasional")

#Se obtienen los datos del poeta creado
print(f"El poeta creado seria: {poeta1.nombre}, su genero literario seria la misma {poeta1.genero}, y el tipo de esta radicaria en {poeta1.tipo_de_poesia}")