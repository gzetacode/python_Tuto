import sqlite3

miconexion=sqlite3.connect("/Volumes/PLATAFORMA-03/--SYNC--/Sync/PROGRAMACION/Aprendizaje-python/base de datos/mibase.db")

micursor=miconexion.cursor()

micursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULOS VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')
#al agregar unique al campo nombre de articulo estamos indicando que es unico 
# y no se puede repetir si ingresamos dos articulos con el mismo nombre da error

variosproductos=[
    ("Camiseta", 800, "Deportes"),
    ("Botines", 7000, "Deportes"),
    ("Jarron", 800, "Ceramica"),
    ("Platos", 450, "Bazar"),
    ("Yerba", 350, "Almacen")
]



micursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)" , variosproductos)

  


miconexion.commit()



miconexion.close()