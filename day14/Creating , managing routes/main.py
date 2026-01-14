from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# Request model for creating Item
class ItemRequest(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Price must be greater than 0")

# Response model for Item
class Item(BaseModel):
    id: int
    name: str
    price: float

# Response model for delete
class DeleteResponse(BaseModel):
    message: str
    status: str

# Response model for get all items
class ItemListResponse(BaseModel):
    items: list[Item]
    total: int

# In-memory storage for items
items_list: list[Item] = []
item_id_counter = 0

@app.post("/items/", response_model=Item)
def create_items(item: ItemRequest):
    global item_id_counter
    item_id_counter += 1
    new_item = Item(id=item_id_counter, name=item.name, price=item.price)
    items_list.append(new_item)
    return new_item

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_list:
        if item.id == item_id:
            return item
    return {"message": f"Item with ID {item_id} not found", "status": "not_found"}

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemRequest):
    for existing_item in items_list:
        if existing_item.id == item_id:
            existing_item.name = item.name
            existing_item.price = item.price
            return existing_item
    return {"message": f"Item with ID {item_id} not found", "status": "not_found"}

@app.delete("/items/{item_id}", response_model=DeleteResponse)
def delete_item(item_id: int):
    global items_list
    items_list = [item for item in items_list if item.id != item_id]
    return {"message": f"Item with ID {item_id} deleted successfully" , "status": "deleted"}

@app.get("/items/", response_model=ItemListResponse)
def get_all_items():
    return {"items": items_list, "total": len(items_list)}
