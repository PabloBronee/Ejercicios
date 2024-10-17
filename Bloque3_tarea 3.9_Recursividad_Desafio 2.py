
"""
Para facilitar la revision y prueba del codigo para el profesor,
se crea el modulo solicitado "resaltar palabra" dentro de el mismo ejercicio
"""
def resaltar_palabra(palabra_elegida, texto):
    """
    Resalta todas las apariciones de "palabra elegida" en "texto" envolviéndolas en asteriscos. Luego, la reemplaza
    por la nueva, ahora rodeada de asteriscos.
    Reemplaza la palabra elegida por la palabra rodeada de asteriscos
    """
    return texto.replace(palabra_elegida, f'**{palabra_elegida}**')

#Aca empieza el ejercicio solicitado
def resaltar_ocurrencias(palabra_elegida, texto):
    # Caso base: Si la palabra elegida no está en el texto, devolvemos el texto tal cual
    if palabra_elegida not in texto:
        return texto
    # Si encontramos la palabra elegida, resaltamos la primera ocurrencia
    texto_resaltado = resaltar_palabra(palabra_elegida, texto)
    # Se encuentra y guarda la posición de la palabra clave
    index = texto_resaltado.find(palabra_elegida)
    # Dividimos el texto en dos partes: antes y después de la primera ocurrencia resaltada
    antes = texto_resaltado[:index + len(palabra_elegida)]
    despues = texto_resaltado[index + len(palabra_elegida):]
    
    # Llamamos recursivamente a la función en la parte del texto que sigue después de la ocurrencia resaltada
    despues_de_resaltado = resaltar_ocurrencias(palabra_elegida, despues)
    
    # Unimos las partes resaltadas del texto
    return antes + despues_de_resaltado

#Se crea y guarda un texto para probar la funcion creada, luego se imprimen los resultados
texto_prueba = "Hoy es un dia bastante soleado, aunque no tan soleado como ayer"
print(resaltar_ocurrencias("soleado", texto_prueba))