import sqlite3
from app.database.connection import db
from app.models.schemas import UsuarioCreate, UsuarioUpdate

def get_all():
    conn = db.get_connection()
    rows = conn.execute("""
        SELECT id_usuario, nombre, apellido, dni, curso
        FROM usuarios
        ORDER BY apellido, nombre
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_by_id(usuario_id):
    conn = db.get_connection()
    row = conn.execute("""
        SELECT id_usuario, nombre, apellido, dni, curso
        FROM usuarios
        WHERE id_usuario = ?
    """, (usuario_id,)).fetchone()
    conn.close()
    return dict(row) if row else None

def create(data: UsuarioCreate):
    conn = db.get_connection()
    try:
        cursor = conn.execute(
            "INSERT INTO usuarios (nombre, apellido, dni, curso) VALUES (?, ?, ?, ?)",
            (data.nombre, data.apellido, data.dni, data.curso)
        )
        conn.commit()
        new_id = cursor.lastrowid
    except Exception as e:
        conn.close()
        raise e
    conn.close()
    return get_by_id(new_id)

def update(usuario_id, data: UsuarioUpdate):
    existing = get_by_id(usuario_id)
    if not existing:
        return None

    nombre = data.nombre if data.nombre is not None else existing["nombre"]
    apellido = data.apellido if data.apellido is not None else existing["apellido"]
    dni = data.dni if data.dni is not None else existing["dni"]
    curso = data.curso if data.curso is not None else existing["curso"]

    conn = db.get_connection()
    conn.execute(
        """
        UPDATE usuarios
        SET nombre = ?, apellido = ?, dni = ?, curso = ?
        WHERE id_usuario = ?
        """,
        (nombre, apellido, dni, curso, usuario_id)
    )
    conn.commit()
    conn.close()
    return get_by_id(usuario_id)

def delete(usuario_id):
    conn = db.get_connection()
    affected = conn.execute(
        "DELETE FROM usuarios WHERE id_usuario = ?",
        (usuario_id,)
    ).rowcount
    conn.commit()
    conn.close()
    return affected > 0
