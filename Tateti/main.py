from random import randrange

def mostrar_tablero(tablero):
    print()
    for i, fila in enumerate(tablero):
        print(" | ".join(fila))
        if i < 2:
            print("-" * 9)
    print()

def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def verificar_ganador(tablero, jugador):
    # Verifica filas, columnas y diagonales
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or \
           all(tablero[j][i] == jugador for j in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)) or \
       all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False

def tablero_lleno(tablero):
    return all(celda != " " for fila in tablero for celda in fila)

def turno_jugador(tablero, jugador):
    while True:
        try:
            fila = int(input(f"Jugador {jugador}, ingresa la fila (0-2): "))
            columna = int(input(f"Jugador {jugador}, ingresa la columna (0-2): "))
            if 0 <= fila <= 2 and 0 <= columna <= 2:
                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugador
                    break
                else:
                    print("Esa casilla ya está ocupada.")
            else:
                print("Fila y columna deben estar entre 0 y 2.")
        except ValueError:
            print("Entrada inválida. Usa números.")

def turno_maquina(tablero):
    print("Turno de la máquina (O):")
    while True:
        fila = randrange(3)
        columna = randrange(3)
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "O"
            break

def jugar_jugador_vs_jugador():
    tablero = crear_tablero()
    turno = "X"

    while True:
        mostrar_tablero(tablero)
        turno_jugador(tablero, turno)

        if verificar_ganador(tablero, turno):
            mostrar_tablero(tablero)
            print(f"¡El jugador {turno} ha ganado!")
            break
        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("¡Empate!")
            break
        turno = "O" if turno == "X" else "X"

def jugar_jugador_vs_maquina():
    tablero = crear_tablero()
    turno = "X"

    while True:
        mostrar_tablero(tablero)
        if turno == "X":
            turno_jugador(tablero, "X")
        else:
            turno_maquina(tablero)

        if verificar_ganador(tablero, turno):
            mostrar_tablero(tablero)
            if turno == "X":
                print("¡Ganaste!")
            else:
                print("¡La máquina ganó!")
            break
        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("¡Empate!")
            break
        turno = "O" if turno == "X" else "X"

def menu():
    while True:
        print("\n--- TATETI ---")
        print("1. Jugador vs Jugador")
        print("2. Jugador vs Máquina")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            jugar_jugador_vs_jugador()
        elif opcion == "2":
            jugar_jugador_vs_maquina()
        elif opcion == "3":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()