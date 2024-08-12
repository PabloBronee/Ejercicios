
'''
El desafio en cuestion se me dificulto de cara a que no tenia idea de como saber si un numero es primo o no en si mismo. Tras
buscar alternativas, creo haber dado, y entendido, la que me resulto mas simple. Procedo a desarrollar el desafio a la par que explicar
su funcionamiento

Primero que nada, instancio el def encargado de verificar si el numero en cuestion es primo:
'''
def verifica_primos(num):
    if num < 2:
        '''
        Esta comprobacion inicial es tan simple como que los números menores que 2 no son primos. 
        Por lo que, si el número es menor que 2, la función directamente devuelve False 
        '''
        return False
    for i in range(2, int(num**0.5) + 1):
        '''
        El bucle for de arriba se repite desde 2 hasta la raíz cuadrada de num (incluyendo el entero más cercano). 
        Esto se debe a que un número no puede tener un divisor mayor que su raíz cuadrada sin tener un divisor menor que su raíz cuadrada.
        Factor que cobra importancia, debido a que si no encontramos ningún divisor menor o igual a la raíz cuadrada de num,
        significa que no habrá divisores mayores que la raíz cuadrada que no hayan sido ya considerados.
        '''
        if num % i == 0:
            '''
            Aqui, dentro del bucle, se verifica si num es divisible por i. 
            Si es divisible, num no es primo y la función devuelve False.
            '''
            return False
    return True 
    '''
    Si el bucle de arriba termina sin encontrar ningún divisor, significara que num solo es divisible por 1 y por si mismo, 
    y que por ende es primo, por lo que la función devuelve True.
    '''

'''
Ahora creo un def que, aprovechando el def anterior, recibe la lista de numeros elegidos en cuestion, y los pasa
todos por el def de verificar si el numero es primo o no, a la par que va incrementando la cuenta de los primos allados. Finalmente,
regresa el total de primos allados.
'''
def contar_primos(lista):
    primos_totales = 0
    for num in lista:
        if verifica_primos(num):
            primos_totales += 1
    return primos_totales

'''
Creo el main solicitado, donde instancio la lista de numeros a usarse. Finalmente, muestro con un print el resultado del
conteo de cuantos numeros primos contiene dicha lista, valiendome de las dos funciones previas creadas al hacerlo.
'''
def main():
    lista_numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(f"En la lista hay {contar_primos(lista_numeros)} números primos.")

'''
Llamo el main en cuestion para que se ejecute el proceso solicitado por el desafio.
'''
main()