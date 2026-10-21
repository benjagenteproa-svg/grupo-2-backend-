import sqlite3
from app.database.connection import db
from app.models.schemas import PrestamoCreate, PrestamoUpdate

def get_all():
    conn = db.get_connection()
    rows = conn.execute("""
        SELECT
            p.id_prestamo,
            p.fecha_prestamo,
            p.fecha_devolucion,
            p.estado,
            p.id_usuario,
            p.id_libro
        FROM prestamos p
        ORDER BY p.fecha_prestamo
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_by_id(prestamo_id):
    conn = db.get_connection()
    row = conn.execute("""
        SELECT
            id_prestamo,
            fecha_prestamo,
            fecha_devolucion,
            estado,
            id_usuario,
            id_libro
        FROM prestamos
        WHERE id_prestamo = ?
    """, (prestamo_id,)).fetchone()
    conn.close()
    return dict(row) if row else None

def create(data: PrestamoCreate):
    conn = db.get_connection()
    try:
        cursor = conn.execute(
            """
            INSERT INTO prestamos
            (fecha_prestamo, fecha_devolucion, estado, id_usuario, id_libro)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                data.fecha_prestamo,
                data.fecha_devolucion,
                data.estado,
                data.id_usuario,
                data.id_libro
            )
        )
        conn.commit()
        new_id = cursor.lastrowid
    except Exception as e:
        conn.close()
        raise e
    conn.close()
    return get_by_id(new_id)

def update(prestamo_id, data: PrestamoUpdate):
    existing = get_by_id(prestamo_id)
    if not existing:
        return None

    fecha_prestamo = (
        data.fecha_prestamo
        if data.fecha_prestamo is not None
        else existing["fecha_prestamo"]
    )

    fecha_devolucion = (
        data.fecha_devolucion
        if data.fecha_devolucion is not None
        else existing["fecha_devolucion"]
    )

    estado = data.estado if data.estado is not None else existing["estado"]

    id_usuario = (
        data.id_usuario
        if data.id_usuario is not None
        else existing["id_usuario"]
    )

    id_libro = (
        data.id_libro
        if data.id_libro is not None
        else existing["id_libro"]
    )

    conn = db.get_connection()
    conn.execute(
        """
        UPDATE prestamos
        SET fecha_prestamo = ?,
            fecha_devolucion = ?,
            estado = ?,
            id_usuario = ?,
            id_libro = ?
        WHERE id_prestamo = ?
        """,
        (
            fecha_prestamo,
            fecha_devolucion,
            estado,
            id_usuario,
            id_libro,
            prestamo_id
        )
    )
    conn.commit()
    conn.close()
    return get_by_id(prestamo_id)

def delete(prestamo_id):
    conn = db.get_connection()
    affected = conn.execute(
        "DELETE FROM prestamos WHERE id_prestamo = ?",
        (prestamo_id,)
    ).rowcount
    conn.commit()
    conn.close()
    return affected > 0
