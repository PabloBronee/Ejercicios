estudiantes_evaluados = int(input("Cuantos estudiantes vas a evaluar?: "))
estudiantes_aprobados = 0
estudiantes_reprobados = 0
calificacion_evaluandose = 0

while calificacion_evaluandose != estudiantes_evaluados:
    calificacion_evaluandose += 1 
    calificacion = int(input(f"Ingresa la calificación número {calificacion_evaluandose}: "))
    if calificacion > 12 or calificacion < 0:
        print("La calificacion no puede ser más de 12 ni menos de 0, inténtalo denuevo")
        calificacion_evaluandose -= 1
    elif calificacion >= 7:
        estudiantes_aprobados += 1
    else:
        estudiantes_reprobados += 1
  
print(f"Este año aprobaron {estudiantes_aprobados} estudiantes, y reprobaron {estudiantes_reprobados}")
