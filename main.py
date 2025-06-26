import pickle, sys, os, random

TICKETS_FILE = "tickets.pkl"

def cargar_tickets():
    if os.path.isfile(TICKETS_FILE):
        with open(TICKETS_FILE, "rb") as f:
            return pickle.load(f)
    return {}

def guardar_tickets(tickets):
    with open(TICKETS_FILE, "wb") as f:
        pickle.dump(tickets, f)

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def generar_numero_ticket(tickets):
    numero = random.randrange(1000, 9999)
    while numero in tickets:
        numero = random.randrange(1000, 9999)
    return numero

def alta_ticket(tickets):
    while True:
        limpiar_pantalla()
        print("--- Alta de Ticket ---")
        nombre = input("Nombre: ")
        sector = input("Sector: ")
        asunto = input("Asunto: ")
        problema = input("Problema: ")

        numero_ticket = generar_numero_ticket(tickets)

        ticket = {
            "Nombre": nombre,
            "Sector": sector,
            "Asunto": asunto,
            "Problema": problema
        }

        tickets[numero_ticket] = ticket
        guardar_tickets(tickets)

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

def leer_ticket(tickets):
    while True:
        limpiar_pantalla()
        if not tickets:
            print("No hay tickets registrados aún.")
            input("Presione Enter para volver al menú...")
            break

        print("--- Lista de Tickets ---")
        lista_tickets = list(tickets.items())
        for i, (num, datos) in enumerate(lista_tickets, start=1):
            print(f"{i}. Ticket #{num} - {datos['Asunto']} ({datos['Nombre']})")

        print(f"{len(lista_tickets)+1}. Volver al menú")

        try:
            opcion = int(input("\nSeleccione un ticket por número: "))
            if opcion == len(lista_tickets)+1:
                break
            elif 1 <= opcion <= len(lista_tickets):
                numero = lista_tickets[opcion-1][0]
                ticket = tickets[numero]
                limpiar_pantalla()
                print(f"--- Ticket #{numero} ---")
                for clave, valor in ticket.items():
                    print(f"{clave}: {valor}")
                input("\nPresione Enter para volver a la lista...")
            else:
                print("Opción inválida.")
                input("Presione Enter para continuar...")
        except ValueError:
            print("Debe ingresar un número válido.")
            input("Presione Enter para continuar...")

def salir():
    confirmacion = input("¿Está seguro que desea salir? (s/n): ").lower()
    if confirmacion == 's':
        print("Saliendo del sistema. ¡Hasta luego!")
        sys.exit()

def menu():
    tickets = cargar_tickets()

    while True:
        limpiar_pantalla()
        print("=== SISTEMA DE TICKETS ===")
        print("1. Alta Ticket")
        print("2. Leer Ticket")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            alta_ticket(tickets)
        elif opcion == '2':
            leer_ticket(tickets)
        elif opcion == '3':
            salir()
        else:
            print("Opción inválida. Presione Enter para continuar.")
            input()

if __name__ == "__main__":
    menu()
