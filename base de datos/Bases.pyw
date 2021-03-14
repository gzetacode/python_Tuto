import sqlite3

miconexion=sqlite3.connect("/Volumes/PLATAFORMA-03/--SYNC--/Sync/PROGRAMACION/Aprendizaje-python/base de datos/mibase.db")

micursor=miconexion.cursor()

#micursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#micursor.execute("INSERT INTO PRODUCTOS VALUES('Balon', 15, 'Deportes')")

#variosproductos=[
#    ("Camiseta", 800, "Deportes"),
#    ("Botines", 7000, "Deportes"),
#    ("Jarron", 800, "Ceramica"),
#    ("Platos", 450, "Bazar"),
#    ("Yerba", 350, "Almacen"),
#]

#micursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)" , variosproductos)




micursor.execute("SELECT * FROM PRODUCTOS")
variosproductos=micursor.fetchall()  
#el metodo fetchall nos devuelve una lista con todos los registros 
# que nos devuelve la instruccion sql y esta lista se almacenara en variosproductos
for producto in variosproductos:
    print("-Nombre Articulo: ", producto[0], "-Precio: $", producto[1], "-Seccion: ", producto[2])



miconexion.commit()



miconexion.close()