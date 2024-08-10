import random

ancho = 5
largo = 5
barcos_creados = 3

# Crear el array 2d (aplicando las medidas para que este preparado para tener bordes con coordenadas)
C = [["o" for _ in range(ancho + 1)] for _ in range(largo + 1)]

# Crea el array 2d donde se guardaran los barcos creados
D = [["?" for _ in range(ancho + 1)] for _ in range(largo + 1)]

# Llena las cordenadas de los bordes
for i in range(1, ancho + 1):
    C[0][i] = str(i - 1)  # Columnas
for j in range(1, largo + 1):
    C[j][0] = str(j - 1)  # Fila

# Un bucle que genera coordenadas aleatorias para los barcos, a la par que los coloca
for _ in range(barcos_creados):
    columna_aleatoria = random.randint(1,5)
    fila_aleatoria = random.randint(1,5)
    D[fila_aleatoria][columna_aleatoria] = str(("1"))

#Variable instanciada para en el bucle siguiente saber cuando termina el juego
termina_juego = False

#Contador de barcos restantes
barcos_restantes = barcos_creados

while termina_juego == False:
    # Muestra el tablero en cada vuelta del bucle, para que se actualice con los cambios
    for x in C:
        print(" ".join(x))

    # Pregunta las coordenadas, para poder buscarlo en la matriz donde se guardan la ubicacion de los barcos
    columna = int(input("Ingresa la columna: "))
    fila = int(input("Ingresa la fila: "))

    #Variable instanciada en falso para resetearse a False cada vuelta del bucle 
    encontrado = False

    '''
    Busca con las coordenadas ingresadas el espacio del array2d correspondienite donde se guardan los datos de los barcos.
    Aunque agregandole +1 para ir acorde a las coordenadas mostradas (falsas). Tambien se actualiza el encontrado a true.
    De paso se marca que se destruyo un barco en el array visual con un "X"
    '''
    # Aunque agregandole +1 para ir acorde a las coordenadas mostradas (falsas)
    if D[fila + 1][columna + 1] == ("1"):
        print(f"Se encontro y destruyo un barco en ({columna}, {fila})!") 
        barcos_restantes -= 1
        C[columna + 1][fila + 1] = "X"
        encontrado = True

    #Si no se encontro un barco en las coordenadas, entonces te lo avisa, y adicionalmente altera el array 2d visible con un "-" para que quede claro
    if not encontrado:
        print(f"No se encontro ningun barco en ({columna}, {fila})")
        C[columna + 1][fila + 1] = "-"

    #Comprueba si quedan barcos restantes. Si no es el caso, convierte "termina juego" en true, dejando que termine el bucle while de juego
    if barcos_restantes == 0:
        termina_juego = True


#Mensaje para informar que ganaste
print("Ganaste")
