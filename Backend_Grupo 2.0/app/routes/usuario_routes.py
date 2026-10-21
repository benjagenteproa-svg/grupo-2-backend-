from fastapi import APIRouter
from app.models.schemas import UsuarioCreate, UsuarioUpdate
from app.controllers import usuario_controller as ctrl

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/")
def listar_usuarios():
    return ctrl.listar()

@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: int):
    return ctrl.obtener(usuario_id)

@router.post("/", status_code=201)
def crear_usuario(body: UsuarioCreate):
    return ctrl.crear(body)

@router.put("/{usuario_id}")
def modificar_usuario(usuario_id: int, body: UsuarioUpdate):
    return ctrl.modificar(usuario_id, body)

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    return ctrl.eliminar(usuario_id)