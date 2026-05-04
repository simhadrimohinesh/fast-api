from fastapi import FastAPI,HTTPException
from uuid import uuid4
from schemas.user import CreateUser,UpdateUser
import json

app = FastAPI()

FILE_PATH = './data/users.json'

@app.delete("/users/{id}",status_code = 204)
def delete_user(id:str):
    users = {}
    with open(FILE_PATH,'r') as f:
        users = json.load(f) 
    users.pop(id)
    with open(FILE_PATH, 'w') as f:
        json.dump(users, f, indent=4)
    return # return None

@app.get("/users/{id}")
def get_user(id:str):
    users = {}
    with open(FILE_PATH,'r') as f:
        users = json.load(f) 
    return users[id]

@app.post("/users",status_code = 201)
def create_user(user:CreateUser):
    users = {}

    with open(FILE_PATH,'r') as f:
        users = json.load(f)

    user_id = str(uuid4())
    user_data = user.model_dump()

    for val in users.values():
        if val['email'] == user_data['email']:
            raise HTTPException(status_code=409, detail="Email already exists")
        
    users[user_id] = user_data
    with open(FILE_PATH, 'w') as f:
        json.dump(users, f, indent=4)
    return {"message":"user created successfully with id:"+user_id}

@app.patch("/users/{id}")
def update_user(user:UpdateUser,id:str):
    users = {}
    with open(FILE_PATH,'r') as f:
        users = json.load(f) 
    user_data = user.model_dump(exclude_unset=True)
    if not user_data:
        raise HTTPException(status_code=400, detail="No data provided for update")
    users[id].update(user_data)
    with open(FILE_PATH, 'w') as f:
        json.dump(users, f, indent=4)
    return {"message":"user updated successfully with id:"+id}
