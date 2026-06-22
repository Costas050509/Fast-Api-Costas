from sqlalchemy.orm import Session
from models import Producto, Categoria
from schemas import ProductoCreate, CategoriaCreate
from utils import hash_password
from sqlalchemy import or_
from sqlalchemy.orm import Session
from models import Usuario  # <-- ¡ESTA IMPORTACIÓN ES LA QUE FALTA EN CRUD.PY!
import schemas


def crear_producto(db: Session, producto:ProductoCreate):
    db_producto = Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto) 
    return db_producto

def obtener_productos(db:Session):
    return db.query(Producto).all()

def obtener_producto(db:Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def actualizar_producto(db:Session, producto_id: int, datos:ProductoCreate):
    producto = obtener_producto(db, producto_id)        

def eliminar_producto(db:Session, producto_id: int):
    producto = obtener_producto(db, producto_id)

    if producto:
        db.delete(producto)
        db.commit()
    return producto


def crear_categoria(db:Session, categoria: CategoriaCreate):
    db_categoria = Categoria(nombre=categoria.nombre)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def obtener_categorias(db:Session):
    return db.query(Categoria).all()

def obtener_usuario_por_mail(db:Session, email: str) -> Usuario | None:
    return db.query(Usuario).filter(Usuario.email == email).first()

def obtener_usuario_por_id(db:Session, usuario_id: int ) -> Usuario | None:
    return db.query(Usuario).filter(Usuario.id == usuario.id). first()

def crear_usuario(db:Session, usuario: UsuarioCreate) -> Usuario:
    existe = db.query(usuario).filter(
        or_(Usuario.email == usuario.email, Usuario.nombre == usuario.nombre)
    ).first()
    if existe:
        raise ValueError("Ya existe un usuario con ese email o nombre")
    
    db_usuario = Usuario(
        nombre = usuario.nombre,
        email = usuario.email,
        hash_password = hash_password(usuario.password),
        es_admin = usuario.es_admin
    )

    db.add(db.usuario)
    db.commit()
    db.refresh(db.usuario)
    return db_usuario

def obtener_usuario_por_id(db:Session, usuario_id: int ) -> Usuario | None:
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def crear_usuario(db:Session, usuario: UsuarioCreate) -> Usuario:
    existe = db.query(Usuario).filter(
        or_(Usuario.email == usuario.email, Usuario.nombre == usuario.nombre)
    ).first()
    if existe:
        raise ValueError("Ya existe un usuario con ese email o nombre")
    
    db.usuario = Usuario(
        nombre = usuario.nombre,
        email = usuario.email,
        hashed_password = hash_password(usuario.password),
        es_admin = usuario.es_admin 
    )
