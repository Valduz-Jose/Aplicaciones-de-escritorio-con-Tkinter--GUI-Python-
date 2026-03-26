import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.configure(bg='#1d2d44')
ventana.title('Manejo de Tablas')

columnas = ('Id', 'Nombre', 'Edad')
tabla = ttk.Treeview(ventana, columns=columnas,show='headings')#show es para ocultar la primera columna que es la de los iconos


# Cabeceros de la tabla
tabla.heading('Id', text='Id')
tabla.heading('Nombre', text='Nombre')
tabla.heading('Edad', text='Edad')

# formato columnas
tabla.column('Id', width=80, anchor=tk.CENTER)
tabla.column('Nombre', width=120, anchor=tk.CENTER)
tabla.column('Edad', width=80, anchor=tk.CENTER)

# Cargar datos a la tabla
datos = ((1, 'Juan', 25), (2, 'María', 30), (3, 'Pedro', 35))

for persona in datos:
    tabla.insert(parent='', index=tk.END, values=persona)



tabla.grid(column=0, row=0, sticky=tk.NSEW)
ventana.mainloop()