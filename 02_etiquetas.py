import tkinter as tk
from tkinter import ttk #es una mejora de tkinter que tiene componentes con un diseño más moderno y atractivo

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Nueva Ventana")
ventana.config(background='#1d2d44')

# creamos una etiqueta (label)
etiqueta = ttk.Label(ventana, text='Saludos')

# Publicamos el componente
etiqueta.pack(pady=20)

# Cambiar el texto usando Configure
etiqueta.configure(text='Nos Vemos...')

# Cambiar el texto con ayuda de la llave text
etiqueta['text'] = 'Adios...'

ventana.mainloop()