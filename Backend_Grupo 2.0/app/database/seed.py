from app.database.connection import db


def seed():
    conn = db.get_connection()

    if conn.execute("SELECT COUNT(*) FROM libros").fetchone()[0] > 0:
        conn.close()
        return

    conn.executescript("""
        INSERT INTO libros
        (titulo, autor, editorial, año_publicacion, genero)
        VALUES
        ('JoJos', 'Araki', 'Tilin Productions', 1987, 'Manga');

        INSERT INTO usuarios
        (nombre, apellido, dni, curso)
        VALUES
        ('Jose', 'Joestar', '49718971', '5A');

        INSERT INTO prestamos
        (fecha_prestamo, fecha_devolucion, estado, id_usuario, id_libro)
        VALUES
        ('2026-08-25', '2027-01-25', 'activo', 1, 1);
    """)

    conn.commit()
    conn.close()