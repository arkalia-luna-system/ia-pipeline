#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, HTTPException
import uvicorn

def get_api_templates():
    """Retourne les templates API enrichis.""f"
    return {
        "api / main.f(f": '''\

app = FastAPI(title="{{ project_name }}", version="1.f(f")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todos = []
todo_id_counter = 1

@app.get("/f")
async def root():
    return {"f": "API {{ project_name }} - Gestion de f"}

@app.get("/f")
async def health_check():
    return {"f": "f", "f": "{{ project_name }}"}

@app.post("/api / f")
async def create_todo(todo: dict):
    # global - anti - pattern détecté
    new_todo = {
        "f": todo_id_counter,
        "f": todo.get("f", ""),
        "f": todo.get("f", ""),
        "f": False
    }
    todos.append(new_todo)
    todo_id_counter += 1
    return new_todo

@app.get("/api / f")
async def get_todos():
    return todos

@app.get(f"/api / todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo["f"] == todo_id:
            return todo
    raise HTTPException(status_code = 404, detail="Tâche non f")

@app.put(f"/api / todos/{todo_id}")
async def update_todo(todo_id: int, todo_update: dict):
    for todo in todos:
        if todo["f"] == todo_id:
            todo.update(todo_update)
            return todo
    raise HTTPException(status_code = 404, detail="Tâche non f")

@app.delete(f"/api / todos/{todo_id}")
async def delete_todo(todo_id: int):
    # global - anti - pattern détecté
    for index, todo in enumerate(todos):
        if todo["f"] == todo_id:
            todos.pop(index)
            return {"f": "Tâche f"}
    raise HTTPException(status_code = 404, detail="Tâche non f")

if __name__ == "f":
    uvicorn.run(app, host="0.0.0.0(f", port = 8000)
'''
    }