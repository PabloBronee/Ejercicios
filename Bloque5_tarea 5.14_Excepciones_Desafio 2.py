def calculo_con_excepciones(lista):
    try:
        # Suma todos los valores
        suma = sum(lista)
        print(f"La suma de todos los valores es: {suma}")

        # Divide el primer valor entre el ultimo
        division = lista[0] / lista[-1]
        print(f"La división del primer valor entre el ultimo es: {division}")
    #Las excepciones solicitadas
    except ZeroDivisionError:  # Captura si se intenta dividir por cero
        print("Error: División por cero no permitida.")
    except TypeError:  # Captura si algun valor en la lista no es numérico
        print("Error: Todos los elementos en la lista deben ser numéricos.")
    except ValueError:  # Captura si hay un valor invalido
        print("Error: Valor invalido en la lista.")
        
# Ejemplo de uso
lista = [10, 5, 3, 0]  
calculo_con_excepciones(lista)



