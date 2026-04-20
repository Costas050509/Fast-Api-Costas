from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "Bienvenido a fastPI!"}

productos = []  

@app.get("/productos")
def listar_productos():
    return {"productos": productos}

@app.post("/productos")
def agregar_productos(nombre:str):
    productos.append(nombre)
    return {"mensaje": "producto agregado", "producto": nombre}

@app.put("/productos/{id}")
def actualizar_producto(id:int, nombre: str):
    productos[id] = nombre
    return {"mensaje": "producto actualizado", "producto": nombre}

@app.delete("/productos/{id}")
def eliminar_producto(id:int):
    eliminado = productos.pop(id)
    return {"mensaje": "producto eliminado", "producto": eliminado}