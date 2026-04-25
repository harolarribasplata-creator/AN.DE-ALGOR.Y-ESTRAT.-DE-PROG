import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setsGanados = 0

    def mostrar(self):
        return f"Equipo: {self.nombre} | Partidos Ganados: {self.partidosGanados} | Partidos Perdidos: {self.partidosPerdidos}"


equipo1 = Equipo("Los Tigres")
equipo2 = Equipo("Los Leones")


def RegistraSet(ganador):
    if ganador == 1:
        equipo1.setsGanados += 1
        if equipo1.setsGanados == 3:
            equipo1.partidosGanados += 1
            equipo2.partidosPerdidos += 1
            equipo1.setsGanados = 0
            equipo2.setsGanados = 0
            print(f"  >> {equipo1.nombre} gana el partido!")
    elif ganador == 2:
        equipo2.setsGanados += 1
        if equipo2.setsGanados == 3:
            equipo2.partidosGanados += 1
            equipo1.partidosPerdidos += 1
            equipo1.setsGanados = 0
            equipo2.setsGanados = 0
            print(f"  >> {equipo2.nombre} gana el partido!")


def Puntos():
    return random.randint(10, 28)


def PuntosExtras():
    return random.randint(0, 6)


def JugarPartido():
    sets1 = 0
    sets2 = 0
    numSet = 1
    while sets1 < 3 and sets2 < 3:
        print(f"\n  --- Set {numSet} ---")
        p1 = Puntos()
        p2 = Puntos()
        print(f"  {equipo1.nombre}: {p1} pts  |  {equipo2.nombre}: {p2} pts")

        if p1 >= 25 and p1 > p2:
            print(f"  {equipo1.nombre} gana el set")
            sets1 += 1
            RegistraSet(1)
        elif p2 >= 25 and p2 > p1:
            print(f"  {equipo2.nombre} gana el set")
            sets2 += 1
            RegistraSet(2)
        else:
            print("  Ninguno supera 25, se juegan puntos extras")
            while True:
                p1 += PuntosExtras()
                p2 += PuntosExtras()
                print(f"  {equipo1.nombre}: {p1} pts  |  {equipo2.nombre}: {p2} pts")
                if p1 > 25 and p1 > p2:
                    print(f"  {equipo1.nombre} gana el set")
                    sets1 += 1
                    RegistraSet(1)
                    break
                elif p2 > 25 and p2 > p1:
                    print(f"  {equipo2.nombre} gana el set")
                    sets2 += 1
                    RegistraSet(2)
                    break
                else:
                    print("  Aún no hay ganador, más puntos extras...")

        print(f"  Sets: {equipo1.nombre} {sets1} - {sets2} {equipo2.nombre}")
        numSet += 1


def ResultadoTorneo():
    print("\n========== RESULTADO DEL TORNEO ==========")
    print(equipo1.mostrar())
    print(equipo2.mostrar())
    print("==========================================")


print("=== SIMULADOR DE VOLEY ===")
print(f"Equipos: {equipo1.nombre} vs {equipo2.nombre}")

while True:
    print("\n--- MENÚ ---")
    print("1. Configurar nombres de equipos")
    print("2. Jugar partidos")
    print("3. Ver resultados del torneo")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        equipo1.nombre = input("Ingrese nombre del equipo 1: ")
        equipo2.nombre = input("Ingrese nombre del equipo 2: ")
        print(f"Equipos configurados: {equipo1.nombre} vs {equipo2.nombre}")

    elif opcion == "2":
        cantidad = int(input("¿Cuántos partidos desea jugar? "))
        for i in range(cantidad):
            print(f"\n{'='*40}")
            print(f"  PARTIDO {i + 1}: {equipo1.nombre} vs {equipo2.nombre}")
            print(f"{'='*40}")
            JugarPartido()

    elif opcion == "3":
        ResultadoTorneo()

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida.")