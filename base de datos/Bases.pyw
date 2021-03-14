import sqlite3

miconexion=sqlite3.connect("/Volumes/PLATAFORMA-03/--SYNC--/Sync/PROGRAMACION/Aprendizaje-python/base de datos/mibase.db")

micursor=miconexion.cursor()

#------Read------
micursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Deportes'")
productos=micursor.fetchall()
print(productos)

#----UPDATE---------------
micursor.execute("UPDATE PRODUCTOS SET PRECIO=1200 WHERE NOMBRE_ARTICULOS='Jarron'")

#------Delete-----------------

micursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULOS='Platos'")


miconexion.commit()


 
miconexion.close()