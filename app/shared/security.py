from datetime import datetime,  timedelta
from jose import jwt
from passlib.context import CryptContext
from app.shared.timezone import COLOMBIA_TZ
import os

# Hash de contraseña
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Configuracion JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES" , 60))

# Funcion para verificar contraseña
def verify_password(plain_password : str, hashed_password : str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Funcion para hasehar contraseña
def hashed_password(password: str) -> str:
    return pwd_context.hash(password)

# Funcion para generar el token JWt
def create_access_token(data: dict) -> str:
    to_encode = data.copy() # Copia la infromacion de lo que envia el usuario
    expire = datetime.now(COLOMBIA_TZ) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # Tiempo de expiracion del token
    to_encode.update({"exp" : expire}) # Actualiza la informacion para cargar la expiracion
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM) # Retorna la informacion y trae la llave secreta con el tipo de algoritmo