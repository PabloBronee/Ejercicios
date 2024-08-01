import random
# Para poder cumplir con el desafio, antes de nada tuve que importar la libreria "random"

'''
Se crean tres variables, en representacion de los tres autos para la carrera, a la par que se asigna
su velocidad entre 1 y 10. Aclarar que decido usar "randint" para esto en pos de tener numeros int, y que 
el proceso se vea mas limpio
'''

auto_rojo_velocidad = random.randint(1, 10)
auto_azul_velocidad = random.randint(1, 10)
auto_verde_velocidad = random.randint(1, 10)


'''
Para iniciar, se crea la variable "segundos" y se la asigna en 0, pues la necesito ya instanciada para
el proceso de la carrera. Posterior a ello se instancian las variables de "avance" para cada auto, por la misma
razon de requerirlas pre echas para la carrera.
'''
segundos = 0
auto_rojo_avance = 0
auto_azul_avance = 0
auto_verde_avance = 0

'''
Se crea un while que se repetira hasta que se cumpal 10 segundos, es decir, hasta que se allan dado 10 vueltas,
mientras tanto los autos incrementaran su avance en funcion de su velocidad
'''
while segundos != 10:
    segundos += 1
    auto_rojo_avance += auto_rojo_velocidad
    auto_azul_avance += auto_azul_velocidad
    auto_verde_avance += auto_verde_velocidad

'''
Una vez acabada la carrera se utiliza la funcion "max" para obtener el mayor avance logrado, en pos de utilizarlo
para el calculo siguiente, en torno a determinar el ganador, o los posibles empates
'''
ganador = max(auto_rojo_avance, auto_azul_avance, auto_verde_avance)

'''
Para el sistema partimos de detectar al ganador a partir de la variable "ganador", siempre teniendo en cuenta
que en caso de un empate, el resultado se repetiria entre dos o tres autos, por lo que podemos evitar bastantes
comprobaciones usandolo a nuestro favor. Dicho esto, simplemente se comprueba el ganador, o los empates, y se
imprime en consola.
'''
if auto_rojo_avance == ganador:
    if auto_rojo_avance == auto_azul_avance == auto_verde_avance:
        print("El resultado fue un empate triple")
    elif auto_rojo_avance == auto_azul_avance:
        print("El resultado fue un empate entre el auto rojo y el auto azul")
    elif auto_rojo_avance == auto_verde_avance:
        print("El resultado fue un empate entre el auto rojo y el auto verde")
    else:
        print("Gano el auto rojo")
elif auto_azul_avance == ganador:
    if auto_azul_avance == auto_verde_avance:
        print("El resultado fue un empate entre el auto azul y el auto verde")
    else:
        print("Gano el auto azul")
else:
    print("Gano el auto verde")