from fastapi import APIRouter
from app.models.schemas import PrestamoCreate, PrestamoUpdate
from app.controllers import prestamo_controller as ctrl

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])

@router.get("/")
def listar_prestamos():
    return ctrl.listar()

@router.get("/{prestamo_id}")
def obtener_prestamo(prestamo_id: int):
    return ctrl.obtener(prestamo_id)

@router.post("/", status_code=201)
def crear_prestamo(body: PrestamoCreate):
    return ctrl.crear(body)

@router.put("/{prestamo_id}")
def modificar_prestamo(prestamo_id: int, body: PrestamoUpdate):
    return ctrl.modificar(prestamo_id, body)

@router.delete("/{prestamo_id}")
def eliminar_prestamo(prestamo_id: int):
    return ctrl.eliminar(prestamo_id)