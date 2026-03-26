import tkinter as tk
from tkinter import ttk #es una mejora de tkinter que tiene componentes con un diseño más moderno y atractivo

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Nueva Ventana")
ventana.config(background='#1d2d44')

def mostrar():
    texto = caja_texto.get()#recupera el valor de la caja de texto
    print(f'El texto ingresado es: {texto}')
    etiqueta['text']=texto

# caja de texto
caja_texto = ttk.Entry(ventana,font=('Arial', 14))
caja_texto.pack(pady=20)

boton1 = ttk.Button(ventana, text='Enviar',command=mostrar)
boton1.pack(pady=20)

# etiqueta
etiqueta = ttk.Label(ventana, text='Valor Inicial', font=('Arial', 14))
etiqueta.pack(pady=20)


ventana.mainloop()