from app.services import libro_service as svc
from app.models.schemas import LibroCreate, LibroUpdate
from app.utils.responses import ok, not_found, db_error

def listar():
    try:
        return ok(svc.get_all(), "Libros obtenidos correctamente.")
    except Exception as e:
        db_error(e)

def obtener(libro_id):
    try:
        data = svc.get_by_id(libro_id)
    except Exception as e:
        db_error(e)
    if not data:
        not_found("Libro", libro_id)
    return ok(data, "Libro encontrado.")

def crear(body: LibroCreate):
    try:
        return ok(svc.create(body), "Libro creado correctamente.")
    except Exception as e:
        db_error(e)

def modificar(libro_id, body: LibroUpdate):
    try:
        data = svc.update(libro_id, body)
    except Exception as e:
        db_error(e)
    if not data:
        not_found("Libro", libro_id)
    return ok(data, "Libro actualizado correctamente.")

def eliminar(libro_id):
    try:
        deleted = svc.delete(libro_id)
    except Exception as e:
        db_error(e)
    if not deleted:
        not_found("Libro", libro_id)
    return ok(None, "Libro eliminado correctamente.")