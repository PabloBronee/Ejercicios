# Función para encontrar el mayor de tres números
def encontrar_mayor(num1, num2, num3):
    # Verificar si todos los números son iguales
    if num1 == num2 == num3:
        print("Todos los números son iguales.")
    else:
        # Determinar cuál es el mayor número
        mayor = max(num1, num2, num3)
        print(f"El número mayor es: {mayor}")

# Solicitar al usuario que ingrese tres números enteros
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Llamar a la función para determinar el mayor número
encontrar_mayor(num1, num2, num3)