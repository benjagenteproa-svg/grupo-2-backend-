import sqlite3
from app.config import DATABASE_PATH


class Database:
    def _init_(self):
        self.dc_path = DATABASE_PATH

    def get_connection(self):
        conn = sqlite3.connect(self.dc_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def init_db(self):
        conn = self.get_connection()
        conn.cursor().executescript("""
CREATE TABLE Usuarios (
id_usuario INTEGER PRIMARY KEY,
nombre VARCHAR(50),
apellido VARCHAR(50),
dni INTEGER
);

CREATE TABLE Libros (
id_libro INTEGER PRIMARY KEY,
titulo VARCHAR(100),
autor VARCHAR(100),
editorial VARCHAR(100)
);

CREATE TABLE Prestamos (
id_prestamo INTEGER PRIMARY KEY,
fecha_prestamo DATE,
fecha_devolucion DATE,
id_usuario INTEGER,
id_libro INTEGER
);

INSERT INTO Usuarios VALUES
(1,'Jose','Perez',40123456),
(2,'Juan','Gomez',42123457),
(3,'Maria','Lopez',43123458),
(4,'Sofia','Martinez',44123459),
(5,'Lucas','Fernandez',45123460);

INSERT INTO Libros VALUES
(1,'El Principito','Antoine de Saint-Exupery','Salamandra'),
(2,'Don Quijote','Miguel de Cervantes','Planeta'),
(3,'Harry Potter','J.K. Rowling','Salamandra'),
(4,'Cien años de soledad','Gabriel Garcia Marquez','Sudamericana'),
(5,'1984','George Orwell','Debolsillo');

INSERT INTO Prestamos VALUES
(1,'2026-09-01','2026-09-15',1,2),
(2,'2026-09-03','2026-09-17',2,1),
(3,'2026-09-05','2026-09-19',3,4),
(4,'2026-09-08','2026-09-22',4,3),
(5,'2026-09-10','2026-09-24',5,5);
""")
        conn.commit()
        conn.close()

db = Database()
