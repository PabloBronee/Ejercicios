import numpy as np

#Se instancia el array solicitada
A = np.array([[1,2,3],[4,5,6],[7,8,9]])

#Se muestra el resultado pedido, a la par que se realizan los calculos correspondientes
print(f"El resultado de la operacion seria: {np.linalg.matrix_rank(A + A.T)}")

