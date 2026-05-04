from fastapi import APIRouter, HTTPException
from typing import List
import json
from pathlib import Path
from schemas.user import User, UserResponse

router = APIRouter()

# Load JSON file
DATA_FILE = Path("data/users.json")

def load_users():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return [User(**user) for user in data]

@router.get("/", response_model=List[UserResponse])
def get_users():
    users = load_users()
    return users

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    users = load_users()
    user = next((u for u in users if u.id == user_id), None)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user