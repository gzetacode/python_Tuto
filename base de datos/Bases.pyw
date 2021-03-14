import sqlite3

miconexion=sqlite3.connect("/Volumes/PLATAFORMA-03/--SYNC--/Sync/PROGRAMACION/Aprendizaje-python/base de datos/mibase.db")

micursor=miconexion.cursor()

micursor.execute('''
    CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULOS VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULOS VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')


variosproductos=[
    ("AR01","Camiseta", 800, "Deportes"),
    ("AR02","Botines", 7000, "Deportes"),
    ("AR03","Jarron", 800, "Ceramica"),
    ("AR04","Platos", 450, "Bazar"),
    ("AR05","Yerba", 350, "Almacen")
]



micursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)" , variosproductos)

  


miconexion.commit()



miconexion.close()