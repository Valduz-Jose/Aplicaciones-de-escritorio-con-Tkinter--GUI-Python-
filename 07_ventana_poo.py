import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        # configurar el grid
        self.configurar_grid()
        self.mostrar_tabla()

    def configurar_ventana(self):
        self.geometry("600x400")
        self.configure(bg="#1d2d44")
        self.title("Manejeo de Ventanas con POO")
        
    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)

    def mostrar_tabla(self):
        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure('Treeview', background='#black', foreground='white', font=('Arial', 12), fieldbackground='black',rowheight=30)
        estilo.map('Treeview', background=[('selected', '#3a86ff')], foreground=[('selected', 'white')])
        columnas = ('Id', 'Nombre', 'Edad')
        self.tabla = ttk.Treeview(self, columns=columnas,show='headings')
        self.tabla.heading('Id', text='Id')
        self.tabla.heading('Nombre', text='Nombre')
        self.tabla.heading('Edad', text='Edad')
        self.tabla.column('Id', width=80, anchor=tk.CENTER)
        self.tabla.column('Nombre', width=120, anchor=tk.CENTER)
        self.tabla.column('Edad', width=80, anchor=tk.CENTER)
        datos = ((1, 'Juan', 25), (2, 'María', 30), (3, 'Pedro', 35))
        for persona in datos:
            self.tabla.insert(parent='', index=tk.END, values=persona)

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(column=1, row=0, sticky=tk.NS)
        self.tabla.bind('<<TreeviewSelect>>', self.mostrar_registro_seleccionado)
        self.tabla.grid(column=0, row=0, sticky=tk.NSEW)


    def mostrar_registro_seleccionado(self, event):
        elemento_seleccionado = self.tabla.selection()[0]#obtenemos el primer elemento seleccionado
        elemento = self.tabla.item(elemento_seleccionado)
        persona = elemento['values']
        showinfo(title='Registro seleccionado', message=f'Id: {persona[0]}\nNombre: {persona[1]}\nEdad: {persona[2]}')



if __name__ == "__main__":
    app = App()
    app.mainloop()
