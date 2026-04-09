# System Control API

# Crear base de datos en PostgreSQL
Crear la base de datos en psql o pgAdmin con el nombre "system_boutique"

## Variables de entorno
1. Seleccionar `.env.example` y renombrarlo a `.env`
2. Completar los valores con tus credenciales

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Git Bash

# Instalar dependencias
pip install -r requirements.txt


## Levantar backend 
# Correr el backend 
uvicorn app.main:app --reload 


## Migración de modelos a la base de datos 

# Inicializar alembic (solo la primera vez) 
alembic init migrations

# Crear migración
alembic revision --autogenerate -m "descripción del cambio"

# Ejecutar migración
alembic upgrade head


## Scripts iniciales 

# Insertar datos iniciales 
Después de migrar, ejecutar en orden los scripts del directorio /sql/
1. 01_roles.sql
2. 02_users.sql (No ejecutar este script sin realizar el paso del hash)

# Generar hash del password admin
ejecutar python hash.py
Copiar el resultado y reemplazar en 02_users.sql la password por el valor dado antes de ejecutarlo