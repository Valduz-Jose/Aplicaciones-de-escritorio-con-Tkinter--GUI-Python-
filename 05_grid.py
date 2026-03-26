import tkinter as tk
from tkinter import ttk #es una mejora de tkinter que tiene componentes con un diseño más moderno y atractivo

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Nueva Ventana")
ventana.config(background='#1d2d44')

# Manejo de grid
boton1 = ttk.Button(ventana, text='Boton 1')
boton2 = ttk.Button(ventana, text='Boton 2')
boton3 = ttk.Button(ventana, text='Boton 3')

# Configurar el grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)

# Publicados d manera horizontal
boton1.grid(row=0, column=0, sticky=tk.NSEW,padx=20, pady=20)
boton2.grid(row=0, column=1,sticky=tk.SE,ipadx=20,ipady=20)
boton3.grid(row=0, column=2,sticky=tk.NW)

# Publicados de manera vertical
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=0)
# boton3.grid(row=2, column=0)

# Publicados en diagonal
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=1)
# boton3.grid(row=2, column=2)


ventana.mainloop()