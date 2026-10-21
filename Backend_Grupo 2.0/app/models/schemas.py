from datetime import date
from pydantic import BaseModel
from typing import Optional

class UsuarioCreate(BaseModel):
    nombre: str
    apellido: str
    dni: int
    curso: str

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    dni: Optional[int] = None
    curso: Optional[str] = None

class LibroCreate(BaseModel):
    titulo: str
    autor: str
    editorial: str
    año_publicacion: int
    genero: str 

class LibroUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    editorial: Optional[str] = None
    año_publicacion: Optional[int] = None
    genero: Optional[str] = None

class UsuarioOut(BaseModel):
    id_usuario: int
    nombre: str
    apellido: str
    dni: int
    curso: str

class LibroOut(BaseModel):
    d_libro: int
    titulo: str
    autor: str
    editorial: str
    año_publicacion: int
    genero: str

class PrestamoOut(BaseModel):
    id_prestamo: int
    fecha_prestamo: str
    fecha_devolucion: Optional[str] = None
    estado: str
    id_usuario: int
    id_libro: int

class PrestamoCreate(BaseModel):
    fecha_prestamo: str
    fecha_devolucion: Optional[str] = None
    estado: str
    id_usuario: int
    id_libro: int

class PrestamoUpdate(BaseModel):
    fecha_prestamo: Optional[str] = None
    fecha_devolucion: Optional[str] = None
    estado: Optional[str] = None
    id_usuario: Optional[int] = None
    id_libro: Optional[int] = None