#Utilizamos la extencion .pyw para que cuando ejecutemos no nos abra la consola detras
# Tambien denominadas GUI, Son Intermediarios entre el prograna y el Usuario
#si estoy en linux puedo instalar tkinter.... $sudo apt-get install python3-tk
#Estructura de una ventana en tkinter
#tenemos una raiz ....luego un frame.... y luego widgets


from tkinter import *   #Importo TODA la libreria tkinter

raiz=Tk()  #Construyo la raiz llamando a la clase Tk

raiz.title("Primera Ventana")  #con el metodo title ponemos un titulo a la ventana(Raiz)
raiz.iconbitmap("logo.ico")
#raiz.geometry("750x350") #le damos una dimension de 750x350
#raiz.resizable(1,0)  #0 seria false con esto le decimos que width es 0(false) y height es 0 (false) o sea que no puede redimencionarse ni en ancho ni en alto
raiz.config(bg="black")

miframe=Frame() #Ccontruyo un frame,
miframe.pack(side="right",anchor="s")#empaqueto el frame... osea lo meto dentro de la raiz,  side indica donde se ancla el frame (Legal values are: 'left', 'right', 'top', 'bottom')anchor me da el punto cardinal
miframe.config(bg="red")#le damos fdo rojo...notese que si ejecutamos no vemo aun el frame, esto es porque aun no le dimos tamaño, lo hacemos a continuacion
miframe.config(width="650",height="350")#le damos tamaño a frame 

miframe.config(bd=35)#le decimos tamaño de borde
miframe.config(relief="groove")#le decimos tipo de borde
miframe.config(cursor="hand2") 

#-----Enlaces para ver:-----
#https://docs.python.org/3/library/tk.html
#https://docs.python.org/3/library/tkinter.html#setting-options



raiz.mainloop()  #el metodo mainloop hace un bucle infinito debe estar siempre al final
