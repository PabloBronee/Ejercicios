import math

# Defe una excepción personalizada para números negativos
class NegativeNumberError(Exception):
    def __init__(self, mensaje = "Error: No se puede calcular la raíz cuadrada de un número negativo"):
        self.mensaje = mensaje
        super().__init__(self.mensaje) #Envia el mensaje asignado al constructor de la clase padre "Exception"

def calcular_raiz_cuadrada():
    try:
        # Solicitamos al usuario que ingrese un número
        num = float(input("Introduce un número para calcular su raíz cuadrada: "))
        
        # Si el número es negativo, lanzamos la excepción personalizada
        if num < 0:
            raise NegativeNumberError
        
        # Si el número es válido, calculamos la raíz cuadrada
        resultado = math.sqrt(num)
        print(f"La raíz cuadrada de {num} es: {resultado:.2f}") #Se limitan los decimales a 2
    
    except NegativeNumberError as x:
        # Capturamos la excepción personalizada y mostramos el mensaje de error
        print(x)
    
    except ValueError:
        # Captura si el valor ingresado no es un número válido
        print("Error: Debes introducir un número válido.")

# Llama a la función para probarla
calcular_raiz_cuadrada()