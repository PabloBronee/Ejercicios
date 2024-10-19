# Clase base Operacion
class Operacion:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def resultado(self):
        pass  # Método a ser sobrescrito por las subclases

# Subclase Suma que sobrescribe el método resultado
class Suma(Operacion):
    def resultado(self):
        return self.valor1 + self.valor2

# Subclase Multiplicacion que sobrescribe el método resultado
class Multiplicacion(Operacion):
    def resultado(self):
        return self.valor1 * self.valor2

# Ejemplo de uso
operacion1 = Suma(5, 3)
print(f"Suma: {operacion1.resultado()}")  # Resultado: 8

operacion2 = Multiplicacion(5, 3)
print(f"Multiplicación: {operacion2.resultado()}")  # Resultado: 15
