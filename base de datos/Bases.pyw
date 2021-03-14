import sqlite3

miconexion=sqlite3.connect("/Volumes/PLATAFORMA-03/--SYNC--/Sync/PROGRAMACION/Aprendizaje-python/base de datos/mibase.db")

micursor=miconexion.cursor()

#micursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#micursor.execute("INSERT INTO PRODUCTOS VALUES('Balon', 15, 'Deportes')")

variosproductos=[
    ("Camiseta", 800, "Deportes"),
    ("Botines", 7000, "Deportes"),
    ("Jarron", 800, "Ceramica"),
    ("Platos", 450, "Bazar"),
    ("Yerba", 350, "Almacen"),
]

micursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)" , variosproductos)

miconexion.commit()



miconexion.close()