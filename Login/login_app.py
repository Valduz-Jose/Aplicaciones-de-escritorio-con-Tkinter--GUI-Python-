import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title('Login')
ventana.configure(bg='#1d2d44')

# grid de la ventana
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# Agregamos el frame 
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

# Titulo
etiqueta = ttk.Label(frame, text="Login", font=("Arial", 20))
etiqueta.grid(column=0, row=0, columnspan=2)

# USUARIO
usuario_etiqueta = ttk.Label(frame, text='Usuario: ')
usuario_etiqueta.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

usuario_caja_texto = ttk.Entry(frame)
usuario_caja_texto.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# PASSWORD
password_etiqueta = ttk.Label(frame, text='Contraseña: ')
password_etiqueta.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

password_caja_texto = ttk.Entry(frame, show='*')
password_caja_texto.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

# boton
login_boton = ttk.Button(frame, text='Enviar')
login_boton.grid(column=0, row=3, columnspan=2, pady=5, padx=5)

frame.grid(column=0, row=0)
ventana.mainloop()