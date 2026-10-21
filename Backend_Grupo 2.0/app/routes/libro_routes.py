from fastapi import APIRouter
from app.models.schemas import LibroCreate, LibroUpdate
from app.controllers import libro_controller as ctrl

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.get("/")
def listar_libros():
    return ctrl.listar()

@router.get("/{libro_id}")
def obtener_libro(libro_id: int):
    return ctrl.obtener(libro_id)

@router.post("/", status_code=201)
def crear_libro(body: LibroCreate):
    return ctrl.crear(body)

@router.put("/{libro_id}")
def modificar_libro(libro_id: int, body: LibroUpdate):
    return ctrl.modificar(libro_id, body)

@router.delete("/{libro_id}")
def eliminar_libro(libro_id: int):
    return ctrl.eliminar(libro_id)