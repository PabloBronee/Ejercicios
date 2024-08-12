
'''
Decido usar la funcion "title" para realizar el ejercicio, aunque este tambien podria haberse realizado
valiendose de la funcion "split", y "upper" de la forma correcta, con el algoritmo correcto.

Primero instancio un def, el cual ha de recibir una cadena cualquiera, y regresar la misma cadena, pero 
con mayuscula en la primera letra de cada palabra
'''
def mayuscula_al_inicio_de_cada_palabra(cadena):
    return cadena.title()

#Instancio la cadena de texto a usarse
texto = "hoy es lunes por la mañana"

#Genero una variable con el texto elegido, pero al que se le aplicara el def que solicitaba el desafio
resultado = mayuscula_al_inicio_de_cada_palabra(texto)

#Muestro el resultado solicitado
print(resultado)

