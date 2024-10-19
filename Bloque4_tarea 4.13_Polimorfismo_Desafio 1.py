#Se crea la clase musico
class Musico:
    def instrumento (self):
        print(f"el musico toca un instrumento")

#Se crea la subclase guitarrista, que hereda de musico y cambia el metodo instrumento
class Guitarrista(Musico):
    def instrumento (self):
        print(f"El guitarrista toca la guitarra")

#Se crea la subclase baterista, que hereda de musico y cambia el metodo instrumento
class Baterista(Musico):
    def instrumento (self):
        print(f"El baterista toca la bateria")

#Se instancia un objeto de cada clase
musico1 = Musico()
guitarrista1 = Guitarrista()
baterista1 = Baterista()

#se guardan los objetos en una lista y se usa para mostrar el polimorfismo con un bucle for
musicos = [musico1, guitarrista1, baterista1]
for musico in musicos:
    musico.instrumento()

