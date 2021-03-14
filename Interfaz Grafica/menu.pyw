from tkinter import *

raiz=Tk()

barramenu=Menu(raiz)
raiz.config(menu=barramenu, width=300, height=300)

archivomenu=Menu(barramenu, tearoff=0)
archivomenu.add_command(label="Nuevo")
archivomenu.add_command(label="Guardar")
archivomenu.add_command(label="Guardar como")
archivomenu.add_separator() #separador
archivomenu.add_command(label="Cerrar")
archivomenu.add_command(label="Salir")


archivoedicion=Menu(barramenu)
archivoedicion.add_command(label="Copiar")
archivoedicion.add_command(label="Pegar")

archivoherramientas=Menu(barramenu)
archivoherramientas.add_command(label="Amoladora")
archivoherramientas.add_command(label="Sierra")
archivoherramientas.add_command(label="Sensitiva")
archivoherramientas.add_command(label="Martillo")

archivoayuda=Menu(barramenu)
archivoayuda.add_command(label="Help")
archivoayuda.add_command(label="Acerca de...")

barramenu.add_cascade(label="Files", menu=archivomenu)
barramenu.add_cascade(label="Edit", menu=archivoedicion)
barramenu.add_cascade(label="Tools", menu=archivoherramientas)
barramenu.add_cascade(label="Help", menu=archivoayuda)


raiz.mainloop()

