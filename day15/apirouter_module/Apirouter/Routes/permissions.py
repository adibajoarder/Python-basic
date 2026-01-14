from fastapi import APIRouter

router = APIRouter()

@router.get("/permissions")
def get_permissions(password: str, email: str):
    return {"permissions": [{"password": password, "email": email}]}