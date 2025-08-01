from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI(
    title="FastAPI Demo Service",
    description="A sample FastAPI application ready for AWS deployment",
    version="0.1.0"
)

# Simple in-memory database
items_db = {}

class Item(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    price: float

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "FastAPI service is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    item_id = str(uuid.uuid4())
    item.id = item_id
    items_db[item_id] = item
    return item

@app.get("/items/", response_model=List[Item])
def read_items():
    return list(items_db.values())

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: str):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: str, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Update the item while preserving its ID
    item.id = item_id
    items_db[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    del items_db[item_id]
    return {"message": "Item deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
