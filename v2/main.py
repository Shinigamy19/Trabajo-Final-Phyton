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
        print("--- Leer Ticket ---")
        numero = input("Ingrese el número de ticket: ")

        if not numero.isdigit():
            print("Debe ingresar un número válido.")
            input("Presione Enter para continuar...")
            continue

        numero = int(numero)
        if numero in tickets:
            ticket = tickets[numero]
            print(f"\n--- Ticket #{numero} ---")
            for clave, valor in ticket.items():
                print(f"{clave}: {valor}")
        else:
            print("Ticket no encontrado.")

        seguir = input("\n¿Desea leer otro ticket? (s/n): ").lower()
        if seguir != 's':
            break

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
