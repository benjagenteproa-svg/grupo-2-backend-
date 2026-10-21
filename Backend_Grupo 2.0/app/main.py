from fastapi import FastAPI
from app.config import APP_TITLE, APP_VERSION
from app.database.connection import db
from app.database.seed import seed
from app.routes.usuario_routes import router as usuario_router
from app.routes.prestamo_routes import router as prestamo_router
from app.routes.libro_routes import router as libro_router


app = FastAPI(title=APP_TITLE, version=APP_VERSION)

db.init_db()
seed()

app.include_router(usuario_router)
app.include_router(prestamo_router)
app.include_router(libro_router)

@app.get("/")
def root():
     return {"message": f"Bienvenido a {APP_TITLE} v{APP_VERSION}"}