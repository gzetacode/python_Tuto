from tkinter import *

raiz=Tk()

miframe=Frame(raiz)
miframe.pack()

operacion="" #variable global inicializada en cadena vacia
resultado=0
#--------------Pantalla-------------

numeropantalla=StringVar()
 
pantalla=Entry(miframe, textvariable=numeropantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #columnspan=4 le estoy diciendo que ocupe 4 columnas
pantalla.config(background="black", fg="#1df707", justify="right") 

#------Pulsaciones teclado------------

def numeropulsado(num):
    global operacion
    if operacion!="":
        numeropantalla.set(num)
        operacion=""
    else:
        numeropantalla.set(numeropantalla.get() + num) #numeropantalla.get() es igual a lo que hay en este momento en pantalla

#--------Funcion Suma-----------

def suma(num):
    global operacion #aca le digo que tenga en cuenta que voy a operar con la variable global operacion
    global resultado
    resultado+=int(num) #esto es igual resultado=resultado+int(num)
    operacion="suma"
    numeropantalla.set(resultado)

#-------funcion el resultado-------

def el_resultado():
    global resultado
    numeropantalla.set(resultado+int(numeropantalla.get()))
    resultado=0


#-----------fila1-------------------

boton7=Button(miframe, text="7", width=5, command=lambda:numeropulsado("7"))
boton7.grid(row=2, column=1)

boton8=Button(miframe, text="8", width=5, command=lambda:numeropulsado("8"))
boton8.grid(row=2, column=2)

boton9=Button(miframe, text="9", width=5, command=lambda:numeropulsado("9"))
boton9.grid(row=2, column=3)

botondiv=Button(miframe, text="/", width=5)
botondiv.grid(row=2, column=4)

#-----------fila2-------------------

boton4=Button(miframe, text="4", width=5, command=lambda:numeropulsado("4")) #aca ejecutamos funcion lambda para que el flujo del programa no ejecute command sin apretar boton
boton4.grid(row=3, column=1)

boton5=Button(miframe, text="5", width=5, command=lambda:numeropulsado("5"))
boton5.grid(row=3, column=2)

boton6=Button(miframe, text="6", width=5, command=lambda:numeropulsado("6"))
boton6.grid(row=3, column=3)

botonmult=Button(miframe, text="x", width=5)
botonmult.grid(row=3, column=4)

#-----------fila3-------------------

boton1=Button(miframe, text="1", width=5, command=lambda:numeropulsado("1"))
boton1.grid(row=4, column=1)

boton2=Button(miframe, text="2", width=5, command=lambda:numeropulsado("2"))
boton2.grid(row=4, column=2)

boton3=Button(miframe, text="3", width=5, command=lambda:numeropulsado("3"))
boton3.grid(row=4, column=3)

botonresta=Button(miframe, text="-", width=5)
botonresta.grid(row=4, column=4)

#-----------fila4 -------------------

boton0=Button(miframe, text="0", width=5, command=lambda:numeropulsado("0"))
boton0.grid(row=5, column=1)

botoncoma=Button(miframe, text=",", width=5)
botoncoma.grid(row=5, column=2)

botonigual=Button(miframe, text="=", width=5, command=lambda:el_resultado())
botonigual.grid(row=5, column=3)

botonsuma=Button(miframe, text="+", width=5, command=lambda:suma(numeropantalla.get()))
botonsuma.grid(row=5, column=4)


raiz.mainloop()