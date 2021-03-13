#corresponde al video 45 

from tkinter import *

#vamos a incorporar un metodo grid o tabla para colocar elementos roww son las filas column son las columnas
raiz=Tk()
miframe=Frame(raiz,width=1200, height="600")
miframe.pack()

#---creamos los labels
nombrelabel=Label(miframe, text="Nombre:")
nombrelabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

apellidolabel=Label(miframe, text="Apellido:")
apellidolabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

direccionlabel=Label(miframe, text="Direccion de Oficina:")
direccionlabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passlabel=Label(miframe, text="Password:")
passlabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)


#creamos los Entry labels

cuadronombre=Entry(miframe)
cuadronombre.grid(row=0, column=1)
cuadronombre.config(fg="red",justify="center") #aca le estoy diciendo que el texto que ingreso este en rojo y centredo

cuadroapellido=Entry(miframe)
cuadroapellido.grid(row=1, column=1)

cuadrodireccion=Entry(miframe)
cuadrodireccion.grid(row=2, column=1)

cuadropass=Entry(miframe)
cuadropass.grid(row=3, column=1)
cuadropass.config(show="*") #aca le digo que lo que me muestra sean ******

#sticky admite n-s-e-w (norte sur este y oeste) ademas ne se sw nw (nor este sud este etc) 
#el pad (pading) nos da el espaciado alrededor dentro del contenedo ej: padx=10 nos dice que va a tener 10 pixel de espacio adelante y 10 atras

raiz.mainloop()

