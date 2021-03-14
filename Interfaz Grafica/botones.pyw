from tkinter import *

root=Tk()


def imprimir():
    #print(varopcion.get())  # Con varopcion.get() rescatamos el valor que tiene la variable varopcion en ese momento
    if varopcion.get()==1:
        etiqueta.config(text="Elejiste la opcion Masculino")
    elif varopcion.get()==2:
        etiqueta.config(text="Elejiste la opcion Femenino")
    else:
        etiqueta.config(text="Elejiste Otras Opciones")


varopcion=IntVar()

Label(root, text="Genero:").pack()

Radiobutton(root, text="Masculino", variable=varopcion, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varopcion, value=2, command=imprimir).pack()
Radiobutton(root, text="Otras Opciones:", variable=varopcion, value=3, command=imprimir).pack()
#value=1 estaria asignado uno a la variable varopcion

etiqueta=Label(root)
etiqueta.pack()

playa=IntVar()
montana=IntVar()
rural=IntVar()

def opciones_viajes():
    opcionescojida=""
    if(playa.get()==1):
        opcionescojida+=" playa"
    if(montana.get()==1):
        opcionescojida+=" montaña"
    if(rural.get()==1):
        opcionescojida+=" turismo rural"

    textofinal.config(text=opcionescojida)




frame=Frame(root)
frame.pack()

Label(frame, text="Elije Destino/s:", width=80).pack()

Checkbutton(frame,text="Playa",variable=playa, onvalue=1, offvalue=0, command=opciones_viajes).pack()
Checkbutton(frame,text="Montaña",variable=montana, onvalue=1, offvalue=0, command=opciones_viajes).pack()
Checkbutton(frame,text="Turismo Rural",variable=rural, onvalue=1, offvalue=0, command=opciones_viajes).pack()

textofinal=Label(frame)
textofinal.pack()



root.mainloop()