import random
import string
def crear_contraseña():
    # Asegura una letra mayúscula, una minúscula y un número
    mayuscula_asegurada = random.choice(string.ascii_uppercase)
    minuscula_asegurada = random.choice(string.ascii_lowercase)
    numero_asegurado = random.choice(string.digits) 

    # Genera los 5 caracteres restantes (mezcla de letras y números)
    digitos_faltantes = random.choices(string.ascii_letters + string.digits, k=5) 

    # Combina todos los caracteres
    contraseña = [mayuscula_asegurada, minuscula_asegurada, numero_asegurado] + digitos_faltantes
    
    # Retorna la contraseña como un string
    return(''.join(contraseña))
    

print(f"Tu nueva contraseña es: {crear_contraseña()}")
