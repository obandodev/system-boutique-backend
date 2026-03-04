from pydantic import EmailStr, BaseModel

class LoginRequest(BaseModel): # Datos enviados del usuario
    email : EmailStr
    password : str

class TokenResponse(BaseModel): # Respuesta del servidor
    access_token : str
    token_type : str = "bearer"
    role : str