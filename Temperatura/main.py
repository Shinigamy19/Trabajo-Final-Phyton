from tkinter import messagebox, Label, Tk, StringVar, CENTER, Entry, ttk

def convertir():
    temp_str = entrada_temp.get().replace(",", ".")

    try:
        temp = float(temp_str)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico válido (puede incluir decimales).")
        return

    origen = combo_origen.current()
    destino = combo_destino.current()

    if origen == destino:
        resultado_var.set(f"{temp:.2f} (sin conversión)")
        return

    if origen == 0:  # Celsius
        celsius = temp
    elif origen == 1:  # Fahrenheit
        celsius = (temp - 32) * 5/9
    elif origen == 2:  # Kelvin
        celsius = temp - 273.15

    if destino == 0:
        resultado = celsius
        unidad = "°C"
    elif destino == 1:
        resultado = (celsius * 9/5) + 32
        unidad = "°F"
    elif destino == 2:
        resultado = celsius + 273.15
        unidad = "K"

    resultado_var.set(f"{resultado:.2f} {unidad}")


ventana = Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("340x260")
ventana.resizable(False, False)

Label(ventana, text="Ingrese la temperatura:", font=("Arial", 12)).pack(pady=5)

entrada_temp = Entry(ventana, justify=CENTER, font=("Arial", 12))
entrada_temp.pack(pady=5)

Label(ventana, text="Convertir de:", font=("Arial", 10)).pack()
combo_origen = ttk.Combobox(ventana, state="readonly", justify=CENTER, font=("Arial", 10))
combo_origen["values"] = ("Celsius", "Fahrenheit", "Kelvin")
combo_origen.current(0)
combo_origen.pack(pady=5)

Label(ventana, text="A:", font=("Arial", 10)).pack()
combo_destino = ttk.Combobox(ventana, state="readonly", justify=CENTER, font=("Arial", 10))
combo_destino["values"] = ("Celsius", "Fahrenheit", "Kelvin")
combo_destino.current(1)
combo_destino.pack(pady=5)

ttk.Button(ventana, text="Convertir", command=convertir).pack(pady=10)

resultado_var = StringVar()
Label(ventana, textvariable=resultado_var, font=("Arial", 14), fg="blue").pack(pady=10)

ventana.mainloop()
