from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    
    # Una categoría tiene MUCHOS productos (plural)
    # Cambiado back_populates a "categoria" (singular)
    productos = relationship("Producto", back_populates="categoria")


class Producto(Base):
    __tablename__ = "productos"  # Cambiado a minúscula para ser consistente
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio = Column(Float)
    en_stock = Column(Boolean, default=True)
    
    # Llave foránea apunta al __tablename__ ("categorias.id")
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    
    # Un producto tiene UNA categoría (singular)
    # Corregido "Categorias" por "Categoria" y renombrado a singular
    categoria = relationship("Categoria", back_populates="productos")


class Usuario(Base):
    __tablename__ = "usuarios"  # Cambiado a plural para mantener el estándar
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    es_admin = Column(Boolean, default=False)