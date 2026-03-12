from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.shared.security import SECRET_KEY, ALGORITHM

security = HTTPBearer() # Le dice a FastAPI que espera un token en el header de la request

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)): # FastAPI extrae el token del header y lo pasa a la funcion
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM]) # Decodifica el token JWT y lo convierte de vuelta al diccionario original
        return payload  # Retorna ese diccionario para que el endpoint sepa quién está haciendo la request.
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalido o expirado"
        ) # Si el token no existe o fue manipulado lanza el error

def require_role(role :str):
    def role_checker(current_user: dict = Depends(get_current_user)): # La funcion va depender el rol que se traiga en el payload
        if current_user.get("role") != role: # Si el rol del payload no esta en el endpoint
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Acceso denegado, no tienes los permisos suficientes"
            ) # Retorna un 403
        return current_user # Retornarmos el dict
    return role_checker # Retornamos la funcion