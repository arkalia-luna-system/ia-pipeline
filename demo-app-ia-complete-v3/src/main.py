#!/usr/bin/env python3
"""
web - API REST avec FastAPI
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="web", version="1.0.0")

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

# Base de données simulée
items_db = []

@app.get("/")
async def root():
    return {"message": "Bienvenue sur web API"}

@app.get("/items/", response_model=List[Item])
async def get_items():
    return items_db

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    item.id = len(items_db) + 1
    items_db.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    if item_id > len(items_db):
        raise HTTPException(status_code=404, detail="Item non trouvé")
    return items_db[item_id - 1]

def main():
    """Point d'entrée principal"""
    uvicorn.run(app, host="0.0.0.0", port=8000)

def run():
    """Exécute l'application"""
    main()

if __name__ == "__main__":
    main()
