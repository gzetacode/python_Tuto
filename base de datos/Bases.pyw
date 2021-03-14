import sqlite3

miconexion=sqlite3.connect("/Volumes/PLATAFORMA-03/--SYNC--/Sync/PROGRAMACION/Aprendizaje-python/base de datos/mibase.db")

micursor=miconexion.cursor()

micursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#micursor.execute("INSERT INTO PRODUCTOS VALUES('Balon', 15, 'Deportes')")
#miconexion.commit()



miconexion.close()