from dotenv import load_dotenv # Función que carga las variables del archivo .env en memoria
import os 
from pathlib import Path

load_dotenv() # Se invoca para leer el .env
DATABASE_URL = os.getenv("DATABASE_URL") # Obtiene el valor de la variable de entorno "DATABASE_URL" definida en el .env