from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "4321"  # Asegúrate de tener tu clave
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def crear_token(sub: str, es_admin: bool):
    # Usamos utcnow() con 'c' para que no falle
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    data = {
        "sub": sub,
        "exp": expire,
        "es_admin": es_admin
    }
    
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None