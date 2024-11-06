codigos_productos = ["01", "02", "03", "04", "05"]

codigo_buscado = input("Ingresa el codigo buscado: ")

if codigo_buscado in codigos_productos:
    print(f"El producto con el codigo ingresado se encuentra en la posicion {codigos_productos.index(codigo_buscado)}")
else:
    print("El codigo ingresado no se pertenece a ningun producto")