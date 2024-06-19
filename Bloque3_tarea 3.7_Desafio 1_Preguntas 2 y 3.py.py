#Se crea el inventario a la par que se asignan los productos
inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brocoli", "cebolla", "kiwis"]

"""
Respuesta a la pregunta 2: Muestro el articulo en la posicion 3 al indicar el numero de su indice entre []. 
Sin embargo, la posicion especificada dentro de estas es la "2", puesto que las listas comienazn en el indice "0".
por lo que "la posicion 2" vendria a ocupar el tercer espacio indexado en realidad, en este caso "zanahorias".
"""
print(inventario[2])

"""
Respuesta a la pregunta 3: Si un cliente compra todas las bananas, habria que eliminar el articulo llamado "bananas"
dentro del inventario, utilizando remove(), de esta forma no importa la posicion en que se encuentre indexado 
el articulo bananas, solamente su nombre, simplificando el proceso.
"""
inventario.remove("bananas")

# Se muestra el inventario actualizado tras la venta, es decir, tras haber removido "bananas".
print(inventario)


