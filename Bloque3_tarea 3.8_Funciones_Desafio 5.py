
'''
Primero que nada instancio la cadena a utilizarse con el def proximo
'''
cadena_elegida = "A ti no, bonita"

'''
Ahora creo el def encacrgado de comprobar si la cadena es un palindromo. Para esto realiza reviamente una serie de acciones:
'''
def comprueba_palindromo(cadena):
    '''
    Primero convierte la cadena en cuestion en minusculas usando "lower", a la par que reemplaza los espacios vacios y las comas con
    recortes, para que la palabra este unida y en minusculas, sin trabas de por medio para analizarla.
    '''
    cadena = cadena.lower().replace(" ", "").replace(",", "") 
    '''
    Posterior a ello regresa un true o false, tras haber comprobado con "[::-1]" si la cadena es igual a su version invertida.
    '''
    return cadena == cadena[::-1]

#Instancio una variable encargada de recibir el true o falso de ser palidromo o no serlo respectivamente, para usarlo en el proximo if
es_palidromo = comprueba_palindromo(cadena_elegida)

#Muestra un mensaje en la consola con el resultado, ya sea que sea palidromo o no
if es_palidromo:
    print(f"{cadena_elegida} es palidromo")
else:
    print(f"{cadena_elegida} No es palidromo")
