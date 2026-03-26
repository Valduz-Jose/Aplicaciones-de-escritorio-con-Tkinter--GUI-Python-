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
etiqueta.grid(column=0, row=0)


frame.grid(column=0, row=0)
ventana.mainloop()