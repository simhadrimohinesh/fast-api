from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_admin: bool
    created_at: datetime


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime