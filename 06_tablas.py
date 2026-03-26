import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.configure(bg='#1d2d44')
ventana.title('Manejo de Tablas')

# configuramos el grid de la ventana
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=0)

# Defnimos el estilo
estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure('Treeview', background='#black', foreground='white', font=('Arial', 12), fieldbackground='black',rowheight=30)
estilo.map('Treeview', background=[('selected', '#3a86ff')], foreground=[('selected', 'white')])

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
# datos = ((1, 'Juan', 25), (2, 'María', 30), (3, 'Pedro', 35), (4, 'Ana', 28), (5, 'Luis', 32), (6, 'Sofía', 27), (7, 'Carlos', 29), (8, 'Marta', 31), (9, 'Diego', 26), (10, 'Lucía', 33),(1, 'Juan', 25), (2, 'María', 30), (3, 'Pedro', 35), (4, 'Ana', 28), (5, 'Luis', 32), (6, 'Sofía', 27), (7, 'Carlos', 29), (8, 'Marta', 31), (9, 'Diego', 26), (10, 'Lucía', 33),(1, 'Juan', 25), (2, 'María', 30), (3, 'Pedro', 35), (4, 'Ana', 28), (5, 'Luis', 32), (6, 'Sofía', 27), (7, 'Carlos', 29), (8, 'Marta', 31), (9, 'Diego', 26), (10, 'Lucía', 33))

for persona in datos:
    tabla.insert(parent='', index=tk.END, values=persona)

# Agregamos un scrollbar a la tabla
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(column=1, row=0, sticky=tk.NS)

tabla.grid(column=0, row=0, sticky=tk.NSEW)
ventana.mainloop()