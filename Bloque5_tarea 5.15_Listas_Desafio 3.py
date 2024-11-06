elementos_repetidos = [1,1,2,2,3,3]

copia_elementos_repetidos = elementos_repetidos.copy()

for x in elementos_repetidos:
    if elementos_repetidos.count(x) > 1:
        elementos_repetidos.remove(x)

print(f"La lista de elementos, tras haber eliminado los repetidos: {elementos_repetidos}")
print(f"Copia de la lista de elementos, antes de eliminar los repetidos: {copia_elementos_repetidos}")
