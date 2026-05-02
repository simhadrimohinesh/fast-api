from fastapi import APIRouter
import json
router = APIRouter()

# load data from JSON
with open("data/users.json", "r") as f:
  users = json.load(f)
# query Parameter
@router.get("/search")
def do_search(username:str=None,email:str=None,role:str=None,city:str=None):
    output = users
    if username:
        output = [user for user in output if user['username'] == username]
    if email:
        output = [user for user in output if user['email'] == email]
    if role:
        output = [user for user in output if user['role'] == role]
    if city:
        output = [user for user in output if user['city'] == city]
    return output
# Path Parameter
@router.get("/{userid}")
def get_users(userid:int):
    output = {"message":"no user found"}
    for user in users:
        if user['id'] == userid:
            output = user       
    return output
