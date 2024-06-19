"""
Se crea la lista de los codigos de identificacion de los libros original, y se les asigna el valor correspondiente.
"""
libreria_original = [5,3,1,2,4]

"""
Ahora, si utilizara sort() para mostrar la lista, me la mostraria en orden ascendente, puesto que sort() la 
ordenaria de menor a mayaro. Sin embargo, nosotros la necesitamos en orden descendente, es decir, de mayor a menor,
por lo que a la funcion "sorted" a la que le pediremos que ordene la lista, vamos a pasarle adiconalmente de
la lista de la libreria original, el parametro "revere=true", para que nos devuelva lo ordenado invertido, es decir,
de mayor a menor, y por lo tanto, en orden descendente.
"""
print(sorted(libreria_original, reverse=True))

"""
¿Por que no simplemente actualice la lista original al usar "sort()" en ella?, pues debido a que eso conllevaria
un problema de segurirar, al peligrar el almacenamiento de los datos, en este caso el de los codigos de
indentificacion. ¿Por que? Una serie de razones, que van desde que si accidentalmente cambio algo que no deberia,
al no tener un respaldo original, pierdo los datos o la forma en la que llegaron; hasta que deberia complicarme
al preparar cada entrada de datos de forma apropiada acorde a como decidi organizarla, o re organizarla cada vez
que ingrese datos, mientras que manteniendo las originales simplemente puedo ingresar datos en ellas y dejar la 
organizacion pre establecida unicamente al momento de necesitar la lista organizada.
"""