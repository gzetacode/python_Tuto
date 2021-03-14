from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
raiz=Tk()

def abrefichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="/Volumes/PLATAFORMA-03", filetypes=(("Archivos Video", "*.mp4"),("Archivos imagen", "*.jpg"),("Todos los Archivos", "*.*"))) #devueve la ruta de el archivo elejido

    print(fichero)




def infoadicional():
    messagebox.showinfo("Software de El Programador", "Programa de enseñanza de libreria visuales")
def avisolicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia exclusiva de:'El Programador' ")
def saliraplicacion():
    valor=messagebox.askquestion("Salir", "Desea Salir de la Aplicacion?")  #esta opcion devuelve un valor segun boton apretado(yes-no)
    if valor=="yes":
        raiz.destroy()
def cerraraplicacion():
    valor=messagebox.askokcancel("Cerrar", "Desea Cerrar la Aplicacion?")  #esta opcion devuelve un valor segun boton apretado(true-false)
    if valor==True:
        raiz.destroy()

def amoladora():
    valor=messagebox.askretrycancel("reintentar", "No es posible Usar esta herramienta")
    if valor==True:
        messagebox.showinfo("Software de El Programador", "Es bueno Reintentar en la vida, pero en este caso no lo es")
barramenu=Menu(raiz)
raiz.config(menu=barramenu, width=300, height=300)

archivomenu=Menu(barramenu, tearoff=0)
archivomenu.add_command(label="Abrir", command=abrefichero)
archivomenu.add_command(label="Nuevo")
archivomenu.add_command(label="Guardar")
archivomenu.add_command(label="Guardar como")
archivomenu.add_separator() #separador
archivomenu.add_command(label="Cerrar", command=cerraraplicacion)
archivomenu.add_command(label="Salir", command=saliraplicacion)


archivoedicion=Menu(barramenu)
archivoedicion.add_command(label="Copiar")
archivoedicion.add_command(label="Pegar")

archivoherramientas=Menu(barramenu)
archivoherramientas.add_command(label="Amoladora", command=amoladora)
archivoherramientas.add_command(label="Sierra")
archivoherramientas.add_command(label="Sensitiva")
archivoherramientas.add_command(label="Martillo")

archivoayuda=Menu(barramenu)
archivoayuda.add_command(label="Help")
archivoayuda.add_command(label="Licencia", command=avisolicencia)
archivoayuda.add_command(label="Acerca de...", command=infoadicional )

barramenu.add_cascade(label="Files", menu=archivomenu)
barramenu.add_cascade(label="Edit", menu=archivoedicion)
barramenu.add_cascade(label="Tools", menu=archivoherramientas)
barramenu.add_cascade(label="Help", menu=archivoayuda)


raiz.mainloop()

