from pydantic import EmailStr, BaseModel

class LoginRequest(BaseModel): # Datos enviados para el inicio de sesion
    email : EmailStr
    password : str

class TokenResponse(BaseModel): # Respuesta inicio-sesion
    access_token : str
    token_type : str = "bearer"
    role : str