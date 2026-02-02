from fastapi import FastAPI 

app = FastAPI() 

@app.get("/")
async def root(): 
    return {
        "message": "Hey you!"
        }

@app.get("/items")
async def display(): 
    return {
        "message": "All items are here!"
    }

@app.get("/items/{item_id}")
async def item_info(item_id: int): 
    return {
        "message": f"you selected item no.{item_id}"
    }

