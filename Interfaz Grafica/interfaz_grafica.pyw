#Utilizamos la extencion .pyw para que cuando ejecutemos no nos abra la consola detras
# Tambien denominadas GUI, Son Intermediarios entre el prograna y el Usuario
#si estoy en linux puedo instalar tkinter.... $sudo apt-get install python3-tk
#Estructura de una ventana en tkinter
#tenemos una raiz ....luego un frame.... y luego widgets


from tkinter import *   #Importo TODA la libreria tkinter

raiz=Tk()  #Construyo la raiz llamando a la clase Tk

raiz.title("Primera Ventana")  #con el metodo title ponemos un titulo a la ventana(Raiz)
raiz.iconbitmap("logo.ico")
raiz.geometry("750x350") #le damos una dimension de 750x350
raiz.resizable(1,0)  #0 seria false con esto le decimos que width es 0(false) y height es 0 (false) o sea que no puede redimencionarse ni en ancho ni en alto
raiz.config(bg="red")
raiz.mainloop()  #el metodo mainloop hace un bucle infinito debe estar siempre al final
