from fastapi import HTTPException

def ok(data, message="OK"):
     return {"success": True, "message": message, "data": data}

def not_found(entidad, id):
     raise HTTPException(status_code=404, detail=f"{entidad} con id={id} no encontrado/a.")

def conflict(detail):
    raise HTTPException(status_code=409, detail=detail)

def db_error(e):
     raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(e)}") 