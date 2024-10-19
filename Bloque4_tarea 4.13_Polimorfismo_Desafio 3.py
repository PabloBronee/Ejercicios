# Clase base Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}"

# Subclase LibroEspecializado que hereda de Libro
class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel_especializacion):
        # Inicializamos los atributos de la clase base
        super().__init__(titulo, autor)
        # Nuevos atributos para la clase especializada
        self.campo_estudio = campo_estudio
        self.nivel_especializacion = nivel_especializacion

    # Sobrescribimos el método para mostrar información del libro especializado
    def mostrar_info(self):
        return (f"{super().mostrar_info()}, Campo de estudio: {self.campo_estudio}, Nivel: {self.nivel_especializacion}")

# Instanciamos un objeto de LibroEspecializado
libro_especializado1 = LibroEspecializado("Necronomicon", "Terrores indescriptibles", "Lo indecible", "avanzado")

# Mostramos la información del libro especializado
print(libro_especializado1.mostrar_info())

