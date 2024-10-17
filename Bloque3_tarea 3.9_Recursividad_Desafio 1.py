
#Se crea una funcion encargada de conseguir el maximo comun divisor a traves del "Algoritmo de Euclides".
def maximo_comun_divisor(a, b):
     # Caso base: si b es 0, se encontro el MCD, que es a. Seguido se devuelve el mcd "a"
    if b == 0:
        return a
    # Si b no es 0, se llama recursivamente a la función, utilizando b y el residuo de a dividido entre b.
    else:
        return maximo_comun_divisor(b, a % b)
    
#Se prueba la funcion y se imprimen los resultados, en este caso hallando el mcd de 8 y 12
print(str(maximo_comun_divisor(8,12)))