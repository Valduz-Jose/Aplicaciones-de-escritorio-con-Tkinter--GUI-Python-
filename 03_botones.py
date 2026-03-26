import tkinter as tk
from tkinter import ttk #es una mejora de tkinter que tiene componentes con un diseño más moderno y atractivo

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Nueva Ventana")
ventana.config(background='#1d2d44')

def saludar(nombre):
    print(f'Saludos desde el boton... {nombre}')

# creamos un boton
boton1 = ttk.Button(ventana, text='Enviar',command=lambda: saludar('Juan'))
# Publicamos el componente
boton1.pack(pady=20)


ventana.mainloop()