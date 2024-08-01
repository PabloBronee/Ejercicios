#Aqui se le pide al usuario que ingrese los respectivos datos del producto
nombre = str(input("Ingrese el nombre del producto: "))
cantidad = str(input("Ingrese la cantidad de unidades a comprar del producto: "))
precio = str(input("Ingrese el precio de cada unidad del producto: "))

'''
Se genera una factura una factura donde se calcula el precio total a pagar,
a partir del precio por unidad, teniendo en cuenta cuantas unidades se compraron.
Para lograrlo, teniendo en cuenta que los datos se ingresaron como strings, se ha de convertir el valor y el precio
a int, al momento de realizar el calculo del precio total.
'''

print(f"Producto: {nombre}" +
      f"\nUnidades compradas: {cantidad}" +
      f"\nPrecio por unidad: {precio}" +
      f"\nPrecio total a pagar: {int(precio) * int(cantidad)}")
