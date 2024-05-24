suma_calificaciones = 0
contador_asignaturas = 0

calificaciones = input('Ingresa todas tus calificaciones separadas por coma, manteniendote en el margen del 1 al 12:' )
calificaciones_a_evaluar = calificaciones.split(",")
for calificacion in calificaciones_a_evaluar:
    calificacion_evaluandose = int(calificacion)
    if calificacion_evaluandose < 1 or calificacion_evaluandose > 12:
        print(f"La calificación {calificacion_evaluandose} no se tomo por válida, debe estar entre 1 y 12")
        continue

    suma_calificaciones += calificacion_evaluandose
    contador_asignaturas += 1

promedio = suma_calificaciones / contador_asignaturas
print(f"El promedio de las calificaciones es: {promedio}")

