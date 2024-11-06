import math

def calcular_factorial():
    try:
        # Solicita al usuario que ingrese un numero
        num = int(input("Introduce un numero entero positivo: "))
        
        # Verifica si el numero es negativo
        if num < 0:
            raise ValueError("El numero no puede ser negativo")
        
        # Calcula el factorial usando la función factorial del modulo math
        resultado = math.factorial(num)
        print(f"El factorial de {num} es: {resultado}")
    
    except ValueError as x:
        # Captura si el valor no es un entero válido o es negativo
        print(f"Error: {x}")
    
    except OverflowError:
        # Captura si el numero es demasiado grande para ser procesado
        print("Error: El numero es demasiado grande como para calcular su factorial")

# Llama a la funcion para probarla
calcular_factorial()
