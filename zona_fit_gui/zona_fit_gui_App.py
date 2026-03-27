import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from cliente import Cliente
from cliente_dao import ClienteDAO

class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.id_cliente = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titilo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit APP')
        self.configure(bg=self.COLOR_VENTANA)
        # estilos
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')
        self.estilos.configure(self, background=App.COLOR_VENTANA, foreground='white', fieldbackground='black', font=('Arial', 12))

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titilo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM))', font=('Arial', 20,'bold'),background=App.COLOR_VENTANA,foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_forma = ttk.Frame(self)
        # Nombre
        nombre_l = ttk.Label(self.frame_forma, text='Nombre:', background=App.COLOR_VENTANA, foreground='white')
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_e = ttk.Entry(self.frame_forma)
        self.nombre_e.grid(row=0, column=1)

        # publicar el frame
        self.frame_forma.grid(row=1, column=0)
        
        # Apellido
        Apellido_l = ttk.Label(self.frame_forma, text='Apellido:', background=App.COLOR_VENTANA, foreground='white')
        Apellido_l.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_e = ttk.Entry(self.frame_forma)
        self.apellido_e.grid(row=1, column=1)

        # publicar el frame
        self.frame_forma.grid(row=1, column=0)
        
        # Membresia
        Membresia_l = ttk.Label(self.frame_forma, text='Membresia:', background=App.COLOR_VENTANA, foreground='white')
        Membresia_l.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_e = ttk.Entry(self.frame_forma)
        self.membresia_e.grid(row=2, column=1)

        # publicar el frame
        self.frame_forma.grid(row=1, column=0)

    def cargar_tabla(self):
        # Definir frame para mostrar tabla
        self.frame_tabla = ttk.Frame(self)
        # Definimos estilos de la tabla
        self.estilos.configure('Treeview', background='black', foreground='white', fieldbackground='black',rowheight=20, font=('Arial', 12))
        # Defenimos las columnas
        columnas = ('Id','Nombre','Apellido','Membresia')
        # creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # Agregamos los cabeceros
        self.tabla.heading('Id', text='ID',anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre',anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido',anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía',anchor=tk.W)

        # Definir las columnas de la tabla
        self.tabla.column('Id', width=50, anchor=tk.CENTER)
        self.tabla.column('Nombre', width=100, anchor=tk.W)
        self.tabla.column('Apellido', width=100, anchor=tk.W)
        self.tabla.column('Membresia', width=100, anchor=tk.W)

        # Cargar los datos desde la Base de Datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END, 
                              values=(cliente.id, cliente.nombre, cliente.apellido, cliente.membresia))
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # Asociar el evento select
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)

        # publicamos la tabla
        self.tabla.grid(row=0, column=0)
        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1,padx=20)

    def validar_cliente(self):
        if(self.nombre_e.get() and self.apellido_e.get() and self.membresia_e.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atencion', message='La membresía debe ser un número entero')
                self.membresia_e.delete(0, tk.END)
                self.membresia_e.focus_set()
        else:
            showerror(title='Atencion', message='Todos los campos son obligatorios')
            self.nombre_e.focus_set()

    def validar_membresia(self):
        try:
            int(self.membresia_e.get())
            return True
        except ValueError:
            return False
    
    def guardar_cliente(self):
        # recuperamos los valores de las cajas de texto
        nombre = self.nombre_e.get()
        apellido = self.apellido_e.get()
        membresia = int(self.membresia_e.get())
        # Validamos el valor de id_cliente
        if self.id_cliente is None:
            # Creamos un objeto cliente
            cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            # Guardamos el cliente en la base de datos
            ClienteDAO.insertar(cliente)
            showinfo(title='Exito', message='Cliente guardado correctamente')
        else:
            cliente = Cliente(self.id_cliente,nombre,apellido,membresia)
            ClienteDAO.actualizar(cliente)
            showinfo(title='Exito', message='Cliente actualizado correctamente')
        # Actualizamos la tabla
        self.recargar_datos()

    def cargar_cliente(self, event):
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_e = elemento['values']
        self.id_cliente = cliente_e[0]
        nombre = cliente_e[1]
        apellido = cliente_e[2]
        membresia = cliente_e[3]
        self.limpiar_formulario()
        self.nombre_e.insert(0, nombre)
        self.apellido_e.insert(0, apellido)
        self.membresia_e.insert(0, membresia)

    def recargar_datos(self):
        # Volver a cargar los datos de la tabla
        self.cargar_tabla()
        # Limpiamos los campos del formulario
        self.limpiar_datos()
        
    def eliminar_cliente(self):
        if self.id_cliente is None:
            showerror(title='Atencion', message='Debe seleccionar un cliente para eliminar')
        else:
            cliente = Cliente(self.id_cliente)
            ClienteDAO.eliminar(cliente)
            showinfo(title='Exito', message='Cliente eliminado correctamente')
            self.recargar_datos()

    def limpiar_datos(self):
        self.limpiar_formulario()
        self.id_cliente = None

    def limpiar_formulario(self):
        self.nombre_e.delete(0, tk.END)
        self.apellido_e.delete(0, tk.END)
        self.membresia_e.delete(0, tk.END)
        self.nombre_e.focus_set()
        
    def mostrar_botones(self):
        self.frame_botones = ttk.Frame(self)
        # crear los botones
        
        # Boton agregar
        agregar_boton = ttk.Button(self.frame_botones, text='Guardar',command=self.validar_cliente)
        agregar_boton.grid(row=0, column=0, padx=30)
        
        # Boton eliminar
        eliminar_boton = ttk.Button(self.frame_botones, text='Eliminar',command=self.eliminar_cliente)
        eliminar_boton.grid(row=0, column=1, padx=30)
        
        # Boton limpiar
        limpiar_boton = ttk.Button(self.frame_botones, text='limpiar',command=self.limpiar_datos)
        limpiar_boton.grid(row=0, column=2, padx=30)
        
        # Aplicar estilo a los botones
        self.estilos.configure('TButton', background='#005f73', foreground='white', font=('Arial', 12), padding=10)
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        # Publicar frame de botoness
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

if __name__ == '__main__':
    app = App()
    app.mainloop()