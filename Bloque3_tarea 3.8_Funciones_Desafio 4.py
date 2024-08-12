
'''
El funcionamiento del algoritmo matematico, por lo que entendi, consta de que, siempre que B no sea 0, se ha de reemplazar A por B, y
B por el resto de la division entre A y B, repitiendo el proceso hasta que B sea 0. Entonces, cuando suceda,
el maximo comun divisor "mcd" sera A.

Primero instancio las variables a usarse para la demostracion:
'''
dato_1 = 56
dato_2 = 96

'''
Instancio un def que recibe ambos numeros elegidos "a" y "b", y relaiza el algoritmo matematico en cuestion con ellos. Regresa A ("a")
una vez B ("b") 0.
'''
def genera_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

mcd = genera_mcd(dato_1, dato_2)

print(f"El mcd de {dato_1} y {dato_2} es: {mcd}")
