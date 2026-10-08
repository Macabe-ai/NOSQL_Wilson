import sqlite3

conexion = sqlite3.connect(":memory:")
conexion.executescript("""
CREATE TABLE emprendedores(id INTEGER PRIMARY KEY, alias TEXT);
CREATE TABLE iniciativas(id INTEGER PRIMARY KEY, emprendedor_id INTEGER, estado TEXT);

INSERT INTO emprendedores VALUES(1, 'Emprendedor A'), (2, 'Emprendedor B'), (3, 'Emprendedor C');
INSERT INTO iniciativas VALUES(101, 1, 'activa'), (102, 2, 'archivada'), (103, 1, 'activa');
""")

# Consulta SQL solicitada: id de la iniciativa activa y alias del emprendedor responsable
consulta = """
SELECT i.id, e.alias 
FROM iniciativas i 
JOIN emprendedores e ON i.emprendedor_id = e.id 
WHERE i.estado = 'activa' 
ORDER BY i.id;
"""

if consulta:
    print(conexion.execute(consulta).fetchall())

conexion.close()