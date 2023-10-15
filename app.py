#Interfaz gráfica

import tkinter as tk


def cambiar_color():
    color_texto = entry.get().lower() # Obtener el texto del Entry y convertir a minúsculas para evitar sobreuso de condicionales
    if color_texto == "rojo":
        boton["fg"] = "red"
    elif color_texto == "amarillo":
        boton["fg"] = "yellow"
    else:
        pass # No hacer nada

# Ventana, entry y label
ventana = tk.Tk()
ventana.geometry("700x400")
ventana.title("Matrícula del alumno: 337213")


entry = tk.Entry(ventana)
entry.pack()

boton = tk.Button(ventana, text="Aceptar")
boton.pack()

etiqueta = tk.Label(ventana, text="¿Rojo o amarillo?")
etiqueta.pack()


boton.config(command=cambiar_color)







ventana.mainloop()