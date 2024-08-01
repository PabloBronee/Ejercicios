import numpy as np

#Se instancias las dos arrays solicitadas
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

#Se muestra el resultado pedido, a la par que se realizan los calculos correspondientes
print(f"El resultado de la operacion seria: {2*A + B.T}")
