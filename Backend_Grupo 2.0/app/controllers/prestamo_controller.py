from app.services import prestamo_service as svc
from app.services import usuario_service as usuario_svc
from app.services import libro_service as libro_svc
from app.models.schemas import PrestamoCreate, PrestamoUpdate
from app.utils.responses import ok, not_found, db_error

def listar():
    try:
        return ok(svc.get_all(), "Préstamos obtenidos correctamente.")
    except Exception as e:
        db_error(e)

def obtener(prestamo_id):
    try:
        data = svc.get_by_id(prestamo_id)
    except Exception as e:
        db_error(e)
    if not data:
        not_found("Préstamo", prestamo_id)
    return ok(data, "Préstamo encontrado.")

def crear(body: PrestamoCreate):
    if not usuario_svc.get_by_id(body.id_usuario):
        not_found("Usuario", body.id_usuario)
    if not libro_svc.get_by_id(body.id_libro):
        not_found("Libro", body.id_libro)
    try:
        return ok(svc.create(body), "Préstamo creado correctamente.")
    except Exception as e:
        db_error(e)

def modificar(prestamo_id, body: PrestamoUpdate):
    if body.id_usuario and not usuario_svc.get_by_id(body.id_usuario):
        not_found("Usuario", body.id_usuario)
    if body.id_libro and not libro_svc.get_by_id(body.id_libro):
        not_found("Libro", body.id_libro)
    try:
        data = svc.update(prestamo_id, body)
    except Exception as e:
        db_error(e)
    if not data:
        not_found("Préstamo", prestamo_id)
    return ok(data, "Préstamo actualizado correctamente.")

def eliminar(prestamo_id):
    try:
        deleted = svc.delete(prestamo_id)
    except Exception as e:
        db_error(e)
    if not deleted:
        not_found("Préstamo", prestamo_id)
    return ok(None, "Préstamo eliminado correctamente.")