from pydantic import BaseModel, EmailStr

# --- CATEGORÍAS ---
class CategoriasBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriasBase):
    pass

class CategoriaResponse(CategoriasBase):
    id: int

    class Config:
        from_attributes = True  # Actualizado para Pydantic v2


# --- PRODUCTOS ---
class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    categoria_id: int

class ProductoResponse(ProductoCreate):
    id: int
    
    class Config:
        from_attributes = True  # Actualizado para Pydantic v2


# --- USUARIOS (Eliminado el duplicado) ---
class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str
    es_admin: bool = False

class UsuarioResponse(UsuarioBase):
    id: int
    es_admin: bool = False

    class Config:
        from_attributes = True  # Actualizado para Pydantic v2


# --- AUTENTICACIÓN ---
class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"