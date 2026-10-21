import sqlite3
from app.database.connection import db
from app.models.schemas import LibroCreate, LibroUpdate

def get_all():
    conn = db.get_connection()
    rows = conn.execute("""
        SELECT id_libro, titulo, autor, editorial, año_publicacion, genero
        FROM libros
        ORDER BY titulo
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_by_id(libro_id):
    conn = db.get_connection()
    row = conn.execute("""
        SELECT id_libro, titulo, autor, editorial, año_publicacion, genero
        FROM libros
        WHERE id_libro = ?
    """, (libro_id,)).fetchone()
    conn.close()
    return dict(row) if row else None

def create(data: LibroCreate):
    conn = db.get_connection()
    try:
        cursor = conn.execute(
            """
            INSERT INTO libros
            (titulo, autor, editorial, año_publicacion, genero)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                data.titulo,
                data.autor,
                data.editorial,
                data.año_publicacion,
                data.genero
            )
        )
        conn.commit()
        new_id = cursor.lastrowid
    except Exception as e:
        conn.close()
        raise e
    conn.close()
    return get_by_id(new_id)

def update(libro_id, data: LibroUpdate):
    existing = get_by_id(libro_id)
    if not existing:
        return None

    titulo = data.titulo if data.titulo is not None else existing["titulo"]
    autor = data.autor if data.autor is not None else existing["autor"]
    editorial = data.editorial if data.editorial is not None else existing["editorial"]
    año_publicacion = (
        data.año_publicacion
        if data.año_publicacion is not None
        else existing["año_publicacion"]
    )
    genero = data.genero if data.genero is not None else existing["genero"]

    conn = db.get_connection()
    conn.execute(
        """
        UPDATE libros
        SET titulo = ?, autor = ?, editorial = ?, año_publicacion = ?, genero = ?
        WHERE id_libro = ?
        """,
        (
            titulo,
            autor,
            editorial,
            año_publicacion,
            genero,
            libro_id
        )
    )
    conn.commit()
    conn.close()
    return get_by_id(libro_id)

def delete(libro_id):
    conn = db.get_connection()
    affected = conn.execute(
        "DELETE FROM libros WHERE id_libro = ?",
        (libro_id,)
    ).rowcount
    conn.commit()
    conn.close()
    return affected > 0
