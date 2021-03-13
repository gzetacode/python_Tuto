
#--Label--
#sintaxis:  variavlelabel=Label(contenedor,opciones)
#opciones = https://docs.python.org/3/library/tkinter.ttk.html#label-options

from tkinter import *

root=Tk()
miframe=Frame(root,width="1200", height="1400")
miframe.pack()

milabel=Label(miframe, text="Aqui va mi primer fucking texto")
#milabel.pack()# si hacemos esto no va a respetar las medidas del frame y las va a adaptar al texto
#si no queremos que eso ocurra en vez de empaquetar el label usamos el metodo place

milabel.place(x="100", y="70")#ahora si respeta la medida del frame y coloca el texto en las coordenadas

#si queremos abreviar cogigo y no crear variable label....

miimagen=PhotoImage(file="/Volumes/PLATAFORMA-03/--SYNC--/Sync/PROGRAMACION/Aprendizaje-python/Interfaz Grafica/dr.png")#utilizamos la clase PhotoImage

Label(miframe, text="Asi tambien se puede hacer").place(x=120, y=100)
Label(miframe, text="Aca jugamos con los parametros", fg="red", font=("Arial Black", 19)).place(x=120, y=140)

Label(miframe, image=miimagen).place(x=20, y=200)


root.mainloop()

