import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title('Login')
ventana.configure(bg='#1d2d44')

# grid de la ventana
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# Creamos un estilo para los widgets
estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure(ventana, background='#1d2d44', foreground='white', font=('Arial', 12),fieldbackground='black')
estilo.configure('TButton', background='#005f73', foreground='white', font=('Arial', 12), borderwidth=0)
estilo.map('TButton', background=[('active', '#0a9396')])



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

def validar(event):
    # print('Se mando a llamar la funcion validar')
    usuario = usuario_caja_texto.get()
    password = password_caja_texto.get()
    if usuario == 'admin' and password == '1234':
        showinfo(title='Login exitoso', message='Bienvenido al sistema')
    else:
        showerror(title='Login fallido', message='Usuario o contraseña incorrectos')

# asociar evento al boton
login_boton.bind('<Return>',validar)#presionar enter para validar
login_boton.bind('<Button-1>',validar)#presionar click para validar

frame.grid(column=0, row=0)
ventana.mainloop()