def controlExcepciones():
    try:
         # Solicitamos al usuario el dividendo y lo convertimos a entero
         a = int(input("Ingrese el dividendo: "))
         # Solicitamos al usuario el divisor y lo convertimos a entero
         b = int(input("Ingrese el divisor: "))

         # Intentamos realizar la división
         resultado = a/b
         print(resultado)
    except ZeroDivisionError:  # Si ocurre una división por cero
     print("Error: División por cero no permitida.")

    except ValueError: # Captura si los valores no son números enteros
     print("Error: Debes introducir valores numericos enteros.")
         
controlExcepciones()
            

    






