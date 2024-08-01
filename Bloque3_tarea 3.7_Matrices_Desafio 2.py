import numpy as np

#Se instancia el array solicitada
A = np.array([[1,0,1],[4,-1,4],[5,6,7]])

#Se muestra el resultado pedido, a la par que se realizan los calculos correspondientes
print(f"El resultado de la operacion seria: {np.trace(np.linalg.inv(A))}")
