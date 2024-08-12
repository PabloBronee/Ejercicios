import math

# Se instancia la lista de numeros a usarse en el proximo def
lista = [1,2,3,4,5]

'''
Por un lado suma la lista de numeros, y por el otro calcula su promedio

Parametros:
a: Lista de numeros a utilizar

Retorna:
suma total de lista a, parametro de lista a
'''
def suma_y_promedia (a):
    resultado_suma = 0
    for _ in a: 
        resultado_suma += _
    promedio = resultado_suma // len(a)
    return resultado_suma, promedio

#Captura ambos resultados del def, y los captura en variables para poder mostrarlas de forma limpia en el print
suma_total, promedio_final = suma_y_promedia(lista)

#Muestra los resultados obtenidos de forma ordenada
print (f"La suma de la lista ingresada seria: {suma_total}, mientras que el promedio daria: {promedio_final}")

