from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "Bienvenido a fastPI!"}

@app.get("/")
def read_root():
    return{"message": "Bienvenido a fastPI!"}
productos = []  

@app.get("/productos", response_model=list[schemas.ProductoResponse])
def listar_productos(db:Session = Depends(get_db)):
    return crud.obtener_productos(db)

@app.get("/productos/{id}", tags=["Productos"], summary="Ver detalle de un producto")
def obtener_descripcion_producto(id: int):

    if id < len(productos):
        producto_nombre = productos[id]
        return {
            "id": id,
            "descripcion": f"Este es el producto: {producto_nombre}",
            "nombre": producto_nombre
        }
    return {"error": "Producto no encontrado"}

@app.post("/productos", response_model=schemas.ProductoCreate)
def agregar_productos(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

@app.put("/productos/{id}", response_model=schemas.ProductoCreate)
def actualizar_producto(producto_id: int, datos: schemas.ProductoCreate, db: Session = Depends(get_db)):
    if not producto:
        raise HTTPException(status_code=484, detail="Producto no encontrado")
    return producto

@app.delete("/productos/{id}")
def eliminar_producto(producto_id: int, db:Session = Depends(get_db)):
    producto = crud.eliminar_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto elimnado"}


@app.get("/items/", description="Esta es una descripción detallada del endpoint")
async def read_items():
    return [{"item_id": "Foo"}]