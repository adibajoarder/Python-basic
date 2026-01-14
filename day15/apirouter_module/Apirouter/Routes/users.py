from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users(username: str, age: int, birth_year: int, gender: str):
    return {"users": [{"username": username, "age": age, "birth_year": birth_year, "gender": gender}]}