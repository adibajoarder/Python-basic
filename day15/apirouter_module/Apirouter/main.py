from fastapi import FastAPI
from Routes import permissions
from Routes import users

app = FastAPI()

# Store users with IDs
users_list = []
permissions_list = []
user_id_counter = 0


@app.get("/")
def home():
    return {"welcome home": "This is the home page of the API"}


@app.get("/users")
def get_users(username: str, age: int, birth_year: int, gender: str):
    global user_id_counter
    user_id_counter += 1
    user_data = {"id": user_id_counter, "username": username, "age": age, "birth_year": birth_year, "gender": gender}
    users_list.append(user_data)
    return {"user": user_data}


@app.get("/permissions")
def get_permissions(password: str, email: str):
    global user_id_counter
    permission_data = {"id": user_id_counter, "password": password, "email": email}
    permissions_list.append(permission_data)
    return {"permission": permission_data}


@app.get("/search/{user_id}")
def search_id(user_id: int):
    user = next((u for u in users_list if u["id"] == user_id), None)
    permission = next((p for p in permissions_list if p["id"] == user_id), None)
    return {"user": user, "permission": permission}

app.include_router(users.router)
app.include_router(permissions.router)
