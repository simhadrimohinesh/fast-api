from fastapi import FastAPI,HTTPException
from uuid import uuid4
from schemas.user import CreateUser
import json

app = FastAPI()

FILE_PATH = './data/users.json'

@app.post("/users",status_code = 201)
def create_users(user:CreateUser):
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
