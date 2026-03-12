from fastapi import HTTPException, status

def validate_role_not_exists(existing_role, name_rol: str):
    if existing_role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El rol '{name_rol}' ya existe"
        )

def validate_role_exists(existing_role, name_rol: str):
    if not existing_role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El rol '{name_rol}' no existe"
        )

def validate_role_access(current_user: dict, name_rol: str):
    if current_user.get("role") != "Admin":
        if current_user.get("role") != name_rol:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos para ver este rol"
            )