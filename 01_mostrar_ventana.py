# Importo la biblioteca tkinter para crear la interfaz gráfica de usuario (GUI)
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# redimensionar la ventana
ventana.geometry("600x400")

# Modificar el titulo
ventana.title("Nueva Ventana")

# Evitar redimiensionar la ventana
ventana.resizable(0, 0)

# Color de la ventana
ventana.config(background='#1d2d44')

# Hacer visible la ventana
ventana.mainloop()