def leer_archivo(file_name):
    try:
        # Intentamos abrir el archivo en modo lectura
        archivo = open(file_name, "r", encoding="utf-8")
        
        # Leemos todo el contenido del archivo
        contenido = archivo.read()
        
        # Mostramos el contenido del archivo
        print("Contenido del archivo:")
        print(contenido)
    
    except FileNotFoundError:
        # En caso de que el archivo no exista, mostramos un mensaje de error
        print(f"Error: El archivo '{file_name}' no existe.")
    
    except Exception as e:
        # Capturamos cualquier otro tipo de excepción y mostramos el error
        print(f"Se produjo un error inesperado: {e}")
    
    finally:
        # Aseguramos que el archivo se cierre correctamente
        if 'archivo' in locals():  # Verificamos que el archivo fue abierto
            archivo.close()
            print("\nEl archivo ha sido cerrado correctamente.")

# Llamamos a la función con un archivo de ejemplo
leer_archivo("ejemplo.txt")
