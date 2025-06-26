import secrets, string, sys

diccionario = {
    'letras': string.ascii_letters,
    'numeros': string.digits,
    'caracteres': string.punctuation
}

def generar_contraseña(longitud, usar_letras, usar_numeros, usar_caracteres):
    seleccion = ''

    if usar_letras:
        seleccion += diccionario['letras']
    if usar_numeros:
        seleccion += diccionario['numeros']
    if usar_caracteres:
        seleccion += diccionario['caracteres']

    if not seleccion:
        print("Error: Debes seleccionar al menos un tipo de caracteres.")
        sys.exit(1)

    password = ''.join(secrets.choice(seleccion) for _ in range(longitud))
    return password

def pedir_opcion(texto):
    respuesta = input(texto + " (s/n): ").strip().lower()
    return respuesta == 's'

def main():
    print("=== Generador de Contraseñas ===")
    
    try:
        longitud = int(input("¿Cuántos caracteres debe tener la contraseña?: "))
    except ValueError:
        print("Error: Debes ingresar un número entero.")
        sys.exit(1)

    usar_letras = pedir_opcion("¿Incluir letras?")
    usar_numeros = pedir_opcion("¿Incluir números?")
    usar_caracteres = pedir_opcion("¿Incluir caracteres especiales?")

    contraseña = generar_contraseña(longitud, usar_letras, usar_numeros, usar_caracteres)
    print("\nContraseña generada:", contraseña)

if __name__ == "__main__":
    main()
