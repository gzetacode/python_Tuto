import sqlite3



def coneccionBBDD():
    miconeccion=sqlite3.connect("/Volumes/PLATAFORMA-03/--SYNC--/Sync/PROGRAMACION/Aprendizaje-python/menu CRUD/Usuarios.db")
    micursor=miconeccion.cursor()

    try:
        micursor.execute('''
        CREATE TABLE DATOSUSUARIOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR(50),
        APELLIDO VARCHAR(50),
        EMPRESA VARCAR(50)UNIQUE,
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