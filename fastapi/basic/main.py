from typing import Union as union 

from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

class Item(BaseModel): 
    name: str 
    price: float 
    is_available: bool 

@app.get("/")
def read_root(): 
    return {"tool": "fastapi"}

@app.get("/item/{item_id}")
def read_item(item_id: int, query: union[str, None] = None): 
    return {"item id": item_id, "Query": query}

@app.put("/items/{item_id}")
def update_item(item_id, item: Item): 
    return {"item name": item.name, "item id": item_id} 