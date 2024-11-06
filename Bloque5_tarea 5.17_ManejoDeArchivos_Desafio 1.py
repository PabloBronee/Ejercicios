# Incializacion del archivo de "prestamos"
with open("prestamos.txt", "w") as archivo:
    archivo.write("Prestamos:\n")

#Creacion del metodo para agendar prestamos, con los requisitos pedidos por el ejercicio
def sacar_prestamo(nombre_libro, prestatario, fecha):
    with open("prestamos.txt", "a") as archivo:
        archivo.write(f"Prestamo del libro: '{nombre_libro}', cedido a '{prestatario}', el dia '{fecha}'\n")
    
#Creacion de metodo para poder leer los prestamos

def ver_prestamo():
    with open("prestamos.txt", "r") as archivo:
        prestamos = archivo.read()
        return prestamos

#Ejemplo de prueba
sacar_prestamo("El color que callo del cielo", "Pablo Bronée", "06/11/24")
print(f"{ver_prestamo()}")

