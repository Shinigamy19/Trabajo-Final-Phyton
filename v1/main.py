import pickle, sys, os, random

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear") # Uso linux Gaby

def generar_numero_ticket():
    return random.randrange(1000, 9999)

def alta_ticket():
    while True:
        limpiar_pantalla()
        print("--- Alta de Ticket ---")
        nombre = input("Nombre: ")
        sector = input("Sector: ")
        asunto = input("Asunto: ")
        problema = input("Problema: ")

        numero_ticket = generar_numero_ticket()
        archivo = f"{numero_ticket}.ticket"

        ticket = {
            "Nombre": nombre,
            "Sector": sector,
            "Asunto": asunto,
            "Problema": problema
        }

        with open(archivo, "wb") as f:
            pickle.dump(ticket, f)

        print("\n--- Ticket Generado ---")
        print(f"Número de Ticket: {numero_ticket}")
        print(f"Nombre: {nombre}")
        print(f"Sector: {sector}")
        print(f"Asunto: {asunto}")
        print(f"Problema: {problema}")
        print("¡Por favor, recuerde su número de ticket!\n")

        seguir = input("¿Desea crear otro ticket? (s/n): ").lower()
        if seguir != 's':
            break

def leer_ticket():
    while True:
        limpiar_pantalla()
        print("--- Leer Ticket ---")
        numero = input("Ingrese el número de ticket: ")
        archivo = f"{numero}.ticket"

        if os.path.isfile(archivo):
            with open(archivo, "rb") as f:
                ticket = pickle.load(f)
            print(f"\n--- Ticket #{numero} ---")
            for clave, valor in ticket.items():
                print(f"{clave}: {valor}")
        else:
            print("El ticket no existe o el número es incorrecto.")

        seguir = input("\n¿Desea leer otro ticket? (s/n): ").lower()
        if seguir != 's':
            break

def salir():
    confirmacion = input("¿Está seguro que desea salir? (s/n): ").lower()
    if confirmacion == 's':
        print("Saliendo del sistema. ¡Hasta luego!")
        sys.exit()

def menu():
    while True:
        limpiar_pantalla()
        print("=== SISTEMA DE TICKETS ===")
        print("1. Alta Ticket")
        print("2. Leer Ticket")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            alta_ticket()
        elif opcion == '2':
            leer_ticket()
        elif opcion == '3':
            salir()
        else:
            print("Opción inválida. Presione Enter para continuar.")
            input()

if __name__ == "__main__":
    menu()
