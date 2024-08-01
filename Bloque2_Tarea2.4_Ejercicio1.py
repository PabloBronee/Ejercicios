#Primero se establecen los tres numeros diferentes a compararse
a = 5
b = 10
c = 15

'''
La estrategia adoptada para realizar el desafio constara de comparar individualmente cada variable, primero con una
y luego con la otra, en pos de descubrir si es la menor de las tres. Una vez realizado esto, se comprobara la menor
de las otras dos variables. Finalmente se imprimiran en consola los numeros ordenados en orden ascendente.

Sin embargo, si resulta que la variable comparada inicialmente con las otras dos no es la menor de las tres, 
entonces el codigo saltara al siguiente "elif" donde se intentara denuevo con la siguiente. Finalmente, si tampoco
resulta ser el segundo intento, el else repetira el proceso con la ultima variable, ya que por default sera la menor.
'''
if a < b and a < c:
    if b < c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b < a and b < c:
    if a < c:
        print(b, a, c)
    else:
        print(b, c, a)
else: 
    if a < b:
        print(c, a, b)
    else:
        print(c, b, a)

'''
La efectividad del codigo puede comprobarse alternando el valor de las tres variables, aunque solo funcionara
mientras se mantenga la regla de que estas sean numeros distintos. 
'''