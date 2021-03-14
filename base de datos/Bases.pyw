import sqlite3

miconexion=sqlite3.connect("/Volumes/PLATAFORMA-03/--SYNC--/Sync/PROGRAMACION/Aprendizaje-python/base de datos/mibase.db")

micursor=miconexion.cursor()

micursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULOS VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')


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