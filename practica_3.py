from typing import Dict, Tuple
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    id: int = Field(..., description="id del producto")
    name: str = Field(..., description="nombre del producto")
    emails: list[str]
    
db: Dict[int, list] = {}

@app.get("/")
async def welcome():
    return {"message":"Computacion en la nube prueba"}

@app.get("/status/")
def status():
    return {"message": "Pong"}

@app.get("/directories/")
def listado_objetos():
    return db

@app.post("/directories/")
def set_product(user: User) -> User:
    print("Ingrese el nombre")
    new_name=input()
    print("Ingrese el email")
    new_email=input()
    user=new_name,new_email
    db.append(user)
    return user

@app.get("/directories/{id}")
def find_by_id(id: int)-> User | None:
    user_tuple = db.get(id)
    
    if user_tuple:       
        return  User(id=id, name=user_tuple[id], emails=user_tuple[id])
    return None

@app.put("/directories/{id}")
def edit_by_id(id: int, user:User)-> User | None:
    print("Ingrese el nuevo nombre")
    new_name=input()
    print("Ingrese el nuevo email")
    new_email=input()
    user=new_name,new_email
    user_tuple = db.get(id)
    
    if user_tuple:
        db[user.id] = user
        return user
    return None

@app.patch("/directories/{id}")
def edit_temp_by_id(id: int, user:User)-> User | None:
    print("Ingrese el nuevo nombre")
    new_name=input()
    print("Ingrese el nuevo email")
    new_email=input()
    user=new_name,new_email
    user_tuple = db.get(id)
    
    if user_tuple:
        db[user.id] = user
        return user
    return None

@app.delete("/directories/{id}")
def delete_by_id(id: int):
    del db[id]
    return None

