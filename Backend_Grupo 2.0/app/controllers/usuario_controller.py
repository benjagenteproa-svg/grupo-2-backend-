from app.services import usuario_service as svc
from app.models.schemas import UsuarioCreate, UsuarioUpdate
from app.utils.responses import ok, not_found, db_error

def listar():
    try:
        return ok(svc.get_all(), "Usuarios obtenidos correctamente.")
    except Exception as e:
        db_error(e)

def obtener(usuario_id):
    try:
        data = svc.get_by_id(usuario_id)
    except Exception as e:
        db_error(e)
    if not data:
        not_found("Usuario", usuario_id)
    return ok(data, "Usuario encontrado.")

def crear(body: UsuarioCreate):
    try:
        return ok(svc.create(body), "Usuario creado correctamente.")
    except Exception as e:
        db_error(e)

def modificar(usuario_id, body: UsuarioUpdate):
    try:
        data = svc.update(usuario_id, body)
    except Exception as e:
        db_error(e)
    if not data:
        not_found("Usuario", usuario_id)
    return ok(data, "Usuario actualizado correctamente.")

def eliminar(usuario_id):
    try:
        deleted = svc.delete(usuario_id)
    except Exception as e:
        db_error(e)
    if not deleted:
        not_found("Usuario", usuario_id)
    return ok(None, "Usuario eliminado correctamente.")