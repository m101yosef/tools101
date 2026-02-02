from typing import Union as union 

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root(): 
    return {"tool": "fastapi"}

@app.get("/item/{item_id}")
def read_item(item_id: int, item_info: union[str, None] = None): 
    return {"item id": item_id, "info": item_info}
