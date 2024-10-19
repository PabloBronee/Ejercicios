import math

# Clase base Figura
class Figura:
    def area(self):
        pass  # Método que será sobrescrito por las subclases

# Subclase Circulo que hereda de Figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    # Sobrescribimos el método area para calcular el área de un círculo
    def area(self):
        return math.pi * (self.radio ** 2) #Pi por radio al cuadrado

# Subclase Cuadrado que hereda de Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    # Sobrescribimos el método area para calcular el área de un cuadrado
    def area(self):
        return self.lado ** 2 #Lado al cuadrado

# Instanciamos objetos de Circulo y Cuadrado
circulo1 = Circulo(5)  # Radio = 5
cuadrado1 = Cuadrado(4)  # Lado = 4

# Usamos polimorfismo para llamar al método area
figuras = [circulo1, cuadrado1]

for figura in figuras:
    print(f"El área de la figura es: {round(figura.area())}") #Se agrega un round para redondear el resultado de las areas
