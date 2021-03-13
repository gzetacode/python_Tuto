#corresponde al video 45 

from tkinter import *

def codigoboton():
    minombre.set("Juan")


#vamos a incorporar un metodo grid o tabla para colocar elementos roww son las filas column son las columnas
raiz=Tk()
miframe=Frame(raiz,width=1200, height="600")
miframe.pack()

minombre=StringVar()
#---creamos los labels
nombrelabel=Label(miframe, text="Nombre:")
nombrelabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

apellidolabel=Label(miframe, text="Apellido:")
apellidolabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

direccionlabel=Label(miframe, text="Direccion de Oficina:")
direccionlabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passlabel=Label(miframe, text="Password:")
passlabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

comentariolabel=Label(miframe, text="Comentarios:")
comentariolabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)


#creamos los Entry labels

cuadronombre=Entry(miframe, textvariable=minombre)
cuadronombre.grid(row=0, column=1)
cuadronombre.config(fg="red",justify="center") #aca le estoy diciendo que el texto que ingreso este en rojo y centredo

cuadroapellido=Entry(miframe)
cuadroapellido.grid(row=1, column=1)

cuadrodireccion=Entry(miframe)
cuadrodireccion.grid(row=2, column=1)

cuadropass=Entry(miframe)
cuadropass.grid(row=3, column=1)
cuadropass.config(show="*") #aca le digo que lo que me muestra sean ******

textocomentario=Text(miframe, width=20, height=8)#creo cuadro de texto
textocomentario.grid(row=4, column=1, padx=5, pady=5)

scrollvertical=Scrollbar(miframe, command=textocomentario.yview) #creamos un elemnto scroll vertica;
scrollvertical.grid(row=4,column=2, sticky="nsew") #lo colocamos en la grilla con sticky="nsew" el scroll se va adaptando al tamaño de la caja de txt
textocomentario.config(yscrollcommand=scrollvertical.set) #con esto la barra del scroll va siguiendo la posicion donde se esta escribiendo

#---Agregamos un boton--

botonenvio=Button(raiz, text="Enviar", command=codigoboton) #creamos un boton enviar en la raiz

botonenvio.pack()

#sticky admite n-s-e-w (norte sur este y oeste) ademas ne se sw nw (nor este sud este etc) 
#el pad (pading) nos da el espaciado alrededor dentro del contenedo ej: padx=10 nos dice que va a tener 10 pixel de espacio adelante y 10 atras

raiz.mainloop()

