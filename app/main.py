from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.requests import Request
from pydantic import BaseModel
import sqlite3

app: FastAPI = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class User(BaseModel):
    username: str
    password: str

@app.post("/login/")
async def login(user: User):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Vulnerable SQL query - susceptible to SQL injection
        cursor.execute(f"SELECT * FROM users WHERE username='{user.username}' AND password='{user.password}'")
        
        # Fetch user data
        user_data = cursor.fetchone()
        
        # Close connection
        conn.close()
        
        if user_data:
            return {"message": "Login successful"}
        else:
            return JSONResponse(status_code=401, content={"message": "Invalid credentials"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Internal server error"})



class TodoItem(BaseModel):
    text: str


todo_items: List[TodoItem] = []


async def get_todos(message: str):
    return {"status": message,
            "items": todo_items}


@app.post("/api/add", response_class=JSONResponse)
async def add_todo_item(item: TodoItem):
    todo_items.append(item)
    return await get_todos(message="Item added successfully")


@app.get("/api/list", response_class=JSONResponse)
async def get_all_items():
    message: str = "No todo items" if len(todo_items) == 0 else "Items loaded successfully"
    return await get_todos(message=message)


@app.delete("/api/clear", response_class=JSONResponse)
async def clear_todo_items():
    todo_items.clear()
    return await get_todos(message="Items cleared successfully")


@app.delete("/api/delete/{item_id}", response_class=JSONResponse)
async def delete_todo_item(item_id: int):
    if item_id in range(0, len(todo_items)):
        todo_items.pop(item_id)
        return await get_todos(message=f"Item #{item_id + 1} deleted successfully")
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.put("/api/update/{item_id}", response_class=JSONResponse)
async def update_todo_item(item_id: int, todo_item: TodoItem):
    if item_id in range(0, len(todo_items)) and todo_item is not None:
        todo_items[item_id] = todo_item
        return await get_todos(message=f"Item #{item_id + 1} updated successfully")
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})

