lista1 = [1,2,3,4,5]

lista2 = [1,2,3]

suma_total = 0

if len(lista1) > len(lista2):
    for x in range(len(lista2)):
        suma_total += lista1[x] + lista2[x]
elif len(lista2) > len(lista1):
    for x in range(len(lista1)):
        suma_total += lista1[x] + lista2[x]
else:
    for x in range(len(lista1)):
        suma_total += lista1[x] + lista2[x]

print(f"La suma de los elementos correspondientes en ambas listas, considerando los que no tienen pareja como 0, es: {suma_total}")