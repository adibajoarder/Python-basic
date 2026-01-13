from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

# custom validation
class User(BaseModel):
    name: str
    price: float
    age: int = Field(..., gt=18, le=100, description="Age must be greater than 18 and less than or equal to 100")
    
    @field_validator('name')
    @classmethod
    def name_must_be_not_empty(cls, value):
        if not value:
            raise ValueError('Name must not be empty')
        return value

# response
@app.post("/users/", response_model=User)
async def create_user(user: User):
    u={"name":user.name,"price":user.price,"age":user.age}
    return u