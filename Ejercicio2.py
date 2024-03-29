Ancho = 5
Largo = 15
Explicacion = "Este programa primero instancia dos variables de tipo 'int' (Largo = " + str(Largo) + ", Ancho = " + str(Ancho) + "), las cuales representan el largo y el ancho del rectangulo, tras ello instancia la variable de tipo int 'Resultado', en donde para obtener su valor multiplica las variables de largo y ancho, utilizando la funcion 'MultiplicarNumeros'. Para finalizar ejecuta un 'print' En donde enseña una variable 'str' con esta explicacion, 'Explicacion', tras lo que muestra el resultado de la multiplicacion, que a la vez es el contenido de 'Resultado', es decir, lo que vendria siendo a ser el area del rectangulo, siendo esta: "

def multiplicarNumeros(Valor1, Valor2):
    return Valor1 * Valor2

Resultado = multiplicarNumeros(Ancho, Largo)

print(Explicacion, Resultado)