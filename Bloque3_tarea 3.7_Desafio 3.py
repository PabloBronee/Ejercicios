# Se crea una lista vacia para su posterior uso
numeros = []

# Se pide al usuario que ingrese la cantidad de numeros que quiere ingresar
cantidad = int(input("Cuántos números quieres ingresar?: "))

'''
Se crea un bucle for para que el usuario ingrese cada numero a la lista.
Se utiliza "range" para hacer el sistema con for, y evitar crear otra variable,
como se necesitaria en un bucle while. Al momento de mostrar el mensaje de "Ingresa el numero x" este inicia
con un +1, ya que el "rangue" empieza por el 0. De esta forma, empieza por "Ingresa el numero 1".
'''
for num in range(cantidad):
    numero = int(input(f"Ingresa el numero {num + 1}: "))
    numeros.append(numero)

'''
Se crea un bucle para convertir cada numero ingresado a su correspondiente ASCII, a la par que se muestra en
consola. Sin embargo, antes de ello un if se asegura que el dato en cuestion efectivamente fuese un numero,
de lo contrario, te advierte de ello y lo ingora para pasar al siguiente dato ingresado previamente.
'''
for num in numeros:
    if type(num) != int:
        print("El dato {num} no es valido, solo podian ingresarse numeros.")
        continue
    else:
       print (f"El correspondiente ASCII del numero {num} seria: {chr(num)}")