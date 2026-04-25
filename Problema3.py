def charlas(lista):
    lista.sort(key=lambda x: x[1])

    resultado = []
    fin = 0

    for inicio, termino in lista:
        if inicio >= fin:
            resultado.append((inicio, termino))
            fin = termino
    return resultado

n = int(input("¿Cuántas charlas vas a ingresar? "))
datos = []

for i in range(n):
    while True:
        inicio = int(input("Inicio: "))
        fin = int(input("Fin: "))
        if inicio < fin:
            datos.append((inicio, fin))
            break
        else:
            print("Error: El inicio debe ser menor que el fin. Intenta de nuevo.")

print("Charlas seleccionadas:", charlas(datos))