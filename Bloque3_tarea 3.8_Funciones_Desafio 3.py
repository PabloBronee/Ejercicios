
'''
Primero instancio ambas listas a utilizarse en el desafio
'''
lista_1 = [1,2,3,4,5]
lista_2 = [5,6,7,8,9]

'''
Ahora creo un def, encargado de recibir dos listas, y pasarlas por un bucle for donde se analizara cada elemento
de una en la otra, buscando similitudes. Si encuentra almenos un numero repetido regresara true, de lo contrario, 
regresara false

parametros:
a: primera lsita
b: segunda lista

retorna: True de haber almenos un numero repetido, False de lo contrario
'''
def busca_repetidos(a, b):
    for _ in a:
        if _ in b:
            return True  # Retorna True inmediatamente si encuentra un repetido
    return False  # Retorna False si no encuentra ningún repetido

#Se crea un if para mostrar en consola si hubo o no repetidos con un print, usando el true/false obtenido
if busca_repetidos(lista_1, lista_2):
    print("Hubo repetidos")
else:
    print("No hubo repetidos")


        
    



