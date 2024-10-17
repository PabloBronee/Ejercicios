'''
Para resolver el ejercicio solicitado, prescindiendo de metodos de python para invertir 
cadeenas o listas, se opta por crear una funcion que divida el texto en palabras y luego
invierta cada palabra,
'''

def invertir_palabra(palabra):
    # Caso base: si la palabra esta vacía o tiene un solo carácter, ya está invertida
    if len(palabra) <= 1:
        return palabra
    '''
    llamada recursiva. Esta seccion es la clave del funcionamiento de este codigo, dado que valiendose
    de recursividad con"palabra[1:]" toma todos los caracteres de la palabra, exceptuando el primero,
    y luego agrega dicho caracter al final de la palabra con "palabra[0]". El proceso se repite hasta que no
    quedan mas caracteres por invertir, y entonces de regresa la palabra invertida con el return.
    '''
    return invertir_palabra(palabra[1:]) + palabra[0]

def invertir_oracion(oracion):
    # Caso base: si la oración está vacía, no hay nada que invertir
    if ' ' not in oracion:
        return invertir_palabra(oracion)
    
    # Encuentra el primer espacio para separar la primera palabra
    i = 0
    while i < len(oracion) and oracion[i] != ' ':
        i += 1
    
    # Invertir la primera palabra y aplicar la función recursiva al resto de la oración
    primera_palabra_invertida = invertir_palabra(oracion[:i])
    resto_invertido = invertir_oracion(oracion[i+1:]) if i+1 < len(oracion) else ''
    
    # Concatenar la palabra invertida con el resto invertido
    return primera_palabra_invertida + (' ' + resto_invertido if resto_invertido else '')

# Ejemplo de uso del codigo
oracion = "Esto es una prueba"
resultado = invertir_oracion(oracion)
print(resultado)  # Resultado: otsE se anu abeurp