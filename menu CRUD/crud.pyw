from tkinter import *
from tkinter import messagebox
import sqlite3


#-----Funciones-------

def coneccionBBDD():
    miconeccion=sqlite3.connect("/Volumes/PLATAFORMA-03/--SYNC--/Sync/PROGRAMACION/Aprendizaje-python/menu CRUD/Usuarios.db")
    micursor=miconeccion.cursor()

    try:
        micursor.execute('''
        CREATE TABLE DATOSUSUARIOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR(50),
        APELLIDO VARCHAR(50),
        EMPRESA VARCAR(50),
        EMAIL VARCHAR(50),
        CUIT INTEGER(50) UNIQUE,
        TELEFONO VARCHAR(25),
        PASSWORD VARCHAR(50),
        COMENTARIOS VARCHAR(200)
        )   
        ''')
        messagebox.showinfo("BBDD", "BBDD Creada con exito")

    except:
        messagebox.showwarning("Atencion!!", "BBDD ya existe!!!!")

def saliraplicacion():
    valor=messagebox.askquestion("salir", "Deseas salir de la Aplicacion?")
    if valor=="yes":
        root.destroy()

root=Tk()

def limpiarcampos():
    miid.set("")
    minombre.set("")
    miapellido.set("")
    miempresa.set("")
    mitelefono.set("")
    miemail.set("")
    micuit.set("")
    mipass.set("")
    textocomentario.delete(1.0, END)
def crear():
    miconeccion=sqlite3.connect("/Volumes/PLATAFORMA-03/--SYNC--/Sync/PROGRAMACION/Aprendizaje-python/menu CRUD/Usuarios.db")
    micursor=miconeccion.cursor()

    micursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, '" + minombre.get() +
        "','" + miapellido.get() +
        "','" + miempresa.get() +
        "','" + miemail.get() +
        "','" + micuit.get() +
        "','" + mitelefono.get() +
        "','" + mipass.get() +
        "','" + textocomentario.get("1.0", END) + "')")
    miconeccion.commit()
    limpiarcampos()
    messagebox.showinfo("BBDD", "Registro insertado con exito")



barramenu=Menu(root)
root.config(menu=barramenu, width=300, height=600)

bbddmenu=Menu(barramenu, tearoff=0)
bbddmenu.add_command(label="Conectar", command=coneccionBBDD)
bbddmenu.add_command(label="Salir", command=saliraplicacion)

borrarmenu=Menu(barramenu, tearoff=0)
borrarmenu.add_command(label="Borrar Campos", command=limpiarcampos)

crudmenu=Menu(barramenu, tearoff=0)
crudmenu.add_command(label="Crear", command=crear)
crudmenu.add_command(label="Leer")
crudmenu.add_command(label="Actualizar")
crudmenu.add_command(label="Borrar")

ayudamenu=Menu(barramenu, tearoff=0)
ayudamenu.add_command(label="Licencia")
ayudamenu.add_command(label="Acerca de...")

barramenu.add_cascade(label="BBDD", menu=bbddmenu)
barramenu.add_cascade(label="Borrar", menu=borrarmenu)
barramenu.add_cascade(label="CRUD", menu=crudmenu)
barramenu.add_cascade(label="Ayuda", menu=ayudamenu)



miframe=Frame()
miframe.pack()

miid=StringVar()
minombre=StringVar()
miapellido=StringVar()
miempresa=StringVar()
miemail=StringVar()
micuit=StringVar()
mitelefono=StringVar()
mipass=StringVar()


#-----------Comienzo los label--------------

idlabel=Label(miframe, text="ID:")
idlabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombrelabel=Label(miframe, text="Nombre:")
nombrelabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidolabel=Label(miframe, text="Apellido:")
apellidolabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

empresalabel=Label(miframe, text="Empresa:")
empresalabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

emaillabel=Label(miframe, text="Email:")
emaillabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

cuitlabel=Label(miframe, text="Cuit:")
cuitlabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

telefonolabel=Label(miframe, text="Telefono:")
telefonolabel.grid(row=6, column=0, sticky="e", padx=10, pady=10)

passlabel=Label(miframe, text="Password:")
passlabel.grid(row=7, column=0, sticky="e", padx=10, pady=10)

comentariolabel=Label(miframe, text="Comentario:")
comentariolabel.grid(row=8, column=0, sticky="e", padx=10, pady=10)

#-----------Comienzo de campos--------------


cuadroiD=Entry(miframe, textvariable=miid)
cuadroiD.grid(row=0, column=1, padx=10, pady=10)

cuadronombre=Entry(miframe, textvariable=minombre)
cuadronombre.grid(row=1, column=1, padx=10, pady=10)

cuadroapellido=Entry(miframe, textvariable=miapellido)
cuadroapellido.grid(row=2, column=1, padx=10, pady=10)

cuadroempresa=Entry(miframe, textvariable=miempresa)
cuadroempresa.grid(row=3, column=1, padx=10, pady=10)

cuadroemail=Entry(miframe, textvariable=miemail)
cuadroemail.grid(row=4, column=1, padx=10, pady=10)

cuadrocuit=Entry(miframe, textvariable=micuit)
cuadrocuit.grid(row=5, column=1, padx=10, pady=10)

cuadrotelefono=Entry(miframe, textvariable=mitelefono)
cuadrotelefono.grid(row=6, column=1, padx=10, pady=10)

cuadropass=Entry(miframe, textvariable=mipass)
cuadropass.grid(row=7, column=1, padx=10, pady=10)

textocomentario=Text(miframe, width=23, height=5)
textocomentario.grid(row=8, column=1, padx=10, pady=10)
scrollvert=Scrollbar(miframe, command=textocomentario.yview)
scrollvert.grid(row=8,column=2, sticky="nsew")
textocomentario.config(yscrollcommand=scrollvert.set)

#----Aqui los botones en otro frame--------

miframe2=Frame()
miframe2.pack()

botoncrear=Button(miframe2, text="Create", command=crear)
botoncrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonleer=Button(miframe2, text="read")
botonleer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonactualizar=Button(miframe2, text="Update")
botonactualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonborrar=Button(miframe2, text="Delete")
botonborrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

root.mainloop()
   